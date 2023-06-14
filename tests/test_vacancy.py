import pytest
from src.vacancy import Vacancy


def test_Vacancy():
    vacancy = Vacancy('Python', 100000, '1 год', 'г. Снежный, ул. Теплая, д. 6',
                      'https://ya.ru', 'Живой')
    vacancy_two = Vacancy('Python', 50000, '1 год', 'г. Снежный, ул. Теплая, д. 6',
                      'https://ya.ru', 'Живой')
    assert vacancy.__dict__ == {"name": "Python", 'salary': 100000, 'experience': "1 год",
                                'address': 'г. Снежный, ул. Теплая, д. 6', 'url': 'https://ya.ru',
                                'requirement': 'Живой'}
    assert vacancy.__eq__(vacancy_two) == False
    assert vacancy.__le__(vacancy_two) == False
    assert vacancy.__lt__(vacancy_two) == False
    assert vacancy.__gt__(vacancy_two) == True
    assert vacancy.__ge__(vacancy_two) == True
    assert str(vacancy) == "Python, 100000, 1 год, г. Снежный, ул. Теплая, д. 6, https://ya.ru, Живой"
    assert repr(vacancy) == "Vacancy('Python', 100000, '1 год', \
'г. Снежный, ул. Теплая, д. 6', 'https://ya.ru', 'Живой')"