class Road:
    def __init__(self,lenght,width):
        self._lenght = lenght
        self._width = width
    def run(self, weith=25,x=5):
        print(f"Масса асфальта - {(self._lenght*self._width*weith*x)/1000} т")
a = Road(5000,20)
a.run()
