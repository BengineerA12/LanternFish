from datetime import datetime
import sys
import copy

class Fish:
    def __init__(self, age = 8):
        self.age = int(age)

    def next(self):
        if self.age == 0:
            self.age = 6
            return True
        else:
            self.age += -1
            return False

    def __str__(self):
        return str(self.age)
    def __repr__(self):
        return str(self.age)


class Simulator:
    def __init__(self, fishes):
        self.fishes = fishes
        self.days_elapsed = 0

    def next(self):
        new_fish = 0
        for f in self.fishes:
            if f.next():
                new_fish +=1

        for i in range(new_fish):
            self.fishes.append(Fish())

        self.days_elapsed += 1
        #print(f"Days {self.days_elapsed}")
    def get_int_fishes(self):
        int_fishes = []
        for fish in self.fishes:
            int_fishes.append(fish.age)
        return int_fishes

#build simulation blocks
block_resolutions = [1,5,10,50,100]
blocks = {}
start_positions = range(9)
for position in start_positions:
    print(f"Building SimBlock for Position: {position}")
    blocks[position] = {}
    sim = Simulator([Fish(position)])
    days_processed = 0
    while days_processed <= 100:
        sim.next()
        days_processed += 1
        if sim.days_elapsed in block_resolutions:
            blocks[position][sim.days_elapsed] = sim.get_int_fishes()
            #blocks[position][sim.days_elapsed] = copy.deepcopy(sim.fishes)

print(blocks[0][1])
print(blocks[0][5])
print(blocks[0][10])
print(blocks[1][10])

#setup starting conditions
#fish_string = "3,4,3,1,2"
fish_string = "3,3,5,1,1,3,4,2,3,4,3,1,1,3,3,1,5,4,4,1,4,1,1,1,3,3,2,3,3,4,2,5,1,4,1,2,2,4,2,5,1,2,2,1,1,1,1,4,5,4,3,1,4,4,4,5,1,1,4,3,4,2,1,1,1,1,5,2,1,4,2,4,2,5,5,5,3,3,5,4,5,1,1,5,5,5,2,1,3,1,1,2,2,2,2,1,1,2,1,5,1,2,1,2,5,5,2,1,1,4,2,1,4,2,1,1,1,4,2,5,1,5,1,1,3,1,4,3,1,3,2,1,3,1,4,1,2,1,5,1,2,1,4,4,1,3,1,1,1,1,1,5,2,1,5,5,5,3,3,1,2,4,3,2,2,2,2,2,4,3,4,4,4,1,2,2,3,1,1,4,1,1,1,2,1,4,2,1,2,1,1,2,1,5,1,1,3,1,4,3,2,1,1,1,5,4,1,2,5,2,2,1,1,1,1,2,3,3,2,5,1,2,1,2,3,4,3,2,1,1,2,4,3,3,1,1,2,5,1,3,3,4,2,3,1,2,1,4,3,2,2,1,1,2,1,4,2,4,1,4,1,4,4,1,4,4,5,4,1,1,1,3,1,1,1,4,3,5,1,1,1,3,4,1,1,4,3,1,4,1,1,5,1,2,2,5,5,2,1,5"
fish_arr = fish_string.split(",")
reduced_fish = {}
for i in fish_arr:
    if i in reduced_fish:
        reduced_fish[i] += 1
    else: 
        reduced_fish[i] = 1
print(reduced_fish)

#simulate full expansion - construct w blocks to 156 and then count exentions to 256
sub_totals = {}
for key in reduced_fish:
    print(f"working on key {key}")
    days_1 = blocks[int(key)][1]
    days_101 = []
    for fish in days_1:
        days_101 += blocks[fish][100]
    days_151 = []
    for fish in days_101:
        days_151 += blocks[fish][50]
    days_156 = []
    for int_fish in days_151:
        days_156 += blocks[int_fish][5]

    print(f"doing subcount")
    extension_to_256 = 0
    for fish in days_156:
        extension_to_256 += len(blocks[fish][100])
    sub_totals[key] = extension_to_256 * reduced_fish[key]

print(sub_totals)

total = 0
for item in sub_totals:
    total += sub_totals[item]

print(total)

sys.exit(0)
