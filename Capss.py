def is_uppercase(x):
    words = x.split("_")
    for word in words:
        if word == word.upper():
            return True
        else:
            return False

(is_uppercase("AM dONALD"))