#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--command", help="command to execute when the countdown reaches zero.")
parser.add_argument("-t", "--theme", help="change gtk theme, specifying a gtkrc file path")
parser.add_argument("-p", "--position", help="x and y of the window")
parser.add_argument("-m", "--message", help="the text message to be displayed")
parser.add_argument("-C", "--countdown", help="value in seconds of the coundown")

args = parser.parse_args()

def get():
	global args
	return args
