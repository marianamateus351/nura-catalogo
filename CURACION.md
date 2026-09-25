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
3. Fuera: códigos de EE.UU. (0…; salvo los UPC-A `0800897…` de NYX y los `0095008…`/`0884486…`/`0080079…` del essie enamel clásico, que son los envases de España, ver NYX y Essie), Brasil (789…), Turquía (869…), México (750…), EAN-8 raros (salvo los EAN-8 auténticos de Unilever, ver Dove),
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
**CORRECCIÓN 2026-09-11 · las cremas de manos Fórmula Noruega tienen mal los códigos.**
Mariana escaneó su tubo de la **Concentrada Con Perfume (4012273123009)** y la etiqueta real
lleva **Methylparaben y Propylparaben**; el INCI que le habíamos puesto es el de la fórmula
ACTUAL de neutrogena.es, sin parabenos (Ethylhexylglycerin + Caprylyl Glycol). O sea que a un
tubo de la fórmula ANTIGUA se le pegó la lista de la nueva.
Causa: estas cuatro cremas la web las publica con la lista **traducida al español**, así que el
INCI se reconstruyó cruzando con etiquetas de OBF de otros tamaños **emparejando por nombre, no
código a código**. Y OBF guarda para estos mismos nombres la fórmula antigua con parabenos.
El código delataba el problema: `4012273123009` empieza por `40` (Alemania) mientras el resto
de la gama es `357466…`. **Ya se ha quitado del catálogo** (la entrada se queda sin código,
como el Cicaplast Labios de LRP: sigue siendo buscable por nombre con la fórmula actual).
**Revisión 2026-09-11, código a código contra la FOTO de la etiqueta en OBF (no por nombre):**
- Concentrada Sin Perfume: **8002110383709** (tubo UK/IE de 50 ml, 2022, fabricado en Val de
  Reuil; el prefijo `800…` es de Johnson & Johnson Italia), **3574661685977** (50 ml DE/FR/NL,
  2022) y **3574661685960** (75 ml, 2024). Las tres etiquetas llevan la lista actual con
  Ethylhexylglycerin + Caprylyl Glycol, código de fórmula [PR-0003658], **sin parabenos**, y
  coinciden ingrediente a ingrediente con el INCI del catálogo. Se quedan.
- Rápida Absorción: **3574660239829** (75 ml, etiqueta finlandesa) y **3574661687018** (75 ml
  DE): lista actual [PR-0003707], sin parabenos, idéntica al catálogo. Se quedan.
  **3574660239805** es el EAN que publica la propia ficha de neutrogena.es (no viene de OBF).
- Manos y Uñas **3574660342352** y Anti-Edad SPF20 **3574661210933**: EAN de la propia ficha
  de neutrogena.es, no de OBF; OBF no tiene ficha de ninguno de los dos.
- Concentrada Con Perfume: sin código (el único que tenía, 4012273123009, era de la fórmula
  antigua con parabenos y ya se quitó). Buscable por nombre.
Resultado: **no sale ningún código más**. Lección para el flujo: cuando el INCI se reconstruya
desde OBF, emparejar por INCI idéntico con la etiqueta (texto o foto) del MISMO código, nunca
por nombre; es lo que se hizo después en Sanex y Colgate.
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

**Elvive, revisión 2026-09-11 (pedida por Mariana).** La gama SÍ estaba en el catálogo desde el
cierre (54 productos, 67 códigos: Total Repair 5, Color Vive, Hidra Hialurónico, Bond Repair,
Glycolic Gloss, Aceite Extraordinario, Dream Long, Full Resist, Collagen Lifter, Growth Booster,
Violeta), pero **la web publica esos nombres sin la palabra "Elvive"** ("Total Repair 5 Champú
Reparador…"), así que buscando "Elvive" solo salían 5. Arreglado: las 48 entradas de cuidado
capilar llevan ahora "Elvive <gama>" delante. De las 72 fichas Elvive de la web, 20 se habían
caído; se recuperan 8 códigos con fuente fiable y el resto se queda fuera:
- **Con lista traducida en la web y lista INCI en incidecoder que coincide 1:1 al traducirla**
  (es la comprobación que faltó en las cremas de manos de Neutrogena): Bond Repair Champú
  (3600524074685) e Hidra Hialurónico Champú 400 ml (3600524029968).
- **Foto de la etiqueta en OBF del mismo código**, envase ES/PT, código de fórmula 1199633 A:
  Aceite Extraordinario Aceite tratamiento de uso universal 100 ml (3600522215455).
- Lista INCI de la propia web con erratas obvias corregidas ("AMMONIUM· LAURYL SULFATE" partido,
  "COCAMIDOPROPUL", "Potassium, Sorbate"): Color Vive Más que un Champú (3600523970087). La
  Dream Long Más que un Champú (3600523969913) tiene un token fusionado no resoluble ("Sodium
  Hydroxycitronellal") y se queda fuera.
- Lista INCI de la web que el parser había marcado como traducida por la nota de marketing que
  la sigue: Dream Long Mascarilla Rapid Reviver (3600523709823).
- Tamaños de la misma ficha (mismo nombre en la web, solo cambia el ml) sumados a la entrada que
  ya tenía la lista: Glycolic Gloss Champú Boost de Brillo 250 y 300 ml, Acondicionador 300 ml.
Fuera por la regla 2-bis (la web solo trae marketing o una lista traducida sin nada con que
contrastarla; OBF no tiene ni texto ni foto; incidecoder no tiene la ficha o no se puede
comprobar): Full Resist Men champú, Crema Stop Rotura y Power Mask; Violeta Mascarilla
Intensiva; Aceite Extraordinario Color Vive; Glycolic Gloss champú/acondicionador/sérum "Con
Ácido Glicólico" y Tratamiento 5 Min; Hialurónico Pure champú y sérum. Script: `fix_elvive.py`.

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

### Colgate (colgate.es) — cerrada 2026-09-10: 9 productos, 13 códigos (de 28 fichas con lista en la web)
Mismo AEM de Colgate-Palmolive que sanex.es y mismo acceso (`dvcurl.sh` en serie con 1,5 s; el
sitemap `sitemap.xml` se lee directo: 245 URL, 50 fichas de producto), **pero la lista no va en
tabla**: va en `<meta name="ingredientList" value="…">` (y repetida en el dataLayer), una por
ficha, con cola "Contains: Sodium Fluoride Total Fluoride content: 1450 ppm" que se quita.
Nombre en `<meta name="itemName">`, categoría en `itemCategory`, `itemId` interno: **sin EAN**,
como se esperaba. Parser: `cg_parse.py` → `cg/db.json`. 28 fichas con lista (pastas, 2
colutorios, 2 sérums); sin lista: 13 cepillos, 2 sedas, el kit LED, y 5 pastas reales (Max Fresh
cristales, Max White Ultra Efecto Instantáneo, MaxWhite cristales, Total + Esmalte ×2).
Códigos: OBF `tag_0=colgate` da 366, 156 europeos (143 `87…`, solo 3 `84…`), 57 con texto de
etiqueta. Emparejado por lista (`gen_colgate.py`, con el cómo de cada código):
- **Las listas de la web llevan los alérgenos del aroma** (Limonene, Menthol, Anethole,
  Beta-Caryophyllene, Carvone, Mentha Viridis Leaf Oil…) y muchas etiquetas de OBF no, así que
  la comparación se hace sobre la lista sin alérgenos y tolerando erratas de OCR ("Cl 74160",
  "Flouride", "Xantham"). Entra solo lo que coincide 1:1: Max White One (2 códigos), Purple
  Reveal (2), Ultra Active Foam, Instant, Sensation Blanqueador (2), Max White Carbón (2, uno
  leído en la foto de la etiqueta española), Triple Action (pack 2×75), Total Prevención Activa
  Original (envase 70 ml con la lista actual de fluoruro de estaño) y Sérum Blanqueador Morado
  (envase español).
- **El aviso heredado se cumplió**: la web repite la misma base (sin alérgenos) en cuatro
  fichas de Total (Original, Junior, Dientes Sensibles y el kit de viaje). Solo entra Original,
  que es la que coincide con una etiqueta real. Junior y Dientes Sensibles, fuera aunque tengan
  código.
- Fuera por no coincidir con la etiqueta: Colgate Total Original antiguo (8718951465756, envase
  español con la fórmula de arginina y zinc; la web ya solo tiene la reformulada "Prevención
  Activa" con fluoruro de estaño), Total Advanced Encías Sanas (8718951471603, otra gama), Max
  White Charcoal UK (Mica + CI 77891 de más), Ultimate Radiance (CI 74160 de más), Plax Taze
  Nane turco (lista igual a Plax Soft Mint pero otro aroma: trampa del aroma), Herbal/Dentagard
  (PT y DE difieren de la web), y los envases españoles sin texto ni foto (Herbal Original,
  "blanqueador total", Plax, MaxFresh): no se emparejan solo por nombre en esta marca.
Las 19 fichas con lista y sin código esperan al código (foto o "Buscados"): Total + Cuidado de
encías / Dientes Sensibles / Limpieza / Blanqueador / Junior, Anti-Placa Expert ×2, Max White
For Coffee, Tea & Wine, Herbal, Kids Animal Gang y Bluey, Plax Soft Mint, Max White colutorio,
Sérum Nocturno, Triple Action (tubo suelto).

### Essie (essie.es) — cerrada 2026-09-10: 27 entradas, 125 códigos (de 253 fichas; 141 con lista en INCI)
**Es la plantilla antigua de la plataforma de L'Oréal**, no la de L'Oréal Paris/Maybelline ni la de
NYX: `dvcurl.sh` en serie con 1 s de pausa entra sin problema (sin Akamai ni Cloudflare), el
sitemap `sitemap.xml` lista las 253 fichas (una página por tono, como L'Oréal Paris), pero **no hay
JSON-LD `Product`** (solo migas). De los scripts anteriores solo vale `limpia_inci`.
- Código: `<accordion-panel tab-title="ingredientes e información de seguridad" product-id="0000030189416">`;
  se quitan los ceros → **EAN-8 `30…` (92 códigos, franceses de L'Oréal) o EAN-13 `3600…`**. Solo
  vale el `product-id` del acordeón de ingredientes: el resto de `product-id` de la página son
  los del carrusel "tonos similares".
- Lista: dentro del mismo acordeón, con viñetas ● y "[+/- PUEDE CONTENER …]" largo, que se
  conserva como colorantes. Parser `es_parse.py` → `es/db.json`.
- **La web da la misma lista a toda una gama**: 36 tonos de essie enamel clásico, 17 de gel
  couture, 17 de la colección de invierno… con todos los colorantes en el "puede contener". Es
  la lista de la caja, no cambia entre tonos, así que aquí **sí se agrupa** (lista idéntica de
  verdad): 27 entradas para 125 códigos, con los tonos en el nombre (hasta 5 y "y N tonos más").
  Las listas distintas (Mrs Always Right, Glazed Metal, Serene Slate…) van solas.
- Tratamientos que traen lista: Good As New, Hard To Resist (×3), Top Coat Brillo, Top Coat
  Stay Longer. Sin lista o con "No se requieren": Smooth-E, Here To Stay, Strong Start, All In
  One, Apricot Cuticle Oil, Good As Gone (quitaesmalte), Quick-E, Gel Setter, Good To Go, Matte,
  Speed Setter, Break Fix, On A Roll…: fuera (34 fichas con código y sin lista).
- **10 fichas traen la lista traducida al español** (la colección de verano 2025: rev it up, new
  highs, strut with it, blushed metal, fuel your life, you can-dy it, crushed gold, dopamine
  rush, y On A Roll ×2): "ACETATO DE BUTILO ● NITROCELULOSA…". Fuera (regla 2).
- **essie.fr NO sirve de apoyo**: tiene el mismo `product-id` y la lista en INCI, pero para el
  mismo código da listas distintas de las de essie.es (aruba blue: en .es la base clásica con
  tosylamide y propyl acetate; en .fr una base con alcohol) en 20 de los 22 códigos comunes. Es
  el aviso de las webs que repiten listas, ahora entre países: no se ha usado nada de .fr.
- **Códigos `0…` (misma excepción que NYX):** el essie enamel clásico se fabrica en EE. UU. y 28
  tonos llevan UPC-A (`095008…`, `0884486…`, `080079…`) que essie.es publica como `product-id`
  de 11-12 dígitos. Son los envases que se venden aquí: entran con ceros hasta 13 dígitos. En
  iOS el escáner ya los lee así; en Android hace falta el build del escáner (ver NYX).
- Erratas de la web corregidas: "Cl 77491" → CI, "Butul Acetate", "CI 77510/Ferric Ammonium,
  Ferrocyanide" partido por la coma, sinónimos "CI 77891/Titanium Dioxide" → CI 77891.
Scripts: `es_parse.py` (ficha .es), `fr_parse.py` (solo para el contraste), `gen_essie.py`
(agrupación por lista idéntica, nombres por gama enamel/expressie/gel couture) → `essie_merged.json`.

## PEDIDOS POR LAS USUARIAS (de la pestaña "Buscados" de la app)
Esta lista manda sobre cualquier otra: son códigos que alguien ha escaneado de
verdad y no le hemos devuelto nada. **Al empezar cualquier sesión de curación,
mirar PRIMERO este apartado**: si hay códigos sin tachar, van antes que cualquier
marca de la cola. Se curan por orden de demanda. Cuando uno
entre, se tacha aquí y Mariana lo quita de la pestaña (o se quita solo, a partir
de la build 90).

**Desde 2026-09-15 los pedidos también salen del recuento de rutinas** (panel de
datos → "Huecos del catálogo"): productos que la gente ya tiene metidos en sus
rutinas y de los que no tenemos ingredientes. Pesan MÁS que un escaneo suelto:
un escaneo puede ser curiosidad en el lineal, pero algo guardado en una rutina es
un producto que esa persona usa. Van ordenados por cuánta gente lo lleva.

### 2026-09-24 · Davines OI — dos aportaciones de una usuaria — resuelto (versión 2026-09-24d)
Una usuaria subió a mano, sin código, **OI Shampoo** y **OI Hair Oil** de Davines. Se abre la
marca entera (ver su apartado).
- **OI Shampoo**: su lista es idéntica a la oficial. Códigos 280 ml 8004608247630, 90 ml
  8004608247654, 500 ml 8004608294566.
- **OI Oil**: su lista también es la oficial, **la de la web española**. En la versión
  2026-09-24c se dejó fuera porque world.davines.com e incidecoder daban otra más corta (sin
  la fragancia nueva de la gama: Hexamethylindanopyran, Eucalyptus, Acetyl Cedrene, Camphor…).
  La usuaria (amiga de Mariana) confirmó que la sacó de la web de la marca; es.davines.com,
  uk, it y us dan la larga. **La web internacional iba atrasada**, y eso obligó a rehacer toda
  la marca desde la web española (ver su apartado). Entra con 135 ml 8004608247593 y 50 ml
  8004608247609.

### 2026-09-24 · Haruharu Wonder (Corea) — pedido de una usuaria — resuelto (versión 2026-09-24b)
Una usuaria probó tres productos: escaneó el **Black Rice Bakuchiol Eye Cream 20 ml
(8809532221523)**, que salía en Buscados como "está pero sin ingredientes", y subió a mano,
sin código, el **Centella Phyto & 5 Peptide Concentrate Cream** y el **Black Rice
Probiotics Barrier Essence**. Se abre la marca entera desde su web (ver su apartado). Las dos
listas que subió la usuaria son **idénticas** a las oficiales (quitando las concentraciones en
ppm); el catálogo las trae ahora con código: 8809532221790 y recarga 8809532221943 (crema) y
8809532221967 / 8809532222131 (esencia 120 y 30 ml).

### 2026-09-18 · 8411582242320, escaneo sin nombre — identificado, NO entra (sin lista oficial)
| Código | Producto | Resultado |
|---|---|---|
| 8411582242320 | **Asevi Vinagre de Limpieza con Detergente Limón, pistola 750 ml** (Asevi Home Brands S.L., Xàbia; prefijo 8411582 = Asevi). Identificado por `gtin13` en ladrogueria.com y ancar3.com; la foto de la tienda enseña el frontal ("Multiusos y cristales"), no la lista | **NO entra (regla 2-bis).** Producto de limpieza → método 648/2004. Asevi sí publica listas Anexo VII completas por EAN (`asevicompany.com/fichas/listado_ingredientes/<EAN>.pdf`, 203 fichas), pero **este código no está entre ellas** y ninguna de las 203 es un vinagre; la ficha del producto en la web no trae ingredientes. Sin lista oficial, fuera. Si Asevi la publica algún día, o Mariana manda foto de la etiqueta trasera, se hace la ficha y se abre la marca |

**Asevi como marca**: curada entera el 2026-09-21 desde ese portal (ver su apartado en la lista de marcas).

### 2026-09-17 · Fotos de Mariana: Elvive Total Repair 5 700 ml, Elvive Hidra Hialurónico mascarilla, Neutrogena Clear & Defend — versiones 2026-09-17a/b/c
| Código | Producto | Resultado |
|---|---|---|
| ~~3600523823710~~ | **L'Oréal Paris Elvive Total Repair 5 Champú Reparador 700 ml** (botella eco-diseñada rellenable; EAN y lista legibles en la foto; F.I.L. Z70072368/1) | **ENTRA en L'Oréal Paris como ficha aparte.** La etiqueta lleva 40 ingredientes: los 35 de la ficha del champú de 250 ml (3600521704424) **más cinco componentes del perfume** (Pinene, Carvone, Geranyl Acetate, Tetramethyl Acetyloctahydronaphthalenes, Citrus Limon Peel Oil). Perfume reformulado con otro F.I.L.: lista distinta, entrada distinta (regla 4), sin tocar la del 250 ml |
| ~~3600524030797~~ | **Elvive Hidra Hialurónico Mascarilla Hidratación Intensa 310 ml** (foto de Mariana; F.I.L. Z70069499/2) | **Ya estaba, pero con otra lista: se SUSTITUYE por la de la etiqueta.** La ficha de loreal-paris.es daba la fórmula anterior (Distarch Phosphate, Quaternium-87, Dimethicone, CI 60730, "72H"); el tarro actual ("100h", Stearamidopropyl Dimethylamine, CI 17200/CI 42090, Coco-Betaine, 26 ingredientes) es una reformulación con el mismo EAN: va la vigente (regla 2) |
| ~~3574661332505~~ | **Neutrogena Clear & Defend Exfoliante Facial 150 ml** (tubo UK/nórdico, foto de Mariana; PR-017564) | **ENTRA en Neutrogena.** No está en neutrogena.es; **neutrogena.co.uk** tiene la ficha con el mismo EAN (`data-mm-ids`) y el mismo PR-017564, 22 ingredientes, y coincide con lo legible de la etiqueta (la foto tiene brillos sobre tres nombres). Truco nuevo: la web británica usa el mismo marcado que la española |
| ~~8057587040952~~ | **Philip Martin's Maple Aqua Rinse Mascarilla Hidratante 200 ml** (Philip Martin's srl, Altavilla Vicentina; foto de la etiqueta de Mariana, EAN y lista legibles) | **ENTRA como marca nueva Philip Martin's** (versión 2026-09-17c) con los 19 ingredientes de la etiqueta. philipmartins.it (Wix) no publica el INCI completo, solo los activos, y remite al envase; el EAN sí aparece en el HTML de la ficha hermana Maple Aqua Wash |

### 2026-09-25 · Segunda cola de marcas + revisión de falsos positivos y negativos por marca

**Regla nueva para TODAS las marcas a partir de ahora:** al cerrar una marca, pasar el detector
de la app por sus fichas y revisar (1) **falsos positivos**: reglas que saltan por un nombre
dentro de otro nombre (el patrón Toluene-2,5-Diamine / Phenylethyl Resorcinol / Polyester-1 /
Methyl Nonyl Ketone), por una categoría equivocada o por un alias demasiado corto; (2) **falsos
negativos**: sustancias con evidencia de disrupción endocrina que estén en las fichas y ninguna
regla reconozca (nombres INCI que faltan como alias, como pasó con Hexamethylindanopyran).
Cada corrección se aplica en la app con la regresión del catálogo entero (cero cambios no
intencionados) y se anota aquí; las decisiones de criterio (riesgo, entra o no) se dejan
escritas para Mariana, como las cuatro de Asevi.

**Orden de la cola** (después de lo pendiente de Buscados y de los huecos de Datos):

1. ~~**Endocare** y **ampliar Heliocare** (Cantabria Labs, mismo portal que Biretix).
   **Ampliar Head & Shoulders** (P&G, mismo circuito que Pantene).~~ — **hecho el 2026-09-25**:
   Endocare 4 códigos (versión 2026-09-25a); Heliocare y Head & Shoulders sin fuente para
   ampliar. Ver sus apartados.
2. ~~**Higiene íntima y menstrual**: Evax, Tampax, Ausonia, Lactacyd, Chilly.~~ — **hecho el
   2026-09-25** (versión 2026-09-25b): 48 códigos y la ficha 34 ya salta; ver su apartado. Es la categoría
   propia de Nura y la única regla específica (fragancia en compresas/tampones, ficha 34) no
   tiene todavía ningún producto que la dispare. Ojo: compresas y tampones no llevan INCI
   cosmético; curar lo que el fabricante publique (composición, "con perfume"/"sin perfume").
3. ~~**Embarazo y bebé**: Mustela (publica INCI completo), Nenuco, Suavinex.~~ — **hecho el
   2026-09-25** (versión 2026-09-25c): Mustela 58 códigos, Nenuco 3, Suavinex sin fuente.
4. **The Ordinary** (INCI completo en su web, fichas cortas). — **preparada el 2026-09-25, sin
   aplicar**: sus códigos son UPC `0769915…` (regla 3); espera la decisión D.
5. **Súper de cada semana**: Babaria, Byphasse, Lactovit, Vaseline; capilar TRESemmé, Gliss,
   Syoss (Unilever y Henkel publican INCI); maquillaje Catrice y Essence (Cosnova publica
   INCI); dental Oral-B y Lacer; limpieza Bosque Verde y KH-7 (método 648/2004, como Asevi).
   — **Catrice y Essence hechas el 2026-09-25** (versión 2026-09-25e): 677 + 740 códigos; ver
   su apartado. Siguen Babaria, Byphasse, Lactovit, Vaseline, TRESemmé, Gliss, Syoss, Oral-B,
   Lacer, Bosque Verde y KH-7. **Vaseline, TRESemmé y Gliss hechas** (versión 2026-09-25f:
   29 + 18 + 29 códigos); Syoss sin fuente válida. **Oral-B y Lacer hechas** (versión 2026-09-25g: 7 + 68).
   **KH-7 y Bosque Verde hechas** (versión 2026-09-25h: 10 + 16).
6. **Deliplus** sigue siendo el hueco más grande (16 fichas): ampliar desde la etiqueta cuando
   Mariana pueda ir a un Mercadona; Bosque Verde en el mismo paseo.

#### Registro de la revisión de falsos positivos y negativos (herramientas y cambios)
Herramientas (scratchpad): `revisa.mjs <marca>` lista, por cada aviso, **qué ingrediente de la
ficha lo dispara** (para ver nombres dentro de otros nombres) y qué ingredientes de una **lista
de vigilancia** de posibles disruptores (listas SCCS/UE, ECHA, TEDX) no reconoce ninguna regla;
`reg.mjs` + `regdiff.py` sacan los avisos de las ~2.900 fichas con la categoría que pone la app
y comparan antes/después de cada cambio (disruptores, "otros" y "otros riesgos").

- **2026-09-25 · Ésteres de propilenglicol y acetatos de (iso)eugenilo** (visto al revisar
  Davines). "Propylene Glycol Dicaprylate/Dicaprate" y "Propylene Glycol Stearate" son ésteres,
  no el propilenglicol humectante de la ficha 38; "Eugenyl Acetate" e "Isoeugenyl Acetate"
  saltaban como Eugenol (207) e Isoeugenol (206) por la tolerancia a erratas. Añadidos a
  `excluyeSi` (38: 17 ésteres de PG; 206 y 207: los acetatos). Regresión: **46 fichas pierden
  un aviso falso (38 ×28, 206 ×14, 207 ×4), ninguna pierde uno verdadero** (comprobado ficha a
  ficha: ninguna de las 46 lleva el propilenglicol, eugenol o isoeugenol sueltos), ningún otro
  cambio.
- **2026-09-25 · Ficha 34 (fragancia en compresas/tampones) sin disparador.** Falso negativo de
  diseño: ver "Higiene íntima y menstrual". Regresión: 0 cambios en las fichas existentes.
- **2026-09-25 · Falso negativo con decisión pendiente: polietileno** (98 cosméticos). Ver la
  decisión B en "Higiene íntima y menstrual".
- **2026-09-25 · KH-7 y Bosque Verde: categoría y un nombre dentro de otro.** (1) 9 fichas de
  limpieza caían en Cuidado personal porque la app no conocía "multisuperficie", "limpiador de
  cocinas"/"cocinas limpiador", "limpia mopas", "limpiador de muebles", "disuelve manchas" ni
  "vela perfumada/aromática"; añadidos a los términos inequívocos de Hogar, junto con las dos
  marcas (`bosque verde`, `kh-7`), que solo hacen limpieza. (2) "Naftaleno 2-etoxi-"
  (2-etoxinaftaleno, nerolina, un componente de perfume) saltaba como Naftaleno (IARC 2B): añadidos
  el etoxi- y el metoxinaftaleno a su `excluyeSi` ("Naphthalene" suelto sigue saltando, probado).
  Regresión: **10 cambios, todos en las 24 fichas nuevas de KH-7 y Bosque Verde** (9 pasan a Hogar,
  con lo que 4 ganan el aviso de alcoholes etoxilados, que es solo de Hogar; la vela Neroli pierde el
  falso Naftaleno); ninguna ficha de otra marca cambia.
- **2026-09-25 · Decisiones B y C de Mariana aplicadas.** (B) La ficha 191 pasa a llamarse
  "Microplásticos (poliéster / polipropileno / polietileno)" y reconoce además polyethylene,
  polietileno, polyethylene terephthalate (PET, purpurina), polyolefin(s) y poliolefina(s);
  "Polyethylene Glycol", "polietilenglicol" y "Polyethylene Oxide" (solubles, no son plástico
  sólido) van a `excluyeSi`. (C) Ficha nueva **211 "Aceites esenciales de lavanda y árbol del
  té"**, riesgo Emergente, solo coincidencia exacta con los nombres de los aceites (Lavandula
  angustifolia/officinalis/hybrida oil con y sin el nombre común, "Lavandula Oil/Extract",
  lavender/lavandin oil, Melaleuca alternifolia (tea tree) leaf oil, tea tree oil y sus nombres en
  castellano). No saltan los extractos ni el agua floral (lo decidido fueron los aceites), ni
  Salvia lavandulifolia ni Melaleuca viridiflora (niaulí). Regresión sobre las 4.261 fichas: **188
  cambian y las 188 son las previstas**: 147 ganan la 191 (polyethylene 128, PET 15, oxidized
  polyethylene 9, poliolefinas 2; NYX 62, Catrice 24, L'Oréal Paris 16, essie y Maybelline 10,
  Avène 8, Vaseline 4, A-Derma 3, Asevi, Klorane y LRP 2, Dove, Ducray, Evax y Garnier 1 — Evax
  Liberty por "poliolefinas") y 41 ganan la 211 (Davines 12, Nivea 7, Cosmia 5, Cocunat y
  Haruharu 4, Asevi, Catrice y L'Oréal Paris 2, Deliplus, Freshly y SkinCeuticals 1). Ningún
  otro cambio, ninguna ficha pierde avisos. **Pendiente de criterio (siguiendo el principio de
  Mariana, "si es microplástico, que figure"):** otros polímeros sólidos que la restricción UE
  2023/2055 también cuenta como microplásticos, sobre todo **Nylon-12/Nylon-6** y **Polymethyl
  Methacrylate** (maquillaje) y los poliuretanos en polvo; no se han añadido sin preguntar.
  Números en el catálogo: Nylon-12 79, Methyl Methacrylate Crosspolymer 26, Nylon-611 15,
  Polymethyl Methacrylate 12, Polyurethane-11/-35 y otros ~30, Nylon-6 3.
- **2026-09-25 · Catrice y Essence: dos nombres dentro de otro nombre.** "Propylene Glycol
  Dibenzoate" (7 fichas de essence) saltaba como Propilenglicol (38): es un éster, mismo criterio
  que los 17 ésteres de arriba. "Phosphoric Acid Polyester" (15 esmaltes UV Gel de essence)
  saltaba como Microplásticos (191) por la palabra "polyester": es una resina líquida del esmalte
  de gel que se cura en película, no una fibra ni una partícula; mismo caso que "poliéster
  modificado". Añadidos a `excluyeSi` de la 38 y de la 191. Regresión sobre las 4.153 fichas:
  **22 cambian (38 ×7, 191 ×15), todas por estas dos frases; ninguna lleva además propilenglicol
  o poliéster sueltos** ("Aliphatic Polyesterurethane Acrylate" de los mismos esmaltes ya no
  saltaba); ningún otro cambio.

### 2026-09-23 · Cola de marcas para la campaña de Instagram (decisión de Mariana)

Mariana está haciendo publicidad y quiere que el **primer escaneo** de quien llega acierte.
Orden, después de lo pendiente de Buscados:

1. ~~**Pantene, Head & Shoulders y Herbal Essences** (P&G)~~ — **hechas el 2026-09-23**
   (versión 2026-09-23b): 18 + 6 + 9 códigos, más Aussie (10) de la misma fuente. No fue
   por info-pg.com (solo detergentes) sino por haircode.es, la web capilar oficial de P&G
   España, que lleva EAN e INCI en cada ficha. Ver su apartado.
2. ~~**Freshly Cosmetics y Cocunat.**~~ — **hechas el 2026-09-23** (versión 2026-09-23c):
   Freshly 11 códigos (la web da INCI pero no EAN; EAN por Douglas, emparejado por lista) y
   Cocunat 39 (el HTML no lleva INCI; sale de la API de la marca con `gtin`). Ver sus apartados.
3. ~~**Heliocare**~~ — **hecha el 2026-09-23**: solo 5 códigos con dos fuentes idénticas;
   Cantabria Labs no publica INCI y las fuentes reflejan reformulaciones. Ver su apartado.
4. Cuando Mariana pueda ir a un Mercadona con el móvil: **ampliar Deliplus** desde la
   etiqueta (hoy 16 fichas; es el hueco más grande del catálogo).

### 2026-09-23 · Biretix (Cantabria Labs) — marca nueva, aportación de una usuaria — resuelto el 2026-09-23 (versión 2026-09-23a)

**Resultado: el código NO es el spray, es el Cleanser.** Open Beauty Facts tiene una foto de la
etiqueta trasera de 8436574361599 (subida por una usuaria, lote 10/2024) con el EAN impreso y
el nombre "Biretix Cleanser Gel Limpiador Purificante 200 ml"; Douglas y SkinLovers dan el
mismo EAN para el Cleanser 200 ml. La lista que pegó la usuaria es la del **Tri-Active Gel**
(idéntica a incidecoder y SkinLovers, con Polyquaternium-10; la del spray lleva Heptyl
Glucoside en su lugar). Es decir: código de un producto, lista de otro. **La aportación manual
aprobada con esa lista está mal para ese código**: al importar Biretix desde la app, la ficha
del catálogo la sobreescribe (la importación por marca hace merge sobre `ingredientesTexto`).
Entra con la lista de la etiqueta. Biretix abierta como marca: ver su apartado.


| Código | Pista | Qué hacer |
|---|---|---|
| 8436574361599 | "Biretix" · prefijo **8436574 = Cantabria Labs** (Industrial Farmacéutica Cantabria). Lista pegada por una usuaria desde una web, con traducciones y porcentajes: Alcohol Denat. 2º, Glycolic Acid 15 %, Niacinamide 5 %, Salicylic Acid 2 %, Retinol + Hydroxypinacolone Retinoate (RetinSphere), Oligopeptide-10 (BIOPEP-15), Boswellia, BHT y BHA | Por el alcohol en 2ª posición y el trío glicólico/salicílico/RetinSphere, casi seguro **Biretix Tri-Active Spray anti-imperfecciones** (formato cuerpo/espalda). Verificar en biretix.com / cantabrialabs.es, confirmar nombre y formato con el EAN, y **abrir Biretix como marca**: la gama es corta (Duo, Tri-Active gel y spray, Cleanser, Hydra, Mask, Isorepair) y Cantabria Labs publica el INCI completo. Mariana aprueba mientras tanto la aportación con la lista limpia |

Lista limpia (sin traducciones ni porcentajes, para comparar con la oficial): Aqua, Alcohol
Denat., Glycolic Acid, Niacinamide, Propylene Glycol, Salicylic Acid, Ammonium Hydroxide,
Polyquaternium-10, Retinol, Hydroxypinacolone Retinoate, Oligopeptide-10, Oryza Sativa Bran
Extract, Boswellia Serrata Extract, Honey Extract, Butylene Glycol, Ethylhexylglycerin,
Tetrasodium EDTA, Pentylene Glycol, Palmitoyl Hydroxypropyltrimonium Amylopectin/Glycerin
Crosspolymer, Dimethyl Isosorbide, 1,2-Hexanediol, Polysorbate 20, Caprylyl Glycol,
Hydrogenated Lecithin, BHT, BHA.

### 2026-09-21 · Decisiones de criterio sobre las cuatro sustancias de Asevi (para aplicar en la app)

Decididas con los números del catálogo entero (2.355 fichas): DDAC 24 fichas de Hogar y
0 de cosmética · TBHQ 4 y 0 · TBOEP 1 y 0 · alcoholes -eth sin laureth **81 de Hogar y 340
de cosmética**. Tres entran como disruptor Emergente; la cuarta va a "otros" y solo Hogar.

**a) DDAC → ya existe: ficha 198. No crear otra. Solo le falta el alias INCI.**
Asevi escribe `Didecyldimonium Chloride` y la 198 solo conocía `didecyldimethylammonium
chloride`. Sustituir estos campos en la 198 (riesgo Emergente se queda):
- aliases: `Didecyldimonium Chloride, didecyldimethylammonium chloride, didecyl dimethyl ammonium chloride, DDAC, cloruro de didecildimetilamonio`
- dondeSeEncuentra: `Desinfectantes de superficies y sanitarios, suavizantes y perfumadores de ropa con efecto higienizante, toallitas y limpiadores antibacterianos.`
- mecanismo: `Amonio cuaternario ('quat'), de la misma familia que el cloruro de benzalconio. La señal viene de estudios en ratón con una mezcla de los dos (ADBAC + DDAC): menos camadas, menos ovulación y menos espermatozoides. En rata, un estudio de varias generaciones no vio efecto hasta dosis muy altas. No está claro cuánto de ese efecto es del DDAC solo, ni si ocurre con la exposición doméstica normal.`
- evidencia: `Melin et al. 2014 y 2016 (ratón, mezcla ADBAC+DDAC); estudio multigeneracional en rata sin efecto hasta 1500 ppm. Sin clasificación como disruptor endocrino en ECHA; en la UE está regulado como biocida.`
- alternativa: `Para limpieza diaria, jabón o detergente y agua. Reservar los desinfectantes con 'quats' para cuando haga falta desinfectar de verdad, y ventilar y aclarar después.`
Comprobación: 24 fichas de Hogar (Asevi + Sanytol), 0 de cosmética.

**b) TBHQ → disruptor, Emergente. Ficha nueva.**
- nombre: `TBHQ (terc-butilhidroquinona)` · categoria: `Hogar` (sin soloCategoria: también E319 en alimentación y en labiales)
- aliases: `tert-Butylhydroquinone, TBHQ, E319, t-butylhydroquinone, tertiary butylhydroquinone, mono-tert-butylhydroquinone` · cas: `1948-33-0` · riesgo: `Emergente`
- dondeSeEncuentra: `Antioxidante sintético: detergentes, fregasuelos y quitamanchas (evita que las grasas y perfumes se oxiden); en alimentación como E319 en aceites, snacks y grasas; en algunos labiales y bálsamos.`
- mecanismo: `En cribados de células (ToxCast) muestra una actividad hormonal muy débil, estrogénica y androgénica, y en células de mama reduce el receptor de estrógenos en presencia de estradiol. No hay estudios en animales que confirmen un efecto hormonal. Es una señal de laboratorio, no una evidencia de daño.`
- evidencia: `Cribados ToxCast/Tox21 (in vitro); estudios en células MCF-7 y T-47D. EFSA (E319) no señala preocupación endocrina; ingesta diaria admisible de 0,7 mg/kg.`
- alternativa: `Productos con antioxidantes naturales declarados: tocoferol (vitamina E), extracto de romero.` · fuente: `ToxCast · EFSA (E319)`
Comprobación: 4 fichas de Asevi, 0 de cosmética.

**c) TBOEP → disruptor, Emergente. Ficha nueva** (misma familia que TPHP 79 y TCEP 132; dejarlo fuera rompe la coherencia, y es de los organofosforados más detectados en polvo doméstico).
- nombre: `Fosfato de tris(2-butoxietilo) (TBOEP)` · categoria: `Hogar`
- aliases: `Tris(2-butoxyethyl) phosphate, TBOEP, TBEP, Tributoxyethyl phosphate, tris(2-butoxyethyl)phosphate` · cas: `78-51-3` · riesgo: `Emergente`
- dondeSeEncuentra: `Abrillantadores y ceras de suelos, plásticos flexibles (PVC), algunas espumas. Se acumula en el polvo de casa.`
- mecanismo: `Organofosforado usado como plastificante y retardante de llama. En pez cebra y en ensayos celulares altera las hormonas tiroideas y el desarrollo temprano. En mamíferos los datos son escasos y no permiten sacar conclusiones.`
- evidencia: `Estudios en pez cebra y ensayos in vitro; biomonitoreo en polvo doméstico y orina (uno de los organofosforados más detectados). Sin clasificación como disruptor endocrino en ECHA.`
- alternativa: `Abrillantadores sin fosfatos orgánicos; limpiar el polvo con paño húmedo y ventilar, que es por donde entra la mayor parte de la exposición.` · fuente: `Estudios en pez cebra · biomonitoreo`
Comprobación: 1 ficha (el abrillantador), 0 de cosmética.

**d) Alcoholes etoxilados -eth → NO entra en disruptores. Entra en OTROS_INGREDIENTES, solo Hogar.**
Ampliar la 192 marcaría 340 fichas más de cosmética (14% del catálogo) por una preocupación que
no es endocrina (1,4-dioxano, IARC 2B) y que en cosmética está controlada; ceteareth-20 va al
1-3% como emulsionante. En un detergente, en cambio, el Pareth/Trideceth es el tensioactivo
principal. "Otros a tener en cuenta" no puntúa: coherencia sin inflar el IEH. La 192 (laureth)
se queda como está.
- nombre: `Alcoholes etoxilados (pareth, trideceth, deceth…)` · soloCategoria: `Hogar`
- aliases: `pareth, trideceth, deceth, undeceth, oleth, ceteareth, steareth, ceteth, alcohols ethoxylated, alcohol ethoxylate, alcoholes etoxilados`
- nota: `Tensioactivos fabricados por etoxilación, que puede dejar trazas de 1,4-dioxano (posible cancerígeno, IARC 2B) que no aparecen en la etiqueta. No es un disruptor endocrino y no cuenta para tu índice; se lista porque en un detergente son el ingrediente principal. El laureth, el más estudiado, sigue en su propia ficha.`
Comprobación: ~81 fichas de Asevi en "otros"; la cosmética no cambia ni un aviso.

