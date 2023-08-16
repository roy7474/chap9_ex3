'''Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary 
to count how many messages have come from each email address, and print the dictionary. '''
#fhand = open('mbox-short.txt') # open the program directly for testing

#create the dictionary
emails_received = dict()
all_emails = dict()

#get the file to be opened
try:
    file_name = input('Enter the name of the file that you would like to open. Include the file format(file_name.format): ')

except:
    print('There was a problem while trying to open the file, please confirm the name of the file and try again!')
    exit()


#open text file
fhand = open(file_name)

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


#For clarity, end of program 1
print('-------------------------- End of the 1st part of the program -------------')


'''Add code to the above program to figure out who has the most messages in the file. After all 
the data has been read and the dictionary has been created, look through the dictionary using a 
maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print 
    how many messages the person has.”'''

cmax_value = 0
clargest = None
for key, value in emails_received.items():
    if value > cmax_value:
        cmax_value = value
        clargest = key
print(f'The amount of emails received where {cmax_value} by {clargest}')
print('-------------------------- End of the 2nd part of the program -------------')


# Extra program
# This part of the program scans the entire text file for all of the emails
fhand = open('mbox-short.txt')
read_file = fhand.read().split() #open the file and make python read and split it into words
for word in read_file:
    
    #add any word with @ to the dictionary all_emails
    if '@' in word:
         all_emails[word] = all_emails.get(word, 0) + 1
print('This part of the program prints all of the emails found in the text file:')

# Print the counted results 
for word, count in all_emails.items():
    #Format for printing, key(word): value(count)
    print(f'{word}: {count}') 
print('-------------------------- End of the program -------------')