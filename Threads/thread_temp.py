# import
from threading import Thread
import nivel as niv
import time

nivel_thread = Thread(target = niv.loop_nivel)
nivel_thread.start()
	
print "Fim da Thread"
