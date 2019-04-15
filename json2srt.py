import argparse, base64, getpass, os, re, smtplib, socket, subprocess, StringIO, sys, urllib2
from email.mime.text import MIMEText
from socket import gethostbyname,gaierror

from collections import Counter
import json, time
filename = "1.1 Subs.json"
with open(filename, "r") as infile:
    data = json.load(infile)

outfile = filename.split(".json")

fileout = str(outfile[0] + ".srt")

##lines = data.readlines()
print len(data)


counter = 0
startTime = time.strftime('%H:%M:%S', time.gmtime(0))
text = data[0]["text"]
with open(fileout, "w") as writefile:
    for item in data:
        endTime = time.strftime('%H:%M:%S', time.gmtime(item["displayTimeOffset"]))
        timestamps = str(startTime) + " --> " + str(endTime) + "\n"
        if (counter > 0):
            writefile.write(str(counter) + "\n")
            writefile.write(timestamps)
            writefile.write(text)
            writefile.write("\n\n")
        text = item["text"]
        startTime = time.strftime('%H:%M:%S', time.gmtime(item["displayTimeOffset"]))
        counter = counter + 1
    writefile.write(str(counter) + "\n")
    timestamps = str(startTime) + " --> \n"
    writefile.write(timestamps)
    writefile.write(text)
    writefile.write("\n\n")