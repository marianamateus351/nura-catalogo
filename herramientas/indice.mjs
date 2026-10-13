// Genera indice.json a partir de catalogo.json: solo nombre, marca, clave de marca,
// códigos y foto, para que la app busque por nombre y calcule las Novedades sin
// descargar las fichas enteras.
// Uso: node herramientas/indice.mjs   (desde la raíz del repo)
import { readFileSync, writeFileSync } from "fs";
const cat = JSON.parse(readFileSync("catalogo.json", "utf8"));
const items = [];
for (const m of cat.marcas) for (const p of m.productos || []) {
  const codes = (p.barcodes || []).map(String).filter(Boolean);
  if (!codes.length || !p.nombre || !p.inci || String(p.inci).length < 5) continue;
  const it = { n: p.nombre, m: m.nombre, k: m.key, c: codes[0] };
  if (codes.length > 1) it.cs = codes;
  if (p.foto) it.i = p.foto;
  items.push(it);
}
writeFileSync("indice.json", JSON.stringify({ version: cat.version, items }));
console.log(`indice.json: ${items.length} productos (catálogo ${cat.version})`);
