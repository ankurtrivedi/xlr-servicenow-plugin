#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys, string, time, traceback
import com.xhaus.jyson.JysonCodec as json
from servicenow.ServiceNowClient import ServiceNowClient

if servicenowServer is None:
    print "No server provided."
    sys.exit(1)

if tableName is None:
    print "No tableName provided."
    sys.exit(1)

if content is None:
    print "No content provided."
    sys.exit(1)

snClient = ServiceNowClient.create_client(servicenowServer, username, password)

print "Sending content %s" % content

try:
    data = snClient.create_record( tableName, content )
    taskId = data["sys_id"]
    Task = data["number"]
    print "Created %s in Service Now." % (taskId)
    print "Created %s in Service Now." % (Task)
    print "\n"
    print snClient.print_record( data )
except Exception, e:
    exc_info = sys.exc_info()
    traceback.print_exception( *exc_info )
    print e
    print "Failed to create record in Service Now"
    sys.exit(1)

