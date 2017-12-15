some_cats = ['cat1', 'cat2', 'cat3', 'murphy']
the_second_cat = some_cats[1]

print(some_cats)

some_cats.remove(some_cats[1])

print(some_cats, the_second_cat)

some_cats.append('smallcat')
some_cats.insert(-4, 'smallercat')

print(some_cats)

some_cats.sort(reverse=True)

print(some_cats)

some_cats.sort(key=str.lower)

print(some_cats)
