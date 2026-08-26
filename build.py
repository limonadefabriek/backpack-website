#!/usr/bin/env python3
"""
Backpack — paginagenerator.

Bouwt alle HTML-pagina's met dezelfde kop, navigatie en voettekst.
Wil je de navigatie of voettekst wijzigen? Doe dat hier, run
`python3 build.py`, en het verandert op elke pagina in één keer.
"""
import os, re

OUT = os.path.dirname(os.path.abspath(__file__))

CLEM = "https://backpack.clientomgeving.nl/afspraak-maken?t=gbFxFmGj"

# Waar de knop "Plan gratis kennismaking" naartoe gaat.
# Nu tijdelijk het contactformulier. Wil je later weer rechtstreeks naar
# het afspraaksysteem van Clementine? Zet dan KENNISMAKING = CLEM en
# EXTERN_KENNISMAKING = True, en draai build.py opnieuw.
KENNISMAKING = "contact.html"
EXTERN_KENNISMAKING = False


def kennismaking_attrs(depth=0):
    """Levert href plus de bijbehorende attributen voor de kennismakingsknop."""
    if EXTERN_KENNISMAKING:
        return f'href="{KENNISMAKING}" target="_blank" rel="noopener" data-book="clementine"'
    return f'href="{"../" * depth}{KENNISMAKING}" data-cta="kennismaking"'

MAAIKE = ("https://widget.onlineafspraken.nl/consumer/booking/book/key/bcah63qhqt55-zzaz41"
          "/l/31112/ln/nl/t/8080dc/f/110e0011/o/theme:gray,dp:modern/at/0/rs/0/pp/0/output/html")
LOGO_BESTAND = "images/logo-backpack.svg"   # zie LEES-MIJ.md

CHECK = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round"><path d="M20 6L9 17l-5-5"/></svg>')


def head(title, desc, slug, depth=0, extra=""):
    r = "../" * depth
    canon = "https://mybackpack.nl/" + ("" if slug == "index.html" else slug)
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#24433A">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:image" content="https://mybackpack.nl/images/hero-duo.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">{extra}
</head>
<body>
"""


def header(active="", depth=0):
    r = "../" * depth
    def cur(name):
        return ' aria-current="page"' if active == name else ''
    return f"""<header class="header" id="header">
  <div class="wrap header-in">
    <a href="{r}index.html" class="brand"><img src="{r}images/logo-backpack.svg" alt="" aria-hidden="true">Backpack</a>
    <nav aria-label="Hoofdmenu">
      <ul class="nav navlist" id="navlist">
        <li><a href="{r}index.html#verhaal"{cur('verhaal')}>Ons verhaal</a></li>
        <li>
          <button class="navbtn" aria-expanded="false">Aanbod</button>
          <ul class="submenu">
            <li><a href="{r}check-up.html">Digitale check-up<span>Gratis, 5 minuten</span></a></li>
            <li><a href="{r}zelf-aan-de-slag.html">Zelf aan de slag<span>Explore · gratis</span></a></li>
            <li><a href="{r}leefstijl-en-systemisch-werk.html">Leefstijl &amp; systemisch werk<span>Discover · met Clementine</span></a></li>
            <li><a href="{r}regressietherapie.html">Regressietherapie<span>Unpack · met Maaike</span></a></li>
            <li><a href="{r}lezingen-en-workshops.html">Lezingen &amp; workshops<span>Voor teams en organisaties</span></a></li>
          </ul>
        </li>
        <li>
          <button class="navbtn" aria-expanded="false">Over ons</button>
          <ul class="submenu">
            <li><a href="{r}clementine.html">Clementine Mol<span>Integratief leefstijlarts · Online &amp; Amsterdam</span></a></li>
            <li><a href="{r}maaike.html">Maaike Oosterveer<span>Regressietherapeut · Voorschoten</span></a></li>
          </ul>
        </li>
        <li><a href="{r}inspiratie/index.html"{cur('inspiratie')}>Inspiratie</a></li>
        <li><a href="{r}tarieven.html"{cur('tarieven')}>Tarieven</a></li>
        <li><a href="{r}veelgestelde-vragen.html"{cur('faq')}>Vragen</a></li>
        <li><a href="{r}contact.html"{cur('contact')}>Contact</a></li>
      </ul>
    </nav>
    <div style="display:flex;align-items:center;gap:8px">
      <a class="btn btn-primary" {kennismaking_attrs(depth)}>
        Plan gratis kennismaking <span class="arw">&rarr;</span></a>
      <button class="burger" id="burger" aria-label="Menu openen" aria-expanded="false" aria-controls="navlist">
        <span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""


def cta(depth=0, direct=True):
    regel = ("""
      <p class="cta-direct">Weet je al bij wie je wilt zijn?
        <a href="{CLEM}" target="_blank" rel="noopener" data-book="clementine">Boek direct bij Clementine</a>
        of <a href="{MAAIKE}" target="_blank" rel="noopener" data-book="maaike">bij Maaike</a>.</p>""".format(CLEM=CLEM, MAAIKE=MAAIKE)
             if direct else "")
    return f"""<section style="padding-bottom:0">
  <div class="wrap">
    <div class="cta reveal">
      <h2>zullen we kennismaken?</h2>
      <p>Twintig minuten, vrijblijvend en gratis. Je ontdekt of onze aanpak bij je past —
      en wij of we je verder kunnen helpen.</p>
      <a class="btn btn-light" {kennismaking_attrs(depth)}>
        Plan gratis kennismaking <span class="arw">&rarr;</span></a>
{regel}
    </div>
  </div>
</section>
"""


def footer(depth=0):
    r = "../" * depth
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <span class="brand"><img src="{r}images/logo-backpack.svg" alt="" aria-hidden="true">Backpack</span>
        <p class="foot-about">Leefstijlgeneeskunde, integrale geneeskunde, systemisch werk en regressietherapie.</p>
      </div>
      <div>
        <h4>aanbod</h4>
        <ul>
          <li><a href="{r}check-up.html">Digitale check-up</a></li>
          <li><a href="{r}zelf-aan-de-slag.html">Zelf aan de slag</a></li>
          <li><a href="{r}leefstijl-en-systemisch-werk.html">Leefstijl, integrale geneeskunde en systemisch werk</a></li>
          <li><a href="{r}regressietherapie.html">Regressietherapie</a></li>
          <li><a href="{r}lezingen-en-workshops.html">Lezingen &amp; workshops</a></li>
        </ul>
      </div>
      <div>
        <h4>Backpack</h4>
        <ul>
          <li><a href="{r}clementine.html">Clementine Mol</a></li>
          <li><a href="{r}maaike.html">Maaike Oosterveer</a></li>
          <li><a href="{r}inspiratie/index.html">Inspiratie</a></li>
          <li><a href="{r}veelgestelde-vragen.html">Veelgestelde vragen</a></li>
        </ul>
      </div>
      <div>
        <h4>praktisch</h4>
        <ul>
          <li><a href="{r}contact.html">Contact</a></li>
          <li><a {kennismaking_attrs(depth)}>Plan kennismaking</a></li>
          <li><a href="{r}tarieven.html">Tarieven</a></li>
          <li><a href="{r}algemene-voorwaarden.html">Algemene voorwaarden</a></li>
          <li><a href="{r}privacyverklaring.html">Privacyverklaring</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 Backpack &middot; KvK 99312050</span>
      <span>Unpack your story</span>
    </div>
  </div>
</footer>
<script src="{r}assets/site.js"></script>
</body>
</html>
"""


def crumb(label, depth=0):
    """Clementine wil de regel 'Home / Pagina' niet zien.

    De zichtbare kruimel is weg. De structured data blijft wel bestaan
    (zie breadcrumb_ld), zodat Google het pad nog steeds in de
    zoekresultaten kan tonen.
    """
    return ""


def breadcrumb_ld(label, slug, depth=0):
    top = "../" * depth + "index.html"
    return ('\n<script type="application/ld+json">\n'
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
            '{"@type":"ListItem","position":1,"name":"Home","item":"https://mybackpack.nl/"},'
            '{"@type":"ListItem","position":2,"name":"%s","item":"https://mybackpack.nl/%s"}]}\n'
            '</script>' % (label.replace("&amp;", "en").replace('"', "'"), slug))


def cap_first(inner):
    """Maakt de eerste echte letter van een kop een hoofdletter.

    Slaat HTML-tags en entiteiten (&euro;, &amp;) over, zodat
    <h2><span>tekst</span></h2> ook goed gaat.
    """
    out = list(inner)
    i, n = 0, len(out)
    while i < n:
        c = out[i]
        if c == "<":                       # tag overslaan
            while i < n and out[i] != ">":
                i += 1
        elif c == "&":                     # entiteit overslaan
            j = i
            while j < min(n, i + 10) and out[j] != ";":
                j += 1
            i = j
        elif c.isalpha():
            out[i] = c.upper()
            break
        i += 1
    return "".join(out)


HEADING_RE = re.compile(r"(<(h[1-6]|blockquote)\b[^>]*>)(.*?)(</\2>)", re.S)


def sentence_case(html):
    """Koppen beginnen met een hoofdletter, de rest blijft zoals geschreven."""
    html = HEADING_RE.sub(lambda m: m.group(1) + cap_first(m.group(3)) + m.group(4), html)
    # Ook de tussenkopjes in het resultatenblok
    html = re.sub(r'(<div class="result"><strong>)([a-z])',
                  lambda m: m.group(1) + m.group(2).upper(), html)
    return html


def write(slug, html, raw=False):
    # raw=True: bestand letterlijk overnemen, geen aanpassing aan de koppen.
    # Gebruikt voor de check-up, die van Clementine zelf komt.
    if not raw:
        html = sentence_case(html)
    path = os.path.join(OUT, slug)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  {slug}  ({len(html)//1000} kB)")


def page(slug, title, desc, body, active="", depth=0, extra=""):
    write(slug, head(title, desc, slug.replace(os.sep, "/"), depth, extra)
          + header(active, depth) + body + footer(depth))


# ============================================================
#  REVIEWS — hergebruikt op meerdere pagina's
# ============================================================
REVIEWS = [
    ("Ik heb een sessie gehad bij Maaike en het heeft me veel nieuwe inzichten gegeven. Supergaaf om dit te mogen ervaren — ik ben enorm dankbaar voor Maaike's talent en begeleiding.", "Helena", "Regressietherapie"),
    ("Maaike nam al mijn angsten van tevoren weg en heeft me heel goed begeleid de hele sessie door. Ik voelde me rustig en vertrouwd. Ook de nazorg was fijn, ze denkt echt met je mee.", "Ayla", "Regressietherapie"),
    ("Clementine really wanted to get deep into the root cause of my problems and listened to me really carefully. She gave me really useful, applicable tips to change my lifestyle for the better.", "Sara", "Leefstijl, integrale geneeskunde &amp; systemisch werk"),
    ("Bedankt voor alle waardevolle sessies Clementine. Het heeft me zoveel mooie nieuwe inzichten gegeven en laten voelen.", "Tessa", "Leefstijl, integrale geneeskunde &amp; systemisch werk"),
    ("Bij Maaike voel je je meteen op je gemak en ze weet goed door te vragen. Nu een dag later voel ik me een stuk vrijer, lichter en vooral vol liefde en leven.", "Mandy", "Regressietherapie"),
    ("Hele fijne sessies met Clementine gehad, met ook praktische tips waar ik mee aan de slag kan.", "Sofie", "Leefstijl, integrale geneeskunde &amp; systemisch werk"),
]


def reviews_section(filter_by=None, google=False):
    google_link = """    <p style="margin:1.6rem 0 0">
      <a class="social" href="https://www.google.com/search?q=Maaike+Oosterveer+Reviews&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxI2MTQ2MrI0MDIxNDIyNDAzNzc13sDI-IpR0jcxMTM7VcE_v7gktagsNbVIISi1LDO1vHgRK245AAIuKUxSAAAA&rldimm=4132290241221067753&tbm=lcl&hl=nl-NL#lkt=LocalPoiReviews" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M22.6 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.94a5.08 5.08 0 0 1-2.2 3.33v2.77h3.57c2.08-1.92 3.29-4.74 3.29-8.11z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84A11 11 0 0 0 12 23z"/><path fill="#FBBC05" d="M5.84 14.1a6.6 6.6 0 0 1 0-4.2V7.06H2.18a11 11 0 0 0 0 9.88l3.66-2.84z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06L5.84 9.9c.87-2.6 3.3-4.52 6.16-4.52z"/></svg>
        <span>Beoordelingen van Maaike op Google</span></a></p>""" if google else ""
    items = [r for r in REVIEWS if filter_by is None or filter_by in r[2]]
    cards = "".join(f"""
      <article class="rev"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p>{q}</p><cite>{who}<span>{what}</span></cite></article>""" for q, who, what in items)
    return f"""<section class="section" id="reviews" style="padding-top:0">
  <div class="wrap head-row reveal">
    <div><p class="eyebrow">Reviews</p><h2>wat anderen ervaren</h2></div>
    <div class="rail-nav">
      <button class="rail-btn" data-rail="prev" aria-label="Vorige reviews">&larr;</button>
      <button class="rail-btn" data-rail="next" aria-label="Volgende reviews">&rarr;</button>
    </div>
  </div>
  <div class="wrap reveal"><div class="rev-rail" id="rev-rail">{cards}
    </div>
{google_link}  </div>
</section>
"""


# ============================================================
#  HOMEPAGE
# ============================================================
# ============================================================
#  ARTIKELEN INLEZEN
#  De artikelen staan als losse tekstbestanden in content/inspiratie/.
#  Die bestanden schrijft het CMS wanneer Clementine iets publiceert.
#  Hieronder worden ze ingelezen en omgezet naar HTML-pagina's.
# ============================================================

WAARSCHUWINGEN = []


def lees_front_matter(tekst, bestand=""):
    """Haalt de gegevens boven aan het bestand (tussen de --- regels) eruit."""
    if not tekst.startswith("---"):
        return {}, tekst
    eind = tekst.index("\n---", 3)
    kop, body = tekst[3:eind], tekst[eind + 4:]
    data = {}
    for regel in kop.strip().splitlines():
        if ":" not in regel:
            continue
        k, v = regel.split(":", 1)
        v = v.strip()
        if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
            # Aanhalingstekens binnen dezelfde soort aanhalingstekens maken het
            # bestand onleesbaar voor het CMS. Dit script leest het nog wel, dus
            # zonder waarschuwing zou zo'n artikel stilletjes uit het CMS
            # verdwijnen terwijl het op de site gewoon zichtbaar blijft.
            if v[0] in v[1:-1]:
                WAARSCHUWINGEN.append(
                    f"  {bestand} \u2014 veld '{k.strip()}': aanhalingstekens binnen aanhalingstekens. "
                    f"Het CMS kan dit artikel niet lezen. Gebruik enkele aanhalingstekens "
                    f"om de hele regel, of haal ze binnenin weg.")
            v = v[1:-1]
        data[k.strip()] = v
    return data, body.strip()


def inline(t):
    """Vet, cursief en links binnen een regel."""
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)",
               r'<a class="sublink" href="\2" target="_blank" rel="noopener">\1</a>', t)
    return t


def naar_html(body, gedicht=False):
    """Zet de tekst van het CMS om naar HTML. Bewust eenvoudig gehouden:
    tussenkoppen, alinea's, opsommingen, vet, cursief en links."""
    if gedicht:
        strofen = [b.strip() for b in body.split("\n\n") if b.strip()]
        return "\n".join(
            '    <p class="vers">%s</p>' % "<br>\n      ".join(inline(r) for r in st.splitlines())
            for st in strofen)
    uit, lijst = [], []
    def sluit_lijst():
        if lijst:
            uit.append("    <ul>" + "".join(f"<li>{inline(x)}</li>" for x in lijst) + "</ul>")
            lijst.clear()
    for blok in body.split("\n\n"):
        blok = blok.strip()
        if not blok:
            continue
        if blok.startswith("- "):
            for r in blok.splitlines():
                lijst.append(r[2:].strip())
            sluit_lijst()
        elif blok.startswith("### "):
            sluit_lijst(); uit.append(f"    <h3>{inline(blok[4:])}</h3>")
        elif blok.startswith("## "):
            sluit_lijst(); uit.append(f"    <h2>{inline(blok[3:])}</h2>")
        else:
            sluit_lijst()
            uit.append("    <p>%s</p>" % inline(" ".join(blok.splitlines())))
    sluit_lijst()
    return "\n".join(uit)


