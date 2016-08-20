import json
import csv


def read_json_to_dictionary(json_file):
	with open(json_file) as json_data:
		data = json.load(json_data)
		for i in data:
			print i["topping"]

def write_keys_to_columns():
	pass

def write_data_to_rows()
	pass

def main():
	read_json_to_dictionary("cake.json")