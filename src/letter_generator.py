import json
from src.models import Vacancy
from pathlib import Path


def load_user_profile(path: str = "data/user_profile.json") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_letter(vacancy: Vacancy) -> str:
    profile = load_user_profile()

    greeting = f"Здравствуйте! Меня зовут {profile['name']}."
    intro = f"Я заинтересован(а) в вакансии \"{vacancy.name}\" в компании {vacancy.employer.name}."
    experience = f"У меня есть опыт: {profile['experience']}."
    motivation = f"Мне особенно интересны задачи, связанные с {profile['interests']}."
    closing = "Буду рад(а) обсудить сотрудничество. Спасибо за внимание!"

    return "\n".join([greeting, intro, experience, motivation, closing])

