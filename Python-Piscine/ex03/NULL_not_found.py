def NULL_not_found(object: any) -> int:
    if object is None:
        print("NULL")
    elif type(object) is float and object != object:
        print("Not a number")
    elif type(object) is int and object == 0:
        print("Zero")
    elif type(object) is str and object == "":
        print("Empty")
    elif type(object) is bool and object == False:
        print("Fake")
    else:
        print("Not found")
    return 42