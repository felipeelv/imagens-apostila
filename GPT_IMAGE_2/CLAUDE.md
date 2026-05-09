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

**Unidade 04 — INTEGRIDADE**:
- ✅ 6º ano EF2 (`saida/Apostila/Integridade-6ano/`) — 6 páginas
- ⏳ 1ª série EM — pendente
- ⏳ 2ª série EM — pendente

Unidades futuras esperadas: outras dimensões de "Vida e Propósito" (caráter, comunidade, vocação, etc.).

---

## Convenções deste projeto

- Sempre responder em **português brasileiro**.
- Sempre confirmar paleta/tipografia/estilo antes de uma série nova.
- Para cada nova unidade:
  1. Receber o conteúdo bruto da unidade (markdown estruturado).
  2. Dividir em 6 páginas (abertura + 4 seções + personagem/aplicação).
  3. Definir paleta (mantém a da série já estabelecida) + frase de impacto por página.
  4. Escrever 6 prompts em inglês detalhado seguindo o template do diretório.
  5. Disparar 5 em paralelo + 1 sequencial (rate limit).
  6. Abrir cada PNG no Read e validar contra a referência.

- Versões iterativas: salvar como `pagina-XX-tema-v2.png`, `v3.png`. Não sobrescrever a aprovada.

---

## Para continuar em outro computador

1. Sincronizar a pasta `GPT_IMAGE_2/` (Git, Drive, etc.).
2. Confirmar `.env` com `OPENAI_API_KEY` válida.
3. Rodar `uv` (instala dependências automaticamente via PEP 723 no header de `gerar.py`).
4. Ler **MEMORY.md** para o estado mais recente das unidades + observações por página.
5. Pedir ao Claude: *"continuar a apostila Vida e Propósito"* — ele consulta CLAUDE.md + MEMORY.md.
