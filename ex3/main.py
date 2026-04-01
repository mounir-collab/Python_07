from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():

    print("\n=== DataDeck Game Engine ===")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()

    print("\nConfiguring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())

    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")

    result = engine.simulate_turn()
    list_cards = []
    for card in result["hand"]:
        list_cards.append(f"{card.name} ({card.cost})")

    print("Hand:", list_cards)

    print("\nTurn execution:")
    print("Strategy:", result["strategy"])
    print("Actions:", result["actions"])

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy "
          "Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error : ", e)
