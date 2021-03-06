"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


def three_best_company_1(company):
    rez_list = []  # O(1)
    list_company = list(company.items())  # O(n)
    list_company.sort(key=lambda i: i[1], reverse=True)  # O(n log n)
    for i in list_company[:3]:  # O(1)
        rez_list.append(i[0])  # O(1)
    return f'Наиболее успешные компании: {rez_list}'  # O(1)


# Общая сложность первого алгоритма -  # O(n log n)

def three_best_company_2(company):
    max_keys_list = []  # O(1)
    list_company_keys = list(company.keys())  # O(n)
    list_company_values = list(company.values())  # O(n)
    i = 0
    while i < 3:  # O(1)
        max_index = list_company_values.index(max(list_company_values))  # O(n)
        max_keys_list.append(list_company_keys[max_index])  # O(1)
        list_company_values.pop(max_index)  # O(1)
        list_company_keys.pop(max_index)  # O(1)
        i = i + 1
    return f'Наиболее успешные компании: {max_keys_list}'


# Итоговая сложность алгоритма O(n), следовательно, этот вариант лучше

company = {'рога и копыта': 1000,
           'ИП Вася Пупкин': 2000,
           'Филатов и партнеры': 500,
           'Билайн': 4000,
           'Лучшая в мире компания': 10,
           'Марфа и Семен': 100000,
           'Вигстар': 0}

print(three_best_company_1(company))
print(three_best_company_2(company))