MAANDEN = ["januari","februari","maart","april","mei","juni",
           "juli","augustus","september","oktober","november","december"]


def nl_datum(d):
    try:
        j, m, dag = d.split("-")[:3]
        return f"{int(dag)} {MAANDEN[int(m)-1]} {j}"
    except Exception:
        return d


ARTIKELEN = []
_map = os.path.join(OUT, "content", "inspiratie")
for _naam in sorted(os.listdir(_map)) if os.path.isdir(_map) else []:
    if not _naam.endswith(".md"):
        continue
    _fm, _body = lees_front_matter(open(os.path.join(_map, _naam), encoding="utf-8").read(), _naam)
    _fm["slug"] = _naam[:-3] + ".html"
    _fm["body"] = _body
    ARTIKELEN.append(_fm)
# Vastgepinde artikelen (veld "vastgepind") staan altijd bovenaan,
# daarna op datum van nieuw naar oud.
ARTIKELEN.sort(key=lambda a: (a.get("vastgepind") != "true", a.get("datum", "")),
               reverse=False)
ARTIKELEN.sort(key=lambda a: a.get("datum", ""), reverse=True)
ARTIKELEN.sort(key=lambda a: a.get("vastgepind") != "true")


def post_cards(posts, pad=""):
    return "".join(f"""
      <a class="post" href="{pad}{a['slug']}">
        <div class="post-img"><img src="{a.get('afbeelding','')}" alt="" loading="lazy"></div>
        <p class="post-meta">{a.get('categorie','')}{' &middot; ' + a['leestijd'] if a.get('leestijd') else ''}</p>
        <h3>{a['titel']}</h3><p>{a.get('samenvatting','')}</p></a>""" for a in posts)


LD_JSON = """
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"MedicalBusiness",
  "name":"Backpack",
  "url":"https://mybackpack.nl/",
  "description":"Leefstijlgeneeskunde, systemisch werk en regressietherapie in Amsterdam, Voorschoten en online.",
  "areaServed":["Amsterdam","Voorschoten","Nederland"],
  "priceRange":"\\u20ac99 - \\u20ac299",
  "location":[
    {"@type":"Place","name":"Backpack Amsterdam \\u2014 Clementine Mol","address":{"@type":"PostalAddress","addressLocality":"Amsterdam","addressCountry":"NL"}},
    {"@type":"Place","name":"Backpack Voorschoten \\u2014 Maaike Oosterveer","address":{"@type":"PostalAddress","streetAddress":"Veurseweg 182","postalCode":"2252 AG","addressLocality":"Voorschoten","addressCountry":"NL"}}
  ],
  "employee":[
    {"@type":"Person","name":"Clementine Mol","jobTitle":"Arts voor integrale geneeskunde en leefstijlgeneeskunde"},
    {"@type":"Person","name":"Maaike Oosterveer","jobTitle":"Regressie- en re\\u00efncarnatietherapeut"}
  ]
}
</script>"""

