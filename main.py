from Task import Task
import csv

reader = csv.reader(open("x.csv"))

to_be_filed = {x[0]: x for x in reader}
index = {}
child_free = []
while len(to_be_filed) != 0:
    for child, row in {x: y for x, y in to_be_filed.items()}.items():
        # check if all dependecies have been made yet
        dep_list = row[2].split(",")
        dep_list = dep_list if dep_list[0] else []
        depend = all(map(lambda x: x in index, dep_list))

        if not depend:
            continue
        if not row[3]:
            child_free.append(row[0])

        to_be_filed.pop(child)
        parents = [index[x] for x in index if x in dep_list]
        index[row[0]] = Task(int(row[1]), parents)

for x in index:
    if x in child_free:
        index[x].mark_as_end()

for x in index:
    print(f"Node {x}")
    print(index[x])