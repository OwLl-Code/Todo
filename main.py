from enter_task_module import BadIdError, BadPriorityError, BadNameError, Task
from show_tasks_module import round_display


def main():
    task_list = Task()
    round_display()

    cond_number = int(input("Выберите номер операции: "))
    while cond_number != 0:
        if cond_number == 1:
            try:
                id_task = int(input("Введите ID задачи: "))
                name = input("Введите название задачи: ")
                priority = int(input("Введите приоритет задачи: "))
                task_list.add_task(id_task, name, priority)
            except BadIdError as e:
                print(e.message)
            except BadNameError as e:
                print(e.message)
            except BadPriorityError as e:
                print(e.message)
            except Exception as e:
                print("Произошла ошибка:", e)

        elif cond_number == 2:
            task_list.show_tasks()

        elif cond_number == 3:
            round_display()

        elif cond_number == 4:
            task_list.write_to_file_using_pickle()

        elif cond_number == 5:
            task_list.read_from_file_using_pickle()

        elif cond_number == 0:
            exit()

        else:
            print("Я не понимаю, пожалуйста, выберите операцию.")

        task_list.write_to_file_using_pickle()
        task_list.read_from_file_using_pickle()

        cond_number = int(input("Выберите номер операции: "))
    print("Thank you!")


if __name__ == "__main__":
    print("main.py - Я работаю самостоятельно, как независимый модуль.")
    main()
else:
    print("main.py - Я запущена как импортируемый модуль.")
