// Genera indice.json a partir de catalogo.json: solo nombre, marca, código y foto,
// para que la app busque por nombre sin descargar las fichas enteras.
// Uso: node herramientas/indice.mjs   (desde la raíz del repo)
import { readFileSync, writeFileSync } from "fs";
const cat = JSON.parse(readFileSync("catalogo.json", "utf8"));
const items = [];
for (const m of cat.marcas) for (const p of m.productos || []) {
  if (!(p.barcodes || []).length || !p.nombre) continue;
  const it = { n: p.nombre, m: m.nombre, c: String(p.barcodes[0]) };
  if (p.foto) it.i = p.foto;
  items.push(it);
}
writeFileSync("indice.json", JSON.stringify({ version: cat.version, items }));
console.log(`indice.json: ${items.length} productos (catálogo ${cat.version})`);
