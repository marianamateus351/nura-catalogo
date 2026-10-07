"""fechaLista: primera fecha (commit de catalogo.json) en que cada código aparece con su lista ACTUAL."""
import json, subprocess
import os
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
revs=subprocess.run(['git','-C',R,'log','--reverse','--format=%H %ad','--date=short','--','catalogo.json'],capture_output=True,text=True).stdout.split('\n')
cur={}
for m in json.load(open(f'{R}/catalogo.json'))['marcas']:
    for p in m['productos']:
        for b in p.get('barcodes',[]): cur[b]=p['inci']
first={}
for line in revs:
    if not line.strip(): continue
    h,d=line.split()
    try: c=json.loads(subprocess.run(['git','-C',R,'show',f'{h}:catalogo.json'],capture_output=True,text=True).stdout)
    except Exception: continue
    seen=set()
    for m in c.get('marcas',[]):
        for p in m.get('productos',[]):
            for b in p.get('barcodes',[]):
                if b in cur and p.get('inci')==cur[b]:
                    seen.add(b)
                    first.setdefault(b,d)
    for b in list(first):          # si la lista cambió después, cuenta desde la vuelta a la lista actual
        if b not in seen: first.pop(b)
json.dump(first,open(os.path.join(R,'herramientas/alternativas/fechas.json'),'w'),indent=0)
print(len(revs),'versiones ·',len(first),'códigos con fecha')
