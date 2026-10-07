"""Imprime las reglas de tipos.py como tabla JS para src/services/alternativas.js (app).
Así la app clasifica la ficha de un producto con las MISMAS reglas que el catálogo usa
para repartir alternativas.json. Uso: python3 exporta_js.py > /tmp/tipos.js y pegar
entre los marcadores 'TIPOS (generado' y 'fin TIPOS' del servicio."""
import json
from tipos import TIPOS, MARCA_TIPO
def js(rx): return '/' + rx.replace('/', '\\/') + '/' if rx else 'null'
print('// TIPOS (generado con nura-catalogo/herramientas/alternativas/exporta_js.py; no editar a mano)')
print('const TIPOS_REGLAS = {')
for cat, reglas in TIPOS.items():
    print(f'  {json.dumps(cat, ensure_ascii=False)}: [')
    for key, _, casa, excluye in reglas:
        print(f'    [{json.dumps(key)}, {js(casa)}, {js(excluye)}],')
    print('  ],')
print('};')
print('const MARCA_TIPO = ' + json.dumps({k: v[0] for k, v in MARCA_TIPO.items()}) + ';')
print('// fin TIPOS')
