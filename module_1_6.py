my_dict={"Julia":1996, "Andreu":1991}
print(my_dict)
print(my_dict["Julia"])
print(my_dict.get("Katya", "Такого ключа нет"))
my_dict.update({"Vasiliy":1995, "Igory":1975})
print(my_dict)
#my_dict.pop("Igory")
#print(my_dict)    в ответе получила: {'Julia': 1996, 'Andreu': 1991, 'Vasiliy': 1995}
a_=my_dict.pop("Igory")
print(a_)
print(my_dict)
my_set={1,8,6,False,"code",(1,2,5),(1,2,5),6}
print(my_set)
my_set.add(7)
my_set.add("Julia")
print(my_set)
my_set.discard(False)
print(my_set)

