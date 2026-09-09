# Fotos del catálogo curado

Fotos de producto para cuando Open*Facts **no** trae imagen. El importador usa
primero la foto de Open*Facts y, si no hay, la que enlacemos aquí.

## Cómo añadir una foto
1. Sube el archivo a esta carpeta. Nómbralo con el **código de barras**:
   `fotos/<codigo>.jpg` (p. ej. `3337875736749.jpg`).
2. En `catalogo.json`, en la entrada del producto, añade el campo `foto`
   con su URL "raw" de GitHub:

   ```json
   {
     "nombre": "H.A. Intensifier",
     "include": ["intensifier"],
     "exclude": ["glycan", "multiglycan"],
     "inci": "…",
     "foto": "https://raw.githubusercontent.com/marianamateus351/nura-catalogo/main/fotos/3337875736749.jpg"
   }
   ```

Añadir/actualizar fotos así **no requiere build** (se leen del catálogo online),
igual que añadir marcas o productos. Formatos: JPG o PNG, tamaño moderado
(idealmente < 300 KB) para que carguen rápido en la app.
