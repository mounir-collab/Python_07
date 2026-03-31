from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard

if __name__ == "__main__":

    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    artif = ArtifactCard("Mana Crystal", 2, "Legendary", 3, "heal")
    spell = SpellCard("Lightning Bolt", 3, "Legendary", "damage")

    deck_manager = Deck()
    deck_manager.add_card(fire_dragon)
    deck_manager.add_card(artif)
    deck_manager.add_card(spell)

    print("Deck stats: ", deck_manager.get_deck_stats())

    # Simulated game state
    game_state = {"mana": 10}

    print("\nDrawing and playing cards:")

    deck_manager.shuffle()

    while True:
        try:
            card = deck_manager.draw_card()

            # Format type name (remove "Card")
            card_type = card.__class__.__name__.replace("Card", "")
            print(f"\nDrew: {card.name} ({card_type})")
            print("Play result:", card.play(game_state))

        except Exception:
            break

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")
