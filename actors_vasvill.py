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

class VVA_3(Actor):
    def run(self):
        while not self.is_out():
            if self.can_move("left"):
                self.move("left")
            elif self.can_move("forward"):
                self.move("forward")
            else:
                self.move("backward")

class VVA_4(Actor):
    def run(self):
        while not self.is_out():
            if self.can_move("left"):
                self.move("left")
            elif self.can_move("forward"):
                self.move("forward")
            else:
                while self.can_move("backward"):
                    self.move("backward")