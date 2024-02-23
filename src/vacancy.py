import datetime
import json

from src.api.hh_vacancy_api import HHVacancyAPI


class Vacancy:
    """
    Класс для работы с вакансиями.
    """
    all = []

    def __init__(self, title, url, salary, salary_currency, date, city):
        self.title = title
        self.url = url
        self.salary = salary
        self.salary_currency = salary_currency
        self.date = date
        self.city = city
        self.all.append(self.__dict__)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title_vacancy):
        self.__title = title_vacancy

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url_vacancy):
        self.__url = url_vacancy

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary_vacancy):
        self.__salary = salary_vacancy

    @property
    def salary_currency(self):
        return self.__salary_currency

    @salary_currency.setter
    def salary_currency(self, salary_curency_vacancy):
        self.__salary_currency = salary_curency_vacancy

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date_vacancy):
        self.__date = date_vacancy

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city_vacancy):
        self.__city = city_vacancy

    def __str__(self):
        return (f'Вакансия: {self.title}, зарплата до {self.salary} '
                f'{self.salary_currency}, дата публикации: {self.date}, '
                f'город: {self.city}, url: {self.url}')

    def __gt__(self, other):
        return int(self.salary) > int(other.salary)

    def __ge__(self, other):
        return int(self.salary) >= int(other.salary)

    @classmethod
    def instance_from_list(cls, vacancy_title) -> None:
        """
        Метод класса инициализирующий экземпляры класса данными из списка.
        :param vacancy_title: Название вакансии
        :return:
        """
        hh_vacancies = HHVacancyAPI().get_vacancies(vacancy_title)
        for hh_vacancy in hh_vacancies:
            title = hh_vacancy['name']
            url = hh_vacancy['alternate_url']
            if hh_vacancy['salary']:
                salary = None
                salary_currency = hh_vacancy['salary']['currency']
            else:
                salary = None
                salary_currency = None
            date = datetime.datetime.strptime(
                hh_vacancy['published_at'], '%Y-%m-%dT%H:%M:').strftime(
                '%d.%m.%Y')
            city = hh_vacancy['area']['name']
            cls(title, url, salary, salary_currency, date, city)

    @classmethod
    def instance_from_json(cls, filename='../vacancies.json') -> None:
        """
        Метод класса инициализирующий экземпляр класса данными из json-файла.
        :param filename: Название файла
        :return: None
        """
        cls.all = []
        try:
            with open(filename, 'rt', encoding='utf-8') as file:
                data = json.load(file)
                for line in data:
                    cls(line["_Vacancy__title"], line["_Vacancy__url"],
                        line["_Vacancy__salary"], line[
                            "_Vacancy__salary_currency"],
                        line["_Vacancy__date"], line["_Vacancy__city"])
        except FileNotFoundError:
            print('Отсутствует файл для чтения')

    @classmethod
    def filtering_vacancies_by_city(cls, city) -> list:
        """
        Метод класса фильтрующий список вакансий по городу
        :param city: Город
        :return: Список вакансий из указанного города
        """
        vacancies_city = []
        vacancies = cls.all
        for vacancy in vacancies:
            if vacancy['_Vacancy__city'] == city:
                vacancies_city.append(vacancy)
            return vacancies_city

    @classmethod
    def filtering_vacancies_by_salary(cls, salary) -> list:
        """
        Метод класса фильтрующий список вакансий по зарплате.
        :param salary: Минимальная зарплата для вывода
        :return: Список вакансий с зарплатой большей или равной указанной
        """
        vacancies_salary = []
        vacancies = Vacancy.filters_the_list(Vacancy.all)
        for vacancy in vacancies:
            if vacancy["_Vacancy__salary"] >= salary:
                vacancies_salary.append(vacancy)
            else:
                vacancies_salary = []
        return vacancies_salary

    @staticmethod
    def sort_the_list(vacancies) -> list:
        """
        Статический метод, который сортирует список вакансий по зарплате.
        :param vacancies: Список вакансий
        :return: Отсортированный список вакансий
        """
        vacancies_filter = Vacancy.filters_the_list(vacancies)
        vacancies_sort = sorted(vacancies_filter, key=lambda s: s[
            "_Vacancy__salary"], reverse=True)
        return vacancies_sort

    @staticmethod
    def filters_the_list(all_vacancies):
        """
        Статический метод, который фильтрует список вакансий по зарплате.
        :param all_vacancies: Список вакансий
        :return: Список содержащий те вакансии, где указана зарплата в RUR
        """
        vacancies = []
        for vacancy in all_vacancies:
            if vacancy.get("_Vacancy__salary") is not None and vacancy.get(
                    "_Vacancy__salary_currency") == "RUR":
                vacancies.append(vacancy)
        return vacancies

    @staticmethod
    def print_formatted_vacancies_list(list_vacancies, number_vacancies=None) \
            -> None:
        """
        Печатает данные о вакансиях для пользователя
        :param list_vacancies: Список вакансий
        :param number_vacancies: Количество вакансий для вывода
        :return: None
        """
        if not list_vacancies:
            print('В файле отсутствуют данные о вакансиях')
        else:
            if number_vacancies is None or number_vacancies > len(
                    list_vacancies):
                number_vacancies = len(list_vacancies)
            for index in range(number_vacancies):
                if list_vacancies[index]['_Vacancy__salary']:
                    print(
                        f"Вакансия: {list_vacancies[index]['_Vacancy__title']}, зарплата до "
                        f"{list_vacancies[index]['_Vacancy__salary']}"
                        f" {list_vacancies[index]['_Vacancy__salary_currency']}, дата публикации: "
                        f"{list_vacancies[index]['_Vacancy__date']}, город: {list_vacancies[index]['_Vacancy__city']}, "
                        f"url: {list_vacancies[index]['_Vacancy__url']}")

                else:
                    print(
                        f"Вакансия: {list_vacancies[index]['_Vacancy__title']}, зарплата не указана, дата публикации: "
                        f"{list_vacancies[index]['_Vacancy__date']}, город: {list_vacancies[index]['_Vacancy__city']}, "
                        f"url: {list_vacancies[index]['_Vacancy__url']}")