import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# -------------------------
# INPUTS
# -------------------------
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

# -------------------------
# SESSION STATE (MEMORY)
# -------------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name)

if "pet" not in st.session_state:
    st.session_state.pet = Pet(pet_name, species, 1)
    st.session_state.owner.add_pet(st.session_state.pet)

# -------------------------
# TASK INPUT
# -------------------------
st.markdown("### Add Tasks")

col1, col2, col3 = st.columns(3)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)

with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

# -------------------------
# ADD TASK BUTTON
# -------------------------
if st.button("Add task"):
    priority_map = {"low": 1, "medium": 2, "high": 3}

    new_task = Task(
        task_title,
        date.today(),
        int(duration),
        priority_map[priority]
    )

    st.session_state.pet.add_task(new_task)
    st.success(f"Added task: {task_title}")

# -------------------------
# SHOW TASKS
# -------------------------
st.subheader("Current Tasks")

tasks = st.session_state.pet.get_tasks()

if tasks:
    for task in tasks:
        st.write(f"- {task.title} (Priority: {task.priority})")
else:
    st.info("No tasks yet. Add one above.")

# -------------------------
# GENERATE SCHEDULE
# -------------------------
st.divider()
st.subheader("Today's Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler()
    schedule = scheduler.generate_schedule(st.session_state.owner)

    if schedule:
        for task in schedule:
            st.write(f"- {task.title} (Priority: {task.priority})")
    else:
        st.warning("No tasks scheduled for today.")