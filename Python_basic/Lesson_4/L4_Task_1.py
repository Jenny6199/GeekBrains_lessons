"""Author - Maksim Sapunov, msdir6199@gmail.com 15/01/2021"""

# Задача #1: реализовать скрипт, в котором доллжна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка на час)+премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, work_hours, hour_price, cake = argv

print("Расчет заработной платы сотрудника. Имя файла: ", script_name)
print('---------------------------------')
print("Количество часов работы сотрудника: ", work_hours)
print("Cтоимость одного часа работы сотрудника: ", hour_price)
print("Cумма премии для сотрудника в данном месяце: ", cake)
print('---------------------------------')
print(f'Заработная плата сотрудника в данном месяце составит {(float(work_hours)*float(hour_price))+float(cake)} руб.')
