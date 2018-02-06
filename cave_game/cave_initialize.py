import shelve

locations = shelve.open("locations")
locations["0"] = {"desc": "Quit",
                  "exits": {},
                  "namedExits": {}}

locations["1"] = {"desc": "You are standing at the end of a road before a small brick building",
                  "exits": {"W": '2', "E": '3', "N": '5', "S": '4', "Q": '0'},
                  "namedExits": {"2": '2', "3": '3', "5": '5', "4": '4'}}

locations["2"] = {"desc": "You are at the top of a hill",
                  "exits": {"N": '5', "Q": '0'},
                  "namedExits": {"5": '5'}}

locations["3"] = {"desc": "You are inside a building, a well house for a small stream",
                  "exits": {"W": '1', "Q": '0'},
                  "namedExits": {"1": '1'}}

locations["4"] = {"desc": "You are in a valley beside a stream",
                  "exits": {"N": '1', "W": '2', "Q": '0'},
                  "namedExits": {"1": '1', "2": '2'}}

locations["5"] = {"desc": "You are in the forest",
                  "exits": {"W": '2', "S": '1', "Q": '0'},
                  "namedExits": {"2": '2', "1": '1'}}

locations.close()


vocabulary = shelve.open("vocabulary")

vocabulary["QUIT"] = "Q"
vocabulary["QUIT"] = "N"
vocabulary["QUIT"] = "S"
vocabulary["QUIT"] = "E"
vocabulary["QUIT"] = "W"
vocabulary["QUIT"] = "1"
vocabulary["QUIT"] = "2"
vocabulary["QUIT"] = "3"
vocabulary["QUIT"] = "4"
vocabulary["QUIT"] = "5"

vocabulary.close()

