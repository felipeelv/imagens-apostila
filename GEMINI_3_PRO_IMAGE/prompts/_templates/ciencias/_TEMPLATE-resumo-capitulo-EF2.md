# Template Canônico — Resumo Visual de Capítulo (Ciências EF2)

Documento de referência para gerar páginas de **resumo visual de capítulo** para Ciências do 6º ao 9º ano EF (estrutura adaptável a Biologia EF2). Cada página vai na ÚLTIMA página do capítulo e funciona como resumo explicativo para o aluno revisar antes da prova.

Versão validada: **v7 — Cap 1 (Transformações Físicas e Químicas)** — `prompts/Ciencias/6ano/Unidade-4-Transformacoes-da-Materia/Cap1-transformacoes-fisicas-e-quimicas-v7.md` (gerado em GPT_IMAGE_2). Estilo aprovado pelo usuário em 2026-05-05.

---

## PARTE A — IDENTIDADE FIXA (não negociar a cada capítulo)

### Aspect ratio e canvas
- **3:4 portrait** (A4 vertical) no Gemini · `1024x1536` no GPT Image 2
- Fundo: **branco puro #FFFFFF**, flat, sem textura, sem grain, sem cream/yellow tint, sem vinheta

### Paleta canônica
- Cor primária A (cool / "calmo, mesmo"): teal #4A8AA8
- Cor primária B (warm / "ativo, novo"): terracota #D67340
- Accent gold: mustard #F0B935
- Pale fills: #E6F0F2 (teal claro) e #FAE8DD (terracota claro)
- Texto: charcoal #1F2937 (nunca preto puro)
- Divisores sutis: cinza claro #E5E5E5

### Tipografia
- **Título principal**: condensed slab-serif uppercase com sutil ink-press (NÃO grunge pesado), charcoal — UMA palavra inteira, nunca quebrada
- **Subtítulo**: serif italic, terracota
- **Ribbon banner tagline**: white sans-serif Black uppercase, sobre faixa terracota com pontas dobradas
- **Headers de seção**: sans-serif Black uppercase, charcoal
- **Labels de conceito** (TRANSFORMAÇÃO FÍSICA / etc): sans-serif Black uppercase, white em card colorido sólido
- **Explicações**: sans-serif regular, charcoal, tamanho confortável para 11-12 anos
- **Exemplos**: serif italic small, cinza médio, prefixo "Ex.:"
- **Banner IDEIA-CHAVE**: sans-serif Black uppercase, white em terracota
- **Versículo**: serif italic small, deep teal

### Estilo visual
- Semi-flat friendly didactic illustration
- NÃO photorealistic, NÃO cartoon childish, NÃO painterly editorial sofisticado
- Ícones rounded friendly recognizable
- Espaçamento generoso, hierarquia óbvia

---

## PARTE B — ESTRUTURA DE 5 ZONAS (esqueleto)

### Zona 1 — Cabeçalho ancorado (~12% altura)
1. Título do capítulo (slab-serif distressed leve)
2. Subtítulo (serif italic terracota)
3. **Ribbon banner terracota** com pontas dobradas + tagline em uppercase

