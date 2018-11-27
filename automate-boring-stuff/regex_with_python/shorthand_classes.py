import re

xmas_regex = re.compile(r"\d+\s\w+") # pattern will match one or more consec. numb, one "space" char, and one or more consec. letter char.
mo = xmas_regex.findall("12 doves, 11 nancies,10 ports, 1 partrige")

print(mo)

another_regex = re.compile(r"\D+\S+\W+") # one or more non-digit char, one or more non-space char, one or more non-word char.
mo2 = another_regex.search("helpingiscaring  14  .w")

"""the above will match until is hits a char. that it's stuck on.
In this case, all the letters(which are not digits), passed the
space(also not digits) right up until the digits. Then it'll switch
to the non-space char. and match the numbers. It'll match 14 and then
hit the space again and switch to the non-word char, which will catch
the period. It won't match the w at the end."""

print(mo2.group())
