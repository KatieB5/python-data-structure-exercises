# This file contains a list of results from Group F of the Euro 2016
# championship.  Each item in the list of results is a dictionary, whose keys
# are the names of the teams playing a match, and whose values are the number
# of goals scored by each team in the match.
#
# When the file is run, it should display some facts about the final results in
# the group.
#
# NB Teams score three points for a win and one point for a draw.

# ASSUMPTIONS:
# 0-0 is a draw, both teams score 1 point.

results = [
        {'Austria': 0, 'Hungary': 2},
        {'Portugal': 1, 'Iceland': 1},
        {'Iceland': 1, 'Hungary': 1},
        {'Portugal': 0, 'Austria': 0},
        {'Iceland': 2, 'Austria': 1},
        {'Hungary': 3, 'Portugal': 3},
]

unique_teams = {k for match in results for k in match}

def main():
     team_goals = {team: 0 for team in unique_teams}
     team_points = {team: 0 for team in unique_teams}

     match_most_goals, match_fewest_goals = get_match_goals()

     team_most_goals, team_fewest_goals = get_team_goals(team_goals)

     team_most_points, team_fewest_points = get_team_points(team_points)

     print_results(match_most_goals, match_fewest_goals, team_most_goals, team_fewest_goals, team_most_points, team_fewest_points)


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
     return sum(results[i].values())

def format_match(match_obj):
     return f"{list(match_obj.keys())[0]} vs {list(match_obj.keys())[1]}"

def get_team_goals(team_goals):
     for match in results:
          teams = list(match.keys())
          goals = list(match.values())

          team_goals[teams[0]] += goals[0]
          team_goals[teams[1]] += goals[1]

     sorted_team_goals = sorted(team_goals.items(), key=lambda item: item[1])
     team_fewest_goals = sorted_team_goals[0][0]
     team_most_goals = sorted_team_goals[-1][0]

     return [team_most_goals, team_fewest_goals]

def get_team_points(team_points):
     for match in results:
          match_list = list(match.items())
          if match_list[0][1] > match_list[1][1]:
               team_points[match_list[0][0]] += 3
          elif match_list[1][1] > match_list[0][1]:
               team_points[match_list[1][0]] += 3
          else :
               team_points[match_list[0][0]] += 1
               team_points[match_list[1][0]] += 1

     sorted_team_points = {k: v for k, v in sorted(team_points.items(), key=lambda item: item[1])}

     team_most_points = list(sorted_team_points.keys())[len(sorted_team_points) - 1]
     team_fewest_points = list(sorted_team_points.keys())[0]

     return [team_most_points, team_fewest_points]

def print_results(match_most_goals, match_fewest_goals, team_most_goals, team_fewest_goals, team_most_points, team_fewest_points):
     print(f'The match with the most goals was {match_most_goals}')
     print(f'The match with the fewest goals was {match_fewest_goals}')
     print(f'The team with the most total goals was {team_most_goals}')
     print(f'The team with the fewest total goals was {team_fewest_goals}')
     print(f'The team with the most points was {team_most_points}')
     print(f'The team with the fewest points was {team_fewest_points}')

if __name__ == "__main__":
    main()

# TODO (extra): Write code to compute and display a league table
