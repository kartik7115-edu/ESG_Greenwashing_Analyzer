import re


def clean_text(text):
    """
    Clean extracted PDF text while preserving sentence structure.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove excessive spaces
    text = re.sub(r'[ \t]+', ' ', text)

    # Preserve periods for sentence tokenization
    text = re.sub(r'[^a-zA-Z0-9\s\.\,\%\-\:]', '', text)

    # Remove repeated newlines
    text = re.sub(r'\n+', '\n', text)

    return text