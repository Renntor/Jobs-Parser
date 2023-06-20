from src.vacancy import Vacancy


def test_Vacancy():
    vacancy = Vacancy('Python', 100000, '1 год', 'г. Снежный, ул. Теплая, д. 6',
                      'full', 'M', 'https://ya.ru', 'test')
    vacancy_two = Vacancy('Python', 50000, '1 год', 'г. Снежный, ул. Теплая, д. 6',
                          'https://ya.ru', 'Живой', 'test', 'test1')
    assert vacancy.__eq__(vacancy_two) is False
    assert vacancy.__le__(vacancy_two) is False
    assert vacancy.__lt__(vacancy_two) is False
    assert vacancy.__gt__(vacancy_two) is True
    assert vacancy.__ge__(vacancy_two) is True
    assert str(vacancy) == "Python, 100000, 1 год, г. Снежный, ул. Теплая, д. 6, full, M, https://ya.ru, test"
    assert repr(vacancy) == "Vacancy('Python', 100000, '1 год', \
'г. Снежный, ул. Теплая, д. 6', 'full', 'M', 'https://ya.ru', 'test')"
