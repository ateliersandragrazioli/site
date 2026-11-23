"""Monta o site sandragrazioli.com.br (vitrine): index.html e privacidade.html.
Os dados que ainda faltam ficam em DADOS. Quando chegarem, é só preencher e rodar de novo: python3 montar_site.py"""
from pathlib import Path
from urllib.parse import quote

AQUI = Path(__file__).parent

DADOS = {
    "nome": "Sandra Grazioli Arte Cerâmica",
    "whatsapp": "",          # só números com DDI, ex.: 5511999999999. Vazio = botões levam para o Contato.
    "email": "ateliersandragrazioli@gmail.com",             # vazio = mostra "em breve"
    "instagram": "ateliersandragrazioli",
    "lojas": [               # (nome, cidade ou bairro, link opcional). A Bárbara vai mandar a lista.
        ("Design Supplier", "Rua Dr. Diogo de Faria, 1158<br>São Paulo, SP", "https://www.instagram.com/designsupplier/"),
    ],
}
MSG_WHATS = "Olá, Sandra! Vi suas peças no site e gostaria de saber mais."

FALTA = '<span class="falta">a preencher</span>'


def link_whats(msg=MSG_WHATS):
    if DADOS["whatsapp"]:
        return f'https://wa.me/{DADOS["whatsapp"]}?text={quote(msg)}'
    return "contato.html"


def botao_whats(texto="Conversar pelo WhatsApp", classe="btn", msg=MSG_WHATS):
    alvo = ' target="_blank" rel="noopener"' if DADOS["whatsapp"] else ""
    return f'<a class="{classe}" href="{link_whats(msg)}"{alvo}>{texto}</a>'


def simbolo(tam, cor="#2f261f"):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 100 100" aria-hidden="true" focusable="false">'
            f'<rect x="3" y="3" width="94" height="94" rx="3" fill="none" stroke="{cor}" stroke-width="4"/>'
            f'<rect x="12" y="12" width="76" height="76" rx="2" fill="#6b5440"/>'
            f'<path d="M12 62 C28 50 40 76 57 59 S82 36 88 41 V88 H12 Z" fill="#f1ece3"/></svg>')


def marca(tam_simb=40, classe="marca"):
    return (f'<a class="{classe}" href="index.html" aria-label="Sandra Grazioli Arte Cerâmica, página inicial">{simbolo(tam_simb)}'
            f'<span class="marca-txt"><span class="marca-nome">Sandra Grazioli</span><span class="marca-desc">Arte Cerâmica</span></span></a>')


