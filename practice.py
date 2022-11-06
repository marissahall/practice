# practice.py

import random

def dice(count = 3, sides = 6):
	num = 0
	for d in range(count):
		num+= random.randint(1,sides)
	return num

stats = {
	'str' : 0,
	'int' : 0,
	'wis' : 0,
	'dex' : 0,
	'con' : 0,
	'cha' : 0, 
}

for key in stats.keys():
	stats[key] = dice()
	
if __name__ == "__main__":
	print(stats)
