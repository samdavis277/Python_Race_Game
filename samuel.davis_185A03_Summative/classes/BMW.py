import classes.Vehicle as v

class BMW(v.Vehicle):
    """Sub class of the Vehicle class

    Args:
        v (class): The parent class
    """
    def __init__(self, model: str, colour: str, is_turbo: bool):
        """
        Initializes a vehicle with the specified model, colour, and turbo configuration.

        Args:
            model (str): The model name of the vehicle.
            colour (str): The colour of the vehicle.
            is_turbo (bool): Indicates whether the vehicle has a turbo configuration (True) or not (False).
    """
        super().__init__(model, colour)
        self.__is_turbo = is_turbo
        
    def __str__(self) -> str:
        """Prints the information of the vehicle

        Returns:
            str: The information of the vehicle
        """
        turbo_status = "Turbo" if self.__is_turbo else "Non-Turbo"
        return f" BMW ({turbo_status}) -> {super().__str__()}"

    def accelerate(self):
        """The acceleration of the BMW
        """
        accel = 0.6 if self.__is_turbo else 0.5
        self.set_speed(self.get_speed() + accel)
        super().accelerate()

    def get_icon(self) -> str:
        """Gets the icon for the BMW

        Returns:
            str: returns the icon for the BMW
        """
        return "L"
    
    def get_position(self) -> float:
        """Gets the position for the BMW

        Returns:
            float: returns the position of the BMW
        """
        return super().get_position()
    
    def get_position_int(self) -> int:
        """The integer position of the BMW

        Returns:
            int: returns the integer position of the BMW
        """
        return int(self.get_position())
    
    def move(self):
        """Adds the speed to the position to get the vehicles new position
        """
        self.set_position(self.get_position() + self.get_speed())