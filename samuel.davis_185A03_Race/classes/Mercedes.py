import classes.Vehicle as v

class Mercedes(v.Vehicle):
    
    # def __init__(self, model, colour):
    #     super().__init__(model, colour)

    def accelerate(self):
        self.set_speed(self.get_speed() + 0.75)

    def get_icon(self) -> str:
        return "M"
    
    def __str__(self) -> str:
        