HOME = f"""<main id="top">

<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Backpack &middot; Amsterdam &middot; Voorschoten &middot; Online</p>
      <h1>je klachten hebben<br>een <em>verhaal</em></h1>
      <p class="lead">Vastgelopen in patronen, aanhoudende klachten of stress die niet weggaat?
        Wij zoeken samen naar de oorzaak. Om van daaruit te bewegen naar meer balans.</p>
      <div class="btn-row">
        <a class="btn btn-primary" {kennismaking_attrs()}>
          Plan gratis kennismaking <span class="arw">&rarr;</span></a>
        <a class="btn btn-ghost" href="#aanbod">Bekijk ons aanbod</a>
      </div>
      <div class="hero-meta">
        <span>Gratis kennismaking van 20 minuten</span><span>Geen wachtlijst</span>
      </div>
    </div>
    <div class="hero-img">
      <picture><source srcset="images/hero-duo.webp" type="image/webp"><img src="images/hero-duo.jpg" width="1400" height="1120"
           alt="Maaike Oosterveer en Clementine Mol van Backpack" fetchpriority="high"></picture>
    </div>
  </div>
</section>

<section class="section" id="verhaal" style="padding-top:clamp(32px,4vw,56px)">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Wat draag jij met je mee?</p>
      <h2>ieder mens draagt een<br>onzichtbare rugzak</h2>
      <p class="lead" style="margin-top:1.3rem;font-size:1rem">Daarin zit veel moois: je talenten,
        je kwaliteiten, je essentie en vele ervaringen. Tegelijk kan hij gevuld zijn met onverwerkte
        verhalen van eerdere ervaringen die je, vaak onbewust, meedraagt. Dat kan zich uiten in:</p>
      <ul class="checks">
        <li>{CHECK}Belemmerende patronen waar je in vastloopt</li>
        <li>{CHECK}Aanhoudende of onverklaarbare lichamelijke klachten</li>
        <li>{CHECK}Stress, burn-out of aanhoudende vermoeidheid</li>
        <li>{CHECK}Emotionele blokkades of relationele vraagstukken</li>
        <li>{CHECK}Levensvragen en zoeken naar richting</li>
      </ul>
      <p style="margin-top:1.6rem;color:var(--muted);font-size:.97rem">Geen quick fix, geen symptomen
        bestrijden — maar terug naar de kern, daar waar het begon. Je hoeft het niet alleen te doen,
        en het kan stap voor stap.</p>
    </div>
    <div class="split-img reveal">
      <picture><source srcset="images/verhaal-wandelen.webp" type="image/webp"><img src="images/verhaal-wandelen.jpg" width="1000" height="1200"
           alt="Maaike en Clementine wandelend over een bospad" loading="lazy"></picture>
    </div>
  </div>
</section>

<section style="padding-bottom:clamp(56px,7vw,90px)">
  <div class="wrap">
    <figure class="quote quote-kort reveal">
      <blockquote>Unpack your story</blockquote>
    </figure>
  </div>
</section>

<!-- ============ DIGITALE CHECK-UP ============
     Laagdrempelig instappunt. Zodra het check-up-bestand er is,
     komt de inhoud op check-up.html te staan.
============================================= -->
<section class="section" id="check-up" style="padding-top:0">
  <div class="wrap">
    <div class="panel-light panel-split reveal">
      <div>
        <p class="eyebrow" style="color:var(--forest);opacity:.6">Gratis &middot; 5 minuten &middot; geen account nodig</p>
        <h2 style="font-size:clamp(1.5rem,2.6vw,2.1rem)">doe de digitale check-up</h2>
        <p style="margin:1rem 0 0;color:var(--muted);max-width:56ch;font-size:.98rem">
          Nog niet klaar voor een gesprek? Begin hier. In een paar minuten krijg je zicht op
          welke lagen je kunt werken, wat jouw stip op de horizon is en wat jij nu nodig hebt.
          Er worden geen gegevens verzameld of opgeslagen. Jouw antwoorden zijn alleen voor jou.</p>
      </div>
      <a class="btn btn-primary" href="check-up.html">Start de check-up <span class="arw">&rarr;</span></a>
    </div>
  </div>
</section>

<section class="section" id="aanbod" style="padding-top:0">
  <div class="wrap">
    <div class="reveal" style="max-width:58ch">
      <p class="eyebrow">Ons aanbod</p>
      <h2>waar wil je beginnen?</h2>
      <p class="lead" style="margin-top:1.1rem;font-size:1rem">Weet je niet welke vorm bij je past?
        Dat hoeft ook niet — in de gratis kennismaking kijken we er samen naar.</p>
    </div>
    <div class="offer-grid reveal">

      <article class="card">
        <div class="card-head">
          <div class="card-icon"><img src="images/icoon-explore.svg" alt=""></div>
          <p class="card-name">Explore</p>
          <h3>Zelf aan de slag</h3>
        </div>
        <p>Kennis, inspiratie en praktische tools: blogs, gedichten, films en interviews over
          leefstijl, bewustzijn, systemisch werk en transgenerationeel trauma.</p>
        <div class="card-foot">
          <div class="who">
            <i style="display:grid;place-items:center">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--forest)" stroke-width="1.8"><path d="M12 3v18M3 12h18"/></svg>
            </i>
            <span><b>Van Clementine &amp; Maaike</b>Online, op eigen tempo</span>
          </div>
          <p class="price"><strong>Gratis</strong></p>
          <div class="card-links">
            <a class="tlink" href="zelf-aan-de-slag.html">Lees meer <span class="arw">&rarr;</span></a>
            <a class="btn btn-primary btn-sm" href="check-up.html">Doe de check-up</a>
          </div>
        </div>
      </article>

      <article class="card">
        <div class="card-head">
          <div class="card-icon"><img src="images/icoon-discover.svg" alt=""></div>
          <p class="card-name">Discover</p>
          <h3>Leefstijl,<br>integrale geneeskunde &amp;<br>systemisch werk</h3>
        </div>
        <p>Onderzoek onder professionele begeleiding wat je meedraagt. Je krijgt inzicht in hoe
          leefstijl je gezondheid beïnvloedt, plus praktische tools en adviezen voor voeding,
          beweging, slaap, energie, stressmanagement en zingeving. Verdiepend kunnen we kijken naar je
          familiesysteem en wat je (onbewust) met je meedraagt.</p>
        <div class="card-foot">
          <div class="who">
            <i><picture><source srcset="images/avatar-clementine.webp" type="image/webp"><img src="images/avatar-clementine.jpg" alt="" width="240" height="240" loading="lazy"></picture></i>
            <span><b>Met Clementine Mol</b>Amsterdam &amp; online</span>
          </div>
          <p class="price">Intake 60 min <strong>&euro;149</strong> &middot; vervolg vanaf <strong>&euro;99</strong></p>
          <div class="card-links">
            <a class="tlink" href="leefstijl-en-systemisch-werk.html">Lees meer <span class="arw">&rarr;</span></a>
            <a class="btn btn-primary btn-sm" href="https://backpack.clientomgeving.nl/afspraak-maken?t=gbFxFmGj" target="_blank" rel="noopener" data-book="clementine">Direct sessie boeken</a>
          </div>
        </div>
      </article>

      <article class="card">
        <div class="card-head">
          <div class="card-icon"><img src="images/icoon-unpack.svg" alt=""></div>
          <p class="card-name">Unpack</p>
          <h3>Regressietherapie</h3>
        </div>
        <p>Krijg inzicht in je familiesysteem. Verwerk onder professionele begeleiding wat nog
          onverwerkt is. In een veilige setting doorvoel je wat toen niet gevoeld kon worden.
          Geen hypnose — je blijft tijdens de sessie volledig bij bewustzijn.</p>
        <div class="card-foot">
          <div class="who">
            <i><picture><source srcset="images/avatar-maaike.webp" type="image/webp"><img src="images/avatar-maaike.jpg" alt="" width="240" height="240" loading="lazy"></picture></i>
            <span><b>Met Maaike Oosterveer</b>Voorschoten</span>
          </div>
          <p class="price">Intake 180 min <strong>&euro;299</strong> &middot; vervolg <strong>&euro;249</strong></p>
          <div class="card-links">
            <a class="tlink" href="regressietherapie.html">Lees meer <span class="arw">&rarr;</span></a>
            <a class="btn btn-primary btn-sm" href="{MAAIKE}" target="_blank" rel="noopener" data-book="maaike">Direct sessie boeken</a>
          </div>
        </div>
      </article>

    </div>
  </div>
</section>

<section style="padding-bottom:var(--section)">
  <div class="wrap">
    <div class="panel reveal">
      <div style="max-width:52ch">
        <p class="eyebrow">Hoe werkt het</p>
        <h2 style="font-size:clamp(1.6rem,2.9vw,2.3rem)">Benieuwd naar hoe we werken?</h2>
      </div>
      <div class="steps-grid">
        <div class="step"><span class="step-no">01</span><h3>gratis kennismaking</h3>
          <p>Twintig minuten, vrijblijvend en online. Je vertelt wat er speelt, wij vertellen wat we
          kunnen betekenen. Daarna beslis je rustig.</p></div>
        <div class="step"><span class="step-no">02</span><h3>intake</h3>
          <p>Je vult vooraf een intakeformulier in. In de eerste sessie brengen we samen in kaart
          wat er speelt en waar we zouden kunnen beginnen. Bij Maaike heb je direct na het
          intakegesprek een regressiesessie.</p></div>
        <div class="step"><span class="step-no">03</span><h3>jouw traject</h3>
          <p>Sessies op jouw tempo, met een plan op maat. Geen vast aantal, geen abonnement — we
          kijken steeds samen wat je nodig hebt.</p></div>
      </div>
      <p style="margin:clamp(28px,3.6vw,42px) 0 0;font-size:.88rem;color:var(--muted);max-width:64ch">
        De sessies worden niet vergoed door de zorgverzekeraar. Wél worden ze regelmatig vergoed
        vanuit een persoonlijk ontwikkelingsbudget — vraag het je werkgever.
        <a class="sublink" href="tarieven.html" style="margin-left:.4em">Bekijk alle tarieven</a></p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap split">
    <!-- Voorlopig alleen de foto. Zodra er een introductievideo is, wordt dit blok:
         een link met class "video reveal" naar de video, met daarin:
           ...dezelfde afbeelding...
           <span class="play"></span>
           <span class="video-cap">Maak kennis met Clementine en Maaike</span>
         </a>
         De opmaak daarvoor staat al klaar in assets/style.css onder "Video". -->
    <div class="split-img wide reveal">
      <picture><source srcset="images/video-still.webp" type="image/webp"><img src="images/video-still.jpg" width="1600" height="1000" alt="Clementine Mol en Maaike Oosterveer" loading="lazy"></picture>
    </div>
    <div class="reveal">
      <p class="eyebrow">Even voorstellen</p>
      <h2 style="font-size:clamp(1.55rem,2.8vw,2.2rem)">wie je tegenover<br>je krijgt</h2>
      <p class="lead" style="margin-top:1.2rem;font-size:1rem">Voordat je een afspraak maakt wil je
        waarschijnlijk weten met wie je te maken krijgt. Clementine is arts, Maaike therapeut — en
        we werken allebei op onze eigen manier naar dezelfde kern toe.</p>
      <div class="btn-row">
        <a class="btn btn-ghost" href="clementine.html">Over Clementine</a>
        <a class="btn btn-ghost" href="maaike.html">Over Maaike</a>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap method">
    <div class="method-sticky reveal">
      <p class="eyebrow">Onze werkwijze</p>
      <h2>integraal<br>en verdiepend</h2>
      <p class="lead" style="margin-top:1.2rem;font-size:1rem">Drie benaderingen, die elkaar kunnen
        aanvullen en versterken. Stap voor stap begeleiden we je naar de kern. Jij bepaalt welke
        benadering voor jou passend is.</p>
    </div>
    <div class="reveal">
      <article class="approach">
        <h3>Leefstijlgeneeskunde &amp; integrale geneeskunde <span class="approach-wie">Clementine</span></h3>
        <p>Inzicht in de invloed van leefstijl op je gezondheid. Praktische tools en adviezen rond
        voeding, beweging, slaap, energiemanagement, stressregulatie en zingeving — met aandacht
        voor alle lagen van gezondheid: fysiek, emotioneel, mentaal en spiritueel.</p></article>
      <article class="approach">
        <h3>Systemisch werk <span class="approach-wie">Clementine</span></h3>
        <p>Door inzicht in je familiesysteem en onbewuste dynamieken wordt duidelijk waar klachten,
        patronen of blokkades hun oorsprong vinden. Je wordt je bewust van jouw Backpack.</p></article>
      <article class="approach">
        <h3>Regressietherapie <span class="approach-wie">Maaike</span></h3>
        <p>Onverwerkte ervaringen die zich hebben vastgezet in je denken (overtuigingen), voelen
        (lichaam en emoties) en doen (gedrag) krijgen ruimte om verwerkt te worden. Je Backpack
        wordt lichter en er ontstaat ruimte voor heling en groei.</p></article>

      <div class="ijsberg reveal">
        <div class="ijs-top">
          <span class="ijs-tip"></span>
          <div><strong>Je klacht of thema</strong>
            <span>Datgene waar je verandering in wilt. Wat je ziet en voelt.</span></div>
        </div>
        <div class="ijs-water"><span>Wat eronder ligt</span></div>
        <div class="ijs-laag">
          <span class="ijs-num">1</span>
          <div><strong>Symptoomverlichting &amp; behandeling</strong>
            <span>Klachten verlichten via medicijnen, therapie of andere behandelingen.</span></div>
        </div>
        <div class="ijs-laag">
          <span class="ijs-num">2</span>
          <div><strong>Leefstijl &amp; zelfzorg</strong>
            <span>Een gezonde basis bouwen met aandacht voor voeding, beweging, slaap,
            ontspanning, verbinding en zingeving.</span></div>
        </div>
        <div class="ijs-laag onderwater">
          <span class="ijs-num">3</span>
          <div><strong>Jouw Backpack: bewustwording en verwerking</strong>
            <span>Inzicht krijgen in jouw familiesysteem, de thema's en patronen. Indien gewenst,
            de onverwerkte ervaringen verwerken die je — vaak onbewust — met je meedraagt.</span></div>
        </div>
      </div>
      <p class="muted" style="font-size:.9rem;margin-top:1.2rem">Ieder mens draagt een rugzak met
        talenten, kwaliteiten en ervaringen. Soms voel je hem nauwelijks, soms voelt hij zwaar. Wij
        geloven dat chronische klachten zelden op zichzelf staan: onder wat je ziet en voelt, liggen
        vaak diepere lagen. Dit zijn de drie lagen waarop je kunt werken.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap reveal">
    <div style="margin-bottom:clamp(28px,3.6vw,42px)">
      <p class="eyebrow">Wat het je kan brengen</p>
      <h2 style="font-size:clamp(1.5rem,2.5vw,2.05rem)">Naar meer gezondheid, welzijn en levensenergie</h2>
    </div>
    <div class="results-grid">
      <div class="result"><span class="result-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20c0-5 3-9 8-10-1 6-4 9-8 10Z"/><path d="M12 20c0-4-2.5-7.5-7-8.5.8 5 3.4 7.9 7 8.5Z"/><path d="M12 20v2"/></svg></span><strong>Betere zelfzorg</strong><p>Concrete handvatten voor een gezondere leefstijl.</p></div>
      <div class="result"><span class="result-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 8c2 0 2 5 4 5s2-9 4-9 2 12 4 12 2-6 4-6 2 2 4 2"/></svg></span><strong>Minder klachten</strong><p>Klachten en patronen kunnen verminderen of verdwijnen.</p></div>
      <div class="result"><span class="result-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="11" r="1.4"/><ellipse cx="12" cy="11" rx="5" ry="1.9"/><ellipse cx="12" cy="11" rx="9.2" ry="3.6"/><path d="M3 17.5c2.4 1.2 5.5 1.9 9 1.9s6.6-.7 9-1.9"/></svg></span><strong>Innerlijke rust &amp; helderheid</strong><p>Meer rust in je hoofd, meer richting.</p></div>
      <div class="result"><span class="result-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2.5 5.5 13.5H11l-1 8 8-11h-5.5l.5-8Z"/></svg></span><strong>Energie &amp; veerkracht</strong><p>Hernieuwde levensenergie en meer veerkracht.</p></div>
      <div class="result"><span class="result-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="19.4" r="2.1"/><circle cx="5" cy="6" r="2.1"/><circle cx="19" cy="6" r="2.1"/><path d="M12 17.3v-4.6M10.4 11.4 6.5 7.7M13.6 11.4l3.9-3.7"/></svg></span><strong>Systemisch inzicht</strong><p>Inzicht in je familiesysteem en bewustwording van je Backpack — wat je meedraagt en wat je onbewust meedroeg.</p></div>
    </div>
  </div>
</section>

<section style="padding-bottom:var(--section)">
  <div class="wrap">
    <figure class="quote reveal">
      <blockquote>duurzame verandering ontstaat wanneer het dagelijks leven en innerlijk werk elkaar ontmoeten</blockquote>
      <figcaption>Carry less, live more</figcaption>
    </figure>
  </div>
</section>

{reviews_section()}

<section class="section" id="inspiratie" style="padding-top:0">
  <div class="wrap">
    <div class="head-row reveal">
      <div><p class="eyebrow">Inspiratie</p><h2>uit onze rugzak</h2></div>
      <a class="tlink" href="inspiratie/index.html">Alles bekijken <span class="arw">&rarr;</span></a>
    </div>
    <div class="blog-grid reveal">{post_cards(ARTIKELEN[:3], "inspiratie/")}
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="panel-light panel-split reveal">
      <div>
        <p class="eyebrow" style="color:var(--forest);opacity:.6">Voor organisaties</p>
        <h3 style="font-size:clamp(1.35rem,2.3vw,1.8rem)">lezingen en workshops</h3>
        <p style="margin:.8rem 0 0;font-size:.96rem;color:var(--muted);max-width:56ch">Voor teams,
          organisaties, congressen en events. Over leefstijl en gezondheid, het verhaal achter de
          klacht, patronen doorbreken en transgenerationeel trauma. Enthousiast en nuchter, in
          eenvoud maar met diepgang.</p>
      </div>
      <a class="btn btn-primary" href="lezingen-en-workshops.html">Meer over lezingen <span class="arw">&rarr;</span></a>
    </div>
  </div>
</section>

{cta()}
</main>
"""

