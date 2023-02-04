# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lista=list()


for lines in handle:
    if lines.startswith("From:"):
        continue
    if lines.startswith("From"):
        hour = lines.split()
        hour = hour[5]
        hour = hour.split(':')
        hour = hour[0]
        lista.append(hour)
        
dicio = dict()
tmp = list()
for hours in lista:
    dicio[hours] = dicio.get(hours,0) + 1


for k,v in sorted(dicio.items()):
    print(k,v)