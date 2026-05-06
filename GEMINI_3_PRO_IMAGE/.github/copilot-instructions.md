# Instruções para sessões Copilot (repositório: Gemini 3 Pro Image)

Resumo rápido
- Projeto simples em Python para gerar imagens pedagógicas usando o modelo gemini-3-pro-image-preview via API Generative Language.

Build / test / lint
- Não há build, test suite ou linter configurados neste repositório.
- Dependências (declaradas no topo de gerar.py): Python >=3.10, requests, python-dotenv, pillow
  - Instalação rápida: pip install requests python-dotenv pillow

Como executar (exemplos do README)
- Usando um runner (documentado):
  uv run gerar.py --prompt prompts/minha-imagem.md --saida saida/minha-imagem.png
- Prompt inline:
  uv run gerar.py "Crie uma pagina A4 vertical de atividades de Matematica sobre fracoes para o 5o ano."
- Controlando formato/tamanho:
  uv run gerar.py --aspect-ratio 9:16 --image-size 2K
- Observações:
  - Variáveis aceitas para --aspect-ratio: 1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, 21:9
  - Valores para --image-size: 1K, 2K, 4K

Arquitetura em alto nível
- Entrypoint: gerar.py
  - Carrega .env (procura em ./ ou em PASTA_MODELO/.env), extrai GEMINI_API_KEY
  - Recebe prompt por arquivo (--prompt) ou inline (argumento posicional)
  - Monta payload JSON com generationConfig (responseModalities: TEXT, IMAGE)
  - Chama endpoint: https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent
  - Extrai imagem do campo inlineData/inline_data (base64) e salva PNG em saida/
  - Suporta opção --google-search que adiciona ferramentas ao payload
- Estrutura de pastas relevante:
  - prompts/: arquivos .md com prompts reais (cada .md = um prompt de imagem)
  - prompt.md: modelo de prompt pedagógico (sempre editar antes de gerar)
  - saida/: imagens resultantes

Convenções e detalhes específicos do repositório
- prompt.md é um template com a linha literal `SUBSTITUA ESTA LINHA`. O script carregar_prompt() reprova prompts que contenham esse texto — editar antes de usar.
- Variável de ambiente esperada: GEMINI_API_KEY (arquivo .env na raiz ou .env local em PASTA_MODELO)
- Cabeçalho de gerar.py declara dependências e versão mínima Python — manter compatibilidade com >=3.10
- Nome do modelo e endpoint estão hard-coded em gerar.py (MODELO = "gemini-3-pro-image-preview"). Atualizar apenas com cuidado.
- Extração de imagem: o script procura por `inlineData` ou `inline_data` em `candidates[].content[].parts[]` — se a API retornar apenas texto, o script montará um erro explicativo com o texto retornado.
- Para adicionar um novo prompt: copiar prompt.md → prompts/nome.md, editar removendo o placeholder e preencher campos (disciplina, ano, objetivo, texto, composição visual).

Arquivos de atenção ao modificar
- gerar.py: alterações afetam autenticação, payload e parsing de resposta — testar com uma requisição real após mudanças
- prompt.md e arquivos em prompts/: pequenas alterações no template podem quebrar verificações de presença do placeholder

Integração com outros arquivos de assistente AI
- Não foram encontrados arquivos específicos de outras ferramentas de assistente (CLAUDE.md, .cursorrules, AGENTS.md, etc.) neste repositório.

Notas finais
- O repositório não define testes/linter; se for desejável, sugerir adicionar requirements.txt/pyproject.toml e um workflow CI para instalar dependências e rodar checagens.

