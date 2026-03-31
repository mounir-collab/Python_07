from ex2.EliteCard import EliteCard


def main() -> None:

    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    arcane_warrior = EliteCard("Arcane Warrior", 5, 3, 4)
    print("playing: ", arcane_warrior.play({}))

    print("\nCombat phase:")
    print("Attack result: ", arcane_warrior.attack("Enemy"))
    print("Defense result: ", arcane_warrior.defend(5))

    print("\nMagic phase:")
    print("Spell cast: ",
          arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    mana_result = arcane_warrior.channel_mana(3)
    print("Mana channel:", mana_result)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":

    try:
        main()
    except Exception as err:
        print("Something wrong : ", err)
