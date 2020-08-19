dic_color = {'AliceBlue': '#f0f8ff', 'AntiqueWhite': '#faebd7', 'AntiqueWhite1': '#ffefdb','AntiqueWhite2': '#eedfcc', 'AntiqueWhite3': '#cdc0b0', 'AntiqueWhite4': '#8b8378', 'aquamarine1': '#7fffd4', 'aquamarine2': '#76eec6', 'aquamarine4': '#458b74', 'azure2': '#f0ffff'}

def color():
    get_choice = str(input('Enter your choice: '))
    while get_choice != '':
        if get_choice in dic_color:
            print(dic_color[get_choice])
            get_choice = 0
        elif get_choice not in dic_color:
            print('invalid choice')
            color()
        return
color()
