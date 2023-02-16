import numpy as np

class Levenstein:
    def __init__(self) -> None:
        pass
    
    def construct_matrix(self):
        len1 = len(self.a)
        len2 = len(self.b)
        self.matrix = np.zeros((len1+1, len2+1))

    def display_matrix(self):
        print(self.matrix)
    
    def initalize_matrix(self):
        self.shape = self.matrix.shape
        max_ = max(list(self.shape))
        for i in range(max_):
            if i < self.shape[0]:
                self.matrix[i][0] = i 
            if i < self.shape[1]:
                self.matrix[0][i] = i 

    def matrix_filling(self):
        for j in range(1,self.shape[1]):   # first accross the row
            for i in range(1, self.shape[0]):  # then across the column
                add = 0
                if self.b[j-1] != self.a[i-1]:
                    add = 1
                min_val = min(self.matrix[i-1][j], self.matrix[i-1][j-1], self.matrix[i][j-1])
                self.matrix[i][j] = min_val + add

    def get_levenshtein_distance(self):
        return self.matrix[-1][-1]

    def evaluate(self, str1, str2):
        self.a = str1
        self.b = str2 
        self.construct_matrix()
        self.initalize_matrix()
        self.matrix_filling()
        print(f'The Levenstein distance between {self.a} and {self.b} is {int(self.get_levenshtein_distance())}.')
        return self.get_levenshtein_distance()


if __name__ == "__main__":
    lev = Levenstein()
    lev.evaluate('sitting', 'mitting')
