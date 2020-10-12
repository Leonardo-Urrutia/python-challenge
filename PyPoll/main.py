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
candidateTotals = {}

#Grabs count of total vote and fills dictionary with vote count for each candidate

with open(csvpath) as pollCSV:
    csvreader = csv.reader(pollCSV, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        allCandidatesWithDupes.append(row[2])
        candidateTotals[row[2]] = candidateTotals.setdefault(row[2], 0) + 1


uniqueCandidates = set(allCandidatesWithDupes)

khanVoteCount = round(int(candidateTotals["Khan"]) / total_votes, 3)
correyVoteCount = round(int(candidateTotals["Correy"]) / total_votes, 3)
liVoteCount = round(int(candidateTotals["Li"]) / total_votes, 3)
oTooleyVoteCount = round(int(candidateTotals["O'Tooley"]) / total_votes, 3)

khanPercentage = "{:.0%}".format(khanVoteCount)
correyPercentage = "{:.0%}".format(correyVoteCount)
liPercentage = "{:.0%}".format(liVoteCount)
oTooleyPercentage = "{:.0%}".format(oTooleyVoteCount)



print(f'Election Results')
print(f'Total Votes: {total_votes}')
print(f'Khan: {khanPercentage} with {candidateTotals["Khan"]} votes')
print(f'Correy: {correyPercentage} with {candidateTotals["Correy"]} votes')
print(f'Li: {liPercentage} with {candidateTotals["Li"]}')
print(f"""O'Tooley: {oTooleyPercentage} with {candidateTotals["O'Tooley"]}""")
print(f'Winner: Khan')

# print(total_votes)
# print(khanVoteCount)
# print(correyVoteCount)
# print(liVoteCount)
# print(oTooleykhanVoteCount)

# for candidate_name, vote_total in canidateTotals.items():
#     print(candidate_name)
#     print(vote_total)