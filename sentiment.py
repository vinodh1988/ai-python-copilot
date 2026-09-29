"""Classify a user comment as positive, negative, or neutral."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


VALID_SENTIMENTS = {"positive", "negative", "neutral"}
ENV_PATH = Path(__file__).resolve().with_name(".env")


def get_api_key() -> str:
    """Load and concatenate the three API-key pieces from .env."""
    if not ENV_PATH.is_file():
        raise RuntimeError(f"Environment file not found: {ENV_PATH}")

    load_dotenv(ENV_PATH, override=True)

    pieces = [
        os.getenv("KEY_PART1", "").strip(),
        os.getenv("KEY_PART2", "").strip(),
        os.getenv("KEY_PART3", "").strip(),
    ]

    if not all(pieces):
        raise RuntimeError(
            "Set KEY_PART1, KEY_PART2, and KEY_PART3 in the local .env file."
        )

    return "".join(pieces)


def classify_sentiment(comment: str) -> str:
    """Return positive, negative, or neutral for a comment."""
    if not comment.strip():
        raise ValueError("The comment cannot be empty.")

    client = OpenAI(api_key=get_api_key())
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=(
            "Classify the sentiment of the user's comment. Reply with exactly one "
            "lowercase word: positive, negative, or neutral. Do not explain."
        ),
        input=comment,
    )

    sentiment = response.output_text.strip().lower()
    if sentiment not in VALID_SENTIMENTS:
        raise RuntimeError(f"Unexpected model response: {response.output_text!r}")

    return sentiment


def main() -> None:
    comment = input("Enter a comment: ").strip()

    try:
        sentiment = classify_sentiment(comment)
    except (ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    except Exception as exc:
        print(f"OpenAI request failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print(f"Sentiment: {sentiment}")


if __name__ == "__main__":
    main()
