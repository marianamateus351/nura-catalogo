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

## Flujo para obtener códigos
- La app (build 88+) tiene "Copiar lista" tras importar: da `código | nombre OF | estado | foto`.
- Con internet abierto se puede consultar Open*Facts directamente:
  `https://world.openbeautyfacts.org/cgi/search.pl?search_terms=<marca>&page_size=100&json=1&fields=code,product_name,brands,image_front_small_url`
  (y también `tagtype_0=brands&tag_contains_0=contains&tag_0=<marca>`).
- Identificar un código: buscar `"<código>"` entre comillas (upcitemdb, digit-eyes, farmacias).

## Pendiente por marca (códigos ya identificados, falta INCI oficial)
### Vichy (vichy.es) — CERRADA (2026-09-09)
Curada al completo desde el sitemap de vichy.es (97 fichas oficiales): 98 productos y 111
códigos, con el INCI que publica la propia marca en cada ficha ("Composición").
Resueltas las dudas que quedaban abiertas:
- 3337875596763 NO es el Minéral 89 Sérum: es el **Minéral 89 Gel Ojos** (movido a su entrada).
- 3337875722520 es Collagen Specialist 16 **Crema de Noche** (no la de día).
- 3337871322502 / 3337871323332 son **Hyaluronic Specialist H.A.** (crema de noche y ojos).
- 3337875522748 es Dercos Aminexil Clinical 5 **Hombre** (Mujer = 3337875522786).
- 3337871321581 es un tono de la **Base de Maquillaje Antiarrugas** (5 tonos en una entrada).
Descartados por regla 3 (descatalogados en España / envase de generación anterior / tester),
comprobados uno a uno con la foto de Open Beauty Facts:
- 3337875695176 Capital Soleil matificante 3-en-1 (envase NL/RU antiguo)
- 3337875703413 Normaderm Phytosolution limpiadora (envase DE/IT antiguo)
- 3337875674997 agua micelar 100 ml y 3337871322533 3-en-1 100 ml (uno es "testez-moi, ne peut
  être vendu"; ambos de la serie "sans parabens" anterior)
- 3337875607346 Liftactiv Hyalu Mask 15 ml · 3337875588317 Aqualia Thermal Riche 15 ml
- 3337875489836/489867 Liftactiv Supreme Serum 10 · 3337871311346 Dercos Sebo Control
- 3337875595681 Dercos Nutrients Vitamin A.C.E · 3337875508896/508919/508933 mascarillas PT 75 ml
Pendiente en Vichy: **Capital Soleil Stick Invisible SPF50+ rostro y zonas sensibles** — INCI
oficial ya recogido, pero vichy.es solo publica el SKU interno `30065949`; falta el EAN-13.

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

## Truco: sacar una marca entera de su web oficial
Las webs de L'Oréal (vichy.es, laroche-posay.es, cerave.es, skinceuticals.es) publican en el
sitemap todas las fichas, y cada ficha lleva el INCI completo dentro del bloque
`<details class="product-composition">` y el EAN en el atributo de tagging
(`"product_info": "<nombre>::<EAN>"`); los tonos van en `v-vch-variant-selector="{ean: ...}"`.
Con eso se saca la marca completa sin depender de que Open*Facts tenga el producto.
Ojo: alguna ficha usa `/` como separador de ingredientes en vez de `•` o `-`, y alguna trae
delante el código de lote o detrás un `FIL code`.

## Estado (2026-09-09)
283 códigos en 8 marcas: **Vichy 111** · CeraVe 54 · Avène 30 · Bioderma 29 · LRP 21 ·
Eucerin 20 · ISDIN 14 · SkinCeuticals 6. Reglas de Firestore ya permiten al admin crear
aprobados. Vichy cerrada; siguiente: repaso de las listas cortadas del resto de marcas y
después Sesderma / Nivea / Garnier.
