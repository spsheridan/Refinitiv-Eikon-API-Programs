# Refinitiv-Eikon-API-Programs
These two programs access information from the Refinitiv desktop application. 

## Description
There are two programs in this repository. 
- The program "newsAppV1.py" continuously accesses news headlines from the Eikon workspace, and prints the news to the terminal. The idea is to have a live newsfeed of stock news that is associated with the tickers in the input ticker CSVs.
- The program "floatApp.py" first takes in a list of desired tickers. Then, it accesses the Eikon workspace for information on those tickers such as free float, shares oustanding, and short interest. It then prints out the information to the terminal. The program could be easily upgraded to include a lot more information and to save the information into a CSV.
