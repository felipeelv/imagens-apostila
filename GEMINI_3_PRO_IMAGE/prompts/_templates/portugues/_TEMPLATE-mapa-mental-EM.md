# Padrão de Mapa Mental — Língua Portuguesa (Ensino Médio: 1ª, 2ª e 3ª série)

Template canônico para gerar mapas mentais visuais de capítulos de Português 1 do Ensino Médio, usando Gemini 3 Pro Image (`gemini-3-pro-image-preview`) via `gerar.py`.

**Abrangência aprovada:** 1ª, 2ª e 3ª série EM. Validado no Cap 1 da Unidade 4 da 1ª série EM (Elementos Mórficos), versão final em `saida/Portugues/1serie/Unidade-4-Estrutura-e-Formacao-de-Palavras/Cap1-elementos-morficos-v5.png`.

**Diferenças em relação aos templates EF1 (4-6) e EF2 (7-9):**

| Característica | EF1 | EF2 | EM |
|---|---|---|---|
| Centro | Círculo + palavra MAIÚSCULA Roboto Black | Palavra em cursiva preta horizontal | **Caixa âncora robusta + título 3D extrudado em duas linhas** (face navy + extrusão magenta) |
| Mascote | Estudante crível | Sem mascote | Sem mascote |
| Setas/ramos | Pinceladas espessas | Finas marker em ângulos orgânicos | **Ramos curvos médio-grossos coloridos** estilo data-viz moderno |
| Cards | Mini-cenas ilustradas | Cards textuais com header colorido | **Cards com header em color block + badge circular com numeral romano** |
| Tipografia | Roboto consistente | Sans-serif + uppercase marker | **Sans-serif moderno editorial** (Plus Jakarta / Manrope / Roboto pesado) |
| Numeração | Não numerados | Não numerados | **Numerais romanos I-VI em badges circulares** |
| Marker-highlights | Não | Não | **Sim — keywords em pílulas pastel coloridas** |
| Fundo | Branco | Branco | Branco LIMPO (sem elementos decorativos espalhados) |
| Versículo | Card dedicado | Banner discreto rodapé | Banner discreto rodapé |
| Tom | Khan/Duolingo lúdico | Sketchnote maduro | Notion/Pinterest premium teen-vibe (vibrante mas maduro) |

---

## Como usar

1. Receber blueprint do capítulo de 1ª, 2ª ou 3ª série EM.
2. Mapear nos slots da PARTE B.
3. Criar pastas: `mkdir -p prompts/Portugues/<serie>/Unidade-<N>-<Nome> saida/Portugues/<serie>/Unidade-<N>-<Nome>` (use `1serie`, `2serie`, `3serie` sem espaço).
4. Salvar prompt em `prompts/Portugues/<serie>/Unidade-<N>-<Nome>/Cap<N>-<slug>-v1.md`.
5. Rodar `gerar.py` salvando imagem na estrutura espelhada com `--aspect-ratio 3:4 --image-size 2K`.

**Aspect ratio 3:4 é a opção mais próxima de A4 retrato** (A4 = ~1:1.414; 3:4 = 1:1.333). Ao imprimir em A4, a imagem fica com leves margens superior/inferior — é a melhor compatibilidade disponível no script.

---

## PARTE A — ESQUELETO FIXO

### Instrução de raciocínio inicial

Before generating the image, think step by step about the spatial layout. The composition is a vertical 3:4 educational **MIND MAP** for a Brazilian student in `{{SERIE_EM}}` (a 15-17 year old learner approaching ENEM/vestibular). The reference is **modern mind-map study aesthetic** — vibrant, energetic, with strong central concept and curved colored branches radiating outward to surrounding cards. Premium teen-study vibe (Notion-meets-Pinterest 2024-2025). NOT a grid poster. NOT a corporate handout. NOT marker sketchnote (that's EF2). NOT Khan/Duolingo with mascot (that's EF1). The layout MUST be clearly recognizable as a MIND MAP. The page is a study reference for revision, readable in 3 to 5 minutes, designed for **A4 print**. Plan placement, color distribution, typographic hierarchy and reading flow first; only then render the final image. Text rendering must be precise: every Portuguese word must include correct diacritics.

### Tipografia

Use a confident **modern editorial sans-serif** (Plus Jakarta Sans, Manrope, Space Grotesk, or Roboto in heavy weights). NO formal serif. NO marker handwritten. NO traditional cursive ANYWHERE.

- **Central title (in anchor box, 3D extruded)**: bold sans-serif **BLACK UPPERCASE**, very large, written across two stacked horizontal lines.
- **Conceptual subtitle (inside anchor)**: sans-serif Regular Italic medium-size, slate gray.
- **Card numerals (I, II, III...)**: oversized **bold sans-serif Roman numerals** inside circular badges.
- **Card titles**: bold sans-serif **UPPERCASE in white**, on a colored solid header strip.
- **Body text**: clean sans-serif Regular/Medium in dark navy. Bold key terms in card's accent color. Selected key concepts wrapped in **soft marker-highlight pills** (translucent pastel rectangle behind word, in card's accent tint).
- **Morphological/technical notation** (if applicable): monospace font in card's accent color.

