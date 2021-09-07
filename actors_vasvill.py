from actor import Actor


class VV_1(Actor):
    def run(self):
        while not self.is_out():
            if self.can_move('forward'): self.move('forward')
            else: self.move('left')   

VV_ACTORS = ( VV_1 )