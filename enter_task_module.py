import pickle


# Объявляем кастомные исключения
class BadIdError(Exception):
    def __init__(self, id_task, message):
        self.id_task = id_task
        self.message = message


class BadNameError(Exception):
    def __init__(self, name_of_task, message):
        self.name_of_task = name_of_task
        self.message = message


class BadPriorityError(Exception):
    def __init__(self, priority, message):
        self.priority = priority
        self.message = message


# Класс для работы с задачами
class Task:
    def __init__(self):
        self.todo_list = []

    # Функция для добавления задачи
    def add_task(self, id_task, name, priority):
        if id_task < 1 or id_task > 100:
            raise BadIdError(self, "Неправильный ID")

        if len(name) < 7:
            raise BadNameError(self, "Имя задачи должно быть больше 7 символов")

        if priority < 1 or priority > 15:
            raise BadPriorityError(self, "Приоритет задачи от 1 до 15 включительно")

        task_for_record = f"№{id_task}{name}{priority}"
        self.todo_list.append(task_for_record)
        return task_for_record

    # Функция для отображения списка задач
    def show_tasks(self):
        for task in self.todo_list:
            print(task)

    # Функция для записи задач в файл с помощью pickle
    def write_to_file_using_pickle(self):
        with open("todo_list.pkl", "wb") as file_for_text:
            pickle.dump(self.todo_list, file_for_text)
        print("Задачи сохранены")

    # Функция для чтения задач из файла с помощью pickle
    def read_from_file_using_pickle(self):
        print("Список имеющихся задач:")
        with open("todo_list.pkl", "rb") as file_for_text:
            data_todo = pickle.load(file_for_text)
            for task in data_todo:
                print(task)


if __name__ == "__main__":
    print("enter_task_module.py - Я работаю самостоятельно, как независимый модуль.")
else:
    print("enter_task_module.py - Я запущена как импортируемый модуль.")
