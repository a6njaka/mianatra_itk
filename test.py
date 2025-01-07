import re

# Compile the regular expression pattern


nn = "3"
phone_regex = re.compile(r"\d{}-\d{3}-\d{4}")

# Use the compiled pattern for matching
text1 = "My phone number is 123-456-7890."
match1 = phone_regex.search(text1)
if match1:
    print("Phone number found in text1:", match1.group())