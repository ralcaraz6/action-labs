#!/usr/bin/env python3
"""Procesa las fotos del equipo: recorte cuadrado centrado en la cara, optimización y actualización del HTML."""
import json, os, re, glob, sys, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EQ = os.path.join(ROOT, "equipo")
E = lambda s: H.escape(s, quote=False)

try:
    from PIL import Image
except ImportError:
    sys.exit("Falta Pillow:  pip3 install Pillow")

def face_box(im):
    """Recorte cuadrado. Usa detección de caras si hay OpenCV; si no, encuadre superior clásico de retrato."""
    w, h = im.size
    side = min(w, h)
    try:
        import cv2, numpy as np
        gray = cv2.cvtColor(np.array(im.convert("RGB")), cv2.COLOR_RGB2GRAY)
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = cascade.detectMultiScale(gray, 1.1, 5, minSize=(60, 60))
        if len(faces):
            x, y, fw, fh = max(faces, key=lambda f: f[2] * f[3])
            cx, cy = x + fw / 2, y + fh / 2
            side = min(side, int(max(fw, fh) * 3.1)) or side
            left = int(max(0, min(w - side, cx - side / 2)))
            top = int(max(0, min(h - side, cy - side * 0.46)))   # deja aire sobre la cabeza
            return (left, top, left + side, top + side)
    except Exception:
        pass
    left = (w - side) // 2
    top = int((h - side) * 0.18) if h > side else 0
    return (left, top, left + side, top + side)

def main():
    content = json.load(open(os.path.join(ROOT, "content.json")))
    members = content["es"]["team"]["members"]
    made = []
    for m in members:
        slug = m.get("slug")
        if not slug: continue
        srcs = [p for ext in ("jpg","jpeg","png","webp","JPG","JPEG","PNG")
                for p in glob.glob(os.path.join(EQ, f"{slug}-src.{ext}")) + glob.glob(os.path.join(EQ, f"{slug}.{ext}"))]
        srcs = [p for p in srcs if not p.endswith(f"{slug}.jpg") or "-src" in p] or srcs
        if not srcs: continue
        src = srcs[0]
        im = Image.open(src).convert("RGB")
        if im.size[0] != im.size[1] or im.size[0] != 320:
            im = im.crop(face_box(im)).resize((320, 320), Image.LANCZOS)
        out = os.path.join(EQ, f"{slug}.jpg")
        im.save(out, "JPEG", quality=88, optimize=True, progressive=True)
        made.append(slug)
    print("fotos listas:", made or "ninguna")

    # actualizar las tarjetas
    def card(i, m):
        slug = m.get("slug", "")
        if os.path.exists(os.path.join(EQ, f"{slug}.jpg")):
            av = (f'<img class="tm-photo" src="equipo/{slug}.jpg" width="160" height="160" loading="lazy" '
                  f'decoding="async" alt="{E(m["name"])}">')
        else:
            av = (f'<div class="tm-avatar" aria-hidden="true"><span>{E(m["initials"])}</span></div>'
                  f'<!-- foto: guarda equipo/{slug}.jpg y vuelve a ejecutar equipo/procesar.py -->')
        return (f'      <li class="tm-card reveal">\n        {av}\n'
                f'        <p class="tm-name" data-i18n="team.members.{i}.name">{E(m["name"])}</p>\n'
                f'        <p class="tm-role" data-i18n="team.members.{i}.role">{E(m["role"])}</p>\n'
                f'        <p class="tm-bio" data-i18n="team.members.{i}.bio">{E(m["bio"])}</p>\n      </li>')

    grid = "\n" + "\n".join(card(i, m) for i, m in enumerate(members)) + "\n    "
    idx = os.path.join(ROOT, "index.html")
    h = open(idx).read()
    mm = re.search(r'(<ul class="team-grid">)([\s\S]*?)(</ul>)', h)
    if mm:
        h = h[:mm.end(1)] + grid + h[mm.start(3):]
        assert len(re.findall(r'class="tm-card', h)) == len(members), "recuento de tarjetas incorrecto"
        open(idx, "w").write(h)
        print("index.html actualizado con", len(members), "tarjetas")

if __name__ == "__main__":
    main()
