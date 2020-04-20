#  Use map to call the strip method on each string in the following list:

from operator import methodcaller

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]


stripped_text = map(methodcaller("strip"), humpty_dumpty)

for line in stripped_text:
    print(line)

