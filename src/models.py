from pydantic import BaseModel
from typing import List, Optional


class Employer(BaseModel):
    name: str


class Area(BaseModel):
    name: str


class Vacancy(BaseModel):
    id: str
    name: str
    employer: Employer
    area: Area
    salary_from: Optional[int] = None
    salary_to: Optional[int] = None
    currency: Optional[str] = None
    published_at: str
    url: str
    snippet_requirement: Optional[str] = None
    snippet_responsibility: Optional[str] = None

    @classmethod
    def from_api(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            employer=Employer(name=data["employer"]["name"]),
            area=Area(name=data["area"]["name"]),
            salary_from=(data["salary"]["from"] if data["salary"] else None),
            salary_to=(data["salary"]["to"] if data["salary"] else None),
            currency=(data["salary"]["currency"] if data["salary"] else None),
            published_at=data["published_at"],
            url=data["alternate_url"],
            snippet_requirement=data.get("snippet", {}).get("requirement"),
            snippet_responsibility=data.get("snippet", {}).get("responsibility"),
        )

