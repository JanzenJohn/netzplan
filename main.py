from Task import Task


tasks = {
    1: Task(1)
}

tasks[2] = Task(2, [tasks[1]])
tasks[3] = Task(4, [tasks[1]])

tasks[4] = Task(5, [tasks[2], tasks[3]])
tasks[4].mark_as_end()

for task_no in tasks:
    print(f"Task no {task_no}")
    print(tasks[task_no])

