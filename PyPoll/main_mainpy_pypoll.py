# -*- coding: utf-8 -*-
import csv
import os


election_data = os.path.join("resources","election_data.csv")


def countvotes():
    total_count = 0
    counter = 0
    
    with open(election_data, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            csv_header = next(csvreader)
        
            for row in csvreader:
                if row[0] == 'Voter ID':
                    pass
                else:
                    counter = counter + 1
                
                total_count = total_count + 1
            return total_count
        



def listcandidates():
    candidates = []
    with open(election_data, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        
        for row in csvreader:
            if row[0] == 'Voter ID':
                pass
            else:
                if row[2] not in candidates:
                    candidates.append(row[2])
                else:
                    pass
        return candidates


def tally_votes():
    candidatedict = {}
    for candidate in candidates:
        candidatedict[candidate] = [0,0]
    
        with open(election_data, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            csv_header = next(csvreader)
            
            for row in csvreader:
                if row[0] == 'Voter ID':
                    pass
                else:
                    for key, value in candidatedict.items():
                        if key == row[2]:
                            value[1] = value[1] + 1
                            value[0] = round(((value[1] / total_count) * 100), 1)
                        else:
                            pass
    return candidatedict

def highestvotes():
    elected_candidate = 0
    for key, value in candidatedict.items():
        if value[1] > elected_candidate:
            elected_candidate = value[1]
            winner = key
        else:
            pass
    return winner



total_count = countvotes()
candidates = listcandidates()
candidatedict = tally_votes()
winner = highestvotes()
    
        

def printresults():
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes:  {total_count}")
    print("--------------------------")
    for key, value in candidatedict.items():
        print('' + key + ':', str(value[0]) + '% (' + str(value[1]) + ')')
    print("--------------------------")
    print('Winner: ', winner)
    
printresults()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
