from dataclasses import dataclass, field
from typing import List
from datetime import date, timedelta


@dataclass
class Task:
    title: str
    due_date: date
    duration: int
    priority: int
    time: str  # HH:MM format
    frequency: str = "once"  # "daily", "weekly"
    completed: bool = False

    def mark_complete(self):
        """Mark task complete and generate next occurrence if recurring."""
        self.completed = True

        if self.frequency == "daily":
            return Task(
                self.title,
                self.due_date + timedelta(days=1),
                self.duration,
                self.priority,
                self.time,
                self.frequency,
            )

        if self.frequency == "weekly":
            return Task(
                self.title,
                self.due_date + timedelta(days=7),
                self.duration,
                self.priority,
                self.time,
                self.frequency,
            )

        return None


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

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by time (HH:MM)."""
        return sorted(tasks, key=lambda t: t.time)

    def filter_tasks(self, tasks: List[Task], completed: bool = None) -> List[Task]:
        """Filter tasks by completion status."""
        if completed is None:
            return tasks
        return [task for task in tasks if task.completed == completed]

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Detect tasks scheduled at the same time."""
        seen = {}
        conflicts = []

        for task in tasks:
            if task.time in seen:
                conflicts.append(
                    f"Conflict: {task.title} overlaps with {seen[task.time]}"
                )
            else:
                seen[task.time] = task.title

        return conflicts

    def generate_schedule(self, owner: Owner, max_time: int = 60) -> List[Task]:
        """Generate a schedule based on priority and time constraint."""
        tasks = self.get_tasks_for_today(owner)

        # Sort by priority (highest first)
        tasks = sorted(tasks, key=lambda t: t.priority, reverse=True)

        selected_tasks = []
        total_time = 0

        for task in tasks:
            if total_time + task.duration <= max_time:
                selected_tasks.append(task)
                total_time += task.duration

        return selected_tasks