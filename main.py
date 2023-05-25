from datetime import datetime, timedelta
import os
from pathlib import Path

def main(): 
	date = (datetime.today() + timedelta(1)).strftime('%m-%d-%Y')

	path = 'standups/{0}.txt'.format(date)
	mode = 'a' if os.path.exists(path) else 'w'

	file = open(path, mode)
	filename = Path(path)

	with file as f:  

		if mode == "w":
			f.write("**Yesterday**\n")

		user_action = None
		while (user_action != ""):
			user_action = input("What task did you accomplish? (enter to quit): ")
			f.write("{0}\n".format(user_action))
		f.write("**Today**\n")

	f.close()

main()