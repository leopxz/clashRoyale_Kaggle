class Player:
    def __init__(self, tag, deck, crowns, starting_trophies):
        self.tag = tag  # Player's unique identifier
        self.deck = deck  # Deck object
        self.crowns = crowns  # Number of crowns won
        self.starting_trophies = starting_trophies  # Number of trophies before the battle

    def __repr__(self):
        return f"<Player Tag: {self.tag}, Crowns: {self.crowns}, Starting Trophies: {self.starting_trophies}>"
