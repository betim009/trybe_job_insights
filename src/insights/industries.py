from typing import List, Dict

from src.insights.jobs import read
# from jobs import read


file = "data/jobs.csv"


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    unique_industries = set()

    for industrys in data:
        industry = industrys.get("industry", "")
        if industry.strip():
            unique_industries.add(industry)

    return list(unique_industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