**Descartados, de acuerdo:** OTNE, metanol, 2-butoxietanol, xileno, DBNPA, IPBC.

Al aplicar: barrer el catálogo entero y confirmar los cuatro números de comprobación. Cero
cambios en cosmética salvo los indicados.

**Aplicado el 2026-09-21** (app, rama claude/redesign-v2-wqk1cj). Barrido de las 2.355 fichas
con la categoría que asigna la app: DDAC **24 de Hogar (20 Asevi + 4 Sanytol) y 0 de cosmética** ·
TBHQ **4 y 0** · TBOEP **1 y 0** · alcoholes -eth en "otros" **90 de Hogar y 0 de cosmética**
(81 con nombre INCI -eth y 9 que Asevi escribe "Alcohol graso etoxilado", incluido como alias;
sin ese alias son los 81 previstos). Ninguna ficha de cosmética cambia un solo aviso de
disruptor. De paso se vio que tres cosméticos caían en Hogar por una palabra del nombre
(pintalabios NYX tono "Laundry Day", stick Maybelline "Multiusos", coloración L'Oréal "sin
amoniaco"): corregido en `guessCategoria` (maquillaje, labiales y tintes no cuentan como
limpieza); la coloración pasa a mostrar su nota de sulfitos como alérgeno de contacto, que
es lo correcto. Hace falta build para que llegue a las usuarias.

### 2026-09-16 · Huecos de marcas que YA tenemos + dos patrones nuevos

Salen del panel de datos de la app (recuento de rutinas + escaneos en vacío), ya
cruzado con las aportaciones aprobadas a mano: lo que Mariana ya resolvió por
nombre (crema de pies de Cien, sérum de camomila Deliplus) NO está aquí.
Identificación **solo por prefijo GS1 y por lo que ya hay en el catálogo**; esta
sesión no tiene salida a internet: verificar producto a producto.

**Primero los tres huecos de marcas hechas.** No son marcas nuevas: son fichas o
códigos que faltan dentro de marcas ya curadas. Es lo más barato de la lista.

| Código | Pista | Qué hacer |
|---|---|---|
| 8718951735163 | "Saner zero" (mal leído) · prefijo **8718951 = Colgate-Palmolive**, el de los 14 códigos de Sanex | **Sanex Zero%.** Ya está curado el *Desodorante roll-on Zero% sin aluminio* (8718951246874). Esto es otro formato de la gama: gel de ducha Zero% o el desodorante en otro tamaño/variante. Si el INCI coincide con una ficha que ya tenemos, es añadir el código; si no, ficha nueva |
| 3574661177229 | "intense repair" · prefijo **3574661 = Neutrogena** | **Fórmula Noruega Reparación Intensa** en envase en inglés. Ya hay tres fichas de la gama: Bálsamo Cica (3574661032436), Crema de Pies Talones Agrietados (3574661255903), Loción Corporal Cica (3574660533408). Casi seguro es una de ellas en otro formato: identificar cuál y añadir el código |
| 8700216234955 | "Fairy Platinum Quick Wash" · prefijo **8700216 = Fairy** (ya tenemos 8700216460781 y 8700216601146) | **Lavavajillas a MÁQUINA**, gama nueva: las 6 fichas de Fairy son todas a mano. Método de PRODUCTOS DE LIMPIEZA (Reglamento 648/2004 Anexo VII, no hay INCI completo por ley) |

