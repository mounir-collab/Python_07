from ex0.Card import Card
from typing import Dict, Union


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int ,
        rarity: str ,
        attack: int ,
        health: int ,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict[str, Union[str, int]]:
        if game_state.get("mana"):

            if (self.is_playable(game_state["mana"])) is True:
                return {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": "Creature summoned to battlefield",
                }
        return {"somthing wrong"}

    def attack_target(self, target: Card) -> Dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> Dict:
        info: dict = super().get_card_info()
        info.update({"type": "Creature",
                     "attack": self.attack,
                     "health": self.health})
        return info
