class Locater:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return str(self)

    @staticmethod
    def add_this_child(child, max_x, max_y):
        return 0 <= child.x <= max_x and 0 <= child.y <= max_y

    def children(self, max_x, max_y):

        child_a = Locater(self.x, self.y + 1)
        child_b = Locater(self.x, self.y - 1)
        child_c = Locater(self.x + 1, self.y)
        child_d = Locater(self.x - 1, self.y)
        child_e = Locater(self.x + 1, self.y + 1)
        child_f = Locater(self.x - 1, self.y - 1)

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
