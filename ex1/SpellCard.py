from ex0.Card import Card
from enum import Enum
from typing import Dict, List


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        if (self.is_playable(game_state["mana"])) is True:
            game_state["mana"] -= self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type,
            }
        return {"error": "Not enough mana"}

    def resolve_effect(self, targets: List) -> Dict:
        results = []

        for target in targets:
            if self.effect_type == EffectType.DAMAGE:
                results.append({"target": target, "damage": 3})

            elif self.effect_type == EffectType.HEAL:
                results.append({"target": target, "healed": 3})

            elif self.effect_type == EffectType.BUFF:
                results.append({"target": target, "buff": "increased stats"})

            elif self.effect_type == EffectType.DEBUFF:
                results.append({"target": target, "debuff": "reduced stats"})

            else:
                results.append({"target": target, "effect": "unknown"})

        return {"effect_type": self.effect_type, "results": results}
