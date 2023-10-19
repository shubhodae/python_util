
class ToDo:

    def __init__(self, name):
        self._name = name
        self._task_list = list()

    def add_task(self, task):
        self._task_list.append(task)

    def __add__(self, task):
        self._task_list.append(task)

    def get_tasks(self):
        return self._task_list
    
    def __str__(self) -> str:
        return self._name
    
    def __len__(self) -> int:
        return len(self._task_list)


todo = ToDo("Today")

# todo.add_task("office work")
# todo.add_task("go to gym")
# todo.add_task("practice meditation")

todo + "office work"
todo + "go to gym"
todo + "practice meditation"

tasks = todo.get_tasks()

print(f"Task name: {todo} || Total task count: {len(todo)}")
for task in todo.get_tasks():
    print(task)