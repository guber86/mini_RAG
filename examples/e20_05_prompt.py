from llm.prompt_builder import build_prompt

question = "Как пройти в библиотеку"

list_facts = [("Вам направо", 0.91), ("Третья улица строителей, д.3", 0.54)]

prompt = build_prompt(question, list_facts)

print(prompt)
