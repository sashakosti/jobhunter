from hh_api import fetch_vacancies


def test_fetch_vacancies():
    vacancies = fetch_vacancies("Python", per_page=2)
    assert len(vacancies) == 2
    assert vacancies[0].name
    assert vacancies[0].url.startswith("https://")

