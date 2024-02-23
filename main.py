from src.api.hh_vacancy_api import HHVacancyAPI
from src.json_vacancy_data import JSONVacancyData
from src.utils import display_top_vacancies_by_salary, filters_and_display_vacancies
from src.vacancy import Vacancy


def user_interaction():
    """
    Функция для взаимодействия с пользователем.
    """
    while True:
        vacancy_title = input('Введите ключевое слово для поиска вакансий\n')
        if not HHVacancyAPI().get_vacancies(vacancy_title):
            print('По вашему запросу ничего не найдено. Измените параметры '
                  'запроса')
            continue
        else:
            break
    Vacancy.instance_from_list(vacancy_title)
    print(f'По вашему запросу {vacancy_title} получены вакансии.')

    while True:
        user_input = input(
            'Выберите дальнейшие действия:\n1 - Вывести на экран все '
            'найденные вакансии\n2 - Сохранить вакансии в файл\n'
            '3 - Вывести топ N вакансий по зарплате\n4 - Ввести дополнительные данные '
            'для фильтрации вакансий\n5 - Вывести информацию о вакансиях из файла\n6 - Удалить '
            'информацию о вакансиях из файла\n7 - Новый поиск\n8 - Выход\n'
        )

        if user_input == '1':
            Vacancy.print_formatted_vacancies_list(Vacancy.all)
            continue
        elif user_input == '2':
            JSONVacancyData().add_vacancies(Vacancy.all)
            print('Вакансии сохранены в файл')
        elif user_input == '3':
            display_top_vacancies_by_salary()
        elif user_input == '4':
            filters_and_display_vacancies()
        elif user_input == '5':
            vacancies_from_file = JSONVacancyData().get_data_from_file()
            Vacancy.print_formatted_vacancies_list(vacancies_from_file)
        elif user_input == '6':
            JSONVacancyData().remove_data_from_file()
            print('Информация о вакансиях удалена')
        elif user_input == '7':
            user_interaction()
            break
        elif user_input == '8':
            print('Работа программы завершена! Скоро увидимся!')
            break
        else:
            print('Не корректный ввод')
            break


if __name__ == '__main__':
    print('Добрый день!')
    user_interaction()

