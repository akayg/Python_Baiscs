import re

snt="hello my name is AK007 and my id is 9877588"

nums = re.findall(r"\d+",snt)

print(nums)

