# 001 – Strona wizytówka (landing) Catering Tamarillo

Status: szablon HTML v8 (iteracja 8, po audycie UI/UX – patrz audyt-v7.md), 18.11.2026

## Decyzje z v6

- Hero w dwóch kolumnach: po lewej pełne logo, hasło (38–62 px), złote pociągnięcie, opis i CTA – wyśrodkowane w kolumnie; po prawej zdjęcie bufetu z dwoma okrągłymi „talerzami”.
- Ostre krawędzie: zdjęcia, panele, przyciski i pola bez zaokrągleń (2 px na przyciskach/polach). Okrągłe zostają tylko „talerze” i miniatury w ofercie.
- Zakładki Komunia / Wesele: przełączenie z delikatnym przenikaniem (0,3 s), obsługa strzałek na klawiaturze.
- Ruch: żadnych animacji przy ładowaniu ani przewijaniu (treść widoczna od razu, bez blokowania renderu i bez wpływu na SEO). Dozwolone tylko delikatne reakcje na najechanie/fokus: przenikanie zdjęcia przy zmianie pozycji w ofercie (0,35 s), zmiana koloru tytułu pozycji, lekkie powiększenie zdjęcia w galerii (1,03) z podpisem, zmiana tła przycisków.
- Galeria „Z naszych stołów”: siatka 3 kolumn (na telefonie 2), zdjęcia w naturalnych proporcjach 3:4, środkowa kolumna przesunięta w dół; podpis dania pojawia się po najechaniu. Bez suwaka.

## Zdjęcia do pozyskania (podmiana tymczasowych)

| Miejsce | Teraz (tymczasowo) | Potrzebne |
|---|---|---|
| Oferta: I Komunia Święta | dania w podgrzewaczach | stół komunijny, półmiski z obiadem, dekoracja komunijna |
| Oferta: Wesela i poprawiny | półmisek owoców | sala weselna, zimna płyta, serwis kelnerski |
| Oferta: Grilluj z nami | kurczak w koszykach | grill, mięsa z grilla |
| Oferta: Live cooking | krem serowy z grzanką | kucharz gotujący przy gościach |
| Oferta: Serwis kawowy | soki i przekąski | kawa, ciasta, przerwa kawowa na szkoleniu |
| Oferta: Posiłki profilaktyczne | sałatki w miseczkach | ciepłe danie obiadowe, zupa w pojemniku |
| Oferta: Szef Kuchni Poleca | smalec na pieczywie | zakąski zimne lub dania na porcje |
| Hero / BOX / galeria | zdjęcia z fanpage’a | mogą zostać; najlepiej oryginały w pełnej rozdzielczości |

Format: poziome i pionowe, min. 2000 px dłuższy bok, bez napisów i kodów QR w kadrze.

## Kierunek wizualny

- Kroje: Instrument Serif (nagłówki, duże ceny, telefon) + Figtree (tekst, przyciski).
- Kolory: tło #FCFBF8, czerń z logo #16130F, złoto z logo #D9B46A (tekst: #85652A), kamień #F1EEE7. Sekcja BOX: złoty gradient jak pociągnięcie pędzla w logo (#E8CD8C → #D9B46A → #C99D4E).
- Logo: pełny logotyp z „by Maciej Nikielski” w hero i stopce; w nagłówku sam napis TAMARILLO / CATERING.
- Złoty akcent: pociągnięcie pędzla z litery „T” w logo (SVG z gradientem) pod hasłem w hero i pod numerem telefonu w kontakcie.
- Nagłówki sekcji w dwóch kolumnach (tytuł po lewej, opis po prawej).
- Motyw: okrągłe „talerze” ze zdjęciami nałożone na zdjęcie bufetu w hero.
- Odrzucone z v1/v2: wyśrodkowany układ, hairline'y i kursywne podpisy nad każdym nagłówkiem (efekt motywu WordPress).

Pliki: `index.html`, `img/`

## Cel

Jednostronicowy landing, który prowadzi odwiedzającego do telefonu (888 015 703). Drugą ścieżką jest krótki formularz „Oddzwońcie”. Treści, ceny i zdjęcia mają być później edytowalne z panelu administracyjnego (wybór panelu otwarty).

## Użytkownicy i scenariusze

- Rodzina planująca komunię lub wesele: widzi ceny „od … zł/os.” i porównanie Menu I–III, dzwoni.
- Osoba zamawiająca przekąski: widzi BOX-y z cenami i warunkami (min. 2 boxy, 3 dni wcześniej), dzwoni.
- Firma (serwis kawowy, posiłki profilaktyczne): znajduje pozycję na liście oferty, dzwoni lub zostawia numer.

