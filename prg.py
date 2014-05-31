from cloudmesh_task.tasks import cm_ssh
from cloudmesh.util.stopwatch import StopWatch

hosts = ["india.futuregrid.org",
         "sierra.futuregrid.org",
         "alamo.futuregrid.org",
         "hotel.futuregrid.org"]

result = {}

watch = StopWatch()


watch.start("sequential")
for host in hosts:
    print host
    result[host] = cm_ssh("gvonlasz", host, "qstat")
watch.stop("sequential")

for host in hosts:
    print result[host]

print "asynchronous calls"
result = {}

watch.start("parallel")
for host in hosts:
    print host
    result[host] = cm_ssh.delay("gvonlasz", host, "qstat")

print "gather results"

for host in hosts:
    print host
    print result[host].get(propagate=False)
watch.stop("parallel")

for timer in ["parallel", "sequential"]:
    print timer, watch.get(timer), "s"


