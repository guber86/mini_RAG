from pathlib import Path

BASE = Path(__file__).resolve().parents[2]

# Заметки: notes/python_learning.md — «Чтение файлов».
def get_content(filename: str = "source.txt") -> str:
    path = BASE / "source" / filename

    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"File {filename} in directory {path.parent} not found."
        ) from error
