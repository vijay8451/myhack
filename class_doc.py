class stud:
    '''This is test doc'''
    def __init__(self, roll_no, grade):
        self.roll_no = roll_no
        self.grade = grade

    def display(self):
        print("Roll no : ", self.roll_no, ", Grade: ", self.grade)

if __name__ == '__main__':
    stud1 = stud(34, 'S')
    stud1.age = 7
    print(hasattr(stud1, 'age'))
    print(stud.__doc__)