**Patrón 1 · Pastillas de lavavajillas, dos usuarias distintas.** Además del Fairy
Platinum, `8436617752667` "Pastilhas para a máquina de loiça" (prefijo español
8436617, empresa sin identificar, etiqueta en portugués). No tenemos NINGUNA
pastilla de lavavajillas y lo han pedido dos personas por separado. Vale la
pena cubrir el tipo de producto, no solo esos dos códigos.

**Patrón 2 · Productos de un viaje a Francia.** `3560071172015` "Dentifrice
fraîcheur", prefijo **3560071 = Carrefour Francia** (marca blanca). Con el
nettoyant désinfectant y el Elmex son tres de la misma usuaria, que vive en
España/Portugal y los trajo de viaje. Prioridad BAJA: cuando se le acaben,
comprará aquí.

**Patrón 3 · Suplementos deportivos, sin código.** "Prozis peanut butter" (2
personas) y "My protein vegan unflavoured" (2). Los escribieron a mano, así que
no hay EAN. Las reglas de ingredientes ya cubren nutrición deportiva; lo que
falta son los productos. Prozis y Myprotein publican la lista completa en su
web. Decisión de Mariana si se abren como marca; apuntado como demanda.

**Erborian · Super BB Concealer (aportación manual, sin código).** Una usuaria
subió el INCI completo desde el tubo (formato L'Occitane, con guiones y
`CI 77891/TITANIUM DIOXIDE`) y Mariana lo aprueba por nombre. Falta el EAN:
buscarlo (erborian.com, Sephora, OBF; prefijo francés 3760…) y verificar el INCI
contra la ficha oficial. Si cuadra, abrir **Erborian** como marca con esta ficha
y su código: así el escáner lo encuentra por código y no solo por nombre. El INCI
que subió la usuaria pasa limpio por el detector (sin parabenos, fenoxietanol,
perfume ni siloxanos cíclicos).

**Resultado 2026-09-16 (versión 2026-09-16b): ENTRA, marca nueva Erborian, EAN 8809255788167.**
- El prefijo no es francés: Erborian fabrica en Corea y todos sus códigos son `8809255…`
  (los 8 de OBF también). El EAN lo da **Douglas España** (`/api/v2/products/1171943?fields=FULL`:
  campos `ean`, `ingredients` y `variantCount`); Douglas confirma que es **un solo tono** (10 ml).
- **Todas las webs de Erborian (es, fr, uk, it) están tras DataDome** con desafío interactivo
  que Playwright no pasa; erborian.com internacional responde pero no tiene fichas. Sephora,
  Primor, Druni, Notino, Promofarma, Atida y El Corte Inglés bloquean o no lo listan.
- INCI: Douglas (traducido al español, con guiones, formato L'Occitane) e **incidecoder** (en
  inglés) dan los **mismos 38 ingredientes**; solo cambian dos parejas adyacentes de orden
  (Synthetic Fluorphlogopite/Lauryl PEG-8 Dimethicone y Propanediol/Triethoxycaprylylsilane).
  Se guarda en inglés con el orden de Douglas, que es el del envase. Mariana: compara con la
  aportación de la usuaria; si el tubo da el otro orden, se cambia en un minuto.

~~**Sigue igual:** Cosmia (Alcampo) como marca, por nombre e INCI de alcampo.es,
nunca por el código interno 20525101.~~ — **hecho el 2026-09-25**: 115 códigos (EAN de Alcampo +
composición de auchan.fr); ver su apartado.

**NO curar sin que Mariana lo decida:** `91598271` VICKS VapoRub es un
**medicamento**, no un cosmético (sin INCI, fuera del reglamento cosmético). Está
abierto si Nura analiza medicamentos o los deja fuera.

**Resultado 2026-09-16 (versión 2026-09-16a): 4 entran (2 huecos + 2 marcas nuevas), 1 fuera, 1 sin curar por decisión.**
Identificación por la foto de OBF de cada código y contraste con la web oficial.

| Código | Qué es de verdad | Resultado |
|---|---|---|
| ~~8718951735163~~ | **Sanex Zero% Extra Control roll-on 50 ml** (envase ES/IT/EL/PT, fabricado en Świdnica; etiqueta legible en OBF) | **ENTRA en Sanex como ficha nueva.** No es el Zero% Invisible/Men que ya está (8718951246874): la etiqueta lleva **Ethylhexylglycerin y Zinc Oxide y no lleva Dimethicone**. La ficha de sanex.es "Zero% Extra Control" da Dimethicone y sin Ethylhexylglycerin: **manda la etiqueta del mismo código** (como con Hydro Oil de ISDIN). Nombre: *Desodorante roll-on Zero% Extra Control 50 ml* |
| 3574661177229 | **Neutrogena Intense Repair baume corps réparation intense 300 ml** (tarro francés "maxi format", foto de OBF de 2018) | **FUERA, dos motivos.** (1) **Descatalogado**: neutrogena.fr solo lista ya Réparation Intense CICA Lait y CICA Crème, y el tarro de 2025 con el mismo aspecto (3574661821252, 400 ml) es la Cica Creme con otra fórmula (la de la Loción Cica). (2) La foto de la etiqueta tiene el borde izquierdo cortado: "…tearyl Alcohol" puede ser Stearyl o Cetearyl, y no se adivina (regla 2). No es ninguna de las tres fichas de la gama: es la fórmula anterior a Cica (Paraffinum Liquidum, Petrolatum, Synthetic Beeswax) |
| ~~8700216234955~~ | **Fairy Platinum QuickWash 520 ml, lavavajillas A MANO** (envase griego; la etiqueta dice "líquido para lavar platos" y lleva Lauramine Oxide y sulfatos) | **ENTRA en Fairy.** Corrección a la pista: no es de máquina. P&G tiene **una sola ficha "Platinum - QuickWash"** (a mano, `pa 90108185001`) y el nombre del envase casa con ella: entra por la regla de Fairy. La etiqueta (Anexo VII resumido) es coherente con la ficha: Benzisothiazolinone, Phenoxyethanol, Hexyl Cinnamal, Linalool |
| ~~8436617752667~~ | **Natulim Eco Pastillas Lavavajillas Máquina 6 en 1, 30 pastillas** (Ecollim Holdings, EU Ecolabel; caja ES/PT) | **ENTRA como marca nueva Natulim.** La caja solo da los rangos del Anexo VII, pero **natulim.com publica la lista completa** en la ficha del producto (FAQ "¿Cuáles son los ingredientes?", 23 componentes en orden: carbonato, citrato y percarbonato de sodio, agua, alcoholes grasos etoxilados, TAED, ácido poliepoxisuccínico, copolímero itacónico, sulfato de sodio, alcohol polivinílico, PEG-90, subtilisina, celulosa, caolín, citrato de bismuto, goma de celulosa, dextrina, carbonato de calcio, alfa-amilasa, sulfato de magnesio, tiosulfato de sodio, polietilenglicol, sacarosa). Es el único producto de pastillas de la marca, así que la ficha es de este envase. Se guarda con los nombres en inglés (como Fairy) para que el detector los reconozca |
| ~~3560071172015~~ | **Carrefour Soft Bio Dentífrico Frescor con agua de menta 75 ml** (fabricado en España; COSMOS Organic) | **ENTRA como marca nueva Carrefour.** Mismo EAN con dos etiquetas en OBF: la de 2020 (con fosfatos) y la de **mayo de 2026** (reformulado: Sodium Citrate, Menthol, Mentha Piperita Oil, Anethole, Eucalyptus, Pinene, Beta-Caryophyllene). Reformulación con el mismo código → va la vigente (regla 2). carrefour.fr y carrefour.es están tras Datadome/Cloudflare y no se pueden consultar |
| 91598271 | VICKS VapoRub | **No se cura** hasta que Mariana decida lo de los medicamentos |

Patrón "pastillas de lavavajillas": cubierto por Natulim. Las de Fairy (Platinum All in One y
Platinum Plus) siguen fuera por lo de siempre: P&G tiene dos y tres fichas con nombres casi
iguales para el mismo envase y OPF no permite decidir (ver Fairy).
De paso: OBF tiene con etiqueta legible de 2025 el **Neutrogena Intense Repair Cica Creme cara y
cuerpo 400 ml** (3574661821252, 13 ingredientes, sin perfume), que es la "Réparation Intense CICA
Crème Multi-Usages" francesa. No se ha añadido porque no está en neutrogena.es; si aparece en
Buscados, es un minuto.

### 2026-09-15 · 4 escaneos en vacío — tres son productos comprados en un viaje

De la sección "Escaneos en vacío" del panel: productos que alguien escaneó y se
guardaron sin ingredientes. Los cuatro tienen dígito de control válido y **ninguno
está en el catálogo**. Lo que dicen en conjunto importa más que cada uno por
separado: **tres de los cuatro son de fuera de España** — dos con nombre en
francés y uno con prefijo suizo. **Corrección de Mariana (16-09):** la app solo se
vende en España y Portugal; esa usuaria no vive en Francia, viajó allí y trajo
productos. Son compras puntuales, no demanda que vaya a repetirse: prioridad
BAJA frente a lo que se compra aquí cada semana.

Identificación por prefijo GS1, **sin confirmar en ninguna base** (la sesión que
escribe esto no tiene salida a internet): hay que verificar producto a producto.

| Código | Pista | Qué hacer |
|---|---|---|
| 8718951058446 | "Dentifrice anti-caries" · prefijo **8718951 = Colgate-Palmolive**, el MISMO que los 16 códigos de Colgate y los 11 de Sanex que ya están curados | **EL MÁS BARATO DE TODOS, empezar por aquí.** No es una marca nueva: es un hueco dentro de una marca que ya tenemos. Un dentífrico Colgate de envase francés (probablemente la gama "Protection Caries"). Si su INCI coincide con una ficha que ya tenemos, es añadir un código |
| 7610108024513 | "Elmex" · prefijo **761 = Suiza**. Elmex es de CP GABA, **también del grupo Colgate-Palmolive** | Dentífrico. Marca nueva pero del mismo grupo que lo que ya se cura. Segundo en orden de coste |
| 3045206392976 | "nettoyant desinfectant" · prefijo **30-37 = Francia** | Producto de LIMPIEZA, no cosmética (ver nota de abajo). Si resulta ser Sanytol francés, enlaza con la tarea pendiente del portal REACH de AC Marca. Aplicar el método de PRODUCTOS DE LIMPIEZA (Reglamento 648/2004 Anexo VII), que no da INCI completo |
| 5059883116631 | "Brownie Chocolate Chunk" · prefijo **50 = Reino Unido** | Alimentación. La menos prioritaria: un brownie no es un producto de rutina |

**Además, esto destapó un fallo en la app (ya corregido, pendiente de build):** el
"nettoyant désinfectant" se había clasificado como **Cuidado personal**. La
categoría decide qué reglas de ingredientes se aplican, así que un desinfectante
analizado como cosmético da lecturas equivocadas. Eran dos cosas: el texto se
comparaba **con tildes**, así que "désinfectant" no casaba con "desinfectant", y
no había ni una palabra francesa de limpieza en la lista. De paso se arregló que
"champú suavizante" cayera en Hogar por la palabra "suavizante".

**Resultado 2026-09-15 (versión 2026-09-15a): 2 entran (marca nueva Elmex), 2 fuera.**
Identificación por OBF (los cuatro tienen ficha con foto) y contraste con la web oficial.

| Código | Qué es de verdad | Resultado |
|---|---|---|
| ~~8718951058446~~ | **elmex Anti-Caries Professional, pack 2 × 75 ml** (envase francés/belga; OBF trae la caja y la etiqueta legible). No es un Colgate: el prefijo `8718951` lo comparte todo el grupo (Colgate, Sanex, elmex, Palmolive) | **ENTRA** como **marca nueva Elmex**. La etiqueta (14 ingredientes) es **idéntica, en el mismo orden, a la ficha de elmex.es** "Protección caries Profesional". Ojo: elmex.fr ya publica para el mismo producto una **fórmula 2026** distinta (con Xylitol, Hydrated Silica, Xanthan Gum, sin CI 77891) bajo el EAN del tubo suelto 8718951209923; ese código no se añade hasta ver una etiqueta, porque la lista francesa es la explicativa y no está confirmada completa |
| ~~7610108024513~~ | **elmex Protección Caries 75 ml**, envase suizo (DE/FR/IT; OBF con etiqueta legible, 36 revisiones) | **ENTRA** en Elmex con la lista de la etiqueta (15 ingredientes, con los alérgenos del aroma). La ficha de elmex.fr "Anti-Caries Original" da los mismos 8 primeros pero sin alérgenos: la lista explicativa de la web omite, así que manda la etiqueta |
| 3045206392976 | **Sanytol Nettoyant Désinfectant Salle de Bain anti-calcaire 500 ml** ("Formule Protection", sin lejía, 1,5 % de peróxido de hidrógeno; AC Marca Ideal) | **FUERA (2-bis)**. La etiqueta solo da los rangos del Anexo VII ("< 5 % blanqueantes oxigenados, fosfonatos, tensioactivos no iónicos y anfóteros; desinfectante y perfumes"). De las 49 FIC públicas de sanytol.fr ninguna es esta: las dos con peróxido son "Nettoyant Désinfectant 4 Actions Fresh" (código 33632250, 2018) y "Pistolet Multi-Surfaces Protection 4 Actions Fresh" (33639298/308/299, 2021), otros productos. En el portal REACH de AC Marca hay una entrada "SANYTOL BAÑOS FRESH" (`9433632199-B`) que probablemente es esta fórmula, pero está tras login: enlaza con la decisión pendiente del portal (ver Sanytol) |
| 5059883116631 | **Myprotein Protein Brownie Chocolate Chunk 75 g** (OFF, Reino Unido) | **FUERA**: alimentación, no es producto de rutina. No se cura |

Lo que enseña: el prefijo `8718951` no identifica a Colgate sino a todo Colgate-Palmolive Europa,
así que un `8718951…` desconocido puede ser Sanex, Palmolive, elmex o meridol. Y las webs de
elmex traen la lista, pero por GraphQL (ver el apartado de Elmex).

### 2026-09-15 · Cosmia (Alcampo) — primer pedido salido del recuento de rutinas

| Código | Producto | Resultado |
|---|---|---|
| 20525101 | **"Cosmia", sin más** · 1 persona, en una rutina propia | **NO ENTRA POR CÓDIGO, y no es un fallo de búsqueda.** Es un EAN-8 con dígito de control válido pero **prefijo 2: circulación restringida** (código interno de tienda, no registrado en GS1). Dos consecuencias: (1) no va a estar en OBF, incibeauty, go-upc ni en ninguna base global — no gastar tiempo buscándolo; (2) **no es único**: el mismo número puede ser otro producto en otra cadena, así que curarlo como "Cosmia X" arriesga servir la lista equivocada a quien escanee otra cosa. Además el nombre guardado es solo la marca: no sabemos QUÉ producto es. Sin identificar el producto, no entra (regla 1) |

**Lo que sí hay que hacer con esto:** Cosmia es la marca propia de cosmética de
**Alcampo (Auchan)**, y encaja exactamente con lo ya curado de Deliplus
(Mercadona), Cien (Lidl) y Eroski: marca blanca de súper, barata, muy usada y mal
cubierta por las bases públicas. **Añadir Cosmia a la cola como marca**, curando
por nombre de producto e INCI oficial de alcampo.es, nunca por este código.

Cuando entre la marca, este código seguirá sin resolverse solo: hace falta que
alguien diga qué producto es (foto del envase). Mientras tanto se queda aquí sin
tachar.

### 2026-09-13 · 8 códigos de ISDIN escaneados (LA MEJOR OPORTUNIDAD DE LA LISTA)
Los ocho nuevos son de **ISDIN**: seis con prefijo `8429420` y dos con `8470001`, los dos que
ya usan los 18 códigos que tenemos de la marca. Todos con dígito de control válido.
**No son demanda de usuarias: los escaneó Mariana en una farmacia**, recorriendo el lineal. No
significa que nadie los pida, significa algo distinto y muy útil: son los envases que están
HOY a la venta en España.

**Por qué esto vale más que una marca nueva:** de ISDIN ya tenemos el INCI de 252 fichas
descargado de isdin.com. Lo que nos falta desde el principio es el EAN, porque la marca no lo
publica, y por eso la marca se quedó en 16 productos. **Aquí no hay que buscar ingredientes:
hay que averiguar QUÉ producto es cada código y engancharle la lista que ya tenemos.**

**Resultado 2026-09-13 (versión 2026-09-13d): 7 entran (uno nuevo fotografiado en la farmacia), 1 espera la foto de la etiqueta (Scalp & Hair), 1 sin identificar.**
Identificación: el EAN aparece en la URL o la ficha de varias farmacias online independientes
(farma2go, farmaelglobo, farmacianautic, El Corte Inglés, paratamtam, chachifarma…), y la lista que
esas farmacias publican se comparó ingrediente a ingrediente con la ficha de isdin.com.

| Código | Producto | Resultado |
|---|---|---|
| ~~8429420285019~~ | **Eryfotona Night Ultra Fluid 50 ml** | **ENTRA**: la lista de farmaelglobo (30 ingredientes) es idéntica a la de isdin.com |
| ~~8429420291263~~ | **Fotoprotector Fusion Water MAGIC by Alcaraz SPF 50** | **ENTRA**: la lista de farmacianautic (32) es idéntica a la ficha "by Alcaraz" de isdin.com (con Sodium Hyaluronate y Porphyridium), que difiere de la Fusion Water MAGIC normal (30) y del resto de variantes. La pista de la tabla era otra: no es la serie del Invisible Stick |
| ~~8429420329867~~ | **Fotoprotector Facial Mist SPF 50 100 ml** | **ENTRA**: isdin.com solo tiene la ficha de 50 ml; la lista francesa de mapharmacienast para este EAN (40 ingredientes) es la misma traducida, así que entra como tamaño de 100 ml |
| ~~8429420246843~~ | **FotoUltra Spot Prevent Color SPF 50+** | **ENTRA**: todas las farmacias lo dan como la versión COLOR (no la sin color, que es otra ficha) y la lista publicada con el EAN (farmacianautic, chachifarma) coincide con isdin.com. La pista de la tabla (Redness) era otra gama |
| ~~8470001548887~~ | **Nutradeica Gel Crema Facial 50 ml** | **ENTRA**: ficha única en isdin.com; OBF tiene la portada (envase argentino, "Seborrheic skin"); incibeauty y farmavazquez publican con este EAN la misma lista que la web. La pista (Gel Cream SPF30) era otra gama |
| ~~8470001902870~~ | **Fotoprotector Hydro Oil SPF 30 200 ml** | **ENTRA (2026-09-13c) con la lista de la etiqueta que fotografió Mariana en la farmacia** (envase ©2025, EAN visible en la foto): es la generación actual (Coco-Caprylate/Caprate, sin Octocrylene ni 4-MBC), pero **no idéntica a la ficha de isdin.com**: el envase no lleva Diethylhexyl Butamido Triazone y sí Amyl Salicylate, y cambia el orden Arginine/Glycerin. Va la del envase (regla de la generación). Las farmacias que publicaban Octocrylene copiaban la fórmula anterior; la web de ISDIN va una generación por detrás del lineal |
| ~~8429420282087~~ | **Fotoprotector Scalp & Hair Spray SPF 50** | **ENTRA (2026-09-23d)** con la fórmula actual: Douglas ES publica para este EAN la lista de isdin.com (37 ingredientes). Antes: **esperaba la foto de la etiqueta**, mismo caso: parafarmaciacampoamor publica con este EAN la fórmula antigua (18 ingredientes, con Octocrylene, Butane/Propane) y skinsort/dermofarma la actual de isdin.com (37, con Pentaclethra Macroloba y Physalis). Con la etiqueta se decide en un minuto |
| ~~8429420280113~~ (nuevo, fuera de la lista de 8) | **FotoUltra 100 Solar Allergy Protect SPF 50+ 50 ml** | **ENTRA (2026-09-13d)**: Mariana fotografió caja y código en la farmacia; la etiqueta (envase ©2025) es idéntica a la ficha de isdin.com, 35 ingredientes en el mismo orden |
| 8429420084551 | ? | **SIN IDENTIFICAR**: no está en OBF, incibeauty, go-upc, upcitemdb ni en ninguna farmacia indexada. Serie `084…`, muy anterior a todo lo que tenemos: probablemente un envase antiguo o un formato de farmacia (muestra, pack). Hace falta la foto |

### 2026-09-12 · 9 códigos escaneados sin resultado — resueltos 2026-09-12 (versión 2026-09-12b)
Identificación de cada código: OBF (ficha y foto), incibeauty por código, go-upc, y las
tiendas que lo listan. INCI solo con fuente verificable (regla 2); si no, fuera (2-bis).

