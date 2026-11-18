import os
from llm.prompt_builder import build_prompt

def get_ai_response(query, chunks, mode="demo"):
    if not chunks:
        return "В базе нет ответа."
    elif mode == "demo":
        return f"[ДЕМО без генерации]\n{chunks[0][0]}"
    elif mode == "gemini":
        from google import genai
        key = os.getenv("GEMINI_API_KEY", "").strip()

        if not key:
            raise ValueError("No GEMINI_API_KEY environment variable")

        prompt = build_prompt(query,chunks)
        model_name = os.getenv("GEMINI_MODEL_NAME", "")

        if not model_name:
            raise ValueError("No GEMINI_MODEL_NAME environment variable")

        with genai.Client(api_key=key, http_options={"timeout": 30_000}) as client:
            response = client.models.generate_content(model=model_name, contents=prompt)

            answer = (response.text or "").strip()
            if not answer:
                raise ValueError("Gemini не вернул текстовый ответ")
            else:
                return answer

    else:
        raise ValueError("Режим неизвестен")


