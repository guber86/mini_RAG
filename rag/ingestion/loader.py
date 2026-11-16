from pathlib import Path

BASE = Path(__file__).resolve().parents[2]

def get_content(filename: str = "source.txt") -> str:
    path = BASE / "source" / filename

    try:
        return path.read_text(encoding="utf-8") # read_text() have with inside
    #  or
    #  with path.open("r", excoding="utf-8") as file:
    #       return file.read()

    #  with can be useful, when you f.e. don't want to download the hole file at once, and want to process it line by line.
    #  with path.open("r", encoding="utf-8") as file:
    #     for line in file:
    #         process_line(line)

    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"File {filename} in directory {path.parent} not found."
        ) from error