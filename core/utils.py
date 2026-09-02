import re


def normalize_command(query: str) -> str:
    """Normalize a voice command for easier processing."""

    query = query.lower().strip()

    # Remove common punctuation
    query = re.sub(r"[?!.,]", "", query)

    # Collapse multiple spaces
    query = re.sub(r"\s+", " ", query)

    return query


def remove_phrases(text: str, phrases: list[str]) -> str:
    """Remove known phrases from text."""

    for phrase in phrases:
        text = text.replace(phrase, "")

    return text.strip()