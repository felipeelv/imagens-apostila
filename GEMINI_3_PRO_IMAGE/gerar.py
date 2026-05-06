# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "python-dotenv", "pillow"]
# ///
from __future__ import annotations

import argparse
import base64
import os
import sys
from io import BytesIO
from pathlib import Path

import requests
from dotenv import load_dotenv
from PIL import Image


PASTA_MODELO = Path(__file__).resolve().parent
RAIZ = PASTA_MODELO.parent
MODELO = "gemini-3-pro-image-preview"


def carregar_prompt(caminho: Path) -> str:
    if not caminho.exists():
        raise RuntimeError(f"Prompt nao encontrado: {caminho}")
    prompt = caminho.read_text(encoding="utf-8").strip()
    if "SUBSTITUA ESTA LINHA" in prompt:
        raise RuntimeError(f"Edite o prompt padrao antes de gerar: {caminho}")
    return prompt


def extrair_imagem(dados: dict) -> bytes:
    textos = []
    for candidate in dados.get("candidates", []) or []:
        content = candidate.get("content") or {}
        for part in content.get("parts", []) or []:
            if part.get("text"):
                textos.append(part["text"])
            inline_data = part.get("inlineData") or part.get("inline_data")
            if inline_data and inline_data.get("data"):
                return base64.b64decode(inline_data["data"])
    extra = f" Texto retornado: {' | '.join(textos)}" if textos else ""
    raise RuntimeError(f"Gemini nao retornou imagem.{extra}")


def salvar_png(caminho: Path, dados: bytes) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    try:
        imagem = Image.open(BytesIO(dados))
        imagem.save(caminho, format="PNG")
    except Exception:
        caminho.write_bytes(dados)
    print(f"Imagem salva em: {caminho}")


def gerar(prompt: str, saida: Path, aspect_ratio: str, image_size: str, usar_google_search: bool) -> None:
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY nao encontrada no .env da raiz.")

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {"aspectRatio": aspect_ratio, "imageSize": image_size},
        },
    }
    if usar_google_search:
        payload["tools"] = [{"googleSearch": {}}]

    resposta = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODELO}:generateContent",
        headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
        json=payload,
        timeout=300,
    )
    try:
        resposta.raise_for_status()
    except Exception as exc:
        raise RuntimeError(f"Erro Gemini: {resposta.text}") from exc
    salvar_png(saida, extrair_imagem(resposta.json()))


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Gerador isolado para Gemini 3 Pro Image.")
    parser.add_argument("texto", nargs="?", default=None,
                        help="Prompt inline. Se omitido, usa --prompt ou prompt.md.")
    parser.add_argument("--prompt", default=str(PASTA_MODELO / "prompt.md"))
    parser.add_argument("--saida", default=str(PASTA_MODELO / "saida" / "imagem.png"))
    parser.add_argument("--aspect-ratio", default="9:16")
    parser.add_argument("--image-size", default="2K")
    parser.add_argument("--google-search", action="store_true")
    return parser


def main() -> int:
    env_local = PASTA_MODELO / ".env"
    load_dotenv(env_local if env_local.exists() else RAIZ / ".env", override=True)
    args = construir_parser().parse_args()
    prompt = args.texto if args.texto else carregar_prompt(Path(args.prompt))
    gerar(prompt, Path(args.saida), args.aspect_ratio, args.image_size, args.google_search)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        raise SystemExit(1)
