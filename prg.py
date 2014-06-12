from cloudmesh_task.tasks import cm_ssh
from cloudmesh_task.parallel import Parallel, Sequential
from cloudmesh.util.stopwatch import StopWatch

hosts = ["india.futuregrid.org",
         "sierra.futuregrid.org",
         "alamo.futuregrid.org",
         "hotel.futuregrid.org"]

result = {}

watch = StopWatch()


watch.start("sequential")
#for host in hosts:
#    print host
#    result[host] = cm_ssh(username="gvonlasz",
#                          host=host,
#                          command="qstat")
result = Sequential(hosts, cm_ssh, username="gvonlasz", command="qstat")
watch.stop("sequential")

for host in hosts:
    print result[host]

print "asynchronous calls"
result = {}

watch.start("parallel")
#for host in hosts:
#    print host
#    result[host] = cm_ssh.delay(username="gvonlasz",
#                                host=host,
#                                command="qstat")

result = Parallel(hosts, cm_ssh, username="gvonlasz", command="qstat")
print "gather results"

for host in hosts:
    id = result[host].get(propagate=False)
watch.stop("parallel")


for host in hosts:
    print result[host]



for timer in ["parallel", "sequential"]:
    print timer, watch.get(timer), "s"


