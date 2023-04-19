#!/usr/bin/env python3

class SurroundingOpenSpaces:
    def __init__(self, ip_filename, op_filename):
        self.ip_filename = ip_filename
        self.op_filename = op_filename

    def get_honeycombs(self):
        honeycombs = []
        with open(self.ip_filename) as f:
            honeycomb = []
            for line in f:
                if line.strip() == "":
                    honeycombs.append(honeycomb)
                    honeycomb = []
                else:
                    honeycomb.append(line.strip())
            honeycombs.append(honeycomb)
        return honeycombs
        
    @staticmethod
    def count_neighbor_Os(honeycomb):
        rows = len(honeycomb)
        cols = len(honeycomb[0])
        count = 0
        neighbor_O_locations = []
        
        for i in range(rows):
            for j in range(cols):
                if honeycomb[i][j] == "W":

                    for di, dj in [(1,-1),(1,1),(-1,-1),(-1,1),(0,-2),(0,2)]:
                        ni, nj = i+di, j+dj

                        if 0 <= ni < rows and 0 <= nj < cols and honeycomb[ni][nj] == "O":
                            neighbor_O_locations.append((ni, nj))
                            count += 1
        return count, neighbor_O_locations
    
    @staticmethod
    def get_W_location_in_honey_comb(honey_comb):
        W_location = ""
        for i in range(len(honey_comb)):
            for j in range(len(honey_comb[i])):
                if honey_comb[i][j] == "W":
                    W_location = (i, j)
        return W_location
    
    @staticmethod
    def get_direction_lines(honeycomb):
        direction_lines = []
        east_line, west_line, north_east, south_east, north_west, south_west = [], [], [], [], [], []
        zero_count = SurroundingOpenSpaces.count_neighbor_Os(honeycomb)[0]
        if zero_count == 0: return "TRAPPED"
        else:
            zero_locations = SurroundingOpenSpaces.count_neighbor_Os(honeycomb)[1]
            w_location = SurroundingOpenSpaces.get_W_location_in_honey_comb(honeycomb)
            for zero_location in zero_locations:
                i, j = zero_location

                while (0 <= j < len(honeycomb[0])) and (0 <= i < len(honeycomb)):
                    if i == w_location[0] and j > w_location[1]:
                        east_line.append(honeycomb[i][j])
                        j += 2
                    elif i == w_location[0] and j < w_location[1]:
                        west_line.append(honeycomb[i][j])
                        j -= 2
                    elif i > w_location[0] and j > w_location[1]:
                        north_east.append(honeycomb[i][j])
                        i += 1
                        j += 1
                    elif i > w_location[0] and j < w_location[1]:
                        north_west.append(honeycomb[i][j])
                        i += 1
                        j -= 1
                    elif i < w_location[0] and j > w_location[1]:
                        south_east.append(honeycomb[i][j])
                        i -= 1
                        j += 1
                    elif i < w_location[0] and j < w_location[1]:
                        south_west.append(honeycomb[i][j])
                        i -= 1
                        j -= 1
                    else:
                        break

        direction_lines.append(east_line)
        direction_lines.append(west_line)
        direction_lines.append(north_east)
        direction_lines.append(south_east)
        direction_lines.append(north_west)
        direction_lines.append(south_west)
        return direction_lines
    
    @staticmethod
    def get_honeycombs_0_counts(honeycombs):
        counts_list = []
        coords_list = []
        for honeycomb in honeycombs:
            count, coords = SurroundingOpenSpaces.count_neighbor_Os(honeycomb)
            counts_list.append(count)
            coords_list.append(coords)
        
        return counts_list
    
    def write_counts(self):
        honeycombs = self.get_honeycombs()
        counts_list = SurroundingOpenSpaces.get_honeycombs_0_counts(honeycombs)
        counts_list = counts_list[1:]
        with open(self.op_filename, "w") as f:
            for i in counts_list:
                f.write(str(i) + "\n")

if __name__ == "__main__":
    ip_file_name = "lvl2/level2_5.in"
    op_file_name = "lvl2/testing.out"
    SurroundingOpenSpaces(ip_file_name, op_file_name).write_counts()
