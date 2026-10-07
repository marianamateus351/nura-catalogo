"""Reglas de clasificación por nombre para alternativas.json (contrato con la app, 2026-10-07).
Se aplican al nombre del producto en minúsculas y sin tildes, en este orden: gana la primera regla
cuya expresión 'casa' encaja y cuya 'excluye' no. Un nombre ambiguo ("Crema", sin decir cara o
cuerpo) se queda sin tipo: mejor fuera que en el tipo equivocado."""
import re, unicodedata
def sin_tildes(s): return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()
CATEGORIAS = [('cuidado-personal', 'Cuidado personal'), ('hogar', 'Hogar')]
TIPOS = {
 'Cuidado personal': [
  # (clave, nombre en plural, casa, excluye)
  ('lubricante', 'Lubricantes', r'lubricante', r''),
  ('higiene-intima', 'Higiene íntima', r'(gel|jabon|espuma|pastilla|limpiador|lavado|solucion|mousse)[^,]*intim|intim[^,]*(gel|jabon|limpiador)|higiene intima', r'toallita|lubricante|preservativo'),
  ('pasta-dientes', 'Pastas de dientes', r'pasta (de )?dientes|dentifric|crema dental|gel dental|pasta dental', r''),
  ('desodorante', 'Desodorantes', r'desodorante|antitranspirante|\bdeo\b', r'pies|zapat|ropa|hogar'),
  ('labial', 'Labiales', r'labial|barra de labios|pintalabios|lipstick|\bgloss\b|brillo de labios|tinte de labios|lip (tint|oil|balm)|balsamo de labios', r'contorno de labios|perfilador|desmaquillante'),
  ('base-maquillaje', 'Bases de maquillaje', r'base de maquillaje|fondo de maquillaje|foundation|\bbb cream\b|\bcc cream\b|base fluida', r'prebase|primer|brocha|pincel|esponja'),
  ('protector-solar', 'Protectores solares', r'protector solar|fotoprotector|pantalla solar|\bspf ?\d|\bfps ?\d|solar.*spf|solar \d\d|locion solar|leche solar|spray solar|fluido solar|crema solar|sun ?(screen|cream)', r'after ?sun|autobronce|bronceador'),
  ('champu', 'Champús', r'champ[uú]|shampoo', r'seco|perro|mascota'),
  ('acondicionador', 'Acondicionadores', r'acondicionador|conditioner|mascarilla capilar|balsamo capilar', r'perro|mascota'),
  ('gel-ducha', 'Geles de ducha', r'gel (de )?(ducha|bano)|gel de bano y ducha|ducha y bano|aceite de ducha|crema de ducha|espuma de ducha|jabon (liquido )?de ducha|shower gel', r'intim'),
  ('crema-corporal', 'Cremas corporales', r'crema corporal|locion corporal|leche corporal|balsamo corporal|hidratante corporal|manteca corporal|crema (de|para el) cuerpo|body (lotion|cream|milk)', r'solar|spf|autobronce'),
  ('limpiador-facial', 'Limpiadores faciales', r'limpiador|limpiadora|agua micelar|micelar|desmaquillante|leche limpiadora|aceite limpiador|balsamo limpiador|espuma limpiadora|gel limpiador|jabon facial|limpieza facial|cleanser', r'corporal|cuerpo|intim|bano|cocina|hogar|dientes|lengua|brocha|pincel'),
  ('serum', 'Sérums', r's[eé]rum|serum|ampolla|concentrado facial|booster', r'cabello|capilar|pelo|pestan|ceja|labio|corporal|cuerpo|manos|unas'),
  ('crema-facial', 'Cremas faciales', r'crema (facial|hidratante|de dia|de noche|antiedad|antiarrugas|calmante|nutritiva|reparadora|matificante|reafirmante|iluminadora|rica|ligera|regeneradora|activa)|gel[- ]crema|crema gel|fluido (facial|hidratante)|emulsion (facial|hidratante)|hidratante facial|crema cara', r'corporal|cuerpo|manos|pies|ojos|contorno|labio|bebe|panal|cabello|solar|spf|color|bb |cc |tono'),
 ],
 'Hogar': [
  ('suavizante', 'Suavizantes', r'suavizante', r''),
  ('lavavajillas', 'Lavavajillas', r'lavavajillas|lavaplatos', r'abrillantador|limpiamaquinas|limpia ?maquinas|ambientador|\bsal\b'),
  ('detergente', 'Detergentes para la ropa', r'detergente|colada', r'lavavajillas|limpia ?lavadoras|limpion|higienizante de lavadoras|parquet|marmol|gres|terracota'),
  ('multiusos', 'Multiusos', r'multiusos|multisuperficies?|multi-superficie', r''),
  ('ambientador', 'Ambientadores', r'ambientador|perfumador de (ambiente|hogar)|difusor|mikado|vela perfumada', r'ropa'),
 ],
}
def tipo_de(nombre, categoria):
    n = sin_tildes(nombre)
    for key, label, casa, excluye in TIPOS.get(categoria, []):
        if re.search(casa, n) and not (excluye and re.search(excluye, n)):
            return key, label
    return None, None
