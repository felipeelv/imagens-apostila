# Padrão de Mapa Mental — Língua Portuguesa (4º, 5º e 6º ano EF)

Template canônico para gerar mapas mentais visuais de capítulos de Língua Portuguesa do Colégio Eleve, usando Gemini 3 Pro Image (`gemini-3-pro-image-preview`) via `gerar.py`.

**Abrangência aprovada:** 4º ano, 5º ano e 6º ano do Ensino Fundamental. Sempre que o usuário enviar blueprint de capítulo de Português dessas três séries, aplicar este template diretamente — não negociar layout, paleta, tipografia, fundo nem estrutura geral.

**Padrão validado em três capítulos:**
- Adjetivo (6º ano EF, protótipo) — `saida/Portugues/6ano/Prototipo-Adjetivo/adjetivo-v8.png` (versão de referência estética)
- Tempos Verbais do Indicativo (4º ano EF, Unidade 4 Verbos, Cap 1) — `saida/Portugues/4ano/Unidade-4-Verbos/Cap1-tempos-verbais-v2.png`
- Concordância Verbal (4º ano EF, Unidade 4 Verbos, Cap 2) — `saida/Portugues/4ano/Unidade-4-Verbos/Cap2-concordancia-verbal-v2.png` (referência atual em fundo branco para impressão A4)

**Faixa etária do mascote por série:**
- 4º ano EF → mascote de 9-10 anos
- 5º ano EF → mascote de 10-11 anos
- 6º ano EF → mascote de 11-12 anos

A linguagem dos exemplos e a profundidade dos conceitos seguem o blueprint de cada capítulo; o esqueleto visual abaixo é fixo.

---

## Como usar

1. **Receber o blueprint do capítulo** (do repositório `~/material-blueprints/` ou colado pelo usuário).
2. **Mapear o conteúdo do blueprint nos slots da PARTE B** abaixo:
   - Conceito central (1 palavra, geralmente o nome do capítulo)
   - Frase definidora (1 linha curta)
   - Elemento visual central (cena cotidiana que ancora o conceito)
   - 5 a 7 tópicos principais → viram as 5-7 setas/cards
   - Versículo bíblico do capítulo → entra no card de ética/escolha
3. **Construir o prompt final** copiando a PARTE A (fixa) e preenchendo os `{{slots}}` da PARTE B com o conteúdo do capítulo.
4. **Salvar** o prompt na estrutura organizada:
   ```
   prompts/Portugues/<ano>ano/Unidade-<N>-<Nome>/Cap<N>-<tema>-v<N>.md
   ```
   Exemplo: `prompts/Portugues/4ano/Unidade-4-Verbos/Cap1-tempos-verbais-v1.md`
5. **Rodar** salvando a imagem na estrutura espelhada:
   ```bash
   cd GEMINI_3_PRO_IMAGE && uv run gerar.py \
     --prompt prompts/Portugues/<ano>ano/Unidade-<N>-<Nome>/Cap<N>-<tema>-v<N>.md \
     --saida saida/Portugues/<ano>ano/Unidade-<N>-<Nome>/Cap<N>-<tema>-v<N>.png \
     --aspect-ratio 3:4 --image-size 2K
   ```
   Antes de rodar, criar as pastas se ainda não existirem: `mkdir -p prompts/Portugues/<ano>ano/Unidade-<N>-<Nome> saida/Portugues/<ano>ano/Unidade-<N>-<Nome>`.

**Convenção de nomenclatura:**
- Pastas: `Portugues/4ano/`, `Portugues/5ano/`, `Portugues/6ano/`. Dentro de cada ano, uma pasta por unidade no formato `Unidade-<N>-<Nome>` (ex: `Unidade-4-Verbos`, `Unidade-2-Substantivo`).
- Arquivos: `Cap<N>-<slug-do-tema>-v<N>.md/png` (ex: `Cap1-tempos-verbais-v1.md`). O sufixo `v<N>` permite múltiplas iterações sem sobrescrever.
6. **Avaliar** o resultado e iterar se preciso (geralmente 1-3 rodadas bastam).

