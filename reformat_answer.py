def reformat_answer(text):
    result = ""
    n = len(text)
    for i in range(n):
        t = text[i]
        tmp = ""
        if i != n - 1:
            tmp = text[i + 1]
        if tmp != "#" and t != "#":
            result += f"{t}".lower()
        elif t != "#":
            result += f"{t}".upper()
    return result


# Example usage
print(reformat_answer("A#NOSY"))  # Output: "Anosy"
