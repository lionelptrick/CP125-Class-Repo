# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # TODO: Implement this function

    names1 = open(file1, 'r')
    namelist1 = names1.read().splitlines()
    names1.close()

    names2 = open(file2, 'r')
    namelist2 = names2.read().splitlines()
    names2.close()

    combined = set(namelist1 + namelist2)
    sorted_names = sorted(combined)

    result = open(output_file, 'w')
    for names in sorted_names:
        result.write(names + "\n")
    result.close()

    return len(sorted_names)

    pass
# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
