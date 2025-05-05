from models import Vacancy, Employer, Area


def test_vacancy_model():
    raw_data = {
        "id": "123",
        "name": "Backend Developer",
        "employer": {"name": "ООО Пример"},
        "area": {"name": "Санкт-Петербург"},
        "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
        "published_at": "2023-01-01T00:00:00+0300",
        "alternate_url": "https://hh.ru/vacancy/123",
        "snippet": {"requirement": "Опыт работы", "responsibility": "Разработка"},
    }

    vacancy = Vacancy.from_api(raw_data)
    assert vacancy.name == "Backend Developer"
    assert vacancy.salary_from == 100000
    assert vacancy.snippet_responsibility == "Разработка"

