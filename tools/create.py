#!/usr/bin/env python

from lib.console import Console
import sys
import os
import requests

def readfile(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content

def createjob(jobtitle, config):
    headers = {'content-type': 'application/xml'}
    home = sys.argv[1]
    r = requests.post('http://localhost:8123/view/' + home + '/createItem?name=' + jobtitle, data=config, headers=headers)
    return r.status_code == requests.codes.ok

def validatepargument():
    if len(sys.argv) != 3:
        sys.exit(console.err("ERROR: ") + "require View name and Which path?" + console.ok(" example $./create.py ViewName Search_Center/quick/history"))

def validatepath(path):
    if not os.path.isdir(path):
        sys.exit(console.err("ERROR: ") + "Path does not exist. Please check.")

    if not path.startswith(relative_path):
        sys.exit(console.err("ERROR: ") + "Path should begin with " + relative_path)

def trimpath(path):
    jobpath = path
    if jobpath.endswith('/'):
        jobpath = jobpath[:-1]
    return jobpath

def replaceconfigpath(jobpath):
    config = readfile("config-working.xml.txt")
    return config.replace("%JOBPATH%", jobpath)

def createjobtitle(jobpath):
    return "DEV_" + jobpath.replace("/", "_")


if __name__ == "__main__":
    console = Console();

    validatepargument()

    path = sys.argv[2]
    # validatepath(path)

    jobpath = trimpath(path)
    config = replaceconfigpath(jobpath)
    jobtitle = createjobtitle(jobpath)

    if not createjob(jobtitle, config):
        sys.exit(console.err("Job cannot be created."))

    print console.ok("Job has been created.")
