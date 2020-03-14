print("Program for a dictionary of a person")
person = {"name": "John Smith", "gender": "Male", "age": 21, "address": "Sheridan Park", "phone": "998-768-9900"}
user = input("What information you want: ")
result = person.get(user, "That information is not available")
print(result)
