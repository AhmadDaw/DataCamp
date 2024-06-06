class Customer:

    def set_name(self,new_name):
        self.name=new_name

    def identify(self):
        print("I'm custmer "+self.name)
    


c=Customer()
c.set_name('Adam')
c.identify()
print(c.name)
