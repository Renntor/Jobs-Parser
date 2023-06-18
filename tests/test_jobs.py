import pytest
from src.jobs import HhApi, SuperJobApi


@pytest.fixture
def hh_date():
    return HhApi('Python')


@pytest.fixture
def supj_date():
    return SuperJobApi('Java')


def test_HhApi(hh_date):
    assert str(hh_date) == 'Python'
    assert repr(hh_date) == "HhApi('Python')"
    assert type(hh_date.get_vacancies()) == dict


def test_SuperJobApi(supj_date):
    assert str(supj_date) == 'Java'
    assert repr(supj_date) == "HhApi('Java')"
    assert type(supj_date.get_vacancies()) == dict