print("Bouwen:")
page("index.html",
     "Backpack | Leefstijlarts &amp; regressietherapie — Amsterdam, Voorschoten en online",
     "Vastgelopen in patronen of aanhoudende klachten? Backpack combineert leefstijlgeneeskunde, "
     "systemisch werk en regressietherapie. Plan een gratis kennismaking van 20 minuten.",
     HOME, extra=LD_JSON)


# ============================================================
#  DISCOVER — leefstijl & systemisch werk
# ============================================================
DISCOVER = f"""<main>
<section class="pagehead">
  <div class="wrap">
    {crumb("Leefstijl &amp; systemisch werk")}
    <p class="eyebrow">Discover &middot; met Clementine Mol</p>
    <h1>Leefstijl, integrale geneeskunde<br>&amp; systemisch werk</h1>
    <p class="lead">Ontdek wat er in jouw Backpack zit. In een 1-op-1 sessie staan jouw klacht,
      vraagstuk en wens centraal — met aandacht voor alle lagen van gezondheid.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="{CLEM}" target="_blank" rel="noopener" data-book="clementine">
        Boek een sessie met Clementine <span class="arw">&rarr;</span></a>
      <a class="btn btn-ghost" href="clementine.html">Over Clementine</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:clamp(30px,4vw,52px)">
  <div class="wrap split">
    <div class="prose reveal">
      <h2>wat je kunt verwachten</h2>
      <p>In een 1-op-1 sessie staan jouw klacht, vraagstuk en wens centraal. Hierbij kunnen alle
        lagen van gezondheid aan bod komen: fysiek, emotioneel, mentaal en spiritueel.</p>
      <p>Je krijgt kennis en inzicht in jezelf, je lichaam en je patronen, en leert hoe
        leefstijlfactoren je gezondheid beïnvloeden. Daarnaast ontvang je praktische tips en tools
        waarmee je zelf aan de slag kunt.</p>
      <p>Indien gewenst kijken we niet alleen naar de huidige klacht en situatie, maar ook naar wat
        erachter zit. Wat draag je met je mee? In een veilige setting help ik je te ontdekken welke
        thema's in jouw Backpack zitten. Eventueel verkennen we ook je familiesysteem.</p>
      <p>Stapsgewijs, en op jouw eigen tempo, gaan we terug naar de kern om van daaruit te bewegen
        naar meer bewustwording en zelfzorg. Hierdoor kunnen klachten verminderen of zelfs
        verdwijnen en kun je meer balans, helderheid en vitaliteit ervaren: het leven weer voelen
        én vieren.</p>
    </div>
    <div class="split-img reveal">
      <picture><source srcset="images/portret-clementine.webp" type="image/webp"><img src="images/portret-clementine.jpg" width="900" height="1125"
           alt="Clementine Mol, arts voor integrale geneeskunde" loading="lazy"></picture>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="panel reveal">
      <div style="max-width:52ch">
        <p class="eyebrow">Onderwerpen</p>
        <h2 style="font-size:clamp(1.5rem,2.7vw,2.1rem)">wat er aan bod kan komen</h2>
      </div>
      <ul class="checks cols2" style="margin-top:1.8rem">
        <li>{CHECK}Voeding</li>
        <li>{CHECK}Beweging</li>
        <li>{CHECK}Slaap</li>
        <li>{CHECK}Energie</li>
        <li>{CHECK}Stress en ontspanning</li>
        <li>{CHECK}Work-life balance</li>
        <li>{CHECK}Levensvragen en persoonlijke ontwikkeling</li>
        <li>{CHECK}Relaties en verbinding</li>
        <li>{CHECK}Terugkerende thema's en belemmerende patronen</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="reveal" style="max-width:52ch;margin-bottom:clamp(26px,3.4vw,40px)">
      <p class="eyebrow">Praktisch</p><h2>duur, tarieven en locatie</h2>
    </div>
    <div class="facts reveal">
      <div class="fact">
        <h4>Wat is inbegrepen</h4>
        <ul><li>Intakeformulier</li><li>Voorbereiding van de sessie</li>
          <li>Sessie inclusief een op maat gemaakt plan</li></ul>
      </div>
      <div class="fact">
        <h4>Locatie</h4>
        <p>Sessies vinden plaats in de praktijk in centrum Amsterdam of online. Het adres of de link
          ontvang je na het inplannen van de sessie.</p>
      </div>
      <div class="fact">
        <h4>Tarieven</h4>
        <table class="rate-table" style="margin-top:0">
          <tr><td>Intake (60 min)</td><td>&euro;149</td></tr>
          <tr><td>Vervolgsessie (45 min)</td><td>&euro;99</td></tr>
          <tr><td>Vervolgsessie (60 min)</td><td>&euro;149</td></tr>
          <tr><td>Vervolgsessie (120 min)</td><td>&euro;249</td></tr>
          <tr><td>Zakelijk uurtarief</td><td>&euro;199</td></tr>
        </table>
        <p style="margin-top:1rem;font-size:.86rem">Vrijgesteld van btw. Niet vergoed door de
          zorgverzekeraar — vraag je werkgever naar het persoonlijk ontwikkelingsbudget.</p>
      </div>
    </div>
  </div>
</section>

{reviews_section("Leefstijl")}
{cta(direct=False)}
</main>
"""

page("leefstijl-en-systemisch-werk.html",
     "Leefstijlarts Amsterdam | Leefstijlgeneeskunde &amp; systemisch werk — Backpack",
     "1-op-1 sessies met arts Clementine Mol over leefstijl, gezondheid en wat je onbewust "
     "meedraagt. In Amsterdam en online. Intake vanaf &euro;149.",
     DISCOVER)


# ============================================================
#  UNPACK — regressietherapie
# ============================================================
UNPACK = f"""<main>
<section class="pagehead">
  <div class="wrap">
    {crumb("Regressietherapie")}
    <p class="eyebrow">Unpack &middot; met Maaike Oosterveer</p>
    <h1>regressietherapie</h1>
    <p class="lead">Voorouderlijk werk, regressie- en reïncarnatietherapie. In een veilige setting
      verwerk je wat toen niet gevoeld kon worden. Praktijk in Voorschoten.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="{MAAIKE}" target="_blank" rel="noopener" data-book="maaike">
        Boek een sessie met Maaike <span class="arw">&rarr;</span></a>
      <a class="btn btn-ghost" href="maaike.html">Over Maaike</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:clamp(30px,4vw,52px)">
  <div class="wrap split">
    <div class="prose reveal">
      <h2>hoe het werkt</h2>
      <p>Deze therapie is een vorm van verwerkingstherapie. Alles wordt geweten in het onderbewuste,
        waar je door de juiste vragen te stellen contact mee kunt maken. Zowel met innerlijk
        kindstukken als met familie- en voorouderlijnen of eigen voorgaande levens.</p>
      <p>Deze vorm van therapie geeft je de mogelijkheid om in een veilige setting en onder
        begeleiding te doorvoelen wat toen niet gevoeld kon worden of is vastgezet.</p>
      <p>Bij het verwerken van onverwerkte verhalen kunnen er beelden ontstaan of ervaringen worden
        beleefd die niet altijd letterlijk kloppen. Je eigen perceptie — wat je ziet, voelt en
        lichamelijk ervaart — mengt zich met herinneringen uit het verleden en vormt het verhaal.</p>
      <p>Wat klopt, is de emotionele lading: een bevroren emotie die eindelijk ruimte krijgt om
        gevoeld en verwerkt te worden. Daarom is voor de verwerking de emotionele waarheid
        belangrijker dan de feitelijke details. De rode draad is betrouwbaar, ook wanneer de beelden
        deels symbolisch zijn.</p>

      <h2>trance, geen hypnose</h2>
      <p>Ik werk met trance, oftewel aandachtsconcentratie: het bewustzijn van nu, gericht op het
        onderbewuste. Ik maak dus geen gebruik van hypnose.
        Tijdens de sessie blijf je bewust en wilsbekwaam. Je kunt het vergelijken met het lezen van
        een goed boek of het kijken van een film: je bent afgestemd op het verhaal, maar je kunt
        gewoon besluiten om even naar de wc te gaan.</p>
    </div>
    <div class="split-img reveal">
      <picture><source srcset="images/portret-maaike.webp" type="image/webp"><img src="images/portret-maaike.jpg" width="900" height="1125"
           alt="Maaike Oosterveer, regressie- en reïncarnatietherapeut" loading="lazy"></picture>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap split">
    <div class="split-img wide reveal">
      <picture><source srcset="images/praktijk-voorschoten.webp" type="image/webp"><img src="images/praktijk-voorschoten.jpg" width="1200" height="900"
           alt="De praktijk van Maaike aan de Veurseweg in Voorschoten" loading="lazy"></picture>
    </div>
    <div class="prose reveal">
      <h2>de praktijk in Voorschoten</h2>
      <p>Op mijn locatie kun je na een sessie naar de sauna, zwemmen, een massage boeken, een
        wandeling maken in de natuur, iets eten of drinken, of een ijsje halen op de natuurboerderij
        waar verschillende dieren lopen.</p>
      <p>Mijn hond Mystic is aanwezig in de praktijk. Het is helaas niet mogelijk om je eigen hond
        mee te nemen.</p>
      <p style="margin-bottom:0"><a class="tlink" href="https://www.ivyboutiquewellness.nl/"
        target="_blank" rel="noopener">Meer over de wellness op locatie <span class="arw">&rarr;</span></a></p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="reveal" style="max-width:52ch;margin-bottom:clamp(26px,3.4vw,40px)">
      <p class="eyebrow">Praktisch</p><h2>duur, tarieven en locatie</h2>
    </div>
    <div class="facts reveal">
      <div class="fact">
        <h4>Wat is inbegrepen</h4>
        <ul><li>Intakeformulier</li><li>Voorbereiding van de sessie</li><li>Sessie</li></ul>
      </div>
      <div class="fact">
        <h4>Locatie</h4>
        <p>Sessies vinden fysiek in de praktijk plaats.<br>
          Veurseweg 182<br>2252 AG Voorschoten</p>
      </div>
      <div class="fact">
        <h4>Tarieven</h4>
        <table class="rate-table" style="margin-top:0">
          <tr><td>Intake (180 min)</td><td>&euro;299</td></tr>
          <tr><td>Vervolgsessie (150 min)</td><td>&euro;249</td></tr>
        </table>
        <p style="margin-top:1rem;font-size:.86rem">Inclusief btw. De sessies worden niet vergoed
          door de zorgverzekeraar.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <figure class="quote reveal">
      <blockquote>I hope you fall in love with being alive</blockquote>
      <figcaption>Maaike Oosterveer</figcaption>
    </figure>
  </div>
</section>

{reviews_section("Regressie", google=True)}
{cta()}
</main>
"""

page("regressietherapie.html",
     "Regressietherapie Voorschoten | Verwerkingstherapie &amp; voorouderlijk werk — Backpack",
     "Regressie- en reïncarnatietherapie bij Maaike Oosterveer in Voorschoten. Geen hypnose, "
     "wel diepgaand werk naar de kern. Intake 180 minuten voor &euro;299.",
     UNPACK)


