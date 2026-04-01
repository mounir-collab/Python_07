from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:

    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.Legendary.value, 7, 5)
    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable : {fire_dragon.is_playable(6)}")
    print("Play result: ", fire_dragon.play({"mana": 6}))

    print("\nFire Dragon attacks Goblin Warrior:")
    target = CreatureCard("Goblin Warrior" , 4 , Rarity.Common.value , 2 , 5)
    print(f"Attack result: {fire_dragon.attack_target(target)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable : {fire_dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("some thing wrong :", e)
