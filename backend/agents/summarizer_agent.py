def summarize_text(text):

    sentences = text.split("\n")

    summary = sentences[:5]

    return " ".join(summary)