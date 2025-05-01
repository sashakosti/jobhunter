import argparse
from rich.table import Table
from rich.console import Console
from .db import SessionLocal
from .models import Job
from .parser import parse_hh

console = Console()

def list_jobs():
    session = SessionLocal()
    jobs = session.query(Job).all()
    table = Table(title="Vacancies")
    table.add_column("ID", justify="right")
    table.add_column("Title")
    table.add_column("Company")
    table.add_column("Viewed", justify="center")

    for job in jobs:
        table.add_row(str(job.id), job.title, job.company, "✅" if job.is_viewed else "❌")

    console.print(table)
    session.close()

def mark_viewed(job_id):
    session = SessionLocal()
    job = session.query(Job).get(job_id)
    if job:
        job.is_viewed = True
        session.commit()
        print(f"Marked job {job_id} as viewed.")
    else:
        print("Not found.")
    session.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["parse", "list", "view"])
    parser.add_argument("--id", type=int)

    args = parser.parse_args()

    if args.command == "parse":
        parse_hh()
    elif args.command == "list":
        list_jobs()
    elif args.command == "view" and args.id:
        mark_viewed(args.id)
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
