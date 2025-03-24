import re

print("1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.\n")

numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]

for n in numbers:
    if n >= 0:
        print(n)

print("\n2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči.\n")

names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
i = 0
value = ''

while value != "Alice":
    print (names[i])
    value = names[i+1]
    i = i+1

print("\n3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0.\n")

random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]
new_list = [x for x in random_codes if '0' in x]
print(new_list)

print("\nDobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'\n")


random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]
rx = re.compile(r'(.)\1\1')
for new_code in random_codes:
    if rx.search(new_code):
        print(new_code)


new_codes = [x for x in random_codes if rx.search(x)]
print(new_codes)