---

## Princípios pedagógicos do mapa

- **Resumo, não aula**: leitura de 2 a 3 minutos, aluno consulta depois da aula.
- **Mostrar pelo desenho, não só nomear**: cada conceito ganha uma mini-cena ilustrada do cotidiano escolar (mochila, bicicleta, livro, colega, sala).
- **Adequação etária**: vocabulário e exemplos calibrados para a faixa do capítulo (6º ano ≠ 1ª EM).
- **Hierarquia clara**: olho cai no centro → segue setas em sentido horário a partir das ~11h.
- **Conexão Eleve**: um dos cards trata uso ético/responsável da palavra, com versículo bíblico discreto no canto.
- **Sem figura histórica/selo de autor** — eles competem com o conteúdo e o aluno não precisa.

---

## PARTE A — ESQUELETO FIXO (não alterar entre capítulos)

> Cole essa seção integral no prompt final, antes da PARTE B preenchida.

### Instrução de raciocínio inicial

Before generating the image, think step by step about the spatial layout. The composition is a vertical 3:4 educational visual summary for a Brazilian student in `{{ANO_SERIE}}`. The page must feel energetic, modern, illustrated and engaging — like a Khan Academy or Duolingo illustration, NOT like a textbook page or a calligraphy poster. Plan placement, color distribution, typographic hierarchy and reading flow first; only then render the final image. Text rendering must be precise: every Portuguese word must include correct diacritics. The page must be readable in 2 to 3 minutes. Use Roboto for ALL text.

### Tipografia

Use the **Roboto** font family for ALL text in the image. No serif, no script, no calligraphy.
- Roboto Black for the central concept word and uppercase titles on cards.
- Roboto Bold for arrow labels (white text on the arrow body).
- Roboto Medium for example pairs.
- Roboto Regular Italic for marginal notes and speech-bubble dialogue.
- Letters must be clean, geometric, sans-serif, with full diacritic support. NO asterisks, hashtags or markdown markers rendered literally.

### Estilo visual geral

Modern editorial illustration in the spirit of Khan Academy / Duolingo / Brainscape — vibrant, friendly, slightly playful but not childish. Hand-drawn outlines combined with saturated color fills that have very subtle painterly texture (gouache-like, gentle brush variation, NOT perfectly flat vector fill). **Pure white background — NO cream tint, NO vignette, NO paper texture, NO background color fill of any kind.** The page is designed for A4 print and must keep the background as solid white so it does not consume printer ink. Cards must remain clearly distinct on white via their colored accent stripe, soft drop shadow and dark-navy outline. Outlines in dark navy ink with slight weight variation, never pure black, never perfectly uniform.

Saturated palette (NOT pastel, NOT neon): coral red, electric blue, golden yellow, emerald green, grape purple, tangerine orange. Each color anchors one branch (one arrow + its destination card). No color dominates more than 25% of the page.

Illustrations whenever possible show MINI SCENES from a Brazilian student's daily life: backpack, bicycle, classroom, friend, book, lunchbox — never abstract icons floating alone. Show the concept through the scene, not just label it.

**Style restriction**: characters must look like real-ish stylized students of the chapter's age, with moderate proportions and friendly faces — no big-headed mascots, no exaggerated bouncy proportions, no Cartoon Network look.

### Estrutura — círculo central + setas pintadas + cards

DO NOT use thin curved branches like a traditional mind map. Also DO NOT use stiff vector-flat geometric arrows. Instead use **lively painterly arrows** that feel alive — like thick brush-stroke ribbons or hand-painted banners with personality. Each arrow:
- Has a thick body in saturated color (one color per arrow), with subtle hand-painted texture (slight ink/paint variation, very subtle grain, NOT solid flat fill).
- Has a clearly defined arrowhead pointing AWAY from the central circle.
- Has a gently curved or slightly tapered body — never a straight rigid rectangle. Width varies organically like a brush stroke, slightly thicker in the middle, slightly tapered toward the head.
- Has a soft hand-drawn dark navy outline that varies in weight, plus a soft drop shadow underneath.
- Carries a short uppercase label written ON the arrow itself in white Roboto Bold, with a very subtle slight tilt to feel less mechanical.

