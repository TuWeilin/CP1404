"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    L_1 = data[0]
    L_2 = data[1]
    L_3 = data[2]
    L_4 = data[3]
    print('{0} is taught by {1} and has {2} '.format(L_1[0], L_1[1], L_1[2]))
    print('{0} is taught by {1} and has {2} '.format(L_2[0], L_2[1], L_2[2]))
    print('{0} is taught by {1} and has {2} '.format(L_3[0], L_3[1], L_3[2]))
    print('{0} is taught by {1} and has {2} '.format(L_4[0], L_4[1], L_4[2]))






def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open('subject_data.txt','r')
    Lines = input_file.readlines()
    L_input = []
    for i in range(4):
        line = Lines[i].split(sep = ',')
        L_input.append(line)
    input_file.close()
    return L_input

main()