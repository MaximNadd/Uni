class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C.")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

# Usage
temp = Temperature(25)
print(temp.celsius)  
print(temp.fahrenheit)

temp.celsius = 0
print(temp.fahrenheit)
