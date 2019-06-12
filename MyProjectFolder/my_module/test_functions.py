"""Test functions that test functions used in the Puzzle and Dragons Calculator"""

from functions import card_identity, combo_multiplier, damage_awakenings, damage_enhancing_skills, total_attack_damage


def test_card_identity():
    
    """Tests for the 'card_identity' function"""
    
    #Checks to see if function returns an int
    assert isinstance(card_identity('Black Dragon, Fatalis'), int)
    
    #Checks to see if input into the function returns expected result
    assert card_identity('Black Dragon, Fatalis') == 4000
                      
    #Checks to see if incorrect input will result in a return of 0    
    assert card_identity('a') == 0
    
    #Checks to see if an empty string will still return 0 
    assert card_identity('') == 0
           