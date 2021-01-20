"""Author - Maksim Sapunov, msdir6199@gmail.com, 2/01/2021"""

# task_2 Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

import datetime as dt
import json


def user_info(name: str, surname: str, year: int, city: str, email: str, phone: str):
    """
    Функция реализует создание информационной строки о пользователе
    :param name: Имя пользователя
    :param surname: Фамилия пользователя
    :param year: Год рождения пользователя
    :param city: Город проживания пользователя
    :param email: E-mail
    :param phone: Номер телефона пользователя
    :return: str параметры через запятую.
    """

    # создаем строку из полученных параметров и распечатываем еe (основная задача)
    string = name + " " + surname + ", " + str(year) + " г.р." + ", " + city + ", " + email + ", " + phone
    print(string.title())
    return string


def new_user():
    """
    Функция запрашивает данные о пользователе и возвращает их в виде словаря
    In: None
    :return dict add_user{}
    """
    print('Здравствуйте гость! Авторизируйтесь ')

    # запрашиваем данные для ввода
    name = input('Введите имя пользователя: ')
    surname = input('Введите фамилию пользователя: ')
    year = int(input('Введите год рождения пользователя: '))
    city = input('Введите город проживания пользователя: ')
    e_mail = input('Введите e-mail пользователя: ')
    phone = input('Введите номер телефона пользователя: ')

    # создаем формализованный словарь из полученных данных
    add_user = {
        "name": name,
        "surname": surname,
        "year": year,
        "city": city,
        "e-mail": e_mail,
        "phone": phone
        }
    return add_user


def save_user(data_user: dict):
    """
    Сохраняет данные, полученные в ходе выполнения программы, в файл
    :param data_user dict (словарь с данными пользователя)
    :return None
    """
    # формируем данные для сохранения и указываем место хранения
    file = 'txt_files/user_info.json'
    text = user_info(
        data_user['name'],
        data_user['surname'],
        data_user['year'],
        data_user['city'],
        data_user['e-mail'],
        data_user['phone']) + str(dt.datetime.utcnow())
    # сохраняем данные в файл
    try:
        with open(file, 'a') as f_1:
            json.dump(text, f_1)
            print('Данные о пользователе сохранены в файл: успешно')
    except FileNotFoundError:
        print('Ошибка сохранения в файл: не удалось найти или создать файл ')


# основной блок программы
user = new_user()
save_user(user)
