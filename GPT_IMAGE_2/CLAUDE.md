# CLAUDE.md — Apostila "Vida e Propósito" / Pipeline GPT Image 2

Guia para Claude Code (claude.ai/code) ao trabalhar neste diretório.

---

## Contexto do projeto

Pipeline de geração de páginas A4 ilustradas para a apostila **"Vida e Propósito"** do **Colégio Eleve**, gerada via API OpenAI `gpt-image-2`. Cada página é uma diagramação editorial-infográfica completa — título + texto + ilustração + cards + ícones + rodapé — renderizada como PNG 1024×1536 (proporção próxima a A4).

A apostila cobre múltiplas unidades temáticas (Identidade, Integridade, etc.), cada uma adaptada para 3 faixas etárias: **6º ano EF2**, **1ª série EM**, **2ª série EM**.

---

## Stack e como rodar

- **Modelo**: `gpt-image-2` (OpenAI Images API)
- **Linguagem**: Python (script `gerar.py`, dependências PEP 723 via `uv`)
- **Tamanho padrão**: `1024x1536` (A4 vertical aproximado)
- **`.env`** local na raiz desta pasta com `OPENAI_API_KEY`

Comando para gerar uma página:

```bash
cd "/Users/feliperosa/Desktop/Pastas Projetos/Imagens apostila./GPT_IMAGE_2"
uv run gerar.py --prompt "prompts/Apostila/<unidade>-<serie>/<arquivo>.md" \
                --saida "saida/Apostila/<unidade>-<serie>/<arquivo>.png" \
                --tamanho 1024x1536
```

**Rate limit OpenAI**: 5 imagens/min. Disparar até 5 em paralelo (`run_in_background: true`); a 6ª espera ~60s.

---

## Estrutura de pastas

```
GPT_IMAGE_2/
├── gerar.py                      # script gerador
├── .env                          # OPENAI_API_KEY
├── prompts/
│   └── Apostila/
│       ├── Identidade-2EM/       # 6 prompts .md
│       ├── Identidade-1EM/
│       ├── Identidade-6ano/
│       └── Integridade-6ano/
└── saida/
    └── Apostila/                 # mesma estrutura, com PNGs
```

Cada unidade × série tem **6 páginas A4** (abertura + 4 conceituais + personagem bíblico/aplicação).

---

## Identidade visual — padrão geral

**Estilo**: infográfico editorial moderno premium. Referências: SM Educação / Moderna PNLD premium, Kinfolk, NYT infographics. Sans-serif bold (Montserrat / Inter), cards modulares pastéis com ícones de linha fina, foto-realista do estudante + ilustrações editoriais leves.

**Estrutura fixa de toda página**:
1. Header strip com dot colorido + linha + 4 ícones em frame tracejado
2. Título massivo sans-serif (palavra-chave em cor primária + subtítulo em cor de acento)
3. Card de pergunta-âncora (lavender/sky pastel + "?")
4. Texto em coluna esquerda (2 parágrafos curtos com 1 frase em destaque colorida)
5. Mini bloco-conceito (frase de impacto na cor de acento)
6. Lista de 3 ícones em cards pastel
7. Hero image central/direita (foto + elementos infográficos sobrepostos)
8. Card lateral "VOCÊ SABIA?" com estatística
9. Pullquote bíblico em banda lavanda/cor pastel
10. Card "PARA CONVERSAR" / "PARE E PENSE" com ilustração + perguntas
11. Bottom band: 4 módulos com ícones + frase de impacto em uppercase
12. Footer fino: "UNIDADE XX — TEMA" + número da página

---

## Paletas por série (NÃO MISTURAR ENTRE SÉRIES)

### 2ª série EM — paleta Navy + Roxo
- Background: `#FAFAFA`
- Primary navy: `#1B2D5E`
- Deep purple: `#6B4FA8`
- Lavender card bg: `#E5DEF5`
- Light blue card bg: `#DCE6F5`
- Orange accent: `#F47B2A`
- Graphite: `#1F1B17`

### 1ª série EM — paleta Verde-petróleo + Terracota
- Background cream: `#F8F4ED`
- Forest green: `#1F4D44`
- Terracotta: `#D26B47`
- Mint card bg: `#DCEAE3`
- Peach card bg: `#F8E1CE`
- Ocre accent: `#E1B548`
- Graphite: `#1F1B17`

### 6º ano EF2 — paleta Cosmos (azul + amarelo + coral)
- Background cream: `#FAFAF2`
- Cosmic blue: `#1F4A82`
- Sun yellow: `#F2B538`
- Coral: `#E87455`
- Sky pastel card bg: `#DCE9F2`
- Cream-yellow card bg: `#FAEFD0`
- Graphite: `#1F1B17`

