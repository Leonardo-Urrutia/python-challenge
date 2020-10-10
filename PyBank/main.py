import os
import csv

csvpath = os.path.join(os.path.abspath(__file__),'..', 'Resources', 'budget_data.csv')

months = []
profitLoss = 0
with open(csvpath) as bankCsv:
    csvreader = csv.reader(bankCsv, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
            splitDates = row[0].split("-")
            months = months + [splitDates[0]]
            profitLoss = profitLoss + float(row[1])

uniqueMonths = set(months)
countOfMonths = len(uniqueMonths)
print(profitLoss)
print(countOfMonths)