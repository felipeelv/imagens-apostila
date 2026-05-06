# Padrão de Mapa Mental — Língua Portuguesa (EF2: 7º, 8º e 9º ano)

Template canônico para gerar mapas mentais visuais de capítulos de Português 1 dos anos finais do Ensino Fundamental, usando Gemini 3 Pro Image (`gemini-3-pro-image-preview`) via `gerar.py`.

**Abrangência:** 7º, 8º e 9º ano EF.

**Diferença em relação ao template EF1 (4º-6º ano):**

| Característica | EF1 (4-6) | EF2 (7-9) |
|---|---|---|
| Centro | Círculo limpo + palavra MAIÚSCULA Roboto Black | Palavra-conceito em SCRIPT/CURSIVA preta grande, sem círculo |
| Mascote | Estudante crível ao lado do círculo | SEM mascote — o foco é texto e esquema |
| Setas | Pinceladas espessas em 6/8 horas regulares | Finas tipo marker, em ângulos variados |
| Cards | Mini-cenas ilustradas + texto | Caixas TEXTUAIS com header colorido, sem ilustrações narrativas |
| Tipografia interna | Roboto consistente | Mistura: header marker uppercase + corpo sans-serif |
| Sub-grupos | Raros | Comuns (3-4 mini-caixas conectadas a um conceito-pai) |
| Tom | Khan/Duolingo, lúdico-amigável | Sketchnote premium, "caderno de estudo" maduro |
| Versículo | Card dedicado de fechamento | Banner discreto no rodapé/canto, sem ocupar card |

**Validação:** primeiro capítulo em produção — Cap 1 Unidade 4 Verbos do 7º ano.

---

## Como usar

1. Receber blueprint do capítulo de 7º, 8º ou 9º ano.
2. Mapear nos slots da PARTE B.
3. Criar pastas: `mkdir -p prompts/Portugues/<ano>ano/Unidade-<N>-<Nome> saida/Portugues/<ano>ano/Unidade-<N>-<Nome>`.
4. Salvar prompt em `prompts/Portugues/<ano>/Unidade-<N>-<Nome>/Cap<N>-<slug>-v1.md`.
5. Rodar `gerar.py` salvando imagem na estrutura espelhada.

Convenção de nomenclatura idêntica ao EF1.

---

## PARTE A — ESQUELETO FIXO

### Instrução de raciocínio inicial