| Código | Producto | Resultado |
|---|---|---|
| ~~4056489447061~~ | **Cien Desmaquillante bifásico de ojos 100 ml** (OBF: envase FR, foto de la etiqueta legible) | **ENTRA** en Cien, INCI transcrito de la foto de OBF del mismo código |
| ~~4056489817642~~ | **Cien Agua micelar Sensitive 3 en 1 400 ml** (OBF: envase IT con el código en la foto; fabricante Mann & Schröder) | **ENTRA** en Cien, INCI de la foto de OBF |
| 4056489872191 | Cien Crema de manos Aloe Vera 100 ml (envase ES, Persada Belleza, Badajoz) | **FUERA (2-bis)**, segundo intento 12-09: la única foto de OBF es la del código, sin lista; incidecoder no la tiene; incibeauty tiene ficha por código pero está tras Cloudflare interactivo; lidl.es responde 404/"navegador no soportado"; las tiendas que lo listan (eBay, tugexp) dan 403 |
| ~~4335619113749~~ | **Cien Sérum facial Vitamina C Glow 30 ml** (incibeauty lo identifica por código; OBF portada FR "Vitamine C Éclat") | **ENTRA** en Cien, INCI de incidecoder (única ficha de ese producto, 18 ingredientes; coincide con skinsort) |
| 4335619208988 | Cien Body Mist Salted Caramel 200 ml (go-upc) | **FUERA (2-bis)**, segundo intento 12-09: sin lista en OBF, incidecoder, skinsort ni lidl.es; incibeauty por código tras Cloudflare |
| ~~8718951579828~~ | **Colgate Sensation White 100 ml** (go-upc) | **ENTRA**: tamaño nuevo de la Sensation Blanqueador, que ya estaba con la lista de colgate.es confirmada por etiqueta |
| ~~8718951738553~~ | **Colgate Max White con cristales blancos 75 ml** (go-upc lo llama "cristales refrescantes"; en colgate.es es "MaxWhite con cristales blancos") | **ENTRA (2026-09-12c)**: la ficha de colgate.es no trae lista, pero **colgate.com/pt-pt usa el mismo `itemId` (61044888) para "Max White com cristais" y sí la trae** (16 ingredientes, con Menthol, CI 74160 y CI 74260). El id compartido es prueba de que es el mismo producto: Max White One es 61042533 en las dos webs y la Instant española es la Optic portuguesa (61042532) con lista idéntica. Erratas del portal PT corregidas ("Cocamidoproxyl", "Methylcellylose"). Truco nuevo para Colgate: **cuando la ficha .es venga vacía, buscar el mismo itemId en colgate.com/pt-pt** |
| ~~8718951763135~~ | **Colgate Max White One 75 ml** (Auchan PT lo lista con este EAN) | **ENTRA**: tercer código de la Max White One, que ya estaba con lista confirmada por dos etiquetas |
| 8436614131144 | go-upc dice "Nat.honey Gel Baño Hidratante 900 ml" (prefijo de Instituto Español) | **SIN IDENTIFICAR DEL TODO, FUERA** (segundo intento 12-09: también están tras Cloudflare la API de WooCommerce `/wp-json/wc/store/v1/products`, el buscador `?s=` y hasta `robots.txt`; el desafío es Turnstile interactivo y Playwright no encuentra la casilla): el gel Natural Honey de 900 ml que vende Mercadona lleva otro EAN (8008970056234), naturalhoney.es ya no lista ese gel y **institutoespanol.com está tras un desafío interactivo de Cloudflare** que ni Playwright pasa. Marca **Instituto Español creada vacía** como pediste; hace falta el envase (foto de etiqueta y código) o que la web se abra |

**8436614131144: DESCARTADO definitivamente (Mariana, 2026-09-14).** No se puede
identificar con certeza ni conseguir su INCI, y es un gel de baño de 900 ml descatalogado. Se
quita de la lista de pedidos; si alguien vuelve a escanearlo, reaparecerá solo.

Los dos "sin identificar":
- ~~**5054563107510**~~ = **Sensodyne Sensibilidad & Encías 75 ml** (Haleon; código UK, envase español según las
  tiendas). **ENTRA como marca nueva "Sensodyne"** con la lista oficial de sensodyne.com/es-es
  (18 ingredientes, fluoruro de estaño + fluoruro sódico). La marca tiene más gama en esa web:
  candidata a curar entera cuando toque.
- **8411660114303** = **Norit Complet detergente líquido 35 dosis** (AC Marca Home Care). Producto de
  limpieza: solo hay rangos de etiqueta (tensioactivos 5-15 %, conservantes, perfume) y la ficha
  completa de ingredientes está tras el portal con cuenta de AC Marca (reach.grupoacmarca.com),
  como pasó con Sanytol. Segundo intento 12-09: norit.es no enlaza ninguna ficha de ingredientes (solo
  aviso legal y cookies) y la lista pública del portal de AC Marca (`/public/v2/ajax?marca=NORIT`)
  devuelve vacío. **FUERA (2-bis)** salvo que se abra esa vía.

**Lo que dice esta lista, y es lo importante:** los huecos caen en marcas que ya tenemos
**a medias** (Cien, Sanex, Colgate) porque no publican bien los ingredientes, y son justo las
que la gente escanea. Antes de abrir marcas nuevas, conviene volver sobre estas.

### 2026-09-11
- ~~**8480000416858 · "Laca de uñas manicura francesa 03"**~~ **HECHO (2026-09-11b)**: entra en
  Deliplus como "Laca de uñas manicura francesa Deliplus 03 rosa" (nombre oficial de
  tienda.mercadona.es, producto 41685; no estaba en las 646 fichas de `mc_det.json` y la API
  no trae ingredientes). INCI transcrito a mano de la **foto de la etiqueta en OBF** de este
  mismo código (la portada de esa ficha es el frasco "03 manicura francesa 11 mL", así que la
  etiqueta es de este tono): 19 ingredientes, con sus colorantes CI 77891, CI 15850 y CI 19140
  (el rosa). No se ha heredado nada de otro tono. incidecoder no tiene la ficha.
- ~~**0810912032347**~~ **HECHO (2026-09-11b)**: es el **Sol de Janeiro Brazilian Bum Bum
  Cream de 50 ml** (UPC `810912…` de Sol de Janeiro, EE. UU.; identificado por incibeauty y por
  las tiendas que lo venden con ese código: Lookfantastic, Extime). Se vende en España
  (Sephora), así que entra: **marca nueva "Sol de Janeiro"** con este único producto, nombrado
  "Brazilian Bum Bum Cream 50 ml (versión EE. UU.)". INCI: la lista oficial vigente de
  soldejaneiro.com (39 ingredientes, con Tin Oxide y CI 77891). Ojo: la lista que publica
  Lookfantastic para el 50 ml es la fórmula antigua con Butylphenyl Methylpropional (Lilial,
  prohibido en la UE desde 2022): no se ha usado (regla 2, fórmula actual). Sin ficha en OBF.

### Freshly Cosmetics — abierta 2026-09-23: 11 productos, 11 códigos (de 64 fichas con INCI en la web)
PrestaShop (`sitemap_products_ES.xml`, 188 URL, 118 fichas reales, 64 con INCI). **La web
publica el INCI completo pero NO el EAN**: la lista va como botones
`data-button="more-information-ingredients-pdp"` (uno por ingrediente, con su glosario);
el nombre comercial está en el `<h2>` ("Golden Radiance Body Oil") y el `<title>` es el
descriptor en castellano ("Aceite corporal para estrías y cicatrices"). Sin `ean13` en el
`data-product` ni JSON-LD. OBF solo tiene 2 códigos.
- **EAN por la API de Douglas ES** (47 fichas Freshly, 44 con `ingredients`). Se empareja
  por lista, no por nombre: entra solo cuando la lista de Douglas es la misma que la de la
  web ingrediente a ingrediente, ignorando los componentes del "perfume natural" (aceites
  de cítricos, pineno, vainillina, mentol…) que la web desglosa y Douglas resume en Parfum.
- Entran 11. Fuera (12 de Douglas con lista distinta a la web): Vibrant Balance champú y
  acondicionador, Rose Cleanser, Hair Radiance Keratin Spray (dos conservantes en otro
  orden), Omega Rich, Curly Power, Radiant Curls Oil, Concentrate, Lime Purifying,
  Frizz-Away Co-Wash, Rose Quartz Cleanser 50 ml, Hyaluronic Energy 50 ml. Y las ~30 fichas
  sin código en Douglas ni en OBF (Bloom Orchid, Bakuchiol, desodorante…).
Nombres: "<nombre comercial> (<descriptor de la web>) <tamaño>". Scripts: `fc/` (fichas
`p/`, `products.json`, `dg/`, `dg_freshly.json`, `freshly_final.json`).

### Cocunat — abierta 2026-09-23: 39 productos, 39 códigos (de 96 fichas en su API)
Shopify headless (Astro). `/products.json` funciona (143 productos) pero sin `barcode` y
casi sin INCI; el HTML de la ficha tampoco lleva la lista. **Los datos salen de la API de
la propia marca**: `https://api-less.cocunat.com/api/products/<handle>` devuelve
`gtin`, `sku`, `ingredients` (texto INCI) y los campos del feed de Google Shopping. 96
fichas responden; 58 con INCI, 47 con `gtin`.
- Entran 39: fichas con `gtin` y lista, sin ser pack/mini/refill/duo, y cuyo `gtin` no
  está compartido con otra lista distinta.
- **Douglas ES (41 fichas Cocunat) da otra lista para el mismo EAN en 24 de 29 casos** y
  coincide solo en Pure Shampoo y Pure Conditioner. Se toma la de la API de la marca (regla
  2: fórmula vigente publicada por el fabricante). Douglas además usa para varios productos
  un EAN distinto del que da la marca (Wondermask, The Architect, The Lift, Savior…): son
  envases anteriores y quedan fuera hasta ver una etiqueta.
- Fuera: bundles y minis (sin `gtin` propio), y las fichas sin `gtin` en la API.
Nombres: el `title` de la API (marca nacida en inglés: "The Cure", "Wondermask").
Scripts: `cc/` (`api/`, `api_all.json`, `dg_cocunat.json`, `cocunat_final.json`).

### Heliocare (Cantabria Labs) — abierta 2026-09-23: 5 productos, 5 códigos (de 61 fichas en cantabrialabs.es)
Mismo circuito que Biretix: **cantabrialabs.es no publica el INCI** (61 fichas Heliocare,
solo activos y CN). EAN por Douglas ES (25 fichas, ids `5011406107…5011996287`) y
SkinLovers (56 fichas con `barcode`; 20 EAN comunes con Douglas, todos iguales); INCI por
SkinLovers (28 fichas con lista, separada por `;`) e incidecoder (53 fichas, muchas
duplicadas por dos subidas y varias marcadas "discontinued").
- Entran solo los 5 con dos fuentes idénticas (erratas aparte): 360º Age Active Fluid,
  360º Fluid Cream, 360º Gel Oil-Free Dry Touch, 360º Water Gel y 360º Pediatrics Mineral.
- **Heliocare reformula mucho y las fuentes lo reflejan**: las dos subidas de incidecoder
  de Age Active, Pigment Solution, Fluid Cream, Water Gel y MD AK difieren entre sí en 4-6
  ingredientes; SkinLovers vs incidecoder difieren en 1 ingrediente en Pediatrics Lotion,
  Advanced Gel, Pediatrics Atopic y Pediatrics Mineral (una errata de truncado en este,
  que sí entra) y en más en Sensation, Mineral Tolerance, Ultra 90 Gel, MD A-R y MD AK.
  Sin etiqueta no se sabe cuál es la vigente: fuera.
- Sin lista en ninguna fuente: Color Gel Oil-Free (3 tonos), Sport, Invisible Spray,
  Pediatrics Transparent Spray, sticks, compactos, cápsulas (Heliocare oral no es cosmética).
Los EAN de los 20 productos fuera están en `hel/dg_heliocare.json` y `hel/sl_lists.json`:
con una foto de etiqueta entran en cinco minutos.

### ISDIN — ampliada 2026-09-23: 60 productos, 68 códigos (antes 23 y 25)
La vía nueva que faltaba desde el principio: isdin.com da el INCI oficial de 252 fichas pero
no el EAN, y ahora el EAN sale de dos tiendas que publican código + lista, y **solo entra un
código si la lista que la tienda publica con él es idéntica (erratas y alérgenos aparte) a
una ficha de isdin.com de ese mismo producto**. Fuentes:
- **Douglas ES** (`/es/search?q=isdin` da 49 fichas de ISDIN/Bexident; la API
  `api/v2/products/<id>?fields=FULL&lang=es` trae `ean` e `ingredients`): 41 con lista, 28 de
  ellas idénticas a isdin.com.
- **SkinLovers** (Shopify, `barcode` en el JSON y bloque "Ingredients"): 120 fichas, 77 con
  lista, 26 idénticas a isdin.com.
- Lo que no casa con ninguna ficha oficial se queda fuera aunque tenga código y lista (unos
  50 códigos: fórmulas anteriores, promo packs de ampollas, Lambdapil cápsulas, Bexident
  colutorios/pastas sin lista…). Están en `nx/isdin_match2.txt` por si algún día hay etiqueta.
- **Fuera por copia de lista**: SkinLovers repite listas entre fichas, exactamente el patrón de
  Nautic con Erborian. 8429420243385 "Salicylic Renewal Serum" lleva la lista de K-Ox Eyes;
  8429420206694 "Nutraisdin AF" (pomada con miconazol, un medicamento) lleva la de la Pomada
  Reparadora; 8470003331180 "Gel Cream SPF 50" lleva en SkinLovers la lista del Gel Cream
  SPF 30 (entra igualmente porque **Douglas** sí da para ese código la lista del SPF 50 de
  isdin.com); 8470001507983 (tubo 10 ml con el nombre viejo "Nutrabalm") lleva la misma lista
  que 8470001507990, y como isdin.com sigue teniendo dos fichas vivas del tubo con dos
  fórmulas, sigue fuera; entra solo 8470001507990.
- **Reformulaciones**: el HydroLotion 8429420192232 lleva en Douglas la fórmula actual de
  isdin.com y en SkinLovers la anterior (Octocrylene, Isohexadecane); en el catálogo sigue con
  la anterior, que es la del envase que se fotografió (decisión del 2026-09-09). Mismo caso el
  Hydro Oil (Douglas = web, catálogo = etiqueta). El Pediatrics Gel Cream 8470001527332 es
  al revés: SkinLovers = web actual, Douglas = fórmula vieja; entra la actual.
- **Resuelto el pendiente del 2026-09-13**: 8429420282087 Scalp & Hair Spray SPF 50 entra con
  la fórmula actual (37 ingredientes), que ahora confirman Douglas e isdin.com para ese EAN.
- Códigos añadidos a productos que ya estaban (mismo producto, segundo EAN): Redness
  8429420245303, Spot Prevent Color 8429420246850, Eryfotona Night 8429420285026.
- Packs con el mismo INCI van como un código más del producto (Woman Higiene Íntima 2×200,
  Ureadin Lotion10 1000 ml junto al 750 ml); el pack Bexident Encías 2×500 va solo porque el
  bote suelto no tiene lista en ninguna tienda.
- Corregida una ligadura rota de isdin.com ("Zingiber O_x001E_cinale" → Officinale) que estaba
  en el Gel Cream SPF 30 del catálogo y en tres fichas nuevas.
Scripts: `nx/match_isdin2.py` (cruce), `nx/inci_cmp.py` (comparación tolerante a erratas y
alérgenos), `nx/gen_isdin_final.py` (lista final; conserva lo que ya estaba), `nx/dg/`.

### Consum (marca blanca) — abierta 2026-09-23: 19 productos, 19 códigos (de 22 fichas)
Sale del portal de Asevi, que la fabrica (ver Asevi): 22 fichas "CONSUM …" en el WP REST
`productoean`, con EAN de Consum (`8414807…`) y PDF de ingredientes del Anexo VII; 3 PDF dan
404. Mismos scripts y misma lectura que Asevi (`asv/parsed.json` → `asv/consum_final.json`).
Fregasuelos (7), suavizantes (9), detergente, quitamanchas y perfumador de ropa. Consum
también vende cosmética de marca blanca, pero eso no está en Asevi: si un día interesa, es
otra vía.

### Sesderma — abierta 2026-09-23: 11 productos, 11 códigos
sesderma.com sigue sin publicar el INCI (ver arriba), así que va como Heliocare/Biretix:
**dos fuentes idénticas o nada**.
- EAN + lista: **SkinLovers** (94 fichas, 28 con lista) y **Douglas ES** (43 fichas de
  Sesderma, 23 con lista). Contraste: **incidecoder** (la página de marca solo enseña 96
  fichas; buscando gama a gama salen 79 más, 175 con lista).
- Entran los 11 con lista idéntica en dos fuentes: Seslash, C-Vit Contorno de Ojos, Daeses
  Mascarilla, Sesnatura Cuerpo y Busto y Repaskin Urban 365 Piel Sensible (SkinLovers =
  incidecoder); Azelac RU Gel Crema, Repaskin Dry Touch, Factor G Renew Óvalo y Contorno de
  Ojos, Abradermol (Douglas = incidecoder, tres con erratas de Douglas); Repaskin Urban 365
  Despigmentante (SkinLovers = Douglas).
- Fuera 28 códigos con lista en una sola fuente o distinta en cada una (Sesderma reformula
  tanto como Heliocare: C-Vit crema, Hidraderm Hyal, Reti Age, Mesoses, Azelac hidratante,
  Repaskin Silk Touch, Sesbalance, Retisil, Oceanskin…), entre ellos 5 fichas cuya
  "lista" es una frase de marketing. Todo en `nx/ses_match.json`.
Scripts: `nx/match_ses.py`, `nx/gen_ses_final.py`, `nx/ic_sesderma_lists2.json`.

### SkinCeuticals — ampliada 2026-09-23: 28 productos, 21 códigos (antes 16 y 6)
skinceuticals.es y el resto de webs de la marca (.fr, .it, .de, .co.uk, .com) siguen detrás de
Cloudflare, y Douglas ES no vende la marca. Así que va como Sesderma: **SkinLovers**
(59 fichas; el bloque "Ingredients" lleva primero los activos en prosa y al final la lista
INCI en mayúsculas, 33 con lista y 36 con `barcode`) contrastado con **incidecoder** (102
fichas con lista entre la página de marca y las búsquedas por gama). Entra lo idéntico.
- 12 productos nuevos con EAN `3606000…`: Antioxidant Lip Repair, Blemish + Age Cleansing
  Gel, Retinol 0.3, Emollience, Glycolic Renewal Cleanser, H.A. Intensifier (fórmula actual),
  Mineral Eye/Matte/Radiance UV Defense, Phyto A+, Phyto Corrective Masque, Soothing Cleanser.
- Código añadido a tres fichas que estaban solo por nombre (Silymarin CF 8431567460174, Triple
  Lipid Restore 3606000435087, Blemish + Age Defense 8431567387990), con la lista confirmada;
  y la lista del Advanced Brightening UV Defense (3337875702478) pasa a la actual, que dan
  igual SkinLovers e incidecoder (la anterior no llevaba Diisopropyl Sebacate).
- **H.A. Intensifier tiene dos EAN con dos fórmulas**: 3337875736749 (la que estaba, ahora
  "fórmula anterior") y 3606000436442 (la actual, con Cyclohexasiloxane). Van separadas.
- Fuera por lista distinta entre fuentes: Metacell Renewal B3 (3606000495470) y Daily
  Moisture (3606000482111). Sin lista en incidecoder: Oil Shield UV Defense, Simply Clean,
  Tripeptide-R Neck Repair. Sin lista o sin código en SkinLovers: cofres, Cell Cycle
  Catalyst, P-Tiox, Serum 10, Discoloration Defense, Retexturing Activator, Glycolic 10.
- **10 productos se quedan fuera solo por la regla 3 (código UPC de EE. UU.)**: SkinLovers
  los vende con UPC-A de 12 dígitos `635494…` (= `0635494…` en EAN-13) y su lista es
  idéntica a incidecoder: C E Ferulic (635494363210), A.G.E. Interrupter (635494345254),
  A.G.E. Eye Complex (635494358209), AOX+ Eye Gel (635494348200), Clarifying Clay Masque
  (635494330205), Hydrating B5 Gel (635494317206) y Masque (635494316209), Phyto Corrective
  Gel (635494314205) y Sheer Mineral UV Defense SPF 50 (635494394207). **Corrección 2026-09-25:
  son 9, no 10**: el Ultra Facial UV Defense SPF 50 (635494349207) tiene los mismos ingredientes
  pero en otro orden, así que no es idéntico. Los 9 están preparados en
  `pendientes/skinceuticals_upc.json` (ver decisión D). Es el mismo caso que NYX (los envases que se venden aquí
  llevan ese código): **si Mariana quiere la misma excepción, entran en un minuto**
  (`sk/sk_match.json`).
Scripts: `sk/parse_sl.py`, `sk/fetch_ic.py`, `sk/match_sk.py`, `sk/gen_sk_final.py`.

### Bioderma — ampliada 2026-09-23: 35 productos, 50 códigos (antes 28 y 42)
Mismo circuito que Sesderma y SkinCeuticals (**dos fuentes idénticas o nada**): bioderma.es
sigue sin publicar el INCI y Douglas ES apenas vende la marca (3 fichas, sin lista). EAN +
lista de **SkinLovers** (78 fichas, 62 con lista, 65 con `barcode`; pega el código de lote
"BI747" al último ingrediente y parte algún nombre en dos, cosa que la comparación ya
tolera) contra **incidecoder** (252 fichas de la marca más las 22 que ya teníamos).
- Entran 7 productos y 8 códigos: Cicabio Arnica+, Hydrabio H2O 100 y 500 ml, Pigmentbio
  Daily Care SPF 50+, Pigmentbio Foaming Cream, Atoderm Intensive Gel-Crème 500 ml, Sensibio
  AR+ Gel Micelar y Sensibio Aceite Micelar 300 ml. Confirmados dos que ya estaban
  (Pigmentbio Sensitive Areas, Photoderm Pediatrics Mineral).
- **Hydrabio H2O**: el 250 ml del catálogo (3401399694127) lleva la lista de la etiqueta de
  OBF (generación anterior, con Disodium EDTA); SkinLovers da para los tres tamaños la actual,
  idéntica a incidecoder. Los 100/500 ml entran como "(fórmula actual)" y el 250 ml se queda
  como está (misma decisión que el HydroLotion de ISDIN).
- Fuera por copia de lista: Pigmentbio H2O Micellar Water (3701129800102) lleva en
  SkinLovers la lista de la Foaming Cream (Magnesium Laureth Sulfate, Cellulose Acetate).
