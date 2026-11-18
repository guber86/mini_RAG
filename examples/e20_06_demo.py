from llm.llm import get_ai_response

question = "Как пройти в библиотеку"
first_list = []
second_list = [("Вам направо", 0.91), ("Третья улица строителей, д.3", 0.54)]

result_1 = get_ai_response(question, first_list)
result_2 = get_ai_response(question, second_list)

print(result_1)
print(result_2)