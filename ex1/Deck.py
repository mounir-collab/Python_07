from ex0.Card import Card
import random



class Deck:

    def __init__(self):
        self.cards : list[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card , Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.lower() == card_name.lower() :
                self.cards.remove(card_name)
                return True
        return False


    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        pass