CSS = """
@font-face { font-family: "Marcellus"; src: url(fontes/marcellus.woff2) format("woff2"); font-display: swap; }
@font-face { font-family: "Jost"; src: url(fontes/jost.woff2) format("woff2"); font-weight: 300 500; font-display: swap; }
@font-face { font-family: "Cormorant Garamond"; src: url(fontes/cormorant-italico.woff2) format("woff2"); font-style: italic; font-display: swap; }
:root { --branco:#f7f6f3; --papel:#ffffff; --linho:#ece5da; --pedra:#d6cfc4; --argila:#6b5440; --azul:#2e5662; --tinta:#2f261f; --apoio:#5f554c; --fio:#e2ddd4; color-scheme: light; }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 84px; }
body { margin: 0; background: var(--branco); color: var(--tinta); font-family: "Jost", Arial, sans-serif; font-weight: 300; font-size: 18px; line-height: 1.65; }
img { max-width: 100%; display: block; }
a { color: inherit; }
:focus-visible { outline: 3px solid var(--azul); outline-offset: 3px; border-radius: 2px; }
.pular { position: absolute; left: -9999px; top: 8px; background: var(--tinta); color: #fff; padding: 10px 16px; z-index: 50; }
.pular:focus { left: 16px; }
.wrap { max-width: 1180px; margin: 0 auto; padding: 0 max(20px, env(safe-area-inset-left)); }
h1, h2, h3 { font-family: "Marcellus", Georgia, serif; font-weight: 400; letter-spacing: .04em; line-height: 1.2; margin: 0; }
h2 { font-size: clamp(30px, 4vw, 44px); }
.olho { font-size: 13px; letter-spacing: .32em; text-transform: uppercase; color: var(--argila); margin: 0 0 14px; font-weight: 400; }
.italico { font-family: "Cormorant Garamond", Georgia, serif; font-style: italic; }
.falta { display: inline-block; font-size: 13px; letter-spacing: .04em; background: #fff3c4; color: #5a4a00; border: 1px dashed #b39500; padding: 1px 8px; border-radius: 4px; }

/* Topo */
.topo { position: sticky; top: 0; z-index: 20; background: rgba(247,246,243,.94); backdrop-filter: blur(8px); border-bottom: 1px solid var(--fio); }
.topo .wrap { display: flex; align-items: center; justify-content: space-between; gap: 20px; height: 76px; }
.marca { display: flex; align-items: center; gap: 14px; text-decoration: none; }
.marca-txt { display: grid; }
.marca-nome { font-family: "Marcellus", serif; text-transform: uppercase; letter-spacing: .14em; font-size: 19px; line-height: 1.1; }
.marca-desc { font-size: 10px; letter-spacing: .42em; text-transform: uppercase; color: var(--apoio); margin-top: 4px; }
.menu { display: flex; gap: 26px; align-items: center; font-size: 15px; }
.menu a { text-decoration: none; padding: 6px 0; }
.menu a:hover { color: var(--azul); }
.menu a[aria-current=page] { color: var(--azul); text-decoration: underline; text-underline-offset: 6px; text-decoration-thickness: 1px; }
.menu .btn { padding: 10px 18px; font-size: 14px; }
.menu-btn { display: none; background: none; border: 1px solid var(--pedra); border-radius: 6px; font: inherit; font-size: 15px; padding: 8px 14px; color: var(--tinta); cursor: pointer; }
@media (max-width: 900px) {
  .menu-btn { display: block; }
  .menu { display: none; position: absolute; top: 76px; left: 0; right: 0; background: var(--branco); flex-direction: column; align-items: stretch; gap: 0; padding: 8px 20px 20px; border-bottom: 1px solid var(--fio); }
  .menu.aberto { display: flex; }
  .menu a { padding: 14px 0; border-bottom: 1px solid var(--fio); font-size: 18px; }
  .menu .btn { margin-top: 14px; text-align: center; border-bottom: 0; }
  .marca-nome { font-size: 16px; }
}

.btn { display: inline-block; background: var(--azul); color: #fff; text-decoration: none; padding: 15px 28px; border-radius: 4px; font-weight: 400; letter-spacing: .04em; font-size: 17px; }
.btn:hover { background: #23434d; }
.btn-linha { display: inline-block; color: var(--tinta); text-decoration: none; padding: 14px 26px; border: 1px solid var(--tinta); border-radius: 4px; font-size: 17px; }
.btn-linha:hover { background: var(--tinta); color: #fff; }

/* Abertura */
.abertura { padding: 64px 0 80px; }
.abertura .wrap { display: grid; grid-template-columns: 1fr 1.05fr; gap: 64px; align-items: center; }
.abertura h1 { font-size: clamp(38px, 5.4vw, 66px); letter-spacing: .02em; }
.abertura p.sub { font-size: 20px; color: var(--apoio); max-width: 30em; margin: 22px 0 34px; }
.abertura .acoes { display: flex; gap: 14px; flex-wrap: wrap; }
.abertura figure { margin: 0; background: var(--papel); padding: 28px; box-shadow: 0 30px 60px -30px rgba(47,38,31,.35); }
.abertura figure img { aspect-ratio: 4 / 4.4; object-fit: cover; width: 100%; }
@media (max-width: 860px) { .abertura .wrap { grid-template-columns: 1fr; gap: 40px; } .abertura { padding-top: 36px; } }

.inicial { min-height: calc(100svh - 76px); display: grid; align-items: center; padding: 40px 0; }
.h-pag { font-size: clamp(32px, 4.6vw, 52px); }
.retrato-vazio { aspect-ratio: 4 / 5; background: var(--pedra); display: grid; place-content: center; text-align: center; gap: 10px; color: var(--apoio); font-family: "Marcellus", serif; letter-spacing: .1em; font-size: 20px; }
main { min-height: 50vh; }
.atelie { display: grid; grid-template-columns: 1fr minmax(260px, 380px); gap: 64px; align-items: center; }
.atelie h2 { margin-bottom: 18px; }
.atelie p { color: var(--apoio); font-size: 19px; }
.atelie video { width: 100%; aspect-ratio: 9 / 16; object-fit: cover; background: var(--pedra); }
@media (max-width: 760px) { .atelie { grid-template-columns: 1fr; gap: 28px; } .atelie video { max-width: 380px; margin: 0 auto; } }
@media (prefers-reduced-motion: reduce) { .atelie video { animation: none; } }
.disp { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 28px; }
.peca img { aspect-ratio: 4 / 5; object-fit: cover; width: 100%; background: var(--pedra); }
.peca h3 { font-size: 20px; margin: 16px 0 2px; }
.peca p { margin: 0 0 8px; color: var(--apoio); font-size: 16px; }
.link-whats { color: var(--azul); font-size: 16px; text-underline-offset: 4px; }
@media (max-width: 520px) { .disp { grid-template-columns: 1fr 1fr; gap: 18px; } .peca h3 { font-size: 17px; } }
/* Séries */
section.bloco { padding: 90px 0; }
.bloco.linho { background: var(--linho); }
.bloco.branco { background: var(--papel); }
.cab-bloco { max-width: 680px; margin-bottom: 48px; }
.cab-bloco p { color: var(--apoio); font-size: 19px; margin: 14px 0 0; }
.series { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
.serie img { aspect-ratio: 3 / 4; object-fit: cover; width: 100%; background: var(--pedra); }
.serie h3 { font-size: 26px; margin: 22px 0 8px; }
.serie p { margin: 0; color: var(--apoio); }
@media (max-width: 860px) { .series { grid-template-columns: 1fr; gap: 48px; } }

/* Galeria */
.galeria { columns: 3 280px; column-gap: 20px; }
.galeria figure { margin: 0 0 20px; break-inside: avoid; }
.galeria figcaption { font-size: 15px; color: var(--apoio); margin-top: 8px; }
.aviso-peca { margin-top: 30px; font-size: 22px; color: var(--argila); max-width: 34em; }

/* Sobre */
.sobre { display: grid; grid-template-columns: .9fr 1.1fr; gap: 70px; align-items: center; }
.sobre img { aspect-ratio: 4 / 5; object-fit: cover; width: 100%; }
.sobre p { margin: 0 0 18px; }
.citacao { font-size: 30px; line-height: 1.3; color: var(--argila); margin: 28px 0 0; padding-left: 22px; border-left: 2px solid var(--pedra); }
@media (max-width: 860px) { .sobre { grid-template-columns: 1fr; gap: 36px; } }

/* Como encomendar */
.passos { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(4, 1fr); gap: 28px; counter-reset: p; }
.passos li { counter-increment: p; border-top: 1px solid var(--tinta); padding-top: 20px; }
.passos li::before { content: counter(p, decimal-leading-zero); font-family: "Marcellus", serif; font-size: 15px; letter-spacing: .2em; color: var(--argila); }
.passos h3 { font-size: 22px; margin: 10px 0 8px; }
.passos p { margin: 0; color: var(--apoio); font-size: 17px; }
@media (max-width: 860px) { .passos { grid-template-columns: 1fr 1fr; } }
@media (max-width: 520px) { .passos { grid-template-columns: 1fr; } }

/* Lojas */
.lojas { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; list-style: none; padding: 0; margin: 0; }
.lojas li { background: var(--papel); border: 1px solid var(--fio); padding: 24px; }
.lojas b { font-family: "Marcellus", serif; font-weight: 400; font-size: 21px; letter-spacing: .04em; display: block; }
.lojas span { color: var(--apoio); font-size: 16px; }

/* Perguntas */
.perguntas { max-width: 820px; }
.perguntas details { border-bottom: 1px solid var(--pedra); }
.perguntas summary { cursor: pointer; padding: 22px 36px 22px 0; font-size: 20px; font-weight: 400; list-style: none; position: relative; }
.perguntas summary::-webkit-details-marker { display: none; }
.perguntas summary::after { content: "+"; position: absolute; right: 4px; top: 18px; font-size: 26px; color: var(--argila); }
.perguntas details[open] summary::after { content: "–"; }
.perguntas details p { margin: 0 0 22px; color: var(--apoio); }

/* Contato */
.contato { text-align: center; }
.contato h2 { margin-bottom: 16px; }
.contato p { color: var(--apoio); font-size: 19px; max-width: 34em; margin: 0 auto 32px; }
.contato .acoes { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }
.contato .dados { margin-top: 34px; font-size: 17px; display: grid; gap: 6px; }

/* Rodapé */
.rodape { background: var(--tinta); color: #e9e3da; padding: 56px 0 40px; font-size: 16px; }
.rodape .wrap { display: grid; grid-template-columns: 1.4fr 1fr 1fr; gap: 40px; }
.rodape .marca-desc { color: #c9bfb2; }
.rodape h3 { font-family: "Jost", sans-serif; font-size: 13px; letter-spacing: .28em; text-transform: uppercase; font-weight: 400; color: #c9bfb2; margin-bottom: 14px; }
.rodape ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 8px; }
.rodape a { text-decoration: underline; text-underline-offset: 3px; text-decoration-color: rgba(233,227,218,.4); }
.rodape .final { grid-column: 1 / -1; border-top: 1px solid rgba(233,227,218,.18); padding-top: 22px; font-size: 14px; color: #c9bfb2; }
@media (max-width: 760px) { .rodape .wrap { grid-template-columns: 1fr; } }

/* Página de texto */
.texto { max-width: 780px; padding: 60px 0 90px; }
.texto h1 { font-size: clamp(34px, 5vw, 48px); margin-bottom: 10px; }
.texto h2 { font-size: 26px; margin: 42px 0 12px; }
.texto p, .texto li { color: #3e352e; }
.texto ul { padding-left: 22px; }
"""

