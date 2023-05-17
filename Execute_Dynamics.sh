#!/bin/bash

# Specify the directory to start with
for dir in charmm*;
do
	# Go into the 'amber' directory
	cd "$dir/amber"
	
	# Check for the README file
	if [ -f "README" ];
	then
		# Execute the README file
		echo "Executing ./README"
		./README
		echo "Go to the next"
		
	else
		echo "README file not found in $dir/amber"
	fi
	
	# Go back to the parend directory
	cd ./../..

done
	
	
