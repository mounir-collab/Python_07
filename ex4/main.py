from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:

    print("\n=== DataDeck Tournament Platform ===")

    Platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...")
    dragon = TournamentCard("Fire Dragon", " dragon_001", 10)
    wizard = TournamentCard("Ice Wizard", " wizard_001", 12)

    Platform.register_card(dragon)
    Platform.register_card(wizard)

    for card in [dragon, wizard]:
        stats = card.get_tournament_stats()

        print(f"\n{stats['name']} (ID: {stats['id']}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {stats['rating']}")
        print(f"- Record: {stats['record']}")

    print("\nCreating tournament match...")

    result = Platform.create_match(dragon.card_id, wizard.card_id)
    print("Match result: ", result)

    print("\nTournament Leaderboard:")

    for idx, card in enumerate(Platform.get_leaderboard(), 1):
        print(
            f"{idx}. {card.name} - "
            f"Rating: {card.rating} ({card.wins }-{ card.loses})"
        )

    print("\nPlatform Report:")
    print(Platform.generate_tournament_report())


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print("Error : ", err)
