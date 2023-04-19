#!/usr/bin/env python3
from lvl2 import SurroundingOpenSpaces

class FreeTrapped:
    def __init__(self, ip_filename, op_filename):
        self.ip_filename = ip_filename
        self.op_filename = op_filename
        open_spaces = SurroundingOpenSpaces(ip_filename, op_filename)
        honeycombs = open_spaces.get_honeycombs()
        self.honeycombs = honeycombs[1:]
    
    def get_free_trapped(self):
        free_trapped = []
        for honeycomb in self.honeycombs:
            free = []
            direction_lines = SurroundingOpenSpaces.get_direction_lines(honeycomb)
            for direction_line in direction_lines:
                if direction_line and all([i == "O" for i in direction_line]):
                    free.append("FREE")
                else:
                    free.append("TRAPPED")
            if "FREE" in free:
                free_trapped.append("FREE")
            else:
                free_trapped.append("TRAPPED")
        return free_trapped        
        
    def write_free_trapped(self):
        free_trapped = self.get_free_trapped()
        with open(self.op_filename, "w") as f:
            for i in free_trapped:
                f.write(str(i) + "\n")

if __name__ == "__main__":
    ip_file_name = "lvl3/level3_5.in"
    op_file_name = "lvl3/level3_5.out"
    FreeTrapped(ip_file_name, op_file_name).write_free_trapped()