## Wymagania funkcjonalne

- FR-1: numer telefonu jako link `tel:` w nagłówku, w hero, w kontakcie i w przyklejonym pasku na telefonie (< 960 px).
- FR-2: oferta jako lista 9 pozycji (wszystkie ze starej strony poza wyłączonymi przez klienta): I Komunia Święta, Wesela i poprawiny (Menu weselne I–III), BOX Finger food, Finger food na sztuki, Szef Kuchni Poleca, Grilluj z nami, Live cooking, Serwis kawowy, Posiłki profilaktyczne. Wyłączone na życzenie klienta: Wypożyczalnia, „Catering firmowy”, Poranki cateringowe, Specjały mięsne w podgrzewaczach, Przerwa lunchowa.
- FR-3: sekcja BOX z 6 boxami i cenami.
- FR-4: sekcja „Menu na uroczystości” z zakładkami Komunia / Wesele: po trzy menu w kolumnach. Komunia z ceną za osobę; wesela „cena po rozmowie”, dopóki klient nie potwierdzi cen. Linki `#komunia` i `#wesele` otwierają właściwą zakładkę.
- FR-5: galeria realizacji z prawdziwymi zdjęciami.
- FR-6: formularz „Oddzwońcie”: imię, telefon, okazja, zgoda na kontakt. Wysyłka na `/api/callback` (do podpięcia z modułem 2/4). Komunikaty błędów mówią, co poprawić.
- FR-7: stopka z danymi firmy, regulaminem, RODO i alergenami, Facebookiem.

## Wymagania niefunkcjonalne (z constitution)

- Polski interfejs, mobile first, układ od 390 px do 1440 px.
- Lokalne SEO: `title`/`description` z miastami, dane strukturalne `FoodEstablishment`, opisy `alt` na zdjęciach.
- Dostępność: link „Przejdź do treści”, widoczny fokus, kontrast tekstu ≥ 4,5:1, etykiety pól, `prefers-reduced-motion`.
- RODO: formularz zbiera minimum danych, zgoda wymagana.
- Wydajność: zdjęcia w 2 rozmiarach (`srcset`), `loading="lazy"` poniżej hero.

## Kontrakt z panelem administracyjnym

Edytowalne obszary są oznaczone atrybutem `data-cms`:

| Klucz | Typ |
|---|---|
| `hero.title`, `hero.subtitle` | tekst |
| `contact.phone`, `contact.email`, `contact.hours` | tekst |
| `offer.items[]` | `{ title, desc, price, href, image }` |
| `boxes[]` | `{ name, price }` |
| `communion.plans[]` | `{ name, price, items[] }` |
| `wedding.plans[]` | `{ name, price, items[] }` |
| `gallery[]` | `{ src, alt, caption }` |
| `testimonial.text`, `testimonial.author` | tekst |

## Inspiracje

Analiza 6 stron cateringowych (Aleje3, Wersal, Food Club, Madam, Belvedere, Royal) z 6.10.2026. Przeniesione wzorce: oferta pogrupowana po okazjach, powtarzany główny CTA, proces w 3 krokach, galeria realizacji, opinie z liczbą poleceń. Odrzucone: długie formularze wyceny (decyzja: strona ma prowadzić do telefonu).

## Otwarte pytania

- Logo: wdrożone nowe logo (monogram „CT”, napis TAMARILLO z owocem, „by Maciej Nikielski”) jako PNG z przezroczystością wycięty z pliku 1254×1254. Do produkcji potrzebny SVG.
- Logo podpisane „by Maciej Nikielski”, a firma w CEIDG to JDG Joanny Nikielskiej: potwierdzić, kogo przedstawiamy na stronie (szef kuchni?) i czy stopka zostaje bez zmian.
- Właściwy e-mail: gmail czy wp.pl (w szablonie wp.pl).
- Ceny wesel: na stronie „cena po rozmowie”; stara strona ma w adresach 140/160/180 zł/os. Pokazujemy publicznie czy nie?
- „Catering firmowy” na liście wyłączeń: na starej stronie nie ma takiej pozycji. Jeśli chodziło o Catering filmowy, zostaje ukryty (stan obecny). Jeśli o całą ofertę dla firm, trzeba też usunąć Serwis kawowy i Posiłki profilaktyczne.
- Godziny kontaktu i wybrana opinia klienta z imieniem i datą.
- Zgoda na publikację zdjęć z fanpage’a na stronie (prawa do zdjęć).
- Rok założenia: logo mówi 2009, Oferteo ok. 2014.
