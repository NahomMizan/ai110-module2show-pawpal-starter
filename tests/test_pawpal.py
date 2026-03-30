from datetime import date
from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Test task", date.today(), 10, 1)
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog", 3)
    task = Task("Walk", date.today(), 20, 2)

    pet.add_task(task)

    assert len(pet.tasks) == 1