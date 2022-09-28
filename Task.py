from typing import List
import csv


class Task:
    def __init__(self, length, name, parents: List["Task"] = None):
        if parents is None:
            parents = []
        self.length = length
        self.parents = parents
        self.name = name
        self.faz = 0
        for parent in parents:
            self.faz = max(parent.fez, self.faz)
        self.fez = self.faz + self.length

        self.sez = None
        self.saz = None
        self.gp = None

    def mark_as_end(self):
        self.sez = self.fez
        self.saz = self.sez - self.length
        self.gp = 0
        self.from_down()

    def from_down(self):
        for parent in self.parents:
            if parent.sez is None:
                parent.sez = self.saz
                parent.saz = parent.sez - parent.length
            else:
                parent.sez = min(parent.sez, self.saz)
                parent.saz = min(parent.sez - parent.length, self.saz)

            parent.gp = parent.sez - parent.fez

            parent.from_down()

    def __repr__(self):
        representation = f"TASK :{self.name}, {self.length}\n"
        representation += f"{self.faz}, {self.gp}, {self.fez}\n"
        representation += f"{self.saz}, 0, {self.sez}\n"
        return representation


def convert_csv_to_flowchart(filename):
    reader = csv.reader(open(filename))
    flow_chart = "digraph {\n"
    to_be_filed = {x[0]: x for x in reader}
    index = {}
    child_free = []
    parent_free = []
    while len(to_be_filed) != 0:
        for child, row in {x: y for x, y in to_be_filed.items()}.items():
            # check if all dependecies have been made yet
            dep_list = row[2].split(",")
            dep_list = dep_list if dep_list[0] else []
            depend = all(map(lambda x: x in index, dep_list))
            if not depend:
                continue
            if not dep_list:
                parent_free.append(row[0])
            if not row[3]:
                child_free.append(row[0])

            to_be_filed.pop(child)
            parents = [index[x] for x in index if x in dep_list]
            for x in dep_list:
                flow_chart += f"{x}->{child}\n"
            index[row[0]] = Task(int(row[1]), child, parents)

    for x in index:
        if x in child_free:
            index[x].mark_as_end()

    for x in index:
        flow_chart += f"{x} [label=\"{index[x]}\"]\n"
    flow_chart += "}"
    return flow_chart