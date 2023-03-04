# A 2D lists of names and hobbies
class_name_hobbies = [["Jenny", "Breakdancing",], ["Alexus", "Photography"], ["Grace", "Soccer"]]
#The sublist of Jenny is at index 0. The hobby is at index 1 of the sublist.
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)
# Output
# [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
#in order to modify elements in a 2D list, an index for the sublist and the index for the elment sublist need to be provided. The format for this list[sublist_index] [element_in_sublist_index] = new_value.
