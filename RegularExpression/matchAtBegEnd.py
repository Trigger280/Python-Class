
import re

pattern = r"^Hello"

text = "Hello world"
match = re.search(pattern, text)
print("Match at start:", match.group() if match else "No match")
pattern = r"world$"
match = re.search(pattern, text)
print("Match at end:", match.group() if match else "No match")