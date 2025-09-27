from django import forms
import pandas as pd 
import os
from . import settings

script_dir = os.path.dirname(os.path.abspath(__file__))

players_csv_path = os.path.join(script_dir, 'data_and_models/players_data.csv')

players = pd.read_csv(players_csv_path)

player_names = players['full_name'].tolist()
player_choices = [(name, name) for name in player_names]

class MatchupForm(forms.Form):
    player_one = forms.ChoiceField(
        label='Player One',
        choices=player_choices,
        required=True
    )
    
    player_two = forms.ChoiceField(
        label='Player Two',
        choices=player_choices,
        required=True
    )
    
    def clean(self):
        """
        Custom validation to ensure player_one and player_two are not the same.
        """
        cleaned_data = super().clean()
        player_one = cleaned_data.get('player_one')
        player_two = cleaned_data.get('player_two')
        
        if player_one and player_two and player_one == player_two:
            raise forms.ValidationError("Please select two different players.")
            
        return cleaned_data