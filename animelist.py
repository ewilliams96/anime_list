class Anime:
	# constructor: takes name of anime (string) and number of episodes (int)
	# and optionally length if episodes are not standard length
	
	def __init__(self, name, episodes, length=22):
		self.name = name
		self.episodes = episodes
		self.length = length
		

	def to_string(self):
		str = self.name + ', ' + self.episodes


def run_animelist():
	read_from_file("animelist.txt")
	run_program = True
	while(run_program):
		print('''1. View list
			2. Total time spent
			3. Append to list
			4. Save Session
			5. Quit''')
		choice = input('>')
			if choice == '1':
				view_list()
			elif choice == '2':
				total_time()
			elif choice == '3':
				add_anime()
			elif choice == '4':
				write_to_file()
			elif choice == '5':
				print("Goodbye!")
				run_program = False
			else:
				print("Invalid input. Try again.")


	


# read saved data from text file	
# takes name of file 
# returns list of Anime objects 
def read_from_file(fname):
	filename = fname
	file = open(fname, 'r')

	line_list = file.readlines()

	anime_list = []

	for line in line_list:
		split_index = 0
		for i, c in enumerate(line):
			if c == ',':
				split_index = i

		anime_name = line[0:split_index]
		anime_episodes = line[split_index+2:]

		anime = Anime(anime_name, anime_episodes)
		anime_list.append(anime)
	return anime_list


run_animelist()


