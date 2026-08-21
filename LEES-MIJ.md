# Backpack — website

Statische site. Geen database, geen WordPress. Elke wijziging in deze map
wordt door Netlify automatisch opnieuw gebouwd en online gezet.

## Hoe het werkt

```
build.py              genereert alle pagina's — dit is het hart
content/inspiratie/   de artikelen, als losse tekstbestanden (schrijft het CMS)
admin/                het inlogscherm waar Clementine artikelen beheert
assets/style.css      alle vormgeving, één bestand voor de hele site
assets/site.js        menu, tabbladen, meetcode
images/               foto's (webp met jpg als terugval)
files/                pdf's: algemene voorwaarden en privacyverklaring
netlify.toml          bouwopdracht en doorverwijzingen van oude adressen
bron/                 het originele check-up-bestand van Clementine
*.html                de gegenereerde pagina's — niet met de hand aanpassen
```

**Belangrijk:** de HTML-bestanden in de hoofdmap worden gegenereerd. Wijzig ze
niet met de hand, want bij de volgende build worden ze overschreven. Wil je iets
aan een pagina veranderen, doe dat in `build.py`.

## Zelf bouwen

```
python3 build.py
```

Geen installatie nodig — het script gebruikt alleen wat standaard in Python zit.

## Wat er nog moet gebeuren

1. **De vier pdf's** in `files/` zetten (algemene voorwaarden en privacyverklaring,
   per praktijk). Ze staan nu nog op de oude server; de links wijzen daar tijdelijk
   naartoe. Zoek in `build.py` op `mybackpack.nl/files` om ze om te zetten.
2. ~~robots.txt weghalen~~ — hoeft niet meer. `build.py` regelt dit zelf: zolang de
   site niet op mybackpack.nl draait blijft hij dicht, daarna gaat hij vanzelf open.
3. **Logo en iconen** lokaal opslaan; die laden nu nog van de oude site.
4. **Bronlinks** invullen bij de zes verwijzingen naar externe artikelen — kan
   gewoon via het CMS, veld 'Link naar de bron'.

## Netlify instellen

1. Koppel deze repository aan de Netlify-site (Site settings → Build & deploy).
2. Zet **Identity** aan en daaronder **Git Gateway**. Zonder Git Gateway kan het
   CMS niets opslaan.
3. Zet registratie op **Invite only** en nodig Clementine uit.
4. Voeg `mybackpack.me` toe als domain alias. Netlify stuurt aliassen automatisch
   door naar het hoofddomein — de e-mail op dat domein blijft ongemoeid.

## Artikelen schrijven

Ga naar `mybackpack.nl/admin`, log in, klik op Inspiratie en dan op New Artikel.
Publiceren duurt daarna ongeveer een minuut.
