# Fonty lokalne

Strona używa dwóch krojów z licencją SIL Open Font License: Instrument Serif i Figtree.
Ze względu na RODO ładujemy je z własnego serwera, nie z Google Fonts.

## Jak dodać pliki

```bash
cd fonts
npm pack @fontsource/instrument-serif @fontsource-variable/figtree
mkdir is fig && tar -xzf fontsource-instrument-serif-*.tgz -C is && tar -xzf fontsource-variable-figtree-*.tgz -C fig
cp is/package/files/instrument-serif-latin-400-normal.woff2 is/package/files/instrument-serif-latin-ext-400-normal.woff2 .
cp is/package/files/instrument-serif-latin-400-italic.woff2 is/package/files/instrument-serif-latin-ext-400-italic.woff2 .
cp fig/package/files/figtree-latin-wght-normal.woff2 fig/package/files/figtree-latin-ext-wght-normal.woff2 .
rm -rf is fig *.tgz
```

Potem w `index.html` usuń trzy linie oznaczone `TYLKO PODGLĄD` (Google Fonts) i odkomentuj `fonts/fonts.css` oraz dwa `preload`.

Uwaga: potrzebne są oba podzbiory. `latin` ma podstawowe litery, `latin-ext` polskie znaki (ą, ę, ł, ś, ż, ź…).
