"""Pasa a amazon_verificados.json lo revisado en la página "Tiendas oficiales en Amazon"
(artifact https://claude.ai/artifact/Viv5kabTFc4yfvbbgG4xN8, colección `productos` de su base de datos).
Uso: exportar la colección con ArtifactData (list, out_dir=<dir>) y
     python3 desde_revision.py <dir>/productos
Solo cuentan las fichas (/dp/) con quien vende = marca, Amazon o farmacia/vendedor de confianza."""
import json, os, re, sys
A = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1]
ETQ = {'amazon': 'Amazon', 'farmacia': 'Farmacia o vendedor de confianza'}
marcas = {}
try:
    for m in json.load(open(os.path.join(A, '../../catalogo.json')))['marcas']: marcas[m['key']] = m['nombre']
except Exception: pass
out = {}
for f in sorted(os.listdir(src)):
    if not f.endswith('.json'): continue
    d = json.load(open(os.path.join(src, f)))
    d = d.get('data', d)
    code = f[:-5]
    url = d.get('amazon') or ''
    if not re.search(r'/(?:dp|gp/product)/[A-Z0-9]{10}', url): continue
    quien = d.get('quien') or ('marca' if d.get('oficial') else '')
    if quien not in ('marca', 'amazon', 'farmacia'): continue
    nombre = (d.get('vendedorNombre') or '').strip()
    vend = nombre or (marcas.get(d.get('marca'), d.get('marca', '')) if quien == 'marca' else ETQ[quien])
    out[code] = {'amazon': url, 'vendedor': vend, 'quien': quien, 'fiable': True, 'visto': (d.get('actualizado') or '')[:10]}
json.dump(out, open(os.path.join(A, 'amazon_verificados.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'fichas comprobadas')
