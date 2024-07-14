def ft_filter(func, str_list):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of
    iterable for which function(item) is true.
    If function is None, return the items that are true.
    """
    if func is None:
        return [word for word in str_list if word is not None]

    return [word for word in str_list if func(word)]
