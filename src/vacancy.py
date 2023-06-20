
class Vacancy:
    """
    Обработка вакансий
    """
    def __init__(self, name: str, salary: int, experience: str,
                 address: str, employment: str, city: str, url: str, requirement: str) -> None:
        self.__name = name
        if salary is not None:
            self.__salary = salary
        else:
            self.__salary = 0
        self.__experience = experience
        self.__address = address
        self.__employment = employment
        self.__city = city
        self.__url = url
        self.__requirement = requirement

    @property
    def salary(self):
        return self.__salary

    def __gt__(self, other):
        return self.__salary > other.__salary

    def __ge__(self, other):
        return self.__salary >= other.__salary

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __le__(self, other):
        return self.__salary <= other.__salary

    def __eq__(self, other):
        return self.__salary == other.__salary

    def __str__(self):
        return f'{self.__name}, {self.__salary}, {self.__experience}, {self.__address}, {self.__employment}, \
{self.__city}, {self.__url}, {self.__requirement}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__salary}, '{self.__experience}', \
'{self.__address}', '{self.__employment}', '{self.__city}', '{self.__url}', '{self.__requirement}')"
