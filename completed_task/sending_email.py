__author__ = 'raghvendra.singh'

import smtplib

server = smtplib.SMTP('csom2.calsoft.org', 587)

server.login('raghvendra.singh', 'Calsoft@567')

msg = "" \
      "Hello," \
      "How are you?"

server.sendmail('raghvendra.singh@calsoftinc.com', 'raghvendra.singh@calsoftinc.com', msg)
