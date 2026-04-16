customers = {"name":"naman","age":23, "is_verify": True}

print(customers["name"])

print(customers.get("name"))

# we can update and add the new keys

customers["name"] = "numun"
print(customers.get("name"))

del customers["name"]
print(customers)

dict1 = {"name":"naman",
         "bike":"CBR",
         "car":"maruti"}

print(sorted(dict1))

#  dict1.update(dict2) concatinate two dict