class Board:
    def __init__(self):
        self.plot = [["Empty" for y in range(6)] for x in range(7)] 
        self.won = False
    

    def set_plot(self, location, color):

        self.plot[location[0]][location[1]] = color

        self.won = self.horizontal_check(location, color)


    def available_plot(self, location):
        if -1 < location < 7:
            for i in range(6):
                if self.plot[location][i] == "Empty": 
                    return True    
        return False
    

    def get_available_plot(self, x):
        for i, plo in enumerate(self.plot[x]):
            if self.plot[x][i] == "Empty":
                return i
    

    def draw(self):
        for i in range(7):
            for j in range(6):
                if self.plot[i][j] == "Empty":
                    return False
        return True


    def horizontal_check(self, location, color):
        empty = [False, False]
        consecutive = 1
        for i in range(3):
            if -1 < location[0] + 1 + i < 7 and not empty[0]:
                if self.plot[location[0] + 1 + i][location[1]] == color:
                    consecutive += 1
                else:
                    empty[0] = True
            if -1 < location[0] - 1 - i < 7 and not empty[1]:
                if self.plot[location[0] - 1 - i][location[1]] == color:
                    consecutive += 1
                else:
                    empty[1] = True
        if consecutive >= 4:
            return True
        else:
            return self.vertical_check(location, color)


    def vertical_check(self, location, color):    
        empty = [False, False]
        consecutive = 1
        for i in range(3):
            if -1 < location[1] + 1 + i < 6 and not empty[0]:
                if self.plot[location[0]][location[1] + 1 + i] == color:
                    consecutive += 1
                else:
                    empty[0] = True
            if -1 < location[1] - 1 - i < 6 and not empty[1]:
                if self.plot[location[0]][location[1] - 1 - i] == color:
                    consecutive += 1
                else:
                    empty[1] = True                
        if consecutive >= 4:
            return True
        else:
            return self.forward_diagonal_check(location, color)
    

    def forward_diagonal_check(self, location, color):
        empty = [False, False]
        consecutive = 1
        for i in range(3):
            if -1 < location[0] + 1 + i < 7 and -1 < location[1] + 1 + i < 6 and not empty[0]:
                if self.plot[location[0]+ 1 + i][location[1] + 1 + i] == color:
                    consecutive += 1
                else:
                    empty[0] = True
            if -1 < location[0] - 1 - i < 7 and -1 < location[1] - 1 - i < 6 and not empty[1]:
                if self.plot[location[0] - 1 - i][location[1] - 1 - i] == color:
                    consecutive += 1
                else:
                    empty[1] = True                
        if consecutive >= 4:
            return True
        else:
            return self.backward_diagonal_check(location, color)
    

    def backward_diagonal_check(self, location, color):
        empty = [False, False]
        consecutive = 1
        for i in range(3):
            if -1 < location[0] - 1 - i < 7 and -1 < location[1] + 1 + i < 6 and not empty[0]:
                if self.plot[location[0] - 1 - i][location[1] + 1 + i] == color:
                    consecutive += 1
                else:
                    empty[0] = True
            if -1 < location[0] + 1 + i < 7 and -1 < location[1] - 1 - i < 6 and not empty[1]:
                if self.plot[location[0] + 1 + i][location[1] - 1 - i] == color:
                    consecutive += 1
                else:
                    empty[1] = True                    
        if consecutive >= 4:
            return True
        else:
            return False