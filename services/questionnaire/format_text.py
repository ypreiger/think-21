"""Punctuation and line breaks only. Words stay as spoken."""

import re

HEBREW = re.compile(r"[\u0590-\u05FF]")
END = ".?!"


def format_transcript(text: str, language: str = "en", segments: list | None = None) -> str:
    language = language if language in {"en", "ru", "he"} else "en"
    if segments:
        built = _from_segments(segments, language)
        if built:
            return built
    return _polish(text or "", language)


def _from_segments(segments: list, language: str) -> str:
    paragraphs: list[list[str]] = []
    current: list[str] = []
    previous_end = None
    for segment in segments:
        piece = _spacing(str(segment.get("text") or ""))
        if not piece:
            continue
        start = float(segment.get("start") or 0)
        end = float(segment.get("end") or start)
        gap = 0 if previous_end is None else start - previous_end
        if current and gap >= 2.0:
            paragraphs.append(current)
            current = [piece]
        elif current and gap >= 0.85:
            current[-1] = _close(current[-1])
            current.append(piece)
        else:
            current.append(piece)
        previous_end = end
    if current:
        paragraphs.append(current)
    lines = []
    for paragraph in paragraphs:
        if not paragraph:
            continue
        paragraph[-1] = _close(paragraph[-1])
        sentence = _spacing(" ".join(paragraph))
        lines.append(_capitalize_sentences(sentence, language))
    return "\n\n".join(line for line in lines if line).strip()


def _polish(text: str, language: str) -> str:
    paragraphs = []
    for block in re.split(r"\n\s*\n", text.replace("\r\n", "\n")):
        cleaned = _capitalize_sentences(_spacing(block), language)
        if not cleaned:
            continue
        paragraphs.append(_close(cleaned))
    return "\n\n".join(paragraphs).strip()


def _spacing(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([,.;:!?…])", r"\1", text)
    text = re.sub(r"([,;:!?…])(?=[^\s])", r"\1 ", text)
    text = re.sub(r"([.])(?=[^\s\d.])", r"\1 ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _close(text: str) -> str:
    text = text.strip()
    if not text or text[-1] in END or text.endswith("…"):
        return text
    return text + "."


def _capitalize_sentences(text: str, language: str) -> str:
    if language == "he" or not text:
        return text
    parts = re.split(r"([.!?…]\s+)", text)
    out = []
    for part in parts:
        if re.fullmatch(r"[.!?…]\s+", part or ""):
            out.append(part)
        else:
            out.append(_cap_first(part))
    text = "".join(out)
    if language == "en":
        text = re.sub(r"\bi\b", "I", text)
    return text


def _cap_first(text: str) -> str:
    chars = list(text)
    for index, char in enumerate(chars):
        if char.isalpha() and not HEBREW.match(char):
            chars[index] = char.upper()
            break
        if char.isalpha():
            break
    return "".join(chars)
