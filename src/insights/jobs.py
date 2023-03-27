from functools import lru_cache
from typing import List, Dict
import csv

file = "data/jobs.csv"


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, newline="") as file:
        jobs_reader = list(csv.DictReader(file))
        return jobs_reader


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    unique_job_types = set()

    for row in data:
        unique_job_types.add(row["job_type"])
    return list(unique_job_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
