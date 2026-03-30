from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create owner
    owner = Owner("Nahom")

    # Create pets
    dog = Pet("Buddy", "Dog", 3)
    cat = Pet("Whiskers", "Cat", 2)

    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create tasks (note: include time + frequency)
    task1 = Task("Walk dog", date.today(), 30, 2, "09:00", "daily")
    task2 = Task("Feed cat", date.today(), 10, 3, "09:00")  # conflict
    task3 = Task("Play", date.today(), 20, 1, "10:00")

    # Add tasks to pets
    dog.add_task(task1)
    dog.add_task(task3)
    cat.add_task(task2)

    scheduler = Scheduler()

    # -------------------------
    # TEST 1: Sorting
    # -------------------------
    print("=== Sorted by Time ===")
    tasks = owner.get_all_tasks()
    sorted_tasks = scheduler.sort_by_time(tasks)

    for t in sorted_tasks:
        print(f"{t.title} at {t.time}")

    # -------------------------
    # TEST 2: Conflict Detection
    # -------------------------
    print("\n=== Conflicts ===")
    conflicts = scheduler.detect_conflicts(tasks)

    if conflicts:
        for c in conflicts:
            print(c)
    else:
        print("No conflicts")

    # -------------------------
    # TEST 3: Filtering
    # -------------------------
    print("\n=== Filtering (Incomplete Tasks) ===")
    filtered = scheduler.filter_tasks(tasks, completed=False)

    for t in filtered:
        print(f"{t.title} (Completed: {t.completed})")

    # -------------------------
    # TEST 4: Recurring Task
    # -------------------------
    print("\n=== Recurring Task Test ===")
    new_task = task1.mark_complete()

    if new_task:
        print(f"New recurring task created for: {new_task.due_date}")

    # -------------------------
    # TEST 5: Generate Schedule
    # -------------------------
    print("\n=== Generated Schedule (Max 60 mins) ===")
    schedule = scheduler.generate_schedule(owner, max_time=60)

    for t in schedule:
        print(f"{t.title} (Duration: {t.duration}, Priority: {t.priority})")


if __name__ == "__main__":
    main()