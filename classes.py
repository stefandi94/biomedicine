class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        print('(x, y) = ({}, {})'.format(self.x, self.y))


class Bone:

    def __init__(self, points):
        self.points = points

    def toString(self):
        for point in self.points:
            point.toString()

class Joint:

    def __init__(self, upper_bone, lower_bone):
        self.upper_bone = upper_bone
        self.lower_bone = lower_bone

    def toString(self):
        print('Upper bone:')
        self.upper_bone.toString()
        print('Lower bone:')
        self.lower_bone.toString()