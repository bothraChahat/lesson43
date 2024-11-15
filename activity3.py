#write a python program to create a  list with five students' details (roll no name grade)
# then  convert that list into a dictinary

def converttodict(lst):
    result_dict={}
    for item in lst:
        result_dict[item[0]]=item[1:]
    return result_dict

students=[[1,'virat',1],[2,'yuvi',4],[3,'hardik',2],[4,'rohit',5],[5,'mahi',8]]

print("original list is ", students)
