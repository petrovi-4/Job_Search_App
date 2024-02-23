import json
from json import JSONDecodeError
from src.vacancy_data import VacancyData


class JSONVacancyData(VacancyData):
    """
    Класс для работы с JSON файлом.
    """
    def __init__(self, filename='vacancies.json'):
        self.filename = filename

    def add_vacancies(self, vacancies) -> None:
        """
        Записывает найденные вакансии в файл.
        :param vacancies: Список вакансий
        :return: None
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)

    def get_data_from_file(self):
        """
        Получает информацию о вакансиях из json-файла.
        :return: Список вакансий. Если файл пустой - пустой список
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                json_file = json.load(file)
                return json_file
        except JSONDecodeError:
            return []

    def remove_data_from_file(self) -> None:
        """
        Удаляет из json-файла данные о вакансиях.
        :return: None
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.seek(0)
            file.truncate()