JS = """<script>
  const b = document.querySelector('.menu-btn'), m = document.getElementById('menu');
  b.addEventListener('click', () => { const a = m.classList.toggle('aberto'); b.setAttribute('aria-expanded', a); });
  m.addEventListener('click', e => { if (e.target.tagName === 'A') { m.classList.remove('aberto'); b.setAttribute('aria-expanded', false); } });
</script>"""


def pagina(titulo, descricao, corpo, atual=""):
    nav = [("Obras", "obras"), ("Sobre", "sobre"), ("Como encomendar", "encomendar"), ("Onde encontrar", "lojas"), ("Contato", "contato")]
    menu = "".join(f'<a href="{i}.html"{" aria-current=page" if i == atual else ""}>{t}</a>' for t, i in nav)
    email = (f'<a href="mailto:{DADOS["email"]}">{DADOS["email"]}</a>' if DADOS["email"] else f'E-mail: {FALTA}')
    whats = (f'<a href="{link_whats()}" target="_blank" rel="noopener">WhatsApp</a>' if DADOS["whatsapp"] else f'WhatsApp: {FALTA}')
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{descricao}">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:image" content="https://sandragrazioli.com.br/fotos/essencias-azul.jpg">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="theme-color" content="#f7f6f3">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="fontes/marcellus.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="topo"><div class="wrap">
  {marca()}
  <button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button>
  <nav id="menu" class="menu" aria-label="Menu principal">{menu}{botao_whats("WhatsApp")}</nav>
