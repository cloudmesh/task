from cloudmesh_task.tasks import add
from cloudmesh_task.tasks import cm_ssh

print add(4,4)


hosts = ["india.futuregrid.org",
         "sierra.futuregrid.org",
         "alamo.futuregrid.org",
         "hotel.futuregrid.org"]

result = {}
"""
for host in hosts:
    print host
    result[host] = cm_ssh("gvonlasz", host, "qstat")

for host in hosts:
    print result[host]
"""
print "asynchronous calls"
result = {}
for host in hosts:
    print host
    result[host] = cm_ssh.delay("gvonlasz", host, "qstat")



print "gather results"

for host in hosts:
    print host
    print result[host].get(propagate=False)
