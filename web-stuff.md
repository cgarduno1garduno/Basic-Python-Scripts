#### Using sockets
```python
# Import modules
import socket as sk

mysock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)  # start socket
mysock.connect(('www.py4inf.com', 80))			    # connect socket to server

mysock.send('GET http://py4inf.com/code/romeo.txt HTTP/1.0\n\n')

# Get data
while True:
	data = mysock.recv(512)
	if (len(data)) < 1:
		break
	print data
mysock.close()
```

#### Using urllib
```python
# This is way nicer than using sockets module
import urllib

# Establish connection
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

# Print data
for line in fhand:
	print line.rstrip()
```
