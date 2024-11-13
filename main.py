class PrisonersDilemma:
    def __init__(self):
        self.payoff_matrix = {
            ('cooperate', 'cooperate'): (-2, -2),
            ('defect', 'cooperate'): (0, -10),
            ('cooperate', 'defect'): (-10, 0),
            ('defect', 'defect'): (-5, -5)
        }
    
    def play_game(self, strategy_a, strategy_b):
        payoff = self.payoff_matrix[(strategy_a, strategy_b)]
        return payoff

if __name__ == '__main__':
    game1 = PrisonersDilemma()
    strategy_a = input("Enter strategy for Player A (cooperate or defect): ")
    strategy_b = input("Enter strategy for Player B (cooperate or defect): ")
    payoff = game1.play_game(strategy_a, strategy_b)
    print(f"Payoff = {payoff}")
