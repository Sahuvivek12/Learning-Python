class MyClass:
    def __init__(self, value) -> None:
        self.value = value

    def info(self):
        return (f"The value of the object is {self.value}")
    
    @property
    def tenx_value(self):
        return (10 * self.value)
    
    @tenx_value.setter
    def tenx_value(self, new_val):
        self.value = new_val




obj = MyClass(10)

print(obj.tenx_value)