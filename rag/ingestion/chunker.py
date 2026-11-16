def get_chunks(content):
    chunks = []

    for chunk in content.split(". "):
        chunk = chunk.strip()

        if chunk:
            chunks.append(chunk)

    return chunks

