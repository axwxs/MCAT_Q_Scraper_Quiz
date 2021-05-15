from bs4 import BeautifulSoup
import requests
import time

incorrect_list = []
correct_list = []
total_attempts = (len(correct_list) + len(incorrect_list))

rst = ''
rst_msg = "\nThe Score Has Been Reset to 0:\n\tCorrect: 0\n\tIncorrect: 0\n\tTotal Questions Answered: 0\n\tPercentage Correct: 0%\n"

while True:
    # Main Program
    source = requests.get('http://mcatquestionoftheday.com/?task=randompost').text
    soup = BeautifulSoup(source, 'lxml')

    question = soup.find('div', class_='entry').find('p', style="text-align: center;").text
    question2 = soup.find('div', class_= 'entry').find_all('label')

    # Currently only works for one paragraph questions w/o images
    print(question)
    print()
    for i in question2:
        print(i.text)

    answer = soup.find('div', class_ = 'entry').find('strong')
    final_answer = list(answer.text)[-2]

    print('\n\n\n\n') # Removed two newlines to test how it looks
    then = time.time()
    attempt_set = set()
    rst = 'False'

    # Answer must be in letters with options A, B, C, or D. Can also skip with S or reset the score with R
    while True:
        attempt = input('The answer is: ')
        if attempt.upper() == final_answer:
            print('Correct!')
            break
        elif attempt.upper() == 'S':
            print('Skipped')
            attempt_set.add(1)
            attempt_set.add(2)
            break
        elif attempt.upper() == 'R':
            print(rst_msg)
            attempt_set = set() # Meant to reset it to 0
            incorrect_list = [] # Meant to reset it to 0
            correct_list = [] # Meant to reset it to 0
            then = time.time() # Meant to reset the time to 0
            rst = 'True' # Marks it for the next code block
            break
        else:
            attempt_set.add(1)
            print('Incorrect')

    # Uses your answer to determine what to do to the recorded scores
    if len(attempt_set) == 1:
        incorrect_list.append(1)
    elif len(attempt_set) == 2:
        continue
    elif rst == 'True':
        continue
    else:
        correct_list.append(1)
            
    # Answer Y to get another question or N to finish
    while True:
        if rst == 'True':
            answer = 'Y'
        if answer != 'Y':
            answer = str(input('Run again? (Y/N): '))
        if answer in ('Y', 'N', 'y', 'n'):
            break
        print("Invalid input")

    # If the answer is Y it give you a new question
    # If it's something other than Y it ends the session
    if answer.upper() == 'Y':
        continue
    else:
        print("Goodbye")
        now = time.time()
        final_time = round(now - then)
        minutes = final_time // 60
        seconds = final_time % 60
        print('\n\n')
        print("It took: " + str(minutes) + " minutes and " + str(seconds) + " seconds\n")
        break

value = (len(correct_list) / (len(correct_list) + len(incorrect_list)) * 100)
rounded_value = round(value, 2)

print('Correct: ' + str(len(correct_list)))
print('Incorrect: ' + str(len(incorrect_list)))
print('Total Questions Answered: ' + str((len(correct_list) + len(incorrect_list))))
print('Percentage Correct: ' + str(rounded_value) + ' %')

# Looking to add a reset feature [Now Done?] and maybe user profiles soon

# Did this update show up on git? Yes I think it shows up!
# When was this last updated? 05/14/2021