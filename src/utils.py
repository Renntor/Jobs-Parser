import ujson

from src.saver import JsonSaver, TXTSaver, CSVSaver
from src.vacancy import Vacancy
from src.jobs import HhApi, SuperJobApi


def user_interaction():
    """
    Взаимодействие с пользователем
    """
    search_vacancy = input("Напишите название профессии: ")

    hh = HhApi(search_vacancy)
    get_hh = hh.get_vacancies()

    superjob = SuperJobApi(search_vacancy)
    get_superjpv = superjob.get_vacancies()

    json_saver = JsonSaver()
    csv_saver = CSVSaver()
    txt_saver = TXTSaver()

    # записывание данные от НН в класс Vacancy и сохраняет их в файл
    for item in get_hh['items']:
        address = item['address']
        salary = item['salary']

        if item['salary'] is not None:
            salary = item['salary']['from']

        if item['address'] is not None:
            address = item['address']['street']

        type_experience = {'Нет опыта': 'Без опыта', 'От 1 года до 3 лет': "От 1 года",
                           'От 3 до 6 лет': 'От 3 лет', 'Более 6 лет': 'От 6 лет', 'Не имеет значения': 'Без опыта'}
        experience = type_experience[item['experience']['name']]

        vacancy = Vacancy(item['name'], salary, experience,
                         address, item['employment']['name'], item['area']['name'],
                         item['alternate_url'], item['snippet']['requirement'])

        json_saver.jobs_adding(vacancy.__dict__)
        csv_saver.jobs_adding(vacancy.__dict__)
        txt_saver.jobs_adding(vacancy.__dict__)

    # записывание данные от superjob в класс Vacancy и сохраняет их в файл
    for item in get_superjpv['objects']:

        vacancy = Vacancy(item['profession'], item['payment_from'], item['experience']['title'], item['address'],
                          item['type_of_work']['title'], item['town']['title'], item['link'], item['candidat'])

        json_saver.jobs_adding(vacancy.__dict__)
        csv_saver.jobs_adding(vacancy.__dict__)
        txt_saver.jobs_adding(vacancy.__dict__)

    try:
        filter_one = json_saver.get_city(input("Укажите город для поиска: "))
        filter_two = json_saver.get_salary(int(input('Укажите зарплату для поиска: ')))
        filter_three = json_saver.get_experience(input("""Укажите опыт работы для поиска("Без опыта", "От 1 года",\
"От 3 лет", "От 6 лет"): """))
        filter_number_vacancy = int(input('Укажите количества вакансий для вывода: '))
        filtered_vacancy = []

        for i in filter_one:  # проверка на пересечение вакансий
            if i in filter_two and i in filter_three:
                filtered_vacancy.append(i)

        if len(filtered_vacancy) > 0 and filter_number_vacancy > 0:
            for i in filtered_vacancy:
                print(ujson.dumps(i, ensure_ascii=False, escape_forward_slashes=False, indent=2))
                filter_number_vacancy -= 1
        else:
            print("Нет вакансий, соответствующих заданным критериям.")

        while True:
            del_file = input('Удалить файл с вакансиями(Y/N): ')
            if del_file.upper() == 'Y':
                json_saver.file_cleaning()
                csv_saver.file_cleaning()
                txt_saver.file_cleaning()
                break
            elif del_file.upper() == 'N':
                break

    except TypeError as e:
        print(f'{e}("Количество вакансий и зарплата должны быть числами")')
