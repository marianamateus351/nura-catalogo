# Guía de curación del catálogo Nura (para retomar en cualquier sesión)

## Qué es
`catalogo.json` (este repo, público, rama `main`) es el catálogo curado que lee la app Nura
en tiempo de ejecución. Cada marca tiene `productos[]` con `nombre` (en español), `barcodes[]`
(códigos EAN exactos) e `inci` (lista oficial completa). **Añadir marcas/productos/fotos NO
requiere build.**

Respaldo empaquetado (mantener en paridad): repo privado `marianamateus351/nura-firebase`,
rama `claude/redesign-v2-wqk1cj`, archivo `src/data/catalogoInci.js` (`CATALOGO_FALLBACK`).
Mismo contenido, formato JS de una línea por producto.

## Reglas (acordadas con Mariana)
1. **Emparejado SOLO por código de barras**: `include: []`, `exclude: []`, `barcodes: [...]`.
   El emparejado por nombre contra Open*Facts colaba falsos positivos; no usarlo.
2. **INCI oficial y completo** (web de la marca `.es`, farmacias españolas, incidecoder,
   incibeauty). Nunca listas cortadas, alfabéticas sin orden real, "y otros ingredientes",
   ni mezclas de dos fórmulas. Si hay reformulación, usar la fórmula actual y solo asignar
   códigos de la serie actual (los envases antiguos se dejan fuera).
3. Fuera: códigos de EE.UU. (0…), Brasil (789…), Turquía (869…), México (750…), EAN-8 raros,
   nombres genéricos ("Vichy", "Cicalfate" sin "+", "Hyaluron-filler" sin decir cuál…),
   productos descatalogados, medicamentos. **El maquillaje SÍ interesa.**
4. Nombre en español (con el nombre EN/FR entre paréntesis si ayuda). Un mismo producto en
   varios tamaños = varios códigos en la misma entrada.
5. Foto: la trae Open*Facts al importar; si no hay, `foto` con URL raw de `fotos/<código>.jpg`.
6. Tras subir cambios: Mariana espera ~5 min (caché de GitHub) y reimporta la marca desde la
   app (Ajustes → Revisar contribuciones → botón de la marca). Debe salir "N importados".
7. Commits con el trailer de atribución de Claude Code. Subir siempre a los dos repos.

## Herramienta de paridad (`tools/sync_catalogo.py`)
`catalogo.json` es la fuente de verdad. El script regenera los bloques `productos: [...]`
de `catalogoInci.js` sin tocar sus comentarios, y valida el catálogo:
- `python3 tools/sync_catalogo.py sync` → regenera el JS desde el JSON.
- `python3 tools/sync_catalogo.py check` → comprueba la paridad JSON↔JS.
- `python3 tools/sync_catalogo.py validate` → formato de códigos, regiones excluidas
  (0…/789…/869…/750…), duplicados entre marcas e INCI sospechosos ("y otros", "…").
Las rutas de los dos repos están al principio del script. No requiere build.

## Flujo para obtener códigos
- La app (build 88+) tiene "Copiar lista" tras importar: da `código | nombre OF | estado | foto`.
- Con internet abierto se puede consultar Open*Facts directamente:
  `https://world.openbeautyfacts.org/cgi/search.pl?search_terms=<marca>&page_size=100&json=1&fields=code,product_name,brands,image_front_small_url`
  (y también `tagtype_0=brands&tag_contains_0=contains&tag_0=<marca>`).
- Identificar un código: buscar `"<código>"` entre comillas (upcitemdb, digit-eyes, farmacias).

## Pendiente por marca (códigos ya identificados, falta INCI oficial)
### Vichy (vichy.es)
- Capital Soleil Spray Fluido Niños SPF50+ 200 ml → 3337875810838
- Capital Soleil Crema Matificante 3-en-1 SPF50+ → 3337875695176
- Normaderm Phytosolution Crema Limpiadora Matificante 125 ml → 3337875703413
- Pureté Thermale Agua Micelar Mineral piel sensible → 3337875674997, 3337875674942
- Liftactiv Hyalu Mask → 3337875607346
- Aqualia Thermal Crema Rica → 3337875588317 (fórmula actual)
- Liftactiv Collagen Specialist (día) → 3337875607254, 3337875722520
- Liftactiv Supreme Serum 10 → 3337875489836, 3337875489867
- Minéral 89 Crema 72h (¿Ligera o Rica?) → 3337875831888
- Minéral 89 Fluido SPF50+ 72h → 3337875895781
- Liftactiv Flexiteint SPF20 (maquillaje) → 3337871321581 (solo fórmula actual)
- Liftactiv Supreme Noche → 3337871322502 · Liftactiv Ojos → 3337871323332
- Dercos Aminexil Clinical 5 (¿Mujer/Hombre?) → 3337875522748
- Dercos Sebo Corrector → 3337871311346 (ver si es fórmula actual)
- Dercos Ultracalmante cabello seco → 3337875486736
- Pureté Thermale 3-en-1 → 3337871322533; mascarillas → 3337875508896/508919/508933
- Dercos Nutrients Vitamin A.C.E → 3337875595681
### CeraVe (cerave.es)
- Skin Renewing Crema con Péptidos → 3606000537606, 3337875903509 (sobrescribe la "Night Cream")
- Loción Rostro SPF30 → 3337875840620 · Fluido Invisible SPF50+ Toque Seco → 3337875945622 ·
  Invisible Hidratante → 3337875945738 · AM Lightweight SPF50 → 3606000612655 ·
  Solar mineral → 3606000514959 · Limpiador Vitamina C → 3337875952804 ·
  Champú Hidratante Suave → 3606000607019 · SA Loción → 3606000537712 · Eye Repair ok ya.
