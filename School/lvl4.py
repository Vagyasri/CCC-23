#!/usr/bin/env python3
from lvl2 import SurroundingOpenSpaces
from lvl3 import FreeTrapped
import filecmp

class FreePosibility:
    def __init__(self, ip_filename, op_filename):
        self.ip_filename = ip_filename
        self.op_filename = op_filename
        free_trapped = FreeTrapped(ip_filename, op_filename)
        self.honeycombs = free_trapped.honeycombs
        self.free_trapped = free_trapped.get_free_trapped()

    def get_neighbor_Os_of_0(self,zero_location):
        neighbor_Os = []
        for honeycomb in self.honeycombs:
            for di, dj in [(1,-1),(1,1),(-1,-1),(-1,1),(0,-2),(0,2)]:
                ni, nj = zero_location[0]+di, zero_location[1]+dj
                if 0 <= ni < len(honeycomb) and 0 <= nj < len(honeycomb[0]) and honeycomb[ni][nj] == "O":
                    neighbor_Os.append((ni,nj))
        return neighbor_Os
    
    def get_free_posibility(self):
        free_possibility = []
        for honeycomb in self.honeycombs:
            free = []
            length = len(honeycomb)
            breadth = len(honeycomb[0])
            neighbor_Os = SurroundingOpenSpaces.count_neighbor_Os(honeycomb)[1]
            count = 0
            for neighbor_O in neighbor_Os:
                while 0 <= neighbor_O[0] < length and 0 <= neighbor_O[1] < breadth:
                    neighbor = self.get_neighbor_Os_of_0(neighbor_O)[0]
                    neighbor_Os = []
                    neighbor_Os.append(neighbor)
                    
                    if honeycomb[neighbor[0]][neighbor[1]] == "O":
                        free.append("FREE")
                        break
                    else:
                        neighbor_O = neighbor
                        count += 1
                        if count == 1000:
                            break
            if "FREE" in free:
                free_possibility.append("FREE")
            else:
                free_possibility.append("TRAPPED")
        return free_possibility




            
    # def get_free_posibility(self):
    #     free_possibility = []
    #     for honeycomb in self.honeycombs:
    #         free = []
    #         neighbor_Os = SurroundingOpenSpaces.count_neighbor_Os(honeycomb)[1]
    #         for neighbor_O in neighbor_Os:
    #             i, j = neighbor_O
    #             for di, dj in [(1,-1),(1,1),(-1,-1),(-1,1),(0,-2),(0,2)]:
    #                 ni, nj = i+di, j+dj
    #                 if 0 <= ni < len(honeycomb) and 0 <= nj < len(honeycomb[0]) and honeycomb[ni][nj] == "O":
    #                     free.append("FREE")
    #                     break
    #         if "FREE" in free:
    #             free_possibility.append("FREE")
    #         else:
    #             free_possibility.append("TRAPPED")
    #     return free_possibility
        
    def write_free_posibility(self):
        free_posibility = self.get_free_posibility()
        with open(self.op_filename, "w") as f:
            for i in free_posibility:
                f.write(str(i) + "\n")

if __name__ == "__main__":
    # ip_file_name1 = "lvl4/level4_2.in"
    ip_file_name2 = "lvl4/level4_example.in"

    # op_file_name1 = "lvl4/test2.out"
    op_file_name2 = "lvl4/test.out"
    # FreePosibility(ip_file_name1, op_file_name1).write_free_posibility()
    FreePosibility(ip_file_name2, op_file_name2).write_free_posibility()

    # if filecmp.cmp(op_file_name1, "lvl4/level4_2.out") == False: print("Test 1 failed")
