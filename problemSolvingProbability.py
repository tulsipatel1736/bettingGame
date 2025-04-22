from probability import *

def makeBet(blackOdds, redOdds, previousOutcome, state):
    # Check if state is None and initialize it with initial counts for black and red
    if state is None:
        state = {'countBlack': 0, 'countRed': 0}

    # Update the count of black or red based on the previous outcome
    if previousOutcome == 'black':
        state['countBlack'] += 1
    elif previousOutcome == 'red':
        state['countRed'] += 1

    # Calculate the probabilities of drawing black and red cards
    total = state['countBlack'] + state['countRed']
    if total > 0:
        black = state['countBlack'] / total
        red = state['countRed'] / total
    else:
        # If no previous outcomes, assume equal probabilities for black and red
        black = 0.5
        red = 0.5

    # Create a dictionary to represent the probabilities of drawing each card
    cards = {'black': black, 'red': red}

    # Create a payout matrix representing the winnings/losses for each combination of outcomes
    payout = {
        'black': {'black': blackOdds, 'red': -20},
        'red': {'black': -20, 'red': redOdds}
    }

    # Use the 'decide' function from the 'probability' module to determine the bet based on probabilities and payouts
    # The function returns a list of bets, but we return only the first one
    bet = decide(cards, payout)[0]

    return bet, state
