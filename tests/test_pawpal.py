from datetime import date, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_completion():
    task = Task("Test", date.today(), 10, 1, "09:00")
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog", 3)
    task = Task("Walk", date.today(), 20, 2, "10:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_sort_by_time():
    scheduler = Scheduler()

    t1 = Task("Task1", date.today(), 10, 1, "10:00")
    t2 = Task("Task2", date.today(), 10, 1, "09:00")

    sorted_tasks = scheduler.sort_by_time([t1, t2])

    assert sorted_tasks[0].time == "09:00"
    assert sorted_tasks[1].time == "10:00"


def test_recurring_task():
    task = Task("Daily Task", date.today(), 10, 1, "09:00", "daily")

    new_task = task.mark_complete()

    assert new_task is not None
    assert new_task.due_date == date.today() + timedelta(days=1)


def test_conflict_detection():
    scheduler = Scheduler()

    t1 = Task("Task1", date.today(), 10, 1, "09:00")
    t2 = Task("Task2", date.today(), 10, 1, "09:00")

    conflicts = scheduler.detect_conflicts([t1, t2])

    assert len(conflicts) == 1