### 7º ano EF2 — paleta Slate + Magenta + Mostarda (tech-editorial, composição em camadas)
- Background off-white: `#F7F5F0`
- Primary slate (azul-grafite): `#2C3E50`
- Magenta vibrante: `#C44A6E`
- Mustard accent: `#D4A02D`
- Slate pastel card bg: `#DCE3EA`
- Rose pastel card bg: `#F5E1E8`
- Graphite: `#1F1B17`
- **Direção visual extra**: composição em camadas explícita — fotografia recortada + color blocks + chips tipográficos + glitch decoration. Maior densidade visual que 6º ano.

**Todas as séries**: tipografia ALL SANS-SERIF (sem serif). Light gray dividers `#DCDCDC`.

---

## Adaptação por idade

| Série | Tom | Densidade de texto | Visual |
|---|---|---|---|
| **6º ano** | direto, 1ª pessoa, frases curtas | mais respiro, texto curto | mais lúdico mas premium, ícones um pouco mais bold |
| **1ª EM** | maduro, conceitual leve | médio | editorial-pop sofisticado |
| **2ª EM** | universitário-light, denso | maior densidade ok | editorial-pop denso, mais conceitual |

Personagens bíblicos (Ester, Daniel, etc.) **devem usar a paleta da unidade** — nunca bordô/dourado tradicionais. Ester com vestes em roxo (2EM) / verde (1EM) / coral (6ano). Daniel idem.

---

## Aprendizados / armadilhas conhecidas

- **Texto longo borra**: hashtags e legendas pequenas dão glitch. Manter blocos de texto curtos e sem hashtags.
- **Garbled text**: explicitar no prompt "every visible word must be one of the words specified above and spelled correctly in Portuguese. NO garbled letters."
- **Versículos bíblicos**: parafraseios curtos rendem melhor que citações longas.
- **Personagens bíblicos**: pedir ilustração editorial painterly, NUNCA "religious art classical" (vira clichê).
- **Foto de teen**: pedir "racially diverse Brazilian preteen/teenager" para resultado natural.
- **Composições com mockup de redes**: cards "VERSÃO EDITADA"/"VERSÃO REAL" funcionam, mas evitar excesso de UI Instagram (curte, hashtag, etc.).
- **Acentos PT-BR**: às vezes saem errados ("constroi", "socíais"). Não há solução total — verificar visualmente.

---

## Status atual da apostila

**Unidade 03 — IDENTIDADE**:
- ✅ 6º ano EF2 (`saida/Apostila/Identidade-6ano/`) — 6 páginas
- ✅ 1ª série EM (`saida/Apostila/Identidade-1EM/`) — 6 páginas
- ✅ 2ª série EM (`saida/Apostila/Identidade-2EM/`) — 6 páginas

**Unidade 04 — INTEGRIDADE** (em produção · 2026-05-09):
- ✅ 6º ano EF2 (`saida/Apostila/Integridade-6ano/`) — 6 páginas
- ✅ 7º ano EF2 (`saida/Apostila/Integridade-7ano/`) — 6 páginas (paleta Slate+Magenta+Mostarda)
- ✅ 2º ano EF1 (`saida/Apostila/Integridade-2ano/`) — 8 páginas (paleta Cuidado & Coragem)
- ✅ 3º ano EF1 (`saida/Apostila/Integridade-3ano/`) — 8 páginas (3D Pixar/Encanto)
- ✅ 4º ano EF1 (`saida/Apostila/Integridade-4ano/`) — 6 páginas (3D cartunizado Disney Channel)
- ✅ 5º ano EF1 (`saida/Apostila/Integridade-5ano/`) — 6 páginas (Marvel cel-shaded comic)
- ⏳ 1ª série EM — pendente
- ⏳ 2ª série EM — pendente

Unidades futuras esperadas: outras dimensões de "Vida e Propósito" (caráter, comunidade, vocação, etc.).

---

## Convenções deste projeto (workflow atualizado em 2026-05-09)

- Sempre responder em **português brasileiro**.
- **O usuário sempre envia o conteúdo bruto** da unidade. Nunca derivar conteúdo sozinho.
- **Total de páginas da unidade é sempre PAR** (6, 8, 10) incluindo a capa. Antes de produzir, propor a divisão e aguardar aprovação.
- **Página 1 é sempre a CAPA** com 3 elementos: título + texto introdutório + box "Para Conversar". Sem indicação textual de "Unidade XX".
- **Texto VERBATIM do conteúdo enviado** — não cortar, não parafrasear, não simplificar bullets. Reduzir font size se preciso para caber.
- **Produção uma página por vez** com aprovação explícita antes de avançar (substitui o lote 5+1 antigo). Iterar com `-v2`, `-v3` na mesma página enquanto não estiver aprovada.
- **Estabelecer padrão de série na primeira unidade**: paleta + estilo + identidade visual aprovados na primeira capa valem para todas as outras unidades dessa série/ano.
- **Continuidade visual com a apostila como um todo** — DNA editorial-infográfico mantido, ajustando densidade/estilo/lúdico por idade.
- Versões iterativas: salvar como `pagina-XX-tema-v2.png`, `v3.png`. Não sobrescrever a aprovada.

## Estilo visual por série/ano (estabelecido na U4 2026-05-09)

