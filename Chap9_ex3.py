'''Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary 
to count how many messages have come from each email address, and print the dictionary. '''
fhand = open('mbox-short.txt')

#create the dictionary
emails_received = dict()
all_emails = dict()
'''
#get the file to be opened
try:
    file_name = input('Enter the name of the file that you would like to open. Include the file format(file_name.format): ')

except:
    print('There was a problem while trying to open the file, please confirm the name of the file and try again!')
    exit()


#open text file
fhand = open(file_name)
'''

#
for line in fhand:
    word = line.split()
    if len(word) < 2 or word[0] != 'From': 
        continue
    else:
        if word[1] not in emails_received:
            emails_received[word[1]] = 1

        else:
            emails_received[word[1]] +=1


print('This part of the program prints all of the emails received in the text file: ')
#unescessary since it is more advanced, but more organized way to print the dict content
for key, value in emails_received.items():
    print(f"{key}: {value}")
print('-------------------------- End of program 1 -------------')
print(word)
# Extra program
# This part of the program scans the entire text file


fhand = open('mbox-short.txt')
read_file = fhand.read().split()
#print(read_file)
for word in read_file:
    # split the lines into words
    
    if '@' in word:
         all_emails[word] = all_emails.get(word, 0) + 1
print('This part of the program prints all of the emails found in the text file:')


for word, count in all_emails.items():
    print(f'{word}: {count}') 