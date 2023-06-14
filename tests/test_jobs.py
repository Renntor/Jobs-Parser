import pytest
from src.jobs import HhApi, SuperJobApi


@pytest.fixture
def hh_date():
    return HhApi('Python')

@pytest.fixture
def supj_date():
    return SuperJobApi('Java')


def test_HhApi(hh_date):
    hh = hh_date
    assert str(hh) == 'Python'
    assert repr(hh) == "HhApi('Python')"
    assert type(hh.get_vacancies()) == str

def test_SuperJobApi(supj_date):
    supj = supj_date
    assert str(supj) == 'Java'
    assert repr(supj) == "HhApi('Java')"
    assert type(supj.get_vacancies()) == str