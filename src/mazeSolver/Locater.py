from __future__ import annotations


class Locater:

    def __init__(self, x, y, parent: Locater, path):
        self.x = x
        self.y = y
        self.parent = parent
        self.path = path + "(" + str(x) + "," + str(y) + "),"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        if self.parent is None:
            return "({}, {}); Parent: None; Path: {}".format(self.x, self.y, self.path)
        else:
            return "({}, {}); Parent: ({}, {}); Path: {}".format(self.x, self.y, self.parent.x, self.parent.y, self.path[:-1])

    def __repr__(self):
        return str(self)

    @staticmethod
    def add_this_child(child, max_x, max_y):
        return 0 <= child.x <= max_x and 0 <= child.y <= max_y

    def children(self, max_x, max_y):

        child_a = Locater(self.x, self.y + 1, self, self.path)
        child_b = Locater(self.x, self.y - 1, self, self.path)
        child_c = Locater(self.x + 1, self.y, self, self.path)
        child_d = Locater(self.x - 1, self.y, self, self.path)
        child_e = Locater(self.x + 1, self.y + 1, self, self.path)
        child_f = Locater(self.x - 1, self.y - 1, self, self.path)

        result = []

        if self.add_this_child(child_a, max_x, max_y):
            result.append(child_a)

        if self.add_this_child(child_b, max_x, max_y):
            result.append(child_b)

        if self.add_this_child(child_c, max_x, max_y):
            result.append(child_c)

        if self.add_this_child(child_d, max_x, max_y):
            result.append(child_d)

        if self.add_this_child(child_e, max_x, max_y):
            result.append(child_e)

        if self.add_this_child(child_f, max_x, max_y):
            result.append(child_f)

        return result
