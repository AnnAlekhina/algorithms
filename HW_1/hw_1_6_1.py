"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        el = self.elems.pop()
        print(el)
        return el

    def size(self):
        return len(self.elems)

    def new_task(self):
        task = input('Введите новую задачу: ')
        return self.to_queue(task)

    def done_task(self):
        pass #todo


def stop_app():
    work_app = False
    return work_app


to_do_queue = QueueClass()
revision_queue = QueueClass()
done_lst = []
while True:
    options_dict = {'0': to_do_queue.new_task,
                    '1': to_do_queue.from_queue,
                    '2': revision_queue.from_queue,
                    '3': stop_app}
    key_options = input('0 - добавить новую задачу\n'
                        '1 - посмотреть новую задачу\n'
                        '2 - посмотреть задачу на доработку\n'
                        '3 - Выйти из приложения\n'
                        ': ')
    if key_options == '3':
        break
    try:
        options_dict[key_options]()
    except IndexError as err:
        print(f'Список задач пуст\n'
              f'{err}')
    except KeyError as err:
        print(f'Введен неверный ключ\n'
              f'{err}')

    c = 1
