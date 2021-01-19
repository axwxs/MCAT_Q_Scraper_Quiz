from bs4 import BeautifulSoup
import requests
import time

incorrect_list = []
correct_list = []
total_attempts = (len(correct_list) + len(incorrect_list))

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

    print('\n\n\n\n\n\n')
    then = time.time()
    attempt_set = set()
    # Answer must be in letters with options A, B, C, or D. Can also skip with S.
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
        else:
            attempt_set.add(1)
            print('Incorrect')
                
    if len(attempt_set) == 1:
        incorrect_list.append(1)
    elif len(attempt_set) == 2:
        continue
    else:
        correct_list.append(1)
            
    # Answer Y to get another question or N to finish   
    while True:
        answer = str(input('Run again? (Y/N): '))
        if answer in ('Y', 'N', 'y', 'n'):
            break
        print("Invalid input")
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

# Did this update properly? Yes it did!