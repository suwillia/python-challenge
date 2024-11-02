# python-challenge
Module 3 challenge

this is to complete the python module 3 challenge. the task is creating a Python script to analyze the financial records of your company.

PYbank folder contains the main.py that gives financial analyis for the bank. It provides, profit/loss totals over the tiem period, the changes and the greatest increase/decrease of profits with the corresponding month.
Running main.py in git bash is done via right clicking on main and then 'reveal in file explorer'. From the explorer file, use the 'show more options' and 'open git bash here'. Once in git bash type in python main.py . Results will be outputted to the analysis folder when done succesfully.

The current fold structure allows the file to be ran without ".." to move up to a separate folder. if you do get a file not found eror when running gitbash , please append the following lines in vistual studio
Line 9: file_to_load = os.path.join("..","Resources", "budget_data.csv")  # Input file path
line 10: file_to_output = os.path.join("..","analysis", "budget_analysis.txt")  # Output file path
