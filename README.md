# Imagens Apostila — Colégio Eleve

Pipeline de geração de imagens pedagógicas para a apostila do Colégio Eleve usando dois modelos isolados:

- **GEMINI_3_PRO_IMAGE/** — geração via Google Gemini 3 Pro Image (`uv run gerar.py --aspect-ratio 3:4 --image-size 2K`)
- **GPT_IMAGE_2/** — geração via OpenAI GPT Image 2 (`uv run gerar.py --tamanho 1024x1536`)

Cada pasta é um projeto isolado com `.env` próprio (API key), `gerar.py` (script de geração), `prompts/` (prompts por disciplina) e `saida/` (PNGs gerados).

## Convenção de organização

```
<MODELO>/
├── gerar.py              ← script
├── .env                  ← API key (NÃO versionado)
├── prompts/
│   ├── _templates/<disciplina>/   ← templates canônicos
│   └── <Disciplina>/<ano>/Unidade-<N>-<Nome>/Cap<N>-<slug>-v<N>.md
└── saida/                ← espelha estrutura de prompts/
    └── <Disciplina>/<ano>/Unidade-<N>-<Nome>/Cap<N>-<slug>-v<N>.png
```

## Templates canônicos validados

- **Português 1 (Análise Linguística):** mapas mentais EF1 / EF2 / EM em `GEMINI_3_PRO_IMAGE/prompts/_templates/portugues/`
- **Ciências (4º-9º ano EF):** resumo visual de capítulo em `prompts/_templates/ciencias/_TEMPLATE-resumo-capitulo-EF2.md`

## Status de produção

### Ciências — páginas-resumo de fechamento de capítulo
- ✅ 6º ano · Unidade 4 (Transformações da Matéria) — 3 capítulos
- ✅ 5º ano · Unidade 4 (Corpo Humano) — 4 capítulos
- ✅ 4º ano · Unidade 4 (Microrganismos) — 3 capítulos

### Português 1 — mapas mentais por capítulo
- ✅ 4º, 5º, 6º, 7º, 8º, 9º ano EF · Unidade 4 (várias)
- ✅ 1ª, 2ª, 3ª série EM · Unidade 4

## Como gerar

### Pré-requisitos
- `uv` instalado (gerencia dependências Python via PEP 723)
- `.env` configurado em cada pasta com a API key correspondente

### Comando padrão
```bash
cd <MODELO>/
uv run gerar.py \
  --prompt prompts/<Disciplina>/<ano>/Unidade-<N>-<Nome>/Cap<N>-<slug>-v<N>.md \
  --saida saida/<Disciplina>/<ano>/Unidade-<N>-<Nome>/Cap<N>-<slug>-v<N>.png \
  --aspect-ratio 3:4 --image-size 2K   # gemini
  # ou
  --tamanho 1024x1536                  # gpt image 2
```

## Padrões editoriais

- Páginas-resumo de Ciências usam estrutura modular de 5 zonas, sem chip de série/ano/unidade, sem retrato de cientista, com IDEIA-CHAVE redesenhada a cada capítulo e versículo VP rotacionado entre os âncoras da unidade.
- Para EF1 (4º-5º ano), linguagem mais simples e ilustrações mais friendly. Para EF2 (6º-9º ano), vocabulário técnico introdutório e identidade visual mais editorial.

---
Mantido por **Felipe Rosa** · Colégio Eleve · [felipe.rosa@colegioeleve.com.br](mailto:felipe.rosa@colegioeleve.com.br)
