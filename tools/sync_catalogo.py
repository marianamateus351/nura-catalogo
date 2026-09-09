#!/usr/bin/env python3
"""Sync catalogo.json (nura-catalogo) -> src/data/catalogoInci.js (nura-firebase).

catalogo.json is the source of truth. The JS file keeps its comments/header;
only the `productos: [...]` array of each brand block is regenerated.
"""
import json, re, sys, datetime

# catalogo.json se busca en la raíz de ESTE repo (el padre de tools/).
# catalogoInci.js se busca en el repo nura-firebase, por defecto al lado de este
# repo (../nura-firebase). Se puede cambiar con la variable de entorno
# NURA_FIREBASE o pasando la ruta:  python3 tools/sync_catalogo.py sync <ruta.js>
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(_ROOT, "catalogo.json")
_FB = os.environ.get("NURA_FIREBASE") or os.path.join(os.path.dirname(_ROOT), "nura-firebase")
JS_PATH = os.path.join(_FB, "src", "data", "catalogoInci.js")

KEY_ORDER = ["nombre", "include", "exclude", "barcodes", "foto", "inci"]


def js_str(s):
    return json.dumps(s, ensure_ascii=False)


def product_line(p):
    parts = []
    for k in KEY_ORDER:
        if k not in p:
            continue
        v = p[k]
        if k in ("include", "exclude"):
            parts.append("%s: [%s]" % (k, ", ".join(js_str(x) for x in v)))
        elif k == "barcodes":
            parts.append("barcodes: [%s]" % ", ".join(js_str(x) for x in v))
        else:
            parts.append("%s: %s" % (k, js_str(v)))
    extra = [k for k in p if k not in KEY_ORDER]
    if extra:
        raise SystemExit("clave desconocida en producto %r: %s" % (p.get("nombre"), extra))
    return "        { " + ", ".join(parts) + " },"


def load():
    return json.load(open(JSON_PATH, encoding="utf-8"))


def save_json(data):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def sync_js(data):
    src = open(JS_PATH, encoding="utf-8").read()
    # bundled version string
    src = re.sub(r'version: "bundled-[^"]*"',
                 'version: "bundled-%s"' % data["version"], src, count=1)
    for brand in data["marcas"]:
        key = brand["key"]
        # find the brand block: from `key: "<key>",` to the closing `      ],`
        m = re.search(r'(      key: "%s",\n(?:.*?\n)*?      productos: )(\[\]|\[\n(?:.*?\n)*?      \])(,\n)'
                      % re.escape(key), src)
        if not m:
            raise SystemExit("no encuentro el bloque de marca %r en el JS" % key)
        prods = brand.get("productos", [])
        if not prods:
            body = "[]"
        else:
            body = "[\n" + "\n".join(product_line(p) for p in prods) + "\n      ]"
        src = src[:m.start(2)] + body + src[m.end(2):]
    with open(JS_PATH, "w", encoding="utf-8") as f:
        f.write(src)


def parse_js_products():
    """Rough parse of the JS file to compare parity."""
    src = open(JS_PATH, encoding="utf-8").read()
    out = {}
    for bm in re.finditer(r'      key: "([a-z]+)",\n(?:.*?\n)*?      productos: (\[\]|\[\n((?:.*?\n)*?)      \]),\n', src):
        key = bm.group(1)
        body = bm.group(3) or ""
        prods = []
        for line in body.splitlines():
            line = line.strip().rstrip(",")
            if not line:
                continue
            nm = re.search(r'nombre: "((?:[^"\\]|\\.)*)"', line)
            bc = re.search(r'barcodes: \[([^\]]*)\]', line)
            inci = re.search(r'inci: "((?:[^"\\]|\\.)*)"', line)
            prods.append({
                "nombre": json.loads('"%s"' % nm.group(1)) if nm else None,
                "barcodes": re.findall(r'"(\d+)"', bc.group(1)) if bc else [],
                "inci": json.loads('"%s"' % inci.group(1)) if inci else "",
            })
        out[key] = prods
    return out


def check_parity():
    data = load()
    js = parse_js_products()
    ok = True
    for brand in data["marcas"]:
        k = brand["key"]
        jp = js.get(k)
        if jp is None:
            print("FALTA marca %s en JS" % k); ok = False; continue
        jsonp = brand["productos"]
        if len(jp) != len(jsonp):
            print("%s: %d productos en JSON vs %d en JS" % (k, len(jsonp), len(jp))); ok = False
        for a, b in zip(jsonp, jp):
            if a["nombre"] != b["nombre"]:
                print("%s: nombre difiere %r / %r" % (k, a["nombre"], b["nombre"])); ok = False
            if a.get("barcodes", []) != b["barcodes"]:
                print("%s / %s: barcodes difieren %s / %s" % (k, a["nombre"], a.get("barcodes"), b["barcodes"])); ok = False
            if a.get("inci", "") != b["inci"]:
                print("%s / %s: INCI difiere" % (k, a["nombre"])); ok = False
    print("PARIDAD OK" if ok else "PARIDAD ROTA")
    return ok


def validate():
    """Structural checks over catalogo.json."""
    data = load()
    seen = {}
    bad = 0
    for brand in data["marcas"]:
        for p in brand["productos"]:
            for k in ("nombre", "include", "exclude", "inci"):
                if k not in p:
                    print("!! %s/%s falta clave %s" % (brand["key"], p.get("nombre"), k)); bad += 1
            for c in p.get("barcodes", []):
                if not re.fullmatch(r"\d{8}|\d{12,14}", c):
                    print("!! código con formato raro: %s (%s)" % (c, p["nombre"])); bad += 1
                if c.startswith(("0", "789", "869", "750")):
                    print("!! código de región excluida: %s (%s)" % (c, p["nombre"])); bad += 1
                if c in seen:
                    print("!! código duplicado %s: %s / %s" % (c, seen[c], brand["key"] + "/" + p["nombre"])); bad += 1
                seen[c] = brand["key"] + "/" + p["nombre"]
            inci = p.get("inci", "")
            for suspect in ("y otros", "...", "…", "etc"):
                if suspect in inci.lower():
                    print("!! INCI sospechoso (%s) en %s" % (suspect, p["nombre"])); bad += 1
    tot = sum(len(b["productos"]) for b in data["marcas"])
    print("productos: %d · códigos: %d · problemas: %d" % (tot, len(seen), bad))
    return bad == 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if len(sys.argv) > 2:
        JS_PATH = sys.argv[2]
    for _p, _q in ((JSON_PATH, "catalogo.json"), (JS_PATH, "catalogoInci.js")):
        if not os.path.exists(_p):
            raise SystemExit(
                "no encuentro %s en %s\n"
                "Indica la ruta del repo nura-firebase con NURA_FIREBASE=<ruta> "
                "o pasa el .js como segundo argumento." % (_q, _p))
    if cmd == "sync":
        d = load(); sync_js(d); print("JS regenerado desde JSON")
    elif cmd == "check":
        check_parity()
    elif cmd == "validate":
        validate()
    elif cmd == "all":
        d = load(); sync_js(d); check_parity(); validate()
