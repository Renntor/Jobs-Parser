
class Vacancy:
    """
    Обработка вакансий
    """
    def __init__(self, name: str, salary: int, experience: str,
                 address: str, url: str, requirement: str) -> None:
        self.name = name
        self.salary = salary
        self.experience = experience
        self.address = address
        self.url = url
        self.requirement = requirement

    def __gt__(self, other) -> bool:
        return self.salary > other.salary

    def __ge__(self, other) -> bool:
        return self.salary >= other.salary

    def __lt__(self, other) -> bool:
        return self.salary < other.salary

    def __le__(self, other) -> bool:
        return self.salary <= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __str__(self):
        return f'{self.name}, {self.salary}, {self.experience}, {self.address}, {self.url}, {self.requirement}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.salary}, \
'{self.experience}', '{self.address}', '{self.url}', '{self.requirement}')"


