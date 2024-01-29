# ASSIGNMENT - 1
# TEAM - 9
# NAME : HRITIK TUTEJA, KRITAN GOTAME, KRISHNA GUPTA, ARYAN VIJAYKUMAR SHAH
# TOPIC - WORD COUNTER
# DESCRIPTION -  Create a program that takes a text file, counts how many times each word appears in the text file, and saves a report of words from most to least frequent to a text file.


# open and read the file
file = open('sample.txt', 'r')
text = file.read()
# split text into individual words
words = text.split()
# create an empty dictionary
wordcount = {}
# count how many times each word appears in the text
for word in words:
 if word in wordcount:
   wordcount[word] += 1
 else:
   wordcount[word] = 1
# close the file
file.close()
# sort the words by frequency
sortedwords = sorted(wordcount.items(), key=lambda kv: kv[1], reverse=True)
# open a new file to write the report
file = open('sampleReport.txt', 'w')
# write the words and their frequency to the report
for word in sortedwords:
 file.write(word[0] + ': ' + str(word[1]) + '\n')
# close the file
file.close()
# print a success message to let user know that your data has been represented there
print('Report saved to sampleReport.txt')
