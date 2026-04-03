"""
Por que precisamos de Ecologia? — Conversão Beamer → mathpres
Fonte: ecologia_modelagem.tex  (Modelagem Matemática, Aula 01)

Exemplo de referência produzido com a skill beamer-to-mathpres.
Documenta as decisões de layout, adaptações de conteúdo e limites respeitados.

Renderizar:
    manim-slides render ecologia_modelagem_manim.py AulaEcologia

Apresentar:
    manim-slides present AulaEcologia
"""

import sys
sys.path.insert(0, "/Users/1moi6/GitHub/Python/manim-layouts")

from manim import *
from mathpres import AcademicBase, place_text, place_graphic, theme
from mathpres import ContentGrid, apply_tex_theme, set_theme
from mathpres.components import build_header_band, build_header_accent, build_header_content

set_theme("ocean_night")
apply_tex_theme()


# ── Helpers ───────────────────────────────────────────────────────────────────

def _T(text, sz=20, bold=False, italic=False, color=None):
    return Text(
        text,
        font_size=sz,
        weight=BOLD if bold else NORMAL,
        slant=ITALIC if italic else NORMAL,
        color=color or theme.C_TEXT_BODY,
        font=theme.FONT_SANS,
    )


def _hdr(scene, title, subtitle=""):
    """Adiciona banda+acento à cena e retorna o VGroup de conteúdo posicionado."""
    band = build_header_band()
    scene.add(band, build_header_accent())
    hdr = build_header_content(title, subtitle)
    hdr.move_to(band).align_to(band, LEFT).shift(RIGHT * 0.55)
    return hdr


# ── Classe principal ──────────────────────────────────────────────────────────

