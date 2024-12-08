import numpy as np

class MapGame:
    def __init__(self, filepath):
        self.original_map = self.loadmap(filepath)  # load the original map
        self.map = self.original_map.copy()  # working copy
        self.num_row, self.num_col = self.map.shape
        self.guard_position = None
        self.original_guard_position = None
        self.perspective = 0
        self.direction = {
            0: (-1, 0),
            90: (0, 1),
            180: (1, 0),
            270: (0, -1)
        }
    
    def loadmap(self, filepath):
        map_array = []
        with open(filepath, 'r') as reader:
            lines = reader.readlines()

        for line in lines:
            row = (list(line.strip()))
            map_array.append(row)
        
        map_array = np.array(map_array) 

        return map_array
    
    def initliase_guard_position(self):
        self.perspective = 0
        position = np.where(self.map == "^")
        if position[0].size > 0:
            self.guard_position = (position[0][0], position[1][0])
            self.original_guard_position = self.guard_position
            # print("set position of guard '^': ", self.guard_position)    

    def get_guard_position(self):
        return self.guard_position

    def set_guard_position(self, new_row, new_col):
        self.map[new_row][new_col] = "^"
        self.guard_position = new_row, new_col

    def get_object(self, row, col):
        object = self.map[row][col]
        return object

    def is_blocked(self):
        cur_row, cur_col = self.get_guard_position()
        movement_row, movement_col = self.direction[self.perspective]
        object = self.get_object(cur_row + movement_row, cur_col + movement_col)
        if object == "#" or object == "O":
            return True
        else:
            return False
    
    """
    1. need to make guard move
    2. need to leave trace on map
    """
    def move_forward(self):
        cur_row, cur_col = self.get_guard_position()
        # self.map[cur_row][cur_col] = "X" # leave X trace on map
        movement_row, movement_col = self.direction[self.perspective]
        self.set_guard_position(cur_row + movement_row, cur_col + movement_col)

    def turn_right(self):
        self.perspective = (self.perspective + 90) % 360 # set back to 0 when it exceeds 360. Values under 360 will just remain the same

    def is_leaving(self):
        cur_row, cur_col = self.get_guard_position()
        # print("is leaving checking cur row and col:", cur_row, cur_col)
        # or cur_row == self.num_row - 1 or cur_col == 0 or cur_col == self.num_col - 1:
        if cur_row == 0 and self.perspective == 0:
            print("leaving!")
            return True
        elif cur_col == (self.num_col - 1) and self.perspective == 90:
            print("leaving!")
            return True
        elif cur_row == (self.num_row - 1) and self.perspective == 180:
            print("leaving!")
            return True
        elif cur_col == 0 and self.perspective == 270:
            print("leaving!")
            return True
        else:
            return False
        
    def count_trace(self):
        count = 0
        num_row, num_col = self.map.shape
        for row in range(num_row):
            for col in range(num_col):
                if self.map[row][col] == "X":
                    count += 1
        return count      

    def reset_map(self):
        self.map = self.original_map.copy()  # reset to the original map  

    def reset_guard_position(self):
        self.guard_position = self.original_guard_position

    def set_wall(self, row, col):
        self.map[row][col] = "O"

    def undo_set_wall(self, row, col):
        self.map[row][col] = "."


if __name__ == "__main__":
    map_game = MapGame("input-dec6-sample.txt")
    # print(map_game.map)
    map_game.initliase_guard_position()
    # part 1 solved
    # while (not map_game.is_leaving()):
    #     if (map_game.is_blocked()):
    #         map_game.turn_right()
    #     map_game.move_forward()
    # print(map_game.count_trace()+1)

    

    
    # print(visited_states)

    # part 2
        # get where we can put extra wall
    empty_slots = []
    for row in range(map_game.num_row):
        for col in range(map_game.num_col):
            if map_game.map[row][col] == ".":
                empty_slots.append((row, col))

    unsolvable_count = 0

    for slot in empty_slots:
        empty_row, empty_col = slot
        map_game.undo_set_wall(empty_row, empty_col)
        map_game.reset_map()
        map_game.initliase_guard_position()
        map_game.set_wall(empty_row, empty_col)
        print("set a wall at ", empty_row, empty_col)
        visited_states = set() # store the guards previous traversed states
        while (not map_game.is_leaving()):
            row, col = map_game.get_guard_position()
            current_state = (row, col, map_game.perspective)
            if current_state not in visited_states:
                visited_states.add(current_state)
            else:
                print("looping at ", current_state)
                unsolvable_count += 1
                print("went into loop")
                break
            if (map_game.is_blocked()):
                map_game.turn_right()
            map_game.move_forward()
    print(unsolvable_count)

