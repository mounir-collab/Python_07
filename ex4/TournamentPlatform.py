from ex4.TournamentCard import TournamentCard
from typing import Dict, List


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.total_match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.update({card.card_id: card})
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)

        result = card1.attack(card2)

        winner = result["winner"]
        loser = result["loser"]

        winner.update_wins(1)
        loser.update_losses(1)
        self.total_match_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> List:
        def rating_key(card: TournamentCard) -> int:
            return card.rating

        leaderboard = list(self.cards.values())
        leaderboard.sort(key=rating_key, reverse=True)
        return leaderboard

    def generate_tournament_report(self) -> Dict:

        if not self.cards:
            avg_rat = 0
        else:
            list_rat = [card.rating for card in self.cards.values()]
            avg_rat = round(sum(list_rat) / len(self.cards), 1)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.total_match_played,
            "avg_rating": avg_rat,
            "platform_status": "active",
        }
