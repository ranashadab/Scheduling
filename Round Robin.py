from operator import itemgetter
nofproc = input("Enter Number Of processes")
ready_q = []
for q in range(nofproc):
	pname = raw_input("enter process %d name : " %(q+1))
	parr_time = input("enter process %d arrival time : " %(q+1))
	pburst_time = input("enter process %d burst time : " %(q+1))
	ready_q.append([pname,pburst_time,parr_time,pburst_time])
print "Ready queue is : \n",ready_q
ready_q.sort(key=itemgetter(2))
print "Ready queue is : \n",ready_q
totaltime = ready_q[0][2]
waiting = []
while len(ready_q) > 0:
	running = ready_q[0][2]
	if ready_q[0][3] > 5:
		if ready_q[0][2] > totaltime:
			totaltime = ready_q[0][2]
		print "Process ",ready_q[0][0]," started at ",totaltime,"completed quantum at ",totaltime + 5
		ready_q[0][3] = ready_q[0][3]-5
		templist = ready_q[0]
		del ready_q[0]
		ready_q.append(templist)
		del templist
		totaltime = totaltime + 5
	elif ready_q[0][3] == 5:
		if ready_q[0][2] > totaltime:
			totaltime = ready_q[0][2]
		print "Process ",ready_q[0][0]," started at ",totaltime,"completed quantum and finished at ",totaltime+5
		#ready_q[0][3] = ready_q[0][3]-5
		totaltime = totaltime + 5
		print "Waiting time is : ",totaltime - ready_q[0][2] - ready_q[0][1]
		waiting.append(totaltime - ready_q[0][2] - ready_q[0][1])
		del ready_q[0]
		
	elif ready_q[0][3] < 5:
		if ready_q[0][2] > totaltime:
			totaltime = ready_q[0][2]
		print "Process ",ready_q[0][0]," started at ",totaltime,"finished before completing quantum at ",totaltime+ready_q[0][3]
		#ready_q[0][3] = ready_q[0][3]-5
		totaltime = totaltime + ready_q[0][3]
		print "Waiting time is : ",totaltime - ready_q[0][2] - ready_q[0][1]
		waiting.append(totaltime - ready_q[0][2] - ready_q[0][1])
		del ready_q[0]
print "Average Waiting Time is : "
sums = 0.0
for i in range(len(waiting)):
	sums = sums + waiting[i]
print sums/len(waiting)
