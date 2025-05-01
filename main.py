import typer
from parser import parse_hh
from db import Base, engine, SessionLocal
from models import Job
from rich.table import Table
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def init():
    """Создаёт таблицы в БД"""
    Base.metadata.create_all(bind=engine)
    console.print("[green]✔ Таблицы созданы.[/green]")

@app.command()
def run(keyword: str = "python", pages: int = 1):
    """Запускает парсинг hh.ru по ключевому слову"""
    parse_hh(keyword=keyword, pages=pages)

@app.command()
def list():
    """Выводит все вакансии"""
    db = SessionLocal()
    jobs = db.query(Job).all()
    table = Table(title="Jobs")
    table.add_column("ID", style="cyan")
    table.add_column("Title")
    table.add_column("Company")
    table.add_column("Location")
    table.add_column("Viewed", justify="center") # Добавляем колонку Viewed

    for job in jobs:
        table.add_row(str(job.id), job.title, job.company, job.location, "✅" if job.is_viewed else "❌") # Отображаем статус Viewed

    console.print(table)
    db.close()

@app.command()
def view(job_id: int):
    """Отмечает вакансию как просмотренную"""
    session = SessionLocal()
    job = session.query(Job).get(job_id)
    if job:
        job.is_viewed = True
        session.commit()
        console.print(f"[green]✔ Вакансия {job_id} отмечена как просмотренная.[/green]")
    else:
        console.print(f"[red]❌ Вакансия с ID {job_id} не найдена.[/red]")
    session.close()

if __name__ == "__main__":
    app()
