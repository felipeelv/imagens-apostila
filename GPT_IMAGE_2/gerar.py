# /// script
# requires-python = ">=3.10"
# dependencies = ["openai", "python-dotenv", "pillow"]
# ///
from __future__ import annotations

import argparse
import base64
import os
import sys
from io import BytesIO
from pathlib import Path

from dotenv import load_dotenv
from PIL import Image


PASTA_MODELO = Path(__file__).resolve().parent
RAIZ = PASTA_MODELO.parent
MODELO = "gpt-image-2"


def carregar_prompt(caminho: Path) -> str:
    if not caminho.exists():
        raise RuntimeError(f"Prompt nao encontrado: {caminho}")
    return caminho.read_text(encoding="utf-8").strip()


def salvar_png(caminho: Path, dados: bytes) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    try:
        imagem = Image.open(BytesIO(dados))
        imagem.save(caminho, format="PNG")
    except Exception:
        caminho.write_bytes(dados)
    print(f"Imagem salva em: {caminho}")


def gerar(prompt: str, saida: Path, tamanho: str) -> None:
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY nao encontrada no .env da raiz.")

    client = OpenAI(api_key=api_key)
    resposta = client.images.generate(model=MODELO, prompt=prompt, size=tamanho)
    imagem_base64 = resposta.data[0].b64_json
    salvar_png(saida, base64.b64decode(imagem_base64))


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Gerador isolado para GPT Image 2.")
    parser.add_argument("texto", nargs="?", default=None,
                        help="Prompt inline. Se omitido, usa --prompt ou modelos/prompt.txt.")
    parser.add_argument("--prompt", default=str(PASTA_MODELO / "modelos" / "prompt.txt"))
    parser.add_argument("--saida", default=str(PASTA_MODELO / "saida" / "imagem.png"))
    parser.add_argument("--tamanho", default="1024x1536")
    return parser


def main() -> int:
    env_local = PASTA_MODELO / ".env"
    load_dotenv(env_local if env_local.exists() else RAIZ / ".env", override=True)
    args = construir_parser().parse_args()
    prompt = args.texto if args.texto else carregar_prompt(Path(args.prompt))
    gerar(prompt, Path(args.saida), args.tamanho)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        raise SystemExit(1)
