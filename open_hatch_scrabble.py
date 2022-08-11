import sys
 
def get_TILE(RACK):
   r = RACK
   for i in range(0, len(r)):
       return r[i]

def get_score(RACK):
    s = 0
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
	TILE = get_TILE(RACK)
	if TILE in score:
		for i in RACK:
        		s += score(keys)
        		score.keys()
        	return s
RACK = sys.argv[1]
RACK = RACK.lower()
A = get_score(RACK) 
print(A)
filename = "scrabble.txt"
words_list = []
for word in open(filename):
        w = word.strip("\n").split(",")
        words_list.extend(w)
print(words_list) 
