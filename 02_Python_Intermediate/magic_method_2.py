# Vector Class
class Vector(object):
    """
    Vector Calculate Class
    """

    def __init__(self, *args):
        """
        Create a vector
        example : v = Vector(5, 10)
        """
        if len(args) == 0:  # if args is empty, initialize (0, 0)
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args  # unpacking

    def __repr__(self):
        """
        Returns the vector informations
        """
        return f"Vector({self._x}, {self._y})"

    def __add__(self, other):
        """
        Returns the vector addition of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        """
        if point is (0, 0) or not
        """
        return bool(max(self._x, self._y))


if __name__ == "__main__":
    # create Vector Instances
    v1 = Vector(5, 7)
    v2 = Vector(23, 35)
    v3 = Vector()

    # print magic mehod docs
    print(Vector.__init__.__doc__)
    print(Vector.__repr__.__doc__)
    print(Vector.__add__.__doc__)

    print(v1, v2, v3)
    print(v1 + v2)
    print(v1 * 3)
    print(v2 * 10)
    print(bool(v1), bool(v2))
    print(bool(v3))

    print()
    print()