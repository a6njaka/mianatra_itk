import re

name = "john"
my_regex = re.compile(rf"{re.escape(name)}-\d{{3}}-\d{{4}}", re.IGNORECASE)
text = "John-123-4567"

match = my_regex.search(text)
if match:
    print("Found:", match.group())