- Fuera por lista distinta o de otra generación (unos 30): Sensibio H2O (orden distinto),
  Photoderm Spot-Age (solo cambia la posición de Fragrance, pero no es idéntica), Photoderm
  Cream/AR/AR+/X Defense/Eau Solaire, Hydrabio Light/Rich/Perfecteur/Booster, Sensibio AR+
  Bi-Serum/SOS/CC, Sébium Kerato+, Cicabio Cleansing Balm…; y 16 fichas de SkinLovers cuya
  "lista" es una frase (Sensibio Defensive, Photoderm Pediatrics Milk, Hyalu+…), más los
  promo packs `5600358…`. Todo en `bio/match.txt`.
Scripts: `bio/fetch.sh`, `bio/parse_sl.py`, `bio/fetch_ic.py`, `bio/match_bio.py`,
`bio/gen_bio_final.py`.

### KH-7 y Bosque Verde (limpieza) — 2026-09-25 (versión 2026-09-25h): 24 productos, 26 códigos
Cola del 25-09, punto 5. Método de limpieza (648/2004), como Asevi. Notas y ejemplos con URL en
el scratchpad (`c5/kh7_notas.md`, `c5/bosqueverde_notas.md`; generador `c5/kh7bv/gen.py`).
- **KH-7 — 8 productos, 10 códigos.** Lista: el PDF de la ficha de ingredientes de cada producto
  en kh7.es (`/hojas_ingredientes/…_ESPANA.pdf`, 14 fichas, casi todas de 2026 y con UFI). kh7.es
  no da EAN: salen de Consum (API `tienda.consum.es/api/rest/V1.0/catalog/product?q=kh-7`),
  identificando cada uno por la foto del envase y el tamaño frente a los envases 2026 de kh7.es;
  el Quitagrasas además por Mercadona, cuya etiqueta trasera lleva **el mismo UFI** que la ficha;
  Desic porque la propia ficha de kh7.es enlaza Consum y Alcampo, que dan el mismo EAN. Entran
  Quitagrasas (pistola y recambio), Quitagrasas Cítrico, Sin Manchas (2), Antical, Baños
  Multisuperficie, Cocinas, Desic (fregasuelos insecticida con permetrina) y Maderas y Cuero (la
  entrada más floja: código solo de Open Products Facts, con foto del envase actual). Fuera: Sin
  Manchas Sin Olores 8420822104342 (se vende como el antiguo Oxi Effect 750 ml; la ficha es del de
  780), Quitagrasas 715 ml 8420822135292 (tamaño que kh7.es no enseña), códigos de Francia e
  Israel, y seis productos con ficha pero sin EAN (Quitagrasas ECO, Baños ECO, Desincrustante,
  Placas de inducción, Vitrocerámica, recambio Cítrico). Errata de la ficha corregida
  ("Metoxhyisopropanol").
- **Bosque Verde — 16 productos, 16 códigos.** Mercadona no da ingredientes (la API de la tienda
  da EAN, proveedor y foto de la etiqueta; la etiqueta solo trae rangos). La lista sale de la ficha
  648/2004 del **fabricante**: **Francisco Aragón** (15: cada ficha de franciscoaragon.com enlaza el
  PDF y el producto en Mercadona, que da el EAN; Oud por nombre y tamaño exactos; en el Limpiador de
  Muebles el código de artículo 07736 de la ficha forma parte del EAN) y **SPB** (1: nombra sus PDF
  por EAN, pero son de 2015-2020 y muchos escaneados; solo Disuelve manchas, de 2020, pasa la
  comprobación). **Comprobación con la etiqueta actual** (foto de Mercadona): todo lo que la
  etiqueta nombra (conservantes, alérgenos, "Contiene…") tiene que estar en la lista, o fuera.
  Entran Limpiacristales, Limpiador de Hornos, Limpia Mopas, Limpiador de Muebles, 5 ambientadores
  en spray (Blossom, Essence, Red Elixir, Oud, Peonía), 2 de perlas (Lima, Tiernos Recuerdos) y 4
  velas perfumadas (Peonía, Santal Vanilla, Neroli, Chai). Ambientadores y velas no son
  detergentes, pero el fabricante publica su lista en el mismo formato y la app ya tiene reglas para
  ambientadores. Fuera: 27 ambientadores, mikados y velas de Francisco Aragón cuya etiqueta nombra
  alérgenos que la lista no trae (lista incompleta o de otra fórmula), la vela Chai en tarro (ficha
  de 120 g, producto de 150 g), el difusor con recambio (lleva aparato), insecticidas sin lista, el
  amoníaco, el friegasuelos Spa, Oxi Active y las lejías de SPB (listas antiguas o que no cuadran con
  la etiqueta), el gel de Persán 8480000404046 (dos listas distintas para el mismo EAN y ninguna con
  los alérgenos de la etiqueta) y los proveedores que no publican (Inquiba, Linasa, McBride…).
- **Revisión FP/FN** (ver el registro): 9 fichas caían en Cuidado personal (categoría equivocada) y
  la vela Neroli saltaba como Naftaleno por "Naftaleno 2-etoxi-"; corregidos los dos. Avisos
  verdaderos que sorprenden: **ftalato de dietilo (DEP) en 6 ambientadores/velas de Bosque Verde**,
  galaxólido en el ambientador Blossom, permetrina en Desic, DDAC en el Antical. **Pregunta de
  criterio para Mariana (F, sin prisa):** "Benzophenone-12" (octabenzona, filtro UV para que no
  amarillee la cera) en 4 velas, sin regla. La app avisa de la benzofenona y de las BP-3/BP-4 por su
  actividad hormonal; para la BP-12 hay muy pocos datos. No se ha añadido.

### Oral-B y Lacer — 2026-09-25 (versión 2026-09-25g): 42 productos, 75 códigos
Cola del 25-09, punto 5. Notas y ejemplos con URL en el scratchpad (`c5/oralb_notas.md`, `c5/lacer_notas.md`).
- **Oral-B (P&G) — 5 productos, 7 códigos.** oralb.es da el EAN de cada ficha pero **ninguna
  lista** (tampoco UK, DE ni PT). Regla de dos fuentes: dos listas idénticas independientes, al
  menos una en la misma ficha que el EAN (dosfarma, arenal.com; contraste con Alcampo,
  Parafarmacia Campoamor e incidecoder). Entran Advanced Protección de Encías 2×75, Advanced
  Prevención del Sarro (75 y 3×75), Pro Junior 6-12 Stitch, 3D White Clinical Blanqueamiento
  Intensivo y Pro-Expert Protección Profesional (75 y 2×75; **único emparejado por nombre y tamaño
  exactos**). Ojo: 8700216675246 (Sarro 75 ml) se vendió antes como "Pro-Expert Advanced Science
  Limpieza Profunda"; no hay otra lista para ese código. Fuera: gama Advanced/Clinical donde P&G
  reutilizó códigos y las tiendas dan dos listas para el mismo (Protección de Encías 75, Sensibilidad,
  Fortalece el Esmalte, Regenera y Remineraliza), fuentes que no coinciden (3D White Luxe
  Perfección, Pro-Expert 125), una sola fuente (Luxe Carbón, Pro-Expert Sensibilidad y
  Blanqueamiento), colutorios y Complete sin lista, sedas sin composición, cepillos.
- **Lacer — 37 productos, 68 códigos.** La web oficial de la gama dental es
  **laceroralhealth.com** (Lacer S.A.; lacer.es lleva a la corporativa): 45 fichas con INCI
  completo y el **código nacional (C.N.)** de cada formato, sin EAN. El EAN de parafarmacia es
  **847000 + los 6 dígitos del C.N. + dígito de control** (en los 84 formatos el dígito de control
  del C.N. cuadra); 33 de los 57 así obtenidos aparecen tal cual en dosfarma o Arenal con el mismo
  producto y tamaño. Además 11 códigos propios `8430340…` (formatos de súper, 600 ml, duplos),
  cada uno con una tienda que da ese EAN y, en la misma ficha, la lista idéntica a la oficial.
  Medicamentos: en la AEMPS solo Flúor Lacer gotas y comprimidos, que no están en la web dental:
  fuera. Afta, Mucorepair, SensiLacer gel bioadhesivo, XeroLacer spray y colutorio y la crema
  adhesiva LacerPro Forte son probablemente productos sanitarios: entran porque la marca publica su
  lista completa en INCI. Fuera: **10 códigos oficiales para los que una tienda da una fórmula
  antigua con el mismo código** (triclosán, parabenos o carbonato cálcico: reformulados sin cambiar
  el código; no se sabe qué envase hay en la estantería), códigos `8430340` dudosos, LacerBlanc
  Menta 125 ml (la web repite el C.N. del de 75), packs con regalo, gama Aligner (sin lista),
  Ortolacer y XeroLacer comprimidos (ya no están en la web), sedas y cintas (la lista es solo del
  recubrimiento), comprimidos para prótesis, cepillos. Erratas de la web corregidas (Cocamydopropyl,
  "ipotassium", Mentyl); "Hydrated Silica" dos veces en el Júnior gel menta, así en la web oficial.
- **Revisión FP/FN:** sin falsos positivos ("Aroma" es el saborizante de pastas y colutorios; el
  eugenol es el alérgeno declarado del aroma; "Sodium Methylparaben/Propylparaben" son parabenos).
  Regresión: 0 cambios en las fichas anteriores. **Pregunta de criterio para Mariana (E, sin
  prisa):** ninguna regla avisa del **flúor** (fluoruro sódico, monofluorofosfato, fluoruro de
  estaño; está en casi todas las pastas del catálogo). Hay estudios sobre tiroides y neurodesarrollo
  con agua muy fluorada (NTP 2024: >1,5 mg/L), no con pasta de dientes usada normalmente; no se ha
  añadido. Si se quiere, sería un aviso "Emergente" limitado a lo infantil o a "no tragar".

### Vaseline, TRESemmé, Gliss y Syoss — 2026-09-25 (versión 2026-09-25f): 66 productos, 76 códigos
Cola del 25-09, punto 5. Notas y ejemplos con URL en el scratchpad (`c5/<marca>_notas.md`).
- **Vaseline (Unilever) — 25 productos, 29 códigos.** `vaseline.com/es` no existe (404, sin
  versión española): se usó **vaseline.com/uk**, misma plataforma que Dove (código e INCI por
  variante en `data-productvariants`). Los códigos son los europeos (`871…`/`872…`, EAN-8 de
  Unilever en la vaselina original y el Lip Therapy Rosy) y la etiqueta de 8712561480369 en OBF
  lleva texto y teléfono de España. Nombres traducidos al castellano. Etiquetas de OBF revisadas
  a mano como contraste. Fuera: body butter 8710908737329 y Essential Healing 200 ml
  8712561479806 (Lilial: fórmula antigua; el de 400 ml entra), Advanced Repair 200 ml
  8712561478762 (la etiqueta muestra otra fórmula), Cocoa Radiant loción 8712561483094 y
  8712561483162 (dos etiquetas sin Benzyl Alcohol, Citronellol ni CI 77891 que sí da la web).
- **TRESemmé (Unilever) — 12 productos, 18 códigos.** `tresemme.com/es`, código e INCI de la
  misma variante. 28 fichas, 42 códigos, solo 15 variantes con lista. Champú y acondicionador
  Intensa Hidratación: la lista está solo en la variante de 100 ml, y **por la regla de Dove**
  (tamaños bajo la misma ficha comparten lista, regla 4) entran también sus 400 y 685 ml
  (8720181435201/256, 8720181435249/331). Fuera: mascarilla Repara & Fortalece 8720181238086
  (Lilial y texto de otra ficha pegado) y 27 códigos sin lista.
- **Gliss (Henkel) — 29 productos, 29 códigos.** `schwarzkopf.es` (sitemap, 37 fichas de
  Gliss): `gtin` en los datos estructurados de la ficha e INCI completo; además se exige que el
  código coincida con el del nombre del archivo de la foto del producto, porque la web tiene
  copias. Fuera: los 3 Full Hair Wonder (código copiado de Oil Nutritive y lista traducida),
  champú Long & Sublime (código de ficha ≠ código de la foto), sérum Aqua Revive (lista cortada),
  Total Repair Reflex Shine y Tratamiento de Puntas (dos productos con la misma lista: uno es
  copia). "7 Seconds" publicado dos veces con el mismo código: una entrada.
- **Syoss (Henkel) — no entra.** `syoss.es` da listas pero ningún código; las de tintes (Permanent
  Color, Oleo Intense, Brow Tint, Root Retouch) están traducidas al castellano. Primor da códigos
  pero con listas de fórmulas antiguas que no coinciden con syoss.es, a veces en el mismo código
  (mousse Keratin 5201143155199). Color Glaze: códigos sin tono. La Matt Cream (84461032) tiene la
  lista cortada en syoss.es y en Primor; completa solo en la foto de etiqueta de OBF (fuente única:
  no vale).
- **Revisión FP/FN:** sin falsos positivos (el "Aroma" que salta en los bálsamos labiales de
  Vaseline es el saborizante, bien; "Sodium Methylparaben" en Gliss es un parabeno, bien). Sin
  falsos negativos nuevos (estireno: mismo criterio que el 21-09). Regresión: 0 cambios en las
  fichas anteriores (no se ha tocado la app).

### Catrice y essence (Cosnova) — abiertas 2026-09-25 (versión 2026-09-25e): 505 + 541 productos, 677 + 740 códigos
Cola del 25-09, punto 5. Fuente única: las webs oficiales en español, `catrice.eu/es-es` y
`essence.eu/es-es` (sitemaps de producto: 680 y 756 fichas; una ficha por tono).
- **Cómo se saca**: cada ficha es `/p/<id>/<slug>`. El nombre y el EAN (`gtin13`) salen del
  JSON-LD (`ProductGroup` → `hasVariant` cuya URL lleva ese `<id>`); el tono, del objeto de
  producto de la página (`"id":"<id>"`, `"gtin"`, `"color":{"number","name"}`); la lista, del
  `c_inciList` de **ese mismo objeto**. Se exige que el EAN sea válido, que contenga el `<id>`
  (Cosnova numera así: 4059729**446930** ↔ id 944693) y que entre el objeto y su `c_inciList` no
  haya otro objeto. Cuando la lista es larga, la página la guarda aparte como referencia (`$53`) en
  los datos de Next.js; se resuelve con su longitud exacta (paletas, cushions: 16 + 37 fichas).
- **Tonos**: una entrada por fórmula. Los tonos con la lista idéntica van juntos con todos sus
  códigos, "Base de maquillaje ... (tonos 10, 20, 30)"; si todos los tonos de un producto comparten
  lista, sin tonos en el nombre. Los colorantes cambian de un tono a otro, así que muchas
  entradas llevan un solo tono.
- **Listas por partes** (paletas, dúos, pestañas con pegamento): se deja cada parte con su
  nombre, como en los tintes de Garnier: "Nº 1/3: Mica, Talc, ... · Nº 2: ...", "Cream: ... ·
  Powder: ...", "Pegamento" en las pestañas postizas. El "[+/- May Contain: CI ...]" de las
  paletas se deja tal cual está en la etiqueta.
- **Fuera**: essence 9 fichas sin lista, 1 con la lista de otro objeto en medio, 1 dúo de contorno
  con la cabecera rota, el set de cejas y los 4 sets de uñas postizas (la única lista es la de la
  toallita limpiadora); Catrice las 3 "Lip Artist" (barra + perfilador, cabecera en siete idiomas
  que no se puede partir con seguridad).
