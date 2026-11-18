# Audyt UI/UX landingu Tamarillo (v7)

Data: 18.11.2026. Metoda: skill `web-review` (plugin website-design), strona renderowana w przeglądarce przy 375, 768 i 1440 px, nawigacja klawiaturą, automatyczny pomiar kontrastu, kolejności nagłówków, rozmiaru celów dotykowych i wagi plików. Porównanie z bazą UXKIN pominięte (serwer niepodłączony).

Uwaga: na zrzutach były fonty zastępcze (środowisko bez internetu), więc oceny typografii dotyczą skali i hierarchii, nie rysunku krojów.

## Co już działa

- Hero mówi, co to jest i dla kogo; jedna główna akcja (telefon) widoczna bez przewijania na każdej szerokości.
- Brak przewijania w poziomie na 375 px; nagłówki w poprawnej kolejności (H1 → H2 → H3); wszystkie zdjęcia mają `alt`.
- Kontrast tekstu ≥ 4,5:1 we wszystkich miejscach poza podpisami w galerii (te stoją na ciemnym gradiencie, więc w praktyce są czytelne).
- Widoczny fokus z klawiatury, link „Przejdź do treści”, etykiety pól, `prefers-reduced-motion`.
- Tytuł strony, opis, dane strukturalne LocalBusiness, favicon.

## 1. Musi być poprawione (blokuje zaufanie lub łamie zasady projektu)

| # | Gdzie | Problem | Poprawka |
|---|---|---|---|
| 1.1 | Opinia, kontakt, oferta | Widoczne placeholdery: „[Wybrana opinia klienta…]”, „[Imię], [okazja], [rok]”, „[godziny kontaktu]”, „[od … zł / os.]”. Na stronie premium jeden nawias kwadratowy niszczy wiarygodność całości. | Do czasu dostarczenia treści: ukryć blok opinii, usunąć godziny, przy weselu zostawić „cena po rozmowie”. W HTML zostawić komentarze `<!-- TODO -->`. |
| 1.2 | `<head>` | Fonty ładowane z serwerów Google. To przesyła IP odwiedzającego do Google (wyrok LG München z 2022 r.), sprzeczne z zasadą „minimum danych / RODO” z constitution. Dodatkowo plik CSS z Google blokuje render. | Hostować Instrument Serif i Figtree lokalnie (woff2, tylko latin + latin-ext), `preload` dla 2 plików, `font-display: swap`, fallback z `size-adjust`, żeby nie było skoku układu. |
| 1.3 | Hero (LCP) | Logo to PNG 176 KB, zdjęcie hero 175 KB JPG; łącznie ok. 350 KB przed pierwszym wyświetleniem. Cała strona ładuje ok. 6 MB obrazów, wszystko w JPG. | Logo w SVG (lub WebP ~25 KB). Zdjęcia w AVIF/WebP przez `<picture>`, cel: hero < 120 KB, miniatury < 10 KB. |

## 2. Powinno być poprawione (to oddziela „ładnie” od „premium”)

| # | Gdzie | Problem | Poprawka |
|---|---|---|---|
| 2.1 | Wszystkie zdjęcia | Zdjęcia z telefonu mają różny balans bieli: jedne ciepłe i pomarańczowe (croissanty), inne zimne i szare (podgrzewacze). Obok siebie wyglądają przypadkowo. To największy pojedynczy czynnik odbioru „premium” w gastronomii. | Jedna korekta koloru dla wszystkich zdjęć (ciepła, lekko wyciszona, podniesione cienie), tak jak robią to marki z jednym „presetem”. Docelowo sesja zdjęciowa. |
| 2.2 | Oferta | Chip „wycena” powtórzony 6 razy w szarych prostokątach. Wygląda jak niedokończony cennik i wizualnie zrównuje pozycje z ceną i bez ceny. | Cena tylko tam, gdzie jest liczba, krojem szeryfowym jak w menu („od 255 zł”). Przy reszcie bez etykiety albo drobne „na zapytanie” w kolorze tekstu pomocniczego, bez tła. |
| 2.3 | Opisy w ofercie | Opisy 15 px w kolorze #625C53: drobne i blade obok tytułów 34 px. Duży skok skali bez stopnia pośredniego. | Opisy 16–17 px, interlinia 1,5; maks. 60 znaków w linii. |
| 2.4 | Telefon (375 px) | Na pierwszym ekranie są 3 przyciski telefonu naraz: ikona w nagłówku, przycisk w hero i przyklejony pasek. Powtórzenie osłabia każdy z nich. | Pasek dolny pokazywać dopiero, gdy przycisk z hero zniknie z ekranu (bez animacji, po prostu się pojawia). Ikona w nagłówku może zostać. |
| 2.5 | Nagłówek + hero | Logo jest widoczne dwa razy na pierwszym ekranie (napis w nagłówku i pełne logo w hero). | Na górze strony nagłówek bez logo; napis pojawia się w nagłówku dopiero po przewinięciu za hero (zmiana stanu, bez animacji). |
| 2.6 | Dowód społeczny | „98% klientów poleca nas na Facebooku” bez liczby opinii i linku. Ogólne procenty czyta się jak marketing. | „98% poleceń z 29 opinii na Facebooku” jako link do opinii. Docelowo 2–3 prawdziwe opinie z imieniem i okazją. |
| 2.7 | Brak sekcji o ludziach | Logo podpisane „by Maciej Nikielski”, a na stronie nie ma ani słowa o nim ani o zespole. Catering premium sprzedaje szefa kuchni. | Sekcja „Kto gotuje”: portret, 3–4 zdania, rok startu, podpis kaligraficzny. Wymaga zdjęcia i tekstu od klienta. |
| 2.8 | „Wystarczy jeden telefon” | Trzy numerowane kroki to najczęstszy szablonowy element landingów. Sekcja zajmuje pełny ekran, a mówi to samo co hero. | Skrócić do jednego zdania nad numerem w sekcji kontaktu albo połączyć z sekcją opinii. |
| 2.9 | Wesele | „cena po rozmowie” trzy razy dużą złotą kursywą: wygląda jak wypełniacz. | Jedno zdanie nad trzema menu („Cenę wesela podajemy po rozmowie”), a w kolumnach zamiast ceny nazwa formy podania (talerz / platery). |
| 2.10 | Galeria (telefon) | Podpisy dań pokazują się tylko po najechaniu myszką, więc na telefonie ich nie ma. | Na ekranach dotykowych (`@media (hover:none)`) podpis zawsze widoczny pod zdjęciem. |
| 2.11 | Formularz | Błąd pokazuje się tylko jako tekst pod przyciskiem; pole z błędem nie jest oznaczone. | `aria-invalid` i obramowanie pola, komunikat przy polu (`aria-describedby`), fokus przenoszony na pierwsze błędne pole. |

