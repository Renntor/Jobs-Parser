import os
import pytest
from src.saver import JsonSaver, TXTSaver, CSVSaver
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_date():
    return Vacancy('Python', 5, '1 year', 'city M, st. K', 'full', 'M', 'https://how.su', 'sleeping')


@pytest.fixture
def vacancy_date_two():
    return Vacancy('Python', 5, '1 year', 'city M, st. K', 'full', 'G', 'https://how.su', 'sleeping')

@pytest.fixture
def vacancy_date_three():
    return Vacancy('Python', 5, '2 year', 'city M, st. K', 'full', 'G', 'https://how.su', 'sleeping')

def test_JsonSaver(vacancy_date, vacancy_date_two, vacancy_date_three):
    saver = JsonSaver()
    saver.file = os.path.join('..', 'tests', 'vacancy.json')

    saver.jobs_adding(vacancy_date.__dict__)
    assert os.path.exists(saver.file) is True

    saver.jobs_adding(vacancy_date_two.__dict__)
    saver.jobs_adding(vacancy_date_three.__dict__)

    assert len(saver.get_salary(5)) == 3
    assert len(saver.get_city('G')) == 2

    test_date = saver.get_experience('2 year')[0]
    saver.jobs_deleting(test_date)

    assert len(saver.get_experience('2 year')) == 0

    saver.file_cleaning()
    assert os.path.exists(saver.file) is False
    saver.jobs_adding({})
    saver.jobs_deleting({})
    saver.jobs_deleting({})
    saver.file_cleaning()


def test_CSVSaver(vacancy_date, vacancy_date_two, vacancy_date_three):
    saver = CSVSaver()
    saver.file = os.path.join('..', 'tests', 'vacancy.csv')

    saver.jobs_adding(vacancy_date.__dict__)
    assert os.path.exists(saver.file) is True

    saver.jobs_adding(vacancy_date_three.__dict__)
    saver.jobs_adding(vacancy_date_two.__dict__)

    assert len(saver.get_salary(5)) == 3
    assert len(saver.get_city('G')) == 2

    test_date = saver.get_experience('2 year')[0]
    saver.jobs_deleting(test_date)

    assert len(saver.get_experience('2 year')) == 0

    saver.file_cleaning()
    assert os.path.exists(saver.file) is False
    saver.jobs_adding({})
    saver.jobs_deleting({})
    saver.jobs_deleting({})
    saver.file_cleaning()


def test_TXTSaver(vacancy_date, vacancy_date_two, vacancy_date_three):
    saver = TXTSaver()
    saver.file = os.path.join('..', 'tests', 'vacancy.csv')

    saver.jobs_adding(vacancy_date.__dict__)
    assert os.path.exists(saver.file) is True

    saver.jobs_adding(vacancy_date_three.__dict__)
    saver.jobs_adding(vacancy_date_two.__dict__)

    assert len(saver.get_salary(5)) == 3
    assert len(saver.get_city('G')) == 2

    test_date = saver.get_experience('2 year')[0]
    saver.jobs_deleting(test_date)

    assert len(saver.get_experience('2 year')) == 0

    saver.file_cleaning()
    assert os.path.exists(saver.file) is False
    saver.jobs_adding({})
    saver.jobs_deleting({})
    saver.jobs_deleting({})
    saver.file_cleaning()
