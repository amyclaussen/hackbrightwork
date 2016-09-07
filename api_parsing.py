from urllib2 import urlopen
from json import load
from pprint import *
from api_movieinfo import *

def get_data():
	#sf open data source: film location in sf
	apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"

	#open the apiUrl and assign data to variable
	response = urlopen(apiUrl)

	json_obj = load(response)

	return json_obj

def get_movie_info(json_data):
	MovieInfo_objects = []
	for entry in range(len(json_data)):
		# print entry
		try:
			director = json_data[entry]["director"]
			release_year = json_data[entry]["release_year"]
			title = json_data[entry]["title"]
			actor_1 = json_data[entry]["actor_1"]
			actor_2 = json_data[entry]["actor_2"]
			location = json_data[entry]["locations"]

			new_MovieInfo_object = "movie_" + str(entry)

			new_MovieInfo_object = MovieInfo(director = director, release_year = release_year, title = title, actor_1 = actor_1, actor_2 = actor_2,location = location)
			MovieInfo_objects.append(new_MovieInfo_object)

		except:
			pass
	return MovieInfo_objects





def main():
	json_data = get_data()
	# pprint(json_data, indent = 4)
	MovieInfo_objects = get_movie_info(json_data)
	print MovieInfo_objects

if __name__ == '__main__':
	main()
