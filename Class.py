class Car(object):

  def __init__(self,model,color,company,speed_limit):
    self.color=color
    self.company=company
    self.model=model
    self.speed_limit=speed_limit

  def start(self):
    print("Started")


  def stop (self):
    print("Stopped")

  def accelerate(self):
    print("Accelerated")

 # def change_gear(self,gear_type):
 #   print("Gear Changed")

audi = Car("A6","Red","Audi","80")
print(audi.start())
print(audi.stop())
print(audi.accelerate())
#print(audi.change_gear())