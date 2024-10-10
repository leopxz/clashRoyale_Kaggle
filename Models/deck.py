class Deck:
    def __init__(self, cards):
        self.cards = cards  # List of card IDs or names in the deck

    def __repr__(self):
        return f"<Deck Cards: {', '.join(self.cards)}>"
