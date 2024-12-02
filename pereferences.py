dic={}
def Preferences(filename):
    with open(filename, "r") as f:
       for line in f:
           [username, singers]=line.strip().split(":")
           singerList=singers.split(",")
           dic[username]=singerList
    return dic

           