### Estilo visual geral

Modern mind-map aesthetic — energetic, vibrant, alive. Card shapes are **rectangles with generous rounded corners (~14 px)**, like modern app cards. Each card has:
- A **solid colored header strip** at the top (full color block) with the card title in bold WHITE.
- A **circular badge** with the Roman numeral floating slightly off the upper-left of the header (white circle, colored border, soft drop shadow).
- White interior body.
- Subtle drop shadow under the entire card.

**Pure white background — NO cream tint, NO grid, NO paper texture, NO vignette.** A4 print-ready.

**NO decorative geometric accents on the background.** The background is CLEAN — no scattered dots, no "+" marks, no diagonal lines, no stars, no dotted clusters. Energy comes from branches, headers and chips.

**Vibrant modern palette** (saturated but harmonized — NOT neon, NOT pastel, NOT corporate sober):
- electric cobalt blue (#3a5fff approx)
- vivid magenta (#e6326e approx)
- lime green (#9ed838 approx)
- mango orange (#f59331 approx)
- deep violet (#7e3aff approx)
- golden yellow (#f5c63e approx)

Each color anchors one card AND its branch.

NO mascot. NO illustrated mini-scenes. NO drawings.

### Estrutura — caixa âncora + 6 ramos curvos + 6 cards

Mind-map structure:

1. **At the geometric center of the page**: a robust ANCHOR BOX containing the chapter title in 3D extruded type — the focal point.
2. **From the anchor box, 6 colored CURVED BRANCHES radiate outward** in varied angles to reach the 6 surrounding cards.
3. **Cards distributed organically** around the central anchor.
4. **Bottom-right small banner**: verse + reflection.

NO identification pill / metadata badge / course tag (like "PORTUGUÊS 1 · Xª SÉRIE EM · UNIDADE Y") anywhere on the page. The chapter title in the central anchor is enough.

#### Estilo das ramificações

Each branch:
- Is a **medium-thick curved colored line** (~6-8 px), with rounded ends, gentle curvature.
- Color matches destination card's accent.
- Branches radiate at varied angles, creating an organic radial fan.
- Each branch may have a **small filled circle (dot)** at its origin on the anchor box, in the branch's color.
- Tapered or rounded end at the card; NO arrowhead.
- Optional thin shadow under each branch.

NOT pinceladas espessas (EF1). NOT linhas finas marker em ângulos retos (EF2). It's data-viz modern: clean, confident, gently curved.

### Caixa âncora central

A robust anchor box at the geometric center, occupying ~28-32% of the page width:
- Subtle dark navy outline (~2 px)
- Clean white interior
- Thin colored top accent strip (cobalt blue)
- 6 small colored connection dots distributed along outer edges (one per branch color)

Inside the anchor:
- **Title (3D extruded)**: `{{CONCEITO_CENTRAL}}` in giant sans-serif Black uppercase, written across **TWO STACKED HORIZONTAL LINES**, both reading left-to-right.

  **3D EXTRUSION RULES (refined and clean):**
  - Front face: solid **dark navy** (~#1e2a44), crisp vector edges, NO blur, NO gradient, NO glow, NO outline.
  - Behind every letter, a **single solid extrusion layer** in **vivid magenta** (~#e6326e), creating clear depth, shifted ~5-7 px down-and-right, uniform across all letters.
  - Single solid color extrusion — NOT multiple stacked shadows, NOT blurred drop shadow.
  - Letters do NOT overlap each other; comfortable letter-spacing.
  - Both lines have the same 3D treatment, same offset direction.
  - Effect: modern poster typography (Spotify Wrapped, sneaker-brand wordmarks, magazine displays). Bold, clean, energetic. NOT cartoonish, NOT chrome, NOT skeuomorphic glossy, NOT WordArt.

- Below title, thin horizontal navy decorative line (~60 px).
- **Conceptual subtitle**: `{{FRASE_DEFINIDORA}}` in sans-serif Regular Italic medium-size, slate gray.

Both title lines MUST be HORIZONTAL.

### Cards (5 a 7)

Distribute 5-7 cards organically around the central anchor, connected by colored curved branches. Each card follows the structure: header color block + circular badge with Roman numeral + white interior + body text + sub-pills/tables when needed + marker-highlight pill at the bottom for the summary.

### Banner de versículo (rodapé discreto)

Bottom-right small banner OUTSIDE the mind map structure:
- Thin vertical line (~3 px) on the left edge in the chapter's primary accent color
- Verse reference in bold sans-serif: `{{VERSICULO}}`
- Brief reflection in italic regular small gray: `{{REFLEXAO_VP_CURTA}}`

### Restrições negativas (sempre)

NÃO incluir:
- Layout em grade rígida 2×3. A página é um MAPA MENTAL — caixa âncora central com ramos curvos coloridos saindo para os cards.
- Mascote-personagem ou ilustração de estudante.
- Mini-cenas ilustradas dentro dos cards.
- Cards sem header colorido sólido. CADA card tem header em color block + badge circular com numeral romano flutuante.
- Cursiva, manuscrito, marker-handwritten ou caligráfica em qualquer texto. APENAS sans-serif moderno.
- Fonte serifada formal.
- Setas pintadas espessas (EF1). Setas finas marker em ângulos retos (EF2). Aqui são **ramos curvos médio-grossos**, estilo data-viz moderno.
- Selos históricos, retratos antigos, créditos a gramáticos.
- Marcas comerciais (Anglo, Bernoulli, Poliedro, Etapa, Descomplica, Hexag, Notion, Figma, etc.), logotipos, propagandas, marca d'água.
- Asteriscos, hashtags, colchetes ou marcadores markdown literais aparecendo no texto.
- Marcadores de posição "11h", "1h", etc.
- Pill badge ou tag de identificação tipo "PORTUGUÊS 1 · Xª SÉRIE EM · UNIDADE Y" em qualquer canto da página.
- Elementos decorativos geométricos espalhados pelo fundo (pontos, "+", traços diagonais, hollow squares, dotted clusters, stars). Fundo LIMPO.
- Fundo de cor (creme, bege). Branco puro.
- Texturas de papel, vinhetas, gradientes pesados.
- Cards repetidos. Cada card aparece UMA única vez.
- Paleta sóbria/corporativa. USE: cobalt blue, magenta, lime green, mango orange, deep violet, golden yellow.
- Título central plano sem 3D. O título DEVE ter extrusão 3D limpa (face navy + extrusão magenta uniforme).
- Título 3D borrado, com glow, com gradient, com chrome, com brilho skeuomorphic, ou com múltiplas sombras empilhadas.
- Texto em idioma diferente de português brasileiro.

---

## PARTE B — SLOTS A PREENCHER

| Slot | Descrição | Exemplo (Cap 1 / 1ª série) |
|---|---|---|
| `{{SERIE_EM}}` | Série + nível em inglês | `1ª série EM (a 15-16 year old learner)` |
| `{{CONCEITO_CENTRAL}}` | Título do capítulo em 2 linhas, MAIÚSCULAS | `ELEMENTOS / MÓRFICOS` |
| `{{FRASE_DEFINIDORA}}` | Subtítulo conceitual, italic, dentro da âncora | `morfemas: as unidades mínimas de significado` |
| `{{VERSICULO}}` | Versículo do campo VP do blueprint | `Provérbios 10:9` |
| `{{REFLEXAO_VP_CURTA}}` | Reflexão de 1 linha conectando tema ao versículo | `cada morfema cumpre seu papel — coerência entre as partes revela integridade` |

**Cards (5-7)**: para cada tópico do blueprint, definir:
- Numeral romano (I, II, III, IV, V, VI, VII)
- LABEL DO CARD (uppercase)
- COR DE ACENTO (uma da paleta sem repetir): cobalt blue, magenta, lime green, mango orange, deep violet, golden yellow
- TIPO: card simples (texto + marker-highlight) OU com sub-pills OU com mini-tabela OU com fórmula visual OU com chips coloridos (para análises segmentadas)
- CONTEÚDO: conceito principal + 3-6 exemplos/regras + frase-resumo

### Bloco "TEXT TO RENDER VERBATIM"

Listar todas as strings que aparecem na imagem, com diacríticos preservados.

---

## Validação antes de gerar

1. Conferir diacríticos.
2. Conferir que NÃO há mascote, mini-cenas ilustradas, cursiva nem serif formal.
3. Conferir que o título central tem extrusão 3D limpa (face navy + extrusão magenta).
4. Conferir que cada card tem header em color block + badge circular numeral romano.
5. Conferir que os ramos são curvos médio-grossos (não pinceladas EF1, não linhas marker EF2).
6. Conferir que NÃO há pill badge identificador no topo.
7. Conferir que o fundo está limpo (sem dots/+/diagonais espalhados).
8. Conferir que o versículo é banner discreto no rodapé.

## Iteração esperada

Pequenos defeitos comuns:
- Modelo às vezes duplica cards → reforçar "render only once" + "count: 1".
- Modelo tenta inserir pill identificador apesar da proibição → reforçar nas restrições negativas.
- 3D do título sai borrado/messy → especificar com detalhes (face sólida + extrusão sólida única, sem blur, sem múltiplas camadas).
- Modelo inclui elementos decorativos espalhados no fundo → reforçar "background CLEAN, no scattered accents".

---

## Referência canônica

Versão final aprovada: `saida/Portugues/1serie/Unidade-4-Estrutura-e-Formacao-de-Palavras/Cap1-elementos-morficos-v5.png`
Prompt-fonte: `prompts/Portugues/1serie/Unidade-4-Estrutura-e-Formacao-de-Palavras/Cap1-elementos-morficos-v5.md`

Sempre abrir essa referência ao lado quando estiver gerando para EM.
