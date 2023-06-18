import os
import pytest
from src.saver import JsonSaver, TXTSaver, CSVSaver
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_date():
    return Vacancy('Python', 1000, '1 year', 'city M, st. K', 'full', 'M', 'https://how.su', 'sleeping')


def test_JsonSaver(vacancy_date):
    saver = JsonSaver()
    saver.file = os.path.join('..', 'tests', 'vacancy.json')

    saver.jobs_adding(vacancy_date.__dict__)
    assert os.path.exists(saver.file) is True

    vacancy_date.salary = 5
    saver.jobs_adding(vacancy_date.__dict__)

    vacancy_date.__city = 'G'
    saver.jobs_adding(vacancy_date.__dict__)

    vacancy_date.__experience = '2 year'
    saver.jobs_adding(vacancy_date.__dict__)

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


def test_CSVSaver(vacancy_date):
    saver = CSVSaver()
    saver.file = os.path.join('..', 'tests', 'vacancy.csv')

    saver.jobs_adding(vacancy_date.__dict__)
    assert os.path.exists(saver.file) is True

    vacancy_date.salary = 5
    saver.jobs_adding(vacancy_date.__dict__)

    vacancy_date.__city = 'G'
    saver.jobs_adding(vacancy_date.__dict__)

    vacancy_date.__experience = '2 year'
    saver.jobs_adding(vacancy_date.__dict__)

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


def test_TXTSaver(vacancy_date):
    saver = TXTSaver()
    saver.file = os.path.join('..', 'tests', 'vacancy.csv')

    saver.jobs_adding(vacancy_date.__dict__)
    assert os.path.exists(saver.file) is True

    vacancy_date.salary = 5
    saver.jobs_adding(vacancy_date.__dict__)

    vacancy_date.__city = 'G'
    saver.jobs_adding(vacancy_date.__dict__)

    vacancy_date.__experience = '2 year'
    saver.jobs_adding(vacancy_date.__dict__)

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
