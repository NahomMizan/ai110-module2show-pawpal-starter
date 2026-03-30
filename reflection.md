# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
My initial design includes four main classes: Owner, Pet, Task, and Scheduler.
The Owner class is responsible for managing pets. It stores basic owner information and keeps a list of pets.
The Pet class represents each individual pet and stores attributes like name, species, and age. It also manages a list of tasks associated with that pet.
The Task class represents a specific pet care activity, such as feeding or walking. It includes attributes like title, due date, duration, priority, and completion status.
The Scheduler class is responsible for organizing and selecting tasks to generate a daily plan. It considers constraints such as time and priority to decide which tasks should be included.

**b. Design changes**
During the design process, I realized the importance of separating responsibilities between classes. Initially, I considered storing all tasks directly within the Pet class, but I introduced a Scheduler class to centralize task management.
This change makes the system more organized and scalable, as the Scheduler can handle logic like filtering tasks by date and priority without overloading the Pet class.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers time constraints and task priority. Each task has a duration and a priority level, and the scheduler selects tasks that fit within a limited time window while prioritizing higher-priority tasks first.

I decided these constraints mattered most because a busy pet owner needs to focus on the most important tasks within the time they have available. Prioritizing tasks ensures essential care activities are not missed.

**b. Tradeoffs**

My scheduler detects conflicts only when tasks have the exact same start time.
It does not account for overlapping durations, which simplifies the implementation but may miss more complex scheduling conflicts.
This tradeoff keeps the system efficient and easier to understand.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools like GitHub Copilot to help design my system, generate class structures, and implement scheduling logic. AI was especially helpful for suggesting Python code patterns for sorting, filtering, and conflict detection.

The most helpful prompts were specific questions like how to implement sorting with lambda functions or how to detect scheduling conflicts efficiently.

**b. Judgment and verification**

One moment where I did not accept an AI suggestion as-is was when it suggested a more complex scheduling structure. I simplified the logic to keep the system easier to understand and aligned with the project requirements.

I verified AI suggestions by running my code, checking outputs in the terminal, and writing tests to ensure the behavior was correct.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, adding tasks to a pet, sorting tasks by time, recurring task generation, and conflict detection.

These tests were important because they verify that the core functionality of the system works correctly and that the scheduler behaves as expected.

**b. Confidence**

I am confident that my scheduler works correctly for standard scenarios.

If I had more time, I would test edge cases such as overlapping task durations, invalid time inputs, and handling a large number of tasks.
---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is successfully connecting the backend logic with the Streamlit UI and seeing the scheduler work in a real application.
**b. What you would improve**

If I had another iteration, I would improve the scheduling algorithm to handle overlapping durations and allow more flexible time management for tasks.

**c. Key takeaway**

One important thing I learned is how to act as the lead architect when working with AI tools. I learned that AI can generate useful code, but it is important to evaluate, simplify, and adapt those suggestions to fit the system design.
