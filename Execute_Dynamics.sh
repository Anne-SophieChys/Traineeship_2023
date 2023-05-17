#!/bin/bash

# Specify the directory to start with
for dir in CHARMM*;
do
	# Go into the 'amber' directory
	cd "$dir/amber" || continue
	
	# Check for the README file
	if [ -f "README" ];
	then
		# Execute the README file
		echo "Executing ./README"
		./README
		
	else
		echo "README file not found in $dir/amber"
	fi
	
	# Go back to the parend directory
	cd ./..

done
	
	
