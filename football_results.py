# This file contains a list of results from Group F of the Euro 2016
# championship.  Each item in the list of results is a dictionary, whose keys
# are the names of the teams playing a match, and whose values are the number
# of goals scored by each team in the match.
#
# When the file is run, it should display some facts about the final results in
# the group.
#
# NB Teams score three points for a win and one point for a draw.
from functools import reduce

results = [
        {'Austria': 0, 'Hungary': 2},
        {'Portugal': 1, 'Iceland': 1},
        {'Iceland': 1, 'Hungary': 1},
        {'Portugal': 0, 'Austria': 0},
        {'Iceland': 2, 'Austria': 1},
        {'Hungary': 3, 'Portugal': 3},
]

unique_teams = {k for dict in results for k in dict.keys()}

team_goals = {team: 0 for team in unique_teams}

team_points = {team: 0 for team in unique_teams}


def main():
#match goals
     match_most_goals, match_fewest_goals = get_match_goals()
#team goals
     team_most_goals, team_fewest_goals = get_team_goals()
#team points
     get_team_points()

# TODO: Write code to answer the following questions:

     print(f'The match with the most goals was {match_most_goals}')
     print(f'The match with the fewest goals was {match_fewest_goals}')
     print(f'The team with the most total goals was {team_most_goals}')
     print(f'The team with the fewest total goals was {team_fewest_goals}?')
     print('The team with the most points was', '?')
     print('The team with the fewest points was', '?')

def get_match_goals():
     most_goals_count = get_goal_total(0)
     match_most_goals = results[0]
     fewest_goals_count = get_goal_total(0)
     match_fewest_goals = results[0]

     for i in range(1, len(results)):
          goal_total = get_goal_total(i)
          if goal_total > most_goals_count:
               most_goals_count = goal_total
               match_most_goals = results[i]
          if goal_total < fewest_goals_count:
               fewest_goals_count = goal_total
               match_fewest_goals = results[i]

     return [format_match(match_most_goals), format_match(match_fewest_goals)]

def get_goal_total(i):
     return reduce(lambda x, y: x+y, results[i].values())

def format_match(match_obj):
     return f"{list(match_obj.keys())[0]} vs {list(match_obj.keys())[1]}"

def get_team_goals():
     for match in results:
          teams = list(match.keys())
          goals = list(match.values())

          team_goals[teams[0]] += goals[0]
          team_goals[teams[1]] += goals[1]

          sorted_team_goals = {k: v for k, v in sorted(team_goals.items(), key=lambda item: item[1])}

          team_most_goals = list(sorted_team_goals.keys())[len(sorted_team_goals) - 1]
          team_fewest_goals = list(sorted_team_goals.keys())[0]

     return [team_most_goals, team_fewest_goals]

def get_team_points():
     for match in results:
          goals = list(match.values())
          if goals[0] > goals[1]:
               pass

if __name__ == "__main__":
    main()

# TODO (extra): Write code to compute and display a league table
