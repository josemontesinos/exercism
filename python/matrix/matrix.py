class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def get_rows(self):
        rows_as_chars = [row.split() for row in self.matrix_string.split('\n')]
        rows_as_int = list(map(lambda row: list(map(lambda item: int(item), row)), rows_as_chars))
        return rows_as_int

    def row(self, index):
        return self.get_rows()[index - 1]

    def column(self, index):
        rows = self.get_rows()
        return [row[index - 1] for row in rows]

