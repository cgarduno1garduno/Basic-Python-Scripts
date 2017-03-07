################################################################################
## Cristopher Garduno Luna
##
## Some basic python for Coursera: Python for Everybody by U. of Michigan
################################################################################
# Contents:
# Assignment 1.0 - Hello, world!
# Assignment 2.1 - Print user name
# Assignment 2.2 - Calculate pay
# Assignment 3.1 - Calculate pay, consider overtime
# Assignment 3.2 - Return grade
# Assignment 4.0 - Calculate pay function
# Assignment 5.0 - Return max,min values for user input of ints
################################################################################


# Assignment 1.0
# Hello, world!
print "Hello, world!"

# Assignment 2.1
# Say hello to user
name = raw_input("Enter your name: ")
print "Hello",name

# Assignment 2.2
# Calculate pay based on hours and hourly pay rate
hrs = raw_input("Enter Hours:"); rate = raw_input("Enter hourly rate:")
pay = int(hrs)*float(rate)
print pay

# Assignment 3.1
# Calculate pay while considering overtime work
h = float(raw_input("Enter Hours:")); rate = float(raw_input("Enter Rate:"))
if h <= 40:		# Regular work
  t = h*rate
  print t
else: 				# Overtime
  t = 40*rate + (h-40)*1.5*rate
  print t

# Assignment 3.2
# Enter numerical score and return grade
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

# Assignment 4.0
# Define a computepay function that calculates pay & considers overtime
def computepay(h,r):
  if h <= 40:
    return h*r
  return (h-40)*r*1.5 + 40*rate

hrs = float(raw_input("Enter Hours:")); rate = float(raw_input("Enter Rate:"))
pay = computepay(hrs,rate)
print pay

# Assignment 5.0
# Request user input (integers) and when the user enters 'done'
# 	the largest and smallest numbers will be returned
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
