#!/bin/bash

# Specify the directory to start with
start_dir=$(pwd)

# Loop through directories
for dir in */;
do
	# Go up one level
	cd "$dir"
	echo "$dir"

	# Find the README file
	README=$(find . -maxdepth 1 -name "README")

	# Check if the README
	if [ -f "$README" ]; then

		# Make the README file executable
		chmod + u+x "$README"

		# Give the name of the README file
		echo "Executing $README"

		# Execute the README file
		bash "$README"
	fi
	# Go one level up
	cd ..

done
