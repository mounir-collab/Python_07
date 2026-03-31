from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.GameStrategy import GameStrategy
from typing import Dict, List


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        cards_played = []
        mana_used = 0
        damage = 0

        # Play first 2 cards for simplicity
        for card in hand[:2]:
            cards_played.append(card.name)
            mana_used += card.cost

            if isinstance(card, CreatureCard):
                damage += card.attack

            elif isinstance(card, SpellCard):
                # Example: assign numeric damage based on effect_type
                if card.effect_type == "damage":
                    damage += 3
                elif card.effect_type == "burn":
                    damage += 4
                # else: other effects = 0 for now

            elif isinstance(card, ArtifactCard):
                # Aggressive artifacts can add fixed damage
                if card.effect.lower() in ["damage", "attack_boost"]:
                    damage += 2
                # else: ignore artifact effect for direct damage
        if battlefield:
            targets = [card.name for card in battlefield]
        else:
            targets = ["Enemy Player"]

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        # simple: no prioritization for now
        return available_targets
