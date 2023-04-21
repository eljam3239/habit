import json
import pickle

class habit():
    def __init__(self, name):
        self.name = name
        self.streak = 0

def save_habit(habit):
    try:
        with open("save.pickle", "wb") as f:
            pickle.dump(habit, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

def load_save():
    with open('save.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    
    return json_object
    #print(type(json_object))


#overwrites contents of save file
def writeSave():
    dictionary = {
    "creatine": "Y",
    "journal": "n",
    "gym": "Y"
    }
 
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
 
    # Writing to sample.json
    with open("save.json", "w") as outfile:
        outfile.write(json_object)

def habitMet():
    habits = load_save()
    for habit in habits:
        print("Habit: "+habit + "?")
        #try:
            #habitToday = input("Y/n: ")




if __name__ == '__main__':
    #writeSave()
    #load_save()
    #habitMet()
    test_habit = habit("Yoyo")
    save_habit(test_habit)