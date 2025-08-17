List1=["Laiba","Anwwar",90,30,50.0,90.5]
print("Simply print the list,Multiple Datatype it contain:\n",List1)
#How i print the Second item of the list
print("Indexing is used to print specific element:,\n")
print(List1[1])

#Iterate the all elements in the list
for item in List1:
    print("Triversing the list elements one by one:\n",item)

    #Append method is used to add the string
List1.append("Cost of the month")
print(List1)
# Insert the value at the sspecific index
List1.insert(0,"Hello")
print(List1)
#Remove the value
List1.remove("Laiba")
print("Removing the specific value",List1)
# pop the element at the pecific index "POP"
List1.pop(1)
print("Removing the specific element through the index",List1)
#Assigning the List1 2nd element to the "500"
List1[1]=500
print("Assigning new value at 1 index /n",List1)
print("check the Type of the Specific item\n") 
print(type(List1[1]))
