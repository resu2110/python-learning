from datetime import datetime
from random import randint
from time import sleep

odds = [
	1,3,5,7,9,11,13,15,17,19,
	21,23,25,27,29,31,33,35,37,39,
	41,43,45,47,49,51,53,55,57,59
]



amount_of_time = randint(5,100)
for i in range(0,5):
	right_this_minute = datetime.today().minute
	if right_this_minute in odds:
		print("This minute seem odds")
	else:
		print("well, dickhead, ..")
	sleep(amount_of_time)