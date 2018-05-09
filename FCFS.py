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
for q in range(nofproc):
	print "Process ",ready_q[0][0]," started at ",totaltime,"ended at ",totaltime+ready_q[0][1]
	print "waiting time is : ",totaltime-ready_q[0][2]
	waiting.append(totaltime-ready_q[0][2])
	totaltime = totaltime + ready_q[0][1]
	del ready_q[0]
print "Average Waiting Time is : "
sums = 0.0;
for i in range(len(waiting)):
	sums = sums + waiting[i]
print sums/len(waiting)
