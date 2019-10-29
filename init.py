from threading import Thread
import nivel as niv
# import tempAWS as temp

class Th(Thread):
    def __init__(self, id_num, func):
        Thread.__init__(self)
        self.id_num = id_num
        self.func = func
        
    def run(self):
        print(self.id_num)
        func()

while(1):
    nivel = niv.loop_nivel()
    # temp_c, temp_f = temp.loop_temp()
    # print("A temperatura em Celcius é: ", temp_c)
    # print("A temperatura em Farenheit é: ", temp_f)
    print("O nivel está ", nivel)
    
    nivel = Th(1, niv.loop_nivel)
    temp = Th(2, temp.loop_temp)
    
    nivel.start()