# ============================================================
#  PROFIELPAGINA'S
# ============================================================
def profile(slug, naam, rol, plaats, portret, intro_paras, opleidingen,
            werkwijze_link, werkwijze_label, book_url, book_label, book_key,
            extra_regel="", title="", desc=""):
    paras = "".join(f"<p>{p}</p>\n      " for p in intro_paras)
    # Clementine wil haar naam hier niet nogmaals zien staan; alleen de
    # BIG-registratie blijft, want die hoort bij een arts thuis op de pagina.
    naam_regel = (f'<p class="muted" style="font-size:.9rem">{extra_regel}</p>'
                  if extra_regel else "")
    lijst = "".join(f"<li>{o}</li>" for o in opleidingen)
    voornaam = naam.split()[0]
    body = f"""<main>
<section class="pagehead">
  <div class="wrap">
    {crumb("Over " + voornaam)}
    <p class="eyebrow">{rol} &middot; {plaats}</p>
    <h1>over {voornaam}</h1>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,3vw,40px)">
  <div class="wrap split">
    <div class="prose reveal">
      {paras}
      {naam_regel}
      <div class="btn-row">
        <a class="btn btn-primary" href="{book_url}" target="_blank" rel="noopener" data-book="{book_key}">
          {book_label} <span class="arw">&rarr;</span></a>
        <a class="btn btn-ghost" href="{werkwijze_link}">{werkwijze_label}</a>
      </div>
    </div>
    <div class="split-img reveal">
      <img src="images/{portret}" width="900" height="1125" alt="{naam}" loading="lazy">
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="panel reveal">
      <p class="eyebrow">Achtergrond</p>
      <h2 style="font-size:clamp(1.5rem,2.7vw,2.1rem)">ervaring en opleidingen</h2>
      <ul class="checks cols2" style="margin-top:1.8rem">{"".join(f"<li>{CHECK}{o}</li>" for o in opleidingen)}</ul>
    </div>
  </div>
</section>

{cta()}
</main>
"""
    page(slug, title, desc, body)


profile(
    "clementine.html", "Clementine Mol",
    "Arts voor integrale geneeskunde en leefstijlgeneeskunde", "Amsterdam &amp; online",
    "portret-clementine-alt.webp",
    ["Niet alleen symptomen bestrijden, maar teruggaan naar de "
     "kern drijft mij. Met mijn achtergrond in geneeskunde, architectuur, Integrative Medicine en "
     "leefstijlgeneeskunde heb ik een brede kijk en combineer ik medische en systemische kennis en ervaring en intuïtie.",
     "In mijn sessies creëer ik een veilige, oordeelloze setting waarin we samen onderzoeken wat "
     "voor jou betekenisvol is. Ik help je bewust te worden van jouw Backpack: alles wat je "
     "meedraagt. Alle lagen van gezondheid — fysiek, emotioneel, mentaal en spiritueel — kunnen "
     "hierbij betrokken worden. Je krijgt uitleg en praktische tips waarmee je direct aan de slag "
     "kunt. Daarnaast ontstaat er inzicht en ruimte om te voelen, waardoor vaak beweging ontstaat."],
    ["Jaartraining Weg van het Wiel — regressietherapie, Maarten Oversier (heden)",
     "Opleiding Systeemdynamieken in families, Bert Hellinger instituut (heden)",
     "From Womb to World, pre- en perinatale psychologie, Anna Verwaal (2025)",
     "Arts voor Integrative Medicine en leefstijlgeneeskunde (2024 – heden)",
     "Academy for Integrative Medicine en leefstijlgeneeskunde, basis- en verdiepingsjaar (2020–2023)",
     "Bouwkundig arts Cordaan: gezonde woonzorgomgevingen (2021–2025)",
     "Basisarts acute ouderengeneeskunde, de Wijkkliniek, Amsterdam UMC &amp; Cordaan (2021–2022)",
     "Basisarts huisartsgeneeskunde (2020)",
     "Arts-onderzoeker <a class=\"sublink\" href=\"https://bensajetcentrum.nl/assets/2021/01/Ouderen-langer-zelfstandig-thuis-Maar-hoe-dan-Samenvatting.pdf\" target=\"_blank\" rel=\"noopener\">&lsquo;Ouderen langer zelfstandig thuis! Maar hoe dan?&rsquo;</a> Ben Sajet Centrum Amsterdam (2020–2021)",
     "Healthcare consultant Royal HaskoningDHV (2018–2019)",
     "Geneeskunde, Universiteit van Amsterdam, bachelor en master (2013–2018)",
     "Bouwkunde, TU Delft, bachelor (2010–2013)"],
    "leefstijl-en-systemisch-werk.html", "Lees meer over mijn werkwijze",
    CLEM, "Boek een sessie met Clementine", "clementine",
    extra_regel="BIG-registratie: 89924263801",
    title="Clementine Mol | Leefstijlarts en arts voor integrale geneeskunde — Amsterdam",
    desc="Clementine Mol is arts voor integrale geneeskunde en leefstijlgeneeskunde. "
         "Sessies in Amsterdam en online. BIG-geregistreerd.")

profile(
    "maaike.html", "Maaike Oosterveer",
    "Regressie- en reïncarnatietherapeut", "Voorschoten",
    "portret-maaike.webp",
    ["Graag breng ik je in contact met je eigen wijsheid. Geen methodes of lange trajecten, maar de "
     "diepte in om tot de kern te komen van hetgeen waar je aan wilt werken.",
     "Ik werk met verwerkingstherapie waarbij we teruggaan naar de periode waar de klacht ooit is "
     "ontstaan. Net als in de natuur is alles in ons leven met elkaar verweven. Onze ziel incarneert "
     "vaak met vele voorgaande levens en lessen in een familiesysteem. In deze familie zijn alle "
     "thema's die ertoe doen terug te vinden.",
     "Ik gun iedereen wat meer bewustzijn hierin, omdat het zo mooi in elkaar zit. We zijn hier om "
     "te leren van elkaar, dualiteit te ervaren en vooral het leven te leven."],
    ["Stage bij Maarten Oversier (2024–2025)",
     "Verdiepingsjaar, Maarten Oversier (2023)",
     "Jaartraining Weg van het Wiel, Maarten Oversier (2022)",
     "Intervisie en supervisie reïncarnatietherapie (2022 – heden)",
     "Ademcoach, Kasper van der Meulen",
     "Wim Hof module 1 &amp; 2",
     "Basistraining familieopstellingen, Het Lichtcentrum Amsterdam",
     "Opleiding coachen met honden",
     "Basic yoga training, Yogic Life",
     "Oersterk coachopleiding",
     "HBO sociale psychologie",
     "Bedrijfshulpverlening",
     "Politieachtergrond"],
    "regressietherapie.html", "Lees meer over mijn werkwijze",
    MAAIKE, "Boek een sessie met Maaike", "maaike",
    title="Maaike Oosterveer | Regressietherapeut in Voorschoten — Backpack",
    desc="Maaike Oosterveer is regressie- en reïncarnatietherapeut met een praktijk in "
         "Voorschoten. Verwerkingstherapie zonder hypnose, terug naar de kern.")


# ============================================================
#  DIGITALE CHECK-UP
# ============================================================
CHECKUP = f"""<main>
<section class="pagehead">
  <div class="wrap-narrow">
    {crumb("Digitale check-up")}
    <p class="eyebrow">Gratis &middot; 5 minuten &middot; geen account nodig</p>
    <h1>de digitale check-up</h1>
    <p class="lead">Nog niet klaar voor een gesprek? Begin hier. Je krijgt in een paar minuten zicht
      op welke leefstijlfactoren en thema's bij jou spelen — en waar de eerste winst te halen valt.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,3vw,40px)">
  <div class="wrap-narrow">

    <!-- ============================================================
         HIER KOMT DE CHECK-UP VAN CLEMENTINE

         Twee manieren om het losse HTML-bestand hier in te zetten:

         1. INSLUITEN (snelst, geen aanpassingen nodig)
            Zet het bestand in de map /check-up/ en vervang dit
            hele blok door:

            <iframe src='check-up/index.html' title='Digitale check-up'
                    style='width:100%;min-height:900px;border:0;border-radius:28px'
                    loading='lazy'></iframe>

         2. INBOUWEN (mooiste resultaat)
            Plak de inhoud van de <body> van het check-up-bestand
            hier rechtstreeks, en verwijder de eigen stijl uit dat
            bestand. Het neemt dan automatisch de Backpack-stijl
            over: kleuren, lettertype, knoppen en formuliervelden
            staan al klaar in assets/style.css.

         Laat mij weten welke van de twee je wilt, dan zet ik het
         voor je klaar.
    ============================================================ -->
    <div class="panel reveal" style="text-align:center;padding-block:clamp(56px,8vw,96px)">
      <p class="eyebrow" style="justify-content:center">Nog te plaatsen</p>
      <h2 style="font-size:clamp(1.4rem,2.5vw,1.9rem)">de check-up komt hier te staan</h2>
      <p class="muted" style="max-width:48ch;margin:1rem auto 0;font-size:.96rem">
        Zodra het bestand van Clementine er is, verschijnt de vragenlijst op deze plek —
        in de stijl van de rest van de site.</p>
    </div>

    <div class="reveal" style="margin-top:clamp(40px,5vw,64px)">
      <h2 style="font-size:clamp(1.4rem,2.5vw,1.9rem)">en daarna?</h2>
      <p class="lead" style="margin-top:1rem;font-size:1rem">De check-up geeft je een eerste beeld.
        Wil je er samen dieper op ingaan, dan is de gratis kennismaking de logische volgende stap.
        Twintig minuten, vrijblijvend.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="{CLEM}" target="_blank" rel="noopener" data-book="clementine">
          Plan gratis kennismaking <span class="arw">&rarr;</span></a>
        <a class="btn btn-ghost" href="index.html#aanbod">Bekijk het aanbod</a>
      </div>
    </div>

  </div>
</section>
</main>
"""

def bouw_checkup():
    """Zet de check-up van Clementine als eigen pagina in de site.

    De check-up blijft een zelfstandig document met een eigen ontwerp — dat is
    bewust. Een vragenlijst werkt beter zonder menu en voettekst eromheen: minder
    afleiding, meer mensen die hem afmaken.

    Aan de inhoud is niets veranderd. Er zijn drie dingen toegevoegd of hersteld:
      1. een terug-link, zodat je halverwege niet vastzit
      2. de link naar Clementine wees nog naar de oude URL (Clementine.html)
      3. titel, omschrijving en canonical voor de vindbaarheid
    """
    bron = os.path.join(OUT, "bron", "backpack-checkup.html")
    if not os.path.exists(bron):
        print("  check-up.html  OVERGESLAGEN — bronbestand niet gevonden")
        return
    s = open(bron, encoding="utf-8").read()

    # 0. huisstijl: kleuren en lettertype gelijktrekken met de rest van de site.
    #    De rustige opzet van één vraag per scherm blijft ongemoeid — die werkt.
    kleuren = {
        "#FDFBF5": "#FAF7F2",   # wit/room
        "#EDE9DC": "#EDE4D6",   # zand
        "#31423C": "#24433A",   # donkergroen
        "#5B6863": "#5F6D66",   # gedempt groen
        "#8FA09A": "#7C9A8B",   # salie
        "#D4DDD9": "#DCE5DE",   # licht salie
        "#d4967d": "#B5794F",   # terracotta -> klei
        "49,66,60": "36,67,58",  # rgba-randen
    }
    for oud_k, nieuw_k in kleuren.items():
        s = re.sub(re.escape(oud_k), nieuw_k, s, flags=re.I)
    s = s.replace(
        "family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Inter:wght@300;400;500;600",
        "family=Work+Sans:wght@300;400;500")
    s = s.replace("'Cormorant Garamond', serif", "'Work Sans', sans-serif")
    s = s.replace("'Cormorant Garamond',serif", "'Work Sans',sans-serif")
    s = s.replace('"Cormorant Garamond", serif', "'Work Sans', sans-serif")
    s = s.replace("'Inter', sans-serif", "'Work Sans', sans-serif")
    s = s.replace("'Inter',sans-serif", "'Work Sans',sans-serif")

    # 1b. tekstwijzigingen van Clementine
    s = s.replace("Bij Backpack geloven we dat klachten zelden op zichzelf staan.",
                  "Bij Backpack geloven we dat chronische klachten zelden op zichzelf staan.")
    s = s.replace("De drie lagen waarop je kunt werken", "Drie lagen waarop je kunt werken")

    # 1c. de kennismakingsknop volgt de instelling van de site
    if not EXTERN_KENNISMAKING:
        s = s.replace('href="https://backpack.clientomgeving.nl/afspraak-maken?t=gbFxFmGj"',
                      'href="contact.html"')

    # 2. verouderde link herstellen
    s = s.replace("https://mybackpack.nl/Clementine.html", "clementine.html")
    s = s.replace('<a href="clementine.html" class="btn-secondary" target="_blank">',
                  '<a href="clementine.html" class="btn-secondary">')

    # 3. metagegevens voor Google en sociale media
    meta = ('<meta name="description" content="Doe de gratis check-up van Backpack. '
            'In een paar minuten zicht op wat je meedraagt: leefstijl, patronen en thema\'s. '
            'Geen account nodig.">\n'
            '<link rel="canonical" href="https://mybackpack.nl/check-up.html">\n'
            '<meta name="theme-color" content="#24433A">\n'
            '<meta property="og:title" content="Wat draag jij met je mee? — Backpack">\n'
            '<meta property="og:description" content="Een check-up van een paar minuten. '
            'Gratis, geen account nodig.">\n'
            '<meta property="og:type" content="website">\n'
            '<meta property="og:locale" content="nl_NL">\n')
    s = s.replace("<link rel=\"preconnect\"", meta + "<link rel=\"preconnect\"", 1)

    # 1. terug-link, in de stijl van de check-up zelf
    terug_css = """
  .site-terug {
    width: 100%; max-width: 480px; padding: 16px 26px 12px;
    font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 400;
    color: #5F6D66; text-decoration: none; display: flex; align-items: center; gap: 8px;
    transition: color .2s;
  }
  .site-terug:hover { color: #24433A; }
"""
    s = s.replace("</style>", terug_css + "</style>", 1)
    s = s.replace("<body>", '<body>\n<a class="site-terug" href="index.html">'
                            '<span aria-hidden="true">&larr;</span> Terug naar Backpack</a>', 1)

    write("check-up.html", s, raw=True)


