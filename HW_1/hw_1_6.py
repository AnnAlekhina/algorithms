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
        return self.elems.pop()

    def size(self):
        return len(self.elems)

def new_task(new_task_obj,task_str):
    new_task_obj.to_queue(task_str)
    return new_task_obj


def read_task(new_task_obj,executed_task_lst,revision_task_obj):
    do_task = new_task_obj.from_queue()
    print(do_task)
    done = {0:False,1:True}
    control_task = int(input('Задание выполнено? Если да, введите 1, если нет, введите 0'))
    if done[control_task]:
        executed_task_lst.append(do_task)
    else:
        new_task(revision_task_obj,do_task)
    return do_task


new_task_obj = QueueClass()
revision_task_obj = QueueClass()
executed_task_lst = []
key_dict ={1:True,0:False}

while True:
    task_str = input('Введите задачу: ')
    new_task(new_task_obj,task_str)
    key = int(input('Ввести еще задачу? Если да, введите 1, если нет, введите 0'))
    if not key_dict[key]
        break
read_task(new_task_obj,executed_task_lst,revision_task_obj) #todo не доделано

