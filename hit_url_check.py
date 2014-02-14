#!/usr/bin/python

import sys
import urllib

from email.mime.text import MIMEText
from subprocess import Popen, PIPE

FROM_EMAIL = "hiredintech@gmail.com"
TO_EMAIL = "hiredintech@gmail.com"

err_cnt = 0

urls_file = open("hit_urls.txt", "r")
for line in urls_file:
  url = line.strip()
  if len(url) == 0:
    continue
  code = urllib.urlopen(url).getcode()
  print '%d --- %s' % (code, url)
  if code != 200:
    print >> sys.stderr, "Received code %d from url %s" % (code, url)
    err_cnt += 1
urls_file.close

if err_cnt == 0:
  print "Finished with no errors"
else:
  print "Found %d errors. Sending an email" % err_cnt
  msg = MIMEText("There were %d problematic URLs" % err_cnt)
  msg["From"] = FROM_EMAIL
  msg["To"] = TO_EMAIL
  msg["Subject"] = "Problemnatic URLs found in HiredInTech"
  p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
  p.communicate(msg.as_string())
