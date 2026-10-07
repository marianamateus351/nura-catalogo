"""Genera alternativas.json (contrato con la app, CURACION.md "ALTERNATIVAS LIMPIAS").
Entran TODOS los productos de limpios.json con tipo (cero disruptores y cero "otros riesgos";
Cuidado personal u Hogar). Amazon NO es condición de entrada.
`amazon` sale de amazon_auto.json (ficha encontrada por Claude con el buscador, decisión de Mariana del
2026-10-07) o, si alguien la revisó a mano, de amazon_verificados.json, que manda. Los campos `amazon` y
`vendedor` de amazon_verificados.json se ponen si trae, para ese código,
la FICHA concreta del producto (amazon.es/dp/<ASIN>, de la tienda de la marca; nunca una búsqueda)
y la persona que la revisó marcó que la venden la marca, Amazon o una farmacia o vendedor de
confianza ("fiable": true). Criterio de Mariana del 2026-10-07.
Uso: node limpios.mjs > limpios.json && python3 fechas.py && python3 genera.py <versión>"""
import json, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from tipos import TIPOS, CATEGORIAS, tipo_de
A = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(A, '../..'))
limpios = json.load(open(f'{A}/limpios.json'))['productos']
fechas = json.load(open(f'{A}/fechas.json'))
ver = json.load(open(f'{A}/amazon_verificados.json')) if os.path.exists(f'{A}/amazon_verificados.json') else {}
# Fichas encontradas por Claude con el buscador (decisión de Mariana del 2026-10-07: enlaces automáticos,
# sin revisión a mano). {código: {"url": "https://www.amazon.es/dp/<ASIN>", "titulo": "…"}}
auto = json.load(open(f'{A}/amazon_auto.json')) if os.path.exists(f'{A}/amazon_auto.json') else {}
fotos = set(os.listdir(f'{R}/fotos')) if os.path.isdir(f'{R}/fotos') else set()
FOTO_URL = 'https://raw.githubusercontent.com/marianamateus351/nura-catalogo/main/fotos/'
import re
def enlace_limpio(u):
    # Enlace directo y sin etiqueta: la etiqueta de afiliada (marianamateus-21) la pone la app.
    m = re.search(r'/(?:dp|gp/product)/([A-Z0-9]{10})', u or '')
    return f'https://www.amazon.es/dp/{m.group(1)}' if m else None
def ddmmaaaa(iso): y, m, d = iso.split('-'); return f'{d}-{m}-{y}'
# Fuera por decisión de Mariana (2026-10-07): la lejía (hipoclorito sódico) no se enseña como alternativa
# limpia aunque el detector no la marque. Sale todo lo que la lleve en su lista: lejías y desatascadores con lejía.
cat = json.load(open(f'{R}/catalogo.json'))
INCI = {b: q.get('inci', '') for m in cat['marcas'] for q in m['productos'] for b in q.get('barcodes', [])}
FUERA = re.compile(r'hypochlorite|hipoclorito', re.I)
# Fuera también lo corrosivo (Mariana, 2026-10-07: "los desatascadores tienen productos peligrosos? si sí,
# sácalos"): todos los desatascadores, y cualquier producto con un ácido o una base fuerte entre sus dos
# primeros ingredientes, que es cuando va a concentración de producto corrosivo (sosa del limpiahornos,
# salfumán del desincrustante, fosfórico del limpiador de paellas, ácido oxálico de la sal de acedera, que es tóxico). La sosa o la potasa al final de la
# lista, para ajustar el pH o saponificar el jabón, no cuenta.
CORROSIVO = re.compile(r'sodium hydroxide|potassium hydroxide|hydrochloric acid|sulfuric acid|sulphuric acid|'
                       r'phosphoric acid|nitric acid|sulfamic acid|oxalic acid|hidroxido|clorhidrico|sulfurico|fosforico|oxalico', re.I)
TIPOS_FUERA = {'desatascador'}
def peligroso(b):
    inci = INCI.get(b, '')
    return bool(FUERA.search(inci)) or any(CORROSIVO.search(x) for x in inci.split(',')[:2])
por = {}
for p in limpios:
    if any(peligroso(b) for b in p['barcodes']): continue
    if tipo_de(p['nombre'], p['categoria'], p.get('marcaKey'))[0] in TIPOS_FUERA: continue
    k, _ = tipo_de(p['nombre'], p['categoria'], p.get('marcaKey'))
    if not k: continue
    bc = p['barcodes'][0]
    e = {'nombre': p['nombre'], 'marca': p['marca'], 'barcode': bc}
    if f'{bc}.jpg' in fotos: e['imagen'] = FOTO_URL + f'{bc}.jpg'
    if bc in fechas: e['fechaLista'] = ddmmaaaa(fechas[bc])
    for c in p['barcodes']:                      # el primer código con ficha comprobada
        v = ver.get(c) or {}
        if (v.get('fiable') or v.get('oficial')) and enlace_limpio(v.get('amazon')) and v.get('vendedor'):
            e['barcode'] = c
            if v.get('formato'): e['formato'] = v['formato']
            e['amazon'] = enlace_limpio(v['amazon']); e['vendedor'] = v['vendedor']
            break
    else:
        for c in p['barcodes']:                  # si nadie la ha revisado, la ficha automática
            a = auto.get(c) or {}
            if enlace_limpio(a.get('url')):
                e['barcode'] = c; e['amazon'] = enlace_limpio(a['url'])
                break
    por.setdefault((p['categoria'], k), []).append(e)
version = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
out = {'version': version, 'categorias': []}
for ckey, cnom in CATEGORIAS:
    tipos = []
    # Orden de presentación: el de demanda que dio Mariana; los demás tipos detrás.
    ORDEN = ['desodorante', 'limpiador-facial', 'crema-facial', 'serum', 'protector-solar', 'champu', 'gel-ducha',
             'pasta-dientes', 'higiene-intima', 'acondicionador', 'crema-corporal', 'base-maquillaje', 'labial', 'lubricante',
             'contorno-ojos', 'tonico', 'exfoliante', 'mascarilla-facial', 'emoliente', 'granos', 'crema-manos',
             'capilar', 'autobronceador', 'mascara-pestanas', 'ojos-cejas', 'colorete', 'esmalte',
             'detergente', 'suavizante', 'lavavajillas', 'multiusos', 'limpiador-cocina-bano', 'aditivo-colada', 'basicos-limpieza', 'lejia', 'desatascador',
             'ambientador']
    for key, label, _, _ in sorted(TIPOS[cnom], key=lambda t: ORDEN.index(t[0]) if t[0] in ORDEN else 99):
        prods = sorted(por.get((cnom, key), []), key=lambda e: (e['marca'].lower(), e['nombre'].lower()))
        if prods: tipos.append({'key': key, 'nombre': label, 'productos': prods})
    if tipos: out['categorias'].append({'key': ckey, 'nombre': cnom, 'tipos': tipos})
json.dump(out, open(f'{R}/alternativas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for c in out['categorias']:
    for t in c['tipos']: print(f"{c['nombre']} · {t['nombre']}: {len(t['productos'])} ({sum(1 for p in t['productos'] if p.get('amazon'))} con enlace)")
