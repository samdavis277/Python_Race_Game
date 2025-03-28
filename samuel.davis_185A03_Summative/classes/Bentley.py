import classes.Vehicle as v

class Bentley(v.Vehicle):
    """Sub class of the Vehicle class

    Args:
        v (class): The parent class
    """
    def __init__(self, model: str, colour: str, is_two_motor: bool):
        """
        Initializes a vehicle with the specified model, colour, and motor configuration.

        Args:
            model (str): The model name of the vehicle.
            colour (str): The colour of the vehicle.
            is_two_motor (bool): Indicates whether the vehicle has a two-motor configuration (True) or not (False).
        """
        super().__init__(model, colour)
        self.__is_two_motor = is_two_motor

    def __str__(self) -> str:
        """Prints the information of the vehicle

        Returns:
            str: The information of the vehicle
        """
        motor_status = "Two Motor" if self.__is_two_motor else "Single Motor"
        return f"Bentley ({motor_status}) -> {super().__str__()}"
    
    def accelerate(self):
        """The acceleration of the Bentley
        """
        accel = 0.8 if self.__is_two_motor else 0.6
        self.set_speed(self.get_speed() + accel)
        super().accelerate()

    def get_icon(self) -> str:
        """Retrieves the icon of the vehicle

        Returns:
            str: returns the icon for the vehicle as a string
        """
        return "B"
    
    def get_position(self) -> float:
        """Gets the position of the vehicle

        Returns:
            float: The position of the vehicle
        """
        return super().get_position()
    
    def get_position_int(self) -> int:
        """Gets the integer position of the vehicle

        Returns:
            int: Returns the integer value of the position
        """
        return int(self.get_position())
    
    def move(self):
        """Adds the speed to the position to get the vehicles new position
        """
        self.set_position(self.get_position() + self.get_speed())