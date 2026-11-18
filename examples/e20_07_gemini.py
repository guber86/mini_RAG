from google.genai import errors
from dotenv import load_dotenv
from llm.llm import get_ai_response
from httpx2 import TimeoutException

load_dotenv()

query = "Можно ли оплатить заказ после получения?"

chunks = [
    ("Заказы отправляются по предоплате", 0.91),
    ("Доставка занимает 3-5 дней", 0.54),
]

try:
    result = get_ai_response(query, chunks, mode="gemini")
    print(result)
except TimeoutException:
    print("Время ожидания ответа Gemini истекло. Попробуйте позже.")
except errors.APIError as e:
    if e.code == 503:
        print("Перегрузка API")
    else:
        print(e.message)

