nofproc = input("Enter Number Of processes")
ready_q = {}
for q in range(nofproc):
	pname = raw_input("enter process %d name : " %(q+1))
	parr_time = input("enter process %d arrival time : " %(q+1))
	pburst_time = input("enter process %d burst time : " %(q+1))
	ready_q[parr_time] = pname,pburst_time
print "Ready queue is : \n",ready_q
totaltime = min(ready_q.keys())
waiting = []
for q in range(nofproc):
	running = min(ready_q.keys())
	print "Process ",ready_q.get(running)[0]," started at ",totaltime,"ended at ",totaltime+ready_q.get(running)[1]
	print "waiting time is : ",totaltime-running
	waiting.append(totaltime-running)
	totaltime = totaltime + ready_q.get(running)[1]
	del ready_q[running]
print "Average Waiting Time is : "
sums = 0.0;
for i in range(len(waiting)):
	sums = sums + waiting[i]
print sums/len(waiting)
