

start = input('enter your age: ')
end = input('enter your max age: ')
years = int(end) - int(start)
Interval = input('Input desired intervals: ')
Count = input('Enter desired count, limit is 4: ')
if int(Count) >=5 :
	exit()	
loss = 0

for x in range(0, int(Count)):
	factor = int(Interval)+x
	temp = int(Count)-factor
	loss = loss+temp



print(loss)
print(years*int(Count)-loss)



