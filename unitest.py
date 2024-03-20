import unittest
from enter_task_module import Task, BadIdError, BadNameError, BadPriorityError


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task_instance = Task()

    def test_add_task_success(self):
        task_added = self.task_instance.add_task(1, "Task name", 5)
        self.assertIn(task_added, self.task_instance.todo_list)

    def test_add_task_bad_id(self):
        with self.assertRaises(BadIdError):
            self.task_instance.add_task(0, "Task name", 5)

    def test_add_task_bad_name(self):
        with self.assertRaises(BadNameError):
            self.task_instance.add_task(1, "Short", 5)

    def test_add_task_bad_priority(self):
        with self.assertRaises(BadPriorityError):
            self.task_instance.add_task(1, "Task name", 20)

    def test_read_write_pickle(self):
        self.task_instance.add_task(1, "Task 1", 10)
        self.task_instance.add_task(2, "Task 2", 8)
        self.task_instance.write_to_file_using_pickle()
        self.task_instance.read_from_file_using_pickle()
        self.assertEqual(self.task_instance.todo_list, ["№1Task 110", "№2Task 2810"])


if __name__ == "__main__":
    unittest.main()
