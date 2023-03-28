from typing import Union, List, Dict

from src.insights.jobs import read

# from jobs import read

file = "data/jobs.csv"

job = {"title": "Data Scientist", "min_salary": "3000", "max_salary": "6000"}
salary = 5000
# result = matches_salary_range(job, salary)
# print(result)

jobs = [
    {
        "id": "1",
        "title": "Software Developer",
        "min_salary": "2500",
        "max_salary": "5000",
    },
    {
        "id": "2",
        "title": "Data Analyst",
        "min_salary": "2000",
        "max_salary": "4000",
    },
    {
        "id": "3",
        "title": "Project Manager",
        "min_salary": "4000",
        "max_salary": "7000",
    },
    {
        "id": "5",
        "title": "UX Designer",
        "min_salary": "3000",
        "max_salary": "5500",
    },
]
# filtered_jobs = filter_by_salary_range(jobs, 2500)


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = set()
    for job in data:
        if job["max_salary"].isnumeric():
            max_salary.add(int(job["max_salary"]))

    return max(max_salary)


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = set()
    for job in data:
        if job["min_salary"].isnumeric():
            min_salary.add(int(job["min_salary"]))

    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)

        if min_salary > max_salary:
            raise ValueError("min_salary é maior que max_salary")
        return min_salary <= salary <= max_salary
    except (KeyError, ValueError, TypeError):
        raise ValueError("parâmetros inválidos")


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            print(f"Erro ao comparar salário do trabalho {job}: {salary}")
    return filtered_jobs
