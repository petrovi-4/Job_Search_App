import os

import pytest

from config import ROOT_DIR
from src.json_vacancy_data import JSONVacancyData


@pytest.fixture
def json_vacancy_data(tmpdir):
    # Создаем временный файл для тенстов.
    temp_file = ROOT_DIR / "test_vacancies.json"
    return JSONVacancyData(temp_file)


def test_add_vacancies(json_vacancy_data):
    # Список словарей вакансий.
    vacancies = [
        {"title": "Программист", "salary": 100_000, "city": "Москва"},
        {"title": "Аналитик данных", "salary": 120_000, "city":
            "Санкт-Петербург"}
    ]

    # Добавляем вакансии в JSON-файл
    json_vacancy_data.add_vacancies(vacancies)

    # Читаем данные из файла и проверяем их соответствие добавленным вакансиям.
    assert json_vacancy_data.get_data_from_file() == vacancies


def test_remove_data_from_file(json_vacancy_data):
    # Определяем некоторые образцовые вакансии
    vacancies = [
        {"title": "Программист", "salary": 100000, "city": "Москва"},
        {"title": "Аналитик данных", "salary": 120000,
         "city": "Санкт-Петербург"}
    ]

    # Добавляем вакансии в JSON-файл
    json_vacancy_data.add_vacancies(vacancies)

    # Удаляем данные из файла
    json_vacancy_data.remove_data_from_file()

    # Проверяем, пуст ли файл после удаления
    assert os.stat(json_vacancy_data.filename).st_size == 0


def test_get_data_from_file_empty(tmpdir):
    # Создаем пустой JSON-файл
    temp_file = tmpdir.join("empty_vacancies.json")
    temp_file.write("[]")

    # Инициализируем JSONVacancyData пустым файлом
    json_vacancy_data = JSONVacancyData(temp_file)
