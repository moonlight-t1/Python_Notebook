from abc import *  # Abstract Base Class


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def studet(self):
        print("Study")

    def go_to_school(self):
        print("go to school")

