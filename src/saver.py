import json
from abc import ABC, abstractmethod
import os
from src.vacancy import Vacancy


class Saver(ABC):

    @abstractmethod
    def jobs_adding(self, jobs):
        pass

    @abstractmethod
    def get_salary(self, salary):
        pass

    @abstractmethod
    def get_city(self, citi):
        pass

    @abstractmethod
    def get_experience(self, experience):
        pass

    @abstractmethod
    def jobs_deleting(self, jobs):
        pass


class JsonSaver(Saver):

    file = os.path.join('..', 'src', 'vacancy.json')

    def jobs_adding(self, jobs: dict) -> None:
        """
        Метод добавление данных в формате json
        :param jobs: словарь, который добавляется в файл
        :return: None
        """
        # проверка существования файла
        if os.path.exists(self.file) is False:
            with open(self.file, 'w', encoding="utf-8") as f:
                f.write('[]')
        # добавление данных в список файла
        json_data = json.load(open(self.file))
        json_data.append(jobs)
        # записывание список в файл
        with open(self.file, 'w', encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

    def get_salary(self, salary: int) -> list:
        """
        Метод на проверку зарплаты
        :param salary: запралата
        :return: Список подходящих вакансий
        """
        jobs_list = []
        with open(self.file, 'r', encoding="utf-8") as f:
            json_data = json.load(f)
            for i in json_data:
                if i['salary'] == salary:
                    jobs_list.append(i['salary'])
        return jobs_list

    def get_city(self, city: str) -> list:
        """
        Метод на проверку города
        :param city: город
        :return: Список подходящих вакансий
        """
        pass

    def get_experience(self, experience: str) -> list:
        """
        Метод на проверку опыта работы
        :param experience: опыт работы
        :return: Список подходящих вакансий
        """
        pass

    def jobs_deleting(self, jobs: dict) -> None:
        """
        Метод на удаление выбранной вакансии
        :param jobs: словарь вакансии
        :return: None
        """
        pass


class CSVSaver(Saver):

    def jobs_adding(self, jobs):
        pass

    def get_salary(self, salary):
        pass

    def get_city(self, citi):
        pass

    def get_experience(self, experience):
        pass

    def jobs_deleting(self, jobs):
        pass


class TXTSaver(Saver):

    def jobs_adding(self, jobs):
        pass

    def get_salary(self, salary):
        pass

    def get_city(self, citi):
        pass

    def get_experience(self, experience):
        pass

    def jobs_deleting(self, jobs):
        pass