**Arrow-card pairing rule (non-negotiable)**: every arrow's label must match the title of the card it terminates at. Each colored arrow lands on its matching card and only on its matching card. Do not swap destinations.

### Círculo central

In the heart of the page, a clean perfect circle (NOT a shield, NOT a rosette, NOT a star, NOT a polygon — only a simple round circle). Dark navy outline, **white interior** (matching the page background — no cream, no warm glow). Inside the circle, in giant Roboto Black uppercase: `{{CONCEITO_CENTRAL}}`. Below, in smaller Roboto Italic (rendered as italic, NOT with literal asterisks): `{{FRASE_DEFINIDORA}}`.

Beside the circle, integrated naturally into the composition, draw a small student mascot (age `{{IDADE_PERSONAGEM}}`, friendly stylized face, simple t-shirt) interacting with `{{ELEMENTO_VISUAL_CENTRAL}}`. The mascot's pose should present the concept naturally — pointing to the circle, holding the object, or showing it to the reader.

### Elementos decorativos de fundo

Spread small playful decorative marks across the **white background**, in the empty spaces between cards and arrows. They must be small, low-saturation (so they don't consume excessive ink when printed on A4), slightly faded, and clearly subordinate to the cards and arrows. Use a mix of:
- Tiny doodled stars (3-4 pointed, hand-drawn, in pale gold or pale coral, scattered)
- Short diagonal motion lines in pencil-gray, like quick gesture marks
- Small dotted clusters of 3 dots, in the accent colors of nearby arrows
- A few tiny circles or sparkle marks (small "+" or "*" shapes — drawn, not literal characters)
- One or two very small open-line squiggles, like ribbon flicks
- Subtle marker-style highlight smudges in pale yellow under one or two key words

These decorations should feel like the natural doodles of a happy student decorating their notebook — never form a pattern, never overlap text, never overlap an arrow body.

### Hierarquia de leitura

The reader's eye must land first on the central circle, then naturally follow the colored arrows in clockwise order starting from the upper-left (~11 o'clock position). Each arrow is the visual highway pulling the eye to its card. Cards are clearly distinct, each with its own accent color matching its arrow. Generous white space between cards — the page must breathe.

### Restrições negativas (sempre)

NÃO incluir:
- Ramos curvos finos como em mapa mental tradicional. Use APENAS setas pintadas com pincelada.
- Setas vetoriais chapadas, geométricas e duras, sem textura.
- Selos históricos, carimbos, retratos antigos, créditos a autores ou linguistas (sem figura histórica de qualquer espécie).
- Marcas comerciais, logotipos, propagandas, marca d'água, assinaturas.
- Estilo cartoon infantil exagerado (cabeções, deformações, look Cartoon Network).
- Personagens famosos, memes, mascotes de marcas.
- Qualquer fonte serifada, manuscrita, caligráfica ou de fantasia. Apenas Roboto.
- Asteriscos, hashtags, colchetes ou marcadores markdown literais aparecendo no texto da imagem.
- Layout de tabela pesada cobrindo a página.
- Página exclusivamente textual ou exclusivamente decorativa.
- Texto pequeno e ilegível.
- Mais de sete cards principais.
- Marcadores de posição "11h", "1h", "3h", etc. — são referência interna, NUNCA renderizar como texto na imagem.
- Cores neon ou pastel chapado. Use saturação média-alta com equilíbrio.
- Texto em idioma diferente de português brasileiro.
- Saturação visual: a página deve respirar.
- Fundo de cor (creme, bege, amarelo, qualquer tom). O fundo é PURO BRANCO — a imagem é feita para impressão A4 e fundo colorido consome tinta sem necessidade.
- Texturas de papel, vinhetas, gradientes ou tonalizações no fundo. Branco chapado total.

