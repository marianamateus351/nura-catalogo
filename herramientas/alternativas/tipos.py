"""Reglas de clasificación por nombre para alternativas.json (contrato con la app, 2026-10-07).
Se aplican al nombre del producto en minúsculas y sin tildes, en este orden: gana la primera regla
cuya expresión 'casa' encaja y cuya 'excluye' no. Un nombre ambiguo ("Crema", sin decir cara o
cuerpo) se queda sin tipo: mejor fuera que en el tipo equivocado."""
import re, unicodedata
def sin_tildes(s): return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()
CATEGORIAS = [('cuidado-personal', 'Cuidado personal'), ('hogar', 'Hogar')]
TIPOS = {
 'Cuidado personal': [
  # (clave, nombre en plural, casa, excluye) — el ORDEN decide los casos dobles
  ('lubricante', 'Lubricantes', r'lubricante', r''),
  ('higiene-intima', 'Higiene íntima', r'(gel|jabon|espuma|pastilla|limpiador|lavado|solucion|mousse)[^,]*intim|intim[^,]*(gel|jabon|limpiador)|higiene intima|vulvar|(crema|mascarilla)[^,]*intim', r'toallita|lubricante|preservativo'),
  ('pasta-dientes', 'Pastas de dientes', r'pasta (de )?dientes|toothpaste|dentifric|crema dental|gel dental|pasta dental', r''),
  ('desodorante', 'Desodorantes', r'desodorante|antitranspirante|\bdeo\b|deodorant|antiperspirant', r'pies|zapat|ropa|hogar'),
  ('esmalte', 'Esmaltes y cuidado de uñas', r'esmalte|laca de unas|\bnail\b|top ?coat|base ?coat|\btopper\b|tratamiento de unas|quitaesmalte|cuticula|pulido de unas|\bunas\b|semipermanente|diluyente|base fortificante', r'manos'),
  ('mascara-pestanas', 'Máscaras de pestañas', r'\bmascara\b|pestanas|\blash|telescopic|extensionist', r'mascarilla|desmaquill|ceja|\bbrows?\b'),
  ('ojos-cejas', 'Sombras, lápices de ojos y cejas', r'sombra|eyeliner|eye liner|delineador|lapiz de ojos|lapiz (de )?cejas|kohl|khol|kajal|paleta de sombras|eyeshadow|cejas|\bbrows?\b|eyebrow', r'desmaquill|contorno'),
  ('labial', 'Labiales', r'labial|barra de labios|pintalabios|lipstick|\bgloss\b|brillo de labios|tinte de labios|lip (tint|oil|balm|liner|marker|stain|pencil)|perfilador de labios|rotulador de labios|balsamo de labios|labios|levres|lip booster', r'contorno de labios|desmaquillante'),
  ('colorete', 'Coloretes, bronceadores e iluminadores', r'colorete|\bblush|bronceador|bronzer|iluminador|highlighter|contouring|\bcontour\b|paleta de contorno', r'autobronce|gotas|mascarilla|crema (facial|hidratante|iluminadora)|serum|aceite|tratamiento|eye contour|contour cream'),
  ('base-maquillaje', 'Bases, correctores y polvos', r'base de maquillaje|base en polvo|fondo de maquillaje|foundation|fond de teint|\bbb cream\b|\bcc cream\b|base fluida|base luminosa|corrector|concealer|polvos|polvo (fijador|compacto|suelto|matificante|bronceador)|powder|prebase|\bprimer\b|fijador de maquillaje|setting spray|cushion', r'brocha|pincel|esponja|manchas|anti-?pigment|limpia|contorno de ojos|imperfecciones|dientes|texturiz|cabello|capilar|hair'),
  ('protector-solar', 'Protectores solares', r'protector solar|fotoprotector|pantalla solar|\bspf ?\d|\bfps ?\d|solar.*spf|solar \d\d|locion solar|leche solar|spray solar|fluido solar|crema solar|sun ?(screen|cream)', r'after ?sun|autobronce|bronceador'),
  ('champu', 'Champús', r'champ[uú]|shampoo', r'seco|perro|mascota'),
  ('acondicionador', 'Acondicionadores y mascarillas capilares', r'acondicionador|conditioner|mascarilla capilar|balsamo capilar|hair mask|apres-shampooing|mascarilla[^,]*(cabello|pelo)|mascarilla nutritiva al mango|mascarilla 3 en 1 al cupua|nutricion mascarilla', r'perro|mascota'),
  ('capilar', 'Tratamientos capilares', r'sin aclarado|leave[- ]in|serum capilar|aceite capilar|tratamiento capilar|anticaida|crecimiento del cabello|cabello|capilar|rizos|cuero cabelludo|texturiz|root color|raices|crecimiento|curl booster', r'champ|acondicionador'),
  ('gel-ducha', 'Geles de ducha', r'gel (de )?(ducha|bano)|gel de bano y ducha|ducha y bano|aceite de ducha|crema de ducha|espuma de ducha|jabon (liquido )?de ducha|shower gel|body wash|aceite de bano', r'intim'),
  ('crema-manos', 'Cremas de manos y pies', r'crema (de |para )?manos|manos y unas|hand cream|crema (de |para )?pies|creme mains|\bmains\b|\bpies\b', r''),
  ('autobronceador', 'Autobronceadores', r'autobronce', r''),
  ('granos', 'Parches y tratamientos anti-granos', r'parche|patch|anti-?granos|granitos|gel secante|anti-?puntos negros|corrector de imperfecciones', r'ojos|ojeras|\beyes?\b|balsamo'),
  ('crema-corporal', 'Cremas y aceites corporales', r'crema corporal|locion corporal|leche corporal|balsamo corporal|hidratante corporal|manteca corporal|crema (de|para el) cuerpo|body (lotion|cream|milk|oil)|aceite corporal|aceite seco|cara y cuerpo|locion hidratante|hidrolocion|after ?sun|atoderm (creme|intensive gel)|antiestrias|anti-estrias|embarazo|masaje', r'solar|spf|autobronce|micelar|limpia|desmaquill'),
  ('contorno-ojos', 'Contornos de ojos', r'contorno de (los )?ojos|contorno ojos|eye cream|ojeras|cuidado de ojos|(gel|serum|crema|parches)( de)? ojos|parpados|palpebral|tratamiento[^,]* ojos|serum[^,]* ojos|eye patch|eye contour|contour cream', r'desmaquill|demaquill|lapiz|sombra|delineador|mascara'),
  ('limpiador-facial', 'Limpiadores faciales', r'limpiador|limpiadora|agua micelar|micelar|desmaquillante|leche limpiadora|aceite limpiador|balsamo limpiador|espuma limpiadora|gel limpiador|jabon facial|limpieza facial|cleanser|demaquillant|cleansing|nettoyant|lavante', r'corporal|cuerpo|intim|bano|cocina|hogar|dientes|lengua|brocha|pincel|toallita'),
  ('exfoliante', 'Exfoliantes', r'exfolia|peeling|\bpeel\b|scrub|gommage', r'pies'),
  ('mascarilla-facial', 'Mascarillas faciales', r'mascarilla|\bmask\b|\bmasque\b', r'capilar|cabello|pelo|intim|pestan'),
  ('tonico', 'Tónicos, esencias y brumas', r'tonico|toner|bruma|\bmist\b|agua termal|esencia\b|essence|locion tonica|discos|\bpads?\b|agua de uva|agua de rosas', r''),
  ('serum', 'Sérums y aceites faciales', r's[eé]rum|serum|ampolla|ampoule|concentrado|booster|\d ?%|corrector de manchas|antimanchas|aceite facial|squalane|argan oil', r'cabello|capilar|pelo|pestan|ceja|labio|corporal|cuerpo|manos|unas|urea|toallita|\bagua\b|pso\b|gel-?crema|\bcream\b'),
  ('crema-facial', 'Cremas faciales', r'crema (facial|hidratante|de dia|de noche|antiedad|antiarrugas|calmante|nutritiva|reparadora|matificante|reafirmante|iluminadora|rica|ligera|regeneradora|activa)|gel[- ]crema|crema gel|fluido (facial|hidratante)|emulsion (facial|hidratante)|hidratante facial|crema cara|\bcream\b|gel hidratante|gel-creme|gel creme|\bcreme\b|aqua-?gel|\bemulsion\b|moisturiz|daily lotion|anti-?imperfecciones|matificante|toleriane (dermallergo|sensitive)|face cream|day cream|night cream', r'corporal|cuerpo|manos|pies|ojos|contorno|labio|bebe|panal|cabello|solar|spf|color|bb |cc |tono|ducha'),
  ('emoliente', 'Bálsamos y cremas reparadoras', r'balsamo|baume|emoliente|relipidizante|reparador|cicaplast|cicalfate|cicavit|antirrascado|barrera aislante|crema aislante|cica\b|cicatri|aquaphor|pomada|vaselina|protecting jelly|cold cream|linimento|panal|costra lactea|spray secante', r'labi|levres|limpiador|desmaquill|espum'),
 ],
 'Hogar': [
  ('suavizante', 'Suavizantes', r'suavizante|softener', r''),
  ('lavavajillas', 'Lavavajillas', r'lavavajillas|lavaplatos|dishwash', r'abrillantador|limpiamaquinas|limpia ?maquinas|ambientador|\bsal\b'),
  ('detergente', 'Detergentes para la ropa', r'detergente|colada|laundry', r'lavavajillas|limpia ?lavadoras|limpion|higienizante de lavadoras|parquet|marmol|gres|terracota'),
  ('multiusos', 'Multiusos', r'multiusos|multisuperficies?|multi-superficie|limpiahogar', r''),
  ('lejia', 'Lejías', r'lejia', r'desatasc'),
  ('desatascador', 'Desatascadores', r'desatasc', r''),
  ('limpiador-cocina-bano', 'Limpiadores de cocina y baño', r'limpiador[^,]*(cocina|bano|horno|acero|paella|vitro|gres)|desincrust', r'lavavajillas|lavadora'),
  ('aditivo-colada', 'Quitamanchas y aditivos para la colada', r'quitamanchas|potenciador de lavado|blanqueador|percarbonato|tierras de sommieres|oxi (clean|white)', r'lavavajillas'),
  ('basicos-limpieza', 'Básicos de limpieza (ácido cítrico, cristales de soda…)', r'acido citrico|cristales de soda|bicarbonato|sal de acedera', r''),
  ('ambientador', 'Ambientadores', r'ambientador|perfumador de (ambiente|hogar)|difusor|mikado|vela perfumada|vela aromatica|scented candle|air freshener', r'ropa'),
 ],
}
# Marcas que solo hacen un tipo de producto: si el nombre no lo dice, lo dice la marca.
MARCA_TIPO = {'manucurist': ('esmalte', 'Esmaltes y cuidado de uñas')}
def tipo_de(nombre, categoria, marca_key=None):
    n = sin_tildes(nombre)
    for key, label, casa, excluye in TIPOS.get(categoria, []):
        if re.search(casa, n) and not (excluye and re.search(excluye, n)):
            return key, label
    return MARCA_TIPO.get(marca_key or '', (None, None))
