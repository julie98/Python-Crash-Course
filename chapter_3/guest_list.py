guests = ['Karolina Kurkova', 'Gisele Bunchen', 'Eugenia Volodina', 'Naomi Campbell']
print(guests)
print(len(guests))

cannot_show = guests[3]
print("\n" + cannot_show + " cannot show.")

guests[-1] = 'Angela Lindvall'
print(guests)
print(len(guests))

print("\nI have a bigger table!")
guests.insert(0, 'Taylor Swift')
guests.insert(2, 'Karlie Kloss')
guests.append('Arianna Grande')
print(guests)
print(len(guests))

print("\nSorry guys, the table cannot be delivered in time, so I can only invite two.")

popped_guest = guests.pop()
print("\nSorry, " + popped_guest + ".")

popped_guest = guests.pop()
print("\nSorry, " + popped_guest + ".")

popped_guest = guests.pop()
print("\nSorry, " + popped_guest + ".")

popped_guest = guests.pop()
print("\nSorry, " + popped_guest + ".")

popped_guest = guests.pop()
print("\nSorry, " + popped_guest + ".")

print(guests)
print(len(guests))

del guests[0]
del guests[0]
print(guests)
print(len(guests))
