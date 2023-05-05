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

#calculate whether increment streak
def habitMet():
    habits = load_save()
    for habit in habits:
        print("Habit: "+habit + "?")
        #try:
            #habitToday = input("Y/n: ")

#function for displaying a specific object
def display_habit(habit):
    print(habit.name)
    print(habit.streak)
    return 0

#function to display habits and their streaks
def display_habits():
    return 0



if __name__ == '__main__':
    #writeSave()
    #load_save()
    #habitMet()
    test_habit = habit("Yoyo")
    display_habit(test_habit)
    #save_habit(test_habit)
    file_test = open('save.pickle', 'wb')
    pickle.dump(test_habit, file_test)

    #read test
    #test_open_filehandler = open('save.pickle', 'rb')
    #objectTest = pickle.load(test_open_filehandler)
    #print(object.name)