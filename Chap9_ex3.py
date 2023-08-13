'''Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary 
to count how many messages have come from each email address, and print the dictionary.
Enter file name: mbox-short.txt'''

#create the dictionary
emails = dict()

#get the file to be opened
try:
    file_name = input('Enter the name of the file that you would like to open. Include the file format(file_name.format): ')

except:
    print('There was a problem while trying to open the file, please confirm the name of the file and try again!')
    exit()

#open text file
fhand = open(file_name)

for line in fhand:
    # split the lines into words
    words=line.split()

    #find the words that start with From
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in emails:
            emails[words[1]] = 1

        else:
            emails[words[1]] +=1

#unescessary since it is more advanced, but more organized way to print the dict content
for key, value in emails.items():
    print(f"{key}: {value}")