'''Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary 
to count how many messages have come from each email address, and print the dictionary.
Enter file name: mbox-short.txt'''

emails = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words=line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in emails:
            emails[words[1]] = 1

        else:
            emails[words[1]] +=1
print(emails)