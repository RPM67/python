marks = {"rpm": 86, "rohit": 78, "ramesh": 45, "rakesh": 67}
print(marks["rpm"])

print((marks.get("rakhi"))) # this line returns none if this key value pair is not present in marks
#print(marks["rakhi"]) # this line gives error if this key value pair is not present in marks

print(marks.keys())
print(marks.values())
print(marks.items())


