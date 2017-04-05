#### Assignment 1.0
Print "Hello, World!" to the console.
```python
print "Hello World!"
```

#### Assignment 2.1
Request user's name and say hello!
```python
name = raw_input("Enter your name: ")
print "Hello",name
```

#### Assignment 2.2
Calculate pay based on hours and hourly pay rate
```python
hrs = raw_input("Enter Hours:"); rate = raw_input("Enter hourly rate:")
pay = int(hrs)*float(rate)
print pay
```

#### Assignment 3.1
Calculate pay while considering overtime work
```python
h = float(raw_input("Enter Hours:")); rate = float(raw_input("Enter Rate:"))
if h <= 40:		# Regular work
  t = h*rate
  print t
else: 				# Overtime
  t = 40*rate + (h-40)*1.5*rate
  print t
```

#### Assignment 3.2
Enter numerical score and return grade
```python
score = float(raw_input("Enter Score: "))
try:
  if score >= 0.9:
    print "A"
  elif score >= 0.8:
    print "B"
  elif score >= 0.7:
    print "C"
  elif score >= 0.6:
    print "D"
  else:
    print "F"
except:
  print "Please enter a valid score:"
  quit()
```

#### Assignment 4.0
Define a computepay function that calculates pay & considers overtime
```python
def computepay(h,r):
  if h <= 40:
    return h*r
  return (h-40)*r*1.5 + 40*rate

hrs = float(raw_input("Enter Hours:")); rate = float(raw_input("Enter Rate:"))
pay = computepay(hrs,rate)
print pay
```

#### Assignment 5.0
Request user input (integers) and when the user enters 'done' the largest and smallest numbers will be returned
```python
largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = float(inp)
    except:
       # print "Please enter a number as input or \'done\'"
        print "Invalid input"
        continue
    if smallest is None:
        smallest = num 
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

def done(largest,smallest):
    print "Maximum is", int(largest)  
    print "Minimum is", int(smallest)

done(largest,smallest)
```
