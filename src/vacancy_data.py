from abc import ABC, abstractmethod


class VacancyData(ABC):
    """
    Абстрактный класс для работы с файлом для хранения вакансий.
    """
    @abstractmethod
    def add_vacancies(self, vacancy):
        pass

    @abstractmethod
    def get_data_from_file(self):
        pass

    @abstractmethod
    def remove_data_from_file(self):
        pass
