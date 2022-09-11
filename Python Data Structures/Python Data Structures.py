#!/usr/bin/env python
# coding: utf-8

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

# In[7]:


text = "X-DSPAM-Confidence:    0.8475";
digit0 = text.find('0')
digit5 = text.find('5')
number = text[digit0 : digit5+1]
numberfloat = float(number)
print(numberfloat)


# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# In[ ]:


# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh.readlines():
    print(line.upper().strip())


# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# In[8]:


fname = input("Enter file name: ")
fh = open(fname)
n = 0 # for amount of lines
n1 = 0 #for summ
xDSPAM = 0
nfloat = float(n)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    n = n + 1
    xDSPAM = line[line.find('0') : ]
    xDSPAMfl = float(xDSPAM)
    n1 = n1 + xDSPAMfl
median = n1 / n
print("Average spam confidence:", median)


# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt
# 

# In[ ]:


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for i in line.split():
        if not i in lst:
            lst.append(i)
lst.sort()
print(lst)


# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
# 
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# In[ ]:


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for i in fh:
    i = i.rstrip()
    if i.startswith('From:') :
        spliti = i.split()
        print(spliti[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")


# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# In[ ]:


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    if not line.startswith("From "):continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) +1

bigcount = None
bigword = None
for k,v in count.items():
    if bigcount == None or v > bigcount:
        bigword = k
        bigcount = v 
print(bigword, bigcount)


# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# In[ ]:


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
di=dict()
for line in handle:
    if line.startswith("From "):
    	pos=line.find(":")
    	lst.append(line[pos-2:pos])
for word in lst:
    di[word]=di.get(word,0)+1
newlst=list()
for key,val in di.items():
    newtup=(key,val)
    newlst.append(newtup)
newlst=sorted(newlst)
for key,val in newlst:
    print(key,val)

