"""
Introdução às Equações Diferenciais — Conversão Beamer → mathpres
Fonte: aula01_intro_edo.tex  (Equações Diferenciais Ordinárias, Aula 1)

Renderizar:
    manim-slides render aula01_intro_edo_manim.py AulaEDO
Apresentar:
    manim-slides present AulaEDO
"""

import sys, os

_MATHPRES = os.path.expanduser("~/.local/mathpres")
if not os.path.isdir(_MATHPRES):
    raise RuntimeError(
        "mathpres não encontrado em ~/.local/mathpres\n"
        "Clone com: git clone --depth=1 https://github.com/1moi6/manim-layouts.git ~/.local/mathpres"
    )
sys.path.insert(0, _MATHPRES)

from manim import *
from mathpres import AcademicBase, place_text, place_graphic, theme
from mathpres import ContentGrid, apply_tex_theme, set_theme
from mathpres.components import build_header_band, build_header_accent, build_header_content

set_theme("ocean_night")
apply_tex_theme()


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
    band = build_header_band()
    scene.add(band, build_header_accent())
    hdr = build_header_content(title, subtitle)
    hdr.move_to(band).align_to(band, LEFT).shift(RIGHT * 0.55)
    return hdr


class AulaEDO(AcademicBase):

    def construct(self):
        self.camera.background_color = ManimColor(theme.BG_MAIN)
        self._slide_capa()
        self._slide_cafe()
        self._slide_intuicao_a()
        self._slide_intuicao_b()
        self._slide_hip1()
        self._slide_hip2()
        self._slide_compare()
        self._slide_classificacao()
        self._slide_tabela()
        self._slide_solucao_a()
        self._slide_solucao_b()
        self._slide_pvi_a()
        self._slide_pvi_b()
        self._slide_qualitativa_a()
        self._slide_qualitativa_b()
        self._slide_multimodelo()
        self._slide_sintese_a()
        self._slide_sintese_b()
        self._slide_proxima()
        self._slide_exercicios()

    # ── Slide 01 — Capa ───────────────────────────────────────────────────────
    # Painel único accent full-screen. Animação progressiva idêntica ao exemplo
    # de referência (ecologia_modelagem_manim.py, _slide_capa).
    def _slide_capa(self):
        g    = ContentGrid(shadow=True)
        main = g.panel(0, 100, 0, 100, accent=True)
        self.add(main)

        titulo = Text(
            "Introdução às Equações Diferenciais",
            font_size=40, weight=BOLD, font=theme.FONT_SANS,
            gradient=(theme.C_TEXT_H1, theme.ACCENT),
        )
        titulo.move_to(ORIGIN)
        self.play(Write(titulo), run_time=0.8)
        self.wait(0.6)

        subtitulo = _T(
            "O que é uma EDO e por que ela aparece",
            sz=24, italic=True, color=theme.C_TEXT_H2,
        )
        g1 = VGroup(titulo.copy(), subtitulo).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        g1.move_to(ORIGIN)
        self.play(
            ReplacementTransform(titulo, g1[0]),
            FadeIn(subtitulo, shift=UP * 0.3),
            run_time=1.0,
        )
        self.wait(0.6)

        info = _T("Equações Diferenciais Ordinárias · Aula 1", sz=18, color=theme.C_TEXT_ANNOT)
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

    # ── Slide 02 — Uma pergunta simples ───────────────────────────────────────
    # Frame 2. Layout: Grid1T2B.
    # TOP accent: 2 linhas com a situação do café (sz=21, usable_h=1.34u → 0.66u ✓).
    # BL / BR: listas puras, 4 itens sz=20, buff=0.30 → h=1.78u < 3.51u ✓.
    # Pause: TOP aparece primeiro; BL+BR revelados após next_slide().
    def _slide_cafe(self):
        hdr = _hdr(self, "Uma pergunta simples", "sem equações")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)
        bl  = g.panel(33, 100,  0,  50)
        br  = g.panel(33, 100, 50, 100)
        vl  = g.v_line(50, r0=33)

        # TOP — 2 linhas sz=21; place_text (contém Text)
        situacao = VGroup(
            _T("Café a 90 °C — sala a 20 °C.", sz=21),
            _T("Quanto tempo até o café atingir 60 °C?",
               sz=21, italic=True, color=theme.C_TEXT_H2),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        place_text(top, situacao)

        # BL — 4 itens sz=20; place_text
        sabe = VGroup(
            _T("O que você sabe:", sz=20, bold=True, color=theme.C_TEXT_H2),
            _T("O café começa quente e esfria.", sz=20),
            _T("Mais diferença → esfria mais rápido.", sz=20),
            _T("Eventualmente atinge a temp. da sala.", sz=20),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(bl, sabe)

        # BR — 4 itens sz=20; place_text
        nsabe = VGroup(
            _T("O que você não sabe:", sz=20, bold=True, color=theme.C_TEXT_H2),
            _T("Em que instante exatamente?", sz=20),
            _T("A que taxa o resfriamento ocorre?", sz=20),
            _T("Como calcular isso?", sz=20),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(br, nsabe)

        self.play_seq(FadeIn(hdr), FadeIn(top), FadeIn(situacao))
        self.next_slide()
        self.play(FadeIn(bl), FadeIn(sabe), FadeIn(br), FadeIn(nsabe))
        self.next_slide()
        self._fadeout()

    # ── Slide 03 — A linguagem verbal já contém a ideia ───────────────────────
    # Frame 3, parte 1. Layout: dois painéis full-width empilhados (50 / 50).
    # TOP accent: 2 linhas de intro sz=21 → 0.66u < 2.43u ✓.
    # BOT: frase-chave como VGroup de 2 Text sz=26 italic → place_text (contém Text).
    def _slide_intuicao_a(self):
        hdr = _hdr(self, "O que a intuição já diz")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  50, 0, 100, accent=True)
        bot = g.panel(50, 100, 0, 100)

        intro = VGroup(
            _T("Seja T(t) a temperatura do café no instante t (minutos).", sz=21),
            _T("A linguagem verbal já contém a ideia-chave:", sz=21),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(top, intro)

        # Frase-chave — VGroup de Text → place_text (não place_graphic)
        frase = VGroup(
            _T('"quanto maior a diferença,', sz=26, italic=True, color=theme.ACCENT),
            _T(' mais rápido esfria"',       sz=26, italic=True, color=theme.ACCENT),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        place_text(bot, frase)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(intro),
                      FadeIn(bot), FadeIn(frase))
        self.next_slide()
        self._fadeout()

    # ── Slide 04 — Da intuição à equação ──────────────────────────────────────
    # Frame 3, parte 2. Layout: Grid1T2B.
    # TOP: contexto textual, 1 linha sz=20 (place_text).
    # BL accent: Padrão A — label sz=18 bold + MathTex sz=36 + anotação sz=16 italic.
    #            Fração sz=36 em painel 4.11u ✓ (limite é TOP-33; aqui é BL-67).
    # BR: pergunta em 2 linhas sz=20 (place_text).
    def _slide_intuicao_b(self):
        hdr = _hdr(self, "Da intuição à equação")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100)
        bl  = g.panel(33, 100,  0, 50, accent=True)
        br  = g.panel(33, 100, 50, 100)
        vl  = g.v_line(50, r0=33)

        ctx = VGroup(
            _T("A intuição é uma afirmação sobre a taxa de variação de T:", sz=20),
        )
        place_text(top, ctx)

        # BL — Padrão A: sz=18 bold / MathTex sz=36 / sz=16 italic
        afirmacao = VGroup(
            _T("Afirmação sobre dT/dt:", sz=18, bold=True, color=theme.C_TEXT_H2),
            MathTex(
                r"\frac{dT}{dt} \;\text{depende de}\; T(t) - T_m",
                font_size=36, color=theme.C_TEXT_BODY,
            ),
            _T("onde T_m = 20 °C é a temperatura do meio.", sz=16,
               italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        place_text(bl, afirmacao)

        pergunta = VGroup(
            _T("Qual é exatamente essa dependência?", sz=20),
            _T("Como transformar a intuição em equação?",
               sz=20, italic=True, color=theme.C_TEXT_H2),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(br, pergunta)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(ctx),
                      FadeIn(bl),  FadeIn(afirmacao),
                      FadeIn(br),  FadeIn(pergunta))
        self.next_slide()
        self._fadeout()

    # ── Slide 05 — Hipótese 1: Temperatura uniforme ───────────────────────────
    # Frame 4. Layout: Grid1T2B, 1 pause.
    # TOP accent: 2 linhas sz=20, buff=0.18 → 0.62u < 1.34u ✓.
    # BL (após pause): lista pura 4 itens sz=20, buff=0.32 → 1.84u < 3.51u ✓.
    # BR (após pause): equação dT/dt isolada → place_graphic (único MathTex). ✓
    #   label= no painel evita título duplicado.
    def _slide_hip1(self):
        hdr = _hdr(self, "Hipótese 1", "Temperatura uniforme")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True,
                      label="Hipótese 1 — Temperatura uniforme")
        bl  = g.panel(33, 100,  0,  50)
        br  = g.panel(33, 100, 50, 100, label="Consequência matemática")
        vl  = g.v_line(50, r0=33)

        # TOP — 2 linhas sz=20 + anotação sz=18; place_text
        hip = VGroup(
            _T("O café tem uma única temperatura em cada instante t:", sz=20),
            _T("a função T(t) está bem definida.", sz=20),
            _T("Custo: ignoramos gradientes internos e a xícara.", sz=18,
               italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        place_text(top, hip)

        # BL — lista pura sz=20; place_text
        ganho = VGroup(
            _T("Ganho: T depende de uma só variável — t.", sz=20,
               bold=True, color=theme.C_TEXT_H2),
            _T("Quando é razoável:", sz=20, bold=True, color=theme.C_TEXT_H2),
            _T("xícara pequena, líquido bem misturado.", sz=20),
            _T("(Não vale para fornos ou para o oceano.)", sz=18,
               italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        place_text(bl, ganho)

        # BR — único MathTex centralizado → place_graphic ✓
        eq = MathTex(r"\dfrac{dT}{dt}", font_size=52, color=theme.ACCENT)
        place_graphic(br, eq)

        self.play_seq(FadeIn(hdr), FadeIn(top), FadeIn(hip))
        self.next_slide()
        self.play(FadeIn(bl), FadeIn(ganho), FadeIn(br), FadeIn(eq))
        self.next_slide()
        self._fadeout()

    # ── Slide 06 — Hipótese 2: Lei de Newton do Resfriamento ─────────────────
    # Frame 5. Layout: Grid1T2B, 2 pauses.
    # TOP accent: 2 linhas sz=20 + anotação sz=18 → 0.82u < 1.34u ✓.
    # BL (após 1° pause): único MathTex → place_graphic ✓.
    # BR (após 2° pause): 4 itens sz=20, buff=0.34 → 1.90u < 3.51u ✓.
    def _slide_hip2(self):
        hdr = _hdr(self, "Hipótese 2", "Lei de Newton do Resfriamento")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True,
                      label="Hipótese 2 — Proporcionalidade")
        bl  = g.panel(33, 100,  0,  50, label="Tradução imediata")
        br  = g.panel(33, 100, 50, 100)
        vl  = g.v_line(50, r0=33)

        hip = VGroup(
            _T("A taxa de variação de T é proporcional à diferença T(t) - Tm.", sz=20),
            _T("Custo: falha para grandes diferenças ou se Tm variar.", sz=18,
               italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        place_text(top, hip)

        # BL — único MathTex → place_graphic ✓
        eq = MathTex(
            r"\frac{dT}{dt} = k\bigl(T(t) - T_m\bigr), \qquad k < 0",
            font_size=36, color=theme.ACCENT,
        )
        place_graphic(bl, eq)

        # BR — lista pura sz=20; place_text
        emergiu = VGroup(
            _T("A equação emergiu — não foi postulada.", sz=20,
               bold=True, color=theme.C_TEXT_H2),
            _T("T(t): Hipótese 1 — temperatura bem definida.", sz=20),
            _T("k: Hipótese 2 — proporcionalidade; k < 0.", sz=20),
            _T("Tm: temperatura do meio, considerada constante.", sz=20),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        place_text(br, emergiu)

        self.play_seq(FadeIn(hdr), FadeIn(top), FadeIn(hip))
        self.next_slide()
        self.play(FadeIn(bl), FadeIn(eq))
        self.next_slide()
        self.play(FadeIn(br), FadeIn(emergiu))
        self.next_slide()
        self._fadeout()

    # ── Slide 07 — Compare: dois tipos de equação ─────────────────────────────
    # Frame 6. Layout: Grid2T1B, 1 pause.
    # TL: Padrão A — label sz=18 bold + MathTex sz=36 + 2 linhas sz=18.
    # TR accent: Padrão A — MathTex sz=32 (fração) + 2 linhas sz=18.
    #            sz=32 em painel TL/TR usable_h=2.43u ✓ (fração ≈0.55u).
    # BOT (após pause): 2 linhas sz=20, place_text.
    def _slide_compare(self):
        hdr = _hdr(self, "Compare: dois tipos de equação")

        g   = ContentGrid(shadow=True)
        tl  = g.panel(0,  50,  0,  50)
        tr  = g.panel(0,  50, 50, 100, accent=True)
        bot = g.panel(50, 100, 0, 100)
        vl  = g.v_line(50, r1=50)
        hl  = g.h_line(50)

        # TL — Padrão A; place_text
        alg = VGroup(
            _T("Equação algébrica:", sz=18, bold=True, color=theme.C_TEXT_H2),
            MathTex(r"x^2 + 5x + 4 = 0", font_size=36, color=theme.C_TEXT_BODY),
            _T("Incógnita: número x.", sz=18),
            _T("Solução: x = -1 ou x = -4.", sz=18),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        place_text(tl, alg)

        # TR — Padrão A; place_text
        # fração sz=32 ≈ 0.55u; total ≈ 0.20+0.35+0.55+0.35+0.20+0.35+0.20 = 2.20u < 2.43u ✓
        dif = VGroup(
            _T("Equação diferencial:", sz=18, bold=True, color=theme.C_TEXT_H2),
            MathTex(r"\frac{dT}{dt} = k(T - T_m)", font_size=32,
                    color=theme.C_TEXT_BODY),
            _T("Incógnita: uma função T(t).", sz=18),
            _T("Solução: função que satisfaz a relação.", sz=18),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        place_text(tr, dif)

        # BOT — Padrão C; place_text
        concl = VGroup(
            _T("Uma equação diferencial envolve uma função desconhecida e suas derivadas.", sz=20),
            _T("A incógnita é uma função — não um número.", sz=20),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        place_text(bot, concl)

        self.play_seq(FadeIn(hdr),
                      FadeIn(tl), FadeIn(alg),
                      FadeIn(tr), FadeIn(dif))
        self.next_slide()
        self.play(FadeIn(bot), FadeIn(concl))
        self.next_slide()
        self._fadeout()

    # ── Slide 08 — Classificação da EDO ───────────────────────────────────────
    # Frame 7. Layout: dois painéis full-width (50 / 50).
    # TOP accent: Padrão A — label sz=18 bold + MathTex sz=28 (máx para fração em
    #             painel que aqui tem usable_h=2.43u; regra top-33 não se aplica).
    #             Fração sz=28 ≈0.48u; total ≈1.26u < 2.43u ✓.
    # BOT: 3 linhas classificação sz=20; place_text.
    def _slide_classificacao(self):
        hdr = _hdr(self, "Classificação", "vocabulário para descrever EDOs")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  50, 0, 100, accent=True)
        bot = g.panel(50, 100, 0, 100)
        hl  = g.h_line(50)

        # TOP — Padrão A; place_text
        ref = VGroup(
            _T("Equação de referência:", sz=18, bold=True, color=theme.C_TEXT_H2),
            MathTex(r"\frac{dT}{dt} = k(T - T_m)", font_size=28,
                    color=theme.C_TEXT_BODY),
            _T("derivada de T em relação à variável t.", sz=16,
               italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        place_text(top, ref)

        # BOT — 3 linhas sz=20; place_text
        classif = VGroup(
            _T("Tipo: derivada em relação a t (uma variável) → EDO ordinária.", sz=20),
            _T("Ordem: maior derivada = dT/dt (1ª derivada) → Ordem 1.", sz=20),
            _T("Linearidade: T e T' ao 1° grau, coefs. em t → Linear.", sz=20),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(bot, classif)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(ref),
                      FadeIn(bot), FadeIn(classif))
        self.next_slide()
        self._fadeout()

    # ── Slide 09 — Tabela de classificação ────────────────────────────────────
    # Frame 8. Layout: dois painéis full-width (50 / 50), 1 pause.
    # TOP: 4 linhas de tabela — cada linha é VGroup(MathTex, Text).arrange(RIGHT).
    #      sz=26 MathTex + sz=16 Text; buff_down=0.26; h≈2.32u < 2.43u ✓.
    # BOT accent (após pause): 3 linhas sz=20; place_text.
    def _slide_tabela(self):
        hdr = _hdr(self, "Mais exemplos de classificação")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  50, 0, 100)
        bot = g.panel(50, 100, 0, 100, accent=True, label="Regra para linearidade")
        hl  = g.h_line(50)

        def _linha(eq_str, classif, linear=True):
            cor = theme.C_TEXT_BODY if linear else theme.C_TEXT_ANNOT
            return VGroup(
                MathTex(eq_str, font_size=26, color=theme.C_TEXT_BODY),
                _T(classif, sz=16, color=cor),
            ).arrange(RIGHT, buff=0.55, aligned_edge=DOWN)

        tabela = VGroup(
            _linha(r"\dfrac{dT}{dt} = k(T - T_m)",
                   "ordem 1 · linear"),
            _linha(r"\dfrac{d^2y}{dx^2} - 2\dfrac{dy}{dx} + y = 0",
                   "ordem 2 · linear"),
            _linha(r"\dfrac{dy}{dx} = x\,y^{1/2}",
                   "ordem 1 · não-linear", linear=False),
            _linha(r"\dfrac{d^2y}{dx^2} + 5\!\left(\dfrac{dy}{dx}\right)^{3} - 4y = e^x",
                   "ordem 2 · não-linear", linear=False),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        place_text(top, tabela)

        # BOT — label= já diz "Regra para linearidade"; sem título duplicado
        regra = VGroup(
            _T("EDO de ordem n é linear se:", sz=20),
            _T("y, y', ..., y⁽ⁿ⁾ aparecem ao 1° grau", sz=20),
            _T("e os coeficientes dependem só da variável independente.", sz=20),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        place_text(bot, regra)

        self.play_seq(FadeIn(hdr), FadeIn(top), FadeIn(tabela))
        self.next_slide()
        self.play(FadeIn(bot), FadeIn(regra))
        self.next_slide()
        self._fadeout()

    # ── Slide 10 — O que é uma solução? ───────────────────────────────────────
    # Frame 9, parte 1. Layout: Grid1T2B.
    # TOP accent: único MathTex sem fração em painel top-33 → place_graphic ✓.
    #             sz=28 (máx para top-33 com fração, mas dT/dt=k(T-20) TEM fração)
    #             → usar sz=26 para garantir (fração ≈0.42u < 1.34u ✓).
    # BL: Padrão A — label + 2 MathTex + anotação; place_text.
    # BR: label= no painel; 3 linhas sz=20; place_text.
    def _slide_solucao_a(self):
        hdr = _hdr(self, "O que é uma solução?", "De volta ao café")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)
        bl  = g.panel(33, 100,  0,  50)
        br  = g.panel(33, 100, 50, 100, label="Definição — Solução")
        vl  = g.v_line(50, r0=33)

        # TOP — único MathTex → place_graphic ✓ (sz=26 respeita limite top-33)
        eq_ref = MathTex(r"\frac{dT}{dt} = k(T - 20)", font_size=26,
                         color=theme.C_TEXT_BODY)
        place_graphic(top, eq_ref)

        # BL — Padrão A: label+MathTex+label+MathTex+anotação; place_text
        # Altura: 0.20+0.35+0.55+0.35+0.20+0.35+0.42+0.35+0.18 = 2.95u < 3.51u ✓
        verif = VGroup(
            _T("Afirmação: T(t) = 20 + 70 e^{kt} satisfaz.", sz=18,
               bold=True, color=theme.C_TEXT_H2),
            _T("Verificação:", sz=18, bold=True, color=theme.C_TEXT_H2),
            MathTex(r"\frac{dT}{dt} = 70k\,e^{kt}", font_size=32,
                    color=theme.C_TEXT_BODY),
            MathTex(r"k(T-20) = 70k\,e^{kt} \quad \checkmark", font_size=32,
                    color=theme.C_TEXT_BODY),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(bl, verif)

        # BR — label= no painel; 4 linhas sz=20; place_text
        defin = VGroup(
            _T("Função φ(t) é solução da EDO se,", sz=20),
            _T("ao substituir na equação, ela se torna", sz=20),
            _T("uma identidade no intervalo I.", sz=20),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(br, defin)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(eq_ref),
                      FadeIn(bl),  FadeIn(verif),
                      FadeIn(br),  FadeIn(defin))
        self.next_slide()
        self._fadeout()

    # ── Slide 11 — Família de soluções ────────────────────────────────────────
    # Frame 9, parte 2. Layout: dois painéis full-width (50 / 50).
    # TOP: Padrão C — 2 linhas sz=20 + MathTex sz=40 (sem fração → inline ≈0.40u)
    #      Total ≈1.48u < 2.43u ✓; place_text (contém Text).
    # BOT accent: 3 linhas sz=20; place_text.
    def _slide_solucao_b(self):
        hdr = _hdr(self, "Família de soluções")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  50, 0, 100)
        bot = g.panel(50, 100, 0, 100, accent=True)
        hl  = g.h_line(50)

        # TOP — Padrão C + MathTex inline; place_text
        familia = VGroup(
            _T("T(t) = 20 + Ce^{kt} é solução para qualquer constante C.", sz=20),
            _T("Isso é a família de soluções — a solução geral.", sz=20,
               italic=True, color=theme.C_TEXT_H2),
            MathTex(r"T(t) = 20 + C\,e^{kt}", font_size=40, color=theme.ACCENT),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(top, familia)

        # BOT — 3 linhas sz=20; place_text
        concl = VGroup(
            _T("A solução geral tem uma constante arbitrária C.", sz=20),
            _T("Ela representa infinitas soluções particulares.", sz=20),
            _T("Para selecionar uma, precisamos de condição inicial.", sz=20),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(bot, concl)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(familia),
                      FadeIn(bot), FadeIn(concl))
        self.next_slide()
        self._fadeout()

    # ── Slide 12 — Problema de Valor Inicial ──────────────────────────────────
    # Frame 10, parte 1. Layout: Grid1T2B, 2 pauses.
    # TOP accent: MathTex com fração sz=26 → place_graphic ✓ (sz≤28, top-33).
    # BL (após 1° pause): Padrão A — label + MathTex sem fração sz=32; place_text.
    # BR (após 2° pause): único MathTex sem fração sz=40 → place_graphic ✓.
    #   label= no painel evita título duplicado.
    def _slide_pvi_a(self):
        hdr = _hdr(self, "Problema de Valor Inicial (PVI)")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)
        bl  = g.panel(33, 100,  0,  50)
        br  = g.panel(33, 100, 50, 100, label="Solução particular")
        vl  = g.v_line(50, r0=33)

        # TOP — fração sz=26 ≤ 28 ✓; place_graphic (único MathTex)
        pvi = MathTex(
            r"\frac{dT}{dt} = k(T - 20), \qquad T(0) = 90",
            font_size=26, color=theme.ACCENT,
        )
        place_graphic(top, pvi)

        # BL — Padrão A; place_text
        resolucao = VGroup(
            _T("O café começa a 90 °C em t = 0.", sz=18,
               bold=True, color=theme.C_TEXT_H2),
            _T("Aplicando a condição inicial:", sz=18,
               bold=True, color=theme.C_TEXT_H2),
            MathTex(r"T(0) = 20 + C = 90 \;\Rightarrow\; C = 70",
                    font_size=32, color=theme.C_TEXT_BODY),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        place_text(bl, resolucao)

        # BR — único MathTex sem fração → place_graphic ✓
        particular = MathTex(r"T(t) = 20 + 70\,e^{kt}",
                             font_size=40, color=theme.ACCENT)
        place_graphic(br, particular)

        self.play_seq(FadeIn(hdr), FadeIn(top), FadeIn(pvi))
        self.next_slide()
        self.play(FadeIn(bl), FadeIn(resolucao))
        self.next_slide()
        self.play(FadeIn(br), FadeIn(particular))
        self.next_slide()
        self._fadeout()

    # ── Slide 13 — Definição de PVI ───────────────────────────────────────────
    # Frame 10, parte 2. Layout: dois painéis full-width (50 / 50).
    # TOP accent: label= já identifica o painel; 3 linhas sz=20; place_text.
    # BOT: 2 linhas de conexão com o café; place_text.
    def _slide_pvi_b(self):
        hdr = _hdr(self, "Definição — PVI")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  50, 0, 100, accent=True, label="Problema de Valor Inicial")
        bot = g.panel(50, 100, 0, 100)
        hl  = g.h_line(50)

        defin = VGroup(
            _T("EDO acompanhada de condições sobre a função", sz=20),
            _T("(e suas derivadas) em um único ponto t₀.", sz=20),
            _T("Resolver o PVI é encontrar a solução particular.", sz=20,
               italic=True, color=theme.C_TEXT_H2),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(top, defin)

        aplicacao = VGroup(
            _T("No café: a condição T(0) = 90 fixou C = 70,", sz=20),
            _T("selecionando T(t) = 20 + 70 e^{kt} da família.", sz=20),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(bot, aplicacao)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(defin),
                      FadeIn(bot), FadeIn(aplicacao))
        self.next_slide()
        self._fadeout()

    # ── Slide 14 — Análise qualitativa: análise de sinal ──────────────────────
    # Frame 11, parte 1. Layout: Grid1T2B.
    # TOP accent: fração sz=26 ≤ 28 ✓ → place_graphic (único MathTex).
    # BL / BR: Padrão A — label sz=18 bold + MathTex sz=30 + texto sz=18; place_text.
    #          Fração sz=30 ≈0.47u; total ≈1.57u < 3.51u ✓.
    def _slide_qualitativa_a(self):
        hdr = _hdr(self, "O que a equação já diz", "sem resolver")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)
        bl  = g.panel(33, 100,  0,  50)
        br  = g.panel(33, 100, 50, 100)
        vl  = g.v_line(50, r0=33)

        # TOP — fração sz=26 ✓; place_graphic
        eq = MathTex(r"\frac{dT}{dt} = k(T - 20), \quad k < 0",
                     font_size=26, color=theme.ACCENT)
        place_graphic(top, eq)

        # BL — Padrão A; place_text
        caso_q = VGroup(
            _T("Se T > 20:", sz=18, bold=True, color=theme.C_TEXT_H2),
            MathTex(r"T-20>0,\; k<0 \;\Rightarrow\; \frac{dT}{dt} < 0",
                    font_size=30, color=theme.C_TEXT_BODY),
            _T("O café esfria. ✓", sz=18, italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        place_text(bl, caso_q)

        # BR — Padrão A; place_text
        caso_f = VGroup(
            _T("Se T < 20:", sz=18, bold=True, color=theme.C_TEXT_H2),
            MathTex(r"T-20<0,\; k<0 \;\Rightarrow\; \frac{dT}{dt} > 0",
                    font_size=30, color=theme.C_TEXT_BODY),
            _T("Um objeto frio aquece. ✓", sz=18, italic=True,
               color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        place_text(br, caso_f)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(eq),
                      FadeIn(bl),  FadeIn(caso_q),
                      FadeIn(br),  FadeIn(caso_f))
        self.next_slide()
        self._fadeout()

    # ── Slide 15 — Equilíbrio e três abordagens ───────────────────────────────
    # Frame 11, parte 2. Layout: Grid2T1B, 1 pause.
    # TL accent: Padrão A — MathTex sz=32 + 2 linhas sz=18; place_text.
    #            Fração sz=32 ≈0.55u; total ≈1.11u < 2.43u ✓.
    # TR: 2 linhas sz=20; place_text.
    # BOT (após pause): 4 linhas sz=20; place_text. h=4×0.22+3×0.28=1.72u < 2.43u ✓.
    def _slide_qualitativa_b(self):
        hdr = _hdr(self, "Equilíbrio e abordagens do curso")

        g   = ContentGrid(shadow=True)
        tl  = g.panel(0,  50,  0,  50, accent=True, label="Equilíbrio")
        tr  = g.panel(0,  50, 50, 100)
        bot = g.panel(50, 100, 0, 100)
        vl  = g.v_line(50, r1=50)
        hl  = g.h_line(50)

        # TL — Padrão A; place_text
        equil = VGroup(
            MathTex(r"\frac{dT}{dt} = 0 \;\Leftrightarrow\; T = 20",
                    font_size=32, color=theme.ACCENT),
            _T("A solução constante T(t) = 20 é a", sz=18),
            _T("solução de equilíbrio.", sz=18, italic=True,
               color=theme.C_TEXT_H2),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(tl, equil)

        # TR — Padrão C; place_text
        qual = VGroup(
            _T("Análise qualitativa: extraímos", sz=20),
            _T("informação sem resolver a EDO.", sz=20),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        place_text(tr, qual)

        # BOT — 4 linhas sz=20; place_text
        abord = VGroup(
            _T("Três abordagens do curso:", sz=20,
               bold=True, color=theme.C_TEXT_H2),
            _T("Analítica — resolver explicitamente.", sz=20),
            _T("Qualitativa — análise de sinal, campo de direções.", sz=20),
            _T("Numérica — aproximar a solução.", sz=20),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(bot, abord)

        self.play_seq(FadeIn(hdr),
                      FadeIn(tl), FadeIn(equil),
                      FadeIn(tr), FadeIn(qual))
        self.next_slide()
        self.play(FadeIn(bot), FadeIn(abord))
        self.next_slide()
        self._fadeout()

    # ── Slide 16 — Uma equação, muitos fenômenos ──────────────────────────────
    # Frame 12. Layout livre: TOP (0→33, accent) + 3 colunas iguais (33→100).
    # TOP accent: 2 linhas sz=20 (conclusão no topo, antes dos exemplos) → 0.66u < 1.34u ✓.
    #             Sem MathTex no TOP — equação dy/dt=ky fica nas colunas via label.
    # 3 colunas estreitas (33% de largura, usable_w=3.52u):
    #   5 itens sz=18, buff=0.22 → h=1.94u < 3.51u ✓.
    #   Máx chars/linha a sz=18: 30. Todas as linhas ≤ 20 chars ✓.
    def _slide_multimodelo(self):
        hdr = _hdr(self, "Uma equação, muitos fenômenos")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)
        c1  = g.panel(33, 100,  0,  33, label="dy/dt = ky  (k > 0)")
        c2  = g.panel(33, 100, 33,  67, label="dy/dt = ky  (k < 0)")
        c3  = g.panel(33, 100, 67, 100, label="dy/dt = ky  (k = r)")
        vl1 = g.v_line(33, r0=33)
        vl2 = g.v_line(67, r0=33)

        # TOP — 2 linhas sz=20; place_text
        msg = VGroup(
            _T("Uma única EDO, três fenômenos diferentes.", sz=20),
            _T("O que muda é a interpretação dos símbolos.", sz=20,
               italic=True, color=theme.C_TEXT_H2),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        place_text(top, msg)

        # C1 — 5 itens sz=18; place_text
        pop = VGroup(
            _T("Crescimento", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("populacional", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("y = P(t): população", sz=18),
            _T("k > 0: crescimento", sz=18),
            _T("(Malthus, 1798)", sz=16, italic=True,
               color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        place_text(c1, pop)

        # C2 — 5 itens sz=18; place_text
        rad = VGroup(
            _T("Decaimento", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("radioativo", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("y = A(t): massa", sz=18),
            _T("k < 0: decaimento", sz=18),
            _T("(datação C-14)", sz=16, italic=True,
               color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        place_text(c2, rad)

        # C3 — 5 itens sz=18; place_text
        jur = VGroup(
            _T("Juros", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("compostos", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("y = S(t): capital", sz=18),
            _T("k = r > 0: taxa", sz=18),
            _T("(capitalização)", sz=16, italic=True,
               color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        place_text(c3, jur)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(msg),
                      FadeIn(c1),  FadeIn(pop),
                      FadeIn(c2),  FadeIn(rad),
                      FadeIn(c3),  FadeIn(jur))
        self.next_slide()
        self._fadeout()

    # ── Slide 17 — Síntese: os 6 passos ──────────────────────────────────────
    # Frame 13, parte 1. Layout F2: TOP (0→33 accent) + BOT (33→100) full-width.
    # TOP: 1 linha sz=20 → 0.22u < 1.34u ✓.
    # BOT: 6 passos numerados. Cada passo = VGroup(num, texto).arrange(RIGHT).
    #      Outer: sz=19, buff=0.25 → h=6×0.224+5×0.25=2.60u < 3.51u ✓ (74%).
    def _slide_sintese_a(self):
        hdr = _hdr(self, "Síntese", "Como chegamos até aqui")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33, 0, 100, accent=True)
        bot = g.panel(33, 100, 0, 100)
        hl  = g.h_line(33)

        ctx = VGroup(
            _T("A EDO dT/dt = k(T - Tm) emergiu de um raciocínio em etapas:", sz=20),
        )
        place_text(top, ctx)

        NB = 0.50   # buff entre número e texto
        SB = 0.25   # buff entre passos

        def _passo(num, texto):
            return VGroup(
                _T(num,   sz=24, bold=True, color=theme.ACCENT),
                _T(texto, sz=19),
            ).arrange(RIGHT, buff=NB, aligned_edge=DOWN)

        passos = VGroup(
            _passo("01", "Problema concreto: resfriamento do café."),
            _passo("02", "Hipótese 1: temperatura uniforme — T(t) bem definida."),
            _passo("03", "Hipótese 2: proporcionalidade — a EDO emergiu."),
            _passo("04", "Solução = função que satisfaz a equação identicamente."),
            _passo("05", "PVI seleciona a solução particular da família."),
            _passo("06", "Análise qualitativa extrai info antes de resolver."),
        ).arrange(DOWN, buff=SB, aligned_edge=LEFT)
        place_text(bot, passos)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(ctx),
                      FadeIn(bot), FadeIn(passos))
        self.next_slide()
        self._fadeout()

    # ── Slide 18 — Vocabulário e abordagens ───────────────────────────────────
    # Frame 13, parte 2. Layout: Grid1T2B.
    # TOP accent: 1 linha sz=20 → 0.22u < 1.34u ✓.
    # BL (label="Vocabulário"): 4 itens sz=20, buff=0.48 → 1.32u < 3.51u ✓.
    # BR (label="Três abordagens"): 6 itens sz=18 (pares bold+body), buff=0.30
    #    → 6×0.20+5×0.30=2.70u < 3.51u ✓.
    def _slide_sintese_b(self):
        hdr = _hdr(self, "Vocabulário e abordagens")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  33,  0, 100, accent=True)
        bl  = g.panel(33, 100,  0,  50, label="Vocabulário da aula")
        br  = g.panel(33, 100, 50, 100, label="Três abordagens do curso")
        vl  = g.v_line(50, r0=33)

        intro = VGroup(
            _T("Conceitos e ferramentas apresentados nesta aula:", sz=20),
        )
        place_text(top, intro)

        # BL — 4 itens sz=20; label= já nomeia o painel; sem título duplicado
        vocab = VGroup(
            _T("EDO / EDP, ordem, linearidade", sz=20),
            _T("Solução geral, solução particular", sz=20),
            _T("Problema de valor inicial (PVI)", sz=20),
            _T("Solução de equilíbrio", sz=20),
        ).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        place_text(bl, vocab)

        # BR — 6 itens sz=18 (pares bold + corpo); place_text
        abord = VGroup(
            _T("Analítica",   sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("Resolver explicitamente.", sz=18),
            _T("Qualitativa", sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("Análise de sinal, campo de direções.", sz=18),
            _T("Numérica",    sz=18, bold=True, color=theme.C_TEXT_H2),
            _T("Aproximar a solução.", sz=18),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(br, abord)

        self.play_seq(FadeIn(hdr),
                      FadeIn(top), FadeIn(intro),
                      FadeIn(bl),  FadeIn(vocab),
                      FadeIn(br),  FadeIn(abord))
        self.next_slide()
        self._fadeout()

    # ── Slide 19 — Próxima aula ───────────────────────────────────────────────
    # Frame 14. Layout: dois painéis full-width (50 / 50), 1 pause.
    # TOP: 2 linhas sz=20; place_text.
    # BOT accent (após pause): Padrão A — texto sz=18 + MathTex sz=36 + 2 linhas;
    #   place_text (contém Text + MathTex).
    #   Fração sz=36 ≈0.62u; total ≈2.16u < 2.43u ✓.
    def _slide_proxima(self):
        hdr = _hdr(self, "Próxima aula", "Equações Separáveis")

        g   = ContentGrid(shadow=True)
        top = g.panel(0,  50, 0, 100)
        bot = g.panel(50, 100, 0, 100, accent=True, label="Pergunta em aberto")
        hl  = g.h_line(50)

        ctx = VGroup(
            _T("Temos T(t) = 20 + 70 e^{kt}, mas ainda não sabemos k.", sz=20),
            _T("Para determiná-lo, precisamos resolver a EDO sistematicamente.", sz=20),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        place_text(top, ctx)

        # BOT — Padrão A + linhas extras; place_text
        pergunta = VGroup(
            _T("A equação pode ser reescrita como:", sz=18,
               bold=True, color=theme.C_TEXT_H2),
            MathTex(r"\frac{dT}{T - 20} = k\,dt",
                    font_size=36, color=theme.ACCENT),
            _T("Coincidência útil — ou existe uma classe inteira?", sz=18,
               italic=True, color=theme.C_TEXT_ANNOT),
            _T("Próxima aula: Equações Separáveis.", sz=18,
               bold=True, color=theme.C_TEXT_H2),
            _T("Pré-req.: integração (substituição, frações parciais).", sz=16,
               italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        place_text(bot, pergunta)

        self.play_seq(FadeIn(hdr), FadeIn(top), FadeIn(ctx))
        self.next_slide()
        self.play(FadeIn(bot), FadeIn(pergunta))
        self.next_slide()
        self._fadeout()

    # ── Slide 20 — Exercícios ─────────────────────────────────────────────────
    # Frame 15. Layout: 2×2.
    # Cada painel TL/TR/BL/BR: usable 5.73×2.43u.
    # Padrão A em todos (label sz=18 bold + MathTex sz=32 + corpo sz=18).
    # TL accent: ex.1 → 3 itens; TR: ex.2 → 4 itens; BL: ex.3 → 2 itens; BR: ex.4 → 4 itens.
    def _slide_exercicios(self):
        hdr = _hdr(self, "Exercícios")

        g  = ContentGrid(shadow=True)
        tl = g.panel(0,  50,  0,  50, accent=True)
        tr = g.panel(0,  50, 50, 100)
        bl = g.panel(50, 100, 0,  50)
        br = g.panel(50, 100, 50, 100)
        hl = g.h_line(50)
        vl = g.v_line(50)

        # TL — Padrão A; place_text; h≈1.55u < 2.43u ✓
        ex1 = VGroup(
            _T("1. Verifique que y = e^{0,1x²} é solução de", sz=18,
               bold=True, color=theme.C_TEXT_H2),
            MathTex(r"\frac{dy}{dx} = 0{,}2xy",
                    font_size=32, color=theme.C_TEXT_BODY),
            _T("em (-∞, +∞).", sz=18),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(tl, ex1)

        # TR — Padrão B (lista de MathTex); place_text
        ex2 = VGroup(
            _T("2. Classifique: tipo, ordem, linearidade.", sz=18,
               bold=True, color=theme.C_TEXT_H2),
            MathTex(r"\dfrac{d^2x}{dt^2} + 16x = 0",
                    font_size=26, color=theme.C_TEXT_BODY),
            MathTex(r"\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = 0",
                    font_size=24, color=theme.C_TEXT_BODY),
            MathTex(r"(1-y)\,y' + 2y = e^x",
                    font_size=26, color=theme.C_TEXT_BODY),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        place_text(tr, ex2)

        # BL — Padrão A; place_text
        ex3 = VGroup(
            _T("3. Mostre que y = xeˣ é solução de", sz=18,
               bold=True, color=theme.C_TEXT_H2),
            MathTex(r"y'' - 2y' + y = 0",
                    font_size=32, color=theme.C_TEXT_BODY),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        place_text(bl, ex3)

        # BR — Padrão C; place_text
        ex4 = VGroup(
            _T("4. Para dP/dt = 0,15P + 20,  P(0) = 100:", sz=17,
               bold=True, color=theme.C_TEXT_H2),
            _T("(a) Taxa de crescimento em t = 0?", sz=17),
            _T("(b) P(t) é crescente ou decrescente?", sz=17),
            _T("Responda sem resolver a EDO.", sz=16,
               italic=True, color=theme.C_TEXT_ANNOT),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        place_text(br, ex4)

        self.play_seq(FadeIn(hdr),
                      FadeIn(tl), FadeIn(ex1),
                      FadeIn(tr), FadeIn(ex2),
                      FadeIn(bl), FadeIn(ex3),
                      FadeIn(br), FadeIn(ex4))
        self.next_slide()
        self._fadeout()
