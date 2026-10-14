class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == "." :
                    continue
                
                if (board[r][c] in rows[r]
                 or board[r][c] in cols[c]
                 or board[r][c] in sqrs[(r//3,c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqrs[(r//3 ,c//3)].add(board[r][c])

        return True 

# Imagine you are a Chief Auditor inspecting a mega-apartment complex called Sudoku Towers.
# The complex has 9 floors (rows r) and 9 vertical wings (columns c). It is also divided into 9 massive family blocks (the 3x3 squares).
# Your job is to walk through every room one by one. If you catch the same person trying to rent two different rooms in the same floor, the same wing, or the same family block, you immediately sound the alarm (return False). If you inspect every single room and find no illegal double-renters, you sign off on the building (return True).
# To keep track of everyone, you carry a clipboard with three distinct binders: rows, cols, and squares. Each binder uses defaultdict(set), which means every floor, wing, and block automatically gets its own secure, empty guest list (set) that won't allow duplicate names.


# 1• The Analogy: You systematically walk the building. You start on Floor 0, checking rooms from Wing 0 to Wing 8. Then you move up to Floor 1, and so on.

# 2• The Analogy: You open a door and find an empty room ("."). There is no tenant to inspect, so you just skip it and move to the next door.


# 3. Calculating the Family Block Address: (r // 3, c // 3)

# • The Analogy: This is the most clever part of the code. The building has 9 family blocks. To know which block a room belongs to, you divide the floor number and wing number by 3 and drop the remainder (//).
# 	• If you are in Room r=0, c=2 (Floor 0, Wing 2) → 0//3 = 0 and 2//3 = 0. You are in Family Block (0, 0).
# 	• If you move to Room r=2, c=2 (Floor 2, Wing 2) → 2//3 = 0 and 2//3 = 0. You are still inside Family Block (0, 0)!
# 	• This grouping perfectly locks every room into its correct 3x3 mini-box identifier.

# 4• The Analogy: You find a tenant—let's say the number "5"—living in Room r=0, c=2. Before doing anything else, you flip open your three binders and check your logs:
# 	• "Is '5' already logged on Floor 0?" (rows[r])
# 	• "Is '5' already logged in Wing 2?" (cols[c])
# 	• "Is '5' already logged inside Family Block (0,0)?" (squares[...])
# • If the answer to any of these questions is Yes, you caught a rule-breaker! You halt the entire audit right then and there and shout False.

# 5• The Analogy: If the tenant "5" passes the check (they haven't been seen anywhere else in those zones yet), you write their name down. You add "5" to the guest list for Floor 0, the guest list for Wing 2, and the guest list for Family Block (0,0).
# Now, if you encounter another "5" later on in any of those three zones, the trap will instantly snap shut!
