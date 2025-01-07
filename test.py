import re

name = "john"
phone_regex = re.compile(rf"{name}-\d{3}-\d{4}")

text = "john-456-7890"
match = phone_regex.search(text)
if match:
    print("Found:", match.group())
