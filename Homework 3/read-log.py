import sys
import lcm

from exlcm import message_t

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)

log = lcm.EventLog(sys.argv[1], "r")

for event in log:
    if event.channel == "message":
        msg = message_t.decode(event.data)

        #print("Message:")
    	#print("   time   = %s" % str(msg.time))
    	#print("   latitude    = %s" % str(msg.latitude))
    	#print("   latitude direction   = %s" % str(msg.latitude_direc))
    	#print("   longtitude = %s" % str(msg.longtitude))
    	#print("   longtitude_direction = %s" % str(msg.longtitude_direc))
    	#print("   altitude =  %s" % str(msg.altitude))
    	#print("   altitude_unit  = '%s" % str(msg.altitude_unit))
	print("   utm_x  = %s" % str(msg.utm_x))  
	print("   utm_y  = %s" % str(msg.utm_y))
