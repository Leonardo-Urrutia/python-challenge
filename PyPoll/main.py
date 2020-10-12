#1 total number of votes cast
#2 complete list of candidates who received votes
#4 percentage of votes per candidate
#3 total of votes per candidate
#5 Winner of poll
#

import os
import csv
csvpath = os.path.join(os.path.abspath(__file__),'..', 'Resources', 'election_data.csv')

total_votes = 0
allCandidatesWithDupes = []
canidateTotals = {}

with open(csvpath) as pollCSV:
    csvreader = csv.reader(pollCSV, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        allCandidatesWithDupes.append(row[2])
        canidateTotals[row[2]] = canidateTotals.setdefault(row[2], 0) + 1

print(total_votes)
uniqueCandidates = set(allCandidatesWithDupes)

for candidate_name, vote_total in canidateTotals.items():
    print(candidate_name)
    print(vote_total)