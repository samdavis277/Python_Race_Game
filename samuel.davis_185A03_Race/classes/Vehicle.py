from abc import ABC, abstractmethod

class Vehicle():
    def __init__(self, model, colour):
        self.__model = model
        self.__colour = colour
        self.__speed = 0.0
        self.__position = 0.0

    def get_model(self) -> str:
        return self.__model
    
    def get_colour(self) -> str:
        return self.__colour
    
    def get_speed(self) -> float:
        return self.__speed
    
    def get_position(self) -> float:
        return self.__position
    
    def set_speed(self, value: float):
        self.__position = value

    def set_position(self, value: float):
        self.__position = value
    
    def move(self):
        self.__position += self.__speed
    
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def get_icon(self) -> str:
        pass

    def get_position_int(self) -> int:
        return int(self.__position)
    
    def __repr__(self) -> str:
        return (f"Model {self.__model}, Colour: {self.__colour}, "
                f"Speed: {self.__speed}, Position: {self.__position}")
    
    def __str__(self) -> str:
        return repr(self)