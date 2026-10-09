from textblob import TextBlob


def correct_text(text):
    if not text or not text.strip():
        return ""

    corrected_text = str(TextBlob(text).correct())

    return corrected_text