---

## PARTE B — SLOTS A PREENCHER POR CAPÍTULO

### Cabeçalho do capítulo (preenche dados-base)

| Slot | Descrição | Exemplo (Adjetivo / 6º EF) |
|---|---|---|
| `{{ANO_SERIE}}` | Série + nível em inglês para o modelo | `6º ano EF (an 11-12 year old student)` |
| `{{IDADE_PERSONAGEM}}` | Idade do mascote, deve casar com o aluno-leitor | `11-12 anos` |
| `{{CONCEITO_CENTRAL}}` | Palavra única, MAIÚSCULA, no círculo | `ADJETIVO` |
| `{{FRASE_DEFINIDORA}}` | 1 linha curta em itálico abaixo do conceito | `caracteriza o substantivo` |
| `{{ELEMENTO_VISUAL_CENTRAL}}` | Cena que materializa o conceito ao lado do mascote | `mochila escolar vermelha com 4 etiquetas penduradas (pesada, nova, vermelha, resistente)` |

### Tópicos do capítulo (5 a 7 cards)

Para cada tópico do blueprint, preencha um bloco. Use 5 a 7 cards no total — menos satura pouco, mais aperta a página.

**Bloco-modelo de card** (repita N vezes):

```
CARD {{N}} — {{COR_DA_SETA}}

- LABEL DA SETA (curto, MAIÚSCULO, escrito sobre a seta): {{LABEL_SETA}}
- TÍTULO DO CARD (mesmo da seta ou variante curta): {{TITULO_CARD}}
- MINI-EXPLICAÇÃO (italic, 1 linha, opcional): {{EXPLICACAO_CURTA}}
- MINI-CENA ILUSTRADA (descrever): {{CENA_ILUSTRADA}}
- EXEMPLOS (2-3 itens, formato par/seta/sequência): {{EXEMPLOS}}
- ANOTAÇÃO ITALIC OPCIONAL (1 linha): {{ANOTACAO}}
```

**Cores disponíveis** (use uma por card, sem repetir):
electric blue, emerald green, golden yellow, coral red, grape purple, tangerine orange, dark red.

**Tipos de tópicos comuns em capítulos de gramática** (mapeie o blueprint para um deles):
- **Definição/Contraponto**: o conceito vs. classe vizinha (ex: substantivo nomeia × adjetivo caracteriza). Bom para o card de abertura.
- **Classificação semântica**: o que indica, em que se divide (qualidade, estado, origem, condição).
- **Variação lexical**: locuções, palavras compostas, prefixos/sufixos, formação.
- **Flexão de gênero**: biforme/uniforme (quando aplicável à classe).
- **Flexão de número**: singular/plural.
- **Graus/Variação semântica**: comparativo/superlativo, aumentativo/diminutivo, modo/tempo (verbo), tônica (sílaba).
- **Função/Concordância**: papel sintático (use sem jargão técnico para EF, com cuidado para EM).
- **Uso ético/Escolha consciente**: card de fechamento com versículo bíblico no canto.

### Card de fechamento (sempre presente)

O último card é sempre sobre **escolha consciente da palavra** + versículo. Preencha:

```
- LABEL DA SETA: ESCOLHA  (ou variante curta de 1 palavra)
- TÍTULO DO CARD: ESCOLHA A PALAVRA CERTA  (ou similar)
- MINI-CENA: mascote pensativo entre dois balões — um verde (palavra positiva), um vermelho (palavra negativa)
- PAR CONTRASTIVO: {{PAR_POSITIVO}} ≠ {{PAR_NEGATIVO}}  (ex: "palavra gentil ≠ palavra ofensiva")
- ANOTAÇÃO ITALIC: {{REFLEXAO_CURTA}}  (ex: "adjetivos podem evitar exageros e ofensas")
- VERSÍCULO (canto direito, Roboto Medium pequeno e discreto): {{VERSICULO}}  (ex: "Provérbios 10:9")
```

### Bloco "TEXT TO RENDER VERBATIM"

