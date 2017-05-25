#!/usr/bin/python

import os

NODES_NUMBER = 2**14

def calculate_parent(id):
	parent = ""
	while (id != 0):
		parent = ("/%d" + parent) % (id)
		id /= 2
	return parent


def generate_body(id):
	parent = calculate_parent(id)
	node = "{\"name\": \"Text%d\", \"path\": \"%s\"}" % (id, calculate_parent(id))
	return node

def generate_id(id):
	return "{\"index\": {\"_id\":\"%d\"}}" % (id)

def generate_node(id):
	index = generate_id(id)
	node = generate_body(id)
	return index + "\n" + node

def main():
	for i in range(1, NODES_NUMBER):
		print generate_node(i)

if __name__ == '__main__':
	main()

# 	{
# >  "name": "1",
# >  "path": "/a/b/c"
# > }