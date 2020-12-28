from bs4 import BeautifulSoup
import requests
import time
import random


while True:
    # main program
    source = requests.get('http://mcatquestionoftheday.com/?task=randompost').text
    soup = BeautifulSoup(source, 'lxml')

    # print(soup.prettify())

    question = soup.find('div', class_='entry').find('p', style="text-align: center;").text
    question2 = soup.find('div', class_= 'entry').find_all('label')

    print(question)
    print()
    for i in question2:
            print(i.text)

    # question2 = soup.find('div', class_= 'entry')
    # print(question2.prettify())

    answer = soup.find('div', class_ = 'entry').find('strong')
    final_answer = list(answer.text)[-2]

    print('\n\n\n\n\n\n')
    then = time.time()

    while True:
        attempt = input('The answer is: ')
        if attempt == final_answer:
                print('Correct!')
                break
        else:
                print('Incorrect')
            
        
    while True:
        answer = str(input('Run again? (Y/N): '))
        if answer in ('Y', 'N'):
            break
        print("invalid input.")
    if answer == 'Y':
        continue
    else:
        print("Goodbye")
        now = time.time()
        final_time = round(now - then)
        minutes = final_time // 60 
        seconds = final_time % 60
        print('\n\n')
        print("It took: " + str(minutes) + " minutes and " + str(seconds) + " seconds")
        break
