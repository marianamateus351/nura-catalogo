"""Copia ESM de src/services/products.js de la app (sin Firebase) para que limpios.mjs use el MISMO detector.
Uso: python3 herramientas/alternativas/gen_products.py [ruta del repo de la app]"""
import os, sys
app = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '../../../nura-firebase')
app = os.path.abspath(app)
s = open(f'{app}/src/services/products.js', encoding='utf-8').read()
s = s.replace('import { getDocs, collection, setDoc, doc, getDoc, deleteDoc, increment, arrayUnion, query, where } from "firebase/firestore";',
              'const getDocs=0,collection=0,setDoc=0,doc=0,getDoc=0,deleteDoc=0,increment=0,arrayUnion=0,query=0,where=0;')
s = s.replace('import { db, currentUserId, auth } from "./firebase";', 'const db=0,currentUserId=0,auth=0;')
for mod in ('ingredients', 'inci'):
    s = s.replace(f'from "../data/{mod}"', f'from "{app}/src/data/{mod}.js"')
s = s.replace('from "../theme/tokens"', f'from "{app}/src/theme/tokens.js"')
s = s.replace('require("../data/catalogoInci")', '__CAT')
s = f'import * as __CAT from "{app}/src/data/catalogoInci.js";\n' + s
assert '"../' not in s and '"./' not in s, 'products.js importa algo nuevo: actualizar gen_products.py'
open(os.path.join(os.path.dirname(__file__), 'products.mjs'), 'w', encoding='utf-8').write(s)
print('products.mjs generado desde', app)
