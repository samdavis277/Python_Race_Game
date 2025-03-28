import classes.Vehicle as v

class Mercedes(v.Vehicle):
    """Sub class of the Vehicle class

    Args:
        v (class): The parent class
    """
    def __init__(self, model: str, colour: str):
        """
        Initializes a vehicle with the specified model and colour.

        Args:
            model (str): The model name of the vehicle.
            colour (str): The colour of the vehicle.
        """
        super().__init__(model, colour)

    def __str__(self) -> str:
        """Prints the information of the vehicle

        Returns:
            str: The information of the vehicle
        """
        return f"Mercedes -> {super().__str__()}"

    def accelerate(self):
        """The acceleration of the Mercedes
        """
        self.set_speed(self.get_speed() + 0.75)
        super().accelerate()

    def get_icon(self) -> str:
        """Gets the icon for the Mercedes

        Returns:
            str: returns the icon for the Mercedes
        """
        return "M"
    
    def get_position(self) -> float:
        """Gets the position of the vehicle

        Returns:
            float: returns the position of the vehicle
        """
        return super().get_position()
    
    def get_position_int(self) -> int:
        """Gets the integer position of the vehicle

        Returns:
            int: returns the integer position of the vehicle
        """
        return int(self.get_position())
    
    def move(self):
        """Adds the speed to the position to get the vehicles new position
        """
        self.set_position(self.get_position() + self.get_speed())