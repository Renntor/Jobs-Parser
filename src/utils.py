import ujson

from src.saver import JsonSaver, TXTSaver, CSVSaver
from src.vacancy import Vacancy
from src.jobs import HhApi, SuperJobApi


def user_interaction():
    """
    Взаимодействие с пользователем
    """

    # search_vacancy = input("Напишите название профессии: ")
    search_vacancy = 'Python'
    hh = HhApi(search_vacancy)
    get_hh = hh.get_vacancies()

    # superjob = SuperJobApi(search_vacancy)
    # get_superjpv = superjob.get_vacancies()

    json_saver = JsonSaver()
    csv_saver = CSVSaver()
    txt_saver = TXTSaver()

    # записывание данные от НН в класс Vacancy c сохранением в файл
    for item in get_hh['items']:
        address = item['address']
        salary = item['salary']

        if item['salary'] is not None:
            salary = item['salary']['from']

        if item['address'] is not None:
            address = item['address']['street']

        vacancy = Vacancy(item['name'], salary, item['experience']['name'],
                         address, item['employment']['name'], item['area']['name'],
                         item['alternate_url'], item['snippet']['requirement'])

        json_saver.jobs_adding(vacancy.__dict__)
        csv_saver.jobs_adding(vacancy.__dict__)
        txt_saver.jobs_adding(vacancy.__dict__)

    # записывание данные от НН в класс Vacancy c сохранением в файл
    for item in get_superjpv:
        pass

        json_saver.jobs_adding(vacancy.__dict__)
        csv_saver.jobs_adding(vacancy.__dict__)
        txt_saver.jobs_adding(vacancy.__dict__)

    filer_city = input("Укажите город для поиска: ")
    filer_salary = input('Укажите зарплату для поиска: ')
    filer_experience = input('Укажите опыт работы для поиска: ')


    t = json_saver.get_city('Москва')

    for i in t:
        print(ujson.dumps(i, ensure_ascii=False, escape_forward_slashes=False, indent=2))

user_interaction()