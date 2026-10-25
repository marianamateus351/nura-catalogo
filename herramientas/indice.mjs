// Genera indice.json a partir de catalogo.json: solo nombre, marca, clave de marca,
// códigos y foto, para que la app busque por nombre y calcule las Novedades sin
// descargar las fichas enteras.
// Uso: node herramientas/indice.mjs   (desde la raíz del repo)
//
// Desde el 2026-10-25 lleva también, en la raíz, las dos listas con las que Novedades
// ofrece lo corregido y lo retirado (contrato confirmado con la app):
//   "actualizados": [{ "c": código, "v": versión en que cambió por última vez su nombre o su lista }]
//   "retirados":    [{ "c": código, "v": versión en que salió del catálogo, "motivo": texto }]
// Para saber qué cambia sin depender de git guarda una huella (nombre + lista) por código en
// herramientas/huellas.json, y el historial en herramientas/cambios.json. El motivo de un
// retirado sale de herramientas/retirados_motivos.json (código → texto) si está ahí.
import { readFileSync, writeFileSync, existsSync } from "fs";
import { createHash } from "crypto";
const leer = (f, def) => (existsSync(f) ? JSON.parse(readFileSync(f, "utf8")) : def);
const huella = (p) => createHash("sha1").update(String(p.nombre || "") + "\n" + String(p.inci || "")).digest("hex").slice(0, 12);

const cat = JSON.parse(readFileSync("catalogo.json", "utf8"));
const v = String(cat.version);
const items = [];
const actual = {};
for (const m of cat.marcas) for (const p of m.productos || []) {
  const codes = (p.barcodes || []).map(String).filter(Boolean);
  if (!codes.length || !p.nombre || !p.inci || String(p.inci).length < 5) continue;
  const it = { n: p.nombre, m: m.nombre, k: m.key, c: codes[0] };
  if (codes.length > 1) it.cs = codes;
  if (p.foto) it.i = p.foto;
  items.push(it);
  const h = huella(p);
  for (const c of codes) if (!(c in actual)) actual[c] = h;
}

const huellas = leer("herramientas/huellas.json", null);
const cambios = leer("herramientas/cambios.json", { actualizados: {}, retirados: {} });
const motivos = leer("herramientas/retirados_motivos.json", {});
let nAct = 0, nRet = 0;
if (huellas) {
  for (const [c, h] of Object.entries(actual)) {
    // Vuelve a estar tras haberse retirado: que se reimporte.
    if (c in cambios.retirados) { delete cambios.retirados[c]; cambios.actualizados[c] = v; nAct++; }
    else if (c in huellas && huellas[c] !== h) { cambios.actualizados[c] = v; nAct++; }
  }
  for (const c of Object.keys(huellas)) {
    if (!(c in actual) && !(c in cambios.retirados)) {
      cambios.retirados[c] = { v, motivo: motivos[c] || "Retirado del catálogo" };
      nRet++;
    }
  }
}
for (const c of Object.keys(cambios.actualizados)) if (!(c in actual)) delete cambios.actualizados[c];
writeFileSync("herramientas/huellas.json", JSON.stringify(actual, Object.keys(actual).sort()));
writeFileSync("herramientas/cambios.json", JSON.stringify(cambios, null, 1));

const actualizados = Object.entries(cambios.actualizados).map(([c, vv]) => ({ c, v: vv }));
const retirados = Object.entries(cambios.retirados).map(([c, r]) => ({ c, v: r.v, motivo: r.motivo }));
writeFileSync("indice.json", JSON.stringify({ version: v, items, actualizados, retirados }));
console.log(`indice.json: ${items.length} productos (catálogo ${v}); ${actualizados.length} actualizados y ${retirados.length} retirados en total (${nAct} y ${nRet} nuevos en esta versión)`);
