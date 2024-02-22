import requests

from src.api.vacancy_api import VacancyAPI


class HHVacancyAPI(VacancyAPI):
    """
    Класс для работы с API hh.ru
    """
    url = 'https://api.hh.ru/vacancies'

    def __init__(self, url=url):
        super().__init__(url)

    def get_vacancies(self, vacancy_title) -> list:
        """
        Метод получает с сайта hh.ru данные о вакансиях.
        :param vacancy_title: Название вакансии для поиска.
        :return: Список вакансий.
        """
        params = {'text': vacancy_title, 'per_page': self._count_vacancies}

        response = requests.get(self.url, params=params)
        response_json = response.json()

        return response_json.get('items', [])
