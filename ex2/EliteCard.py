from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from enum import Enum
import random


class itt:
    aa = 12
    bb = 33


class CombatType(Enum):
    MELEE = "melee"
    RANGED = "ranged"


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name, attack_power, defense, mana):
        self.name = name
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {"card": self.name, "status": "played", "type": "Elite"}

    def attack(self, target) -> dict:
        damage = self.attack_power
        return {
            "attacker": self.name,
            "target": target,
            "damage": damage,
            "combat_type": random.choice(list(CombatType)).value,
        }

    def defend(self, incoming_damage) -> dict:
        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = incoming_damage - damage_blocked

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": True,
        }

    def get_combat_stats(self) -> dict:

        return {"attack": self.attack_power, "defense": self.defense}

    def cast_spell(self, spell_name: str, targets: list) -> dict:

        mana_cost = 4

        if self.mana < mana_cost:
            return {"error": "Not enough mana"}

        self.mana -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount):
        self.mana += amount

        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self):
        return {"mana": self.mana}
