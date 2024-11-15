mydict={'name':'seru','age':5}

print(mydict)

#adding values
mydict['grade']=1

print("updated dictionary is",mydict)

print(mydict.get('name'),"studies in grade",mydict.get('grade'))

#removing value
mydict.pop('age')

print("updated didctionary after removal is ",mydict)

#update value of dictionary
mydict['name']="prince"

print("updated dictionary is",mydict)
