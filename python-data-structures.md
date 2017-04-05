#### Assignment 6.0
Find character and subset string
```python
text = "X-DSPAM-Confidence:    0.8475"; numpos = text.find('0')
print float(text[numpos:])
```

#### Assignment 7.1
Reads through file and ouputs text in upper case
```python
fname = raw_input("Enter file name: ")
fh = open(fname)

for letter in fh:
  letter = letter.rstrip()
  print letter.upper()
```
  
#### Assignment 7.2
This is using a file called mbox-short.txt
Read text, find spam confidence, print average
```python
fname = raw_input("Enter file name: "); fh = open(fname)
count = 0; num_total = 0

for line in fh:
  if not line.startswith("X-DSPAM-Confidence:") : continue
  count = count + 1  
  num = float(line[20:])
  num_total = num_total+num
        
print 'Average spam confidence:',num_total / count
```

#### Assignment 8.1
Read in file, split lines, return set of words used in text
```python
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for i in line.split():
        lst.append(i)
lst.sort()
print list(set(lst))
```

#### Assignment 8.2
Open mbox-short.txt, read line by line, take lines that start with 'From' and find emails, then print list of emails & how many emails were found
```python
fname = raw_input("Enter file name: "); if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname); count = 0

for i in fh:
  if i.startswith('From '):
    count = count + 1
    print i.split()[1]
    
print "There were", count, "lines in the file with From as the first word"
```

#### Assignment 9 
Working with dictionaries, read through mbox-short.txt, find greatest number of emails sent from a single person using a dictionary to keep track of senders and number of emails sent. Iterate through dictionary to find greates value
```python
name = raw_input("Enter file:"); if len(name) < 1 : name = "mbox-short.txt"
name = "mbox-short.txt"; handle = open(name); text = handle.read()
words = list(); counts = dict()

for line in handle:
  if not line.startswith("From:") : continue
  line = line.split()
  words.append(line[1])

for word in words:
  counts[word] = counts.get(word, 0) + 1 
  
max_val = None; max_key = None
for key,val in counts.items() :
  if val > max_val:
    max_val = val
    max_key = key   

print max_key, max_val
```

#### Assignment 10
Read in mbox-short.txt, find distribution of messages by the hour
```python
name = raw_input("Enter file:"); if len(name) < 1 : name = "mbox-short.txt"
handle = open(name); counts = dict()

# Count occurrences of each hour
for line in handle:
  if not line.startswith('From '): continue
  words = line.split()
  time = words[5]
  hour = time[:2]
  counts[hour] = counts.get(hour,0) + 1

# Place counts in a list and sort
lst = list()
for key,val in counts.items():
  lst.append((key,val))
lst.sort()

# Print
for key,val in lst:
  print key,val
```