</div></header>
<main id="conteudo">
{corpo}
</main>
<footer class="rodape"><div class="wrap">
  <div>{marca(44).replace('class="marca"', 'class="marca" style="color:#f7f6f3"').replace('#2f261f', '#f7f6f3')}
    <p style="margin:18px 0 0;max-width:24em">Peças únicas em cerâmica, feitas à mão em São Paulo.</p></div>
  <div><h3>Contato</h3><ul><li>{whats}</li><li>{email}</li>
    <li><a href="https://instagram.com/{DADOS["instagram"]}" target="_blank" rel="noopener">Instagram @{DADOS["instagram"]}</a></li></ul></div>
  <div><h3>Informações</h3><ul><li><a href="privacidade.html">Privacidade e cookies</a></li><li><a href="encomendar.html">Como encomendar</a></li><li><a href="encomendar.html#perguntas">Perguntas frequentes</a></li></ul></div>
  <p class="final">{DADOS["nome"]} · © 2026</p>
</div></footer>
{JS}
</body>
</html>
"""


def largura(arq):
    # Lê a largura real da foto (para o navegador escolher a versão certa).
    import subprocess
    out = subprocess.run(["sips", "-g", "pixelWidth", str(arq)], capture_output=True, text=True).stdout
    return int(out.split()[-1])


def img(nome, alt, extra="", sizes="(max-width: 860px) 100vw, 45vw"):
    menor = AQUI / "fotos" / f"{nome}-800.jpg"
    src = (f' srcset="fotos/{nome}-800.jpg {largura(menor)}w, fotos/{nome}.jpg {largura(AQUI / "fotos" / f"{nome}.jpg")}w" sizes="{sizes}"'
           if menor.exists() else "")
    return f'<img src="fotos/{nome}.jpg"{src} alt="{alt}" loading="lazy" decoding="async"{extra}>'


SERIES = [
    ("coluna-azul", "Essências", "Placas de cerâmica esmaltadas em várias cores, cada uma na sua moldura de madeira. Sozinhas ou em conjunto, viram um painel na parede.",
     "Coluna de placas da série Essências, em azul, branco e preto, cada uma em moldura de madeira"),
    ("texturas", "Texturas", "Cerâmica com relevo e esmalte, em moldura de madeira. A luz bate diferente ao longo do dia e a peça muda junto.",
     "Placas da série Texturas, escuras, com relevo de pontinhos e um brilho claro no centro"),
    ("acrilico", "Acrílico", "A peça de cerâmica dentro de uma caixa de acrílico transparente: parece flutuar na parede, como numa galeria.",
     "Peça de cerâmica verde com um traço cor de barro, dentro de uma caixa de acrílico transparente"),
]

GALERIA = [
    ("paineis", "Duas colunas de placas, uma em tons de barro e outra em azul e branco", "Painéis de parede"),
    ("tigela-ambar", "Tigela de bordas onduladas, cor de mel por fora, com esmalte azul e verde no fundo", "Tigela, esmalte de mel e azul"),
    ("tigela-branca", "Peça branca de bordas ondulantes, como uma flor aberta, sobre uma mesa de madeira", "Peça branca, forma orgânica"),
    ("acrilico-trio", "Três peças da série Acrílico, uma acima da outra, em verde, branco e barro", "Acrílico, trio"),
    ("tigela-verde", "Tigela verde-oliva brilhante, de bordas onduladas, com jardim ao fundo", "Tigela verde-oliva"),
    ("coluna-terra", "Coluna de placas em tons de barro e marrom, com manchas brancas", "Essências, coluna em barro"),
    ("tigela-grande", "Tigela grande de cerâmica clara, com bordas irregulares e pinceladas azuis", "Tigela grande"),
]

# Peças disponíveis (fotos tratadas a partir do que a Sandra mandou no WhatsApp). (foto, título, medida, alt)
DISPONIVEIS = [
    ("peca-acrilico-noite", "Série Acrílico", "16 × 16 cm",
     "Placa quadrada de cerâmica escura com relevo de escamas e um centro claro, dentro de caixa de acrílico"),
    ("peca-acrilico-oval", "Série Acrílico", "20 × 29 cm",
     "Peça oval de cerâmica cinza com esmalte em azul, verde, laranja e vermelho, dentro de caixa de acrílico"),
    ("peca-acrilico-oval-2", "Série Acrílico", "26 × 29 cm",
     "Peça oval de cerâmica cinza com esmalte em vermelho, laranja, lilás e verde, dentro de caixa de acrílico"),
    ("peca-folha", "Tigela com folhas", "21 × 17 cm",
     "Tigela branca de bordas curvas com desenho de folhas em tom bronze"),
    ("peca-tigela-oval", "Tigela oval esmaltada", "19 × 13 cm",
     "Tigela oval branca com bordas escuras e centro em verde, azul e lilás com esmalte craquelado"),
    ("peca-branca", "Peça branca orgânica", "25 × 22 cm",
     "Peça branca de bordas onduladas, como uma flor aberta"),
    ("peca-branca-2", "Peça branca orgânica", "25 × 11 cm",
     "Peça branca alongada, de bordas onduladas e levantadas nas pontas"),
    ("peca-cumbuca", "Cumbuca de barro e esmalte branco", "14 cm",
     "Cumbuca arredondada de barro cinza com borda irregular e interior em esmalte branco pontilhado"),
    ("peca-tigela-22", "Tigela esmaltada com relevo", "22 cm",
     "Tigela redonda de borda ondulada, com esmalte em tons de areia, lilás e mel por dentro e relevo escuro por fora"),
    ("peca-travessa", "Travessa oval esmaltada", "33 × 20 cm",
     "Travessa oval de barro escuro com esmalte em azul, âmbar e um centro verde brilhante"),
    ("peca-travessa-textura", "Travessa com textura", "25 × 14 cm",
     "Travessa de borda irregular, escura por fora e com textura em relevo dourada e marrom por dentro"),
    ("peca-prato-verde", "Prato fundo verde-oliva", "17 cm",
     "Prato fundo de borda ondulada em esmalte verde-oliva, com centro escuro brilhante"),
    ("peca-travessinha-azul", "Travessinha azul cobalto", "16 × 11 cm",
     "Travessinha oval com borda metálica escura e centro em esmalte azul cobalto"),
    ("peca-turquesa", "Peça orgânica turquesa", "15 × 10,5 cm",
     "Pequena peça de bordas dobradas em esmalte verde-água brilhante, com veio azul e prata no fundo"),
]

PERGUNTAS = [
    ("A peça vai ficar igual à da foto?",
     "Cada peça é única. Os esmaltes reagem de um jeito diferente a cada queima, então a sua peça terá a mesma série, as mesmas cores e o mesmo cuidado, mas nunca será idêntica à da foto. É isso que faz dela uma peça só sua."),
    ("Posso encomendar em outro tamanho ou com outras cores?",
     "Pode conversar comigo pelo WhatsApp e me contar o que você imagina. Eu digo o que é possível fazer e mando o orçamento."),
    ("Quanto tempo demora?",
     "Peças sob encomenda ficam prontas em cerca de 20 a 30 dias, dependendo do tamanho e da quantidade. O prazo exato vai no orçamento."),
    ("Como é o pagamento?",
     "Pelo Pix. Nas encomendas, metade é paga para começar e a outra metade na entrega. Tudo combinado no orçamento."),
    ("Vocês entregam?",
     "Sim. Em São Paulo, a entrega é feita por motoboy. Para outras cidades, a gente combina. O frete é cobrado à parte e informado antes."),
    ("Atendem arquitetos, decoradores e lojas?",
     "Sim. É só me chamar no WhatsApp contando sobre o projeto."),
]


def cab_pagina(olho, titulo, sub=""):
    s = f"<p>{sub}</p>" if sub else ""
    return f'<div class="cab-bloco"><p class="olho">{olho}</p><h1 class="h-pag">{titulo}</h1>{s}</div>'


def index():
    corpo = f"""
