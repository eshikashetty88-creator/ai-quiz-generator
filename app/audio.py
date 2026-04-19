from gtts import gTTS

def generate_summary(text):
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 40]
    summary = ". ".join(sentences[:5])

    if not summary:
        summary = text[:300]

    return summary


def generate_audio(text):
    summary = generate_summary(text)

    tts = gTTS(summary)
    file_path = "summary.mp3"
    tts.save(file_path)

    return file_path, summary