bouw_checkup()


# ============================================================
#  EXPLORE — zelf aan de slag
# ============================================================
EXPLORE = f"""<main>
<section class="pagehead">
  <div class="wrap">
    {crumb("Zelf aan de slag")}
    <p class="eyebrow">Explore &middot; gratis</p>
    <h1>zelf aan de slag</h1>
    <p class="lead">We willen je inspireren, kennis laten maken met onze visie en verhalen delen.
      Praktisch en concreet gericht op je gezondheid en leefstijl, en verdiepend zodat je begrip
      krijgt voor het familiesysteem waar je uit komt.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="check-up.html">Doe de digitale check-up <span class="arw">&rarr;</span></a>
      <a class="btn btn-ghost" href="inspiratie/index.html">Naar de artikelen</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:clamp(28px,3.6vw,48px)">
  <div class="wrap">
    <div class="offer-grid reveal" style="margin-top:0">
      <article class="card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="var(--forest)" stroke-width="1.6"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="9"/></svg></div>
        <h3>digitale check-up</h3>
        <p>Vijf minuten, gratis en zonder account. Zicht op welke leefstijlfactoren en thema's bij
          jou spelen.</p>
        <div class="card-foot"><a class="tlink" href="check-up.html">Start de check-up <span class="arw">&rarr;</span></a></div>
      </article>
      <article class="card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="var(--forest)" stroke-width="1.6"><path d="M4 19.5V5a2 2 0 012-2h13v18H6a2 2 0 01-2-1.5z"/><path d="M8 7h7M8 11h7"/></svg></div>
        <h3>artikelen en gedichten</h3>
        <p>Blogs, gedichten, films, boeken en interviews over o.a. leefstijl, bewustzijn,
          familiesysteem en transgenerationeel trauma.</p>
        <div class="card-foot"><a class="tlink" href="inspiratie/index.html">Naar de inspiratie <span class="arw">&rarr;</span></a></div>
      </article>
      <article class="card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="var(--forest)" stroke-width="1.6"><path d="M17 21v-2a4 4 0 00-4-4H6a4 4 0 00-4 4v2"/><circle cx="9.5" cy="7" r="4"/><path d="M22 21v-2a4 4 0 00-3-3.87"/></svg></div>
        <h3>lezingen en workshops</h3>
        <p>Voor teams, organisaties, congressen en events. Inspirerend, verbindend en aanzettend tot
          bewustwording.</p>
        <div class="card-foot"><a class="tlink" href="lezingen-en-workshops.html">Meer hierover <span class="arw">&rarr;</span></a></div>
      </article>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="head-row reveal">
      <div><p class="eyebrow">Inspiratie</p><h2>recent gedeeld</h2></div>
      <a class="tlink" href="inspiratie/index.html">Alles bekijken <span class="arw">&rarr;</span></a>
    </div>
    <div class="blog-grid reveal">{post_cards(ARTIKELEN[:3], "inspiratie/")}
    </div>
  </div>
</section>

{cta()}
</main>
"""

page("zelf-aan-de-slag.html",
     "Zelf aan de slag | Gratis inspiratie over leefstijl en bewustzijn — Backpack",
     "Artikelen, gedichten, films en interviews over leefstijl, gezondheid, bewustzijn en "
     "familiesystemen. Plus een gratis digitale check-up.",
     EXPLORE)


# ============================================================
#  LEZINGEN EN WORKSHOPS
# ============================================================
LEZINGEN = f"""<main>
<section class="pagehead">
  <div class="wrap">
    {crumb("Lezingen &amp; workshops")}
    <p class="eyebrow">Voor teams en organisaties</p>
    <h1>lezingen &amp; workshops</h1>
    <p class="lead">Met een persoonlijke insteek verzorgen wij lezingen en workshops voor teams,
      organisaties, congressen en events. Lezingen die inspireren, verbinden en aanzetten tot
      bewustwording en beweging.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="contact.html">Neem contact op <span class="arw">&rarr;</span></a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:clamp(28px,3.6vw,48px)">
  <div class="wrap split">
    <div class="prose reveal">
      <h2>wat we brengen</h2>
      <p>We delen onze visie op gezondheid en vitaliteit aan de hand van de Backpack-metafoor.
        Verhalen, praktische voorbeelden en nieuwe perspectieven, afgestemd op het thema en de
        doelgroep. Op onze manier: enthousiast, nuchter, in eenvoud, maar met diepgang.</p>
      <h2>onderwerpen</h2>
      <ul class="checks" style="margin-top:0">
        <li>{CHECK}Leefstijl, bewustzijn en gezondheid</li>
        <li>{CHECK}Het verhaal achter de klacht</li>
        <li>{CHECK}Ongezonde patronen: waarom ze ontstaan en hoe je ze doorbreekt</li>
        <li>{CHECK}Familiesystemen</li>
        <li>{CHECK}Transgenerationeel trauma en epigenetica</li>
        <li>{CHECK}Het verwerken van onverwerkte ervaringen</li>
      </ul>
      <p style="margin-top:1.8rem">Nieuwsgierig geworden? We denken graag met je mee.</p>
    </div>
    <div class="split-img wide reveal">
      <picture><source srcset="images/video-still.webp" type="image/webp"><img src="images/video-still.jpg" width="1600" height="1000"
           alt="Clementine en Maaike" loading="lazy"></picture>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="panel reveal">
      <div style="max-width:52ch">
        <p class="eyebrow">Ook mogelijk</p>
        <h2 style="font-size:clamp(1.5rem,2.7vw,2.1rem)">sessies voor medewerkers</h2>
        <p style="margin:1rem 0 0;color:var(--muted);font-size:.97rem">Naast lezingen verzorgen we
          ook individuele sessies binnen organisaties, bijvoorbeeld bij verzuim, stress of
          duurzame inzetbaarheid. Het zakelijk uurtarief is &euro;199, vrijgesteld van btw.</p>
        <div class="btn-row"><a class="btn btn-primary" href="contact.html">Vraag de mogelijkheden op <span class="arw">&rarr;</span></a></div>
      </div>
    </div>
  </div>
</section>

{cta()}
</main>
"""

page("lezingen-en-workshops.html",
     "Lezingen en workshops over leefstijl en bewustzijn — Backpack",
     "Lezingen en workshops voor teams, organisaties en congressen over leefstijl, gezondheid, "
     "patronen doorbreken en transgenerationeel trauma.",
     LEZINGEN)


# ============================================================
#  TARIEVEN
# ============================================================
TARIEVEN = f"""<main>
<section class="pagehead">
  <div class="wrap-narrow">
    {crumb("Tarieven")}
    <p class="eyebrow">Tarieven</p>
    <h1>wat kost een sessie?</h1>
    <p class="lead">Alle bedragen staan hieronder, zodat je vooraf weet waar je aan toe bent.
      Betaling vindt plaats voorafgaand aan de sessie.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,3vw,40px)">
  <div class="wrap-narrow">

    <div class="reveal">
      <p class="eyebrow">Discover &middot; met Clementine Mol</p>
      <h2 style="font-size:clamp(1.4rem,2.4vw,1.85rem)">Leefstijl, integrale geneeskunde &amp; systemisch werk</h2>
      <table class="rate-table">
        <tr><th>Sessie</th><th style="text-align:right">Tarief</th></tr>
        <tr><td>Intake (60 min)</td><td>&euro;149</td></tr>
        <tr><td>Vervolgsessie (45 min)</td><td>&euro;99</td></tr>
        <tr><td>Vervolgsessie (60 min)</td><td>&euro;149</td></tr>
        <tr><td>Vervolgsessie (120 min)</td><td>&euro;249</td></tr>
        <tr><td>Zakelijk uurtarief</td><td>&euro;199</td></tr>
      </table>
      <p class="muted" style="font-size:.88rem;margin-top:1rem">Vrijgesteld van btw. Sessies vinden
        plaats in Amsterdam of online.</p>
      <div class="btn-row" style="margin-top:1.4rem">
        <a class="btn btn-primary" href="{CLEM}" target="_blank" rel="noopener" data-book="clementine">
          Boek bij Clementine <span class="arw">&rarr;</span></a>
      </div>
    </div>

    <div class="reveal" style="margin-top:clamp(48px,6vw,76px)">
      <p class="eyebrow">Unpack &middot; met Maaike Oosterveer</p>
      <h2 style="font-size:clamp(1.4rem,2.4vw,1.85rem)">regressietherapie</h2>
      <table class="rate-table">
        <tr><th>Sessie</th><th style="text-align:right">Tarief</th></tr>
        <tr><td>Intake (180 min)</td><td>&euro;299</td></tr>
        <tr><td>Vervolgsessie (150 min)</td><td>&euro;249</td></tr>
      </table>
      <p class="muted" style="font-size:.88rem;margin-top:1rem">Inclusief btw. Sessies vinden fysiek
        plaats in de praktijk in Voorschoten.</p>
      <div class="btn-row" style="margin-top:1.4rem">
        <a class="btn btn-primary" href="{MAAIKE}" target="_blank" rel="noopener" data-book="maaike">
          Boek bij Maaike <span class="arw">&rarr;</span></a>
      </div>
    </div>

    <div class="panel reveal" style="margin-top:clamp(48px,6vw,76px)">
      <h2 style="font-size:clamp(1.3rem,2.2vw,1.7rem)">vergoeding</h2>
      <p style="margin:1rem 0 0;color:var(--muted);font-size:.97rem">Wij werken niet samen met
        zorgverzekeraars. Dat is een bewuste keuze: de mogelijke vergoedingen staan niet in
        verhouding tot wat we aanbieden, en zo blijven we vrij om de juiste aanpak te kiezen zonder
        beperkingen of protocollen.</p>
      <p style="margin:1rem 0 0;color:var(--muted);font-size:.97rem">Wél zien we regelmatig dat
        werkgevers de sessies vergoeden vanuit een persoonlijk ontwikkelingsbudget of
        vitaliteitsbudget. Vraag het gerust na — we denken graag mee over de onderbouwing.</p>
    </div>

    <div class="reveal" style="margin-top:clamp(40px,5vw,64px)">
      <h2 style="font-size:clamp(1.3rem,2.2vw,1.7rem)">annuleren en verzetten</h2>
      <div class="facts" style="margin-top:1.6rem">
        <div class="fact">
          <h4>Bij Clementine</h4>
          <p>Kosteloos tot 3 werkdagen voor de sessie, via de link in de herinneringsmail. Daarbinnen
            wordt 50% in rekening gebracht. Bij niet verschijnen of meer dan 15 minuten te laat komen
            het volledige bedrag.</p>
        </div>
        <div class="fact">
          <h4>Bij Maaike</h4>
          <p>Uiterlijk 48 uur van tevoren annuleren. Daarbinnen wordt de sessie volledig in rekening
            gebracht, tenzij er sprake is van overmacht.</p>
        </div>
      </div>
    </div>

  </div>
</section>

{cta()}
</main>
"""

