class NQueens:
    def __init__(self,n):
        self.n=n
        self.board=[[0] *n for _ in range (n)]
        self.solutions=[]


    def is_safe(self,col,row):
        for i in range(row):
            if self.board[i][col]==1:
                return False
            if 0<=col-row+i <self.n and self.board[i][col-row+i]==1:
                return False
            if 0<=col+row-i<self.n and self.board[i][col+row-i]==1:
                return False
        return True

    def solve_backtracking(self,row=0):
        if row==self.n:
            self.solutions.append([row[:]for row in self.board])
            return True


        for col in range(self.n):
            if self.is_safe(col,row):
                self.board[row][col]=1
                self.solve_backtracking(row+1)
                self.board[row][col]=0
                
       

    def solve_branch_and_bound(self,row=0):
        if row==self.n:
            
            self.solutions.append([row[:] for row in self.board])
            return True


        for col in range(self.n):
            if self.is_safe(col,row):
                self.board[row][col]=1
                self.solve_branch_and_bound(row+1)
                self.board[row][col]=0
                
       

    def print_solution(self):
        for i,solution in enumerate(self.solutions):
            print(f"solution for {i+1}")
            for row in solution:
                print("".join("Q" if cell ==1 else "-"for cell in row))
            print()

n_queen = NQueens(4)
n_queen.solve_backtracking()
print("using backtracking")
n_queen.print_solution()

n_queen=NQueens(4)
n_queen.solve_branch_and_bound()
print("solution")
n_queen.print_solution()
