from fastapi import FastAPI
from word_generator import generate_word as generate

app = FastAPI()


@app.get("/{language}")
def serve_word(language: str,
               min_len: int | None = 4,
               max_len: int | None = 11,
               start_letter: str | None = None):
    try:
        word = generate(language,
                        min_len=min_len,
                        max_len=max_len,
                        start_letter=start_letter)
        exception = None
    except Exception as e:
        word = None
        exception = e
    finally:
        return {
            "word": word,
            "error": str(exception) if exception else None,
            "language": language,
            "length": len(word) if word else 0
        }
