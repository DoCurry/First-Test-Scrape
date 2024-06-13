import json

with open('./tree.json') as f:
    data = json.load(f)

def getchoices(ques):
    if ques in data["end"]:
        return "The END"
    return list(data[ques].keys())

def respond(sys,user):
    try:
        if user in data["end"]:
            return "The END"
        
        if user==None or "":
            return getchoices(sys)
        elif sys in data.keys():
            if user in data[sys]:
                return data[sys][user]
            else:
                return sys
        else:
            return "User Request Not Valid"
    except Exception as e:
        return "An Unexpected Error Occured"+repr(e)