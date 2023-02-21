# Intellisense-Test
Take home Test
#Use the Kuberenetes API and create a simple command line tool to provide a table output which includes
#the following details:
● Name of deployments
● Images of each deployment
● Date deployment was updated
Extend the tool to give the difference between two namespaces to show when some services are missing
or running different image versions. Deploy to a second namespace and make a few changes to it so that
we can see the difference in output.


# Execution Instruction
Instruction on how to Run the tool.

Requirements
1. Ubuntu KOPS cluster
2. Python
	
#	sudo apt install python
3. Python package installer - PIP
#	sudo apt install python3-pip
4. install Tabulate
	This is used to give a clean tabulated view of the results 
#	sudo pip install tabulate

Execution Instructions.

1. API_1.py is for solution 1 of the task. In other to 	execute this. 
#	Run python3 API_1.py
	This would give the result in "image for solution1.jpg"

2. API_2.py is for solution2 of the task, which gives extends the tool.
#	Run python3 API_2.py
	This would give the result in "image for solution2.jpg"



