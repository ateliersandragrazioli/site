"""Ferramenta do site: adiciona, marca como vendida ou remove uma peça.

Adicionar (trata a foto no padrão do site: vertical 4:5, mesma luz e cor):
  python3 ferramentas/peca.py adicionar FOTO.jpg --titulo "Peça orgânica azul" --medida "18 × 12 cm" \
      --tipo decoracao --descricao "Peça de bordas onduladas em esmalte azul" [--centro 0.55]

  --tipo      parede (placas, painéis, Acrílico)  ou  decoracao (pecinhas para mesa, lavabo...)
  --centro    onde está a peça na altura da foto, de 0 (topo) a 1 (base). Padrão 0.55.

Marcar como vendida (some do site, mas fica guardada):
  python3 ferramentas/peca.py vendida "Peça orgânica azul"

Listar:
  python3 ferramentas/peca.py listar

Depois de qualquer mudança: python3 montar_site.py
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FOTOS = RAIZ / "fotos"
LISTA = RAIZ / "pecas.json"


def carregar():
    return json.loads(LISTA.read_text(encoding="utf-8"))


def salvar(pecas):
    LISTA.write_text(json.dumps(pecas, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slug(texto):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:40]


def tratar_foto(origem, destino_base, centro=0.55):
    """Recorta em 4:5 na largura toda, centrando a peça na altura, e acerta luz e cor (tira o amarelado)."""
    from PIL import Image, ImageEnhance, ImageOps

    im = ImageOps.exif_transpose(Image.open(origem)).convert("RGB")
    w, h = im.size
    alvo_h = int(w * 5 / 4)
    if alvo_h > h:  # foto mais larga que 4:5: corta nas laterais
        alvo_w = int(h * 4 / 5)
        x = (w - alvo_w) // 2
        im = im.crop((x, 0, x + alvo_w, h))
    else:
        y = int(h * centro - alvo_h / 2)
        y = max(0, min(h - alvo_h, y))
        im = im.crop((0, y, w, y + alvo_h))
    im = im.resize((1200, 1500), Image.LANCZOS)

    # Luz e cor: neutraliza o tom quente da luz da estante, clareia um pouco, contraste leve.
    r, g, b = im.split()
    r = r.point(lambda v: v * 0.95)
    b = b.point(lambda v: min(255, v * 1.05))
    im = Image.merge("RGB", (r, g, b))
    im = ImageEnhance.Brightness(im).enhance(1.05)
    im = ImageEnhance.Contrast(im).enhance(1.04)

    grande = destino_base.with_suffix(".jpg")
    im.save(grande, quality=82, optimize=True, progressive=True)
    pequena = destino_base.parent / f"{destino_base.name}-800.jpg"
    im.resize((640, 800), Image.LANCZOS).save(pequena, quality=74, optimize=True, progressive=True)
    return grande.name


def adicionar(a):
    pecas = carregar()
    nome = "peca-" + slug(a.titulo + " " + a.medida)
    base = FOTOS / nome
    n = 2
    while base.with_suffix(".jpg").exists():
        base = FOTOS / f"{nome}-{n}"
        n += 1
    tratar_foto(a.foto, base, a.centro)
    pecas.append({"foto": base.name, "titulo": a.titulo, "medida": a.medida,
                  "descricao_foto": a.descricao, "tipo": a.tipo, "disponivel": True})
    salvar(pecas)
    print(f"Adicionada: {a.titulo} ({a.medida}) -> fotos/{base.name}.jpg")


def vendida(a):
    pecas = carregar()
    achou = [p for p in pecas if a.titulo.lower() in p["titulo"].lower() and p.get("disponivel", True)]
    if a.medida:
        achou = [p for p in achou if a.medida.replace(" ", "") in p["medida"].replace(" ", "")]
    if len(achou) != 1:
        print("Encontrei", len(achou), "peças com esse nome. Diga também a medida (--medida).")
        for p in achou:
            print(" -", p["titulo"], p["medida"])
        sys.exit(1)
    achou[0]["disponivel"] = False
    salvar(pecas)
    print("Marcada como vendida:", achou[0]["titulo"], achou[0]["medida"])


def listar(_):
    for p in carregar():
        estado = "disponível" if p.get("disponivel", True) else "vendida"
        print(f'{p["tipo"]:10} {estado:11} {p["titulo"]} · {p["medida"]}')


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("adicionar")
    s.add_argument("foto")
    s.add_argument("--titulo", required=True)
    s.add_argument("--medida", required=True)
    s.add_argument("--tipo", choices=["parede", "decoracao"], required=True)
    s.add_argument("--descricao", required=True)
    s.add_argument("--centro", type=float, default=0.55)
    s.set_defaults(fn=adicionar)
    s = sub.add_parser("vendida")
    s.add_argument("titulo")
    s.add_argument("--medida", default="")
    s.set_defaults(fn=vendida)
    s = sub.add_parser("listar")
    s.set_defaults(fn=listar)
    a = ap.parse_args()
    a.fn(a)