<section class="abertura inicial"><div class="wrap">
  <div>
    <p class="olho">Ateliê de cerâmica · São Paulo</p>
    <h1>A arte do fogo, que tudo transforma.</h1>
    <p class="sub">Peças únicas de cerâmica para a parede e para a mesa, feitas à mão por Sandra Grazioli. Do barro ao forno, cada uma no seu tempo.</p>
    <div class="acoes"><a class="btn" href="obras.html">Ver as obras</a>{botao_whats(classe="btn-linha")}</div>
  </div>
  <figure>{img("essencias-azul", "Conjunto de nove placas da série Essências, em azuis, verde e branco, com molduras de madeira", ' loading="eager" fetchpriority="high"').replace(' loading="lazy"', '')}</figure>
</div></section>
"""
    return pagina("Sandra Grazioli · Arte Cerâmica",
                  "Peças únicas de cerâmica feitas à mão por Sandra Grazioli: séries Essências, Texturas e Acrílico, painéis e tigelas. Encomendas pelo WhatsApp.",
                  corpo, atual="")


def obras():
    series = "".join(f'<article class="serie">{img(f, alt)}<h3>{t}</h3><p>{d}</p></article>' for f, t, d, alt in SERIES)
    galeria = "".join(f'<figure>{img(f, alt)}<figcaption>{leg}</figcaption></figure>' for f, alt, leg in GALERIA)
    disponiveis = "".join(
        f'<article class="peca">{img(f, alt, sizes="(max-width: 600px) 50vw, 25vw")}<h3>{t}</h3><p>{m}</p>'
        f'{botao_whats("Quero saber mais", classe="link-whats", msg=f"Olá, Sandra! Vi no site a peça {t} ({m}) e gostaria de saber mais.")}</article>'
        for f, t, m, alt in DISPONIVEIS)
    corpo = f"""
