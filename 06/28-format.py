arr = [1,  23,   5, 382,   1,  17,   4, 936]
string_ints = [str(num) for num in arr]

formated = [num.zfill(4).replace("0", " ") for num in string_ints]

print(
    len(formated) * 5 * "-",
    "\n",
    "|".join(formated),
    "\n",
    len(formated) * 5 * "-"

)