- **Nombres**: los de la web española tal cual (Cosnova mezcla castellano y mayúsculas de marca:
  "Laca de uñas GEL AFFAIR", "BASE DE MAQUILLAJE EN BARRA"). Arreglados a mano: las tres mini
  paletas "the BROWN/MAUVE/PEACH edition" (el JSON-LD llamaba "BROWN" a las tres) y el perfilador
  "line n' STAIN!" de la primera tanda (01 y 02, fórmula distinta de la gama nueva "line and
  stain", marcado "(primera versión)").
- **Revisión FP/FN** (`revisa.mjs catrice essence`). Falsos positivos corregidos: Propylene
  Glycol Dibenzoate y Phosphoric Acid Polyester (ver el registro). Avisos verdaderos que
  sorprenden: **Hexamethylindanopyran (galaxólido) en 1 Catrice y 6 essence**, BHT en 16 essence
  (los esmaltes UV Gel y un topper), octisalato en 20 + 15 (los que llevan SPF), octocrileno y
  etilhexil metoxicinamato en la prebase Ten!sational 10 in 1 Dream de Catrice. Revisado sin cambio: los copolímeros de estireno
  ("Styrene/Acrylates Copolymer" y afines, 80 + 6) siguen sin aviso, mismo criterio que el 21-09 (el
  polímero no es el monómero); "Lauryl Polyneopentyl Glycol Adipate Phthalate/PEI-45
  Crosspolymer" (9 essence) es un poliéster con el ftalato ligado a la cadena, no un ftalato
  plastificante suelto, así que no se añade a la ficha de ftalatos (si Mariana lo quiere avisado,
  es una decisión de criterio); siloxanos "Tris(trimethylsiloxy)silylethyl Dimethicone" (no son
  D4/D5/D6) y "Tris(tetramethylhydroxypiperidinol) Citrate" (estabilizante UV del envase, sin
  datos de disrupción): sin cambio. Aceite de lavanda en 2 Catrice: decisión C.
- Scripts: `su/cosnova.py`, `su/cosnova2.py` (comprobación estricta del objeto),
  `su/cosnova3.py` (referencias `$xx`), `su/build_cosnova.py`, `su/group_cosnova.py`.

### The Ordinary (DECIEM) — preparada 2026-09-25, NO aplicada: 26 productos, 26 códigos UPC (decisión D)
Cola del 25-09, punto 4.
- **INCI**: la web española de la marca (`theordinary.com/es-es`, sitemap `sitemap-es_ES.xml`,
  101 URL) trae la lista completa en `data-original-ingredients` y el nombre en `product-name`
  (el `<title>` y el primer h1 llevan promociones, no sirven). 80 productos con lista.
- **Código**: la web no lo publica. Douglas ES vende 48 fichas de The Ordinary, con **UPC-A de 12
  dígitos `769915…`** (DECIEM es canadiense), que en EAN-13 es `0769915…`. **La regla 3 deja fuera
  los códigos que empiezan por 0** salvo excepción expresa (NYX y essie). Por eso no se aplica.
- Emparejado por **nombre exacto** entre Douglas y la web (sin quitar palabras como "Solution",
  que confundía la mascarilla de ácido salicílico con la solución) y, cuando Douglas da una lista
  útil, comprobando que es idéntica. Douglas traduce muchas listas al castellano ("glicerina") o
  las pega sin comas: en esas vale la lista oficial y el nombre exacto.
- Fuera por lista distinta (posible reformulación): Squalane Cleanser, Retinol 1% in Squalane,
  AHA 30% + BHA 2%. Fuera por no tener ficha con el mismo nombre en la web española: 18 (Hyaluronic
  Acid 2% + B5, Caffeine, Glycolic 7%, lácticos, mandélico, capilares…); con una tabla de nombres a
  mano se pueden sumar varios. Fuera The Daily Set (es un set).
- Preparado en `pendientes/theordinary_upc.json` (códigos ya en 13 dígitos con el 0 delante, como
  NYX). Si Mariana da la excepción, entra con `apply.py`.

### Cosmia (Alcampo / Auchan) — abierta 2026-09-25 (versión 2026-09-25d): 115 productos, 115 códigos
Hueco de Datos del 2026-09-15 (marca blanca de Alcampo; el código 20525101 de aquel pedido sigue
sin identificar, ver esa entrada). Dos fuentes oficiales, una para cada cosa:
- **EAN**: la tienda de Alcampo (`compraonline.alcampo.es`, plataforma Ocado) tiene una API por
  producto, `/api/webproductpagews/v5/products/bop?retailerProductId=<id>`, con el EAN en
  `bopData.fields[features]` ("EAN | 3596710516957"). La búsqueda solo enseña 50 resultados por
  consulta: se unieron 41 búsquedas por tipo de producto (201 fichas, 133 con EAN). **El firewall
  corta si se va rápido**: con pausas y reintentos.
- **Composición**: Cosmia es de **Auchan SAS** (el "operador" que da la propia Alcampo) y
  **auchan.fr** publica la "Composition" de cada ficha con su "Réf / EAN". Se busca el EAN en
  auchan.fr y **solo se acepta si la ficha francesa muestra ese mismo EAN**. 121 de 133.
- Fuera: 6 maquinillas (la composición que da Auchan es la de la banda lubricante), la esponja,
  un 3 en 1 sin composición y 10 que auchan.fr no vende (champús secos, desodorantes, el
  anticaspa con climbazol, la mascarilla de argán…).
- Nombre: el de Alcampo sin "COSMIA" delante. Asteriscos de ingredientes ecológicos quitados.
- Revisión FP/FN: sin falsos positivos (el "aroma" que salta es el de la pasta de dientes, bien).
  Falso negativo con decisión pendiente: el aceite de lavanda (decisión C).

### Embarazo y bebé: Mustela, Nenuco, Suavinex — 2026-09-25 (versión 2026-09-25c): 47 productos, 61 códigos
Cola del 25-09, punto 3.
- **Mustela** (mustela.es, Shopify de Laboratoires Expanscience): **web oficial sola**. EAN por
  variante en `/products/<handle>.js` (`barcode`; `products.json` no lo trae) e INCI completo en
  la ficha ("Lista de ingredientes:", o un párrafo que es la lista). **45 productos, 58 códigos**
  (tamaños con la misma lista juntos). Fuera: packs, rutinas, neceseres, canastillas y dúos
  (varios productos en una ficha), muestras sin código, dos fichas con la lista traducida al
  castellano (toallitas compostables formato ahorro, aceite de baño piel seca: "AGUA,
  GLICERINA, BENZOATO DE SODIO…" no es INCI), el aceite de estrías (sin lista) y el pijama
  Stelatopia (es un textil impregnado). La web va con cortes de protección: descargar despacio.
- **Nenuco** (nenuco.es): publica el INCI de 10 fichas pero **no el EAN**. Alcampo da EAN solo de
  algunos y Open Beauty Facts tiene 5 códigos. Entran 2 productos y 3 códigos, solo con nombre y
  tamaño exactos o lista idéntica: Agua de Colonia 200 ml (8428076006733 por nombre y tamaño;
  8410104445775 con la etiqueta de OBF idéntica a la web) y Agua de Colonia Classic 650 ml
  (8428076006795, Alcampo). Fuera los que cambian de nombre o de tamaño entre fuentes (champú
  "extra suave" en la web y "ultra suave" en la tienda, jabón de 650 ml en la web y de 750 ml
  en OBF…). La web mete un espacio invisible tras "Geraniol" en una ficha: quitado (había otro
  en el nombre de una ficha de CeraVe, también quitado).
- **Suavinex** (suavinex.com): no publica INCI ni EAN; SkinLovers e incidecoder no la tienen y
  Douglas solo trae accesorios. Fuera entera (regla 2-bis).
- Revisión FP/FN: Mustela y Nenuco limpias (perfume y propilenglicol, bien disparados; nada de
  la lista de vigilancia sin aviso).

### Higiene íntima y menstrual: Evax, Tampax, Ausonia, Lactacyd, Chilly — 2026-09-25 (versión 2026-09-25b): 6 productos, 48 códigos
Cola del 25-09, punto 2. Compresas y tampones no llevan INCI: se guarda **la composición que
publica el fabricante**, con sus palabras, y si lleva o no fragancia según lo que él declara.
- **Evax y Tampax** (P&G, evaxtampax.es). Composición oficial en dos artículos: "¿Qué contienen
  las compresas Evax?" (capa superior y exterior de poliolefinas; núcleo de espuma absorbente
  en Liberty, de celulosa con gel en Fina y Segura y Cottonlike; adhesivo; "aroma: solo en las
  versiones etiquetadas con un ligero aroma"; envoltorio) y "¿De qué están hechos los tampones
  Tampax?" (rayón y algodón, polietileno y polipropileno, cordón, hilo de poliéster, aplicador
  sin BPA, "no se añade ningún perfume"). **Los EAN** salen del bloque de reseñas de cada ficha
  (`bvData.eaNs`), que mezcla códigos entre familias; **solo se acepta un código si aparece en
  una sola familia** (dentro de una familia la composición es la misma; cambia la absorción).
  Open*Facts confirma el nombre en los que tiene.
  - Entran: **Evax Liberty** (9 códigos; su ficha dice "delicada fragancia") y **Tampax Pearl
    (10), Compak (17) y Pearl Compak (6)**, sin perfume.
  - **Fuera, esperan etiqueta**: Evax Cottonlike, Fina y Segura, Salvaslip (normal, maxi, fresh,
    aroma) y Adapt. La web no dice si llevan aroma (Cottonlike habla de "perlas activas", que
    según P&G solo van en las versiones con aroma) y la familia Salvaslip mezcla con y sin
    aroma bajo los mismos códigos. Con una foto del paquete ("con un ligero aroma" o no) entran.
- **Ausonia** (P&G, ausonia.es). Las compresas menstruales no tienen composición publicada, solo
  frases ("los protegeslips no tienen perfume"): fuera. Sí la tiene la gama **Discreet** (pérdidas
  de orina): núcleo de celulosa o poliéster/polipropileno/polietileno o gel, capa superior
  sintética, "control de olor: contiene un ligero aroma", adhesivos, capa trasera. Entra como
  una ficha con 5 códigos (los que no salen en ninguna otra ficha de Ausonia).
- **Lactacyd** (gel íntimo, INCI normal): lactacyd.es no publica lista ni código. Por dos
  fuentes idénticas (SkinLovers = incidecoder) entra 1: Pharma Sensitive 250 ml. Otro que casaba
  lleva un código con prefijo 2 (código interno de tienda): fuera. El resto, listas distintas.
- **Chilly** (gel íntimo, Bolton): chilly-intimate.com/es solo da activos, sin lista ni código;
  Douglas trae dos listas sin segunda fuente. Fuera.

**Cambio en la app: la ficha 34 ya salta.** No tenía forma de hacerlo: su alias era una frase
("'Perfume' en productos menstruales") que nunca aparece en una lista. Ahora, si el texto es la
composición de un **producto absorbente** (lleva "núcleo absorbente", "compresa", "protegeslip",
"salvaslip", "tampón" o "aplicador") y lleva fragancia, el aviso genérico de perfume (5) **se
sustituye** por el específico de la 34 (perfume en contacto con mucosa). La 34 queda como
"solo por lógica" (no salta por nombre). Regresión: **0 cambios** en las 2.935 fichas que ya
había; salta en Evax Liberty y Ausonia Discreet. La 191 (microplásticos) salta en los tampones
y en Ausonia por "polipropileno"/"poliéster", como dice su propia ficha.

**Decisiones de Mariana (2026-09-25):** A, que se quede como está ("el punto es que detecte que
hay fragancia": en compresas y tampones sale el aviso específico 34); B, sí ("si el polietileno
es un microplástico, debería figurar como tal; si las poliolefinas lo son, también"); C era una
pregunta suya ("¿son disruptores endocrinos o no?"). Respuesta dada: **no está demostrado**; hay
casos aislados de ginecomastia prepuberal (Henley 2007) y actividad débil en células (Ramsey
2019), pero en ratas no se vio efecto estrogénico (Politano 2013) y ningún organismo (UE, ECHA,
SCCS) los clasifica como disruptores. Decisión: **opción 1, mantenerlos como "Emergente" (el nivel
más bajo) "pero no alarmando, porque la evidencia es bajísima"**: los textos de la ficha 211 dicen
que la evidencia es muy baja, que no hace falta evitarlos y, si preocupa, en niños pequeños y uso
diario. B y C aplicados en la app el mismo día, ver el registro de la revisión FP/FN. D sigue
pendiente.

**Decisiones que se le plantearon:**
- **A) ¿La 34 sustituye o se suma a la 5?** Aplicado: sustituye (un solo aviso de perfume, el
  específico). Si prefieres los dos, es una línea.
- **B) Polietileno y poliolefinas como microplásticos (ficha 191).** Hoy la 191 solo reconoce
  poliéster y polipropileno. Números del catálogo entero:
  - "Polyethylene" como ingrediente propio: **98 cosméticos** (maquillaje, exfoliantes,
    espesantes) y 2 de Hogar. Es el microplástico clásico de la cosmética (restricción UE
    2023/2055). Añadirlo suma un aviso "Emergente" a esos 98.
  - "Polyethylene Terephthalate" (purpurina PET): 11 cosméticos. "Oxidized Polyethylene": 8.
  - "Poliolefinas"/"polietileno" en composiciones de compresas: Evax Liberty (hoy sin aviso de
    microplásticos, porque P&G escribe "poliolefinas") y los tampones (que ya avisan por el
    polipropileno).
  Propuesta: añadir "polyethylene, polietileno, poliolefinas, polyolefin, polyethylene
  terephthalate" a la 191. Dime sí o no.
- **C) Aceites esenciales de lavanda y árbol del té.** Hoy ninguna regla los reconoce. Hay señal
  publicada de actividad estrogénica y antiandrogénica (Henley et al. 2007, NEJM: ginecomastia
  prepuberal con productos de lavanda y árbol del té; Ramsey et al. 2019, in vitro, con
  componentes como linalyl acetate y terpineol), aunque la evidencia en personas es de casos
  aislados y está discutida. Números: **"Lavandula" en 41 fichas** (Davines 12, Nivea 7, Cosmia 6,
  Cocunat 4, Haruharu 4…) y árbol del té en 1. Si entra, propuesta: riesgo "Emergente", alias
  "lavandula angustifolia oil, lavandula oil, lavender oil, lavandula hybrida oil, lavandin
  oil, melaleuca alternifolia leaf oil, tea tree oil". Dime sí o no.
- **D) Excepción a la regla 3 para los UPC de The Ordinary y SkinCeuticals.** Los envases que se
  venden en España llevan el UPC-A de su fabricante (`0769915…` The Ordinary, canadiense;
  `0635494…` SkinCeuticals EE. UU.), igual que NYX (`0800897…`), que ya tiene la excepción. Sin
  ella no entra ningún The Ordinary (26 preparados) ni esos 9 SkinCeuticals (entre ellos el C E
  Ferulic). La app ya normaliza los UPC-A de 12 dígitos. Dime sí o no.

### Endocare (Cantabria Labs) — abierta 2026-09-25: 4 productos, 4 códigos (de 43 EAN encontrados)
Cola del 25-09, punto 1. Mismo circuito que Biretix y Heliocare: cantabrialabs.es no publica
el INCI, así que **dos fuentes idénticas o nada**. EAN de SkinLovers (34 fichas, 31 con
`barcode`) y Douglas ES (Endocare, casi todas sin lista); listas de SkinLovers (24),
incidecoder (26) y Douglas.
- Entran 4: Hydractive Solución Micelar 100 ml, Radiance Contorno de Ojos, Age Barrier
  Hyaluboost Sérum y Contorno de Ojos y Labios (SkinLovers = incidecoder).
- **SkinLovers transcribe muy mal las listas de Endocare**: palabras pegadas
  ("caprylictriglyceridebutyrospermumparkii"), letras cambiadas ("niaciamide", "undecnae"),
  trozos desordenados ("butyrospermum parkii maintain"). No sirven como fuente. Douglas casi
  no trae lista. farmaelglobo y farmacianautic tienen el EAN en la URL pero solo los activos.
  Open Beauty Facts no tiene ninguna lista transcrita de estos códigos.
- Los 39 EAN que quedan fuera están en `cl/endocare/match.json`: con una foto de etiqueta
  entran en cinco minutos (Tensage, Cellage, Renewal, Radiance C, Expert Drops, Aquafoam…).

### Heliocare y Head & Shoulders — revisadas 2026-09-25 para ampliar: sin cambios
- **Heliocare**: con las fuentes de hoy (SkinLovers 55 fichas, Douglas 41, incidecoder 35,
  farmacias y OBF) solo se confirman los 5 que ya estaban. De los que casan de más, uno es
  una copia (el "360º Pigment Solution Fluid" de SkinLovers lleva la lista del Age Active)
  y otro tiene un código con prefijo de otra empresa (`8437002…`, como el que ya se
  descartó en Biretix). Sigue esperando etiquetas: los EAN están en `cl/heliocare/match.json`.
- **Head & Shoulders**: haircode.es sigue con las mismas 6 fichas `hys-` (los 53 enlaces del
  sitemap incluyen las páginas de categoría; no hay fichas nuevas de ninguna marca P&G). Las
  webs de H&S de Reino Unido, Francia e Italia dan listas distintas para el mismo EAN, así
  que no valen (lo mismo que con Pantene). Sin fuente oficial española, no se amplía.

### Davines (es.davines.com) — abierta 2026-09-24, rehecha el mismo día: 134 productos, 189 códigos
Marca italiana (códigos `8004608…`). Tienda Shopify con una web por país; **manda la
española, es.davines.com**.
- **Lección: la web "internacional" (world.davines.com) va atrasada.** La primera versión
  (2026-09-24c, 173 códigos) salió de ahí. Al contrastar el OI Oil con la aportación de una
  usuaria se vio que es.davines.com (y uk, it, us) publican otra lista, con la fragancia
  nueva. Comparadas las dos webs código a código: de 145 códigos comunes, **38 tienen lista
  distinta** (OI Oil, Hand Balm, Body Wash, Hair Butter, champús y acondicionadores
  NATURALTECH, lacas, espumas…). Con la española, el galaxólido sale en 17 productos en vez
  de 8. Para cualquier marca con webs por país: **usar la del país, no la global**.
