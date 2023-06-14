#!/bin/bash

# Specify the directory to start with
for dir in charmm*;
do
	cd "$dir"
	for subdir in charmm*;
	do
		# Go into the 'amber' directory
		cd "$subdir/amber"
		
		# Check for the README file
		if [ -f "README" ];
		then
			# Give permissions to the README file
			echo "FillInPasswordOfSudoPermissions" | sudo -S chmod 777 README
			echo "Permissions set for README"

			# Execute the README file
			echo "Executing the README file"
			./README
			echo "Go to the next"
			
		else
			echo "README file not found in $dir/$subdir/amber"
		fi
		
		# Go back to the $subdir directory
		cd ../..
	done

	# Go back to the $dir directory
	cd ..

done
	
	