Before generating the image, think step by step about the spatial layout. The composition is a vertical 3:4 educational mind map for a Brazilian student in `{{ANO_SERIE}}` (a 12-15 year old learner). The visual reference is the **sketchnote / clean handwritten study-poster** style — like a polished notebook page from a study-savvy teen. NOT Khan Academy / Duolingo (that's for younger kids). NOT corporate infographic. The page must feel like premium handwritten study notes: clean, structured, slightly playful but academically serious. Plan placement, color distribution, typographic hierarchy and reading flow first; only then render the final image. Text rendering must be precise: every Portuguese word must include correct diacritics. The page must be readable in 2 to 3 minutes.

### Tipografia

Use a careful mix of three type roles:
- **Central concept**: large hand-drawn **SCRIPT/CURSIVE** in solid black (think "Caveat Bold", "Sacramento", "Pacifico" — flowing handwritten style with personality, not formal calligraphy). This is the only cursive on the page.
- **Card titles**: bold marker-style **SANS-SERIF UPPERCASE** in the card's accent color. Spacing slightly wider than normal. Looks like written with a colored marker.
- **Body text inside cards**: clean sans-serif **Roboto Regular/Medium** in dark navy or near-black, with key terms highlighted in the card's accent color or via marker-style underline.
- **Marginal handwritten notes**: light handwritten-feel sans-serif italic, in pencil-gray, used sparingly for definitions or asides.

NO formal serif. NO multiple cursive fonts. The cursive appears ONLY at the central concept word.

### Estilo visual geral

Style guide: **modern sketchnote** / **clean study-poster** look. Hand-drawn outlines in dark navy or black ink (slight weight variation). Card frames look like they were drawn by a student with a fineliner. Each card uses a single colored marker accent: a thick marker-style line under or around the card title, plus a colored frame border. Interior of every card stays white — color enters via title, border and underlines, NEVER as full card fill.

**Pure white background — NO cream tint, NO grid pattern, NO paper texture, NO vignette, NO background color fill.** A4 print-ready: economical with ink. The decoration comes from the connectors and card borders, not from background fills.

Saturated marker palette (vibrant but not neon): magenta-red, coral-orange, golden yellow, lime green, sky blue, teal cyan, royal purple, hot pink. 6 to 8 colors total, each anchoring one card. No color dominates more than 25% of the page.

NO illustrated mini-scenes inside cards. NO mascot characters. NO drawings of children, school items, or daily-life vignettes. Cards contain ONLY text + small structural diagrams (sub-boxes, arrows, small geometric icons). The "drawings" of this template are abstract structures: tables, sub-grouped boxes, arrows linking concepts.

### Estrutura — conceito central + setas finas + cards textuais

The composition centers on the chapter's main concept word, written in large flowing cursive. From this central word, **thin marker-style arrows** radiate outward in **varied angles** — NOT fixed clock positions. Some arrows curve gently, some are nearly straight, some have small bends. Each arrow:
- Is a thin line drawn with marker confidence (about 2-3 px equivalent), NOT a thick painted ribbon.
- Has a clearly defined arrowhead at the destination side.
- Is colored in the same hue as the destination card's accent (the arrow visually "belongs" to its card).
- Can be straight, curved, or dog-legged depending on layout.
- Carries NO label on the arrow itself. The destination card's title carries the label.

Cards are RECTANGULAR with subtly rounded corners (~6-8 px radius), distributed organically around the central word — NOT in a strict 6-position clock. Layout feels balanced but not symmetrical: cards can have varied sizes depending on content density. Each card has:
- A colored top header strip OR a colored frame border in the accent color.
- The title in bold marker-style UPPERCASE in the accent color.
- Body text in clean sans-serif (Roboto), centered or left-aligned depending on content.
- Sub-groups appear as 2-4 mini-boxes connected to the parent card by tiny inner arrows. Use sub-groups when a concept naturally splits into typed categories (e.g., "MODES → Indicative / Subjunctive / Imperative" or "CONJUGATIONS → -ar / -er / -ir").

### Conceito central

In the heart of the page, write the chapter's main concept in large hand-drawn cursive in solid black: `{{CONCEITO_CENTRAL_CURSIVA}}`. The cursive must look like a confident handwritten flourish — not stiff, not overly decorative.

**CRITICAL ORIENTATION RULE:** the central concept word MUST be written **HORIZONTALLY**, with all letters reading left-to-right on a single straight horizontal baseline. NEVER vertical, NEVER rotated, NEVER stacked, NEVER curved along an arc. This is non-negotiable — vertical orientation harms student readability.

To the left or right of the central word (the side with empty space), or below it on a separate horizontal line, in handwritten-feel italic small (pencil-gray): `{{FRASE_DEFINIDORA}}`. This is a brief explanation that sits as marginal note next to or below the central word, NOT as a full card. Each line of text reads horizontally.

### Cards (5 a 7)

Distribute 5 to 7 cards organically around the central concept, connected by thin colored arrows. Each card follows the structure described above.

### Banner de versículo (rodapé discreto)

In the bottom-right or bottom-center of the page, place a small unobtrusive horizontal banner with the chapter's verse, formatted as:
- Tiny marker-style underline in the chapter's primary color
- Verse reference in bold sans-serif: `{{VERSICULO}}`
- Brief reflection in handwritten-feel italic small: `{{REFLEXAO_VP_CURTA}}`

The banner must be clearly subordinate to the main content. NO full card for the verse.

### Restrições negativas (sempre)

NÃO incluir:
- Mascote-personagem ou ilustração de estudante. EF2 não usa mascote.
- Mini-cenas ilustradas dentro dos cards (sem cenas de mochila, bicicleta, sala, criança, etc).
- Cards com fundo colorido sólido. Os interiores são SEMPRE brancos.
- Fonte serifada formal, calligraphic ou de fantasia em qualquer texto que não seja o conceito central.
- Mais de uma palavra em cursiva. APENAS o conceito central usa cursive.
- Layout em 6 horas fixas do relógio. Distribuição é orgânica, ângulos variados.
- Setas pintadas espessas tipo pincelada (estilo EF1). Aqui as setas são finas, tipo marker.
- Selos históricos, retratos antigos, créditos a gramáticos.
- Marcas comerciais, logotipos, propagandas, marca d'água.
- Asteriscos, hashtags, colchetes ou marcadores markdown literais aparecendo no texto da imagem.
- Marcadores de posição "11h", "1h", "3h" ou qualquer indicação de horas literais.
- Fundo de cor (creme, bege, qualquer tom). Branco puro.
- Texturas de papel, vinhetas, gradientes ou tonalizações no fundo.
- Mais de 7 cards principais.
- Texto em idioma diferente de português brasileiro.

---

## PARTE B — SLOTS A PREENCHER

| Slot | Descrição | Exemplo (Cap 1 Verbos / 7º EF) |
|---|---|---|
| `{{ANO_SERIE}}` | Série + nível em inglês | `7º ano EF (a 12-13 year old learner)` |
| `{{CONCEITO_CENTRAL_CURSIVA}}` | Palavra-conceito em cursiva, no centro | `Verbo` |
| `{{FRASE_DEFINIDORA}}` | Frase curta lateral ao conceito central | `indica ação, estado, fenômeno ou mudança` |
| `{{VERSICULO}}` | Versículo do campo VP do blueprint | `Provérbios 10:9` |
| `{{REFLEXAO_VP_CURTA}}` | Reflexão de 1 linha conectando o tema ao versículo | `classificar com integridade é nomear o que é` |

**Cards (5-7)**: para cada tópico do blueprint, definir:
- LABEL DO CARD (uppercase, marker-style)
- COR DE ACENTO (da paleta marker)
- TIPO: card simples (texto + exemplos) OU card com sub-grupos (parent + 2-4 mini-boxes conectados)
- CONTEÚDO TEXTUAL: 3-6 linhas por card

**Cores disponíveis** (use uma por card, sem repetir): magenta-red, coral-orange, golden yellow, lime green, sky blue, teal cyan, royal purple, hot pink.

### Bloco "TEXT TO RENDER VERBATIM"

Listar todas as strings que aparecem na imagem, com diacríticos preservados, sem markdown literal.

---

## Validação antes de gerar

1. Conferir diacríticos.
2. Conferir que a única cursiva é o conceito central.
3. Conferir que NÃO há mascote nem mini-cenas ilustradas em cards.
4. Conferir que as setas são finas (marker-style), não pinceladas espessas.
5. Conferir que os cards têm interior branco, com cor apenas em borda/header/underline.
6. Conferir que o versículo é um banner discreto, não card dedicado.
7. Conferir que cards sub-agrupam conceitos quando faz sentido (ex: 3 conjugações sob CONJUGAÇÕES).

## Iteração esperada

Pequenos defeitos comuns nesta estética:
- Modelo desenha mascote sem ser pedido → reforçar exclusão.
- Cards saem com fundo colorido → reforçar "white interior, color only on border/header".
- Cursiva escapa para outros textos → reforçar "ONLY central word in cursive".
- Setas saem pinceladas espessas (estilo EF1) → reforçar "thin marker arrows".

---

## Referência canônica

- EF1 (estilo Khan/Duolingo, com mascote): `prompts/_TEMPLATE-mapa-mental-portugues.md`
- EF2 (estilo sketchnote, sem mascote): este arquivo

Sempre abrir a referência visual do COC by Pearson "Verbos" (a inspiração estética) ao lado quando estiver gerando para EF2.