<section class="bloco branco"><div class="wrap">
  {cab_pagina("Obras", "Três jeitos de levar a cerâmica para a parede", "Todas as peças são feitas uma a uma. Cores, tamanhos e combinações podem ser pensados junto com você.")}
  <div class="series">{series}</div>
</div></section>
<section class="bloco linho" id="disponiveis" aria-labelledby="t-disp"><div class="wrap">
  <div class="cab-bloco"><p class="olho">Pronta entrega</p><h2 id="t-disp">Peças disponíveis</h2>
    <p>Peças prontas, que podem ir para a sua casa agora. Para saber o valor ou reservar, é só me chamar.</p></div>
  <div class="disp">{disponiveis}</div>
</div></section>
<section class="bloco" aria-labelledby="t-gal"><div class="wrap">
  <div class="cab-bloco"><p class="olho">Do ateliê</p><h2 id="t-gal">Painéis, tigelas e peças únicas</h2></div>
  <div class="galeria">{galeria}</div>
  <p class="aviso-peca italico">Cada peça é única: o esmalte reage de um jeito em cada queima, por isso nenhuma sai igual à outra.</p>
  <p style="margin-top:34px">{botao_whats("Perguntar sobre uma peça")}</p>
</div></section>
"""
    return pagina("Obras · Sandra Grazioli", "As séries Essências, Texturas e Acrílico, painéis e tigelas de Sandra Grazioli.", corpo, atual="obras")


def sobre():
    foto = AQUI / "fotos" / "sandra.jpg"
    retrato = (img("sandra", "Retrato de Sandra Grazioli, sorrindo, de óculos e cabelos longos") if foto.exists()
               else f'<div class="retrato-vazio" role="img" aria-label="Espaço para a foto da Sandra">Foto da Sandra<br>{FALTA}</div>')
    corpo = f"""
<section class="bloco linho"><div class="wrap sobre">
  {retrato}
  <div>
    {cab_pagina("Sobre", "Sandra Grazioli")}
    <p>Conheci a cerâmica numa exposição e me encantei. Fiz um curso e nunca mais parei.</p>
    <p>A cerâmica me ensina a lidar com o tempo, com a ansiedade, com as perdas e com as surpresas. Cada peça passa por várias fases: a ideia, a modelagem, o esmalte e a queima. Cada uma tem o seu tempo.</p>
    <p>Abrir o forno é a hora mais ansiosa e mais gostosa. Às vezes a peça sai completamente diferente do que eu imaginei, porque os esmaltes reagem de outro jeito. Ver o barro que eu amassei virar uma peça é mágico.</p>
    <p class="citacao italico">“E aí está a arte do fogo, que tudo transforma.”</p>
  </div>
