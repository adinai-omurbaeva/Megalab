def is_isogram(string):
    if len(string) == len(set(string.lower())):
        return True
    else:
        return False