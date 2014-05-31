from cloudmesh_task.tasks import add
from cloudmesh_task.tasks import cm_ssh

print add(4,4)

print cm_ssh("gvonlasz", "india.futuregrid.org", "qstat")
print cm_ssh("gvonlasz", "sierra.futuregrid.org", "qstat")
print cm_ssh("gvonlasz", "alamo.futuregrid.org", "qstat")
print cm_ssh("gvonlasz", "hotel.futuregrid.org", "qstat")
