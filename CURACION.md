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
2-bis. **Sin INCI no entra.** Un producto solo se añade si se le puede poner su INCI oficial
   completo. Un código de barras suelto, aunque esté identificado y aunque salga en Open*Facts,
   NO se mete en el catálogo: el catálogo existe para poner los ingredientes, así que una
   entrada sin ellos no aporta nada. Si de una marca solo se consiguen los códigos, esa marca
   se queda fuera hasta que haya de dónde sacar el INCI.
3. Fuera: códigos de EE.UU. (0…; salvo los UPC-A `0800897…` de NYX, que son los envases de España, ver NYX), Brasil (789…), Turquía (869…), México (750…), EAN-8 raros (salvo los EAN-8 auténticos de Unilever, ver Dove),
   nombres genéricos ("Vichy", "Cicalfate" sin "+", "Hyaluron-filler" sin decir cuál…),
   productos descatalogados, medicamentos. **El maquillaje SÍ interesa.**
4. Nombre en español (con el nombre EN/FR entre paréntesis si ayuda). Un mismo producto en
   varios tamaños = varios códigos en la misma entrada.
5. Foto: la trae Open*Facts al importar; si no hay, `foto` con URL raw de `fotos/<código>.jpg`.
6. Tras subir cambios: Mariana espera ~5 min (caché de GitHub) y reimporta la marca desde la
   app (Ajustes → Revisar contribuciones → botón de la marca). Debe salir "N importados".
7. Commits con el trailer de atribución de Claude Code. Subir siempre a los dos repos.

## Flujo para obtener códigos
- **Primero, la web de la marca** (ver la tabla de más abajo): da EAN e INCI a la vez y cubre
  el catálogo entero, esté o no en Open*Facts.
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

### CeraVe (cerave.es) — CERRADA (2026-09-09)
Curada desde el sitemap: 35 productos y 73 códigos (antes 22 y 54).
**Aviso: el `gtin13` de cerave.es no es de fiar.** Copia el mismo código en fichas distintas
(las 5 recargas comparten uno). El INCI de cada ficha sí es el suyo, así que: se usa el EAN de
la web solo cuando lo reclama UNA sola ficha, y si no, se recupera el código ya curado
emparejando **por nombre**. Por INCI no vale: la Crema Hidratante y la Crema de Manos
Reparadora llevan los mismos ingredientes en otro orden y se confunden.
Corregido: 3337875597449 es la Facial Moisturising Lotion (confirmado en Open Beauty Facts),
no el sérum de retinol, donde estaba mal puesto.
Fuera por la regla 2-bis:
- **Fluido Protector Invisible Oil Control SPF50+ (3337875945622)**: cerave.es le pone el INCI
  del Invisible Hidratante; incidecoder confirma que esa lista es la del Hidratante. Hasta que
  no haya el INCI bueno del Oil Control, no entra.
- Parches Anti-Granos: en el campo de ingredientes hay texto de marketing, no un INCI.
- Limpiador Control Imperfecciones y las 4 recargas: sin código fiable (una recarga es otro
  SKU y no puede heredar el del producto principal).
Siguen pendientes, no están en cerave.es (parecen no venderse en España): SA Loción
3606000537712 · Limpiador Vitamina C 3337875952804 · Champú Hidratante Suave 3606000607019 ·
Solar mineral 3606000514959 · AM Lightweight SPF50 3606000612655 · Night Cream 3606000537606
(Open*Facts lo da como "Skin Renewing Night Cream", no como la crema de péptidos) ·
3337875945738 (177 ml: no está claro si es el fluido o la loción invisible hidratante).

### La Roche-Posay (laroche-posay.es) — CERRADA (2026-09-09)
Curada al completo desde el sitemap: 125 productos y 160 códigos. Resueltos todos los
pendientes que había, incluido el que no tenía código:
- Anthelios UVMune 400 Oil Control Fluido SPF50+ → **3337875847292**
- Cicaplast Lavant B5 → 3337872418532 + 3337875548519 · Lipikar Leche Hidratante →
  3337875552127 + 3337875549608 · Anthelios UVAir Sérum → 3337875932349 (y el de color,
  3337875932301/3337875932264) · Bruma anti-brillos → 3337875549530
