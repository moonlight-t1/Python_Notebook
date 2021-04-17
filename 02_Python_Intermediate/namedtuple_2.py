from collections import namedtuple

Point1 = namedtuple("Point", ["x", "y"])
Point2 = namedtuple("Point", "x, y")
Point3 = namedtuple("Point", "x y")
Point4 = namedtuple("Point", "x y z class", rename=True)  # Default=False

# Dict to Unpacking
temp_dict = {"x": 75, "y": 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

print(p1[0] + p2[1])
print(p1.x + p2.y)

# unpacking
x, y = p3
print(x + y)

temp = [52, 38]

# _make() : convert List into Nametuple
p4 = Point1._make(temp)
print(p4)

# _field() : check field name
print(p1._fields, p2._fields, p3._fields)

# _asdict() : Ordered Dict
print(p1._asdict(), p4._asdict())