## 3. Szlif

| # | Gdzie | Poprawka |
|---|---|---|
| 3.1 | Stopka | Dodać obszar działania (Wejherowo, Reda, Rumia, Gdynia, Sopot, Gdańsk), godziny i telefon: lepsze lokalne SEO i domknięcie strony. |
| 3.2 | Stopka, linki | Linki 14 px z celem dotykowym < 24 px; zwiększyć odstępy na telefonie. |
| 3.3 | Podgląd w social media | `og:image` to logo na białym tle. Lepiej zdjęcie bufetu 1200×630 z logo. |
| 3.4 | Sekcja BOX (768 px) | Na tablecie zdjęcie boxu zajmuje cały ekran przed treścią; ograniczyć do proporcji 4:3. |
| 3.5 | Złoto | Złoty gradient na całej szerokości sekcji BOX jest mocny. Do decyzji: zostawić albo spokojniejszy szampański odcień (#EFE3C6) z gradientem tylko na cienkim pasku u góry. To kwestia gustu, nie błąd. |

## Kolejność proponowanych prac

1.1 → 1.2 → 1.3 → 2.1 → 2.2 + 2.3 → 2.4 + 2.5 → 2.6 → 2.8 + 2.9 → 2.10 + 2.11 → szlif. Punkt 2.7 czeka na materiały od klienta.

## Status wdrożenia (v8, 18.11.2026)

| # | Status | Co zrobiono |
|---|---|---|
| 1.1 | wdrożone | Placeholdery usunięte; w HTML zostały komentarze TODO (opinie, godziny). Wesela: „na zapytanie”. |
| 1.2 | przygotowane | `fonts/fonts.css` i `fonts/README.md` gotowe (latin + latin-ext, `font-display: swap`, fallbacki z `size-adjust`). Środowisko nie miało internetu, więc pliki woff2 trzeba pobrać jednym poleceniem z README; do tego czasu podgląd korzysta z Google Fonts (oznaczone `TYLKO PODGLĄD`). |
| 1.3 | wdrożone | Wszystkie zdjęcia w WebP z JPG jako zapasem (`<picture>`), preload obrazu LCP, logo WebP 50 KB zamiast PNG 176 KB, miniatury 4–5 KB. Łączna waga WebP ok. 3 MB zamiast 6 MB JPG. Docelowo logo w SVG. |
| 2.1 | wdrożone | Wspólny preset kolorów (`tools/grade.py`): wyrównanie balansu bieli, ciepły ton, lekkie wyciszenie, podniesione cienie. |
| 2.2, 2.3 | wdrożone | Ceny krojem szeryfowym tylko przy liczbach, „na zapytanie” bez tła; opisy 16 px, kolor #3D3832, maks. 60 znaków. Na telefonie cena pod tytułem. |
| 2.4, 2.5 | wdrożone | Pasek „Zadzwoń” pojawia się dopiero po zniknięciu przycisku z hero; napis w nagłówku dopiero po zniknięciu logo z hero. Obie zmiany bez animacji. |
| 2.6 | częściowo | „98% poleceń w 29 opiniach na Facebooku” z linkiem. Prawdziwe opinie czekają na klienta. |
| 2.7 | czeka | Sekcja „Kto gotuje”: potrzebne zdjęcie i tekst. |
| 2.8 | wdrożone | Sekcja z 3 krokami usunięta; jedno zdanie o procesie w sekcji kontaktu. |
| 2.9 | wdrożone | Wesele: jedno zdanie o cenie, w kolumnach forma podania. |
| 2.10 | wdrożone | Na ekranach dotykowych podpisy galerii zawsze widoczne. |
| 2.11 | wdrożone | Błąd przy polu, `aria-invalid`, fokus na pierwszym błędnym polu, zgoda podświetlona. |
| 3.1, 3.2 | wdrożone | Stopka w 4 kolumnach: kontakt, obszar dowozu, informacje, dane firmy; większe cele dotykowe. |
| 3.3 | wdrożone | `og:image` 1200×630 ze zdjęciem bufetu. |
| 3.4 | wdrożone | Na tablecie zdjęcie boxu 4:3. |
| 3.5 | do decyzji | Złoty gradient bez zmian. |
