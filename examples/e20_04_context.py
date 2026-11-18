from llm.prompt_builder import build_context

list_facts = [("Hello world!", 0.54), ("Я достаю из широких штанин", 0.94)]

result = build_context(list_facts)
print(result)

