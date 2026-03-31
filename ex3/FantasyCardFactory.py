import random
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Union, Dict


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.creatures = [
            ("Fire Dragon", 6, "legendary", 8, 8),
            ("Goblin Warrior", 2, "common", 2, 2),
        ]

        self.spells = [
            ("Lightning Bolt", 3, "rare", "damage"),
            ("Fireball", 4, "rare", "burn"),
        ]

        self.artifacts = [
            ("Mana Ring", 2, "rare", 5, "mana boost"),
            ("Crystal Staff", 3, "epic", 4, "spell power"),
        ]

    def create_creature(self,
                        name_or_power: Union[str, int, None] = None) -> Card:

        name, cost, rarity, attack, health = random.choice(self.creatures)

        # If user provided a name
        if isinstance(name_or_power, str):
            name = name_or_power

        # If user provided a power value
        elif isinstance(name_or_power, int):
            attack = name_or_power

        return CreatureCard(
            name=name,
            cost=cost,
            rarity=rarity,
            attack=attack,
            health=health,
        )

    def create_spell(self,
                     name_or_power: Union[str, int, None] = None) -> Card:
        name, cost, rarity, effect = random.choice(self.spells)

        if isinstance(name_or_power, str):
            name = name_or_power

        elif isinstance(name_or_power, int):
            cost = name_or_power

        return SpellCard(
            name=name,
            cost=cost,
            rarity=rarity,
            effect_type=effect,
        )

    def create_artifact(self,
                        name_or_power: Union[str, int, None] = None) -> Card:
        name, cost, rarity, durability, effect = random.choice(self.artifacts)

        if isinstance(name_or_power, str):
            name = name_or_power

        elif isinstance(name_or_power, int):
            durability = name_or_power

        return ArtifactCard(
            name=name,
            cost=cost,
            rarity=rarity,
            durability=durability,
            effect=effect,
        )

    def create_themed_deck(self, size: int) -> Dict:

        deck: list[Card] = []

        for _ in range(size):

            card_type = random.choice(["creature", "spell", "artifact"])

            if card_type == "creature":
                deck.append(self.create_creature())

            elif card_type == "spell":
                deck.append(self.create_spell())

            else:
                deck.append(self.create_artifact())

        return {"deck": deck}

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "lightning"],
            "artifacts": ["mana_ring", "staff"],
        }
