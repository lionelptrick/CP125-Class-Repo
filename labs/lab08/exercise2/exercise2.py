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
    list1 = open(file1, 'r')
    list2 = open(file2, 'r')
    merged = open(output_file, 'w')

    names1 = set(list1.readlines())
    names2 = set(list2.readlines())
    result = list((names1 | names2) - (names1 & names2))

    merged.writelines(sorted(result))

    list1.close()
    list2.close()
    merged.close()



# Test your code here
result = merge_lists("C:/Users/User/CP125-Class-Repo/labs/lab08/exercise2/data/list1.txt", 
                     "C:/Users/User/CP125-Class-Repo/labs/lab08/exercise2/data/list2.txt", 
                     "C:/Users/User/CP125-Class-Repo/labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
