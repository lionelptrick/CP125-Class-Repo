# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id and score on alternating lines)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    # TODO: Implement this function
    score_file = open(input_file, 'r')
    passing_file = open(output_file, 'w')

    lines = score_file.readlines()

    count = 0

    for i in range(0, len(lines), 2):
        student_id = lines[i].strip()
        score = int(lines[i+1].strip())

        if score >= 80:
            passing_file.write(f"{student_id} {score}\n")
            count += 1

    score_file.close()
    passing_file.close()

    return count

    pass


# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
