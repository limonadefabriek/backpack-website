#!/usr/bin/env python3
"""
Backpack — foto's bijsnijden.

Alle uitsnedes staan hieronder in één lijst. Wil je een foto anders
gesneden hebben, pas dan het kadervak aan en draai dit script opnieuw.

Draaien:  python3 tools/fotos.py
Daarna:   open tools/CONTROLE.jpg en kijk of alles goed staat.

Waarom dit script bestaat: bij het bijsnijden werd eerder een foto op
de gok gecentreerd, waardoor gezichten buiten beeld vielen. Nu staat
elke uitsnede vastgelegd, is hij herhaalbaar, en dwingt het script je
om achteraf te kijken.

Het kadervak (l, t, r, b) is een fractie van de originele foto:
0 is links/boven, 1 is rechts/onder. Binnen dat vak wordt op de
gevraagde verhouding gesneden, met het midden van het vak als hart.
"""
import os
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
BRON = os.path.join(REPO, "bron", "fotos")      # hier staan de originelen
UIT = os.path.join(REPO, "images")

# bestand,                  doel,                        breedte, hoogte, kadervak
UITSNEDES = [
    ("AM2A5314.jpg",        "hero-duo",                   1400, 1120, (0, 0, 1, 1)),
    ("AM2A5122.jpg",        "verhaal-wandelen",           1000, 1200, (0, .04, 1, 1)),
    # Even voorstellen: begint hoog genoeg, anders vallen de gezichten eruit
    ("AM2A5296(1).jpg",     "video-still",                1600, 1000, (.06, .16, .80, .86)),
    ("AM2A5095.jpg",        "contact-duo",                1000, 1250, (0, .06, 1, 1)),
    ("pAM2A4857_pp(1).jpg", "portret-clementine",          900, 1125, (0, 0, 1, .88)),
    ("AM2A4528.jpg",        "portret-clementine-alt",      900, 1125, (.12, .16, .98, 1)),
    ("AM2A4449.jpg",        "portret-maaike",              900, 1125, (.18, .22, .96, 1)),
    ("AM2A4684.jpg",        "portret-maaike-alt",          900, 1125, (.22, .22, 1, 1)),
    ("pAM2A4857_pp(1).jpg", "avatar-clementine",           280,  280, (.10, .05, .86, .74)),
    ("AM2A4449.jpg",        "avatar-maaike",               280,  280, (.365, .295, .655, .58)),
    ("IMG_1917.jpg",        "praktijk-voorschoten",       1200,  900, (0, 0, 1, 1)),
]


def snijd(bestand, naam, breedte, hoogte, kader, kwaliteit=84):
    pad = os.path.join(BRON, bestand)
    if not os.path.exists(pad):
        print(f"  overgeslagen (origineel ontbreekt): {bestand}")
        return False
    im = Image.open(pad).convert("RGB")
    W, H = im.size
    l, t, r, b = (int(v * d) for v, d in zip(kader, (W, H, W, H)))
    im = im.crop((l, t, r, b))
    W, H = im.size
    doel = breedte / hoogte
    nw, nh = (int(H * doel), H) if W / H > doel else (W, int(W / doel))
    im = im.crop(((W - nw) // 2, (H - nh) // 2, (W - nw) // 2 + nw, (H - nh) // 2 + nh))
    im = im.resize((breedte, hoogte), Image.LANCZOS)
    im.save(os.path.join(UIT, naam + ".webp"), "WEBP", quality=kwaliteit, method=6)
    im.save(os.path.join(UIT, naam + ".jpg"), "JPEG", quality=kwaliteit,
            optimize=True, progressive=True)
    print(f"  {naam}  {breedte}x{hoogte}")
    return True


def controleblad(namen):
    """Zet alle uitsnedes naast elkaar in één afbeelding, zodat je in
    één oogopslag ziet of er niets is afgesneden."""
    from PIL import ImageDraw
    TH, KOL = 300, 4
    beelden = []
    for n in namen:
        p = os.path.join(UIT, n + ".webp")
        if os.path.exists(p):
            im = Image.open(p).convert("RGB")
            im.thumbnail((TH, TH))
            beelden.append((n, im))
    if not beelden:
        return
    rijen = (len(beelden) + KOL - 1) // KOL
    blad = Image.new("RGB", (KOL * (TH + 10) + 10, rijen * (TH + 34) + 10), "#eee")
    d = ImageDraw.Draw(blad)
    for i, (n, im) in enumerate(beelden):
        x, y = 10 + (i % KOL) * (TH + 10), 10 + (i // KOL) * (TH + 34)
        blad.paste(im, (x, y))
        d.text((x, y + TH + 8), n, fill="black")
    blad.save(os.path.join(HIER, "CONTROLE.jpg"), quality=88)
    print(f"\nControleblad: tools/CONTROLE.jpg — kijk hier of alles goed staat.")


if __name__ == "__main__":
    print("Foto's bijsnijden:")
    gelukt = [naam for bestand, naam, w, h, k in UITSNEDES if snijd(bestand, naam, w, h, k)]
    controleblad(gelukt)
    if not gelukt:
        print("\nGeen originelen gevonden. Zet ze in bron/fotos/ en draai dit opnieuw.")