Cada série/ano tem **paleta distinta** + **estilo de hero distinto** que evolui com a idade. Resumo:

| Série/Ano | Paleta | Estilo do hero | Tema visual |
|---|---|---|---|
| 2º ano EF1 (~7 anos) | sky-blue + warm-orange + leaf-green ("Cuidado & Coragem") | Foto-realista premium friendly | Pictogramas de segurança |
| 3º ano EF1 (~8 anos) | teal turquesa + coral salmão + sunny gold ("Integridade Investigativa") | 3D Pixar/Encanto realista | Pictogramas de ciência (lupa, microscópio) |
| 4º ano EF1 (~9 anos) | deep plum + mustard + sage ("Caráter Maduro") | 3D cartunizado Disney Channel/Bluey | Pictogramas mistos ciência+construção (tijolo, plumb-line) |
| 5º ano EF1 (~10 anos) | deep slate blue + coral red + mint green ("Vida Inteira") | **Marvel cel-shaded comic** (Spider-Verse / What If...?) | Pictogramas do corpo humano (coração, pulmão, cérebro) |
| 6º ano EF2 (~11-12 anos) | Cosmos (azul cósmico + amarelo + coral) | Foto-realista premium | Ícones diversos |
| 7º ano EF2 (~12-13 anos) | Slate + Magenta + Mostarda | Foto-realista + composição em camadas | Tech-editorial denso |
| 1ª série EM (~15 anos) | Verde-petróleo + Terracota | Foto-realista editorial | Editorial-pop sofisticado |
| 2ª série EM (~16 anos) | Navy + Roxo | Foto-realista denso | Editorial-pop conceitual |

**Personagens bíblicos** (Daniel, Davi, Ester) sempre em **vestes nas cores da unidade da série** — nunca bordô/dourado clássicos.

## Componentes-sticker (design system, estabelecido na U4 2ano EF1)

Boxes recorrentes são **componentes-sticker** com identidade fixa, repetidos idênticos em todas as páginas/unidades como peças coladas reconhecíveis (drop shadow + tilt + washi-tape ou decoração específica). Lista:

1. **VOCÊ SABIA?** — sky-pastel base + sky-blue pill + ícone "?" em circle + washi-tape
2. **PENSE UM POUCO** — mint-pastel + leaf-green pill + nuvem de pensamento + 3 bolinhas escalonadas
3. **PARE E PENSE** — gold-pastel + sunny-gold pill + ícone stop-hand + washi-tape
4. **PARA CONVERSAR** — peach-pastel full-width + warm-orange pill + balão de fala + ilustração lateral fixa de 2 crianças no banco
5. **DA HISTÓRIA PRA MINHA VIDA** — peach-pastel full-width + handshake icon + lista numerada em circles (P-personagem-fim)
6. **NO FINAL DAS CONTAS** — sky-pastel full-width + banner-style header com notches + estrela + texto-amarra final (P-fechamento)

Paleta dos stickers se adapta à paleta da série, mas estrutura/forma/ícone permanecem.

No 5º ano EF1 (Marvel cel-shaded), os stickers ganharam **bold black ink outline ~3px + spike de speech-bubble + lightning-bolt mark + halftone benday dots** mantendo a identidade.

## Regras invioláveis (estabelecidas em 2026-05-09)

- ❌ **NO header strip** com dot+linha no topo-esquerda (rejeitado a partir do 4º ano EF1)
- ❌ **NO frame tracejado com pictogramas** no topo-direita (mesmo motivo)
- ❌ **NO numeração de tópicos/subtópicos** ("1.", "1.1") visível nas páginas — só pra organização interna do conteúdo
- ❌ **NO uniforme escolar** (polo, gola colorida, logo) nos personagens — usar roupas comuns (camiseta lisa, blusa, jeans)
- ❌ **NO caracterização folclórica** dos personagens (sem brincos étnicos, vestido típico, cocar) — diversidade pela pele/cabelo/traços faciais com aparência urbana contemporânea
- ❌ **NO setas/conectores** ligando texto a elementos da imagem — integração só por overlap de cards e pictogramas na fronteira
- ❌ **NO título massivo** — proporcional para A4 impresso (~36pt equivalente, NÃO "extreme bold dominant")
- ❌ **NO texto truncado** — manter bullets verbatim do conteúdo enviado, reduzir fonte se preciso
- ❌ **NO crowded layout** — espaçamento generoso entre boxes, cards nunca encostando

---

## Para continuar em outro computador

1. Sincronizar a pasta `GPT_IMAGE_2/` (Git, Drive, etc.).
2. Confirmar `.env` com `OPENAI_API_KEY` válida.
3. Rodar `uv` (instala dependências automaticamente via PEP 723 no header de `gerar.py`).
4. Ler **MEMORY.md** para o estado mais recente das unidades + observações por página.
5. Pedir ao Claude: *"continuar a apostila Vida e Propósito"* — ele consulta CLAUDE.md + MEMORY.md.
