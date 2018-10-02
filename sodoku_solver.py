def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    new_puzzle = Puzzle(puzzle)
    i = 0
    while(new_puzzle.zero_count>0):
        new_puzzle.check_poss()
        #print([x.posses for x in [y for y in new_puzzle.rows]])
        i += 1
        if i > 10:
            print('failed')
            return new_puzzle.rows
    return new_puzzle.rows
    
class Puzzle:
    def __init__(self, rows):
        self.temp_col_vals = [[rows[i][r] for i in range(len(rows))] for r in range(len(rows))]
        self.temp_row_vals = rows
        self.temp_block_vals = make_blocks(rows)
        self.ind_list = []
        i = 0
        for item in self.temp_row_vals:
            for num in item:
                self.ind_list.append(Index(self.temp_col_vals, self.temp_row_vals, self.temp_block_vals, i, num))
                i += 1
        self.check_poss()
        
    @property
    def rows(self):
        return [Row(self.ind_list, r) for r in range(9)]
        
    @property
    def cols(self):
        return [Col(self.ind_list, c) for c in range(9)]
        
    @property
    def blocks(self):
        return [Block(self.ind_list, b) for b in range(9)]
        
    @property
    def row_vals(self):
        return [self.rows[r] for r in range(9)]
        
    @property
    def col_vals(self):
        return [self.cols[c] for c in range(9)]
        
    @property
    def block_vals(self):
        return [self.blocks[b] for b in range(9)]
        
    @property
    def zero_count(self):
        return len([x.val for x in self.ind_list if x.val==0])
        
    def check_poss(self):
        for i, index in enumerate(self.ind_list):
            pos = [1,2,3,4,5,6,7,8,9]
            if index.val==0:
                for n in self.row_vals[index.row]:
                    if n in pos:
                        pos.remove(n)
                for n in self.col_vals[index.col]:
                    if n in pos:
                        pos.remove(n)
                for n in self.block_vals[index.block]:
                    if n in pos:
                        pos.remove(n)
                self.ind_list[i].pos = pos
                if len(pos)==1:
                    self.ind_list[i].val = pos[0]
            else:
                self.ind_list[i].pos = [index.val]
    
    def __repr__(self):
        return str(self.row_vals)
        
class Row:
    def __init__(self, ind_list, row):
        self.indexes = []
        self.values = []
        self.posses = []
        for i in ind_list:
            if i.row==row:
                self.indexes.append(i)
                self.values.append(i.val)
                self.posses.append(i.pos)
        
    def __getitem__(self, key):
        return self.values[key]
        
    def __setitem__(self, key, value):
        self[key] = value
            
    def __repr__(self):
        return str(self.values)
            
class Col(Row):
    def __init__(self, ind_list, col):
        self.indexes = []
        self.values = []
        self.posses = []
        for i in ind_list:
            if i.col==col:
                self.indexes.append(i)
                self.values.append(i.val)
                self.posses.append(i.pos)

class Block(Row):
    def __init__(self, ind_list, block):
        self.indexes = []
        self.values = []
        self.posses = []
        for i in ind_list:
            if i.block==block:
                self.indexes.append(i)
                self.values.append(i.val)
                self.posses.append(i.pos)
                
                
def make_blocks(rows):
    return make_three_blocks(rows, 0) + make_three_blocks(rows, 3) + make_three_blocks(rows, 6)
    
def make_three_blocks(rows, row_start):
    blocks = [[],[],[]]
    for row in range(row_start,row_start+3):
        for col in range(0,3):
            blocks[0].append(rows[row][col])
        for col in range(3,6):
            blocks[1].append(rows[row][col])
        for col in range(6,9):
            blocks[2].append(rows[row][col])
    return blocks
    
class Index():
    def __init__(self, cols, rows, blocks, i, val):
        self.val = val
        if val!=0:
            self.pos = [val]
        else:
            self.pos = [1,2,3,4,5,6,7,8,9]
        self.i = i
        self.col = i%9
        self.row = int(i/9)
        if self.row in range(0,3) and self.col in range(0,3):
            self.block = 0
        if self.row in range(0,3) and self.col in range(3,6):
            self.block = 1
        if self.row in range(0,3) and self.col in range(6,9):
            self.block = 2
        if self.row in range(3,6) and self.col in range(0,3):
            self.block = 3
        if self.row in range(3,6) and self.col in range(3,6):
            self.block = 4
        if self.row in range(3,6) and self.col in range(6,9):
            self.block = 5
        if self.row in range(6,9) and self.col in range(0,3):
            self.block = 6
        if self.row in range(6,9) and self.col in range(3,6):
            self.block = 7
        if self.row in range(6,9) and self.col in range(6,9):
            self.block = 8
            
    def __repr__(self):
        return str(self.i)

def main():
    puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

    new_puzzle = sudoku(puzzle)  
    print(new_puzzle)

if __name__=='__main__':
    main()
