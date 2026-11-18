from dotenv import load_dotenv
from rag.requests.controller import get as answer_question
from google.genai import errors
from httpx2 import TimeoutException



load_dotenv()
query = input("Ваш вопрос: ")
# query = "Можно ли оплатить при получении?"


try:
    response = answer_question(query, top_k=2, mode="gemini")
    print(response)
except TimeoutException:
    print("Время ожидания ответа Gemini истекло. Попробуйте позже.")
except errors.APIError as e:
    if e.code == 503:
        print("Перегрузка API")
    else:
        print(e.message)