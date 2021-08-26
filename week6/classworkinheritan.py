class All:
    def say_hi(self):
        print('Hi people')

class A(All):
    def method_A(self):
        print('Method is A')
class B(All):
    def method_B(self):
        All.say_hi()
        print('Method is B')
class C(A,B):
    def method_C(self):
        print('Method id C')
c = C()
c.say_hi()



    
  
class Wheels_Mixin:
    def say_wheels(self,wheels):
        self.wheels = wheels
class Radio(Wheels_Mixin):
    def play_music(self,music):
        print(f'You listen this {music}')
class Engine(Radio,Wheels_Mixin):
    def say_engine(self,engine,volume):
        print(f'You have act {engine} with {volume}')

class Oil(Engine,Radio,Wheels_Mixin):
    def __init__(self,oil):
        self.oil = oil
class Car(Oil,Engine,Radio,Wheels_Mixin):
    def __init__(self,oil,engine,volume,music,name,wheels):
        self.name = name 
        self.wheels = wheels
        
        
        





class Boat(Oil,Engine,Radio):
     def __init__(self,oil,engine,volume,music,type):
      
        self.music = music
        self.type = type
    


class Ship(Oil,Engine,Radio):
    def __init__(self,oil,engine,volume,music,type):
      
        self.music = music
        self.type = type


class Bike(Oil,Engine,Radio,Wheels_Mixin):
    def __init__(self,oil,engine,volume,music,type):
      
        self.music = music
        self.type = type
buggati = Car('Benzin','V8','6')
buggati.play_music()