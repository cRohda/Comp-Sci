class Student:
    def __init__(self, fname, id_num):
        self.fn = fname
        self.id = id_num


s1 = Student('John', 111)
s2 = Student('Emmanuel', 112)
s3 = Student('Luke', 113)

print(s1)
print(s2.fn)
print(s3.id)
