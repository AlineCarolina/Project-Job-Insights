from src.counter import count_ocurrences


def test_counter():
    counter = count_ocurrences("src/jobs.csv", "JavaScript")
    assert counter == 122

    counter = count_ocurrences("src/jobs.csv", "salesforce")
    assert counter == 646
