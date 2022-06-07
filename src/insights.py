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


def filter_by_salary_range(jobs, salary):
    list_items = []
    for index, job in enumerate(jobs):
        try:
            if (matches_salary_range(jobs[index], salary)) is True:
                list_items.append(jobs[index])
        except ValueError:
            ...
    return list_items
