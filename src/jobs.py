import os
from abc import ABC, abstractmethod
import httpx
import ujson


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
            'page': 0,  # Страница в HH
            'per_page': 100,  # Количество вакансий на 1 странице
        }

    def get_vacancies(self) -> dict:
        """
        Функция для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        hh_request = httpx.get('https://api.hh.ru/vacancies', params=self.__params)
        date_hh = hh_request.content.decode()
        hh_json = ujson.loads(date_hh)
        return hh_json

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"


class SuperJobApi(Job):
    """
    Класс для получения вакансий от SuperJob по API
    """
    api: str = os.environ.get('SUPERJOB_API')
    headers = {
        'Host': 'api.superjob.ru',
        'X-Api-App-Id': api,
        'Authorization': 'Bearer r.000000010000001.example.access_token',
        'Content-Type': 'application / x-www-form-urlencoded',
    }

    def __init__(self, name: str) -> None:
        self.name = name
        self.__params = {
                        'keywords': [self.name],  # Название вакансии
                        'payment_from': 0,  # зарплата от
                        'published': 1,

                        }

    def get_vacancies(self) -> dict:
        """
        Функция для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        get_sup = httpx.get('https://api.superjob.ru/2.0/vacancies/', params=self.__params, headers=self.headers)
        date_superjob = get_sup.content.decode()
        superjob_json = ujson.loads(date_superjob)
        return superjob_json

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"
