import sys

def text_analyzer(*txt):
    nb_arg = len(txt)
    # print(nb_arg)
    total = 0
    space_count = 0
    punct_count = 0
    upper_count = 0
    lower_count = 0
    if (nb_arg == 0):
        print("What is the text to analyse?")
        txt = []
        txt.append(input())
    elif (nb_arg > 1):
        print("ERROR")
        exit()
        
    for str in txt:
        total = len(str)
        for a in str:
            if (a.isupper() == True):
                upper_count += 1
            elif (a.islower() == True):
                lower_count += 1
            elif (a.isspace() == True):
                space_count += 1
            elif (a.isalnum() == False):
                punct_count += 1
    print("The text contains ", total, " characters:\n- ", upper_count," upper letters\n- ", lower_count, " lower letters\n- " , punct_count," punctuation marks\n- ", space_count,"spaces")