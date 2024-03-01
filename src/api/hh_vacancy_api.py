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
        params = {'text': vacancy_title, 'per_page': self._count_vacancies}
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            response_json = response.json()
            return response_json.get('items', [])
        except requests.exceptions.RequestException as error:
            print(f'Ошибка получения данных: {error}')


if __name__ == '__main__':
    find = HHVacancyAPI()
    vacancies = find.get_vacancies('python')
    print(vacancies)
