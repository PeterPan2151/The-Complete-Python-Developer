class Player:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('You are running')

player1 = Player('Peter')
player1.run()
