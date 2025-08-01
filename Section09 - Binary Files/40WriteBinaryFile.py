#Import module pickle to write binary files

import pickle

color_list = ["red", "green", "blue", "yellow"]

#Open the file in binary mode
file = open("colors.pckl", "wb")

#Write the list to the file
pickle.dump(color_list, file)

#Close the file
file.close()