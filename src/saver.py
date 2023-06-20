import csv
import os
import pickle
import ujson
from abc import ABC, abstractmethod


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

    @abstractmethod
    def file_cleaning(self):
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
        json_data = ujson.load(open(self.file))  # добавление данных в список файла
        json_data.append(jobs)
        # записывание список в файл
        with open(self.file, 'w', encoding="utf-8") as f:
            ujson.dump(json_data, f, indent=2, ensure_ascii=False, escape_forward_slashes=False)

    def get_salary(self, salary: int) -> list:
        """
        Метод на проверку зарплаты
        :param salary: запралата
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            ujson_data = ujson.load(f)
            return [ujson_data[item] for item in range(len(ujson_data)) if
                    ujson_data[item]['_Vacancy__salary'] == salary]

    def get_city(self, city: str) -> list:
        """
        Метод на проверку города
        :param city: город
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            ujson_data = ujson.load(f)
            return [ujson_data[item] for item in range(len(ujson_data)) if ujson_data[item]['_Vacancy__city'] == city]

    def get_experience(self, experience: str) -> list:
        """
        Метод на проверку опыта работы
        :param experience: опыт работы
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            ujson_data = ujson.load(f)
            return [ujson_data[item] for item in range(len(ujson_data)) if
                    ujson_data[item]['_Vacancy__experience'] == experience]

    def jobs_deleting(self, jobs: dict) -> None:
        """
        Метод на удаление выбранной вакансии
        :param jobs: словарь вакансии
        :return: None
        """
        try:
            ujson_data = ujson.load(open(self.file))
            ujson_data.remove(jobs)
            with open(self.file, 'w', encoding="utf-8") as f:
                ujson.dump(ujson_data, f, indent=2, ensure_ascii=False, escape_forward_slashes=False)
        except ValueError:
            print('Все вакансии удалены')

    def file_cleaning(self) -> None:
        """
        Очищение файла от вакансий
        :return: None
        """
        os.remove(self.file)


class CSVSaver(Saver):
    file = os.path.join('..', 'src', 'vacancy.csv')

    def jobs_adding(self, jobs: dict) -> None:
        """
        Метод добавление данных в формате json
        :param jobs: словарь, который добавляется в файл
        :return: None
        """
        if os.path.exists(self.file) is False:
            with open(self.file, 'w', encoding='utf-8') as f:
                write = csv.DictWriter(f, fieldnames=jobs.keys(), quoting=csv.QUOTE_NONNUMERIC)
                write.writeheader()
                write.writerow(jobs)
        else:
            with open(self.file, 'a', encoding='utf-8') as f:
                write = csv.DictWriter(f, fieldnames=jobs.keys(), quoting=csv.QUOTE_NONNUMERIC)
                write.writerow(jobs)

    def get_salary(self, salary: int) -> list:
        """
        Метод на проверку зарплаты
        :param salary: запралата
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            return [item for item in csv.DictReader(f) if int(item['_Vacancy__salary']) == salary]

    def get_city(self, city: str) -> list:
        """
        Метод на проверку города
        :param city: город
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            return [item for item in csv.DictReader(f) if item['_Vacancy__city'] == city]

    def get_experience(self, experience: str) -> list:
        """
        Метод на проверку опыта работы
        :param experience: опыт работы
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            return [item for item in csv.DictReader(f) if item['_Vacancy__experience'] == experience]

    def jobs_deleting(self, jobs: dict) -> None:
        """
        Метод на удаление выбранной вакансии
        :param jobs: словарь вакансии
        :return: None
        """
        try:
            file = open(self.file)
            file_csv = csv.DictReader(file)
            jobs_list = [item for item in file_csv if item != jobs]
            with open(self.file, 'w', encoding='utf-8') as f:
                write = csv.DictWriter(f, fieldnames=jobs_list[0].keys(), quoting=csv.QUOTE_NONNUMERIC)
                write.writeheader()
                for item in jobs_list:
                    write = csv.DictWriter(f, fieldnames=item.keys(), quoting=csv.QUOTE_NONNUMERIC)
                    write.writerow(item)
        except IndexError:
            print('Все вакансии удалены')

    def file_cleaning(self) -> None:
        """
        Очищение файла от вакансий
        :return: None
        """
        os.remove(self.file)


class TXTSaver(Saver):
    file = os.path.join('..', 'src', 'vacancy.txt')

    def jobs_adding(self, jobs: dict) -> None:
        """
        Метод добавление данных в формате json
        :param jobs: словарь, который добавляется в файл
        :return: None
        """
        # проверка на существование файла
        if os.path.exists(self.file) is False:
            with open(self.file, 'wb') as f:
                pickle.dump([], f)
        # добавление в список вакансию
        with open(self.file, 'rb') as f:
            file = pickle.load(f, encoding='utf-8')
            file.append(jobs)
        # запись в файл
        with open(self.file, 'wb') as f:
            pickle.dump(file, f)

    def get_salary(self, salary: int) -> list:
        """
        Метод на проверку зарплаты
        :param salary: запралата
        :return: Список подходящих вакансий
        """
        with open(self.file, 'rb') as f:
            txt_date = pickle.load(f, encoding='utf-8')
            return [item for item in txt_date if int(item['_Vacancy__salary']) == salary]

    def get_city(self, city: str) -> list:
        """
        Метод на проверку города
        :param city: город
        :return: Список подходящих вакансий
        """
        with open(self.file, 'rb') as f:
            txt_date = pickle.load(f, encoding='utf-8')
            return [item for item in txt_date if item['_Vacancy__city'] == city]

    def get_experience(self, experience: str) -> list:
        """
        Метод на проверку опыта работы
        :param experience: опыт работы
        :return: Список подходящих вакансий
        """
        with open(self.file, 'rb') as f:
            txt_date = pickle.load(f, encoding='utf-8')
            return [item for item in txt_date if item['_Vacancy__experience'] == experience]

    def jobs_deleting(self, jobs: dict) -> None:
        """
        Метод на удаление выбранной вакансии
        :param jobs: словарь вакансии
        :return: None
        """
        try:
            with open(self.file, 'rb') as f:
                txt_date = pickle.load(f, encoding='utf-8')
                txt_date.remove(jobs)
            with open(self.file, 'wb') as f:
                pickle.dump(txt_date, f)
        except ValueError:
            print('Все вакансии удалены')

    def file_cleaning(self) -> None:
        """
        Очищение файла от вакансий
        :return: None
        """
        os.remove(self.file)
