from abc import ABC, abstractmethod
import requests
import json
from datetime import datetime
import time


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

    def get_vacancies(self) -> str:
        """
        Функция для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        hh_request = requests.get('https://api.hh.ru/vacancies', params=self.__params)
        date_hh = hh_request.content.decode()
        hh_json = json.loads(date_hh)
        hh_json = json.dumps(hh_json, indent=2, ensure_ascii=False)
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


# r = requests.get('https://api.hh.ru/')
#
# r_json = json.dumps(r)
# params = {
#         'text': 'NAME:Python', # Текст фильтра. В имени должно быть слово "Аналитик"
#         'area': 1, # Поиск ощуществляется по вакансиям города Москва
#         'page': 0, # Индекс страницы поиска на HH
#         'per_page': 8 # Кол-во вакансий на 1 странице
#     }
#
#
#
# answer = requests.get('https://api.hh.ru/vacancies', params=params)
# data = answer.content.decode()
# a_json = json.loads(data)
#
# print(json.dumps(a_json, indent=2, ensure_ascii=False))
# # with open('test.json', 'w', encoding="utf-8") as f:
#     json.dump(a_json, f, ensure_ascii=False)



# for i in a_json['items']:
#     print(f"""{i['name']}
# от:{i['salary']['from']}
# до:{i['salary']['to']}
#     """)

i = HhApi('Python')

print(type(i.get_vacancies()))