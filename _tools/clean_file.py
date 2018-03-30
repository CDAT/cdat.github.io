from sys import argv, exit
import os.path

if len(argv) < 2:
	print "Need a file to fix."
	exit(1)

file_to_fix = argv[1]

if len(argv) < 8:
	print "Not enough arguments given"
	exit(1)

rest_of_args = argv[7:]

# Substitute the argument value for any use of args
def arg_replace(args, match):
	# Group 0 is the whole matched string
	usage = match.group(0)
	value = eval(usage)
	return repr(value)

import re
with open(file_to_fix) as infile:
	lines = []
	# Use this RE to replace any use of args with the value from argparse
	args_re = re.compile('args\.(\w+)')
	ifs = []
	skip_till = -1
	for index, line in enumerate(infile):
		if index < 2:
			lines.append(line)
			continue

		if index >= 2 and index < 17:
			# We want to build the same argparse object so we can get the relevant values
			# Exec is for statements, eval is for expressions
			exec(line)
			if index == 16:
				# Done building the argparse
				args = p.parse_args(rest_of_args)

				if args.gm == "oned":
					args.gm = "oneD"

				from functools import partial
				# Creates a function that calls partial with the first argument prepopulated with args
				replacer = partial(arg_replace, args)
		else:
			
			if index < 23 or index < skip_till:
				continue

			if line[:4] == "exec":
				line = "gm = vcs.create%s()\n" % args.gm

			
			# Replace any use of args
			line = args_re.sub(replacer, line)
			# we're stripping out any if statements, so indentation doesn't matter
			line = line.lstrip()

			if line[:3] == "try":
				try:
					int(args.projtype)
				except Exception:
					line = "ptype = '%s'\n" % args.projtype
					skip_till = index + 4
				else:
					line = "ptype = %d\n" % int(args.projtype)
					skip_till = index + 2


			if len(line) == 0 or line[:7] == "nm_xtra" or line[:3] == "fnm":
				line = "\n"

			# If statements are irrelevant; only code that is used got printed.
			if line[:2] == "if" or line[:4] == "elif":
				continue

			if line == "x.png(fnm)\n":
				lines.append("x.png('%s')\n" % os.path.basename(args.src))
				break
			
			lines.append(line)

with open(file_to_fix, "w") as f:
	f.writelines(lines)
