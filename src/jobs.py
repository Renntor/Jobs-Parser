from abc import ABC, abstractmethod
import requests
import json


class Job(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HhApi(Job):
    """
    Класс для получения вакансий от НН по API
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.__params = {
            'text': 'NAME:'+self.name,  # Поиска вакансии по имени
            'area': 1,  # Поиск по городам
            'page': 0,  # Страница в HH
            'per_page': 8  # Количество вакансий на 1 странице
        }

    def get_vacancies(self) -> dict:
        """
        Функция для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        hh_request = requests.get('https://api.hh.ru/vacancies', params=self.__params)
        date_hh = hh_request.content.decode()
        hh_json = json.loads(date_hh)
        return hh_json

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"


class SuperJobApi(Job):
    """
    Класс для получения вакансий от SuperJob по API
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def get_vacancies(self) -> str:
        """
        Функция для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        pass

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"


