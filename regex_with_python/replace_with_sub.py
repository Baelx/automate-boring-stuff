import re

my_reg = re.compile(r"waterboarding",re.I)

redaction = my_reg.sub("REDACTED", "Waterboarding the capives only proved somewhat successful in yielding information.")

print(redaction)
