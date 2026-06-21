def main():
    l1 = [1, 2, 3, 4, 5]
    
    # Store the function references in a list
    cloning_methods = [slice_l1, using_list, com_list]
    
    # Iterate through the functions, call them with l1, and print the result
    for method in cloning_methods:
        cloned_list = method(l1)
        # Using method.__name__ dynamically gets the name of the function
        print(f"Cloned using {method.__name__}: {cloned_list}")

# Manner 1: Slicing
def slice_l1(l1):
    l2 = l1[:]
    return l2

# Manner 2: Using the list() constructor
def using_list(l1):
    l2 = list(l1)
    return l2

# Manner 3: List Comprehension
def com_list(l1):
    l2 = [i for i in l1]
    return l2

if __name__ == "__main__":
    main()