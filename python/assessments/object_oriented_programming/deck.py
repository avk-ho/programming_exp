import random

class Deck:
    suits = ["H", "D", "C", "S"]
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    
    def __init__(self):
        self.cards = [value + suit for suit in Deck.suits for value in Deck.values]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        if n > len(self):
            return self.cards

        cards = []
        while n > 0:
            card = self.cards.pop()
            cards.append(card)
            n -= 1
            
        return cards
    
    # H < D < C < S
    def sort_by_suit(self):
        suits = ["H", "D", "C", "S"]
        for suit in reversed(suits):
            idx = 0
            
            while idx < len(self):
                card = self.cards[idx]
                if suit in card:
                    self.cards.pop(idx)
                    self.cards.insert(0, card)
                idx += 1

    def contains(self, card):
        return card in self.cards

    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards[:] # !!!
        return new_deck

    def get_cards(self):
        return self.cards[:] # !!!


# d = Deck()
# d.shuffle()
# print(d.cards)
# d.sort_by_suit()
# print(d.cards)