from typing import List


class Task:
    def __init__(self, length, parents: List["Task"] = None):
        if parents is None:
            parents = []
        self.length = length
        self.parents = parents
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
        representation = f"{self.faz}, {self.gp}, {self.fez}\n"
        representation += f"{self.saz}, 0, {self.sez}\n"
        return representation