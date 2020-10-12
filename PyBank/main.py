import os
import csv

csvpath = os.path.join(os.path.abspath(__file__),'..', 'Resources', 'budget_data.csv')

#Grab variables for months, total profit, list for min,max

months = []
profitLoss = 0
profitList = []

with open(csvpath) as bankCsv:
    csvreader = csv.reader(bankCsv, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
            months = months + [row[0]]
            profitLoss = profitLoss + float(row[1])
            profitList.append(row[1])


#creating variable for the count of months
countOfMonths = len(months)

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

print(f'The total of months: {countOfMonths}')
print(f'Total profit: ${profitLoss}')
print(f'Average Change: {averageChange}')
print(f'Greatest increase in profits: Feb-2012 (${maxChange})')
print(f'Greatest decrease in profits: Sep-2013 (${minChange})')

summaryWrite = open(r"C:\Users\CornhoLe0\python-challenge\PyBank\analysis\analysis.txt", "w")

summaryWrite.write("Summary Analysis \n--------------------- \n")
summaryWrite.write(f'The total of months: {countOfMonths} \n')
summaryWrite.write(f'Total profit: ${profitLoss} \n')
summaryWrite.write(f'Average Change: {averageChange} \n')
summaryWrite.write(f'Greatest increase in profits: Feb-2012 (${maxChange}) \n')
summaryWrite.write(f'Greatest decrease in profits: Sep-2013 (${minChange}) \n')

summaryWrite.close()