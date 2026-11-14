# Overdracht werkboek Unpack your story: repository backpack-website

Backpack · 14 november 2026 · voor Jan en zijn Claude Code

## Lees dit eerst

- **Dit document hoort in de repository `backpack-website`**, die Jan beheert. Zet het bijvoorbeeld in `docs/OVERDRACHT-WERKBOEK.md` en de vier beelden in `docs/werkboek-beelden/`.
- **Alles hieronder is werk voor deze repository**: vier pagina's van mybackpack.nl, het bestelformulier en de betaalpagina.
- **Niet voor deze repository:** het werkboek zelf en de digitale tool My Backpack. Die staan in de repository `backpack-werkboek`, die Clementine beheert. Wat daar gebeurt, staat in een eigen document. Pas in deze repository niets aan het werkboek of de tool aan. Zie hoofdstuk W9 voor wat je van Clementine nodig hebt.
- **Dit is de enige en laatste versie.** Eerdere overdrachtsdocumenten over het werkboek zijn vervallen. Teksten in dit document zijn definitief en worden letterlijk overgenomen.
- **Twee momenten:** de checklist "Nu doorvoeren" (W7) kan direct. De checklist "Op donderdag 10 december aanpassen" (W7) mag pas op 10 december worden uitgevoerd.

## Uitgangspunten

- **De huisstijl, opmaak en componenten van de huidige site zijn leidend.** Kleuren, kaders, blokken en lettergroottes in de referentiebeelden zijn indicatief en worden niet nagebouwd. Gebruik de bestaande classes en componenten.
- **Huisregels voor tekst:** geen em-streepjes, geen "en" direct na een komma, payoff is "Unpack your story".
- **Deadline:** de introductieprijs loopt tot en met woensdag 9 december. Op donderdag 10 december verandert een aantal prijzen en teksten (W7).

## Referentiebeelden

Bij dit deel horen vier afbeeldingen. Ze staan in de map `werkboek-beelden` naast dit document. Zet ze in deze repository in `docs/werkboek-beelden/`:

| Bestand | Pagina |
| --- | --- |
| 1-homepage-blok-werkboek.png | Homepage, het blok werkboek (W2) |
| 2-werkboekpagina.png | /werkboek, de hele pagina (W3 en W4) |
| 3-bestelling-ontvangen.png | /bestelling-ontvangen (W5) |
| 4-zelf-aan-de-slag.png | /zelf-aan-de-slag (W6) |

**Belangrijk:** de beelden laten alleen de opbouw en de inhoud zien: welke blokken er zijn, in welke volgorde en met welke tekst. Ze zijn niet in de stijl van de site gemaakt. **De stijl, opmaak en componenten van de huidige site van Jan zijn sturend.** Neem kleuren, kaders, lettergroottes, afronding en afstanden niet over uit de beelden. Grijze en groene vlakken met tekst erin zijn plekken voor bestaande foto's of het teaserfilmpje. Waar beeld en tekst verschillen, geldt de tekst in dit document.

## Achtergrond bij de keuzes (ter informatie)

- **"Introductieprijs" in plaats van "pre-order":** na 9 december is er voorraad en wordt direct verzonden. Een doorgestreepte "van €59,95" mag niet, omdat het werkboek nooit voor €59,95 is verkocht; "nu €49,95, na 9 december €59,95" mag wel.
- **Vinkje voor de digitale tool:** de bedenktijd voor digitale inhoud vervalt alleen met uitdrukkelijke toestemming van de koper. Een zin in de kleine lettertjes is daarvoor niet genoeg.
- **Verzending:** één boek als brievenbuspakje (€5,95), twee of meer als pakket (€7,95). Verzendkosten één keer per bestelling.
- **Betaallinks per aantal:** met de bestaande Rabo-betaalverzoeken, zonder nieuw betaalsysteem voor kerst. Bij 5 of meer volgt een betaalverzoek op maat.

## W1. Bestanden en acties in het kort

