from bs4 import BeautifulSoup
import requests
import time


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
    
    # Answer must be in capital letters with options A, B, C, or D
    while True:
        attempt = input('The answer is: ')
        if attempt == final_answer:
                print('Correct!')
                break
        else:
                print('Incorrect')
            
    # Answer Y or N to get another question    
    while True:
        answer = str(input('Run again? (Y/N): '))
        if answer in ('Y', 'N'):
            break
        print("Invalid input")
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
