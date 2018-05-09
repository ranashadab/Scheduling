from operator import itemgetter
nofproc = input("Enter Number Of processes : ")
quantum = 5
inputtime = 3
inputwait = 4
inproc = input("Input for even or odd processes ? (0 for even, 1 otherwise) : ")
ready_q = []
for q in range(nofproc):
	pname = raw_input("enter process %d name : " %(q+1))
	parr_time = input("enter process %d arrival time : " %(q+1))
	pburst_time = input("enter process %d burst time : " %(q+1))
	ready_q.append([pname,pburst_time,parr_time,pburst_time,q,0])
print "Processes will wait for input after every 3 time units of execution and wait for input for 5 time units !"
print "Ready queue is : \n",ready_q
ready_q.sort(key=itemgetter(2))
print "Ready queue is : \n",ready_q
totaltime = ready_q[0][2]
waiting = []
aux_q=[]
input_arri = []
next = 0
done = 0
while ( (len(ready_q) > 0) | (len(aux_q) > 0) ):
	print ready_q
	print aux_q 
	print "length : ",len(input_arri)
	if len(input_arri) > 0 :
			print "totaltime : ",totaltime,"check : ",input_arri[next] + inputwait
			if ((len(aux_q) > 0 ) & (totaltime >= input_arri[next] + inputwait)):
				print "Process ",aux_q[0][0]," started at ",totaltime,"from aux and moved to ready at ",totaltime + aux_q[0][5]
				totaltime = totaltime + aux_q[0][5]
				aux_q[0][5] = 0
				templist = aux_q[0]
				del aux_q[0]
				ready_q.append(templist)
				del templist
				del input_arri[next]
				#next=next+1
				done = 1
	if ( (done!=1) & (len(ready_q) > 0) ):
		if ready_q[0][3] > quantum:
			if ready_q[0][2] > totaltime:
				totaltime = ready_q[0][2]
			if ((inproc == 0) & (ready_q[0][4]%2 == 0)) | ((inproc == 1) & (ready_q[0][4]%2 != 0)):
				print "Process ",ready_q[0][0]," started at ",totaltime,"moved to i/o at ",totaltime + inputtime
				ready_q[0][3] = ready_q[0][3]-inputtime
				ready_q[0][5] = quantum-inputtime
				templist = ready_q[0]
				del ready_q[0]
				aux_q.append(templist)
				del templist
				totaltime = totaltime + inputtime
				input_arri.append(totaltime)
			else:
				print "Process ",ready_q[0][0]," started at ",totaltime,"completed quantum at ",totaltime + quantum
				ready_q[0][3] = ready_q[0][3]-quantum
				templist = ready_q[0]
				del ready_q[0]
				ready_q.append(templist)
				del templist
				totaltime = totaltime + quantum
		elif ready_q[0][3] == quantum:
			if ready_q[0][2] > totaltime:
				totaltime = ready_q[0][2]
			print "Process ",ready_q[0][0]," started at ",totaltime,"completed quantum and finished at ",totaltime+quantum
			#ready_q[0][3] = ready_q[0][3]-5
			totaltime = totaltime + 5
			print "Waiting time is : ",totaltime - ready_q[0][2] - ready_q[0][1]
			waiting.append(totaltime - ready_q[0][2] - ready_q[0][1])
			del ready_q[0]
		
		elif ready_q[0][3] < quantum:
			if ready_q[0][2] > totaltime:
				totaltime = ready_q[0][2]
			print "Process ",ready_q[0][0]," started at ",totaltime,"finished before completing quantum at ",totaltime+ready_q[0][3]
			#ready_q[0][3] = ready_q[0][3]-5
			totaltime = totaltime + ready_q[0][3]
			print "Waiting time is : ",totaltime - ready_q[0][2] - ready_q[0][1]
			waiting.append(totaltime - ready_q[0][2] - ready_q[0][1])
			del ready_q[0]
	done=0
print "Average Waiting Time is : "
sums = 0.0
for i in range(len(waiting)):
	sums = sums + waiting[i]
print sums/len(waiting)
