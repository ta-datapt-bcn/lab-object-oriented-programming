def rowcolumn(mat):
    # This function takes a list of lists and returns the size of the rows and the columns 
    # Input: list of lists
    # Output: Tuple of rows and columns
    #
    # Sample input: [[1,2,3],[4,5,6]]
    # Sample Output: (2, 3)
    
    # Your code here:
    rows = len(mat)
    columns = len(mat[0])

    print((rows, columns))  


class Matrix2D():
    # First, we will write the __init__ function. 
    # In this function, we will initialize rows and the columns using the matrix that we have passed to the class.
    
    def __init__(self, mat):
        # Assign mat to self.mat
        # Assign rows and cols to self.rows and self.cols
        # To find the rows and the cols, use the rowcolumn function and pass self.mat to the function.
        # Since the rowcolumn function is now a member of the class, make sure to refer to the function as self.rowcolumn
        
        # Your code here:
        self.mat = mat
        rows = rowcolumn(mat)[0]
        cols = rowcolumn(mat)[1]
        self.rows = rows
        self.cols = cols
    
    # Insert the twodim function here.
    # The only change you need to make is that now we are passing self and mat to the function (make sure self is first).
    
    # Your code here:
    def twodim(self, mat):
        if not isinstance(mat, list):
            return False
        for sublist in mat:
            if not isinstance(sublist, list):
                return False
            for i in sublist:
                if isinstance(i, list):
                    return False
        return True  
    
    # Insert the rowcolumn function here.
    # The changes you need to make: 
    # 1. The function now takes self and mat as arguments (make sure to pass self first).
    # 2. Any reference to twodim will be changed to self.twodim since this function is a member of the class and takes self 
    
    # Your code here:
    def rowcolumn(self, mat):
        rows = len(self.mat)
        columns = len(self.mat[0])

        print((rows, columns))
    
    # Insert the compare function here
    # Add self as the first argument passed to the function
    
    # Your code here:
    def compare(self, matrix):
        if (len(self.mat) == len(matrix.mat)) and (len(self.mat[0]) == len(matrix.mat[0])):
            return True
        else:
            return False

    # Insert the addition function here
    # This function now takes self and matrix (another matrix of the Matrix2D class)
    # Change the compare function to self.compare 
    # Change any reference to mat1 and mat2 to self.mat and matrix.mat respectively
    # Return your result as a Matrix2D(result). This will ensure that we return a new matrix and not a list of lists.
    
    # Your code here:
    def addition(self, matrix):
        list_1 = []
        for a in range(len(self.mat)):
            list_2 = []
            for b in range(len(self.mat[0])):
                list_2.append(self.mat[a][b] + matrix.mat[a][b])
            list_1.append(list_2)
        return list_1


Matrix2D([[1,2,3],[4,5,6]]).addition(Matrix2D([[7,8,9],[10,11,12]])).mat