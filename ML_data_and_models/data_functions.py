import re

def calculate_games_add_tiebreak(score_string):
    """
    Calculates total games won for P1 and P2, adding 1 game for P1 for each tie-breaker set.
    
    Args:
        score_string (str): The tennis score string for a match.
        
    Returns:
        tuple: A tuple (games_p1, games_p2) containing the total games won.
    """
    games_p1, games_p2 = 0, 0
    # Split the string into individual set scores
    set_scores = score_string.split()
    
    for set_score in set_scores:
        if "RET" in set_score:
            # Stop processing if a retirement is noted
            break
        
        # Use regex to find the game scores, capturing both sides
        match = re.match(r'(\d+)-(\d+)', set_score)
        if match:
            p1_games_in_set = int(match.group(1))
            p2_games_in_set = int(match.group(2))
            
            # Add the base game scores
            games_p1 += p1_games_in_set
            games_p2 += p2_games_in_set
            
            # Check for a tie-breaker within the score
            if re.search(r'7-6\(\d+\)', set_score):
                # Add 1 bonus game for Player 1 due to winning the tie-breaker
                games_p1 += 1
            
    return games_p1, games_p2