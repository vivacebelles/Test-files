import os
import shutil
from os import path

if path.exists("loop.py"):
	src = path.realpath("loop.py")
	head, tail = path.split(src)
	print "path: " + head
	print "file: " + tail;
