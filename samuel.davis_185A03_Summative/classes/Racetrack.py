class Racetrack:
    """A class for building a racetrack for vehicles
    """
    def __init__(self, race_vehicles: list, name: str = "ITAS Motor Speedway", length: int = 20):
        """
        Initializes a race with the given vehicles, name, and length.

        Args:
            race_vehicles (list): A list of vehicles participating in the race.
            name (str, optional): The name of the race or speedway. Defaults to "ITAS Motor Speedway".
            length (int, optional): The length of the race. Defaults to 20
        """
        self.__name = name
        self.__length = length
        self.__current_round = 1
        self.__race_vehicles = race_vehicles

    def __str__(self) -> str:
        """Prints out the race track

        Returns:
            str: The race track with the icons if the vehicle is at that position
        """
        print(f"\n{self.__name}")
        output = f"\nRound [{self.__current_round}]\n"
        vehicle_output = " | ".join(str(i + 1) for i in range(len(self.__race_vehicles)))
        output += f"| {vehicle_output} |\n"
    
        # Iterate through each position on the track
        for position in range(self.__length + 1):
            # Print the left lane marker
            line = "|"
            
            # Check each vehicle's position
            for vehicle in self.__race_vehicles:
                # Get the vehicle's integer position
                vehicle_pos = vehicle.get_position_int()

                if vehicle_pos >= self.__length:
                    vehicle_pos = self.__length
                
                # If the vehicle is at the current position add its icon
                if vehicle_pos == position:
                    line += f" {vehicle.get_icon()} "
                else:
                    # Add spaces if no vehicle is at this position
                    line += "   "
                
                # Add lane separator
                line += "|"
            
            # Add the completed line to the output
            output += line + f"Position: [{position}]\n"
        
        return output

    def get_name(self) -> str:
        """The name for the racetrack

        Returns:
            str: returns the name of the racetrack
        """
        return self.__name
    
    def get_length(self) -> int:
        """Gets the length of the track

        Returns:
            int: returns the length of the track
        """
        return self.__length
    
    @property
    def current_round(self) -> int:
        """The current round of the race

        Returns:
            int: Returns the round of the race
        """
        return self.__current_round
    
    @current_round.setter
    def current_round(self, value):
        """Accesses and changes the current round value

        Args:
            value (int): The current round of the race
        """
        self.__current_round = value
    
    def champion(self, winning_vehicle: object) -> str:
        """The winner of the race

        Args:
            winning_vehicle (object): The vehicle and its attributes that won

        Returns:
            str: A description of the vehicle that won
        """
        return f"Congratulations to {winning_vehicle} for winning the race!"