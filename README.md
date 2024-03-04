# Job Search App
Job search app - это приложение для поиска работы из [API сайта hh.ru](https://api.hh.ru/openapi/redoc#tag/Perepiska-(otklikipriglasheniya)-dlya-soiskatelya/operation/get-negotiation-messages)

Пользователь может осуществлять поиск вакансий по ключевым словам, сортировать вакансии по заработной плате, фильтровать вакансии по дополнительным параметрам, а так же сохранять найденные вакансии в файл, получать и удалять вакансии из файла

## Технологии
**- Python 3.12**  
**- Requests**  
**- Pytest**  
**- Poetry**


## Установка

##### 1. Склонировать репозиторий:  
`git clone https://github.com/petrovi-4/coursework_4.git`

##### 2. Установить пакетный менеджер Poetry:  
`pip install poetry`

##### 3. Перейти в папку проекта:  
`cd coursework_4`

##### 4. Установить необходимые для работы зависимости:  
`poetry install`


## Использование 
Для запуска приложения необходимо выполнить команду:  
`python main.py`  

После запуска приложения необходимо ввести запрос для поиска вакансий, отфлитровать вакансии по дополнительным критериям при необходимости, сохранить в файл полученный результат, а так же можно получить вакансии из файла и удалить вакансии из файла

****

**Автор**  
[Мартынов Сергей](https://github.com/petrovi-4)

![GitHub User's stars](https://img.shields.io/github/stars/petrovi-4?label=Stars&style=social)
![licence](https://img.shields.io/badge/licence-GPL--3.0-green)
