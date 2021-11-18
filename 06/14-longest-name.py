def get_longest_name(names):
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longestss = name
    return longest


print(get_longest_name(
    ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']))
