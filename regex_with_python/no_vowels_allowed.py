import re

no_vowels_regex = re.compile(r"[^aeiouAEIOU]")

normal_text = "One time I went to the park and it was real nice the end."

mo = no_vowels_regex.findall(normal_text)

print(mo)
