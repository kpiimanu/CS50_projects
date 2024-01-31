import csv
import sys


def main():

    # TODO: Check for command-line usage (program,  database, DNA sequence ID )
    if len(sys.argv) != 3:
        print("Command-Line Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable using dictionary to organize data
    database = []
    with open(sys.argv[1], 'r') as file:
        # Variable to store cvs file being read into a dictionary
        read_cvs = csv.DictReader(file)
        # Each dictionary containing an individuals data appended into the database list
        for persons_data in read_cvs:
            database.append(persons_data)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        dna_sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence (using longest_match function)
    # Creating a list of the STR's (AGATC,AATG,TATC) but omitting name
    subsequences = list(database[0].keys())[1:]

    results = {}
    # Assistance with understanding how the longest_match function works in breaking it down and helping logic with Anvea
    for subsequence in subsequences:
        # Execute longest_match function for each subsequence and add to results
        results[subsequence] = longest_match(dna_sequence, subsequence)

    # TODO: Check database for matching profiles & print name of indiviual or "no match"
    for individual in database:
        match = 0
        for subsequence in subsequences:
            if int(individual[subsequence]) == results[subsequence]:
                match += 1

        # If all subsequences match with an individual
        if match == len(subsequences):
            print(individual["name"])
            return

    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()