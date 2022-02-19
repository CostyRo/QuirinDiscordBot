from random import choice
from json import dump as dump_json,load as load_json
# import choice from random module to generate a number element from a list
# and import the necessary functions from the json module

# a private function that update a user
def _update_user_points(id,modification,mode):

    """Private function that update a user""" 

    with open("json/points.json","r") as f: userpoints=load_json(f)
    # open the database

    if mode=="+": userpoints[str(id)]+=modification
    elif mode=="-": userpoints[str(id)]-=modification
    else: userpoints[str(id)]=modification
    # check if the modification is an additon or a substraction
    # or setting the number and perform the task

    with open("json/points.json","w") as f: dump_json(userpoints,f,indent=4)
    # update the database

# a function that check if user have an acccount or not
def have_account(id):

    """Function that check if user have an account or not"""

    with open("json/points.json","r") as f: return True if str(id) in load_json(f) else False 
    # open the database an check if the user have an account or not

# a function that return a random fact
def random_fact(fact):

    """Function that return a random fact"""

    if fact=="ff":
        with open("funfacts/fflist.txt","r") as f: return choice(f.readlines())
    else:
        with open("funfacts/sfflist.txt","r") as f: return choice(f.readlines())
    # load the correct list and return a random element

# a function that return the suggestion channel
def suggestion_channel(server_id):

    """Function that return the suggestion channel"""

    with open("json/suggestions.json","r") as f: channels=load_json(f)
    # open database with channels

    return channels[str(server_id)]
    # return the channel

# a function that update database
def update_points(id_list,modification_list,mode_list):

    """Function that update database"""

    for id,mod,mode in zip(id_list,modification_list,mode_list): _update_user_points(id,mod,mode)
    # browse the 3 lists and update all users with the given modifications

# a function that update the database with suggestion channels
def update_suggestion(server_id,channel_id):

    """Function that update the database with suggestion channels"""

    with open("json/suggestions.json","r") as f: channels=load_json(f)
    # open database with channels

    channels[str(server_id)]=channel_id
    # set the channel

    with open("json/suggestions.json","w") as f: dump_json(channels,f,indent=4)
    # update the database

# a function that return user's points
def user_points(id):

    """Function that return user's points"""

    with open("json/points.json","r") as f: userpoints=load_json(f) 
    # open database

    return userpoints[str(id)]
    # return the number of user's points