import os
from dotenv import load_dotenv

load_dotenv()

student = os.getenv("LAB_STUDENT", "не задано")

print(student)