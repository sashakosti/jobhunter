import requests
from typing import List
from models import Vacancy


BASE_URL = "https://api.hh.ru/vacancies"


def fetch_vacancies(text: str, area: str = "1", per_page: int = 10) -> List[Vacancy]:
    """
    Ищет вакансии по ключевому слову.
    :param text: Ключевые слова (например "Python")
    :param area: Регион (по умолчанию - Москва, см. https://api.hh.ru/areas)
    :param per_page: Кол-во вакансий
    :return: Список вакансий
    """
    params = {
        "text": text,
        "area": area,
        "per_page": per_page
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    items = response.json()["items"]
    return [Vacancy.from_api(item) for item in items]

