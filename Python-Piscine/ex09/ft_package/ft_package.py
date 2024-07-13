def count_in_list(lst, item):
    """Counts the number of occurrences of the item in the list."""
    count = 0
    for element in lst:
        if element == item:
            count += 1
    return count