# nura-catalogo

Catálogo curado de productos para la app **Nura** (bienestar hormonal + escáner
de disruptores endocrinos).

Este repo es **público a propósito**: la app lo lee en tiempo de ejecución para
saber qué marcas/productos puede importar, **sin necesidad de publicar un build
nuevo cada vez**. El código de la app vive en otro repo privado; aquí solo hay
**datos de producto** (nombres, códigos de barras, ingredientes INCI y fotos),
que no son secretos.

## Archivos
- `catalogo.json` — el catálogo. La app lo lee de la URL "raw":
  `https://raw.githubusercontent.com/marianamateus351/nura-catalogo/main/catalogo.json`
- `fotos/` — fotos de producto para cuando Open*Facts no trae imagen (ver
  `fotos/README.md`).

## Formato de `catalogo.json`
```
{
  "version": "AAAA-MM-DD",
  "marcas": [
    {
      "key": "identificador-sin-espacios",
      "nombre": "Nombre de la marca",
      "productos": [
        {
          "nombre": "Nombre del producto",
          "include": ["subcadenas", "que", "deben", "estar"],
          "exclude": ["subcadenas", "que", "no", "deben", "estar"],
          "inci": "Ingrediente 1, Ingrediente 2, …",
          "foto": "(opcional) URL raw de una foto en fotos/"
        }
      ]
    }
  ]
}
```

El emparejado con Open*Facts es por subcadenas distintivas del nombre (todas las
`include` presentes, ninguna `exclude`), sobre el nombre "aplastado" (minúsculas,
sin acentos ni signos). Conservador, para no confundir variantes.
