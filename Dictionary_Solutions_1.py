grades = {
    "John": [98, 79, 100],
    "Mary": [56, 79, 28],
    "Eve": [68, 45, 88],
    "Alice": [80, 99, 65],
    "Bob": [87, 90, 95]
}

def listStudents(dic):
    """Given a dictionary with (student name,list of grades) as key-value pairs, 
       return the list of students names"""
    return list(dic.keys())


list_average = lambda input_list: round(sum(input_list)/len(input_list),3)


def searchStudent(dic, name):
    """Given a dictionary with (student name,list of grades) as key-value pairs and a student name,
       return a tuple containing the student name and average grade for that student"""
    if name in dic:
        return (name, list_average(dic[name]))
    else:
        return "Student not found"


def computeIndividualAverage(grades):
    """Given a dictionary with (student name,list of grades) as key-value pairs,
       return a dictionary containing the student name and average grade as key-value pairs"""
    return dict(map(lambda dict_item: (dict_item[0], list_average(dict_item[1])),
                    grades.items()))

def getSubsetStudents(grades, threshold):
    """Given a dictionary with (student name,list of grades) as key-value pairs and a threshold,
       return the list of tuples containing students names and their avergeraves for students
       with average grade greater than the threshold"""
    dic = computeIndividualAverage(grades)
    return list(filter(lambda v: v[1] >= threshold , dic.items()))






