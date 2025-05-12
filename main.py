import argparse
from src.hh_api import fetch_vacancies
from src.letter_generator import generate_letter


def print_vacancies(vacancies):
    for i, vac in enumerate(vacancies, 1):
        print(f"\n[{i}] {vac.name}")
        print(f"Компания: {vac.employer.name} — Город: {vac.area.name}")
        if vac.salary_from or vac.salary_to:
            salary_str = f"{vac.salary_from or ''} - {vac.salary_to or ''} {vac.currency or ''}"
            print(f"Зарплата: {salary_str}")
        print(f"Требования: {vac.snippet_requirement}")
        print(f"Обязанности: {vac.snippet_responsibility}")
        print(f"Ссылка: {vac.url}")
        print("-" * 50)


def main():
    parser = argparse.ArgumentParser(description="Поиск вакансий через hh.ru")
    parser.add_argument("--keywords", required=True, help="Ключевые слова (например: Python developer)")
    parser.add_argument("--area", default="1", help="ID региона (по умолчанию Москва — 1)")
    parser.add_argument("--limit", type=int, default=10, help="Количество вакансий")

    args = parser.parse_args()

    print(f"🔍 Поиск вакансий по ключевым словам: {args.keywords}")
    vacancies = fetch_vacancies(args.keywords, area=args.area, per_page=args.limit)
    print_vacancies(vacancies)

    if vacancies:
        choice = input("\nВыбери номер вакансии, для которой сгенерировать сопроводительное письмо (или Enter для выхода): ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(vacancies):
                letter = generate_letter(vacancies[index])
                print("\n📄 Сопроводительное письмо:\n")
                print(letter)
            else:
                print("❌ Неверный выбор.")
        else:
            print("Завершено.")


if __name__ == "__main__":
    main()

