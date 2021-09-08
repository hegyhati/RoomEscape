from actor import Actor


class VVA_1(Actor):
    def run(self):
        while not self.is_out():
            if self.can_move("forward"):
                self.move("forward")
            else:
                self.move("left")

class VVA_2(Actor):
    def run(self):
        while not self.is_out():
            if self.can_move("left"):
                self.move("left")
            else:
                self.move("forward")