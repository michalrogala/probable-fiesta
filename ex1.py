types_of_people = 10
x = f"Istnieje {types_of_people} rodzajow ludzi."

binary = 'binarny'
do_not = "nie znają"
y = f"Ci, ktorzy znają system {binary} i ci, ktorzy go {do_not}."

print(x)
print(y)

print(f"Powiedziałem: {x}")
print(f"Powiedziałem rowniez: '{y}'")

hilarious = False
joke_evaluation = "Czyż to nie jest przezabawny dowcip!? {}"

print (joke_evaluation.format(hilarious))

w = "To jest lewa strona..."
e = "łańcucha znakow z prawą stroną."

print(w+e)
