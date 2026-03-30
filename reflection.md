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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

My scheduler detects conflicts only when tasks have the exact same start time.
It does not account for overlapping durations, which simplifies the implementation but may miss more complex scheduling conflicts.
This tradeoff keeps the system efficient and easier to understand.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
