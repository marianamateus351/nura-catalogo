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
# Fotos de Open Beauty Facts por código (pedido de Mariana, 2026-10-14): {código: url de la foto frontal}.
# Se enlazan (no se copian) y llevan la fuente, porque OBF las publica con licencia CC BY-SA. Manda la foto
# propia de fotos/ si la hay. Nunca fotos copiadas de Amazon (CLAUDE.md de la app).
fotos_obf = json.load(open(f'{A}/fotos_obf.json')) if os.path.exists(f'{A}/fotos_obf.json') else {}
# Subtipo, línea y tono explícitos (contrato "SUBTIPOS Y LÍNEAS DE TONOS", 2026-10-14): {código: {subtipo, linea, tono}}.
# Mandan sobre lo que la app deduce del nombre. Se aplican por cualquiera de los códigos del producto.
lineas = json.load(open(f'{A}/lineas.json')) if os.path.exists(f'{A}/lineas.json') else {}
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
                       r'phosphoric acid|nitric acid|sulfamic acid|sulphamic acid|sulfamidic acid|sulphamidic acid|amidosulfonic acid|sulfamico|oxalic acid|hidroxido|clorhidrico|sulfurico|fosforico|oxalico', re.I)
TIPOS_FUERA = {'desatascador'}
# Oxidantes de coloración (agua oxigenada, reveladores): no son una alternativa a nada y el tipo por nombre los
# confundía con sérums o cremas ("Oxidante en crema 10 vol", Valquer, 2026-10-12).
# Ambientadores y velas: solo con una composición de verdad, que nombra la base (cera, agua, alcohol, disolvente,
# propelente…). Sin ella, la "lista" es la frase CONTIENE del aviso de peligro (alérgenos del perfume), no la composición:
# así entró la vela Precious Amber de Rituals, con un solo ingrediente (Mariana, 2026-10-25).
BASE_AMBIENTADOR = re.compile(r'wax|cera|paraffin|parafina|aqua|water|agua|alcohol|glycol|isopar|hydrocarbon|solvent|propan|butan|'
                              r'nitrogen|nitr[oó]geno|ethanol|polymer|carrageenan|stearic|ester|alkane|propellant|propelente', re.I)
NOMBRE_FUERA = re.compile(r'oxidante|agua oxigenada|revelador|developer|peróxido|peroxido', re.I)
def peligroso(b):
    inci = INCI.get(b, '')
    return bool(FUERA.search(inci)) or any(CORROSIVO.search(x) for x in inci.split(',')[:2])
# Limpios para el detector pero con dudas que decide Mariana: fuera de Alternativas hasta entonces. (El Serum capilar
# Nature de Tahe estuvo aquí hasta la decisión X, 2026-10-12: ahora lo marca el detector, ficha 215.)
# Absorbentes de Saugella y Organyc: estuvieron aquí el 2026-10-24 hasta la propuesta D (aprobada el mismo día), que les
# pone ya el aviso de microplásticos y perfume. Vacío.
PENDIENTE_DECISION = set()
# Limpios SOLO con el detector nuevo: hasta que salga el build que lo trae, la app instalada aún les pondría un aviso,
# así que no se enseñan todavía como alternativa. Quitar el código de aquí cuando el build esté publicado.
# Códigos retenidos hasta que la app publicada lleve el arreglo del detector que los deja limpios.
# Vacío desde el 2026-10-22: el build 110 (0.2.54) ya lleva la nota alemana de perfume natural y la ficha 193.
HASTA_BUILD = set()
por = {}
for p in limpios:
    if any(peligroso(b) for b in p['barcodes']): continue
    if any(b in HASTA_BUILD for b in p['barcodes']): continue
    if any(b in PENDIENTE_DECISION for b in p['barcodes']): continue
    if NOMBRE_FUERA.search(p['nombre']): continue
    if tipo_de(p['nombre'], p['categoria'], p.get('marcaKey'))[0] == 'ambientador' and not any(BASE_AMBIENTADOR.search(INCI.get(b, '')) for b in p['barcodes']): continue
    if tipo_de(p['nombre'], p['categoria'], p.get('marcaKey'))[0] in TIPOS_FUERA: continue
    k, _ = tipo_de(p['nombre'], p['categoria'], p.get('marcaKey'))
    if not k: continue
    bc = p['barcodes'][0]
    e = {'nombre': p['nombre'], 'marca': p['marca'], 'barcode': bc}
    if f'{bc}.jpg' in fotos: e['imagen'] = FOTO_URL + f'{bc}.jpg'
    else:
        obf = next((fotos_obf[c] for c in p['barcodes'] if c in fotos_obf), None)
        if obf: e['imagen'] = obf; e['fotoFuente'] = 'Open Beauty Facts (CC BY-SA)'
    lin = next((lineas[c] for c in p['barcodes'] if c in lineas), None)
    if lin: e.update({k: v for k, v in lin.items() if k in ('subtipo', 'linea', 'tono') and v})
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
