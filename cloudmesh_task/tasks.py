from __future__ import absolute_import

from cloudmesh_task.celery import app
from sh import ssh 

@app.task
def cm_ssh(username, host, command):
    #result = ssh("{0}@{1}".format(username, host), command)
    result = "{0}@{1}:{2}".format(username, host, command)
    return result


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
