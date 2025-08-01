import pickle

file = open("Section09 - Binary Files/colors.pckl", "rb")

read_color_list = pickle.load(file)

print(read_color_list)