- **INCI completo** en la ficha (`specifics__list ingredients`), con una coletilla ("La
  información del producto incluida aquí puede estar sujeta a cambios…") que se quita.
- **EAN por tamaño** en el JSON-LD de la ficha (`gtin13` junto a su `sku`) y en el nombre de
  la foto (`Davines-<sku>-<nombre>-<EAN>-1.jpg`). Se cruzan: 7 tamaños de SU dan un EAN
  distinto en cada sitio, y 9 SKU (Rebalancing Shampoo, Liquid Spell, Curl Building Serum,
  Pliable Paste, Purifying Gel, Cleansing Nectar…) dan un EAN en la web española y otro en la
  internacional. Todos fuera.
- **Tamaños que solo trae la web internacional** (sobre todo los de viaje de 75 ml): se suman
  al producto español solo si la lista de las dos webs para ese producto es idéntica (15
  códigos). Si no coincide, fuera (Finishing Gum, Styling Paste, Intense Treatment,
  Replenishing Butter en su código internacional; en su código español sí están).
- Fuera también: monodosis de muestra (8 "sachet", algunas con fórmula anterior), kits,
  cofres, calendario y el estuche del champú sólido.
- Douglas ES no vende Davines: no hay segunda fuente, vale la web de la marca sola.
- Nombre: el de la marca (en inglés, con la gama en mayúsculas como la escribe Davines) +
  tipo en español + tamaños con la misma lista juntos. Errata corregida: "2-Bromo-2
  -Nitropropane-1,3-Diol" (bronopol, Purifying Shampoo). **La web española pega palabras**
  ("Basicbrown 17", "Hydrogenatedrapeseed Alcohol", "Glycerylolivate", "Disodiumedta"…,
  14 casos): se separan en la versión 2026-09-24e (`PEGADAS` en `dv/es/gen.py`), buscadas
  partiendo cada palabra desconocida en dos que ya existen en el resto del catálogo.
Scripts: `dv/es/crawl.py`, `dv/es/gen.py` (y los de la web internacional en `dv/`).

### Haruharu Wonder (haruharuwonder.com) — abierta 2026-09-24: 29 productos, 40 códigos (de 45 fichas)
Marca coreana (códigos `8809532…`, prefijo 880 de Corea: vale, como Erborian). La web es la
tienda Shopify de la marca y basta sola (misma regla que Nivea o Cocunat):
- **EAN por tamaño** en `/products/<handle>.js` (`variants[].barcode`) y en el JSON-LD
  (`gtin13`); `products.json` no lo trae.
- **INCI completo** en el modal "Full Ingredients" de la ficha
  (`#ingredientsModal … metafield-multi_line_text_field`).
- Se quitan las concentraciones que la marca intercala ("(2,000ppm)", "(5%)"), que además
  llevan comas y partirían la lista en la app. Erratas evidentes de la web corregidas
  ("Sodium Chlori de", "Hydroxyethylcell ulose", "Cydodextrin", "catearyl Olivate",
  "Ehtylhexylglycerin", "Sterois", "Zanthoxylum, Piperitum", "Cetearyl Alcohol C14-22
  Alcohols" sin coma…).
- Tamaños con la misma lista, juntos (tónicos 30/150/300 ml, esencia 30/120 ml, crema y su
  recarga…). Los tres Peptide Glowy Balm van separados porque cambian los colorantes.
- Nombre: gama (Black Rice, Centella, Black Bamboo, Rose PDRN) + nombre del producto + tipo
  en español + tamaños.
- **Fuera**: los dos solares Moisture Pure Mineral Relief (8809532221691) y Moisture Airyfit
  (8809532221707), porque la web publica una lista pasada por OCR y estropeada
  ("Propylheptyi", "Polyglycery1", "DibuyiAdipate Propanedial"…) y no se transcribe a ojo;
  el 10 Hyaluronic Cream sin perfume (8809532221721), cuya "lista" es texto de marketing;
  sets, cofres y accesorios sin código.
Scripts: `hh/crawl.py`, `hh/gen.py`, datos en `hh/db.json`.

### Ducray, Klorane y A-Derma (Pierre Fabre) — cerradas 2026-09-24: 228 productos, 228 códigos (de 241 fichas)
Las tres webs (`ducray.com/es-es`, `klorane.com/es-es`, `aderma.es`) son la misma plataforma
que Avène: `product.xml` en el sitemap, **EAN en la URL** (`/p/<slug>-<EAN>-<hash>`), INCI
en el panel `composition_inci`, nombre en el h1. Mismos scripts (`avene.py`, `gen_avene.py`
parametrizado en `pf/gen_pf.py`), con dos añadidos en `pf/prep.py`:
- **Klorane marca los ingredientes BIO con un asterisco** ("Water (Aqua)*"): se quita antes
  de comparar, porque partía el nombre y hacía que la lista pareciera rara.
- **Ducray y A-Derma no ponen la gama en el título** ("Champú de tratamiento anticaspa",
  "Crema calmante"): se antepone la gama sacada de la URL (Kelual DS, Keracnyl, Melascreen,
  Ictyane, Dexyane MeD…; Exomega Control, Epitheliale A.H, Biology AC, Dermalibour+…) para
  que el nombre identifique el producto. Klorane ya lleva la planta en el título.
- Ducray 59 de 62 (fuera: dos Anacaps, que son complementos alimenticios, y una segunda ficha
  de Dexyane MeD sin lista) · Klorane 105 de 109 (fuera: tres sin lista y la mascarilla
  Hidratación & Brillo, cuya ficha trae la lista en chino) · A-Derma 64 de 64.
- Dos fichas vivas con el mismo nombre y distinta fórmula, separadas por referencia como en
  Avène: Dexyane MeD Palpebral, Cutalgan roll-on, Klorane crema de ducha de cupuaçu.
- Los `3282…` que aparecen además en cada ficha son enlaces cruzados de la web, no otros
  tamaños: se ignoran (igual que en Avène).
Datos: `pf/<marca>_db.json` (crudo), `pf/<marca>_db2.json` (preparado), `pf/<marca>_new.json`.

### Pantene, Head & Shoulders, Herbal Essences y Aussie (P&G, haircode.es) — cerradas 2026-09-23: 43 productos, 43 códigos (de 46 fichas)
**La premisa de la cola era otra vía y no vale para champús**: info-pg.com (el circuito de
Fairy) es solo la web del Reglamento 648/2004, y para España lista 20 marcas de limpieza,
ninguna capilar. Los champús no tienen ficha del Anexo VII. La fuente buena es otra:
- **haircode.es**, la web capilar oficial de P&G España (pantene.es redirige ahí). Next.js;
  cada ficha lleva en `__NEXT_DATA__` → `props.pageProps.templateProps` el **`ean`** y el
  INCI completo en `ingredientsSection.ingredientsText`, además del `title` en castellano.
  El listado visible "Productos que amamos" solo enseña 20 fichas, pero **`/sitemap.xml`
  lista 46** (`/productos-que-amamos/<tipo>/<slug>`): 24 Pantene, 6 Head & Shoulders
  (`hys-…`), 9 Herbal Essences y 10 Aussie. Se han bajado las 46.
- **Los códigos son los de los envases españoles**: los tres Pantene de OBF con `en:spain` que
  coinciden (espumas Rizos y Ondas Perfectas, ampollas Repara & Protege) están en haircode.es
  con ese mismo EAN, y la transcripción de etiqueta de OBF de las ampollas es idéntica a la
  lista de la web salvo erratas de quien la tecleó. Las listas de Herbal Essences Hidratante y
  Reparador coinciden (sin alérgenos) con las italianas de haircode.it, otro EAN.
- **Fuera (3):** las tres lacas Pantene Pro-V (Fijación con Movimiento, Volumen Perfecto,
  Fijación Ultrafuerte) traen la misma lista de 15 ingredientes las tres; sin segunda fuente
  que lo confirme, regla de Sanex/Rexona, fuera.
- **Aussie no estaba en la cola**: se ha abierto porque sale de la misma fuente a coste cero y
  es champú de súper (Mariana decide si se queda).
- **Lo que NO hay que usar**: las otras webs de P&G se contradicen entre sí para el MISMO
  EAN. Para Head & Shoulders, headandshoulders.co.uk (85 fichas, `gtin` por tamaño e INCI en
  `ingredientsInfo`) y haircode.uk dan listas distintas en 6 de los 9 códigos comunes, y la
  etiqueta de OBF de Classic Clean 400 ml (8006540810538) es una tercera versión. H&S
  reformula y mantiene el EAN. Los 80 códigos británicos no se tocan: solo 3 están en OBF y
  ninguno con `en:spain`. **headandshoulders.es no existe** (DNS) y herbalessences.es
  redirige a lacuponera.es (cupones). haircode.fr e .it tienen sus propias gamas con EAN
  franceses/italianos.
Nombres: el `title` de la ficha sin la marca delante ("Pro-V Espuma Rizos Perfectos", "Classic
Champú 2 en 1", "Champú Hidratante"). Scripts/datos: `pg/hc/` (fichas `p/`, `products.json`,
`<marca>_final.json`), `pg/hs/uk/` y `pg/hcuk/` (webs UK, solo para contraste), `pg/hcit/`,
`pg/obf_all.json` (302 códigos de OBF de las tres marcas).

### Biretix (Cantabria Labs) — cerrada 2026-09-23: 5 productos, 8 códigos (de 15 fichas en cantabrialabs.es)
Cantabria Labs (antes IFC, Santander). **La web del fabricante NO publica el INCI**: ni
cantabrialabs.es (solo "Composición" con los activos y el CN de farmacia), ni .com, ni .pt.
Vía: INCI por dos fuentes independientes idénticas + EAN por dos fuentes.
- **EAN.** API de Douglas ES (`/api/v2/products/<id>?fields=FULL`, campo `ean`; 11 fichas con
  ids `5011406034…5011990016`, variantes del Cleanser por `variant=`) y **SkinLovers**
  (Shopify, `"barcode"` en el JSON de la ficha, 11 fichas): coinciden código a código.
  farmacianautic (EAN en la URL) añade 8436574365856 (Tri-Active Gel, envase nuevo) y
  8436574361582 (Isorepair, también en Douglas). Cosmetis publica `ean` en `<meta>`.
- **INCI.** incidecoder (22 fichas, varias duplicadas por dos subidas distintas), SkinLovers
  (bloque "Ingredients" con erratas de transcripción), shop-apotheke.de (con erratas y una
  ficha, Mask, que copia la lista del Gel) y la **etiqueta de OBF** del Cleanser 200 ml. Se
  guarda la lista limpia de incidecoder (o la etiqueta) cuando otra fuente da la misma lista
  ingrediente a ingrediente (erratas de transcripción toleradas, nunca un ingrediente de más
  o de menos).
- **Entran (5):** Cleanser 200/400/recarga (etiqueta + incidecoder ×2 + SkinLovers ×3),
  Micropeel (incidecoder ×2 + SkinLovers), Tri-Active Gel (incidecoder + SkinLovers + la lista
  de la usuaria), Tri-Active Spray (incidecoder + SkinLovers) e Isorepair crema (incidecoder ×2
  + shop-apotheke).
- **Fuera (10) y por qué:**
  - **Duo Gel** 8470001859853: dos fórmulas en circulación (incidecoder/shop-apotheke con
    Phenoxyethanol, 27; SkinLovers con BHT/BHA/1,2-Hexanediol y sin Phenoxyethanol, 34). La
    nueva solo la da una fuente: hace falta foto de etiqueta.
  - **Double Correction Serum** 8470002160040: incidecoder ×2 (43) y SkinLovers (44) difieren
    en un ingrediente (Sphingomonas Ferment Extract). Foto de etiqueta.
  - **Gel** 8470001723505: incidecoder y shop-apotheke dan la misma lista, pero lleva
    Methyl/Ethyl/Butylparaben y huele a fórmula antigua; sin etiqueta actual, fuera.
  - **Hydramat Day SPF30** 8470001999726 (solo incidecoder), **Hydramat Day SPF30 Color**
    8436574364477 (solo SkinLovers), **Mask** (incidecoder 33 vs 38), **Oil Control Solution**
    8470002119451, **Tri-Active Intensive Gel** 8436574365849, **Tri-Active Control Gel**,
    **Isorepair Bálsamo Labial** 8436574365481 e **Isorepair Limpiador Cremoso** 8436574365498:
    sin lista en ninguna fuente o con una sola.
  - Códigos descartados: 8437002567255 (Nautic, Cleanser 200 ml, prefijo de otra empresa) y
    8032715360546 (Nautic, spray, envase italiano).
- Con una foto de etiqueta (Buscados o Mariana) cualquiera de los 10 entra en cinco minutos:
  los EAN ya están.
Nombres: los de cantabrialabs.es sin "Biretix" delante. Scripts/datos: `brx/` (Douglas
`dg/`, incidecoder `ic/`, SkinLovers `sl/`, Nautic `nt/`, shop-apotheke `sa/`, foto OBF
`obf_ingr.jpg`, `biretix_final.json`).

### Asevi (asevicompany.com) — cerrada 2026-09-21: 135 productos, 167 códigos (de 203 fichas en su portal)
Asevi Home Brands (antes Pons Químicas, Xàbia): fregasuelos, detergentes, suavizantes,
ambientadores, desinfectantes. Primera marca de limpieza curada **entera desde el
fabricante**: publica el EAN y la lista completa de cada referencia en su propia web.
- **Dónde está.** Buscador "Introduce el EAN" en el pie de cada ficha (`?s=<EAN>&post_type=productoean`),
  que enlaza a `/fichas/listado_ingredientes/<EAN>.pdf`. El listado completo sale de la API
  de WordPress: `/es/wp-json/wp/v2/productoean?per_page=100&page=N&_fields=id,title,acf`
  (203 entradas; `acf.codigo_ean` y `acf.archivo`). Los PDF son "Lista de Ingredientes según
  648/2004/CE, 907/2006/EC": nombre INCI por línea, en orden, sin rangos; los descriptivos
  sin INCI van en castellano ("Poliester modificado", "Fosfonato de disodio"). Tres fichas
  inglesas van en formato de bandas de concentración (CAS · nombre químico · INCI): se toma
  el INCI, y el nombre químico si no lo hay.
- **Acceso.** La web va detrás de un reto JavaScript (SiteGuarding, `/.well-known/sgcaptcha/`),
  no un captcha visual: Playwright con el Chromium del contenedor lo pasa en ~30 s y deja la
  cookie `_I_`, que luego vale para `curl` durante horas (`asv/pw.js`, `asv/ck.sh`).
- **Lectura de los PDF.** Dos generadores distintos: fuentes CID con ToUnicode (hex) y PDF de
  Word con fuentes WinAnsi (cadenas literales); algunos linealizados guardan la página 2 antes
  que la 1 y otros parten `/Contents` en 8 trozos. `pdfcid.py` cubre los dos formatos, ordena
  por `/Kids` y corta líneas por posición vertical; `asv/parse_all.py` separa nombre y lista
  (cabeceras en castellano, rumano, polaco e inglés) y une las líneas partidas de los nombres
  químicos largos (paréntesis sin cerrar, guion o coma al final).
- **Qué queda fuera (36 de 203).** 14 fichas cuyo PDF da 404 en el portal (Higienizante Hogar y
  Textil, los tres Fregasuelos Desinfectante, Desinfectante Textil 720/1440, Multiusos Gerpostar
  95 ml, Limpiador y Baños Gerpostar 1280 ml, Antihollín Asevi-IQ y tres Consum). 21 fichas de
  **marca blanca Consum** (fregasuelos, suavizantes, detergente, quitamanchas, perfumador):
  son de Consum, no de Asevi; están bajadas y leídas por si algún día se abre esa marca.
  Y `8411582881550` "PARDOSELI ASEVI CIAN": el portal le enlaza el PDF de Mio (el
  identificador del producto dentro del PDF no coincide con el título), así que no se sabe
  qué lista es la suya. Fuera.
- **Envases de fuera de España.** 66 códigos son envases de Rumanía (`PARDOSELI`, `BALSAM`,
  `DET RUFE`, `DEO`…), Polonia (`PL …`) o en inglés (`… FLOOR CLEANER`, `FABRIC CONDITIONER`).
  EAN oficial y lista oficial igual que los españoles, así que entran; el nombre va en
  castellano con "(envase de Rumanía)" / "(envase de Polonia)" / "(envase en inglés)". Cuando
  la lista coincide exactamente con la del envase español (Fregasuelos Naranja rumano, Suavizante
  Azul inglés…), el código se suma a la ficha española. Los nombres químicos descriptivos en
  rumano, polaco o inglés se han pasado al castellano que usan las fichas españolas del mismo
  producto (`TR` en `asv/gen_asevi.py`), y "perfumes" de las fichas inglesas es `Parfum`.
- **Agrupación.** Lista idéntica = una ficha con todos sus tamaños (Fregasuelos Naranja 900 ml,
  950 ml, 1 L y 1,15 L; Suavizante Azul 60, 84 y 125 lavados). Lista distinta = ficha aparte
  aunque sea el mismo producto (Fregasuelos Mio 900 ml lleva 25 ingredientes y los otros
  tamaños 27; Desinfectante Baños 750 ml y 1,1 L difieren). `COLORANT` se escribe `Colorante`
  como en Fairy; las comas internas de los nombres químicos se quitan para no partir la lista.
- **Rarezas oficiales que se dejan tal cual.** El Ambientador Primavera declara
  "((3-(trifluorometil)piridin-2-il)sulfonil)carbamato de metilo"; el Desincrustante rumano
  solo lleva Aqua, Hydrochloric Acid y colorante; el Limpión Lavadoras son tres sales. Es lo
  que publica el fabricante.
- **El vinagre de limpieza pedido por una usuaria (8411582242320) no está en el portal**: sigue
  fuera (ver PEDIDOS 2026-09-18).
- **Versión 2026-09-21b.** Tres fragmentos de nombre químico partido ("(9CI", "*) 6b]…") unidos a su
  línea, y traducidos los restos en rumano/polaco/inglés ("Kopolimer" → Copolímero, "Polisiloxan" →
  Polisiloxano, "(R)-p-menta-1,8-dieno" → Limonene, que es la misma molécula). Al unificarse
  nombres, tres listas extranjeras pasaron a coincidir con la española: 138 → 135 fichas, mismos 167 códigos.
- **Falsos negativos (2026-09-21).** "Hexamethylindanopyran" es el nombre INCI del galaxólido (HHCB)
  y la app solo conocía "Galaxolide": añadido el alias (salta en 27 fichas de Asevi y en 4 de
  Avène/Deliplus que ya lo llevaban). Pendientes de decisión de Mariana: Didecyldimonium Chloride
  (DDAC, 20 fichas; mismos estudios en ratón que el cloruro de benzalconio ya recogido), TBHQ
  (4 fichas; actividad estrogénica/androgénica muy débil en ToxCast), Fosfato de tris(2-butoxietilo)
  (TBOEP, 1 ficha) y los alcoholes etoxilados tipo Pareth/Trideceth (la ficha de tensioactivos
  etoxilados solo reconoce "laureth"). OTNE (Tetramethyl acetyloctahydronaphthalenes, 41 fichas):
  sensibilizante y tóxico acuático, sin datos de disrupción; no se añade.
- **Otros riesgos (no disruptores), añadidos a esa lista de la app el 2026-09-21:** acrilato de etilo
  (IARC 2B; los cuatro perfumadores de ropa) y glutaraldehído (sensibilizante respiratorio; suavizante
  Rosa Mosqueta). Vistos y descartados por falta de clasificación relevante: metanol, 2-butoxietanol,
  xileno, DBNPA (sensibilizante cutáneo), IPBC.
- **Revisión de la detección (2026-09-21).** Pasado el detector de la app sobre las fichas.
  Avisos verdaderos que sorprenden pero están en la ficha oficial: Diethanolamine en casi
  todos los detergentes, Diethyl Phthalate en Max Higyenic, Toluene en el ambientador WC
  Purple rumano, Resorcinol en varios perfumadores y suavizantes, Lilial en 23 fichas.
  Falsos positivos corregidos en la app: Clordecona por "Methyl Nonyl Ketone" (coincidencia
  difusa kepone/ketone), Estireno por "Sodium Styrene/Acrylates Copolymer", Propilenglicol
  por "Propylene Glycol Butyl Ether"; y 33 fichas caían en Cuidado personal porque la app
  conocía "friegasuelos" pero no "fregasuelos", "limpiahogar" ni "perfumador de ropa".
  "Poliester modificado" (polímero antirredeposición de los detergentes, soluble en agua, sin
  evidencia de disrupción endocrina) disparaba "Microplásticos (poliéster)": excluido por
  decisión de Mariana (2026-09-21); el aviso sigue para fibras de poliéster/polipropileno.
Nombres: "<tipo> <variante> <tamaño>" ("Fregasuelos Mio (950 ml, 1 L y 1,15 L)", "Suavizante
Hipoalergénico Talco Rosa (60, 84 y 125 lavados)", "Detergente Max Active 50 lavados"); las
dosis "44D"/"40W" del portal son lavados. Scripts: `asv/pw.js`, `asv/ck.sh`, `pdfcid.py`,
`asv/parse_all.py` (→ `asv/parsed.json`), `asv/gen_asevi.py` (→ `asv/asevi_final.json`),
`asv/pdf/` (187 PDF).

### Rexona (rexona.com/es) — cerrada 2026-09-14: 14 productos, 14 códigos (de 25 con EAN en la web)
Unilever, misma plataforma que Dove y misma vía (`dvcurl.sh`, listado paginado
`/es/productos.html?page=productlist-31138391e9~N`, ficha `/es/p/<slug>.html/<GTIN-14>`,
código e INCI en `data-productvariants`). Diferencias con Dove:
- **La web solo tiene 25 fichas** (5 páginas de 6), una variante por ficha (sin tamaños
  agrupados), y **todas traen INCI**. El sitemap `/es/sitemap.xml` no lista fichas. La ficha
  responde con cualquier slug (`/es/p/x.html/<GTIN-14>`): se probaron así los 165 códigos
  Rexona de OBF y de rexona.com/pt que no están en el listado, y ninguno tiene ficha en `/es`.
- Códigos: `872…`/`871…`/`8718…`/`8711…`/`8712…` (Unilever Países Bajos) y **EAN-8
  auténticos de Unilever** `59…`/`50…` en roll-on y aerosol de 100 ml (como en Dove). Ningún
  `84…` ni `0…`.
Qué decidió lo que entra (regla de Sanex/Neutrogena: solo lo que no está contradicho):
- **Fórmula antigua (Lilial)**: roll-on Men Invisible 87340679, roll-on mujer Invisible Aqua
  87340631 y aerosol Men Cobalt 48h 8710447493861 traen Butylphenyl Methylpropional. Fuera.
- **Ficha ≠ etiqueta de OBF del mismo código**: roll-on Men Cobalt Dry 50096954 (la web da
  Citral e Hydroxycitronellal; la etiqueta, Eugenol) y aerosol Cotton Dry 8720181213991 (la
  etiqueta lleva Alpha-Isomethyl Ionone y no Coumarin). Fuera.
- **La web repite listas entre aromas distintos** (como Sanex): Cotton Dry aerosol = Marine
  Fresh Men, Bright Bouquet aerosol = Invisible Pure aerosol, Cobalt Dry roll-on = Quantum Dry
  roll-on. Una de cada par es una copia y no hay etiqueta que decida: fuera las seis.
- **rexona.com/pt** (38 fichas, mismo marcado) sirve para contrastar el mismo código, pero
  **va por detrás**: para las cremas 8718114202372 y 8711600504141 da la lista antigua con
  Lilial mientras la ficha `/es` coincide con la etiqueta de OBF. Cuando `/es` y `/pt` dan
  listas distintas para un código sin etiqueta que decida (aerosol Men Invisible Black & White
  72h 8720181213854, stick Men Cobalt 73103714, roll-on Quantum Dry 59095460), fuera.
- Entran las 14 restantes: 4 con etiqueta de OBF idéntica (cremas Clean Scent mujer y Men,
  Stress Control, roll-on Cotton Dry), 1 con `/pt` idéntica (roll-on Uplifting & Fresh) y 9
  con lista única en la web y sin contradicción.
- Los 95 códigos Rexona de OBF que no están en `/es` son en su mayoría envases franceses
  (lotes, comprimidos de 100 ml, MotionSense) y no se han tocado: sin ficha `/es` no hay
  fuente oficial para España. Si alguno sale en "Buscados" con foto de etiqueta, se cura por
  el código como se hizo con Deliplus.
Nombres: "Antitranspirante <formato> <gama> <horas> <aroma> <tamaño>", con "Men" delante en
los de hombre. Un aroma × formato × género = una entrada, con su tamaño en el nombre.
Scripts: `dvcurl.sh`, `gen_rexona.py` (→ `rexona_merged.json`), `rexona_db.json` (fichas
`/es`), `rexona_pt_db.json` (fichas `/pt`), `obf_rexona_site.json`.

### Elmex (elmex.es / elmex.fr) — abierta 2026-09-15: 2 productos, 2 códigos (pedidos por una usuaria)
CP GABA, grupo Colgate-Palmolive. Misma plataforma AEM que Colgate pero con **plantilla
"pim-pdp"**: la ficha HTML solo trae plantillas Handlebars (`{{activeIngredients}}`) y el
contenido se carga por JavaScript desde una consulta GraphQL persistida:
- `<body data-product="/content/dam/cp-sites-aem/pim-cf/oral-care/elmex/<locale>/<gama>/<slug>">`
  → `https://www.elmex.<tld>/graphql/execute.json/astra/productpath;path=<esa ruta>`. Devuelve
  `data.productDataModelByPath.item` con `name`, `activeIngredients` (lista con explicación de
  cada ingrediente, en HTML `<li>`), `upc` (EAN, solo en algunas fichas; en elmex.fr también
  como `data-ean` en el botón "Où acheter") y `skus` (el itemId de Colgate, p. ej. 61035324).
- **El campo `ingredients` no vale**: es un texto por defecto repetido en todas las fichas
  (la lista del elmex Kids con Olaflur). La lista real es `activeIngredients`, y hay que
  contrastarla con una etiqueta porque es explicativa y puede omitir alérgenos (la del
  Anti-Caries Original francés no los trae; la etiqueta suiza sí).
- elmex.es tiene 5 fichas de producto (Anti-Caries Professional, Sensitive Professional, Kids,
  Junior y dos colutorios) sin EAN; elmex.fr, unas 40 con EAN en varias. Se han curado solo los
  dos códigos pedidos; la gama completa queda como candidata (ver la cola).
Scripts: `dvcurl.sh`; los JSON de GraphQL en `ped15/gq_*.json`.

### Natulim (natulim.com) — abierta 2026-09-16: 1 producto, 1 código (pedido por una usuaria)
Ecollim Holdings, marca española de limpieza ecológica (Shopify). La caja solo lleva los rangos
del Anexo VII, pero **la ficha web publica la lista completa** en la FAQ "¿Cuáles son los
ingredientes?" (un nombre por párrafo, con el nombre técnico entre paréntesis en algunos).
`/products/<slug>.json` da variantes y SKU interno, **no el EAN**: el código vino del escaneo.
Se traduce al nombre INCI/inglés habitual (Sodium Percarbonate, TAED, Subtilisin…) como se hizo
con Fairy. Candidatos si alguien los pide: lavavajillas a mano, tiras de detergente, quitamanchas.

### Carrefour (marca blanca) — abierta 2026-09-16: 1 producto, 1 código (pedido por una usuaria en Francia)
carrefour.fr (Datadome) y carrefour.es (Cloudflare) devuelven 403 a todo. La única fuente es la
etiqueta: OBF tiene fotos por código y, en este caso, dos generaciones bajo el mismo EAN. Se
cura código a código desde "Buscados" con la foto más reciente; no hay vía para recorrer la marca.

### Erborian (L'Occitane) — cerrada 2026-09-16: 18 productos, 30 códigos (vía farmacias) (pedido por una usuaria)
Sin web utilizable: es.erborian.com, fr, uk e it son Salesforce Commerce Cloud tras **DataDome**
(desafío interactivo `geo.captcha-delivery.com`, no pasa ni con Playwright). La vía que funciona
es **Douglas**: `https://www.douglas.es/api/v2/products/<código>?fields=FULL` devuelve `ean`,
`ingredients` (lista completa, en español y con guiones), `variantCount` y `variantOptions`;
el código de producto se saca del buscador `douglas.es/es/search?q=…` (`"code":"1171943"`). La
lista de Douglas se contrasta con incidecoder (inglés). Códigos `8809255…` (Corea), no `3760…`.
Sirve para cualquier marca selectiva sin web accesible (Sephora y las webs de L'Occitane).
**Intento de completar la marca (2026-09-16, versiones 2026-09-16c/d): 5 códigos, los 5 que vende Douglas España.**
- Douglas España solo vende **4 productos** de Erborian (búsqueda `q=erborian`: 46 en Alemania,
  4 aquí). Douglas Alemania tiene la gama entera pero su API responde 403 (Akamai) y la ficha
  HTML no lleva los datos; Douglas Francia devuelve HTML en vez de JSON. Sephora, Primor, Druni,
  Notino y skinsort bloquean.
- **Skin Therapy Eye 15 ml (8809255788358): ENTRA.** Douglas e incidecoder ("Skin Therapy Eye
  Cream") dan los mismos 56 ingredientes en el mismo orden.
- **Skin Therapy Sérum Light (10 ml 8809255788464 y 30 ml 8809255788402): ENTRA (2026-09-16d,
  decisión de Mariana)** con la lista de Douglas (45 ingredientes) como fuente única: incidecoder
  no tiene el sérum (su "Skin Therapy" es otra crema). Los dos tamaños comparten lista.
- **BB Crème au Ginseng travel 15 ml Beige (8809255786460): ENTRA (2026-09-16d, decisión de
  Mariana)** con la lista de Douglas (45), que es la fórmula "mejorada" (Ethylhexyl Salicylate,
  Hexyl Laurate, Tin Oxide, Alcohol); todas las fichas de incidecoder y la etiqueta de OBF
  (8809255780376) son fórmulas anteriores. Solo este tono y tamaño: los demás no están en Douglas ES.
- Ojo con las listas de Douglas: vienen con nombres pegados ("TITANIUMDIOXIDE", "HEXYLLAURATE")
  y guiones dentro de nombres (PEG-10, 1,2-Hexanediol) iguales al separador: no se pueden usar
  sin contrastarlas con una lista bien formada.

**Vía de farmacia (2026-09-16, versión 2026-09-16e): 18 productos, 30 códigos.** Mariana preguntó
por las farmacias y ahí estaba la gama entera:
- **farmaelglobo.com** (47 fichas Erborian) y **farmacianautic.com** (62) publican el **EAN en la
  URL** de cada ficha (`…-8809255787078.html`), 69 códigos distintos entre las dos, tonos y
  tamaños incluidos. El Globo no trae INCI; **Nautic sí**, bajo el epígrafe `INCI`, en el formato
  de L'Occitane (separado por " - "). Farmaciamarket, Farma2go y Parafarmacia-online no tienen
  fichas útiles; Dosfarma, Farmaciasdirect y Morlán no venden la marca.
- **Nautic copia listas entre fichas**: sus seis fichas de BB Crème (Clair/Nude/Doré × 15/40 ml)
  llevan, palabra por palabra, la lista de la CC Crème con Centella. Por eso de Nautic **solo
  entra lo que confirma incidecoder o Douglas** con la misma lista (comparación sin alérgenos,
  como en Colgate): Bamboo Super Serum, CC Body, CC Crème Clair/Doré/Caramel (Doré y Caramel
  llevan además los alérgenos del perfume), CC Dull Correct, CC Eye Clair y Doré, CC Water Clair
  y Doré (4 códigos), Centella Barrier Cream, Cleansing Balm, Cleansing Gel, Cleansing Oil, Red
  Serum, SOS Patch, y los otros 4 tonos del Super BB Concealer (Clair, Doré, Caramel, Chocolat),
  con la misma lista que el Nude. El Sérum Light queda confirmado: Nautic y Douglas dan los mismos
  45.
- **Solo en Nautic, sin segunda fuente: NO ENTRAN (decisión de Mariana, 2026-09-16: solo lo
  confirmado por dos fuentes). Quedan apuntados por si aparece etiqueta o ficha oficial:** Ginseng Power
  Cream 50 ml (8809255786842, 56), Ginseng Power Eye 15 ml (8809255786873, 44), Skin Hero Eye
  10 ml (8809255787696, 48), Skin Hero Glow 15 ml (8809255788112, 43; El Globo tiene el de 40 ml
  8809255788105), Skin Therapy Sérum en Aceite 30 ml (8809255787368, 39), Super BB Crème
  Clair 40 / Nude 15 / Doré 15 y 40 (8809255787078, 8809255787122, 8809255787160,
  8809255787153, 48; El Globo tiene Nude 40 ml 8809255787115), CC Crème Deep 15 ml
  (8809255787993, 48) y Porcelain 15 ml (8809255787955, 41), CC Red Correct 15 y 45 ml
  (8809255788679, 8809255788662, 44; El Globo tiene el de 40 ml 8809255783773). Listas únicas
  (no copiadas de otra ficha), pero Nautic ya ha demostrado que copia.
- **Fuera:** BB Crème (lista copiada), Centella Crème 50 ml (a Nautic le faltan Beta-Glucan y
  T-Butyl Alcohol frente a incidecoder), Ginseng Micro Shot, Glow y Matte Moisturizer, Water
  Serum, Water Shot Mask (sin INCI en la ficha), kits y neceseres (`3253581…`, varios productos).
Scripts: `erb/ph_urls.json` (URL+EAN de las dos farmacias), `erb/ph/` (fichas), `erb/ic/`
(incidecoder), `erb/nautic_final.json`, `erborian_merged.json`.
**Cerrada por Mariana el 2026-09-16 tal cual**: entran los tonos hermanos (concealer, CC Eye
Doré, CC Water) con la lista del tono confirmado, y la BB Crème Beige de viaje con la lista de
Douglas; los 15 de Nautic sin segunda fuente, fuera.

### Kérastase (L'Oréal Professionnel) — cerrada 2026-09-16: 47 productos, 59 códigos (de 165 en Douglas)
**Sin web utilizable**: kerastase.es, .fr, .co.uk y .it están tras el Cloudflare interactivo
("Un momento…", no lo pasa Playwright ni con varias cargas); kerastase.com (EE. UU.) sirve el
sitemap pero las fichas dan 403; kerastase.pt da 500. Misma vía que Erborian: **Douglas + incidecoder**.
- Douglas: el buscador `douglas.es/es/search?q=kerastase&page=N` (páginas desde 1; la 0 y la 1
  son la misma; 132 resultados, 3 páginas) da en el JSON de cada tile la URL del producto base
  (`/es/p/<10 dígitos>`); `/api/v2/products/<base>?fields=FULL` lista las variantes en
  `variantOptions` y `/api/v2/products/<variante>` da `ean`, `name` (tamaño), `baseProductName`
  e `ingredients`. 148 productos base, 254 variantes, **165 de Kérastase** (el buscador mezcla
  IT Cosmetics, Lancôme y sets de Douglas `4045129…`).
- La lista de Douglas viene del feed de L'Oréal con sus manías: separadores `•`/`●`/comas,
  prefijo `1199765 M - INGREDIENTS:`, códigos F.I.L. al final (`C240231/1`), "Aqua/Water/Eau",
  erratas ("Phenoxyethaol", "Helanthus") y, en 27 fichas, texto descriptivo en español en vez de
  la lista. Se compara con incidecoder (191 fichas de la marca, listado por `?offset=N`)
  **tolerando esos artefactos** (tokens partidos, erratas con similitud ≥ 0,9, alérgenos que a
  incidecoder le faltan) y se guarda la lista limpia de incidecoder.
- Resultado: 67 variantes con lista idéntica en las dos fuentes. Fuera de esas: 3 sets/estuches,
  y **3 copias de Douglas detectadas por el contraste**: "Le Parfum" 30 ml con la lista del
  champú Hydra-Glaze, "Masque Densité" con la lista del champú Bain Densité, y los 6 códigos de
  Chroma Respect con una sola lista (la del Bain Riche) para el Bain y el Bain Riche, que en
  incidecoder son fórmulas distintas: no se puede asignar y no entran. Douglas también copia,
  aunque menos que Nautic.
- **57 variantes con lista distinta de incidecoder** (Bain Force Architecte, Baño Regenerador,
  Curl Manifesto Gelée/Huile/Masque, Scalp & Hair Serum, Oléo-Relax, Cicagloss, L'Huile
  Originale…): incidecoder va por detrás (fórmulas antiguas con parabenos y Lilial) o no tiene
  el producto. Con la regla de "solo lo confirmado" no entran; sus códigos están en
  `ks/dg_match2.json`. Otras 41 no traen lista en Douglas.
- Nombres: gama + nombre francés del producto + tipo en español + tamaños; los tamaños con la
  misma lista van juntos (250, 500 y recambio). Códigos `3474636…`/`3474637…`/`3474630…`.
Scripts: `ks/dg_base.txt`, `ks/dgb/` y `ks/dg/` (API de Douglas), `ks/ic/` (incidecoder),
`ks/dg_match2.json` (contraste), `kerastase_merged.json`.

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
| Cosmia (Alcampo/Auchan) | — | sí, API de compraonline.alcampo.es (`bop`), con pausas | composición en auchan.fr, mismo EAN | ver su apartado |
| Mustela | Shopify (`products.json`, 117 fichas) | sí, `barcode` en `/products/<handle>.js` | sí, en la ficha | web oficial sola; ver su apartado |
| Nenuco | sí (`sitemap-0.xml`, 10 fichas) | **no** | sí | código solo con nombre y tamaño exactos o lista idéntica |
| Evax · Tampax (P&G) | solo 3 fichas de Tampax; las de Evax por la web | sí, en el bloque de reseñas de cada ficha (`bvData.eaNs`), mezclado entre familias | no hay INCI: composición en dos artículos de evaxtampax.es | código solo si es único de una familia; ver su apartado |
| Ausonia (P&G) | sí (`sitemap.xml`, 153) | sí (`gtin` por variante) | composición solo de la gama Discreet | ver "Higiene íntima y menstrual" |
| Endocare (Cantabria Labs) | — | no; SkinLovers y Douglas ES | no; incidecoder (SkinLovers transcribe mal) | dos fuentes idénticas o nada; ver su apartado |
| Vaseline · TRESemmé (Unilever) | Vaseline: solo vaseline.com/uk | sí, por variante (`data-productvariants`) | sí, por variante | como Dove, `dvcurl.sh` |
| Gliss (Henkel) | sí (schwarzkopf.es) | sí, `gtin` + código en el archivo de la foto | sí | ver su apartado; Syoss sin códigos |
| KH-7 | — | no: Consum/Alcampo/Mercadona (UFI) | ficha 648/2004 en PDF en kh7.es | ver su apartado |
| Bosque Verde (Mercadona) | — | API de Mercadona | ficha 648/2004 del fabricante (Francisco Aragón, SPB), contrastada con la etiqueta | ver su apartado |
| Lacer | laceroralhealth.com (web dental oficial) | no: C.N. por formato → EAN 847000+C.N.; `8430340…` por tiendas | sí | ver su apartado |
| Oral-B (P&G) | oralb.es | sí | **no** (ni UK/DE/PT) | dos fuentes idénticas; ver su apartado |
| Catrice · essence (Cosnova) | sí (sitemap de producto por país, `es-es`) | sí, `gtin13` en el JSON-LD y `gtin` en el objeto de producto | sí, `c_inciList` del mismo objeto (o referencia `$xx` en los datos de Next.js) | ver su apartado |
| Davines | Shopify por país: **es.davines.com** (la global va atrasada) | sí, `gtin13` + `sku` en el JSON-LD y en el nombre de la foto | sí, completo en la ficha | web española; ver su apartado |
| Haruharu Wonder | Shopify (`products.json`, 45 fichas) | sí, `barcode` en `/products/<handle>.js` | sí, modal "Full Ingredients" | web oficial sola; ver su apartado |
| Ducray · Klorane · A-Derma | sí (`product.xml`: 67 · 110 · 64) | sí, **en la URL** | sí (`composition_inci`) | plataforma de Avène; gama desde la URL en Ducray y A-Derma; ver su apartado |
| ISDIN | sí (310 fichas) | **no**; EAN en la API de Douglas ES y en el JSON de SkinLovers | sí | código solo si la lista de la tienda es idéntica a la ficha de isdin.com; ver su apartado |
| Bioderma | sí (108 fichas) | no; `barcode` en el JSON de SkinLovers | **no**; SkinLovers e incidecoder | dos fuentes idénticas o nada (50 códigos); antes incidecoder + foto de OBF; ver sus apartados |
| Sesderma | sí (~120 fichas ES) | no; Douglas ES y SkinLovers | no; SkinLovers, Douglas e incidecoder | dos fuentes idénticas o nada (11 códigos); ver su apartado |
| SkinCeuticals | — (Cloudflare en todas las webs de la marca) | no; `barcode` en el JSON de SkinLovers | no; SkinLovers (lista INCI al final del bloque "Ingredients") e incidecoder | dos fuentes idénticas o nada (21 códigos); ver su apartado |
| Neutrogena | sí (`/sitemap.xml`) | sí | sí | EAN en `data-mm-ids`; INCI en `data-sb-field-path="product.ingredients"` (a veces un `<p>` por ingrediente); ver su apartado |
| Cien (Lidl) | API lidl.es / lidl.de | sí | solo lidl.de, y solo lo que vende online (4 solares) | OBF con criba de erratas por vocabulario + lidl.de (ver su apartado) |
| Kérastase | — (Cloudflare interactivo en .es/.fr/.uk/.it) | sí, en la API de Douglas (`ean` por variante) | sí en la API de Douglas (`ingredients`, con artefactos del feed de L'Oréal), contrastada con incidecoder | ver su apartado |
| Erborian | — (DataDome en todas las webs de la marca) | sí: **EAN en la URL** de farmaelglobo y farmacianautic (69 códigos) y en la API de Douglas | sí en farmacianautic (`INCI`) y Douglas, pero Nautic copia listas entre fichas: solo con incidecoder/Douglas idéntico | ver su apartado |
| Natulim | sí (Shopify `sitemap_products_1.xml`, ~40) | **no** (SKU interno) | sí, lista completa en la FAQ de la ficha | código del escaneo; ver su apartado |
| Carrefour | — (403 en .fr y .es) | — | — | solo etiqueta de OBF por código; ver su apartado |
| Elmex | sí (`sitemap.xml`; 5 fichas ES, ~40 FR) | en `upc`/`data-ean` de algunas fichas FR; ninguna ES | sí, en `activeIngredients` por GraphQL (`/graphql/execute.json/astra/productpath;path=`), explicativa; el campo `ingredients` es un texto por defecto | ver su apartado |
| Rexona | no (solo home); listado paginado por id de componente (25 fichas) | sí (en la URL y en `data-productvariants`) | sí en las 25, pero 3 con Lilial y 3 pares de aromas con lista repetida | vía Dove; contraste con etiqueta OBF y con rexona.com/pt; ver su apartado |
| Dove | solo categorías | sí (en la URL y en `data-productvariants`) | 1 de cada 3 fichas, y a veces fórmula antigua | listado paginado por id de componente; ver su apartado |
| Fairy (P&G) | info-pg.com vía Contentful (354 fichas ES) | **no** | sí, lista completa Anexo VII | EAN de OPF emparejado por nombre exacto del envase; ver su apartado |
| Sanytol (AC Marca) | sí (`page-sitemap.xml`, 36) | sí, en el nombre de la imagen principal | **no**; la lista está en los PDF FIC de sanytol.fr (mismo código de fórmula) y tras login en reach.grupoacmarca.com | ver su apartado |
| L'Oréal Paris | sí (2075 URL, sin las páginas de tono) | sí (`gtin13` JSON-LD; tonos en `oap-product-variant-selector`) | sí (`additionalProperty` Ingredients), salvo tintes y ~100 fichas vacías | ver su apartado |
| Maybelline | por comprobar | por comprobar | por comprobar | misma plataforma que L'Oréal Paris: reusar sus scripts (ver su apartado) |
| Eroski | tienda tras reCAPTCHA interactivo (solo desde navegador) | **no** (solo id interno; el buscador acepta EAN) | sí, en texto (`feature-text-ingredients`) | códigos de "Buscados" o fotos → ficha por EAN → pegar bloque; ver su apartado |
| Sanex | sí (`sitemap.xml`, 63 fichas; Akamai: `dvcurl.sh` en serie) | **no** (solo SKU interno) | sí, tabla INGREDIENTE/PROPÓSITO (54 fichas; 5 traducidas al español; geles Neutro con lista repetida) | códigos de OBF por INCI idéntico o por nombre solo con envase ES/PT; ver su apartado |
| NYX | **no** (Cloudflare); fichas a fuerza bruta por ID `/p/NYX_nnn.html` con Playwright | **UPC-A de 12 dígitos** por tono (`data-js-pid`), que es `0800897…` en EAN-13 | sí, por tono, en el popin `Product-Information?cid=pdp-popin-ingredient&pid=` | Salesforce Commerce Cloud, no la plataforma de L'Oréal Paris; ver su apartado |
| Colgate | sí (`sitemap.xml`, 50 fichas; `dvcurl.sh` en serie) | **no** (`itemId` interno) | sí, en `<meta name="ingredientList">` (28 fichas, con alérgenos del aroma) | códigos de OBF solo por lista idéntica (sin alérgenos); ver su apartado |
| Essie | sí (`sitemap.xml`, 253 fichas, una por tono) | sí, `product-id` del acordeón de ingredientes (EAN-8 `30…`, `3600…` y UPC `0…`) | sí, en el acordeón (141 fichas; 10 traducidas; misma lista por gama) | plantilla antigua de L'Oréal, sin JSON-LD; ver su apartado |
| Maybelline | sí (758 URL, solo 113 fichas) + enlaces de categoría | sí (`gtin13` + `data-variant-ean` por tono en la misma ficha) | sí, una lista por ficha con "puede contener" | scripts de L'Oréal Paris; ver su apartado |
| Sensodyne | no se ha rastreado: un producto pedido por una usuaria | código UK `5054563…` | sí, en sensodyne.com/es-es (lista oficial) | marca con gama: candidata a curar entera |
| Instituto Español | **no**: Cloudflare interactivo (curl y Playwright) | — | — | creada vacía; ver PEDIDOS POR LAS USUARIAS |
| Sol de Janeiro | no se ha rastreado: un solo producto pedido por una usuaria | UPC de EE. UU. `0810912…` | sí, en soldejaneiro.com (lista vigente) | ver PEDIDOS POR LAS USUARIAS |
| Freshly Cosmetics | sí (`sitemap_products_ES.xml`, 118 fichas) | **no** | sí, botones `more-information-ingredients-pdp` (64 fichas) | EAN por Douglas, emparejado por lista idéntica; ver su apartado |
| Cocunat | `/products.json` (143) sin barcode ni INCI | **sí**, `gtin` en `api-less.cocunat.com/api/products/<handle>` | sí, `ingredients` en esa API (58) | API oficial de la marca; Douglas da listas antiguas; ver su apartado |
| Heliocare (Cantabria Labs) | sí (61 fichas en cantabrialabs.es) | **no** (solo CN); Douglas ES + SkinLovers | **no**; SkinLovers e incidecoder | dos fuentes idénticas o nada; ver su apartado |
| Pantene · Head & Shoulders · Herbal Essences · Aussie | sí (`haircode.es/sitemap.xml`, 46 fichas; el listado visible solo enseña 20) | **sí** (`templateProps.ean` en `__NEXT_DATA__`) | **sí**, completo (`ingredientsSection.ingredientsText`) | web capilar oficial de P&G España; las webs UK/FR/IT se contradicen entre sí por EAN; ver su apartado |
| Biretix (Cantabria Labs) | sí (`sitemap.xml` de cantabrialabs.es, 15 fichas) | **no** (solo CN); EAN en la API de Douglas ES y en el JSON de SkinLovers | **no** (solo activos); INCI en incidecoder, SkinLovers y shop-apotheke, más etiqueta OBF | dos fuentes idénticas o nada; ver su apartado |
| Asevi | sí (WP REST `productoean`, 203 fichas) tras reto JavaScript (SiteGuarding → Playwright, cookie `_I_`) | **sí**, en cada ficha (`acf.codigo_ean`) | sí, lista completa Anexo VII en PDF por EAN (`/fichas/listado_ingredientes/<EAN>.pdf`; dos formatos de PDF) | **cerrada, 167 códigos**; ver su apartado |
| Consum (marca blanca) | portal de Asevi (22 fichas `CONSUM …`) | **sí** (`acf.codigo_ean`) | sí, PDF Anexo VII por EAN | igual que Asevi; ver su apartado |
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

## Estado (2026-09-25)
6225 códigos en 67 marcas: NYX 999 · **Bosque Verde 16** · **KH-7 10** · **Lacer 68** · **Oral-B 7** · **essence 740** · **Catrice 677** · **Vaseline 29** · **Gliss 29** · **TRESemmé 18** · L'Oréal Paris 520 · Maybelline 455 · Nivea 235 ·
Garnier 234 · Asevi 167 · Avène 162 · LRP 160 · Eucerin 137 · Essie 125 · Vichy 111 · **Davines 189** · **Klorane 105** · CeraVe 73 ·
**ISDIN 68** · **A-Derma 64** · **Ducray 59** · Kérastase 59 · Neutrogena 56 · **Bioderma 50** · Cocunat 39 · Erborian 30 · Cien 29 · Dove 28 ·
**SkinCeuticals 21** · **Haruharu Wonder 40** · **Consum 19** · Pantene 18 · Deliplus 16 · Colgate 16 · Sanex 15 · Rexona 14 · Fairy 12 · Freshly 11 ·
**Sesderma 11** · Aussie 10 · Herbal Essences 9 · Biretix 8 · Head & Shoulders 6 · Sanytol 5 · Eroski 5 ·
Heliocare 5 · **Endocare 4** · **Cosmia 115** · **Mustela 58** · **Tampax 33** · **Evax 9** · **Ausonia 5** · **Lactacyd 1** · **Nenuco 3** · Elmex 2 · Sol de Janeiro 1 · Sensodyne 1 · Niyok 1 · Philip Martin's 1 · Natulim 1 ·
Carrefour 1. Ninguno de los 4285 productos está sin INCI (las compresas y tampones llevan la composición del fabricante). Instituto Español sigue vacía.
ISDIN ampliada de 25 a 68 códigos con EAN de Douglas/SkinLovers cruzados con isdin.com (ver su apartado).
Asevi cerrada con 167 códigos (135 fichas): primera marca de limpieza entera desde el fabricante (ver su apartado).
Eroski: la tienda da INCI pero no EAN; se llena con los códigos de "Buscados" (ver su apartado).
Sanex cerrada con 15 códigos: la web da INCI sin EAN y OBF solo confirma 15 (ver su apartado).
NYX cerrada con 999 códigos, todos `0800897…` (UPC-A de NYX; excepción a la regla 3, ver su
apartado). **Hay que compilar la app**: el escáner ahora normaliza los UPC-A de 12 dígitos.
Colgate cerrada con 13 códigos: la web da la lista sin EAN y OBF solo confirma 13 (ver su apartado).
Essie cerrada con 125 códigos (28 son UPC `0…` de essie clásico, misma excepción que NYX; ver su apartado).
Rexona cerrada con 14 códigos de 25: la web da EAN e INCI en todo, pero 3 listas son fórmula
antigua y 8 están contradichas o repetidas entre aromas (ver su apartado).
Pedidos del 15-09: 2 de 4 curados (Elmex, marca nueva); el Sanytol francés y el brownie, fuera.
Erborian (aportación manual del 16-09): EAN encontrado en Douglas, 30 códigos vía farmacias online (EAN en la URL) contrastadas con incidecoder; 15 códigos con lista solo en Nautic quedan fuera por decisión de Mariana (ver su apartado).
Pedidos del 16-09: 4 de 6 curados (Sanex y Fairy como huecos; Natulim y Carrefour como marcas
nuevas); el Neutrogena francés descatalogado, fuera; Vicks a la espera de decisión.
Portal REACH de AC Marca: Mariana ha pedido la cuenta (15-09); cuando llegue, Sanytol entera.
Kérastase cerrada con 59 códigos vía Douglas + incidecoder (ver su apartado).
Siguientes de la cola: Redken y Cosmia (Alcampo).
