#!/usr/bin/python -tt
# 'shroom-scorer

'''
This scoring program takes as an argument the input ...blah, blah

...finish documentation
'''

def scorer(key, predictions):
    msg = False    
    #-----
    # normalize input by ensuring all lowercase and remove whitespace
    submit = [answer.lower().strip() for answer in predictions]
    #-----
    # compare input to answer key
    correct = [e for e in range(len(key)) if key[e] == submit[e]]
    accuracy = len(correct)/len(submit)
    if accuracy < 1: msg = True
    print('    ' + str(len(correct)) + ' correct and ' + 
        str((len(submit)-len(correct))) + ' wrong.')
    print('    Prediction accuracy is {:.2%}'.format(accuracy))
    return(msg)
 
# Calls the above functions with participant inputs.
def main():
    import sys
    #-----
    # read in answer key and assign to list
    f = open('shroom_answer_key.txt', 'r')
    truth_data = [e.strip() for e in f.readlines()] #remove \n characters
    f.close
    #-----
    # read in participant's submission from .txt file
    team_input = sys.argv[1]
    t = open(team_input,'r') 
    submission = t.readlines()
    t.close
    #-----
    # print preamble to console
    print('\nThank you for submitting your predictions...')
    print('    How well did you choose?\n')
    print("Your 'shroom-a-thon results:")
    #-----
    # call scorer function, assigning output to flag
    flag = scorer(truth_data, submission)
    if flag == True:
        print('\n    ...and one bad mushroom spoils the whole meal!!')
    else:
        print("\n    Congratulations! Let's eat.")

if __name__ == '__main__':
    main()