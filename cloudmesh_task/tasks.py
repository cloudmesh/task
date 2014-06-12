from __future__ import absolute_import

from cloudmesh_task.celery import app
from sh import ssh 

@app.task
def cm_ssh(host, username, command):
    print "{0}@{1}:{2}".format(username, host, command)
    result = ssh("{0}@{1}".format(username, host), command)
    #result = "{0}@{1}:{2}".format(username, host, command)
    return str(result)

