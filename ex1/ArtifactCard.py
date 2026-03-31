from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        if (self.is_playable(game_state["mana"])) is True:
            game_state["mana"] -= self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect,
            }
        return {"error": "Not enough mana"}

    def activate_ability(self) -> Dict:
        if self.durability <= 0:
            return {"artifact": self.name, "status": "broken", "effect": None}

        self.durability -= 1

        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_remaining": self.durability,
        }