Ao final do prompt, listar TODAS as strings que devem aparecer na imagem, exatamente como devem ser renderizadas (com diacríticos, sem asteriscos). Modelo:

```
**TEXT TO RENDER VERBATIM**

Render every string below exactly as written, with all diacritics intact. Do not paraphrase, translate, abbreviate or substitute any of these strings.

Centro:
- {{CONCEITO_CENTRAL}}
- {{FRASE_DEFINIDORA}}
- (palavras das etiquetas/objeto central)

Setas (escritas sobre as próprias setas):
- {{LABEL_SETA_1}}
- {{LABEL_SETA_2}}
- ... (até 7)

Card 1:
- (todas as strings que aparecem nesse card)

Card 2:
... e assim por diante para cada card.

Card de fechamento:
- {{VERSICULO}}
```

---

## Adaptações por tipo de capítulo de Português

O esqueleto acima é otimizado para **análise linguística** (classes de palavras, sintaxe, morfologia). Para outros tipos, ajustar:

### Produção textual (gêneros)
- Conceito central = nome do gênero (CRÔNICA, CARTA, DISSERTAÇÃO, RELATO).
- Cards típicos: estrutura, finalidade, marcas linguísticas, exemplos de circulação, dicas de escrita, critérios de avaliação, fechamento ético.
- Card central pode ser um caderno aberto ou tela com texto sendo escrito.

### Literatura (Português 2)
- Conceito central = movimento ou autor (ROMANTISMO, MACHADO DE ASSIS).
- Cards típicos: contexto histórico, características estéticas, autores principais, obras-âncora, temas, comparações com movimento anterior, fechamento ético.
- Substituir "mascote estudante" por elemento da época (livro antigo, pena, paisagem) — manter mascote em UM card como leitor.

### Alfabetização (1º-3º EF)
- Conceito central = unidade linguística simples (SÍLABA, FONEMA, PALAVRA).
- Cards reduzidos a 4-5, exemplos amplamente visuais, texto mínimo.
- Mascote menor (criança 6-8 anos), letras grandes, paleta um pouco mais saturada.
- Versículo opcional, mais focado no encantamento com a língua.

---

## Validações antes de gerar

Antes de rodar `gerar.py`:
1. Conferir diacríticos em todas as strings da seção "TEXT TO RENDER VERBATIM".
2. Conferir que cada label de seta corresponde ao título do card de destino.
3. Conferir que a contagem de cards é entre 5 e 7.
4. Conferir que o versículo bíblico é coerente com o tema do capítulo.
5. Conferir que os exemplos são adequados à idade do leitor (sem jargão técnico em EF; profundidade adequada em EM).
6. Conferir que o mascote tem idade compatível com o leitor.

## Iteração esperada

A primeira rodada já costuma sair boa. Pequenos defeitos comuns que pedem v2/v3:
- Setas trocando de destino → reforçar a regra de pareamento no prompt.
- Marcadores literais "11h"/"1h" sendo desenhados → reforçar restrição negativa.
- Pódio do superlativo em ordem olímpica (2-1-3) → exigir explicitamente "ascending left-to-right (1, 2, 3)".
- Mochila central com etiquetas ilegíveis → aumentar tamanho do mascote/objeto.
- Página apertada → reduzir cards de 7 para 5-6 ou pedir mais respiro explícito.

---

## Referência canônica

- Estética e vivacidade: `saida/Portugues/6ano/Prototipo-Adjetivo/adjetivo-v8.png` (prompt: `prompts/Portugues/6ano/Prototipo-Adjetivo/adjetivo-v8.md`)
- Fundo branco para impressão A4: `saida/Portugues/4ano/Unidade-4-Verbos/Cap2-concordancia-verbal-v2.png` (prompt: `prompts/Portugues/4ano/Unidade-4-Verbos/Cap2-concordancia-verbal-v2.md`)

Sempre que invocar este template para um novo capítulo, abrir essas duas referências ao lado para inspirar a estética concreta.
