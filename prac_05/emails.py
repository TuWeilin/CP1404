import re
mail_name_dic = dict()
def mail_name_get():
    '''To get user mails and name'''
    #use re.findall
    mails = str(input('enter your mail: '))
    mails = str(mails)
    while mails != '':
        names = ''.join(re.findall(r'[A-Za-z]', mails))
        print('Is this your name? {} Y/N'.format())
        Choice = str(input('>>>'))
        Choice = str(Choice)
        while Choice == 'Y' or Choice == 'y ':
            names = names.title()
            mail_name_dic[names] = mails
            mail_name_get()
        if Choice == 'N' or Choice == 'n':
            names = list(names).pop
        else:
            print('invalid choice')
    return
mail_name_get()
