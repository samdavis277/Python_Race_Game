import classes.Mercedes as m
import classes.Bentley as b
import classes.BMW as l
import classes.Racetrack as r

def main ():
    """The program to check if the right file is entered and then loops and prints the racetrack
    until a winner is found.
    """
    filename = input("Enter the filename for vehicle data: ")
    while True:
        try:
            with open(filename, 'r') as file:
                data = file.readlines()
                break
        except FileNotFoundError:
            print("File not found. Please try again.")
            filename = input("Enter the filename for vehicle data: ")

    race_vehicles = []
    for line in data:
        attributes = line.strip().split(",")
        if attributes[0] == "Mercedes":
            race_vehicles.append(m.Mercedes(attributes[1], attributes[2]))
        elif attributes[0] == "BMW":
            race_vehicles.append(l.BMW(attributes[1], attributes[2], attributes[3].strip() == "True"))
        elif attributes[0] == "Bentley":
            race_vehicles.append(b.Bentley(attributes[1], attributes[2], attributes[3] == "True"))
    
    racetrack = r.Racetrack(race_vehicles)
    winner_declared = False
    while not winner_declared:

        print(racetrack)
        winning_vehicle = None
        max_position = -1
        for vehicle in race_vehicles:
            vehicle.accelerate()
            vehicle.move()

            if vehicle.get_position() > max_position:
                max_position = vehicle.get_position()
                winning_vehicle = vehicle

        if max_position >= racetrack.get_length() and not winner_declared:
            winner_declared = True
            
        racetrack.current_round += 1
    print(racetrack)
    print(racetrack.champion(winning_vehicle))
main()