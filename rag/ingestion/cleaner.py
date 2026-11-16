import re

def clean_content(content):
    patten = r"[^а-яА-ЯёЁ0-9.,!?\-\s]"
    step_1 = re.sub(patten, "", content)

    return re.sub(r"\s+", " ", step_1).strip()
    #  removing extra spaces inside string and side spaces
