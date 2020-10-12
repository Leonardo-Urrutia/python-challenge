#1 total number of votes cast
#2 complete list of candidates who received votes
#4 percentage of votes per candidate
#3 total of votes per candidate
#5 Winner of poll


import os
import csv
csvpath = os.path.join(os.path.abspath(__file__),'..', 'Resources', 'election_data.csv')
summaryWrite = os.path.join(os.path.abspath(__file__),'..', 'analysis', 'analysis.txt')

total_votes = 0
candidateTotals = {}

#Grabs count of total vote and fills dictionary with vote count for each candidate

with open(csvpath) as pollCSV:
    csvreader = csv.reader(pollCSV, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidateTotals[row[2]] = candidateTotals.setdefault(row[2], 0) + 1


#Converting the values in dictionary to unique variable and use that variable to format as percentage.

khanVoteCount = round(int(candidateTotals["Khan"]) / total_votes, 3)
correyVoteCount = round(int(candidateTotals["Correy"]) / total_votes, 3)
liVoteCount = round(int(candidateTotals["Li"]) / total_votes, 3)
oTooleyVoteCount = round(int(candidateTotals["O'Tooley"]) / total_votes, 3)

khanPercentage = "{:.0%}".format(khanVoteCount)
correyPercentage = "{:.0%}".format(correyVoteCount)
liPercentage = "{:.0%}".format(liVoteCount)
oTooleyPercentage = "{:.0%}".format(oTooleyVoteCount)

#store the printing analysis as a variable to use multiple times
output = (
    f'Election Results\n'
    f'--------------------\n'
    f'Total Votes: {total_votes}\n'
    f'Khan: {khanPercentage} with {candidateTotals["Khan"]} votes\n'
    f'Correy: {correyPercentage} with {candidateTotals["Correy"]} votes\n'
    f'Li: {liPercentage} with {candidateTotals["Li"]} votes\n'
    f"""O'Tooley: {oTooleyPercentage} with {candidateTotals["O'Tooley"]}\n"""
    f'--------------------\n'
    f'Winner: Khan\n'
)

print(output)
with open(summaryWrite, "a") as txtSummary:
    txtSummary.write(output)