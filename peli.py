# from typing import List

# def func(): # -> List(str):
#     lst = List[str]

#     lst.append("a")

#     # for i in range(5):
#     #     lst.append(str(i))
#     return lst

# aa = func()
# print(aa)

from typing import List

Vector = List[float]

def func(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.
new_vector = func(2.0, [1.0, -4.2, 5.4])

print(new_vector)