| Pagina | URL | Wat er verandert |
| --- | --- | --- |
| Homepage | / | Blok werkboek: nieuwe teksten en prijsregel. Regel "Unpack your story" linken. Werkboek bij Ons aanbod. Payoff controleren. |
| Werkboekpagina | /werkboek | Nieuwe volgorde van tien blokken, nieuwe teksten, blok My Backpack, cadeaublok, uitklapbare veelgestelde vragen, nieuw bestelformulier, blok begeleiding. |
| Bestelling ontvangen | /bestelling-ontvangen | Acht betaalknoppen met eigen links, nieuwe teksten. |
| Zelf aan de slag | /zelf-aan-de-slag | Nieuw blok met twee opties. Label "Explore · gratis" wordt "Explore". |

Claude Code zoekt zelf de bijbehorende bestanden in de repository op (de HTML-bestanden of templates van deze vier pagina's en het stylesheet).

## W2. Homepage: blok werkboek

Het bestaande blok direct onder de hero blijft op dezelfde plek. Alleen de inhoud verandert. Van boven naar onder:

1. **Label:** Nieuw · introductieprijs tot en met 9 december
2. **Kop:** Werkboek *Unpack your story* en digitale tool *My Backpack*. De twee productnamen in dezelfde saliegroene kleur als "verhaal" in de hero (#7C9A8B). De rest van de kop zoals de bestaande koppen.
3. **Tekst:** Een werkboek én een digitale tool om je familiesysteem in kaart te brengen en te ontdekken wat je meedraagt in je Backpack. Met het werkboek verken en verdiep je. Met de tool zie je je familiesysteem in één oogopslag. Geschreven door Clementine en Maaike.
4. **Prijsregel:** Nu **€49,95** introductieprijs, na 9 december €59,95 · plus verzendkosten
5. **Deadline:** Bestel uiterlijk woensdag 9 december, dan heb je het op tijd voor kerst in huis.
6. **Alleen digitaal:** Liever alleen digitaal? Met My Backpack breng je je familiesysteem online in kaart, zonder het gedrukte werkboek. Binnen één werkdag na je betaling ontvang je een mail met je persoonlijke toegangscode en de factuur.
7. **Knop:** Bekijk het werkboek en de digitale tool → (naar /werkboek)
8. **Beeld:** de bestaande foto van het werkboek.

De huidige tekst met "92 pagina's ... binnen twee weken in huis" vervalt.

**Overige acties op de homepage**

- De losse regel "Unpack your story" onder het blok over de onzichtbare rugzak wordt een link naar /werkboek.
- Voeg het werkboek toe aan "Ons aanbod", bij Explore (Zelf aan de slag).
- Payoff: op de homepage staat nog "Carry less, live more". Volgens de merkgids is die vervallen. De payoff is "Unpack your story". Vervang hem waar hij nog voorkomt.

## W3. Werkboekpagina (/werkboek): blokken en teksten

Tien blokken in deze volgorde. De paginatitel (browsertab) wordt: *Werkboek Unpack your story | Backpack* ("Pre-order" eruit).

### W3.1 Hero

- **Label:** Werkboek
- **Kop (H1):** Unpack your story
- **Prijsregel direct onder de kop:** Introductieprijs · €49,95 tot en met 9 december
- **Tekst, alinea 1:** Een prachtig vormgegeven werkboek dat je stap voor stap meeneemt in je familiegeschiedenis. Geschreven door Clementine Mol en Maaike Oosterveer. Met verdiepende vragen die het echte verhaal naar boven halen.
- **Tekst, alinea 2:** Het brengt gesprekken op gang die je anders misschien nooit zou voeren, met je ouders, opa's en oma's. Je schrijft het zelf vol en zo wordt het een boek over jouw familie dat je kunt bewaren.
- **Knop:** Bestel nu → (springt naar blok W3.7 Twee opties)
- **Naast de knop, klein kader:** Op tijd voor kerst · Bestel uiterlijk woensdag 9 december
- **Specificaties (kopje + tekst):** 92 pagina's, A4, stevige kaft, verkennende en verdiepende vragen, met ruimte om in te schrijven en opdrachten om te reflecteren en waar te nemen.
- **Beeld:** de bestaande foto van het werkboek op de houten tafel.

### W3.2 Waarom dit werkboek

Je bent gebouwd uit de verhalen van je voorouders. Sommige daarvan ken je. Andere zijn nooit verteld en juist die werken vaak door: in hoe je reageert, waar je steeds tegenaan loopt, in wat je lichaam je probeert te vertellen.

Dit werkboek helpt je die verhalen op te halen, met vragen over jezelf, je ouders en de families waar zij uit komen. Alleen al door je aandacht op je familie te richten, komt er vaak van alles in beweging.

Je kunt het alleen doen, in je eigen tempo. Het werkt ook als voorbereiding op een sessie bij Clementine of Maaike: je komt dan binnen met je familiesysteem in beeld.

Heb je vragen? Lees de veelgestelde vragen.

*Links:* "een sessie bij Clementine of Maaike" springt naar W3.10 (#begeleiding). "Lees de veelgestelde vragen" springt naar W3.8.

### W3.3 Wat erin zit

Twee kolommen: links de naam van het hoofdstuk, rechts de omschrijving.

| Hoofdstuk | Omschrijving |
| --- | --- |
| Welkom | Hoe je het werkboek gebruikt en hoe je goed voor jezelf zorgt onderweg |
| Jij nu | Je eigen levensloop, gezondheid, relaties en verlies |
| Je ouders | Wie ze zijn, wat ze meedroegen, hoe het tussen jullie was |
| De familie van je vader | Ooms, tantes, opa's en oma's, omstandigheden en ervaringen, thema's en patronen |
| De familie van je moeder | Ooms, tantes, opa's en oma's, omstandigheden en ervaringen, thema's en patronen |
| Het gesprek | Hoe je er met familie over begint en welke vragen je kunt stellen |
| Even uitzoomen | Je familiesysteem in kaart, zien wat er doorloopt van generatie op generatie |
| My Backpack | Wat draag jij mee en wat wil je ermee doen? |

De regel "Het is een werkboek, geen leesboek" vervalt.

### W3.4 Een kijkje binnenin

Ongewijzigd: de drie bestaande foto's met hun bijschriften.

### W3.5 De digitale tool: My Backpack (nieuw)

Links tekst, rechts het teaserfilmpje. Anker: #my-backpack.

- **Label:** De digitale tool
- **Kop:** My Backpack
- **Ondertitel:** Bij het werkboek inbegrepen of los te bestellen · €29,95 · persoonlijke toegangscode
- **Tekst:** Met het werkboek verken en verdiep je. Met de tool zie je je familiesysteem in één oogopslag; je creëert overzicht en brengt de kern bij elkaar.
- **Tussenkopje:** Je doorloopt een aantal stappen
- **Genummerde stappen:**
    1. Je ontvangt per mail een persoonlijke toegangscode en een link naar de tool.
    2. Je vult informatie over jezelf en je familie in, inclusief de belangrijke gebeurtenissen en wat ieder in zijn of haar Backpack draagt.
    3. Het genogram groeit automatisch mee.
    4. Je beantwoordt verdiepende vragen.
    5. Als je alles hebt ingevuld en beantwoord, kun je de PDF My Backpack downloaden.
    6. Het genogram (stamboom) kun je toevoegen aan je werkboek. De PDF kun je voor jezelf bewaren of meenemen naar een sessie.
- **Onderaan, met een slotje-icoon:** Je gegevens blijven van jou. Net als bij de check-up bewaren wij niets van wat je invult. Sla tussendoor op, zodat je niets kwijtraakt.
- **Rechts:** het teaserfilmpje van My Backpack (volgt).

### W3.6 Een cadeau dat echt iets betekent (nieuw)

- **Label:** Voor de feestdagen
- **Kop:** Een cadeau dat echt iets betekent
- **Tekst:** Een mooi cadeau voor de feestdagen, voor jezelf of voor iemand die je dierbaar is. Het geeft je de kans om jezelf en je familie beter te leren kennen. Juist in deze tijd van het jaar, als de familie samenkomt, is er alle ruimte voor de verhalen die ertoe doen.
- **Link:** Bestel uiterlijk 9 december, op tijd voor kerst → (naar het bestelformulier)

### W3.7 Twee opties

- **Kop:** Twee opties
- **Kaart 1.** Label: Compleet · introductieprijs. Titel: Werkboek + digitale tool. Tekst: Het gedrukte werkboek, thuisbezorgd, plus toegang tot de digitale tool My Backpack met een persoonlijke toegangscode. Prijs: **€49,95** tot en met 9 december · Daarna €59,95 · plus verzendkosten. Knop: Bestel dit →
- **Kaart 2.** Label: Digitaal. Titel: Alleen de digitale tool. Tekst: De digitale tool My Backpack, met een persoonlijke toegangscode. Geen verzendkosten. Prijs: **€29,95** · Geen verzendkosten. Knop: Bestel dit →
- **Onder de kaarten:** Alle prijzen zijn inclusief btw.

### W3.8 Veelgestelde vragen

Uitklapbaar: alleen de vragen zichtbaar, het antwoord klapt open bij een klik (bijvoorbeeld met `<details>` en `<summary>`). Anker op de kop. Volgorde en teksten:

**Wanneer krijg ik het?**
Na 9 december gaan alle bestellingen tegelijk naar de drukker. Bestel je uiterlijk woensdag 9 december, dan heb je het uiterlijk 21 december in huis, op tijd voor kerst. Kies je alleen de digitale tool, dan krijg je binnen 1 werkdag na je betaling per mail je persoonlijke toegangscode en de factuur.

**Waarom een introductieprijs?**
De eerste oplage laten we drukken op basis van de bestellingen. Wie uiterlijk 9 december bestelt, betaalt de introductieprijs van €49,95. Daarna kost het werkboek €59,95.

**Hoe betaal ik?**
Je vult eerst het formulier hieronder in. Daarna kom je op een pagina waar je veilig afrekent via een betaallink. Je bestelling is definitief zodra de betaling binnen is.

**Wat krijg ik precies?**
Bij de complete bestelling krijg je het gedrukte werkboek thuisbezorgd en een persoonlijke toegangscode voor de digitale tool. Kies je alleen digitaal, dan krijg je de persoonlijke toegangscode. Die sturen we je binnen een werkdag na je betaling, samen met de factuur. Bestel je meer exemplaren, dan krijg je per exemplaar een eigen toegangscode. Alle codes sturen we naar jou, zodat je ze kunt doorgeven. In het boek zal ook een kaartje met je persoonlijke toegangscode zitten.

**Wat zijn de verzendkosten?**
Eén werkboek versturen we als brievenbuspakje, voor €5,95. Bestel je twee of meer, dan versturen we ze samen als pakket, voor €7,95. Je betaalt de verzendkosten dus maar één keer per bestelling. Voor de digitale tool betaal je geen verzendkosten.

**Wat gebeurt er met mijn gegevens in de tool?**
Net als bij de check-up blijft wat je invult van jou. Je gegevens worden alleen bewaard op je eigen apparaat, niet bij ons. Wij kunnen er dus niet bij en niemand anders ook.

Dat betekent wel dat je zelf zorgt dat je werk bewaard blijft. Sla daarom tussendoor regelmatig op, zeker voordat je de tool sluit of op een ander apparaat verdergaat. Wis je je browsergegevens zonder op te slaan, dan ben je wat je hebt ingevuld kwijt. Op elke pagina van de tool staat een knop om op te slaan en de tool herinnert je er onderweg aan.

**Kan ik met het werkboek aan de slag als mijn ouders niet meer leven?**
Ja, ook dan helpt het werkboek. Je haalt de verhalen op bij broers en zussen, ooms en tantes en uit oude brieven, papieren en foto's.

**Is het werkboek ook geschikt als ik geadopteerd ben?**
Ja. Je adoptieouders krijgen een eigen plek in hoofdstuk 2. De rest van het werkboek vul je in voor je biologische ouders en hun families, want daar ben je uit gebouwd.

Weet je weinig of niets over je biologische familie? Dan kun je een groot deel van het werkboek niet invullen en past een sessie beter. Ook wat je nooit verteld is, draag je mee, in je lichaam en in je onderbewuste. In een sessie halen we dat samen naar boven.

Twijfel je? Of heb je een vraag? Stuur ons gerust een berichtje. (link naar /contact)

**Wat als ik het werkboek of de digitale tool heb ingevuld?**
Dan heb je je familieverhaal op papier en je familiesysteem in beeld. Voor de een is dat genoeg: het geeft overzicht en rust. De ander merkt dat er iets in beweging is gekomen en wil verder de diepte in.

Heb je behoefte aan begeleiding? Plan een gratis kennismaking met Clementine of boek een verdiepende sessie. Stuur je PDF My Backpack 3 dagen voor de sessie naar Clementine of Maaike, zodat zij zich kunnen voorbereiden op de sessie. (links: kennismaking en boekingspagina's, zie W3.10)

### W3.9 Bestelformulier

Zie hoofdstuk W4.

### W3.10 Begeleiding (nieuw, onderaan de pagina)

Anker: #begeleiding.

- **Label:** Liever niet alleen?
- **Kop:** Heb je behoefte aan begeleiding?
- **Tekst:** Het werkboek kun je zelf doen, in je eigen tempo. Merk je dat er veel in beweging komt? Plan een gratis kennismaking van twintig minuten met Clementine, of boek direct een verdiepende sessie bij Clementine of Maaike.
- **Knop:** Plan gratis kennismaking → (https://backpack.clientomgeving.nl/afspraak-maken)
- **Regel eronder:** Weet je al wat je zoekt? Boek direct een sessie bij Clementine of Maaike. (De namen linken naar de bestaande boekingspagina's, zoals in de afsluitende kennismakingsblokken van de andere pagina's.)

## W4. Bestelformulier op /werkboek

Het formulier blijft een Netlify-formulier dat na verzenden naar /bestelling-ontvangen gaat. Kop en intro blijven: *Je bestelling*. Na het versturen volgt de betaalpagina.

**Samenvatting bovenaan het formulier**

| Regel | Bedrag |
| --- | --- |
| Werkboek + digitale tool | €49,95 |
| Introductieprijs, na 9 december €59,95 | |
| Verzending (bij 2 of meer werkboeken €7,95) | €5,95 |
| Totaal | €55,90 |

Daaronder: Bestel je uiterlijk 9 december, dan heb je het uiterlijk 21 december in huis.

**Velden in deze volgorde.** Bovenaan: "Velden met * zijn verplicht."

| Veld | Type | Verplicht | Opties of hulptekst |
| --- | --- | --- | --- |
| Wat wil je bestellen? | keuzelijst | ja | Werkboek + digitale tool (€49,95 + verzendkosten) · Alleen de digitale tool (€29,95) |
| Je bestelt als | keuzerondjes | ja | Particulier (standaard) · Zakelijk |
| Bedrijfsnaam | tekst | ja, alleen bij Zakelijk | Alleen zichtbaar bij Zakelijk |
| Btw-nummer | tekst | nee | Alleen zichtbaar bij Zakelijk |
| Referentie of inkoopnummer | tekst | nee | Alleen zichtbaar bij Zakelijk. Eronder: De factuur komt op naam van je bedrijf. Bestel je voor een team of groep? Zet het aantal hierboven en laat in de opmerking weten waar de boeken heen moeten. |
| Aantal | getal, minimaal 1 | ja | Hulptekst: Bestel je 5 of meer? Dan sturen we je een betaalverzoek op maat. |
| Naam | tekst | ja | |
| E-mailadres | e-mail | ja | Hulptekst: Hierop ontvang je je toegangscode en de factuur. |
| Straat en huisnummer | tekst | ja | Kopje erboven: Bezorgadres |
| Postcode | tekst | ja | |
| Plaats | tekst | ja | |
| Heb je het op een bepaald moment nodig? | keuzelijst | ja | Maak een keuze · Graag voor de Kerst (25 december) · Geen haast. De optie "Graag voor de Sint" vervalt. |
| Opmerking | tekstvak | nee | |

**Onder de velden**

1. Tekst: Je hebt veertien dagen bedenktijd vanaf het moment dat je het werkboek ontvangt. Stuur het ongebruikt terug en je krijgt het aankoopbedrag terug; de retourkosten zijn voor jou.
2. Vinkje, verplicht, standaard **niet** aangevinkt: Ik ga ermee akkoord dat ik de digitale tool direct na mijn betaling ontvang. Ik weet dat ik mijn bedenktijd voor de digitale tool verlies zodra ik de toegangscode heb gebruikt.
3. Tekst: We gebruiken je gegevens alleen om je bestelling te versturen en te administreren. Zie onze privacyverklaring en algemene voorwaarden. (met de bestaande links)
4. Knop: Naar betalen →

De oude zin "Bij de digitale tool vervalt dat recht zodra je de toegangscode hebt gebruikt." vervalt. Het vinkje vervangt hem. Stuur de waarde van het vinkje mee in de inzending, zodat de toestemming per bestelling vastligt.

## W5. Bestelling ontvangen (/bestelling-ontvangen)

De twee betaalknoppen worden acht knoppen: één per aantal, met verzendkosten één keer per bestelling.

- **Label:** Bijna klaar
- **Kop:** Nog één stap: betalen
- **Tekst:** Je bestelling staat genoteerd. Hij is definitief zodra de betaling binnen is. Kies hieronder het bedrag dat bij je bestelling hoort.

**Kopje: Werkboek + digitale tool**

| Knop | Bedrag | Betaallink |
| --- | --- | --- |
| 1 werkboek | €55,90 | https://betaalverzoek.rabobank.nl/betaalverzoek/?id=ShFKNHx0TIKG5JgAiBXkug |
| 2 werkboeken | €107,85 | https://betaalverzoek.rabobank.nl/betaalverzoek/?id=UL2IhZI5ReiHS_U4lrpfYw |
| 3 werkboeken | €157,80 | https://betaalverzoek.rabobank.nl/betaalverzoek/?id=SGqpSBlqSda6hSeGygCzXA |
| 4 werkboeken | €207,75 | https://betaalverzoek.rabobank.nl/betaalverzoek/?id=mi58UqXAR-6ibos-BmNm2A |

Eronder: Inclusief verzending: €5,95 bij één werkboek, €7,95 bij twee of meer. Je betaalt de verzendkosten maar één keer.

**Kopje: Alleen de digitale tool**

| Knop | Bedrag | Betaallink |
| --- | --- | --- |
| 1 toegangscode | €29,95 | https://betaalverzoek.rabobank.nl/betaalverzoek/?id=0lHuZBpkQxWUTjDLX5deOA |
| 2 toegangscodes | €59,90 | https://betaalverzoek.rabobank.nl/betaalverzoek/?id=rfik5L71SN6ZN42cqyE1qw |
| 3 toegangscodes | €89,85 | https://betaalverzoek.rabobank.nl/betaalverzoek/?id=kUEApiyJQ8iDy28YLfZs2g |
| 4 toegangscodes | €119,80 | https://betaalverzoek.rabobank.nl/betaalverzoek/?id=wRVNjkFOTx-wnG3_N-OkWA |

Als het kan: toon alleen de knop die past bij het gekozen product en aantal uit het formulier. Kan dat niet, dan alle acht.

**Kader: Wat er nu gebeurt**

1. **Bestel je 5 of meer?** Dan sturen we je binnen één werkdag een betaalverzoek op maat. Je hoeft nu nog niets te betalen. Bestel je zakelijk, dan komt de factuur op naam van je bedrijf.
2. Na je betaling krijg je binnen één werkdag een mail van ons. Daarin staan de bevestiging met je persoonlijke toegangscode voor de digitale tool en de factuur.
3. Het gedrukte werkboek gaat na 9 december naar de drukker en ligt uiterlijk 21 december bij je op de mat, op tijd voor kerst.
4. Klopt er iets niet, of lukt het betalen niet? Mail ons gerust via de contactpagina. (link naar /contact)

De oude alinea "twee boeken betekent twee keer betalen" vervalt.

## W6. Zelf aan de slag (/zelf-aan-de-slag)

Eén nieuw blok, direct na de drie bestaande kaarten (check-up, artikelen, lezingen). De rest van de pagina blijft gelijk, met één kleine wijziging bovenaan.

- **Label bovenaan de pagina:** "Explore · gratis" wordt **Explore**, want niet alles op de pagina is nog gratis.

**Nieuw blok**

- **Label:** Nieuw · introductieprijs tot en met 9 december
- **Kop:** Verder met je familieverhaal: *Unpack your story* en *My Backpack* (productnamen in saliegroen, zoals op de homepage)
- **Tekst:** Wil je zelf dieper ingaan op wat je meedraagt? Met het werkboek verken en verdiep je. Met de digitale tool zie je je familiesysteem in één oogopslag. In je eigen tempo, geschreven door Clementine en Maaike.
- **Kaart 1** (met foto van het werkboek). Label: Compleet. Titel: Ga aan de slag met het werkboek en de digitale tool. Tekst: Het gedrukte werkboek van 92 pagina's, thuisbezorgd, plus toegang tot My Backpack. Je schrijft je familieverhaal op papier en ziet je familiesysteem online in beeld. Prijs: **€49,95** tot en met 9 december, daarna €59,95 · plus verzendkosten. Knop: Bekijk het werkboek → (naar /werkboek)
- **Kaart 2** (met een still uit de teaser van My Backpack). Label: Digitaal. Titel: Ga aan de slag met de digitale tool. Tekst: My Backpack, met een persoonlijke toegangscode. Je brengt je familiesysteem online in kaart, het genogram groeit automatisch mee en je downloadt je eigen PDF. Zonder het gedrukte werkboek. Prijs: **€29,95** · geen verzendkosten. Knop: Meer over My Backpack → (naar /werkboek#my-backpack)

## W7. Technische acties

**Nu doorvoeren**

- [ ] Veelgestelde vragen uitklapbaar maken.
- [ ] Ankers toevoegen: #begeleiding, #my-backpack en een anker op de veelgestelde vragen.
- [ ] Formulier: de zakelijke velden alleen tonen bij "Zakelijk"; het vinkje verplicht en standaard uit; de waarde van het vinkje meesturen.
- [ ] Bestelling ontvangen: de acht betaallinks koppelen; liefst alleen de passende knop tonen.
- [ ] Herroepingsknop: verplicht voor webshops met een wettelijke bedenktijd. Een functie op de site waarmee een klant de bestelling kan herroepen; een link in de bevestigingsmail alleen is niet genoeg.
- [ ] Homepage: regel "Unpack your story" linken, werkboek bij Ons aanbod, payoff "Carry less, live more" vervangen door "Unpack your story".

**Op donderdag 10 december aanpassen** (niet nu uitvoeren)

- [ ] Prijs van het werkboek: €49,95 wordt €59,95 op homepage, werkboekpagina, formulier en Zelf aan de slag.
- [ ] Teksten met "introductieprijs", "tot en met 9 december" en "op tijd voor kerst" weghalen of herschrijven.
- [ ] Vier nieuwe betaallinks voor het werkboek: 1 = €65,90 · 2 = €127,85 · 3 = €187,80 · 4 = €247,75. De links voor alleen de digitale tool blijven gelijk.
- [ ] Levertijd aanpassen in de veelgestelde vragen, de samenvatting van het formulier en op Bestelling ontvangen: na 9 december is er voorraad en versturen we direct. De zinnen over de drukker en "uiterlijk 21 december" vervallen; drukrondes noemen we niet op de site.

## W8. Besluiten die de site raken (ter informatie)

- **Levertijd digitale tool:** binnen één werkdag, overal hetzelfde.
- **Na 9 december:** er komt voorraad en we versturen direct; de site noemt geen drukrondes.
- **Meerdere toegangscodes:** elk exemplaar krijgt een eigen toegangscode. Alle codes gaan per mail naar de koper en in elk boek zit een kaartje met de persoonlijke toegangscode. Clementine verstuurt de codes; de site hoeft geen codes te maken of te versturen.
- **Verzending:** 1 boek als brievenbuspakje (€5,95), 2 of meer als pakket (€7,95).

## W9. Wat je nodig hebt uit backpack-werkboek (van Clementine)

Deze onderdelen worden niet in deze repository gemaakt. Je krijgt ze van Clementine; tot die tijd laat je een duidelijke plek open.

- [ ] **Teaserfilmpje van My Backpack** voor blok W3.5, plus een still daaruit voor kaart 2 op /zelf-aan-de-slag (W6).
- [ ] **Bevestiging dat de teksten over de tool kloppen** met de tool zelf: gegevens alleen op het eigen apparaat, een knop om op te slaan op elke pagina, een herinnering om op te slaan, de PDF My Backpack. Deze teksten staan in W3.5 en W3.8; pas ze niet zelf aan.
- [ ] **De link naar de tool** staat niet op de site. Kopers krijgen hem per mail met hun toegangscode.
- [ ] **Na 9 december:** vier nieuwe betaallinks voor het werkboek (zie W7). Clementine maakt ze aan en geeft ze aan jou.
