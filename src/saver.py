import ujson
import os
import csv
from abc import ABC, abstractmethod
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
            return [ujson_data[item] for item in range(len(ujson_data)) if ujson_data[item]['salary'] == salary]


    def get_city(self, city: str) -> list:
        """
        Метод на проверку города
        :param city: город
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            ujson_data = ujson.load(f)
            return [ujson_data[item] for item in range(len(ujson_data)) if ujson_data[item]['city'] == city]

    def get_experience(self, experience: str) -> list:
        """
        Метод на проверку опыта работы
        :param experience: опыт работы
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            ujson_data = ujson.load(f)
            return [ujson_data[item] for item in range(len(ujson_data)) if ujson_data[item]['experience'] == experience]

    def jobs_deleting(self, jobs: dict) -> None:
        """
        Метод на удаление выбранной вакансии
        :param jobs: словарь вакансии
        :return: None
        """
        ujson_data = ujson.load(open(self.file))
        ujson_data.remove(jobs)
        try:
            with open(self.file, 'w', encoding="utf-8") as f:
                ujson.dump(ujson_data, f, indent=2, ensure_ascii=False, escape_forward_slashes=False)
        except ValueError:
            pass

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
            return [item for item in csv.DictReader(f) if int(item['salary']) == salary]

    def get_city(self, city: str) -> list:
        """
        Метод на проверку города
        :param city: город
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            return [item for item in csv.DictReader(f) if item['city'] == city]

    def get_experience(self, experience: str) -> list:
        """
        Метод на проверку опыта работы
        :param experience: опыт работы
        :return: Список подходящих вакансий
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            return [item for item in csv.DictReader(f) if item['experience'] == experience]

    def jobs_deleting(self, jobs: dict) -> None:
        """
        Метод на удаление выбранной вакансии
        :param jobs: словарь вакансии
        :return: None
        """
        file = open(self.file)
        file_csv = csv.DictReader(file)
        jobs_list = [item for item in file_csv if item != jobs]
        with open(self.file, 'w', encoding='utf-8') as f:
            write = csv.DictWriter(f, fieldnames=jobs_list[0].keys(), quoting=csv.QUOTE_NONNUMERIC)
            write.writeheader()
            for item in jobs_list:
                write = csv.DictWriter(f, fieldnames=item.keys(), quoting=csv.QUOTE_NONNUMERIC)
                write.writerow(item)


    def file_cleaning(self) -> None:
        """
        Очищение файла от вакансий
        :return: None
        """
        os.remove(self.file)


class TXTSaver(Saver):

    file = os.path.join('..', 'src', 'vacancy.txt')

    def jobs_adding(self, jobs):
        """
        Метод добавление данных в формате json
        :param jobs: словарь, который добавляется в файл
        :return: None
        """
        if os.path.exists(self.file) is False:
            with open(self.file, 'w', encoding='utf-8') as f:
                pass

    def get_salary(self, salary):
        """
        Метод на проверку зарплаты
        :param salary: запралата
        :return: Список подходящих вакансий
        """
        pass

    def get_city(self, city):
        """
        Метод на проверку города
        :param city: город
        :return: Список подходящих вакансий
        """
        pass

    def get_experience(self, experience):
        """
        Метод на проверку опыта работы
        :param experience: опыт работы
        :return: Список подходящих вакансий
        """
        pass

    def jobs_deleting(self, jobs):
        """
        Метод на удаление выбранной вакансии
        :param jobs: словарь вакансии
        :return: None
        """
        pass

    def file_cleaning(self) -> None:
        """
        Очищение файла от вакансий
        :return: None
        """
        os.remove(self.file)



# vacancy = Vacancy('Python', 100000, '1 год', 'г. Снежный, ул. Теплая, д. 6', 'https://ya.ru', 'Живой', 'gfd', 'gd')
# u = JsonSaver()
# u.jobs_adding(vacancy.__dict__)
# u.jobs_adding(vacancy.__dict__)
# vacancy.salary = 5
# u.jobs_deleting(vacancy.__dict__)

# i = CSVSaver()
# #i.jobs_adding(vacancy.__dict__)
# p = i.get_salary(5)[0]
# i.jobs_deleting(p)
# # print(i.jobs_deleting(1))