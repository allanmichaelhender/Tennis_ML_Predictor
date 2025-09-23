from django.shortcuts import render
from .forms import MatchupForm
from .predictor_functions import random_forest_predict, logistic_regression_predict, decision_tree_predict

def random_forest(request):
    if request.method == 'POST':
            form = MatchupForm(request.POST)
            if form.is_valid():
                player_one = form.cleaned_data['player_one']
                player_two = form.cleaned_data['player_two']
                # Process your data, e.g., save to a database or perform a lookup
                context = {
                    'form': form,
                    'player_one': player_one,
                    'player_two': player_two,
                    'message': f'If {player_one} played {player_two} on 2025-01-01',
                    'return_val': random_forest_predict(player_one,player_two)
                }
                return render(request, 'random_forest.html', context)
            else:
                return render(request, 'random_forest.html', {'form': form})
    else:
        form = MatchupForm()
    return render(request, 'random_forest.html', {'form': form})

def logistic_regression(request):
    if request.method == 'POST':
            form = MatchupForm(request.POST)
            if form.is_valid():
                player_one = form.cleaned_data['player_one']
                player_two = form.cleaned_data['player_two']
                # Process your data, e.g., save to a database or perform a lookup
                context = {
                    'form': form,
                    'player_one': player_one,
                    'player_two': player_two,
                    'message': f'If {player_one} played {player_two} on 2025-01-01',
                    'return_val': logistic_regression_predict(player_one,player_two)
                }
                return render(request, 'logistic_regression.html', context)
            else:
                return render(request, 'logistic_regression.html', {'form': form})
    else:
        form = MatchupForm()
    return render(request, 'logistic_regression.html', {'form': form})

def decision_tree(request):
    if request.method == 'POST':
            form = MatchupForm(request.POST)
            if form.is_valid():
                player_one = form.cleaned_data['player_one']
                player_two = form.cleaned_data['player_two']
                # Process your data, e.g., save to a database or perform a lookup
                context = {
                    'form': form,
                    'player_one': player_one,
                    'player_two': player_two,
                    'message': f'If {player_one} played {player_two} on 2025-01-01',
                    'return_val': decision_tree_predict(player_one,player_two)
                }
                return render(request, 'decision_tree.html', context)
            else:
                return render(request, 'decision_tree.html', {'form': form})
    else:
        form = MatchupForm()
    return render(request, 'decision_tree.html', {'form': form})


