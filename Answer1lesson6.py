from time import sleep
class TrafficLight:
    __color = 'White'
    def running(self):
        while True:
            print('red')
            sleep(7)
            print('yellow')
            sleep(2)
            print('green')
            sleep(7)
            print('yellow')
            sleep(2)
trafficLight = TrafficLight()
trafficLight.running()
