import os
import csv

csvpath = os.path.join(os.path.abspath(__file__),'..', 'Resources', 'budget_data.csv')

months = []
profitLoss = 0
profitList =[]
with open(csvpath) as bankCsv:
    csvreader = csv.reader(bankCsv, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
            splitDates = row[0].split("-")
            months = months + [splitDates[0]]
            profitLoss = profitLoss + float(row[1])
            profitList.append(row[1])
uniqueMonths = set(months)
countOfMonths = len(uniqueMonths)
# print(profitList)

# Grabing the difference of current index subtracting by previous index
# for loop starts at 1 to start looking at second line to allow subtracting the first index
# end of range in loop is length of profitList

profitChange = []
singleChange = 0

for i in range(1, len(profitList)):
    singleChange = int(profitList[i]) - int(profitList[i - 1])
    profitChange.append(singleChange)

lengthOfProfitChange = len(profitChange)
totalOfProfitChange = sum(profitChange)
averageChange = round(totalOfProfitChange / lengthOfProfitChange, 2)
maxChange = max(profitChange)
minChange = min(profitChange)

print(profitLoss)
print(countOfMonths)
print(averageChange)
print(maxChange)
print(minChange)