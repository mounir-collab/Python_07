from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict
import random
from enum import Enum


class Costs(Enum):
    low_cost = 3
    medium_cost = 5
    high_cost = 7


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name, card_id: str, power: int):
        super().__init__(
            name, random.choice(list(Costs)).value,
            random.choice(list(Rarity)).value
        )
        self.card_id = card_id
        self.power = power

        self.wins = 0
        self.loses = 0
        self.rating = 1200

    # concretisation of methods in Card Interface
    def play(self, game_state: Dict) -> Dict:
        return {"card": self.name, "effect": "played", "state": game_state}

    # concretisation of methods in Combatable Interface
    def attack(self, target) -> Dict:
        my_score = self.power + random.randint(0, 10)
        target_score = target.power + random.randint(0, 10)

        if my_score >= target_score:
            return {"winner": self, "loser": target}
        else:
            return {"winner": target, "loser": self}

    def defend(self, incoming_damage: int) -> Dict:
        self.power -= incoming_damage
        return {"defender:": self.name, "incoming_damage": incoming_damage}

    def get_combat_stats(self) -> Dict:
        return {"power": self.power, "wins": self.wins, "losses": self.losses}

    # concretisation of methods in Rankable Interface
    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += wins * 10

    def update_losses(self, losses: int) -> None:
        self.loses += losses
        self.rating -= losses * 10

    def get_rank_info(self) -> Dict:
        return {"rating": self.rating,
                "wins": self.wins,
                "losses": self.losses}

    # this is a regular method
    def get_tournament_stats(self) -> Dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.loses}",
        }
