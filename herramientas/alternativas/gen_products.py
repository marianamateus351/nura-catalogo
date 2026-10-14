"""Copia ESM de src/services/products.js de la app (sin Firebase) para que limpios.mjs use el MISMO detector.
Uso: python3 herramientas/alternativas/gen_products.py [ruta del repo de la app]"""
import os, sys
app = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '../../../nura-firebase')
app = os.path.abspath(app)
s = open(f'{app}/src/services/products.js', encoding='utf-8').read()
import re
# Cualquier import de firebase/firestore (la lista de funciones cambia con la app) → constantes vacías.
s = re.sub(r'import \{([^}]*)\} from "firebase/firestore";', lambda m: 'const ' + ','.join(f'{x.strip()}=0' for x in m.group(1).split(',') if x.strip()) + ';', s)
s = s.replace('import { db, currentUserId, auth } from "./firebase";', 'const db=0,currentUserId=0,auth=0;')
for mod in ('ingredients', 'inci'):
    s = s.replace(f'from "../data/{mod}"', f'from "{app}/src/data/{mod}.js"')
s = s.replace('from "../theme/tokens"', f'from "{app}/src/theme/tokens.js"')
s = s.replace('require("../data/catalogoInci")', '__CAT')
s = f'import * as __CAT from "{app}/src/data/catalogoInci.js";\n' + s
assert '"../' not in s and '"./' not in s, 'products.js importa algo nuevo: actualizar gen_products.py'
open(os.path.join(os.path.dirname(__file__), 'products.mjs'), 'w', encoding='utf-8').write(s)
print('products.mjs generado desde', app)
