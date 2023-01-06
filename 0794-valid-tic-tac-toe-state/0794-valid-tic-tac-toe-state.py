class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        #counting the occurrence of both 'X' and 'O'
        #check vertically,horizontally and diagonally compare with the winning conditions
        #Time complexity O(1) since it is  O(9)
        #Space complexity O(1)
        num_x = 0
        num_o = 0
        x_wins = False
        o_wins = False
        
        for i in range(3):
            for j in range(3):
                num_x += (board[i][j] =='X')
                num_o += (board[i][j] =='O')
            #horizontal rows
            horizontal = board[i]
            if horizontal == 'XXX':
                x_wins = True
            elif horizontal == 'OOO':
                o_wins = True
            #vertical columns
            vertical = board[0][i] + board[1][i] + board[2][i]
            if vertical == 'XXX':
                x_wins = True
            elif vertical == 'OOO':
                o_wins = True
        #left diagonal
        left_diagonal = board[0][0] + board[1][1] + board[2][2]
        if left_diagonal == 'XXX':
            x_wins = True
        elif left_diagonal == 'OOO':
            o_wins = True
        #right diagonal 
        right_diagonal = board[0][2] + board[1][1] + board[2][0]
        if right_diagonal == 'XXX':
            x_wins = True
        elif right_diagonal == 'OOO':
            o_wins = True
        if x_wins:
            return not o_wins and num_x - num_o == 1
        elif o_wins:
            return num_x == num_o
        return num_x >= num_o and num_x-num_o <= 1
        