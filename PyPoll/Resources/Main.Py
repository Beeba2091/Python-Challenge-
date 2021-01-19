import os
import csv

# Define Variables
num_votes = 0
candidates  = []
vote_counts = []

# List of files
election_data = ['1','2']

# Loop through files
for files in election_data:
    #Get CSV
    election_dataCSV = os.path.join("//Users/habibasani/Desktop/GT_Bootcamp_Dataviz_homework/Python-Challenge-/PyPoll", 'election_data_' + files + '.csv')

    # Open current CSV
    with open(election_dataCSV) as cvsfile:

        cvsreader = cvs.reader(csvfile, delimeter=',')

        # Skip Headers
        line = next(cvsreader,None)

        # Process votes
        for line in cvsReader:

            #Add to total number of votes
            num_votes = num_votes + 1

            # Candidate voted for
            candidate = line[2]

            #If the cancdidate has other votes then add to vote total
            if candidate in candidates:
                candidate_index = candidate_index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
            # Else create new place in list for candidate
            else:
                candidates.append(candidate)
                vote_counts
    
    # Create variables for calculations
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    # Percentage of vote for each candidate and the winner
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/num_votes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]

    # Round decimal

    percentages = [round(i,2) for i in percentages]

    # Print results
    print ("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {num_votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
        print("----------------------------")
        print(f"Winner: {winner}")
        print("----------------------------")

        # Name white file
        output_file = election_dataCSV[0:-4]

        write_election_dataCSV = f"{output_file}pypoll_results.text"
        
        # Open write file
        filewriter = open(write_election_dataCSV, mode = 'w')

        # Print to write file
        filewriter.write("Election Results\n")
        filewriter.write("--------------------------\n")
        filewriter.write(f"Total Votes: {num_votes}\n")
        for count in range(len(candidates)):
            filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
        filewriter.write("--------------------------\n")
        filewriter.write(f"Winner: {winner}\n")
        filewriter.write("--------------------------\n")

        # Close file
        filewriter.close()