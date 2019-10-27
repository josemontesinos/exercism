class School(object):

    school_roster = None

    def __init__(self):
        self.school_roster = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }

    def add_student(self, name, grade):
        self.school_roster[grade].append(name)
        self.school_roster[grade] = sorted(self.school_roster[grade])

    def roster(self):
        roster = []
        for grade in sorted(self.school_roster.keys()):
            roster += self.school_roster[grade]
        return roster

    def grade(self, grade_number):
        return self.school_roster[grade_number]
