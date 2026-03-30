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

    # Create tasks
    task1 = Task("Walk the dog", date.today(), 30, 2)
    task2 = Task("Feed the cat", date.today(), 10, 3)
    task3 = Task("Play with dog", date.today(), 20, 1)

    # Assign tasks
    dog.add_task(task1)
    dog.add_task(task3)
    cat.add_task(task2)

    # Generate schedule
    scheduler = Scheduler()
    schedule = scheduler.generate_schedule(owner)

    print("Today's Schedule:")
    for task in schedule:
        print(f"- {task.title} (Priority: {task.priority})")


if __name__ == "__main__":
    main()