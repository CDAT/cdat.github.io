#!/bin/bash
echo "Please enter the path to your install of UVCDAT"
read -ep "Path: " binpath

source $binpath/bin/setup_runtime.sh

echo "Please enter the path to your build directory for UVCDAT"
read -ep "Path: " buildpath

tests="$buildpath/Testing/vcs/CTestTestfile.cmake"

# Find the relevant tests
IFS=$'\n'
results=$(grep 'test_vcs_basic_gms.py' $tests)

py=$(which python)
for test in $results
do
	# Strip out extra information
	args=$(echo $test | sed -E -e "s/^[^\"]+\"[^\"]+python\" //" -e "s/\"//g" -e "s/\)$//")
	
	# Figure out what the --source argument's value is (the name of the script we'll be building)
	image_file=$args
	regex="source=(.+)"
	[[ $image_file =~ $regex ]]
	image_file="${BASH_REMATCH[1]}"

	# Build the command to trace the script
	command="$py -m trace --trace $args"

	echo "Image file: $image_file"
	echo "Command to generate file: $command"

	output_file=${image_file##*/}
	output_file=${output_file%%.*}.py
	echo "Output file: $output_file";

	# IFS has to be all whitespace for $command to be correctly interpreted by BASH
	unset IFS

	echo "Tracing & cleaning test script...";
	$command 2>/dev/null | grep test_vcs_basic_gms | sed -E -e "s/ --- modulename.*//" -e "s/^[^ ]+ //" > $output_file

	echo "Cleaning script of test cruft"
	python clean_file.py $output_file $command

	# Restore it to \n before we continue looping
	IFS=$'\n'
done
unset IFS

echo "Done!"
