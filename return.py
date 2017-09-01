def range1(start,stop, step=1):
	l=[]
	while start<stop:
		l.append(start)
		start=start+step
	return l


res = range1(1,1300000000)
for i in res:
	print i




