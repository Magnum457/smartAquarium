# threads dos sensores
import thread_temp as temp
import thread_nivel as nivel


temp.temp_thread.start()
nivel.nivel_thread.start()