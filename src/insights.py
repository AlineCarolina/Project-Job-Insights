from src import jobs


def get_unique_job_types(path):
    data = jobs.read(path)
    job_type = []
    for type in data:
        job_type.append(type['job_type'])
    return list(set(job_type))


def filter_by_job_type(jobs, job_type):
    type_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            type_list.append(job)
    return type_list


def get_unique_industries(path):
    data = jobs.read(path)
    industries = []
    for industry in data:
        if industry['industry'] != '':
            industries.append(industry['industry'])
    return list(set(industries))


def filter_by_industry(jobs, industry):
    industry_list = []
    for job in jobs:
        if job["industry"] == industry:
            industry_list.append(job)
    return industry_list


def get_max_salary(path):
    data = jobs.read(path)
    salaries = [
        int(job["max_salary"])
        for job in data
        if job["max_salary"].isdigit()
    ]
    return max(salaries)


def get_min_salary(path):
    data = jobs.read(path)
    salaries = [
        int(job["min_salary"])
        for job in data
        if job["min_salary"].isdigit()
    ]
    return min(salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("1")
    if (
        not str(job["min_salary"]).isdigit()
        or not str(job["max_salary"]).isdigit()
    ):
        raise ValueError("2")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("3")
    if type(salary) != int:
        raise ValueError("4")
    return job["min_salary"] <= int(salary) <= job["max_salary"]
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
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
    return []
