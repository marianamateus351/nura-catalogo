"""Genera alternativas.json (contrato con la app, CURACION.md "ALTERNATIVAS LIMPIAS").
Entra un producto solo si cumple LAS TRES condiciones:
  1 y 3: está en limpios.json (cero disruptores y cero "otros riesgos"; Cuidado personal u Hogar) y tiene tipo;
  2: tiene en amazon_verificados.json una entrada con enlace directo de Amazon.es y el vendedor visto, y ese
     vendedor es la tienda oficial de la marca (lo decide quien verifica: campo "oficial": true).
Sin entradas verificadas NO se escribe alternativas.json (la app enseña "Estamos preparando las primeras opciones").
Uso: node limpios.mjs > limpios.json && python3 fechas.py && python3 genera.py <version>"""
import json, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from tipos import TIPOS, CATEGORIAS, tipo_de
A = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(A, '../..'))
limpios = json.load(open(f'{A}/limpios.json'))['productos']
fechas = json.load(open(f'{A}/fechas.json'))
ver = json.load(open(f'{A}/amazon_verificados.json')) if os.path.exists(f'{A}/amazon_verificados.json') else {}
fotos = set(os.listdir(f'{R}/fotos')) if os.path.isdir(f'{R}/fotos') else set()
FOTO_URL = 'https://raw.githubusercontent.com/marianamateus351/nura-catalogo/main/fotos/'
def ddmmaaaa(iso): y, m, d = iso.split('-'); return f'{d}-{m}-{y}'
por = {}
for p in limpios:
    k, _ = tipo_de(p['nombre'], p['categoria'])
    if not k: continue
    for bc in p['barcodes']:
        v = ver.get(bc)
        if not (v and v.get('oficial') and v.get('amazon') and v.get('vendedor')): continue
        e = {'nombre': p['nombre'], 'marca': p['marca'], 'formato': v.get('formato', ''), 'barcode': bc}
        if f'{bc}.jpg' in fotos: e['imagen'] = FOTO_URL + f'{bc}.jpg'
        if bc in fechas: e['fechaLista'] = ddmmaaaa(fechas[bc])
        e['amazon'] = v['amazon']; e['vendedor'] = v['vendedor']
        por.setdefault((p['categoria'], k), []).append(e)
        break                                     # un enlace por producto (el primer código verificado)
if not por:
    print('Ningún producto verificado en Amazon.es: no se escribe alternativas.json'); sys.exit(0)
version = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
out = {'version': version, 'categorias': []}
for ckey, cnom in CATEGORIAS:
    tipos = []
    for key, label, _, _ in TIPOS[cnom]:
        prods = sorted(por.get((cnom, key), []), key=lambda e: (e['marca'].lower(), e['nombre'].lower()))
        if prods: tipos.append({'key': key, 'nombre': label, 'productos': prods})
    if tipos: out['categorias'].append({'key': ckey, 'nombre': cnom, 'tipos': tipos})
json.dump(out, open(f'{R}/alternativas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for c in out['categorias']:
    for t in c['tipos']: print(f"{c['nombre']} · {t['nombre']}: {len(t['productos'])}")
