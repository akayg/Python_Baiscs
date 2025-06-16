import re

strn = "hello my name is AK007 and id is 6897316"

masked = re.sub(r"\d", "#", strn)

print(masked)