- Effaclar H Iso-Biome: la ficha actual es 3337875777797 (el antiguo queda fuera).
Quedan 5 entradas antiguas aparte porque su fórmula ya no coincide con ninguna ficha viva
(Toleriane Sensitive Crème, Hyalu B5 Serum, Toleriane Dermallergo Fluido y Contorno de Ojos,
Cicaplast Labios). "Cicaplast Labios" sigue con el SKU interno 30106659, sin EAN-13.
### SkinCeuticals — BLOQUEADA en la web (2026-09-09)
skinceuticals.es está detrás de un reto de Cloudflare que no se supera ni con navegador
headless (se queda en "Un momento…"). El sitemap sí sale (408 URLs, fichas del mismo motor de
L'Oréal, `/productos/<slug>/S17.html`), así que el día que se pueda pasar el reto la marca
sale entera como Vichy o LRP. Mientras tanto: los 16 productos ya tienen INCI; el hueco son
los códigos de 10 de ellos. Open*Facts no aporta más (sus 8 códigos ya están o son de EE. UU.),
y las farmacias se contradicen (para C E Ferulic 30 ml dan un UPC americano, un EAN interno de
distribuidor y 3606000604643), así que **no se añade ninguno sin escanear el envase**.

### ISDIN (isdin.com) — CERRADA hasta donde llegan los códigos (2026-09-09)
isdin.com publica el INCI de sus 310 fichas (`"completeIngredientList"` en el JSON de la
página; 252 con lista) **pero no el EAN**, así que la marca solo crece con códigos de fuera
(Open*Facts, 18; escaneos). Emparejado a mano, ficha por ficha, con la foto de Open*Facts:
16 productos y 18 códigos (antes 14 y 14). INCI actualizado desde la web en 10 productos.
- Corregido: 8429420135444 es el **Protector Labial SPF 30** (estaba como SPF 50+).
- Nuevos: 8470001594945 Pediatrics Lotion Spray SPF50 200 ml · 8470001549990 Gel Cream SPF30
  250 ml ("nueva fórmula") · 8470003173704 After Sun Lotion 400 ml (unido al de 200 ml) ·
  8429420264106 Transparent Spray Wet Skin 250 ml (unido al 8429420187948).
- **Ojo con las reformulaciones**: el Transparent Spray Wet Skin (8429420187948) y el
  HydroLotion (8429420192232) del catálogo son envases de la generación anterior ("Ginger
  Cell Protect", "Protects & Detox"): se dejan con su INCI antiguo, que es el suyo, y no se
  les pone el actual de la web.
- Fuera: 8470001507983 Reparador Labial tubo 10 ml (isdin.com tiene DOS fichas vivas con
  distinta fórmula y no se puede atar el código a una) · 8470003924801 Nutraisdin Bath
  gel-champú (línea antigua, hoy Babynaturals) · 8429420181021 "loción corporal" (sin foto ni
  nombre) · 8470006896624 Mupirocina (medicamento) · 8470001677013 (sin nombre).

### Avène (eau-thermale-avene.es) — CERRADA (2026-09-09)
Curada desde `product.xml` (149 fichas): 153 productos y 162 códigos (antes 23 y 30).
- **El EAN va en la URL** (`/p/<slug>-<EAN>-<hash>`); el `gtin` del JSON de la página está
  mal (le falta el último dígito), no usarlo. El INCI está en el panel `composition_inci`.
- Avène escribe cada ingrediente como "nombre (común) (INCI puro)", p. ej. "Ricinus Communis
  (Castor) Seed Oil (Ricinus Communis Seed Oil)": se guarda solo el INCI puro.
- El Agua Termal en spray tiene dos ingredientes de verdad (agua termal y nitrógeno): entra
  aunque la lista sea tan corta.
- Fuera: Sunsimed KA y Sunsimed Pigment (productos sanitarios, la ficha no publica INCI).
- Fluido mineral SPF50+, Fluido mineral con color SPF50+ y la Espuma de afeitar MEN tienen
  dos fichas vivas con distinta fórmula (otro envase): se dejan las dos, con "(ref. …)" en
  el nombre para distinguirlas.
Pendientes resueltos: Comedomed SPF30 (3282771001432 = Comedomed+ Fluido intensivo SPF30),
"Cold Cream stick lèvres" (3282770204797 = Bálsamo labial SPF 50+), Lip butter (3282770147261
= Bálsamo hidratación intensa 24h). Siguen fuera por no estar en la web: XeraCalm Aceite
400 ml 3282779405447 · Comedomed 3282770390414 · Ultra Fluid 3282779428897.

### Bioderma — vía incidecoder + foto de Open*Facts (2026-09-09)
bioderma.es NO publica el INCI (ni en la ficha renderizada con navegador, ni en su GraphQL
`/api/graphql`, que devuelve `p_class_phrase_ingredient_reglementaire` vacío en los 108
productos). Se curó por la vía alternativa: 28 productos y 42 códigos (antes 16 y 29).
Método, código a código, sobre los 94 de Open*Facts:
1. Fuera los que no son EAN-13 europeos (3401…/3701…) y los sin foto.
2. Foto de OBF: solo entra el envase actual (marca "Care first · NAOS"). Los "Sans parabens",
   "Cellular Bioprotection", "Skin Protect Complex" son generaciones anteriores y se descartan
   (fueron la mayoría: 26 de 44).
3. INCI de incidecoder. Cuando hay varias versiones del mismo producto, desempata el texto de
   la etiqueta que los usuarios de OBF fotografiaron (`ingredients_text`): se exige que ≥80 %
   de sus ingredientes estén en la versión elegida y que saque 0,25 a la siguiente. Sin texto
   y con varias versiones (Photoderm Brume invisible, Atoderm Crème 500 ml NAOS, toallitas
   Sensibio H2O), fuera. Sensibio H2O AR se queda en 0,67: fuera.
4. Sensibio AR 3401343696245: Mariana lo tenía como AR+ pero la foto de OBF dice "AR" y las
   fórmulas AR/AR+ no se parecen en nada: fuera hasta escanearlo.
Añadidos: Sensibio Defensive · Nodé DS+ · Nodé P · Photoderm Pediatrics Spray y Mineral ·
Hydrabio Mascarilla · Cicabio Lip Repair · Atoderm Gel de Ducha eco-recarga · Atoderm
Intensive Baume 500 ml · Sensibio Gel Moussant (200 y 500 ml) · Photoderm Max Fluide SPF100 ·
Pigmentbio Sensitive Areas. Scripts: `incidecoder.py` (búsqueda + lista completa) y
`bio_pick.py` (desempate con OBF), reutilizables para Sesderma y otras.

### Eucerin (eucerin.es) — CERRADA (2026-09-09)
Curada desde el sitemap: 124 productos y 137 códigos (antes 13 y 20).
- INCI: array ordenado `ingredients[].IngredientTitle.value` dentro del JSON de la página.
  Eucerin traduce al español unos pocos ingredientes clave (Glicerina, Pantenol, Carnitina,
  Creatina, Niacinamida, Ácido glicirretínico/láctico/salicílico/glicólico, "Aceite de semilla
  de ricino communis"), que se devuelven a INCI con una tabla; y arrastra erratas
  ("Arginine HCI", "Titanium Dioxide (nano)", "Laureth-9,4-t-Butylcyclohexanol" pegados).
- **El EAN no está en la ficha del propio producto**, solo en los teasers que lo enlazan desde
  otras páginas (`data-tracking-product-id` + `href`). Se recolectan de todo el sitio y luego
  se cruzan. Así salieron 132 códigos; 4 fichas se quedaron fuera porque ningún teaser las
  enlaza (Aquaphor 220 g, Probiom8, pH5 Loción Ligera, Sun Fluid Sensitive Protect).
Los 9 códigos que quedaban pendientes de esta marca **siguen fuera**: la web cubre ya esos
productos pero con SU propio EAN (otro formato), y no hay forma de confirmar que el código
antiguo sea de la misma fórmula. Son 4005800309854, 4005800264887, 4005800027932,
4005800102363, 4005800066382, 4005800287510, 4005800631702, 9005800352756 y 4005800193705.

### Nivea (nivea.es) — CERRADA (2026-09-09)
Marca entera desde el sitemap: 233 productos y 235 códigos (rostro, cuerpo, sol, desodorantes,
cabello, hombre, niños). Ficha: `"gtin13"`/`"ean"` en el JSON de la página (y el EAN también
va en la URL), INCI en el bloque "Incluye", nombre en el h1.
- 12 minis/formatos de viaje fuera: su URL lleva un código interno corto, no un EAN-13.
- 4 fichas sin INCI (packs y dos sérums), fuera.
- El h1 no distingue las versiones NIVEA MEN de las de mujer (Dry Fresh, Protect & Care):
  se separan por el slug y se anota "(NIVEA MEN)".

### Sesderma (sesderma.com) — NO PUBLICA EL INCI (2026-09-09)
Salesforce Commerce Cloud. Renderizada con navegador, la ficha (p. ej. Bodyses) solo trae
descripción, beneficios y modo de empleo: ni INCI, ni EAN (solo el SKU interno). Open*Facts
tiene 2 códigos. Por la regla 2-bis la marca se queda vacía; si alguna vez interesa, la vía
sería incidecoder producto a producto.

### Deliplus (Mercadona) — CERRADA hasta donde llega OBF (2026-09-10)
Resultado: **15 productos y 15 códigos**, de 532 códigos de Deliplus en Open Beauty Facts.
Lo que se comprobó, por orden:
1. **tienda.mercadona.es** — la API JSON funciona sin código postal (`?lang=es&wh=vlc1`):
   `/api/categories/` (árbol), `/api/categories/<id>/` (productos de la subcategoría) y
   `/api/products/<id>/`. La ficha trae **EAN-13, nombre oficial y fotos, pero NO el INCI en
   texto**: `nutrition_information.ingredients` viene vacío en las 646 fichas de cosmética,
   higiene, maquillaje y bebé (categorías 20, 21, 22, 24 y 23). El INCI solo está en la foto
   del envase, y de una foto no se transcribe. Aun así, Mercadona vale como **validador de
   códigos**: solo se acepta un código de OBF si está en el catálogo vivo de Mercadona
   (producto a la venta hoy, nombre oficial). Script: `mercadona.py`.
2. **Open Beauty Facts** — `tag_0=deliplus` (479) + `search_terms=deliplus` (132 más) = 532
   códigos. Solo **147** siguen en el catálogo vivo de Mercadona; el resto son referencias
   descatalogadas. De esos 147, **89 no tienen INCI transcrito** (muchos tienen solo la foto de
   la etiqueta) y de los 58 restantes la transcripción es de calidad OCR: 18 con basura
   ("Lote", "www.mercadona.com RECICLA", "Utilícese preferentemente…"), 17 que no son un INCI,
   y varias con comas perdidas o tramos garbleados. Quedaron 15 listas completas y limpias
   (tres con una coma perdida o una errata evidente, corregidas: "Coco-Glucoside Cocamidopropyl
   Betaine", "Polyquarternium", "Tocopheryl Acetate Citric Acid"). Script: `gen_deliplus.py`.
3. **incidecoder** tiene unas 30 fichas de Deliplus subidas por usuarios; sirvió para el sérum
   de Ácido Hialurónico y Ceramidas (lista limpia, 0,82 con la de OBF).
Entran: Agua de peinado Aqua Styling · Champú Hydra hyaluronic · Champú Natural · Champú Zero ·
Champú protección y brillo · Crema para pies 10 % urea · Desodorantes aqua, power, seda y
pies fresh & dry · Gel de higiene íntima hidratante · Jabón de manos dermoprotector y su
recarga · Toallitas íntimas · Sérum Ácido Hialurónico y Ceramidas.
**Cómo hacer crecer Deliplus**: hay 646 fichas de Mercadona con EAN y nombre oficial ya
descargadas (`mc_det.json`); lo que falta es el INCI. La vía realista es que las usuarias
fotografíen la etiqueta desde la app (OCR) o que se transcriba a mano de la foto de OBF
(`image_ingredients_url`, 89 productos la tienen) — eso ya sería trabajo de persona, no de
script, porque una foto no se transcribe automáticamente sin revisarla.
### Cien (Lidl) — CERRADA hasta donde llega OBF (2026-09-10)
Resultado: **26 productos y 26 códigos** (22 de OBF + 4 con INCI oficial de lidl.de). Recuento del embudo de OBF:
- Open Beauty Facts: `tag_0=cien` 237 + `search_terms=cien` → 366 códigos; con `brands` que
  contiene "cien" (palabra de verdad, no "cien" suelto en el nombre): 344; **EAN-13 reales**
  (fuera los 118 que empiezan por `20…`, código interno de tienda): 214.
- Con INCI transcrito en OBF: 87 de 214. De esos, la criba: 18 con basura de envase, 10 que
  no son un INCI, 9 sin nombre, ~10 con encabezados en varios idiomas ("/Sestavine:/Sastojci:").
- **Criba de erratas de OCR** (nueva, `vocab.py`): cada ingrediente se contrasta con el
  vocabulario de los 1.076 productos ya curados (1.621 nombres). Si un ingrediente no está y
  se parece ≥ 0,88 a uno conocido ("Glyceny Oleate", "Hydrobenzoyl", "arfum", "shea bitter",
  "Seed Dil"…), es una errata y **el producto se descarta**, no se arregla a ojo. Si no está
  pero es un INCI real (Sodium Silicate, Polyglyceryl-3 Caprylate, Citrus Aurantium Amara
  Flower Water…), vale. Así cayeron 17 de los 39 que habían pasado el resto de filtros.
- Solo se han quitado asteriscos y notas al pie ("*Ingrédients issus de l'Agriculture
  Biologique", "**sauf bouchon"); eso es formato, no reconstrucción.
- Nombres: OBF los trae en francés/alemán/italiano (Cien se vende en toda Europa con el mismo
  EAN); se han puesto en español a mano. La cantidad es la de OBF.
- **lidl.es no sirve de validador**: su API de búsqueda (`/q/api/query/<término>` con
  `Accept: application/mindshift.search+json;version=2`) sí devuelve EAN y nombre oficial,
  pero la tienda online solo lista los aparatos CIEN BEAUTY (secadores, afeitadoras, 28
  artículos), ninguna cosmética de tienda. No se puede saber qué Cien está a la venta hoy.
- **lidl.de SÍ publica el INCI oficial** de la poca cosmética Cien que vende online (misma
  API con `locale=de_DE&assortment=DE`; la ficha lleva la lista completa en un `<p>` dentro
  de `content-tabs__tab`). El EAN es el mismo en toda Europa, así que vale para España. Hoy
  solo lista 4 (Cien Sun leche SPF30/SPF50, Kids crema y Kids spray SPF50): entran con INCI
  oficial. Conviene repetir la búsqueda en temporada (la oferta online cambia). lidl.fr, .it
  y .pt no listan cosmética Cien.
Entran: antitranspirantes Extra Dry (roll-on mujer y hombre, spray hombre), Comfort Fresh,
desodorantes roll-on, espuma de afeitar Sensitive, geles de ducha (Sensitive, almendra,
argán y flor de naranjo, aloe vera, 400 ml, sólido), champú y gel melocotón-albaricoque,
champú hombre, jabón de manos Gentle & Pure, limpiador facial hidratante, crema de manos aloe
Bio, crema de día VitalBeauty, crema corporal hidratante, mascarilla capilar regeneradora y
crema solar Active SPF30. Scripts: `gen_cien.py`, `vocab.py`, `final_cien.py`.

### Neutrogena (neutrogena.es) — cerrada 2026-09-10: 50 productos, 56 códigos
Marca de Kenvue. **neutrogena.es publica EAN-13 e INCI en texto**, así que la marca sale
entera de la web y OBF queda para confirmar tamaños. Cómo va la ficha (Next.js/Contentful):
- Sitemap `/sitemap.xml` (201 URL). Las fichas **no siguen una sola ruta**: la mayoría van en
  `/productos-*/<gama>/<slug>`, pero los solares Ultra Sheer cuelgan de `/proteccion-solar/`,
  y hay fichas sueltas en `/cuerpo/…`, `/rostro/…` y `/lineas-de-productos/…`. No filtrar
  por ruta: descargar todo lo que no sea artículo de consejos y quedarse con lo que traiga EAN
  (52 fichas con EAN; el resto son páginas de gama o FAQ).
- **EAN** en el widget de compra: `data-mm-ids="<EAN>,0<EAN>"` (en Ultra Sheer, sin la coma;
  también en el JSON-LD como `"gtin":"0<EAN>"` con el 0 delante, que hay que quitar).
- **INCI** en `<div data-sb-field-path="product.ingredients">`: normalmente un `<p>` con
  comas, pero Collagen Bank e Hydro Boost crema/contorno traen **un `<p>` por ingrediente**, el
  sérum de niacinamida una lista `<li>` tras "Los ingredientes del … son:", y las fichas nuevas
  (Ultra Gentle, Hydro Boost SPF50) un `<p class="rich-text">` suelto. Llevan pegado el código
  interno de fórmula (`[PR-017060]`, `FPT0793`), que se quita pero **sirve para identificar
  tamaños en OBF**: si la etiqueta de OBF trae el mismo PR-, es la misma fórmula.
- Erratas de la web corregidas contra el vocabulario: `C12-15 Alky Benzoate`, `Tocophero`,
  `Glycreryl Stearate SE`.
Qué se quedó fuera y por qué:
- **Bálsamo Reparación Inmediata Nariz y Labios** (3574660602609): la web acaba la lista en
  `CI 7789` (colorante truncado) y no hay etiqueta en OBF ni ficha en incidecoder → lista
  incompleta, regla 2.
- **Clear & Defend+ Parches** (3574661889085): hidrocoloide, la web no publica ingredientes.
- Las **cuatro cremas de manos Fórmula Noruega** la web las publica con la lista **traducida
  al español** ("Glicerina, Alcohol Cetearílico…"). Entraron con el INCI en inglés porque las
  etiquetas de OBF de los otros tamaños (3574661685977 sin perfume, 3574660239829 rápida
  absorción) coinciden término a término y en el mismo orden; las dos hermanas (con perfume,
  manos y uñas) se pasaron con esa misma correspondencia. Ojo: OBF guarda para esos mismos
  nombres la **fórmula antigua con parabenos/fenoxietanol**, que no es la actual.
- De los 171 códigos de OBF (107 empiezan por `3`, 47 por `0`, 11 por `7`) solo entraron los
  que casan con una ficha actual por código PR- o por lista idéntica (crema de pies ultra
  hidratante 100 ml, limpiador Hydro Boost, cremas de manos). El resto son EE. UU. (`0…`),
  Brasil (`789…`) o gamas ya no publicadas (Visibly Clear, Deep Clean, Nordic Berry, Hydro
  Boost Aqua-Gel de fórmula antigua): regla 3, no entran.
Scripts: `neutrogena.py` (parseo de fichas), `gen_neutrogena.py` (nombres en español y
erratas), `obf_inci.py`, `vocab.py`.

### Dove (dove.com/es) — cerrada 2026-09-10: 22 productos, 28 códigos (de 74 con EAN en la web)
Marca de Unilever. **dove.com/es publica el EAN de todo, pero el INCI solo en una de cada tres
fichas**, y parte de esas listas son fórmulas antiguas. Cómo va la web (AEM de Unilever):
- Akamai devuelve 403 al `curl` pelado: hay que mandar cabeceras de navegador completas
  (`dvcurl.sh`: User-Agent, Accept, Accept-Language, sec-ch-ua, Sec-Fetch-*).
- El `sitemap.xml` solo trae categorías. Las fichas se sacan del listado de `/es/products.html`
  (64 fichas, `data-list-count`), que pagina con el id del componente:
  `<ruta data-productlist-path>?page=productlist-c9e3a36c89~2`, `~3`… (sin el id devuelve vacío).
- Ficha `/es/p/<slug>.html/<GTIN-14>`. El EAN va en la URL y en `data-productvariants`, un JSON
  con **todas las variantes** (tamaños y aromas), cada una con su código, tamaño e
  `ingredientStatement`. Quitar los ceros a la izquierda del GTIN-14: quedan EAN-13 o, en
  roll-on y crema, **EAN-8 auténticos de Unilever** (59095842, 80466437…), que sí entran.
- El acordeón "Ingredientes" del HTML es solo una plantilla (`##…ingredientStatement@@`): si
  el JSON no trae la lista, la ficha no la tiene. 74 códigos con EAN, **23 con INCI**.
Criterios que decidieron qué entra:
- **INCI de la web** solo si es la fórmula vigente: cinco listas de la web (Men+Care aerosol y
  roll-on, crema 50 ml) traen **Butylphenyl Methylpropional** (prohibido en la UE desde 2022)
  o **HICC** (2021): fórmulas antiguas, no entran. Ese filtro (`PROHIBIDO` en `gen_dove.py`)
  vale para cualquier marca: un prohibido en la lista delata una ficha sin actualizar.
- **INCI de OBF solo por el mismo código** (nunca por nombre, por la trampa de fórmula distinta
  por país) y solo si la etiqueta está limpia: gel Nutritivo, gel Hidratación Profunda,
  roll-on Original, jabón en pastilla y autobronceadora medio-oscuro. Cuando la web agrupa
  tamaños del mismo aroma bajo una ficha, la lista de un tamaño vale para los demás (regla 4).
- Fuera: crema de manos Aguacate (la web parte "Calendula, Officinalis Flower" y duplica
  Propylparaben: lista no fiable) y 46 códigos sin INCI en ningún sitio (aerosoles, roll-on
  0 % aluminio, casi todos los geles de ducha): regla 2-bis.
- `wiop.unilever.es` ("What's in our products") existe pero solo cubre hogar (Mimosín, Skip,
  Cif, Domestos). Primor publica el EAN pero no la lista. incibeauty está tras Cloudflare.
  Los códigos de OBF con `en:spain` que no están en la web son latinoamericanos o sin INCI.
Scripts: `dvcurl.sh`, `dove.py` (fichas → `dove_db.json`), `gen_dove.py`, `obf2.py` (OBF con
reintentos), `obf_inci.py`.

## PRODUCTOS DE LIMPIEZA: se curan distinto que la cosmética
Categoría nueva (pedida por Mariana, 2026-09-10). Antes de empezar, lo que cambia:

**1. La etiqueta NO lleva lista de ingredientes.** Un detergente declara *rangos por familia*
("5-15% tensioactivos aniónicos, <5% tensioactivos no iónicos, perfume, Limonene"). Eso NO
sirve para el catálogo: no dice qué conservante ni qué tensioactivo lleva. **No meter nunca
esos rangos en el campo `inci`.**

**2. La lista completa sí existe y es obligatoria.** El Reglamento (CE) 648/2004 de detergentes
(Anexo VII) obliga al fabricante a publicar en una web la **ficha de datos de ingredientes**
con la lista completa. Esa web es la fuente buena, el equivalente al INCI de la cosmética.
El envase suele llevar la URL. Ahí es donde hay que ir: **si una marca no la publica de forma
usable, se queda fuera igual que Sesderma** (regla 2-bis, sin cambios).

**3. Los códigos salen de Open Products Facts**, no de Open Beauty Facts. La app ya consulta
las tres bases (`fetchBrandProducts` en `src/services/products.js`), así que las fotos vienen
solas al importar. La cobertura es más floja que en cosmética: contar con menos códigos.

**4. Merece la pena, y está comprobado.** De los 206 disruptores que detecta Nura, 34 son de
categoría Hogar, y entre ellos están justo los que aparecen en estas fichas: MIT, MCI, BIT y
OIT (isotiazolinonas), cloruro de benzalconio, DDAC, nonilfenol y alquilfenoles etoxilados,
2-butoxietanol, fenoxietanol y los tensioactivos etoxilados. Un detergente escaneado da
resultado de verdad, no un "todo bien" vacío.

**5. El campo `inci` se usa igual** aunque técnicamente no sea un INCI: es el texto de
ingredientes que lee el detector. Nombres en español, como siempre.

### Fairy (P&G) — cerrada 2026-09-10: 6 productos, 11 códigos (de 71 variantes con lista completa)
**P&G publica la ficha del Anexo VII de forma usable y se recorre entera.** Lo que falla es el
emparejamiento con el código, no la lista. Cómo está montado:
- **info-pg.com** es la web del Reglamento 648/2004 para toda Europa. Es una app Next.js con
  selectores país → marca → formato, y los datos salen de **Contentful** (espacio
  `damp14uglyq4`, clave pública de lectura en el propio JavaScript; `cf.py`). Consultas:
  `brandSelector` (`fields.countryId=11` = España), `prodFormSelector` (marca + país),
  `productDetails` (país + formato: `variants`, `paNumber`, `ipms`) e `ingredients`
  (`fields.paNumber` → `ingredientNames`, la lista completa y ordenada). El `sitemap.xml`
  apunta a un host de desarrollo y no lista fichas: no sirve.
- Para España: 20 marcas de P&G, 354 fichas; Fairy tiene 71 variantes en 6 formatos
  (a mano 544, máquina 498, gel 1023, abrillantador 1392, Professional 1573/1661), 62 fórmulas
  distintas (`fairy_pg.json`). **La misma consulta vale para Ariel (50), Don Limpio (140),
  Lenor (218), Ambi Pur (789), Febreze (188)…**: `cf.get({'content_type':'productDetails',
  'fields.countryId':11,...})` y filtrar por `prodFormId` de la marca.
- La lista trae nombres químicos largos con comas dentro ("Alcohols, C9-11-branched and
  linear, ethoxylated"); se quitan las comas internas porque la app trocea por comas.
  "Colorant" y "PARFUM" se dejan como "Colorante" y "Parfum".
**El problema: la ficha no lleva EAN y el envase no lleva la clave de la ficha.** En la foto
del envase (OPF) sale un código de 8 cifras junto al código de barras (90590462, 90794278…),
pero **no coincide** ni con el `paNumber` ni con el `ipms` de Contentful. Así que el
emparejamiento es solo por el **nombre exacto del envase** (leído en la foto de OPF) contra el
nombre de la variante de P&G, y P&G lista **varias fichas con nombres casi iguales** para el
mismo producto comercial: "Original", "Ultra Original", "Ultra Poder Original"; "Lemon",
"Ultra Lemon", "Limón", "Limón / Limão", "Maxi Poder - Limón"; tres fichas distintas para las
cápsulas "Original All in One con aroma a limón". Si el envase casa con una sola ficha, entra;
si caben dos, no (regla de las dos fórmulas).
- Entran (a mano): Ultra Poder Original, Ultra Poder Más Rápido, Ultra Original (4 tamaños),
  Maxi Poder, Limpieza & Cuidado Aloe Vera y Pepino (ficha `91228936007`, cuyo nombre es
  el del envase; la `…004` es otra revisión), Limpieza & Cuidado Rosa y Satén.
- Fuera: cápsulas Todo en Uno y Original All in One (dos y tres fichas posibles), Poder 3 en 1
  (dos listas distintas bajo dos formatos), Fairy Professional 5 L ("Original" no existe en
  la ficha: solo Regular/Classico), Fairy Ultra sin subnombre legible, y el Ultra Lemon con
  envase portugués. OPF solo tiene 15 códigos con `en:spain` de 113 (el resto UK, DE, FR).
- Etiquetas viejas (fotos de 2019-2020) declaran Methylisothiazolinone; las fichas actuales
  de esos mismos productos ya no la llevan (Benzisothiazolinone + Phenoxyethanol): se usa la
  ficha vigente, como manda la regla 2.
Scripts: `cf.py` (Contentful), `opf2.py`/`opf_inci.py` (Open Products Facts), `gen_fairy.py`.

### Sanytol (AC Marca) — cerrada 2026-09-10: 4 productos, 5 códigos (de 36 fichas en sanytol.es)
**AC Marca sí publica la lista completa del Anexo VII, pero no en España.** Lo que hay:
- **sanytol.es** (WordPress, `page-sitemap.xml`, 36 fichas): nombre, formato y aroma, pero ni
  ingredientes ni Anexo VII. **El EAN va en el nombre del archivo de la imagen principal**
  (`og:image` → `…/8411660170231-SANYTOL-…png`); 11 fichas lo traen. Ojo: las imágenes de
  "productos relacionados" arrastran otros EAN, hay que quedarse solo con la principal.
- **sanytol.pt** enlaza "Composição do produto" a **info.grupoacmarca.com** →
  `reach.grupoacmarca.com/public/v2`, el portal REACH/Anexo VII de AC Marca (solo http). La
  **lista** de productos es pública (`/public/v2/ajax?marca=SANYTOL`: 175 entradas con su
  código interno, `sy/sanytol_list.json`), pero la **ficha de ingredientes pide cuenta de
  usuario** (`/productos/<id>` → login). No se ha creado cuenta: es una decisión de Mariana.
- **sanytol.fr/composition-des-produits/** publica 49 PDF "FIC public" (fiche des ingrédients
  du consommateur, Anexo VII, fabricante GRUPO AC MARCA, L'Hospitalet) con el **código de
  fórmula** de AC Marca. Ese código es el mismo que usa el portal español: la ficha
  "Cuisine Dégraissant PURE" lleva `9433639396`, que en el portal es "SANYTOL DESINFECTANTE
  QUITAGRASAS LIMON"; "Salle de Bain PURE" lleva `9433639397` = "DESINFECTANTE LIMPIADOR
  BAÑOS EUCALIPTUS"; "Multi-usages Eucalyptus PURE" cubre `33630000…33630400` = base de
  `9433630000-M` (multiusos) y `9433630000-B` (botella limpiahogar). **Solo entra un producto
  cuando el código de la ficha francesa coincide con el del producto español**; el nombre
  parecido no basta.
- Entran: Multiusos Eucaliptus (pistola + recarga), Suelos y Superficies Eucaliptus (botella),
  Baños Eucaliptus, Quitagrasas Limón. Las listas son cortas (7-8 nombres: DDAC como activa,
  isopropanol, etanolamina, ácido málico, tensioactivo etoxilado, perfume) y el detector ya
  reconoce el cloruro de didecildimetilamonio.
- Fuera: sprays Hogar y Tejidos Menta y Algodón (la ficha francesa es de los códigos
  `33639415`/`33639465` y el producto español es `…416`/`…466`: código distinto, no se asume
  la misma fórmula); Multiusos Manzana y Suelos Limón (dos entradas posibles en el portal y
  ninguna ficha con su código); toallitas, geles de manos, colada, quitamanchas y
  limpialavadoras (sin EAN en sanytol.es ni en OPF). OPF solo tiene 32 códigos de Sanytol y
  27 son franceses (`30…`): aquí el EAN vino de la propia web.
- Cómo seguir si Mariana quiere más: pedir cuenta en reach.grupoacmarca.com (formulario
  público "Solicitar una nueva cuenta"); con ella la ficha de cada código español se lee
  directa y valdría también para Norit, Alex, Denenes y Ecran, que están en el mismo portal.
Scripts: `dvcurl.sh`, `sy/` (fichas, PDF y listas), `gen_sanytol.py`.

### L'Oréal Paris (loreal-paris.es) — cerrada 2026-09-10: 250 productos, 511 códigos
**Sale entera de la web, con EAN + INCI oficiales**, pero con marcado propio (no es el de
Garnier ni el de Vichy):
- `sitemap.xml` con 2075 URL sin distinguir fichas de artículos: se bajan todas (`lp/get.sh`,
  4 en paralelo, ~40 min) y es ficha la que trae un JSON-LD `Product`. **Las páginas de tono
  NO están en el sitemap**: cada ficha lleva `<oap-product-variant-selector :variants='[…]'>`
  con `{value, url, ean, name}` por tono, y hay que bajar esas URL en pasadas sucesivas hasta
  que no aparezcan nuevas (tres pasadas: 2075 → 2501 páginas, 734 fichas con código).
- **EAN**: `gtin13` del JSON-LD (a veces GTIN-14 con ceros delante: quitarlos). Los `30…` de
  8 cifras son **EAN-8 franceses de L'Oréal** (máscaras, eyeliners), auténticos: entran.
- **INCI**: `additionalProperty[name="Ingredients"].value`, precedido del código F.I.L.
  ("G974712 - INGREDIENTS:") y seguido de la nota legal; sinónimos con barra ("Aqua / Water",
  "CI 77891 / Titanium Dioxide": se toma el primero); "[+/- puede contener: …]" se conserva
  como colorantes. Erratas de la web corregidas contra el vocabulario (`TYPOS_LP` en
  `lp_parse.py`: "Cocamidopropul", "Sodium Citrat E", "Catyl Alcohol", "PEG, 30"…).
- **Tonos** (regla 4): los tonos de una ficha con el **mismo INCI** van en una entrada con
  todos sus códigos (Accord Parfait base 26 tonos, Cushion 17, Laque Resistance 13…); si el
  INCI cambia entre tonos, entradas separadas con los tonos en el nombre (Color Riche, Labial
  Infalible 24H, Le Shadow Stick, More Than Concealer…). El nombre base es el prefijo común
  de los nombres de los tonos cortado en el número de tono. Tamaños con INCI idéntico y
  nombre parecido se funden.
Fuera y por qué:
- **Tintes y coloración**: de 128 fichas, **13 traen la caja entera** (marcadores de revelador
  —Hydrogen Peroxide, Phosphoric Acid— y de crema de color —Resorcinol, p-Phenylenediamine,
  m-Aminophenol— juntos, cosa imposible en un solo bote): Age Perfect Nudes (5) y Retoca
  Raíces (6) con los componentes etiquetados en el propio texto ("1252400 K - CREMA
  COLORANTE: … (F.I.L. x). 1152439 - CREMA REVELADORA: …"), y Universal Nudes (2) con los
  componentes separados por "Value2:", "Value3:" sin etiqueta (se etiquetan por marcadores).
  Entran con el formato de componentes de Garnier ("Crema Colorante: … · Crema Reveladora:
  …"). Las otras **115 publican un solo bote** (34 solo revelador, 21 solo crema de color,
  45 solo acondicionador, 12 sin marcadores, 3 vacías), con un único código F.I.L.: no hay
  lista escondida, y no entran (regla de Mariana). Los tintes de cejas Brow Color traen
  "SIN AMONIACO" en vez de lista.
- Ojo con "Value2:"/"Value3:" en fichas normales: son **versiones repetidas de la misma lista**
  (con o sin "/ EAU", con o sin [NANO]); si tras limpiar quedan idénticas se toma una, y si
  son **fórmulas distintas** sin decir cuál va (Clásico contorno de ojos, Le Shadow Stick 290
  y 125, Crema Embellecedora), el producto no entra (5 fichas).
- 96 fichas **sin lista** en la web (Bright Reveal, Clásico, Filler, Glycolic Gloss, varias
  máscaras…): el campo "Ingredients" viene vacío o con texto de marketing.
- 3 listas **traducidas al español** (base en polvo Infalible, sérum Vitamina C…) y 3 con un
  nombre roto ("Alumi", "Sorbate" suelto): fuera, como en Neutrogena.
Scripts: `lp/get.sh`, `lp_parse.py`, `lp_agg.py` (fichas → `lp/db.json` + URL de tonos que
faltan), `gen_lp.py` (agrupación y nombres). OBF no hizo falta.

### Maybelline New York (maybelline.es) — cerrada 2026-09-10: 81 productos, 455 códigos
Sale entera de la web con los scripts de L'Oréal Paris, con dos diferencias de marcado:
- `sitemap.xml` (758 URL) solo lista **113 fichas**; el resto de fichas de producto se
  recogen de los enlaces `/todos-los-productos/<gama>/<tipo>/<slug>` de las páginas de
  categoría (segunda pasada: 744 páginas, 101 fichas con código).
- **Los tonos van todos en la misma ficha**, sin página propia: `<input
  class="shade-selector__input" data-variant-ean="…" data-name="…">` por tono, y **una sola
  lista de ingredientes por ficha** con los colorantes en "[+/- puede contener]". Así que
  cada ficha es una entrada con todos los EAN de sus tonos (Super Stay Matte Ink 44, Tattoo
  Studio 26, Fit Me Mate 24, Vinyl Ink 22…). Nombre en `<span class="product__header-name">`
  (el JSON-LD trae solo la gama, "FIT ME®").
- La nota legal va **delante** de la lista (en L'Oréal Paris iba detrás), la lista a veces sin
  "INGREDIENTS:" y separada por "●"; el "puede contener" aparece también en francés sin
  corchete ("/PEUT CONTENIR"). Todo eso está en `lp_parse.py` (`NOTA`, viñetas antes de las
  barras de sinónimos) y vale para las dos webs.
- **114 EAN-8 `30…`** (máscaras, eyeliners, gloss): los franceses auténticos, entran.
Fuera: 10 fichas sin lista (calendario de adviento, dos primers, Master Fix, dos Lash
Sensational, paleta Burgundy Bar…), 1 traducida al español (Sky High Green Altitude) y 6
códigos de EE. UU. (`41554…`, UPC de 12 cifras). Scripts: `mb/get.sh`, `mb_parse.py`,
`mb_gen.py`. Detrás, en el mismo grupo y con la misma plataforma: **NYX Professional
Makeup** y **Essie**.

### Eroski — cerrada 2026-09-10: 5 productos, 5 códigos (fuente OBF; la tienda da INCI pero no EAN)
**Comprobado con Mariana desde su navegador** (el dominio entero responde a las máquinas con
el desafío "Comprobando tu navegador" de Google Cloud Armor, un reCAPTCHA interactivo que ni
Chromium headless pasa; ni la Wayback Machine ni Common Crawl son alcanzables desde el proxy;
la web corporativa `www.eroski.es` no tiene catálogo):
- La ficha de `supermercado.eroski.es/es/productdetail/<id>-<slug>/` **sí publica los
  ingredientes en texto**, en `<div class="feature feature-text-ingredients"><span
  class="title">Ingredientes</span><p class="text">…</p>`, montada en el servidor (Tapestry),
  sin API JSON detrás. Para limpieza da la lista real ("Vinagre de alcohol 8%"), no rangos.
- **No publica el EAN**: el único identificador es el interno de la tienda (`25622853`, que
  también nombra las fotos); no hay ningún número de 13 cifras en la página. Es el caso
  inverso de Mercadona (EAN sin INCI).
- **Higiene y cosmética: la ficha NO trae ingredientes.** Comprobado con un script en la
  consola de Chrome de Mariana sobre 42 fichas de gel de ducha (Eroski Basic, Sanex,
  Palmolive): "Características" solo da fabricante y dirección. El bloque "Ingredientes" solo
  aparece en limpieza (vinagre). Las fotos de ficha son miniaturas de 200 px; el código de
  barras de la foto trasera no se lee a ese tamaño (hay una versión grande, `_2_x.jpg`, sin
  probar). **Eroski queda aparcada por decisión de Mariana (2026-09-10)**: la tienda no sirve
  para higiene y el circuito de fotos no compensa. Solo entraría algo por "Buscados" + OBF.
- **El buscador de la tienda acepta un EAN** y devuelve su ficha (probado con 8480010184396 →
  crema de manos Belle). Cada código que se consiga por otro lado se resuelve a su lista en
  un minuto, desde un navegador normal.
Circuito para ir llenando Eroski (no hay forma de sacar la gama entera de golpe):
1. Los códigos llegan de la pestaña **"Buscados"** de la app (escaneos sin resultado, con el
   nombre de Open*Facts si lo hay) o de fotos del código de barras en tienda.
2. Mariana teclea el EAN en el buscador de la tienda y pega aquí el bloque "Características"
   de la ficha, con el código delante.
3. Se limpia, se pasa la criba por vocabulario (`vocab.py`) y se sube.
Lo que hay: 10 códigos en OBF/OPF (`tag_0=eroski` + `search_terms=eroski`), 6 con lista;
entraron los 5 que pasan la criba (crema de manos reparadora y Natural de **Belle**, la línea
de cosmética de Eroski; Belle Men; jabón líquido Basic Dermo; gel íntimo), con tres erratas
de coma corregidas por inequívocas. Los otros 5 (8480010168426, 8480010185195,
8480010191110, 8480010198249, 8480010195552) **ya no existen en la tienda**: descatalogados,
fuera (regla 3). En Open Food Facts hay cientos de Eroski, pero es alimentación.
`gen_eroski.py`, `er/`.

### Sanex (Colgate-Palmolive) — cerrada 2026-09-10: 14 productos, 14 códigos (de 54 fichas con INCI en la web)
Gel de ducha y desodorante. **sanex.es publica el INCI completo pero ningún EAN**, así que los
códigos vienen de Open Beauty Facts (156 códigos, 123 europeos) emparejados con las fichas.
Cómo va la web (AEM tras Akamai, como Dove):
- `curl` pelado → "Access Denied"; en paralelo, errores SSL. Funciona `dvcurl.sh` (cabeceras de
  Chrome completas) **en serie con 1,5 s de pausa**. Sitemap `sitemap.xml` (149 URL, 63 fichas).
- El INCI está en la pestaña "INGREDIENTES" como tabla `INGREDIENTE | PROPÓSITO` (una fila por
  ingrediente); la tabla no lleva marca fija, hay que buscar cualquier `<table>` que contenga
  "INGREDIENTE". 54 fichas la traen (11–22 ingredientes). No hay JSON-LD con `gtin13`, ni
  `data-…` de compra: solo SKU internos.
- **5 fichas traen la lista traducida al español** (Derma Therapy anti-sequedad, aceite de ducha y
  alisar textura, Ultrahidratante Urea, agave revitalizante): "Cocamidopropil Betaína", "Sulfonato
  De Sodio C14-16 Olefinas"… Fuera (regla 2), como las cremas de manos de Neutrogena.
- Erratas de la web corregidas: "Parfumingrediente" → Parfum, "Poloxámero 124" → Poloxamer 124.
- **La web repite la misma lista de 11 ingredientes en las cinco fichas de gel Neutro/Zero%**
  (Family, Hidratación Delicada, Hidratante, recarga, Nutritivo), y la etiqueta española del
  Zero% piel sensible (8718951389519, sin perfume) demuestra que es falso: 8 ingredientes y sin
  Parfum. Esas fichas no son fiables → **ningún gel Neutro/Zero% entra**, aunque OBF tenga 8 códigos.
Cómo se emparejó (por orden de fiabilidad):
1. **INCI idéntico** (Jaccard 1,00 entre la etiqueta de OBF y la lista de la web): 3 códigos con
   texto (Zero% roll-on 50 ml, Natur Protect piedra de alumbre spray 200 ml, Dermo Protector
   stick 65 ml) + 1 leído en la foto (Natur Protect antimanchas roll-on). Vale cualquier país.
2. **Nombre y formato, solo con envase español o portugués** (etiquetados `en:spain`/`en:portugal`
   en OBF y portada comprobada en la foto): 10 códigos (roll-on Dermo+ Invisible/Extra
   Control/Sensitive, Men Invisible y Men Active Control, spray Men Invisible, roll-on Mineral
   Protect piel normal, geles Cuidado Experto Protector, Aceite y Atopiderm Nutri Repair). Cuando
   la etiqueta de OBF trae otra lista (Extra Control roll-on con BHT y ciclopentasiloxano, Men
   Invisible roll-on 2024 sin aloe, Men Active Control con óxido de zinc) es la fórmula anterior:
   se usa la de la web (regla 2, reformulación). No se aceptan emparejamientos por nombre con
   envases de otros países: Sanex cambia fórmula por mercado (los Zero% franceses de OBF tienen
   9 ingredientes; los españoles, 8 u 11).
3. Nombres nuevos de la web: "pH Balance Dermo" ahora es "Dermo+"; "Natur Protect" ahora es
   "Mineral Protect"; "Zero%" gel ahora es "Sanex Neutro" (las URL antiguas `zero-…` siguen).
Fuera y por qué: gama antigua sin ficha (Dermo Protector gel con SLES, Zero% con SLES, Natur
Protect bambú, Men Natur Protect, Men Stress Response, Atopiderm crema de manos, BiomeProtect
loción, Hygiene Protector jabón de manos, Men Dermo Sensitive gel, Dermo Equilibrante), listas de
OBF que difieren en 1–3 ingredientes de la ficha (BiomeProtect gel UK con Polyquaternium-7, Natur
Protect anti-traces con alumbre, Zero% roll-on francés con inulina), 14 códigos `31…` (Francia
antigua) y los `0…`. Las fichas de la web sin código en OBF (Dermo+ sprays, cremas desodorantes
Sensitive/Fresh Defence/Total Freshness, Men Fresh Protect, Zero% sprays, Mineral Protect piel
sensible, Cuidado Experto Pro Hydrate, niños, germen de trigo, Micellar Equilibrante, piel seca
Cuidado Experto +) esperan a que aparezca el código: se entra con la foto o con "Buscados".
Scripts: `sx/get.sh` + `dvcurl.sh` (descarga), `sx_parse.py` (tabla → `sx/db.json`),
`obf2.py`/`obf_inci.py` (`obf_sanex.json`, `sx/obf_inci.json`), `gen_sanex.py` (lista PROD con
el cómo de cada emparejamiento) → `sanex_merged.json`.
Dato ya comprobado y que ahorra tiempo: **la tienda de Eroski NO trae ingredientes de Sanex**
(se miraron 42 fichas de gel de ducha, solo dan fabricante y dirección). No volver por ahí.

### NYX Professional Makeup (nyxcosmetics.es) — cerrada 2026-09-10: 542 productos, 999 códigos (de 219 fichas vivas)
**No es la plataforma de L'Oréal Paris/Maybelline**: nyxcosmetics.es va sobre Salesforce Commerce
Cloud (URLs `…/NYX_007.html`, `dwsid`, `demandware.store`) y detrás de un **desafío interactivo
de Cloudflare**. Scripts de L'Oréal Paris reutilizados: solo `limpia_inci` (mismo formato de
lista: código de fórmula + "INGREDIENTS:" + viñetas + F.I.L.). El resto, nuevo (`nx/`).
Cómo se pasa Cloudflare (probado):
- `curl` con cabeceras de Chrome → "Just a moment…" (Turnstile) en TODO, sitemap incluido.
  Chromium con Playwright pasa: la **primera navegación** de la sesión se queda en el desafío
  (se resuelve solo en segundo plano) y **las siguientes pasan**. `page.request` no pasa (huella
  TLS distinta); `fetch()` ejecutado DENTRO de la página sí, y es rápido (~5 páginas/s).
- Los endpoints `/on/demandware.store/…` (rejilla de categoría `Search-UpdateGrid`, variantes,
  popin) van desafiados aparte: hay que hacer una navegación (`goto`) a uno de ellos, y a partir
  de ahí el `fetch()` interno también pasa. Scripts: `nx/xfetch.js` (páginas), `nx/popin.js`.
- El sitemap no se puede leer y las categorías pintan la rejilla con JavaScript desde un
  endpoint desafiado, así que **las fichas se sacaron a fuerza bruta por ID**: `/p/NYX_001.html`
  … `/p/NYX_1300.html` (el slug da igual). 348 responden, de las que **219 son fichas vivas**,
  129 redirigen a una categoría (descatalogadas) y 952 no existen.
Cómo va la ficha:
- Los tonos van en la misma ficha: `<option data-js-pid="800897078133">Los Angeles</option>` y
  `<a class="c-swatch" data-js-pid=…>`. **El pid es el UPC-A de 12 dígitos del tono (800897…)**;
  no hay `gtin13` ni JSON-LD `Product` (solo `ProductGroup` y migas).
- La lista de ingredientes es **por tono** y se sirve con
  `Product-Information?cid=pdp-popin-ingredient&pid=<pid>` (~1 KB): 1248 popins bajados. Dos
  formatos: el de L'Oréal ("952049 3 - INGREDIENTS: … (F.I.L. …)", 479 entradas) y uno antiguo
  de NYX sin código ni F.I.L. ("Talc, Mica, … MAY CONTAIN / PEUT CONTENIR (+/-): Titanium
  Dioxide (CI 77891), Iron Oxides (CI 77499, 77491, 77492)", 63 entradas; se normalizan los
  colorantes a "CI nnnnn"). Variantes: "INGREDIENTES:", "INGREDIENTS / INGRÉDIENTS:", bloques
  "Value1:", lista que empieza por viñeta, y dos notas legales que se quitan.
- Paletas y kits: un bloque por grupo de tonos ("SHADES 01, 03, 17 … INGREDIENTS:" o "Shades 01,
  03 & 08 Talc, …") o por componente. **Se funden en una lista sin repetidos** (es la lista de la
  caja, como se acordó con los tintes): 8 popins, la mayor con 31 bloques (The Smokey, 102
  ingredientes). Si se prefiere fuera, es `MULTI` en `nx_gen.py`.
- Tonos con la misma lista → una entrada con todos los códigos (78 entradas con varios códigos);
  labiales, delineadores y sombras cambian de fórmula por tono → una entrada por fórmula con los
  tonos en el nombre (hasta 5 y "y N tonos más"; "01 - Clearly Spicy - Clear" → "01 Clearly Spicy").
**Códigos 0… (regla 3, excepción acordada aquí):** NYX es marca de EE. UU. y **todos** sus
códigos son UPC-A `800897…`, que en EAN-13 es `0800897…`. Son los códigos de los envases que se
venden en España (la web .es los publica tono a tono), así que **entran** con el 0 delante; la
regla 3 sigue valiendo para el resto de marcas (un `0…` en Dove o Maybelline sí es un envase de
EE. UU.). Efecto en la app: Android devuelve el UPC-A con 12 dígitos e iOS con 13, así que el
escáner normaliza los de 12 dígitos anteponiendo el 0 (`App.js`, `BarcodeScanner`); sin eso NYX
no casaría en Android. **Hay que compilar la app para que aplique.**
Fuera y por qué: 70 fichas sin lista en la web (brochas, esponjas, pestañas, sacapuntas, y
también producto real: Powder Blush 23 tonos, Invincible Coverage 14, Rouge Cream Blush, Xtreme
Lip Cream, Roll On Eye Shimmer, eyeliners líquidos, Matte Lipstick Vault, Boudoir mascara…: 213
popins vacíos); 7 tonos con fórmula antigua (CC Cream con HICC, Jumbo Eye Pencil selección con
Isobutylparaben); Shine Loud (22 tonos: la web solo da la lista del top coat, 3 ingredientes);
Studio Finishing Powder (la lista viene en chino: "硅石"). Aviso: la web trae bastantes tonos
que ya no se venden dentro de fichas vivas; entran igual (mismo producto, código válido).
Scripts: `nx/xfetch.js` (fichas por ID → `nx/grp`), `nx_parse.py` (título, pid seleccionado,
tonos), `nx_agg.py` (→ `nx/db.json`, `nx/pids.txt`), `nx/popin.js` (→ `nx/pop/<pid>.html`),
`nx_gen.py` (limpieza, fusión de bloques, agrupación por INCI, `EXCLUIR`) → `nyx_merged.json`.
Detrás de NYX, en el mismo grupo: **Essie** (comprobar plataforma antes: puede ser SFCC como NYX).

### Colgate (colgate.es) — SIGUIENTE MARCA (pedida por Mariana, 2026-09-10)
Pasta de dientes y colutorios: producto de uso diario en todas las casas y con exposición en
mucosa, así que interesa aunque la marca sea pequeña en número de referencias.
**Es de Colgate-Palmolive, igual que Sanex**, así que lo primero es probar si comparte web:
`dvcurl.sh` (cabeceras completas de Chrome, **en serie con 1,5 s de pausa**, porque `curl`
pelado da "Access Denied" tras Akamai) y el parser de la tabla `INGREDIENTE | PROPÓSITO` que
se usó en sanex.es. Si colgate.es es el mismo AEM, la marca sale casi sola.
Lo que hay que comprobar y lo que se espera:
1. Sitemap de colgate.es y si la ficha trae la pestaña de ingredientes en tabla.
2. **El EAN será el hueco**, como en Sanex (sanex.es no publica ninguno): los códigos, de
   Open Beauty Facts (`tag_0=colgate`, `search_terms=colgate`), emparejando por nombre y, mejor
   aún, **por INCI idéntico** contra la etiqueta de OBF, que es como se emparejó Sanex por
   orden de fiabilidad. Códigos buenos: `84…` (España) y `87…` (Países Bajos, Colgate-Palmolive
   Europa); los `0…` son de EE. UU., fuera (regla 3).
3. **Aviso heredado de Sanex: la web de esta empresa repite listas entre fichas.** En Sanex
   ponía el mismo INCI en las cinco fichas de gel Neutro/Zero% y se demostró falso con la
   etiqueta real. Si en Colgate aparece la misma lista en varias pastas distintas, **no
   fiarse**: contrastar con la etiqueta de OBF y, si no cuadra, fuera.
4. Ojo con la **pasta de dientes**: no lleva "INCI" al uso sino la lista de ingredientes de
   producto de higiene bucal (Aqua, Sorbitol, Hydrated Silica, Sodium Fluoride/Sodium
   Monofluorophosphate, Sodium Lauryl Sulfate, aromas…). Vale igual, es la lista que lee el
   detector. Los **cepillos y la seda dental no entran**: no tienen lista de ingredientes.
5. Colutorios y blanqueadores sí entran (son líquidos con lista completa).
Fuera por la regla 3: gama descatalogada, que en esta marca es abundante porque renombra mucho.

## Navegador headless (para webs renderizadas por JavaScript)
Hay Chromium en la máquina y Playwright se instala con `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
npm install playwright`. **El proxy de la sesión no digiere el TLS 1.3 de Chromium**: hay que
lanzarlo con `--ssl-version-max=tls1.2 --disable-http2 --disable-quic
--ignore-certificate-errors` y `proxy: {server: process.env.HTTPS_PROXY}`; si no, todo da
`ERR_CONNECTION_RESET`. Con eso Sesderma y Bioderma renderizan; Cloudflare (SkinCeuticals) no.

## Fuente principal: la web oficial de cada marca (comprobado 2026-09-09)
Casi todas publican la ficha con EAN + INCI completo, así que **la web de marca manda** y ya
no dependemos de que el producto esté en Open*Facts: se recorre el catálogo entero de la marca
y se añade todo lo que traiga EAN + INCI. Open*Facts queda solo para la foto y como respaldo.

| Marca | Sitemap | EAN en la web | INCI en la web | Cómo se saca |
|---|---|---|---|---|
| Vichy | sí | sí | sí | `product-composition` + `"product_info":"<nombre>::<EAN>"`; tonos en `v-vch-variant-selector` |
| La Roche-Posay | sí | sí | sí | `product-ean` y `:upc-list` (varios tamaños); INCI en el atributo `other-ingredient`; nombre en la miga de pan |
| CeraVe | sí | sí | sí | mismo grupo, marcado propio (`product-details`) |
| Garnier | sí (`/sitemap.xml`) | sí | sí | fichas en `/marcas/<gama>/<subgama>/<slug>`; INCI tras `INGREDIENTS:` |
| Eucerin | sí (`/sitemap`) | sí | sí | INCI como array ordenado `ingredients[].IngredientTitle.value` en el JSON de la página |
| Nivea | sí | sí | sí | **el EAN va en la propia URL**: `tonico-facial-suave-40058081826880244.html` → EAN 4005808182688 |
| Avène | sí (`/product.xml`, 149 fichas) | sí | sí | **el EAN va en la URL**; INCI tras "Ingredientes Composición" |
| ISDIN | sí (310 fichas) | **no** | sí | INCI sí, pero no publica EAN: los códigos hay que sacarlos de Open*Facts |
| Bioderma | sí (108 fichas) | no | **no** | ni renderizada ni por GraphQL publica el INCI: vía incidecoder + foto de OBF (ver su apartado) |
| Sesderma | sí (~120 fichas ES) | no | no | Magento PWA renderizado por JavaScript; solo expone el SKU interno |
| SkinCeuticals | — | — | — | Cloudflare responde 403 a todo, incluido el sitemap |
| Neutrogena | sí (`/sitemap.xml`) | sí | sí | EAN en `data-mm-ids`; INCI en `data-sb-field-path="product.ingredients"` (a veces un `<p>` por ingrediente); ver su apartado |
| Cien (Lidl) | API lidl.es / lidl.de | sí | solo lidl.de, y solo lo que vende online (4 solares) | OBF con criba de erratas por vocabulario + lidl.de (ver su apartado) |
| Dove | solo categorías | sí (en la URL y en `data-productvariants`) | 1 de cada 3 fichas, y a veces fórmula antigua | listado paginado por id de componente; ver su apartado |
| Fairy (P&G) | info-pg.com vía Contentful (354 fichas ES) | **no** | sí, lista completa Anexo VII | EAN de OPF emparejado por nombre exacto del envase; ver su apartado |
| Sanytol (AC Marca) | sí (`page-sitemap.xml`, 36) | sí, en el nombre de la imagen principal | **no**; la lista está en los PDF FIC de sanytol.fr (mismo código de fórmula) y tras login en reach.grupoacmarca.com | ver su apartado |
| L'Oréal Paris | sí (2075 URL, sin las páginas de tono) | sí (`gtin13` JSON-LD; tonos en `oap-product-variant-selector`) | sí (`additionalProperty` Ingredients), salvo tintes y ~100 fichas vacías | ver su apartado |
| Maybelline | por comprobar | por comprobar | por comprobar | misma plataforma que L'Oréal Paris: reusar sus scripts (ver su apartado) |
| Eroski | tienda tras reCAPTCHA interactivo (solo desde navegador) | **no** (solo id interno; el buscador acepta EAN) | sí, en texto (`feature-text-ingredients`) | códigos de "Buscados" o fotos → ficha por EAN → pegar bloque; ver su apartado |
| Sanex | sí (`sitemap.xml`, 63 fichas; Akamai: `dvcurl.sh` en serie) | **no** (solo SKU interno) | sí, tabla INGREDIENTE/PROPÓSITO (54 fichas; 5 traducidas al español; geles Neutro con lista repetida) | códigos de OBF por INCI idéntico o por nombre solo con envase ES/PT; ver su apartado |
| NYX | **no** (Cloudflare); fichas a fuerza bruta por ID `/p/NYX_nnn.html` con Playwright | **UPC-A de 12 dígitos** por tono (`data-js-pid`), que es `0800897…` en EAN-13 | sí, por tono, en el popin `Product-Information?cid=pdp-popin-ingredient&pid=` | Salesforce Commerce Cloud, no la plataforma de L'Oréal Paris; ver su apartado |
| Colgate | por comprobar | por comprobar | por comprobar | Colgate-Palmolive como Sanex: probar `dvcurl.sh` y el parser de la tabla INGREDIENTE\|PROPÓSITO (ver su apartado) |
| Maybelline | sí (758 URL, solo 113 fichas) + enlaces de categoría | sí (`gtin13` + `data-variant-ean` por tono en la misma ficha) | sí, una lista por ficha con "puede contener" | scripts de L'Oréal Paris; ver su apartado |
| Deliplus | API tienda.mercadona.es (646 fichas) | **sí** (EAN-13) | **no** (solo en la foto) | Mercadona valida el código; el INCI, de OBF solo si la lista está completa y limpia |

Para Bioderma, Sesderma y SkinCeuticals sigue haciendo falta otra vía (renderizar la ficha
con un navegador headless, farmacias, incidecoder). Por la regla 2-bis, de estas tres marcas
solo entrarán los productos a los que se les pueda poner el INCI oficial; los demás se quedan
fuera aunque se tenga su código.

Ojo con los detalles del HTML: alguna ficha usa `/` como separador de ingredientes en vez de
`•` o `-`, alguna trae delante el código de lote y detrás un `FIL code`, y las webs tienen sus
erratas (`CITRIC ACIDv`, `Ehtylhexylglycerin`, `Ethylhexil Salicylate`). Los acrónimos se
normalizan en mayúsculas (PEG, PPG, EDTA, PCA, SE, MEA, CI) para que casen con lo ya curado.

## PENDIENTES DE MARIANA (no los puede resolver Claude solo)
- **Cuenta en el portal REACH de AC Marca** (`reach.grupoacmarca.com`), que desbloquearía las
  fichas de ingredientes de las **175 referencias de Sanytol** en vez de las 4 que se han
  podido curar desde los PDF franceses. Requiere registrarse a su nombre en un portal de un
  tercero, así que es decisión suya. **Estado (2026-09-10): lo deja pendiente, no ahora.**
  Si algún día dice que sí, Sanytol se retoma desde ahí y el mismo portal cubre el resto de
  marcas de AC Marca.

## Estado (2026-09-10)
3303 códigos en 21 marcas: **NYX 999** · L'Oréal Paris 511 · Maybelline 455 · Nivea 235 ·
Garnier 234 · Avène 162 · LRP 160 · Eucerin 137 · Vichy 111 · CeraVe 73 · Neutrogena 56 ·
Bioderma 42 · Dove 28 · Cien 26 · ISDIN 18 · Deliplus 15 · Sanex 14 · Fairy 11 ·
SkinCeuticals 6 · Sanytol 5 · Eroski 5. Ninguno de los 2076 productos está sin INCI. Sesderma
sigue vacía.
Eroski: la tienda da INCI pero no EAN; se llena con los códigos de "Buscados" (ver su apartado).
Sanex cerrada con 14 códigos: la web da INCI sin EAN y OBF solo confirma 14 (ver su apartado).
NYX cerrada con 999 códigos, todos `0800897…` (UPC-A de NYX; excepción a la regla 3, ver su
apartado). **Hay que compilar la app**: el escáner ahora normaliza los UPC-A de 12 dígitos.
**Colgate ya está creada y vacía** (botón visible en la app), pendiente de curar: misma empresa
que Sanex, ver su apartado.