</div></section>
<section class="bloco branco"><div class="wrap atelie">
  <div>
    <p class="olho">No ateliê</p><h2>Do barro à peça</h2>
    <p>Antes do esmalte e do forno, cada placa nasce assim: o barro aberto à mão, as linhas riscadas uma a uma e a textura feita com calma, até a peça ganhar o seu desenho.</p>
  </div>
  <video src="videos/atelie-barro.mp4" poster="videos/atelie-barro.jpg" autoplay muted loop playsinline controls preload="metadata"
    aria-label="Vídeo: as mãos da Sandra riscando linhas e texturas numa placa de barro no ateliê"></video>
</div></section>
"""
    return pagina("Sobre · Sandra Grazioli", "Quem é Sandra Grazioli e como nasce cada peça de cerâmica.", corpo, atual="sobre")


def encomendar():
    perguntas = "".join(f'<details><summary>{q}</summary><p>{r}</p></details>' for q, r in PERGUNTAS)
    passos = [
        ("Me chame no WhatsApp", "Conte qual peça chamou sua atenção, ou o que você imagina para o seu espaço."),
        ("Receba o orçamento", "Eu mando as medidas, o valor, o prazo e a entrega, tudo por escrito."),
        ("Reserve com o Pix", "Metade para começar. Aí a peça entra no ateliê: modelagem, esmalte e queima."),
        ("Receba em casa", "Em cerca de 20 a 30 dias. A outra metade é paga na entrega."),
    ]
    passos_html = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in passos)
    corpo = f"""
<section class="bloco branco"><div class="wrap">
  {cab_pagina("Como encomendar", "Simples, pelo WhatsApp", "Não tem carrinho nem cadastro. Você conversa direto comigo.")}
  <ol class="passos">{passos_html}</ol>
  <p style="margin-top:40px">{botao_whats("Pedir um orçamento", msg="Olá, Sandra! Gostaria de pedir um orçamento.")}</p>
</div></section>
<section class="bloco linho" id="perguntas"><div class="wrap">
  <div class="cab-bloco"><p class="olho">Perguntas frequentes</p><h2>Antes de encomendar</h2></div>
  <div class="perguntas">{perguntas}</div>
</div></section>
"""
    return pagina("Como encomendar · Sandra Grazioli", "Como encomendar uma peça de Sandra Grazioli: orçamento pelo WhatsApp, Pix, prazo e entrega.", corpo, atual="encomendar")


def lojas():
    itens = "".join(
        f'<li><b>{n}</b>{f"<span>{c}</span><br>" if c else ("" if l else f"<span>{FALTA}</span>")}{f"<a href={l} target=_blank rel=noopener>Ver a loja no Instagram</a>" if l else ""}</li>'
        for n, c, l in DADOS["lojas"])
    corpo = f"""
<section class="bloco"><div class="wrap">
  {cab_pagina("Onde encontrar", "Minhas peças nas lojas" if len(DADOS["lojas"]) > 1 else "Minhas peças na loja", "Você também encontra as peças, ao vivo, " + ("nestas lojas parceiras." if len(DADOS["lojas"]) > 1 else "na loja parceira."))}
  <ul class="lojas">{itens}</ul>
</div></section>
"""
    return pagina("Onde encontrar · Sandra Grazioli", "Lojas onde encontrar as peças de Sandra Grazioli.", corpo, atual="lojas")


def contato():
    corpo = f"""
<section class="bloco branco contato"><div class="wrap">
  {cab_pagina("Contato", "Vamos conversar?").replace('class="cab-bloco"', 'class="cab-bloco" style="margin:0 auto 18px"')}
  <p>Me mande uma mensagem contando qual peça você gostou ou o que você imagina. Eu respondo pessoalmente.</p>
  <div class="acoes">{botao_whats()}<a class="btn-linha" href="https://instagram.com/{DADOS["instagram"]}" target="_blank" rel="noopener">Ver o Instagram</a></div>
  <div class="dados">
    <span>WhatsApp: {DADOS["whatsapp"] and "+" + DADOS["whatsapp"] or FALTA}</span>
    <span>E-mail: {DADOS["email"] or FALTA}</span>
    <span>Instagram: @{DADOS["instagram"]}</span>
  </div>
</div></section>
"""
    return pagina("Contato · Sandra Grazioli", "Fale com Sandra Grazioli pelo WhatsApp ou Instagram.", corpo, atual="contato")


def erro404():
    corpo = f"""
<section class="bloco"><div class="wrap" style="text-align:center;max-width:640px">
  <div style="display:grid;justify-items:center;margin-bottom:28px">{simbolo(84)}</div>
  <p class="olho">Página não encontrada</p>
  <h1 class="h-pag" style="margin-bottom:18px">Essa página não existe</h1>
  <p style="color:var(--apoio)">O endereço pode ter mudado. Volte para o início ou veja as obras.</p>
  <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:30px"><a class="btn" href="/">Ir para o início</a><a class="btn-linha" href="/obras.html">Ver as obras</a></div>
