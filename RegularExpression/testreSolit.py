import re
test="""

1. asdfas
2. asdf
3. sorted asdfas
4. sdfsdf asdfas """
pattern = r"\d.\s"

splittedList = re.split(pattern, test)
print(splittedList)