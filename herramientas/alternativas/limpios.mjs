// Condiciones 1 y 3 de alternativas.json (contrato con la app, CURACION.md "ALTERNATIVAS LIMPIAS"):
// productos del catálogo con código y CERO detecciones con el detector de la app sobre la lista oficial:
// ni disruptores (matchIngredients + dedupeIngredients) ni "otros riesgos" (matchOtrosRiesgos).
// Los "otros a tener en cuenta" (matchOtros) NO excluyen. Categoría con guessCategoria(nombre + marca),
// igual que la ficha de producto; Alimentación queda fuera.
// Necesita el repo de la app al lado: NURA_APP=../nura-firebase (por defecto) y una copia ESM de
// src/services/products.js generada con gen_products.py.
// Uso: node herramientas/alternativas/limpios.mjs > herramientas/alternativas/limpios.json
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
const aqui = path.dirname(fileURLToPath(import.meta.url));
const { matchIngredients, dedupeIngredients, guessCategoria, matchOtrosRiesgos } = await import(path.join(aqui, "products.mjs"));
const cat = JSON.parse(fs.readFileSync(path.join(aqui, "../../catalogo.json"), "utf8"));
const out = [];
for (const m of cat.marcas) for (const p of m.productos) {
  if (!p.inci || !(p.barcodes || []).length) continue;
  const c = guessCategoria("", undefined, p.nombre + " " + m.nombre);
  if (c !== "Cuidado personal" && c !== "Hogar") continue;
  if (dedupeIngredients(matchIngredients(p.inci), c).length || matchOtrosRiesgos(p.inci, c).length) continue;
  out.push({ marcaKey: m.key, marca: m.nombre, nombre: p.nombre, categoria: c, barcodes: p.barcodes });
}
process.stdout.write(JSON.stringify({ version: cat.version, productos: out }, null, 1));
