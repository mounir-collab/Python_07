from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name , cost , rarity)
        self.effect_type = effect_type


    def play(self, game_state: dict) -> dict:
        if ( self.is_playable(game_state['mana'])) is True:
            game_state["mana"] -= self.cost
            return { "card_played" : self.name , 
                "mana_used" : self.cost ,
                "effect" : self.effect_type
                }
        return {"error": "Not enough mana"}

    def resolve_effect(self, targets: list) -> dict:
        results = []

        for target in targets:
            if self.effect_type == "damage":
                results.append({
                    "target": target,
                    "damage": 3
                })

            elif self.effect_type == "heal":
                results.append({
                    "target": target,
                    "healed": 3
                })

            elif self.effect_type == "buff":
                results.append({
                    "target": target,
                    "buff": "increased stats"
                })

            elif self.effect_type == "debuff":
                results.append({
                    "target": target,
                    "debuff": "reduced stats"
                })

            else:
                results.append({
                    "target": target,
                    "effect": "unknown"
                })

        return {
            "effect_type": self.effect_type,
            "results": results
        }     



