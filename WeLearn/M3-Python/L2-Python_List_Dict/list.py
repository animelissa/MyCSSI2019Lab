# students = ["Alice", "Javi", "Damien"]
# students.append("Delilah")
# print(students)

# students = ["Alice", "Javi", "Damien"]
# students.insert(1, "Zoe")
# print(students)

# students = ["Alice", "Javi", "Damien", "Javi"]
# students.remove("Javi")
# # print(students)


# smith_siblings = ["Emliy", "Monique", "Giovanni"]
# smith_siblings.append("Delilah")
# smith_siblings.append("Thor")
# smith_siblings.append("Smith")
# smith_siblings.append("Greg")
# for name in smith_siblings:
#     print(name + " Smith")


# smith_siblings = ["Emliy", "Monique", "Giovanni", "Brianna", "Javi"]
# for index in range(len(smith_siblings)):
#     smith_siblings[index] = smith_siblings[index] + " Smith"
# print(smith_siblings)

# superheroes = ["Captain Marvel", "Wonder Woman", "Storm", "Kamala Khan", "Bubmblebee", "Jessica Jones"]
# demoteed_hero = str(raw_input("What superhero do you want to eliminate from the top 5? "))
# if demoteed_hero in superheroes:
#     superheroes.remove(demoteed_hero)
#     print("Top 5 heroes:", superheroes)
# else:
#     print("Hero not found.")


names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
print(names[::-1])
print(names[4:2:-1])
x = names
print(names[::2])
