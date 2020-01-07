#!/usr/local/bin/python3
"""
Bradley Dilger, cbdilger@gmail.com
parse captions copied from YouTube,
reduce the number of timestamps printed out,
put them in brackets,
and concatenate the strings involved. 

Usage:
process-yt-captions.py < raw-caption-file.txt > processed-captions.txt

00:00	all right we see red lights that's what
00:02	we want to see all right so I printed
00:06	out the questions okay so what we're
00:08	gonna do is first we have some questions
"""

# make an empty hash
Transcript = {}

# start our counter
increment = 0

# higher numbers will print fewer timestamps
timestamp = 8

# read in file from standard input
# https://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin

# needed for standard input
import sys

# read transcript file and build a directory with time:content as key:value pairs
for line in sys.stdin:
    time,content = (line.rstrip()).split('\t')
    Transcript[time] = content

# print transcript file 
for time in Transcript.keys():
	increment = increment + 1
	
	if (increment % timestamp == 0):
		print("\n\n", '[', time, ']', sep='')
		print(Transcript[time], end=' ')
	else:
		print(Transcript[time], end=' ')


print()