class AulaEcologia(AcademicBase):

    def construct(self):
        self.camera.background_color = ManimColor(theme.BG_MAIN)
        self._slide_capa()
        self._slide_colapso()
        self._slide_brasil()
        self._slide_padrao_comum()
        self._slide_intuicao_verbal()
        self._slide_por_que_ecologia()
        self._slide_definicao_krebs()
        self._slide_tres_palavras()
        self._slide_por_que_modelos()
        self._slide_o_que_o_modelo_exige()
        self._slide_conclusao2()
        self._slide_sintese()
        self._slide_proxima_aula()

    # ── Slide 01 — Capa ───────────────────────────────────────────────────────
    # Sem header band. Painel accent full-screen como fundo.
    # Animação progressiva: título → subtitle desliza → info desliza.
    # Adaptado da lógica de slide_titulo() em aula1_slides_manim.py (Fuzzy).
    def _slide_capa(self):
        g    = ContentGrid(shadow=True)
        main = g.panel(0, 100, 0, 100, accent=True)
        self.add(main)

        # ── 1. Título aparece sozinho, centralizado ──────────────────────────
        titulo = Text(
            "Por que precisamos de Ecologia?",
            font_size=44,
            weight=BOLD,
            font=theme.FONT_SANS,
            gradient=(theme.C_TEXT_H1, theme.ACCENT),
        )
        titulo.move_to(ORIGIN)
        self.play(Write(titulo), run_time=0.8)
        self.wait(0.6)

        # ── 2. Subtítulo desliza por baixo ───────────────────────────────────
        subtitulo = _T(
            "E por que a matemática é sua linguagem natural",
            sz=26, italic=True, color=theme.C_TEXT_H2,
        )
        g1 = VGroup(titulo.copy(), subtitulo).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        g1.move_to(ORIGIN)

        self.play(
            ReplacementTransform(titulo, g1[0]),
            FadeIn(subtitulo, shift=UP * 0.3),
            run_time=1.0,
        )
        self.wait(0.6)

        # ── 3. Info da aula desliza por baixo ────────────────────────────────
        info = _T("Modelagem Matemática · Aula 01", sz=20, color=theme.C_TEXT_ANNOT)
        g2 = VGroup(g1.copy(), info).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        g2.move_to(ORIGIN)

        self.play(
            ReplacementTransform(g1[0], g2[0][0]),
            ReplacementTransform(subtitulo, g2[0][1]),
            FadeIn(info, shift=UP * 0.3),
            run_time=1.0,
        )

        self.next_slide()
        self._fadeout()

    # ── Slide 02 — Um colapso que ninguém previu ──────────────────────────────
    # Blocos: intro (3 linhas) + Paradoxo (5 linhas) + "Por quê?" (retórica)
    # Layout: Grid1T2B
    #   · top (accent) — contexto histórico compacto
    #   · bl           — Paradoxo (block Beamer)
    #   · br           — pergunta retórica em destaque (place_graphic)
    def _slide_colapso(self):
        hdr = _hdr(self, "Um colapso que ninguém previu")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)  # 13.00 × 1.94 u
        bl  = g.panel(33, 100, 0,  50)               #  6.33 × 4.11 u
        br  = g.panel(33, 100, 50, 100)              #  6.33 × 4.11 u

        intro = VGroup(
            _T("Em 1989, o bacalhau do Atlântico Norte entrou em colapso", sz=21),
            _T("após 500 anos de pesca contínua. Em 1992: moratória total.", sz=21),
            _T("Trinta anos depois — a população não se recuperou.", sz=19,
               italic=True, color=theme.C_TEXT_H2),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        place_text(top, intro)

        paradoxo = VGroup(
            _T("Paradoxo:", sz=20, bold=True, color=theme.C_TEXT_H2),
            _T("Pescadores, gestores e biólogos", sz=20),
            _T("observavam o sistema há gerações.", sz=20),
            _T("Tinham intuição, experiência e dados.", sz=20),
            _T("E ainda assim — não previram,", sz=20),
            _T("não evitaram, não reverteram.", sz=20),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        place_text(bl, paradoxo)

        # Pergunta retórica: place_graphic para centralizar no painel
        pergunta = _T("Por quê?", sz=36, bold=True, color=theme.ACCENT)
        place_graphic(br, pergunta)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(intro),
                      FadeIn(bl),  FadeIn(paradoxo),
                      FadeIn(br),  FadeIn(pergunta))
        self.next_slide()
        self._fadeout()

    # ── Slide 03 — O mesmo problema acontece no Brasil ────────────────────────
    # Blocos: figura cpue_pantanal.pdf (não convertível) + lista 3 itens + nota CPUE
    # Decisão: substituir figura por painel de contexto metodológico
    # Layout: Grid1T2B
    #   · top           — contexto: o que é CPUE e por que é proxy de abundância
    #   · bl  (accent)  — dados observados (Pacu, Pintado, Dourado)
    #   · br            — nota sobre figura ausente + instrução para inserir
    def _slide_brasil(self):
        hdr = _hdr(self, "O mesmo problema acontece no Brasil",
                   "CPUE — Pantanal MS, 1994–2017 · SCPESCA/MS, Embrapa Pantanal")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100)               # 13.00 × 1.94 u
        bl  = g.panel(33, 100, 0,  50, accent=True)  #  6.33 × 4.11 u
        br  = g.panel(33, 100, 50, 100)              #  6.33 × 4.11 u

        ctx = VGroup(
            _T("CPUE (Captura Por Unidade de Esforço) é o proxy padrão", sz=26),
            _T("de abundância do estoque em pesqueiros monitorados.", sz=26),
        ).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        place_text(top, ctx)

        dados = VGroup(
            _T("O que os dados mostram:", sz=21, bold=True, color=theme.C_TEXT_H2),
            _T("Pacu: CPUE caiu de 14 para 2,5 kg/pescador", sz=20),
            _T("em 6 anos com esforço crescente.", sz=20),
            _T("Após restrição (2000): patamar inferior.", sz=20),
            _T("Pintado e dourado: declínio contínuo.", sz=20),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(bl, dados)

        # br: nota sobre gráfico original + padrão geral observado
        nota = VGroup(
            _T("Gráfico original:", sz=19, bold=True, color=theme.C_TEXT_H2),
            _T("cpue_pantanal.pdf — inserir via", sz=18, italic=True,
               color=theme.C_TEXT_ANNOT),
            _T("ImageMobject('cpue_pantanal.pdf')", sz=18, italic=True,
               color=theme.C_TEXT_ANNOT),
            _T("Padrão observado:", sz=19, bold=True, color=theme.C_TEXT_H2),
            _T("queda com esforço crescente,", sz=19),
            _T("sem recuperação após intervenção.", sz=19),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        place_text(br, nota)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(ctx),
                      FadeIn(bl),  FadeIn(dados),
                      FadeIn(br),  FadeIn(nota))
        self.next_slide()
        self._fadeout()

    # ── Slide 04 — Padrão comum: Bacalhau × Pantanal ─────────────────────────
    # Blocos: block[Padrão comum] + exampleblock[Bacalhau] + exampleblock[Pantanal]
    #         + alertblock[Pergunta Krebs] — 4 blocos → condensar
    # Decisão: alertblock condensado para 1 linha e incorporado ao topo
    # Layout: Grid1T2B
    #   · top (accent) — padrão comum (3 itens compactos) + pergunta de Krebs
    #   · bl           — Bacalhau Atlântico Norte
    #   · br           — Pescados Pantanal MS
    def _slide_padrao_comum(self):
        hdr = _hdr(self, "Bacalhau e Pantanal: o mesmo argumento",
                   "dois contextos, um padrão")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)  # 13.00 × 1.94 u
        bl  = g.panel(33, 100, 0,  50)               #  6.33 × 4.11 u
        br  = g.panel(33, 100, 50, 100)              #  6.33 × 4.11 u

        # TOP: 3 itens do padrão comum (sz=19, buff=0.18 para caber na h=1.34 usável)
        padrao = VGroup(
            _T("(1) Captura cai com esforço crescente.", sz=19),
            _T("(2) Dados contínuos não previram o declínio.", sz=19),
            _T("(3) Linguagem verbal não distingue recuperação de colapso.", sz=19),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        place_text(top, padrao)

        bacalhau = VGroup(
            _T("Bacalhau — Atlântico Norte:", sz=22, bold=True, color=theme.C_TEXT_H2),
            _T("500 anos de pesca contínua.", sz=22),
            _T("Colapso em 1989, moratória em 1992.", sz=22),
            _T("Não se recuperou em 30 anos.", sz=22),
        ).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        place_text(bl, bacalhau)

        pantanal = VGroup(
            _T("Pescados — Pantanal MS:", sz=22, bold=True, color=theme.C_TEXT_H2),
            _T("23 anos de dados (SCPESCA/MS).", sz=22),
            _T("Declínio detectado; restrições aplicadas.", sz=22),
            _T("Recuperação parcial e lenta.", sz=22),
        ).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        place_text(br, pantanal)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(padrao),
                      FadeIn(bl),  FadeIn(bacalhau),
                      FadeIn(br),  FadeIn(pantanal))
        self.next_slide()
        self._fadeout()

    # ── Slide 05 — O limite da intuição verbal ────────────────────────────────
    # Blocos: intro (1 linha) + enumerate (3 afirmações) + alertblock[Problema]
    # Layout: dois painéis full-width empilhados (top=50%, bot=50%)
    #   · top (accent) — intro + 3 afirmações verbais
    #   · bot          — alertblock[Problema]: limitações da linguagem verbal
    def _slide_intuicao_verbal(self):
        hdr = _hdr(self, "O limite da intuição verbal")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  50,  0, 100, accent=True)  # 13.00 × 3.03 u
        bot = g.panel(50, 100, 0, 100)               # 13.00 × 3.03 u

        afirmacoes = VGroup(
            _T("Considere estas afirmações — todas razoáveis, todas verbais:", sz=21),
            _T("1.  \"Se pescamos menos, o estoque se recupera.\"",
               sz=20, italic=True, color=theme.C_TEXT_H2),
            _T("2.  \"A população é resiliente — sempre se recuperou antes.\"",
               sz=20, italic=True, color=theme.C_TEXT_H2),
            _T("3.  \"O ambiente mudou; por isso não volta.\"",
               sz=20, italic=True, color=theme.C_TEXT_H2),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(top, afirmacoes)

        problema = VGroup(
            _T("Problema:", sz=21, bold=True, color=theme.C_TEXT_H2),
            _T("Todas as três podem ser verdadeiras. Ou falsas.", sz=21),
            _T("Ou verdadeiras sob certas condições e falsas sob outras.", sz=21),
            _T("A linguagem verbal não diz quando, por que, nem sob quais condições.", sz=21),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(bot, problema)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(afirmacoes),
                      FadeIn(bot), FadeIn(problema))
        self.next_slide()
        self._fadeout()

    # ── Slide 06 — Por que precisamos de ecologia? ────────────────────────────
    # Blocos: intro (2 frases contrastivas) + block[Observação] + exampleblock[Ecologia]
    # Layout: Grid1T2B
    #   · top (accent) — contraste "observação descreve vs ecologia explica"
    #   · bl           — block[Observação]: 3 exemplos de padrões observados
    #   · br           — exampleblock[Ecologia pergunta]: 3 perguntas mecanísticas
    def _slide_por_que_ecologia(self):
        hdr = _hdr(self, "Por que precisamos de ecologia?")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)
        bl  = g.panel(33, 100, 0,  50)
        br  = g.panel(33, 100, 50, 100)

        intro = VGroup(
            _T("Observação bruta descreve padrões.", sz=26),
            _T("Ecologia explica mecanismos.", sz=26, bold=True, color=theme.C_TEXT_H2),
        ).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        place_text(top, intro)

        obs = VGroup(
            _T("Observação:", sz=22, bold=True, color=theme.C_TEXT_H2),
            _T("Captura caiu 90% em 10 anos.", sz=22),
            _T("Estoque não volta após moratória.", sz=22),
            _T("Temperatura do oceano subiu.", sz=22),
        ).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        place_text(bl, obs)

        eco = VGroup(
            _T("Ecologia pergunta:", sz=22, bold=True, color=theme.C_TEXT_H2),
            _T("Quais interações causaram o colapso?", sz=22),
            _T("Existe um ponto sem retorno?", sz=22),
            _T("Como o ambiente altera a dinâmica?", sz=22),
        ).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        place_text(br, eco)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(intro),
                      FadeIn(bl),  FadeIn(obs),
                      FadeIn(br),  FadeIn(eco))
        self.next_slide()
        self._fadeout()

    # ── Slide 07 — Definição de Krebs ─────────────────────────────────────────
    # Blocos: ctx (2 linhas) + block[Definição Krebs] + exampleblock[Pergunta central]
    # Layout: Grid1T2B
    #   · top           — contexto: "definição como resposta, não ponto de partida"
    #   · bl  (accent)  — definição original de Krebs (1972)
    #   · br            — reformulação como pergunta operacional
    def _slide_definicao_krebs(self):
        hdr = _hdr(self, "Conclusão 1 — A pergunta que organiza tudo")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100)
        bl  = g.panel(33, 100, 0,  50, accent=True)
        br  = g.panel(33, 100, 50, 100)

        ctx = VGroup(
            _T("Chegamos a uma definição que não é ponto de partida — é resposta.", sz=24),
            _T("Krebs (1972); adotada por Begon, Townsend & Harper (2006).",
               sz=18, italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        place_text(top, ctx)

        definicao = VGroup(
            _T("Definição de Krebs (1972):", sz=20, bold=True, color=theme.C_TEXT_H2),
            _T("\"A ecologia é o estudo científico das", sz=20, italic=True),
            _T("interações que determinam", sz=20, italic=True),
            _T("a distribuição e a abundância", sz=20, italic=True),
            _T("dos organismos.\"", sz=20, italic=True),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(bl, definicao)

        pergunta = VGroup(
            _T("A pergunta central:", sz=20, bold=True, color=theme.C_TEXT_H2),
            _T("Quais interações determinam", sz=24, italic=True, color=theme.ACCENT),
            _T("onde os organismos ocorrem", sz=24, italic=True, color=theme.ACCENT),
            _T("e em que quantidade?", sz=24, italic=True, color=theme.ACCENT),
        ).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        place_text(br, pergunta)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(ctx),
                      FadeIn(bl),  FadeIn(definicao),
                      FadeIn(br),  FadeIn(pergunta))
        self.next_slide()
        self._fadeout()

    # ── Slide 08 — Três palavras que carregam todo o peso ─────────────────────
    # Blocos: itemize 3 itens (com subitens) + exampleblock[Implicação]
    # Layout: dois painéis 50/50 full-height
    #   · esq (accent) — 3 palavras-chave com definição (9 linhas, h=5.80 usável)
    #   · dir          — exampleblock[Implicação]: por que o objeto já é matemático
    def _slide_tres_palavras(self):
        hdr = _hdr(self, "Três palavras que carregam todo o peso",
                   "anatomia da definição de Krebs")

        g   = ContentGrid(shadow=True)
        esq = g.panel(0, 100, 0,  50, accent=True)  # 6.33 × 6.40 u
        dir = g.panel(0, 100, 50, 100)              # 6.33 × 6.40 u

        # esq: cada palavra em bold seguida de 2 linhas de definição
        palavras = VGroup(
            _T("Interações", sz=22, bold=True, color=theme.C_TEXT_H2),
            _T("relação de dependência entre variáveis", sz=20),
            _T("que mudam no tempo", sz=20),
            _T("Determinam", sz=22, bold=True, color=theme.C_TEXT_H2),
            _T("causalidade: não basta descrever,", sz=20),
            _T("é preciso explicar", sz=20),
            _T("Distribuição e abundância", sz=22, bold=True, color=theme.C_TEXT_H2),
            _T("grandezas mensuráveis:", sz=20),
            _T("o objeto já é quantitativo", sz=20),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        place_text(esq, palavras)

        impl = VGroup(
            _T("Implicação:", sz=21, bold=True, color=theme.C_TEXT_H2),
            _T("A ecologia não matematiza a biologia", sz=21),
            _T("por opção estética.", sz=21),
            _T("Seu objeto central —", sz=21),
            _T("abundância variável no tempo —", sz=21),
            _T("já é matemático.", sz=21, bold=True, color=theme.ACCENT),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        place_text(dir, impl)

        self.play_seq(FadeIn(hdr),
                      FadeIn(esq), FadeIn(palavras),
                      FadeIn(dir), FadeIn(impl))
        self.next_slide()
        self._fadeout()

    # ── Slide 09 — Por que precisamos de modelos? ─────────────────────────────
    # Blocos: intro + 2 requisitos + "esse objeto é o modelo" + alertblock[Questão]
    # Layout: dois painéis full-width empilhados
    #   · top (accent) — argumento completo: intro → requisitos → objeto
    #   · bot          — alertblock[Questão]: a provocação que leva ao próximo slide
    def _slide_por_que_modelos(self):
        hdr = _hdr(self, "Por que precisamos de modelos?")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  50,  0, 100, accent=True)
        bot = g.panel(50, 100, 0, 100)

        intro = VGroup(
            _T("A pergunta de Krebs exige mais do que observação qualitativa.", sz=20),
            _T("Precisamos de um objeto que:", sz=19, color=theme.C_TEXT_H2),
            _T("·  force precisão nas hipóteses", sz=18),
            _T("·  gere predições testáveis", sz=18),
            _T("Esse objeto é o modelo matemático.", sz=19, bold=True, color=theme.ACCENT),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        place_text(top, intro)

        questao = VGroup(
            _T("Questão:", sz=23, bold=True, color=theme.C_TEXT_H2),
            _T("Mas o que construir um modelo,", sz=23),
            _T("de fato, nos força a fazer?", sz=23),
        ).arrange(DOWN, buff=0.44, aligned_edge=LEFT)
        place_text(bot, questao)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(intro),
                      FadeIn(bot), FadeIn(questao))
        self.next_slide()
        self._fadeout()

    # ── Slide 10 — O que o modelo nos força a responder ──────────────────────
    # Bloco: itemize 4 itens com pergunta + seta + consequência (original sz pequeno)
    # Layout: Grid1T2B
    #   · top (accent) — contextualização: "cada pergunta é uma hipótese"
    #   · bot          — 4 pares pergunta→consequência (full-width, 8 linhas)
    def _slide_o_que_o_modelo_exige(self):
        hdr = _hdr(self, "O que o modelo nos força a responder")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)
        bot = g.panel(33, 100, 0, 100)

        ctx = _T("Cada pergunta abaixo é uma hipótese explícita sobre o mecanismo.", sz=20)
        place_graphic(top, ctx)

        # 4 pares: pergunta (bold, sz=18) + consequência (italic, sz=16, ANNOT/ACCENT)
        perguntas = VGroup(
            _T("A que taxa os indivíduos nascem e morrem?", sz=18, bold=True,
               color=theme.C_TEXT_H2),
            _T("→  A dinâmica é o mecanismo, não o padrão.", sz=16, italic=True,
               color=theme.C_TEXT_ANNOT),
            _T("Essa taxa depende do tamanho atual da população?", sz=18, bold=True,
               color=theme.C_TEXT_H2),
            _T("→  Dependência de densidade — existe um limite.", sz=16, italic=True,
               color=theme.C_TEXT_ANNOT),
            _T("Como a pesca altera essa taxa?", sz=18, bold=True,
               color=theme.C_TEXT_H2),
            _T("→  A intervenção entra como parâmetro.", sz=16, italic=True,
               color=theme.C_TEXT_ANNOT),
            _T("O sistema tem mais de um equilíbrio?", sz=18, bold=True,
               color=theme.C_TEXT_H2),
            _T("→  Pode haver um ponto sem retorno.", sz=16, italic=True,
               color=theme.ACCENT),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        place_text(bot, perguntas)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(ctx),
                      FadeIn(bot), FadeIn(perguntas))
        self.next_slide()
        self._fadeout()

    # ── Slide 11 — Conclusão 2: A linguagem necessária ────────────────────────
    # Blocos: intro (4 linhas) + equação dN/dt=f(N) + anotação + exampleblock[Conclusão]
    # Layout: Grid2T1B
    #   · tl          — intro textual
    #   · tr          — equação em destaque + anotação (place_graphic)
    #   · bot (accent) — exampleblock[Conclusão]: ecologia chega à matemática por necessidade
    def _slide_conclusao2(self):
        hdr = _hdr(self, "Conclusão 2 — A linguagem necessária")

        g   = ContentGrid(shadow=True)
        tl  = g.panel(0,  50,  0,  50)               # 6.33 × 3.03 u
        tr  = g.panel(0,  50, 50, 100)               # 6.33 × 3.03 u
        bot = g.panel(50, 100, 0, 100, accent=True)  # 13.00 × 3.03 u

        intro = VGroup(
            _T("Para responder à pergunta de Krebs,", sz=21),
            _T("precisamos representar como", sz=21),
            _T("quantidades mudam por interações.", sz=21),
            _T("O modelo mais simples possível:", sz=20, color=theme.C_TEXT_H2),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(tl, intro)

        # Equação display (place_graphic) + anotação como subitem
        eq_grupo = VGroup(
            MathTex(r"\frac{dN}{dt} = f(N)", font_size=48, color=theme.ACCENT),
            _T("taxa de mudança = função das interações",
               sz=15, italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.42)
        place_graphic(tr, eq_grupo)

        conclusao = VGroup(
            _T("Conclusão:", sz=24, bold=True, color=theme.C_TEXT_H2),
            _T("A linguagem que representa mudança por interação é o cálculo diferencial.", sz=22),
            _T("A ecologia chega à matemática não por abstração — mas por necessidade.", sz=22),
        ).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        place_text(bot, conclusao)

        self.play_seq(FadeIn(hdr),
                      FadeIn(tl),  FadeIn(intro),
                      FadeIn(tr),  FadeIn(eq_grupo),
                      FadeIn(bot), FadeIn(conclusao))
        self.next_slide()
        self._fadeout()

    # ── Slide 12 — Síntese: O fio condutor ───────────────────────────────────
    # Bloco: enumerate 5 itens (fio narrativo da aula inteira)
    # Layout: topo estreito (snap 25%) + base larga
    #   · top (accent) — chamada para o enumerate
    #   · bot          — 5 passos com itens intercalados conceito+contexto
    def _slide_sintese(self):
        hdr = _hdr(self, "Síntese — O fio condutor")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  25,  0, 100, accent=True)  # 13.00 × 1.43 u
        bot = g.panel(25, 100, 0, 100)               # 13.00 × 4.62 u

        ctx = _T("Cinco passos que constroem o argumento desta aula:", sz=19,
                 color=theme.C_TEXT_H1)
        place_graphic(top, ctx)

        # Os dois Conclusões destacados em ACCENT para evidenciar a estrutura narrativa
        fio = VGroup(
            _T("1.  Problema concreto", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("     colapso do bacalhau e dos pescados do Pantanal",
               sz=16, italic=True, color=theme.C_TEXT_ANNOT),
            _T("2.  Intuição verbal falha", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("     precisamos de mecanismo",
               sz=16, italic=True, color=theme.C_TEXT_ANNOT),
            _T("3.  Conclusão 1: a pergunta de Krebs",
               sz=18, bold=True, color=theme.ACCENT),
            _T("4.  Descrição qualitativa falha", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("     precisamos de modelo matemático",
               sz=16, italic=True, color=theme.C_TEXT_ANNOT),
            _T("5.  Conclusão 2: cálculo diferencial como linguagem",
               sz=18, bold=True, color=theme.ACCENT),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        place_text(bot, fio)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(ctx),
                      FadeIn(bot), FadeIn(fio))
        self.next_slide()
        self._fadeout()

    # ── Slide 13 — Próxima aula: Da pergunta ao primeiro modelo ───────────────
    # Blocos: intro (2 linhas) + equação logística + itemize N/r/K
    # Layout: Grid1T2B
    #   · top (accent) — contexto: "construímos o modelo mais simples que..."
    #   · bl           — equação logística em destaque (place_graphic, sz=44)
    #   · br           — significado de cada símbolo (cada um = uma hipótese)
    def _slide_proxima_aula(self):
        hdr = _hdr(self, "Próxima aula — Da pergunta ao primeiro modelo")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)
        bl  = g.panel(33, 100, 0,  50)
        br  = g.panel(33, 100, 50, 100)

        ctx = VGroup(
            _T("Com a linguagem estabelecida, construímos o modelo mais simples", sz=26),
            _T("que responde à pergunta de Krebs para uma única espécie.", sz=26),
        ).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        place_text(top, ctx)

        # Equação logística — modelo de Verhulst; place_graphic para centralizar
        eq = MathTex(
            r"\frac{dN}{dt} = rN\!\left(1 - \frac{N}{K}\right)",
            font_size=44, color=theme.ACCENT,
        )
        place_graphic(bl, eq)

        # br: cada símbolo = uma hipótese explícita (padrão rótulo + descrição)
        simbolos = VGroup(
            _T("Cada símbolo é uma hipótese:", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("N — abundância", sz=18),
            _T("     (o que Krebs quer explicar)", sz=16, italic=True,
               color=theme.C_TEXT_ANNOT),
            _T("r — taxa intrínseca de crescimento", sz=18),
            _T("     (interação indivíduo-recurso)", sz=16, italic=True,
               color=theme.C_TEXT_ANNOT),
            _T("K — capacidade de suporte", sz=18),
            _T("     (limite imposto pelo ambiente)", sz=16, italic=True,
               color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        place_text(br, simbolos)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(ctx),
                      FadeIn(bl),  FadeIn(eq),
                      FadeIn(br),  FadeIn(simbolos))
        self.next_slide()
        self._fadeout()
