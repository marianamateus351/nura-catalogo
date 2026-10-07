// Comprobación de alternativas.json: cada producto debe dar CERO en los tres grupos del detector de la app
// (disruptores, otros riesgos y otros a tener en cuenta). Pasarla después de genera.py; todo tiene que salir 0.
import fs from "fs";
const { matchIngredients, dedupeIngredients, guessCategoria, matchOtros, matchOtrosRiesgos } = await import(new URL("./products.mjs", import.meta.url).href);
const cat = JSON.parse(fs.readFileSync(new URL("../../catalogo.json", import.meta.url), "utf8"));
const alt = JSON.parse(fs.readFileSync(new URL("../../alternativas.json", import.meta.url), "utf8"));
const porCodigo = {};
for (const m of cat.marcas) for (const p of m.productos) for (const b of (p.barcodes || [])) porCodigo[b] = { p, m };
let n = 0, conDet = 0, conRiesgo = 0, conOtros = 0; const otros = {}; const ej = {};
for (const c of alt.categorias) for (const t of c.tipos) for (const a of t.productos) {
  n++; const { p, m } = porCodigo[a.barcode];
  const cat2 = guessCategoria("", undefined, p.nombre + " " + m.nombre);
  if (dedupeIngredients(matchIngredients(p.inci), cat2).length) conDet++;
  if (matchOtrosRiesgos(p.inci, cat2).length) conRiesgo++;
  const o = matchOtros(p.inci, cat2);
  if (o.length) { conOtros++; for (const x of o) { otros[x.nombre] = (otros[x.nombre] || 0) + 1; (ej[x.nombre] ||= []).length < 3 && ej[x.nombre].push(m.nombre + " · " + p.nombre); } }
}
console.log(JSON.stringify({ total: n, conDisruptor: conDet, conOtrosRiesgos: conRiesgo, conOtrosATenerEnCuenta: conOtros, otros, ej }, null, 1));
