from typing import Union, List, Dict

from src.insights.jobs import read

# from jobs import read

file = "data/jobs.csv"
job = {"title": "Data Scientist", "min_salary": "3000", "max_salary": "6000"}
salary = 5000

# result = matches_salary_range(job, salary)
# print(result)


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
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
