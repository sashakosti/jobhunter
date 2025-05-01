import requests
from bs4 import BeautifulSoup
from db import SessionLocal
from models import Job
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

def parse_hh(keyword="python", pages=1):
    """Парсит hh.ru по ключевому слову"""
    db = SessionLocal()
    base_url = "https://hh.ru"
    search_url = f"{base_url}/search/vacancy"

    for page in range(pages):
        params = {
            "text": keyword,
            "page": page,
        }

        response = requests.get(search_url, headers=HEADERS, params=params)
        soup = BeautifulSoup(response.text, "html.parser")

        vacancies = soup.find_all("div", {"class": "vacancy-serp-item__layout"})

        if not vacancies:
            print(f"🛑 Нет вакансий на странице {page}")
            break

        for vac in vacancies:
            title_tag = vac.find("a", {"data-qa": "serp-item__title"})
            company_tag = vac.find("a", {"data-qa": "vacancy-serp__vacancy-employer"})
            location_tag = vac.find("div", {"data-qa": "vacancy-serp__vacancy-address"})

            if title_tag:
                title = title_tag.text.strip()
            else:
                title = "Без названия"

            company = company_tag.text.strip() if company_tag else "Не указана"
            location = location_tag.text.strip() if location_tag else "Не указано"

            job = Job(title=title, company=company, location=location)
            db.add(job)

        db.commit()
        print(f"✅ Страница {page + 1} обработана.")
        time.sleep(1.5)  # пауза, чтобы не спамить hh.ru

    db.close()
    print("🎉 Парсинг завершён.")

def parse():
    parse_hh()
