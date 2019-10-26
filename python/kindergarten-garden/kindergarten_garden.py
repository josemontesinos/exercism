DEFAULT_STUDENTS = (
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'
)
PLANTS = {'V': 'Violets', 'G': 'Grass', 'C': 'Clover', 'R': 'Radishes'}


class Garden(object):

    students = None
    diagram = None

    def __init__(self, diagram, students=None):
        self.students = tuple(enumerate(sorted(students or DEFAULT_STUDENTS)))
        self.diagram = diagram.split('\n')

    def plants(self, student):
        index = next(std for std in self.students if std[1] == student)[0]
        letters = self.diagram[0][index*2:index*2+2] + self.diagram[1][index*2:index*2+2]
        return [PLANTS[letter] for letter in letters]