page("tarieven.html",
     "Tarieven | Wat kost een sessie bij Backpack?",
     "Alle tarieven van Backpack op een rij. Leefstijlsessies vanaf &euro;99, regressietherapie "
     "vanaf &euro;249. Inclusief informatie over vergoeding en annuleren.",
     TARIEVEN, active="tarieven")


# ============================================================
#  VEELGESTELDE VRAGEN
# ============================================================
FAQ_ITEMS = [
 ("Met welke klachten en thema's kan ik terecht?", """
   <h4>Sessies met Clementine</h4>
   <p>Voor lichamelijke, emotionele en mentale klachten kun je terecht als je aan de slag wilt met je
   leefstijl en bewuster wilt worden van wat je onbewust nog met je meedraagt. Thema's die aan bod
   kunnen komen: voeding, beweging, slaap, energie, stress en ontspanning, work-life balance,
   levensvragen en persoonlijke ontwikkeling, relaties en verbinding, terugkerende thema's en
   belemmerende patronen.</p>
   <h4>Sessies met Maaike</h4>
   <p>Deze verwerkingstherapie is breed inzetbaar bij lichamelijke, emotionele en mentale klachten,
   en efficiënt omdat je naar de kern van het probleem gaat. Je hoeft niet in reïncarnatie te
   geloven, maar je moet je er wel voor kunnen openstellen. Voorbeelden: levensvragen,
   relatieproblemen, seksuele problemen, eetproblemen, traumaherstel, bindings- en verlatingsangst,
   onverklaarbare lichamelijke klachten, angsten en fobieën, dwanggedachten, misofonie, depressie,
   burn-out, vermoeidheid en allergie.</p>"""),
 ("Hoe ziet een eerste sessie eruit?", """
   <h4>Bij Clementine</h4>
   <p>Voor het intakegesprek ontvang je het intakeformulier. Ik neem dat vooraf door, zodat ik
   gerichtere vragen kan stellen en al een beeld heb van jou en je situatie. Tijdens de intake gaan
   we in op je klachten en thema's, en welke leefstijlfactoren een rol spelen. We formuleren een
   doelstelling en maken afspraken. In een vervolgsessie is er ruimte voor evaluatie of verdieping.</p>
   <h4>Bij Maaike</h4>
   <p>De sessie begint eigenlijk al bij het invullen van het intakeformulier. Het eerste uur gaan we
   in gesprek over jou en je familiesysteem, zodat we samen kunnen onderzoeken waar we die dag een
   sessie op gaan doen. Na een korte pauze volgt direct de eerste sessie. Bij een vervolgsessie is de
   voorbereiding al gedaan en volstaat een half uur gesprek vooraf.</p>"""),
 ("Hoe kan ik me voorbereiden?", """
   <p>Zodra je de afspraak gemaakt hebt, krijg je een e-mail met verdere informatie en het
   intakeformulier. Het invullen kost wat tijd — je kunt merken dat er dan al beweging ontstaat.
   Dankzij het formulier kunnen wij ons goed voorbereiden op de sessie.</p>"""),
 ("Wat kan ik na een sessie verwachten?", """
   <h4>Bij Clementine</h4>
   <p>Dat hangt af van de sessie. Een korte vervolgsessie is een evaluatiemoment: we bespreken wat
   goed gaat en wat nog een uitdaging is, en definiëren praktische vervolgstappen. In een lange
   vervolgsessie verkennen we verder wat je meedraagt. Dat kan intensief zijn, dus het is fijn om
   daarna wat tijd voor jezelf te nemen.</p>
   <h4>Bij Maaike</h4>
   <p>De sessies zijn vaak intensief. De eerste weken kun je wat meer dromen en kan er vermoeidheid
   loskomen. De ervaring is persoonlijk en meestal niet eenvoudig uit te leggen aan je omgeving.
   Vertrouw op je gevoel en zorg goed voor jezelf. Je gaat een proces in dat vaak een maand tot drie
   maanden nodig heeft. Daarom maak ik nooit direct een nieuwe afspraak — je voelt vanzelf wanneer
   dat nodig is.</p>"""),
 ("Hoeveel sessies heb ik nodig?", """
   <h4>Bij Clementine</h4>
   <p>Dat verschilt per cliënt. We stemmen het samen af en kijken per keer wat er nodig en gewenst is.</p>
   <h4>Bij Maaike</h4>
   <p>Vooraf is dat niet te zeggen. Soms is een klacht na één sessie opgelost; gemiddeld komen mensen
   twee tot vijf keer, met minimaal zes weken tot enkele maanden ertussen. Wat ik wel kan beloven is
   dat een sessie je altijd iets brengt.</p>"""),
 ("Wanneer kan ik geen sessie boeken?", """
   <h4>Bij Clementine</h4>
   <p>Mijn begeleiding is aanvullend op de reguliere zorg en niet ter vervanging van je huisarts of
   specialist. Ik bied geen acute of spoedeisende zorg. Het is belangrijk dat je een vaste huisarts hebt.</p>
   <h4>Bij Maaike</h4>
   <p>Omdat we bewust trauma's doorleven, is deze therapie in eerste instantie niet geschikt voor
   zwangere vrouwen, mensen die door een psychotische episode gaan, of wie tijdens een sessie niet
   nuchter kan zijn. Ik werk momenteel niet met kinderen; je bent welkom vanaf 16 jaar.</p>"""),
 ("Waarom moet ik vooraf betalen?", """
   <p>Om een efficiënte planning en administratie mogelijk te maken hebben wij er bewust voor gekozen
   de betaling vooraf te laten plaatsvinden. Zo kunnen wij onze tijd volledig besteden aan het geven
   van sessies.</p>"""),
 ("Hoe kan ik verzetten of annuleren?", """
   <h4>Bij Clementine</h4>
   <p>In de herinneringsmail vind je een link om de sessie af te zeggen. Kosteloos tot 3 werkdagen
   vooraf. Daarbinnen wordt 50% in rekening gebracht; bij niet verschijnen of meer dan 15 minuten te
   laat komen het volledige bedrag.</p>
   <h4>Bij Maaike</h4>
   <p>Afspraken dienen uiterlijk 48 uur van tevoren geannuleerd te worden. Daarbinnen wordt de sessie
   volledig in rekening gebracht, tenzij er sprake is van overmacht.</p>"""),
 ("Wat kost een sessie?", """
   <h4>Bij Clementine</h4>
   <p>Intake 60 min &euro;149 &middot; vervolg 45 min &euro;99 &middot; vervolg 60 min &euro;149
   &middot; vervolg 120 min &euro;249 &middot; zakelijk uurtarief &euro;199. Alles vrijgesteld van btw.</p>
   <h4>Bij Maaike</h4>
   <p>Intake 180 min &euro;299 &middot; vervolg 150 min &euro;249. Inclusief btw.</p>
   <p><a class="tlink" href="tarieven.html">Naar de tarievenpagina <span class="arw">&rarr;</span></a></p>"""),
 ("Worden de sessies vergoed door een verzekeraar?", """
   <p>Nee. Wij werken niet samen met verzekeraars, en dat is een bewuste keuze: de mogelijke
   vergoedingen staan niet in verhouding tot wat we aanbieden. Zo blijven we vrij om de juiste aanpak
   te kiezen, zonder beperkingen of protocollen. Vraag eventueel bij je werkgever na of er budget
   beschikbaar is.</p>"""),
]

FAQ_HTML = "".join(f"""
      <details>
        <summary>{q}</summary>
        <div class="answer">{a}</div>
      </details>""" for q, a in FAQ_ITEMS)

# Structured data zodat vragen en antwoorden in Google kunnen verschijnen
def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip().replace('"', "'")

FAQ_LD = ('\n<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"FAQPage",'
          '"mainEntity":[' + ",".join(
              '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
              % (q.replace('"', "'"), strip_tags(a)) for q, a in FAQ_ITEMS)
          + "]}\n</script>")

FAQ_BODY = f"""<main>
<section class="pagehead">
  <div class="wrap-narrow">
    {crumb("Veelgestelde vragen")}
    <p class="eyebrow">Veelgestelde vragen</p>
    <h1>vragen die vaak gesteld worden</h1>
    <p class="lead">Staat je vraag er niet bij? <a class="tlink" href="contact.html">Neem gerust
      contact op</a> — we antwoorden meestal binnen een werkdag.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(20px,2.6vw,36px)">
  <div class="wrap-narrow">
    <div class="faq reveal">{FAQ_HTML}
    </div>
    <div class="btn-row"><a class="btn btn-ghost" href="contact.html">Stel je vraag</a></div>
  </div>
</section>

{cta()}
</main>
"""

page("veelgestelde-vragen.html",
     "Veelgestelde vragen | Backpack",
     "Antwoord op de meestgestelde vragen over sessies bij Backpack: klachten, verloop, "
     "voorbereiding, aantal sessies, tarieven en vergoeding.",
     FAQ_BODY, active="faq", extra=FAQ_LD)


# ============================================================
#  CONTACT
# ============================================================
CONTACT = f"""<main>
<section class="pagehead">
  <div class="wrap">
    {crumb("Contact")}
    <p class="eyebrow">Contact</p>
    <h1>we horen graag<br>van je</h1>
    <p class="lead">Liever meteen een afspraak? Plan een gratis kennismaking van twintig minuten.
      Heb je eerst een vraag, gebruik dan het formulier hieronder.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,3vw,40px)">
  <div class="wrap split" style="align-items:start">

    <div class="reveal">
      <h2 style="font-size:clamp(1.4rem,2.4vw,1.85rem)">stel je vraag</h2>
      <!-- Het attribuut data-netlify zorgt dat Netlify de verzending gratis afhandelt.
           Bij een andere hostingpartij vervang je dit door hun formulier-adres. -->
      <form class="form" id="contactformulier" name="contact" method="POST" action="/bedankt.html"
            data-netlify="true" data-netlify-honeypot="bot-field" style="margin-top:1.6rem">
        <input type="hidden" name="form-name" value="contact">
        <p hidden><label>Niet invullen: <input name="bot-field"></label></p>
        <div class="field">
          <label for="naam">Naam</label>
          <input id="naam" name="naam" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="email">E-mailadres</label>
          <input id="email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="onderwerp">Waar gaat je vraag over?</label>
          <select id="onderwerp" name="onderwerp">
            <option>Leefstijl, integrale geneeskunde en systemisch werk</option>
            <option>Regressietherapie</option>
            <option>Lezing of workshop voor een organisatie</option>
            <option>Iets anders</option>
          </select>
        </div>
        <div class="field">
          <label for="bericht">Je bericht</label>
          <textarea id="bericht" name="bericht" required></textarea>
        </div>
        <div><button class="btn btn-primary" type="submit">Verstuur <span class="arw">&rarr;</span></button></div>
      </form>
    </div>

    <div class="reveal">
      <div class="split-img wide" style="aspect-ratio:4/5;margin-bottom:clamp(26px,3.4vw,38px)">
        <picture><source srcset="images/contact-duo.webp" type="image/webp">
          <img src="images/contact-duo.jpg" width="1000" height="1250"
               alt="Clementine Mol en Maaike Oosterveer" loading="lazy"></picture>
      </div>
      <div class="panel" style="padding:clamp(30px,4vw,44px)">
        <h3>direct een afspraak</h3>
        <p style="margin:.9rem 0 0;color:var(--muted);font-size:.95rem">Twintig minuten,
          vrijblijvend en gratis.</p>
        <div class="btn-row" style="margin-top:1.4rem">
          <a class="btn btn-primary" href="#contactformulier">
            Naar het formulier <span class="arw">&rarr;</span></a>
        </div>
      </div>

      <div class="facts" style="margin-top:clamp(30px,4vw,44px);grid-template-columns:1fr">
        <div class="fact">
          <h4>Praktijk Amsterdam</h4>
          <p>Clementine Mol &middot; leefstijl, integrale geneeskunde &amp; systemisch werk<br>
            Centrum Amsterdam — het adres ontvang je na het inplannen van de sessie.<br>
            Sessies kunnen ook online.</p>
        </div>
        <div class="fact">
          <h4>Praktijk Voorschoten</h4>
          <p>Maaike Oosterveer &middot; regressietherapie<br>
            Veurseweg 182<br>2252 AG Voorschoten</p>
        </div>
        <div class="fact">
          <h4>Mail ons rechtstreeks</h4>
          <ul>
            <li><a class="sublink" href="mailto:clementine@mybackpack.me">clementine@mybackpack.me</a></li>
            <li><a class="sublink" href="mailto:maaike@mybackpack.me">maaike@mybackpack.me</a></li>
          </ul>
        </div>
        <div class="fact">
          <h4>Volg onze reis</h4>
          <a class="social" href="https://www.instagram.com/mybackpack.nl" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"
                 stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/>
              <circle cx="12" cy="12" r="4.2"/>
              <circle cx="17.6" cy="6.4" r="1.1" fill="currentColor" stroke="none"/>
            </svg>
            <span>@mybackpack.nl</span>
          </a>
        </div>
        <div class="fact">
          <h4>Bedrijfsgegevens</h4>
          <p>Backpack<br>KvK 99312050</p>
        </div>
      </div>
    </div>

  </div>
</section>
</main>
"""

