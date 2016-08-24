import json
import csv


def read_json_to_dictionary(json_file):
	with open(json_file) as json_data:
		data = json.load(json_data)
		return data

def write_keys_to_columns(data):
	keylist = data.keys

def write_data_to_rows():
	pass

def main():
	print read_json_to_dictionary("cake.json")
	#print write_keys_to_columns(data)

if __name__ == '__main__':
	main()