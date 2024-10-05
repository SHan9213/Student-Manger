class Student:
    def __init__(self, name, physics, chemistry, maths, computer_science):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths
        self.computer_science = computer_science

    def get_marks(self):
        return {
            'Physics': self.physics,
            'Chemistry': self.chemistry,
            'Maths': self.maths,
            'Computer Science': self.computer_science
        }
