#!/usr/bin/env python3

def array_of_ones(persons):
	name = []
	for first, last in persons.items():
		full_name = first.capitalize() + " " + last.capitalize()
		name.append(full_name)
	return name

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_ones(persons))
