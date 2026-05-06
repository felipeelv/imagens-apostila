# Gemini 3 Pro Image

Pasta simples para gerar imagens de conteudo pedagogico com Gemini 3 Pro Image.

## Arquivos principais

- `prompt.md`: modelo padrao de prompt pedagogico.
- `prompts/`: coloque aqui os prompts reais de cada imagem.
- `gerar.py`: script de geracao.
- `.env`: chave `GEMINI_API_KEY`.
- `saida/`: imagens geradas.

## Como usar

Copie `prompt.md` para `prompts/`, edite o novo arquivo e rode:

```bash
uv run gerar.py --prompt prompts/minha-imagem.md --saida saida/minha-imagem.png
```

Ou passe um prompt direto no terminal:

```bash
uv run gerar.py "Crie uma pagina A4 vertical de atividades de Matematica sobre fracoes para o 5o ano."
```

Para controlar formato e tamanho:

```bash
uv run gerar.py --aspect-ratio 9:16 --image-size 2K
```

Valores aceitos pela API para `--aspect-ratio`: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `9:16`, `16:9`, `21:9`.

Valores aceitos para `--image-size`: `1K`, `2K`, `4K`.

## Prompt

A documentacao recomenda descrever a imagem de forma clara e narrativa. Evite apenas listas de palavras-chave. Para conteudo pedagogico, informe disciplina, ano/serie, objetivo de aprendizagem, formato visual, texto que deve aparecer, nivel de leitura e restricoes.