### Zona 2 — Conceito-âncora dual com explicação (~26% altura)
- Split horizontal em dois meios separados por linha cinza fina vertical
- LEFT (pale teal #E6F0F2): ilustração + label sólido teal + explicação 2 linhas
- RIGHT (pale terracota #FAE8DD): ilustração + label sólido terracota + explicação 2 linhas

### Zona 3 — Itens enumerados com explicação (~40% altura)
- Header centralizado (sans-serif Black uppercase)
- Subtítulo em italic charcoal
- Linha horizontal de N cards (4 ou 5) em retângulo vertical
- Cada card: badge circular teal+ring mostarda + label uppercase + explicação 1-2 linhas + exemplo italic
- Nota integrada italic centralizada abaixo da linha de cards

### Zona 4 — Banner IDEIA-CHAVE DO CAPÍTULO (~12% altura)
- Escudo deep teal com estrela mostarda à esquerda + texto "IDEIA-CHAVE / DO CAPÍTULO"
- Faixa terracota à direita com 2 linhas de síntese em uppercase Black

### Zona 5 — Versículo VP (~5% altura)
- Linha terracota fina horizontal
- Referência bíblica (uppercase Black charcoal) + reflexão (italic small deep teal)

---

## PARTE C — SLOTS A PREENCHER POR CAPÍTULO

| Slot | Descrição | Ex Cap 1 (Transf.) | Ex Cap 2 (Sintéticos) |
|---|---|---|---|
| `{{TÍTULO}}` | Palavra-chave gigante uppercase | TRANSFORMAÇÕES | MATERIAIS |
| `{{SUBTÍTULO}}` | Complemento serif italic | Físicas e Químicas | Sintéticos |
| `{{TAGLINE}}` | Tagline na ribbon | O QUE MUDA NA MATÉRIA · COMO RECONHECER | O QUE SÃO · ONDE ESTÃO NO DIA A DIA |
| `{{CONCEITO_A_LABEL}}` | Label do conceito A | TRANSFORMAÇÃO FÍSICA | MATERIAL NATURAL |
| `{{CONCEITO_A_VISUAL}}` | Ilustração simbólica A | ovo cracked | madeira/algodão |
| `{{CONCEITO_A_DESC}}` | Explicação 2 linhas A | "Muda só de aparência..." | "Vem direto da natureza..." |
| `{{CONCEITO_B_LABEL}}` | Label do conceito B | TRANSFORMAÇÃO QUÍMICA | MATERIAL SINTÉTICO |
| `{{CONCEITO_B_VISUAL}}` | Ilustração simbólica B | ovo cozido em metade | garrafa PET |
| `{{CONCEITO_B_DESC}}` | Explicação 2 linhas B | "Vira substância nova..." | "Foi criado pelo ser humano..." |
| `{{ITENS_HEADER}}` | Header da zona 3 | AS 5 EVIDÊNCIAS DE TRANSF. QUÍMICA | OS 4 TIPOS DE MATERIAIS SINTÉTICOS |
| `{{ITENS_SUBTITLE}}` | Subtítulo da zona 3 | Sinais que indicam... | Onde a química está... |
| `{{ITENS}}` | Array N=4 ou 5 itens | 5 evidências (cor/gás/temp/cheiro/precipitado) | 4 tipos (plásticos/tecidos/borrachas/construção) |
| Cada item tem: | `{ICON, LABEL, EXPLANATION, EXAMPLE}` | | |
| `{{NOTA_INTEGRADA}}` | Italic abaixo dos cards | "Uma evidência sozinha pode enganar..." | "Cada material foi criado para..." |
| `{{IDEIA_CHAVE_TEXTO}}` | Síntese 2 linhas Banner | "FÍSICA OU QUÍMICA? O CRITÉRIO..." | "MATERIAL SINTÉTICO É CRIADO..." |
| `{{VERSÍCULO_REF}}` | Referência bíblica | DANIEL 6:4 | LUCAS 16:10 |
| `{{VERSÍCULO_TEXTO}}` | Reflexão 1 linha | "Integridade científica..." | "Criar matéria nova exige cuidado..." |

---

## PARTE D — RESTRIÇÕES INVIOLÁVEIS

- ❌ Fundo cream/yellow/beige — somente branco puro
- ❌ Chip/banner/label de série/ano/unidade ("CIÊNCIAS", "6º ANO", "UNIDADE 4", "CAPÍTULO 1") — NUNCA aparecer
- ❌ Retrato de cientista, biografia, "Esse foi o cara"
- ❌ Bloco "Para não esquecer" com bullets de resumo
- ❌ Pergunta-problema como gancho (card é declarativo, não pergunta)
- ❌ Drops em formato de gota com "DROPS PRA PROVA" (gimmick rejeitado)
- ❌ Cena painterly editorial complexa (rejeitado)
- ❌ Photorealismo
- ❌ Cartoon childish
- ❌ Mascote, personagem humano, figura cartoon
- ❌ Equações químicas, fórmulas moleculares, diagramas atômicos
- ❌ Drop shadows nos cards
- ❌ Ornamentos, frames decorativos
- ❌ Logo, QR code, marca de editora
- ❌ 3D extruded text, embossed, neon, glow
- ❌ Grunge pesado (apenas ink-press sutil no título)
- ❌ Comic Sans, handwriting, script
- ❌ Quebrar título em 2 palavras (manter como UMA palavra única)
- ❌ Duplicar cards/badges/labels — cada item renderizado EXATAMENTE 1 vez

---

## OBSERVAÇÃO SOBRE GEMINI VS GPT IMAGE 2

Mesmo prompt, mas execução pode variar:
- **GPT Image 2**: tipografia mais nítida, cards mais limpos, semi-flat mais "school study sheet"
- **Gemini 3 Pro Image**: mais ilustrativo, cores mais ricas, sensação editorial

Validar resultado em ambos quando estabilizar template novo.