</div></section>
"""
    return pagina("Página não encontrada · Sandra Grazioli", "Página não encontrada.", corpo).replace('href="', 'href="/').replace('href="/http', 'href="http').replace('href="/mailto', 'href="mailto').replace('href="/#', 'href="#').replace('src="fotos', 'src="/fotos').replace("url(fontes", "url(/fontes").replace('href="//', 'href="/')


def privacidade():
    email = DADOS["email"] or FALTA
    corpo = f"""
<div class="wrap"><article class="texto">
  <p class="olho">Privacidade e cookies</p>
  <h1>Como cuidamos dos seus dados</h1>
  <p>Última atualização: novembro de 2026.</p>

  <h2>Quem é a responsável</h2>
  <p>Este site é de {DADOS["nome"]}, ateliê da artista Sandra Grazioli, em São Paulo. Para qualquer assunto sobre os seus dados, escreva para: {email}.</p>

  <h2>O que este site coleta</h2>
  <p>Este site é uma vitrine. Ele <b>não tem formulário, cadastro, carrinho nem pagamento</b>, e não usa cookies de propaganda nem de estatística (como Meta Pixel ou Google Analytics).</p>
  <p>Como todo site, a empresa que hospeda as páginas (Netlify) registra automaticamente dados técnicos de acesso, como o endereço IP, o navegador e a data e hora da visita, para manter o site no ar e protegido.</p>

  <h2>Quando você fala comigo pelo WhatsApp ou Instagram</h2>
  <p>Os botões do site abrem o WhatsApp ou o Instagram. A partir daí, você está usando o serviço dessas empresas (Meta), com as regras de privacidade delas. Eu recebo o que você me enviar, como nome, telefone e o que você quer encomendar, e uso isso <b>só para responder, fazer o orçamento, combinar a entrega e emitir os documentos da venda</b>.</p>
  <p>A base legal é a execução do pedido que você me fez (procedimentos preliminares de contrato) e, no que for exigido por lei, o cumprimento de obrigações legais.</p>

  <h2>Com quem os dados são compartilhados</h2>
  <ul>
    <li><b>Netlify</b>: hospedagem do site.</li>
    <li><b>Meta (WhatsApp e Instagram)</b>: quando você escolhe falar comigo por lá.</li>
    <li><b>Banco ou instituição do Pix</b>: quando você faz um pagamento.</li>
    <li><b>Entregador ou transportadora</b>: nome, endereço e telefone, só para a entrega.</li>
  </ul>
  <p>Seus dados não são vendidos nem usados para propaganda.</p>

  <h2>Por quanto tempo guardo</h2>
  <p>As conversas e os orçamentos ficam guardados enquanto forem necessários para atender você e pelo tempo que a lei exigir para os registros da venda. Você pode pedir para apagar o que não for obrigatório guardar.</p>

  <h2>Seus direitos</h2>
  <p>Pela Lei Geral de Proteção de Dados (LGPD), você pode pedir para saber quais dados tenho sobre você, corrigir, apagar, saber com quem foram compartilhados e retirar uma autorização dada. É só escrever para {email}.</p>

  <h2>Cookies</h2>
  <p>Este site não usa cookies de rastreamento. As fontes e as fotos ficam no próprio site, sem chamar serviços de terceiros. Se um dia passarmos a usar ferramentas de estatística ou de anúncios, elas só vão funcionar depois que você clicar em “Aceitar” num aviso, e esta página vai ganhar um botão para você mudar a sua escolha.</p>
</article></div>
"""
    return pagina("Privacidade e cookies · Sandra Grazioli", "Como o site de Sandra Grazioli Arte Cerâmica trata os seus dados.", corpo, atual="privacidade")


for nome, fn in [("index", index), ("obras", obras), ("sobre", sobre), ("encomendar", encomendar), ("lojas", lojas), ("contato", contato)]:
    (AQUI / f"{nome}.html").write_text(fn(), encoding="utf-8")
(AQUI / "privacidade.html").write_text(privacidade(), encoding="utf-8")
(AQUI / "404.html").write_text(erro404(), encoding="utf-8")
SITE = "https://sandragrazioli.com.br"
PAGS = ["", "obras.html", "sobre.html", "encomendar.html", "lojas.html", "contato.html", "privacidade.html"]
(AQUI / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
(AQUI / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}/{p}</loc></url>\n" for p in PAGS) + "</urlset>\n", encoding="utf-8")
(AQUI / "favicon.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">{simbolo(100)[simbolo(100).index(">") + 1:-6]}</svg>', encoding="utf-8")
print("site ok")