page("contact.html",
     "Contact | Backpack — Amsterdam, Voorschoten en online",
     "Neem contact op met Backpack of plan direct een gratis kennismaking van twintig minuten. "
     "Praktijk in Amsterdam en Voorschoten.",
     CONTACT, active="contact")



# ============================================================
#  BEDANKPAGINA NA HET CONTACTFORMULIER
# ============================================================
BEDANKT = f"""<main>
<section class="pagehead">
  <div class="wrap-narrow">
    <p class="eyebrow">Bericht verstuurd</p>
    <h1>Dank je wel</h1>
    <p class="lead">We hebben je bericht ontvangen en reageren meestal binnen een werkdag.
      Heb je haast? Plan gerust alvast een gratis kennismaking.</p>
    <div class="btn-row">
      <a class="btn btn-primary" {kennismaking_attrs()}>
        Plan gratis kennismaking <span class="arw">&rarr;</span></a>
      <a class="btn btn-ghost" href="index.html">Terug naar de homepage</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,3vw,44px)">
  <div class="wrap-narrow">
    <div class="panel-light panel-split reveal">
      <div>
        <p class="eyebrow" style="color:var(--forest);opacity:.6">In de tussentijd</p>
        <h3 style="font-size:clamp(1.25rem,2.1vw,1.6rem)">Doe de digitale check-up</h3>
        <p style="margin:.8rem 0 0;font-size:.96rem;color:var(--muted);max-width:52ch">Gratis, vijf
          minuten, geen account nodig. Zicht op welke lagen je kunt werken en wat jij nu nodig hebt.</p>
      </div>
      <a class="btn btn-primary" href="check-up.html">Start de check-up <span class="arw">&rarr;</span></a>
    </div>
  </div>
</section>
</main>
"""

page("bedankt.html", "Bericht verstuurd | Backpack",
     "Je bericht is verstuurd. We reageren meestal binnen een werkdag.",
     BEDANKT, extra='\n<meta name="robots" content="noindex">')

# ============================================================
#  INSPIRATIE — overzichtspagina
# ============================================================
INSPIRATIE = f"""<main>
<section class="pagehead">
  <div class="wrap">
    {crumb("Inspiratie", 1)}
    <p class="eyebrow">Inspiratie</p>
    <h1>uit onze rugzak</h1>
    <p class="lead">Hier vind je artikelen, gedichten, films en interviews. Met informatie en
      inspiratie over leefstijl, gezondheid, bewustzijn en verwerking.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(20px,2.6vw,36px)">
  <div class="wrap">
    <div class="blog-grid reveal">{post_cards(ARTIKELEN)}
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="panel-light panel-split reveal">
      <div>
        <p class="eyebrow" style="color:var(--forest);opacity:.6">Liever zelf ontdekken?</p>
        <h3 style="font-size:clamp(1.3rem,2.2vw,1.7rem)">doe de digitale check-up</h3>
        <p style="margin:.8rem 0 0;font-size:.96rem;color:var(--muted);max-width:52ch">Gratis, vijf
          minuten, geen account nodig. Zicht op welke leefstijlfactoren en thema's bij jou spelen.</p>
      </div>
      <a class="btn btn-primary" href="../check-up.html">Start de check-up <span class="arw">&rarr;</span></a>
    </div>
  </div>
</section>

{cta(1)}
</main>
"""

page(os.path.join("inspiratie", "index.html"),
     "Inspiratie | Artikelen over leefstijl, bewustzijn en verwerking — Backpack",
     "Blogs, gedichten, films en interviews over leefstijl, gezondheid, familiesystemen en "
     "het verwerken van onverwerkte ervaringen.",
     INSPIRATIE, active="inspiratie", depth=1)


# ============================================================
#  JURIDISCHE PAGINA'S (nog te vullen)
# ============================================================
def legal(slug, kop, titel, intro, links):
    # LET OP: deze pdf's staan nu nog op de oude site. Kopieer ze vóór livegang
    # naar de map files/ en maak de links relatief, anders breken ze bij de verhuizing.
    rijen = "".join(
        f'<li><a class="tlink" href="{u}" target="_blank" rel="noopener">{t} '
        f'<span class="arw">&rarr;</span></a></li>' for t, u in links)
    body = f"""<main>
<section class="pagehead">
  <div class="wrap-narrow">
    <h1>{kop}</h1>
    <p class="lead">{intro}</p>
  </div>
</section>
<section class="section" style="padding-top:clamp(20px,2.6vw,36px)">
  <div class="wrap-narrow reveal">
    <ul class="doclist">{rijen}</ul>
    <p class="muted" style="font-size:.88rem;margin-top:2rem">Vragen over deze documenten?
      <a class="sublink" href="contact.html">Neem contact op</a>.</p>
  </div>
</section>
</main>
"""
    page(slug, titel, intro, body)


legal("algemene-voorwaarden.html", "Algemene voorwaarden",
      "Algemene voorwaarden | Backpack",
      "Beide praktijken hanteren hun eigen algemene voorwaarden. Je kunt ze hieronder downloaden.",
      [("Algemene voorwaarden praktijk Clementine Mol (pdf)",
        "files/Algemenevoorwaarden-PraktijkClementineMol.pdf"),
       ("Algemene voorwaarden praktijk Maaike Oosterveer (pdf)",
        "files/Algemenevoorwaarden-PraktijkMaaikeOosterveer.pdf")])

legal("privacyverklaring.html", "Privacyverklaring",
      "Privacyverklaring | Backpack",
      "Beide praktijken hebben een eigen privacyverklaring. Je kunt ze hieronder downloaden.",
      [("Privacyverklaring praktijk Clementine Mol (pdf)",
        "files/PrivacyverklaringPraktijkClementineMol.pdf"),
       ("Privacyverklaring praktijk Maaike Oosterveer (pdf)",
        "files/PrivacyverklaringPraktijkMaaikeOosterveer.pdf")])


# ============================================================
#  ARTIKELPAGINA'S
#  Dit is het sjabloon dat het CMS straks vult. Elk artikel dat
#  Clementine publiceert krijgt automatisch deze opmaak.
# ============================================================
def article(bestand, categorie, titel, samenvatting, afbeelding, leestijd, datum, inhoud):
    body = f"""<main>
<article>
<section class="pagehead">
  <div class="wrap-narrow">
    <p class="eyebrow">{categorie}{leestijd}</p>
    <h1 style="font-size:clamp(2rem,4.2vw,3.1rem)">{titel}</h1>
    <p class="lead">{samenvatting}</p>
    <p class="muted" style="font-size:.85rem;margin-top:1.4rem">{datum}</p>
  </div>
</section>

<section style="padding-bottom:clamp(36px,4.5vw,60px)">
  <div class="wrap-narrow">
    <div class="split-img wide artikel-beeld reveal" style="aspect-ratio:16/9">
      <img src="{afbeelding}" alt="" loading="lazy">
    </div>
  </div>
</section>

<section style="padding-bottom:var(--section)">
  <div class="wrap-narrow prose reveal">
{inhoud}
  </div>
</section>
</article>

<section class="section" style="padding-top:0">
  <div class="wrap-narrow">
    <div class="panel-light reveal">
      <p class="eyebrow" style="color:var(--forest);opacity:.6">Verder lezen</p>
      <h3 style="font-size:clamp(1.25rem,2.1vw,1.6rem)">meer uit onze rugzak</h3>
      <div class="btn-row">
        <a class="btn btn-primary" href="index.html">Naar alle artikelen <span class="arw">&rarr;</span></a>
        <a class="btn btn-ghost" href="../check-up.html">Doe de check-up</a>
      </div>
    </div>
  </div>
</section>

{cta(1)}
</main>
"""
    page(os.path.join("inspiratie", bestand),
         f"{titel[0].upper()}{titel[1:]} | Backpack", samenvatting, body,
         active="inspiratie", depth=1)


for _a in ARTIKELEN:
    _bron = ""
    if _a.get("bronlink"):
        _bron = (f'\n    <div class="btn-row"><a class="btn btn-primary" href="{_a["bronlink"]}"'
                 f' target="_blank" rel="noopener">Bekijk de bron <span class="arw">&rarr;</span></a></div>')
    elif _a.get("categorie", "").split(" ")[0] in ("Gelezen", "Gezien", "Film"):
        _bron = ('\n    <div class="panel" style="margin-top:2rem"><p style="margin:0;font-size:.93rem">'
                 '<strong>Link naar de bron volgt.</strong> Vul in het CMS het veld '
                 '&lsquo;Link naar de bron&rsquo; in, dan verschijnt hier een knop.</p></div>')
    article(_a["slug"], _a.get("categorie", ""), _a["titel"], _a.get("samenvatting", ""),
            _a.get("afbeelding", ""),
            (" &middot; " + _a["leestijd"]) if _a.get("leestijd") else "",
            nl_datum(_a.get("datum", "")) + (" &middot; " + _a["auteur"] if _a.get("auteur") else ""),
            naar_html(_a["body"], _a.get("gedicht") == "true") + _bron)


# ============================================================
#  ROBOTS.TXT EN SITEMAP
#  Zoekmachines worden geweerd zolang de site niet op het echte
#  domein draait. Zodra mybackpack.nl eraan gekoppeld is, zet
#  Netlify de omgevingsvariabele URL en gaat de deur vanzelf open.
#  Zo kun je niet vergeten het om te zetten.
# ============================================================
LIVE_DOMEIN = "mybackpack.nl"
_url = os.environ.get("URL", "") or os.environ.get("DEPLOY_PRIME_URL", "")
IS_LIVE = LIVE_DOMEIN in _url

if IS_LIVE:
    write("robots.txt", "User-agent: *\nAllow: /\n\n"
                        f"Sitemap: https://{LIVE_DOMEIN}/sitemap.xml\n", raw=True)
else:
    write("robots.txt",
          "# Deze versie draait nog niet op het echte domein.\n"
          "# Zoekmachines wordt gevraagd hem te negeren. Dit gaat vanzelf open\n"
          f"# zodra de site op {LIVE_DOMEIN} draait \u2014 zie build.py.\n"
          "User-agent: *\nDisallow: /\n", raw=True)

_paginas = sorted(
    [f for f in os.listdir(OUT) if f.endswith(".html")] +
    ["inspiratie/" + f for f in sorted(os.listdir(os.path.join(OUT, "inspiratie")))
     if f.endswith(".html")] if os.path.isdir(os.path.join(OUT, "inspiratie")) else [])
_items = "".join(
    f"  <url><loc>https://{LIVE_DOMEIN}/{'' if p == 'index.html' else p}</loc></url>\n"
    for p in _paginas)
write("sitemap.xml",
      '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + _items + "</urlset>\n",
      raw=True)

if WAARSCHUWINGEN:
    print("\nLET OP:")
    for w in WAARSCHUWINGEN:
        print(w)

print("\nKlaar." + ("" if IS_LIVE else
      "  (robots.txt houdt zoekmachines nog buiten \u2014 dat klopt zolang dit niet mybackpack.nl is)"))
