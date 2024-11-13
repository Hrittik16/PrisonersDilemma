import random

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

    def iterated_prisoners_dilemma_with_random_choice(self, rounds=10):
        print(f"Now we are going to simulate iterated prisoners dilemma for {rounds} rounds where Player A and Player B will randomly choose between cooperate and defect. We are interested in the total accumulated payoffs for both the players.")
        
        total_payoff_a, total_payoff_b = 0, 0
        strategy_a = random.choice(['cooperate', 'defect'])
        strategy_b = random.choice(['cooperate', 'defect'])

        for _ in range(rounds):
            payoff_a, payoff_b = self.play_game(strategy_a, strategy_b)
            total_payoff_a += payoff_a
            total_payoff_b += payoff_b

        print(f"Total payoff for Player A: {total_payoff_a}")
        print(f"Total payoff for Player B: {total_payoff_b}")


if __name__ == '__main__':
    game1 = PrisonersDilemma()
    choice1 = input("Do you want to play a single game of prisoners dilemma: ")
    if choice1.lower() == 'yes':
        strategy_a = input("Enter strategy for Player A (cooperate or defect): ")
        strategy_b = input("Enter strategy for Player B (cooperate or defect): ")
        payoff = game1.play_game(strategy_a, strategy_b)
        print(f"Payoff = {payoff}")
    choice2 = input("Do you want to simulate iterated prisoners dilemma: ")
    if choice2.lower() == 'yes':
        rounds = input("How many rounds do you want to simulate: ")
        if rounds.isnumeric():
            game1.iterated_prisoners_dilemma_with_random_choice(int(rounds))
        else:
            game1.iterated_prisoners_dilemma_with_random_choice()
