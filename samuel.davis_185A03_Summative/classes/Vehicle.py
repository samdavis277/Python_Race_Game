from abc import abstractmethod
import random

class Vehicle():
    """The parent class for vehicles
    """
    def __init__(self, model: str, colour: str):
        """Initializes a vehicle with the specified model and colour, along with default speed and position.

        Args:
            model (str): The model name of the vehicle.
            colour (str): The colour of the vehicle.
        """
        self.__model = model
        self.__colour = colour
        self.__speed = 0.0
        self.__position = 0.0

    def __repr__(self) -> str:
        """The information of the object

        Returns:
            str: The information of the object
        """
        return (f"Model {self.__model}, Colour: {self.__colour}, "
                f"Speed: {self.__speed:.2f}, Position: {self.__position:.2f}")
    
    def __str__(self) -> str:
        """The information of the vehicle

        Returns:
            str: the information of the vehicle
        """
        return repr(self)

    def get_model(self) -> str:
        """Gets the model of the vehicle

        Returns:
            str: returns the model of the vehicle
        """
        return self.__model
    
    def get_colour(self) -> str:
        """Gets the colour of the vehicle

        Returns:
            str: returns the colour of the vehicle
        """
        return self.__colour
    
    def get_speed(self) -> float:
        """Gets the speed for the vehicle

        Returns:
            float: returns the speed of the vehicle
        """
        return self.__speed
    
    def get_position(self) -> float:
        """Gets the position of the vehicle

        Returns:
            float: returns the position of the vehicle
        """
        return self.__position
    
    def set_speed(self, value: float):
        """Sets the speed of the vehicle

        Args:
            value (float): the speed of the vehicle
        """
        self.__speed = value

    def set_position(self, value: float):
        """Sets the position of the vehicle

        Args:
            value (float): the position of the vehicle
        """
        self.__position = value
    
    def move(self):
        """Adds the speed to the position to get the vehicles new position
        """
        self.__position += self.__speed
    
    # @abstractmethod
    def accelerate(self):
        """The random acceleration of the vehicle
        """
        acceleration_change = [-0.2, -0.1, 0, 0.1, 0.2]
        weight_values = (1, 2, 6, 2, 1)
        variance = random.choices(acceleration_change, weights=weight_values, k=1)[0]
        self.set_speed(self.get_speed() + variance)

    @abstractmethod
    def get_icon(self) -> str:
        """Gets the icon of the vehicle

        Returns:
            str: the icon of the vehicle
        """
        pass

    def get_position_int(self) -> int:
        """Gets the integer position of the vehicle

        Returns:
            int: returns the integer position of the vehicle
        """
        return int(self.__position)