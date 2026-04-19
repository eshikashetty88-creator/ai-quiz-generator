def clean_text(text):
    lines = text.split("\n")
    clean = []

    for line in lines:
        line = line.strip()
        if len(line) > 30:   # remove short noisy lines
            clean.append(line)

    return " ".join(clean)