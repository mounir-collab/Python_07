from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:

    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.lower() == card_name.lower():
                self.cards.remove(card_name)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise Exception("Deck is empty")

        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.cards:
            total_cost += card.cost

            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1

        avg_cost = total_cost / total_cards if total_cards > 0 else 0

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1),
        }