### La Roche-Posay (laroche-posay.es)
- Lipikar Lait Relipidante 48h → 3337875552097, 3337875552127, 3337875549615
- Cicaplast B5 Gel Lavante → 3337875548519 · Agua Micelar Ultra → 3337872411595, 3337872420696
- Anthelios UVMune 400 Oil Control Fluido SPF50+ → ya tiene INCI, FALTA CÓDIGO
- Anthelios UVAIR sérum → 3337875932349, 3337875932417 · Bruma anti-brillos → 3337875549530
- Effaclar H Iso-Biome (fórmula actual; 3337875398961 es el antiguo)
### SkinCeuticals
- 10 productos sin código en el catálogo (C E Ferulic, Silymarin, Triple Lipid, AGE Advanced,
  Blemish+Age, Discoloration, Serum 10, Retinol 0.5, Metacell, Glycolic 10): buscar sus EAN
  (serie L'Oréal 33378757367xx: Phloretin 3337875736763, H.A. Intensifier 3337875736749).
### ISDIN (isdin.com)
- Fotoprotector Gel Cream SPF30 → 8470001549990 · Nutraisdin Baby gel-champú → 8470003924801
- Reparador Labial Fluido → 8470001507983 · Pediatrics SPF50 (formato?) → 8470001594945
### Avène (eau-thermale-avene.es)
- XeraCalm Aceite 400 ml → 3282779405447 · Comedomed SPF30 → 3282771001432 ·
  Comedomed (¿clásico o +?) → 3282770390414 · Ultra Fluid (¿cuál?) → 3282779428897 ·
  Cold Cream labios "Stick lèvres" → 3282770204797 · Lip butter → 3282770147261 ·
  Hydrance/Trixera/Pédiatril/DermAbsolu: identificar por código.
### Bioderma (bioderma.es)
- Photoderm Max Aquafluide (sin color) → 3401561197715 · Max Spray → 3401353688742 ·
  Spray Invisible SPF30 → 3701129807255 · Sensibio AR+ (actual) → 3401343696245 ·
  Sensibio Defensive → 3701129804445 · Sébium Gel Moussant Actif → 3701129803400 ·
  Nodé A/P/DS+ → 3401396545132, 3701129804773, 3701129805060 · Hydrabio mask → 3401343613730
### Eucerin (eucerin.es)
- Sun Oil Control Gel-Crema SPF50+ → 4005800309854 · Dry Touch SPF30 → 4005800264887 ·
  Kids Spray → 4005800027932 · Kids Loción → 4005800102363 · Allergy Protect → 4005800066382 ·
  Anti-Pigment Crema de Manos SPF30 → 4005800287510 · Lip Activ SPF20 → 4005800631702,
  9005800352756 · pH5 Gel Lavant recarga → 4005800193705
### Marcas creadas y vacías (siguiente)
- Sesderma, Nivea, Garnier: sacar la lista de códigos (app "Copiar lista" o Open*Facts) y curar.

## ⚠️ Acceso a las fuentes (importante para sesiones en Claude Code web)
En el entorno remoto la política de egress solo deja salir a GitHub y a los registros de
paquetes. Quedan BLOQUEADOS (comprobado 2026-09-09): `vichy.es`, `laroche-posay.es`,
`cerave.es`, `isdin.com`, `eau-thermale-avene.es`, `bioderma.es`, `eucerin.es`,
`incidecoder.com`, `incibeauty.com`, `cosdna.com`, Open*Facts (`world.openbeautyfacts.org`
y espejos) y todas las farmacias españolas probadas. `WebFetch` falla con `EGRESS_BLOCKED`.

Lo único disponible es la búsqueda web, que devuelve un RESUMEN generado a partir de
fragmentos: llega con listas cortadas, reordenadas o mezcladas entre variantes (se comprobó
con Capital Soleil Niños y con Normaderm Phytosolution). **No sirve como fuente de INCI**
según la regla 2. No copiar INCI de ahí.

Para seguir la curación hace falta una de estas vías:
- un entorno con egress abierto a las webs de marca / incidecoder / Open*Facts, o
- pegar en el chat el INCI (o la "Copiar lista" de la app) para que la sesión lo formatee,
  valide y suba a los dos repos.

## Estado (2026-09-09)
185+ códigos en 8 marcas: CeraVe 54 · Avène 30 · Bioderma 29 · LRP 21 · Eucerin 20 · ISDIN 14 ·
Vichy 13 · SkinCeuticals 6. Reglas de Firestore ya permiten al admin crear aprobados.
