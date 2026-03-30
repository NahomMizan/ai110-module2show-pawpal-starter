from dataclasses import dataclass, field
from typing import List
from datetime import date


@dataclass
class Task:
    title: str
    due_date: date
    duration: int
    priority: int
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


class Owner:
    def __init__(self, name: str):
        """Initialize an owner with a name and empty pet list."""
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_pets(self) -> List[Pet]:
        """Return all pets owned."""
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks


class Scheduler:
    def get_tasks_for_today(self, owner: Owner) -> List[Task]:
        """Return tasks due today."""
        today = date.today()
        return [task for task in owner.get_all_tasks() if task.due_date == today]

    def generate_schedule(self, owner: Owner) -> List[Task]:
        """Return today's tasks sorted by priority."""
        tasks = self.get_tasks_for_today(owner)
        return sorted(tasks, key=lambda t: t.priority, reverse=True)