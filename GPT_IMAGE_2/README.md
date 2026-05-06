# GPT Image 2

Pasta isolada para gerar imagens com GPT Image 2.

## Como gerar

Uso recomendado com prompt inline:

```bash
uv run gerar.py "prompt da imagem aqui"
```

Se voce nao passar prompt inline, o script usa o arquivo local:

```bash
uv run gerar.py
```

Nesse caso, preencha antes o arquivo `modelos/prompt.txt`.

A pasta ja possui um `.env` local com `OPENAI_API_KEY`.
As dependencias ficam declaradas no topo de `gerar.py` via PEP 723, entao nao ha `requirements.txt`.

## Modelos YAML locais

Esta pasta tambem possui modelos YAML proprios, ajustados para este provider:

- `modelos/projeto.yaml`: modelo generico.
- `modelos/projeto_infografico.yaml`: infografico.
- `modelos/projeto_hq.yaml`: HQ/paginas.
- `modelos/projeto_poster_card.yaml`: poster, card, capa ou thumbnail.
- `modelos/projeto_carrossel.yaml`: carrossel.

Use esses YAMLs como referencia de briefing e estrutura. O arquivo `modelos/prompt.txt` e o prompt direto usado por `gerar.py` quando nenhum prompt inline e informado.
