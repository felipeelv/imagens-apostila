# Contexto padrão — GPT Image 2

Esta pasta é independente. Ela contém o necessário para gerar uma imagem com GPT Image 2:

- `gerar.py`: script de geração.
- `prompt.txt`: prompt exclusivo deste modelo.
- `.env`: chave `OPENAI_API_KEY`.
- `requirements.txt`: dependências Python.
- `saida/`: pasta de destino criada automaticamente.

## Perfil de prompt recomendado

GPT Image 2 tende a funcionar melhor com instruções literais, diretas e sem contradição.

Use:

- descrição objetiva da imagem final;
- formato e proporção;
- estilo visual;
- lista exata de textos permitidos;
- restrições claras sobre o que não criar.

Evite:

- notas técnicas de API dentro do prompt;
- excesso de contexto histórico;
- regras longas que competem entre si.
