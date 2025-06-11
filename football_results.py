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

def main():
#match goals
        [most_goals, fewest_goals] = get_match_goals()
#team goals

#team points


# TODO: Write code to answer the following questions:

        print(f'The match with the most goals was {most_goals}')
        print(f'The match with the fewest goals was {fewest_goals}')
        print('The team with the most total goals was', '?')
        print('The team with the fewest total goals was', '?')
        print('The team with the most points was', '?')
        print('The team with the fewest points was', '?')

def get_match_goals():
      most_goals_count = get_goal_total(0)
      most_goals_match = results[0]
      fewest_goals_count = get_goal_total(0)
      fewest_goals_match = results[0]

      for i in range(1, len(results)):
        goal_total = get_goal_total(i)
        if goal_total > most_goals_count:
             most_goals_count = goal_total
             most_goals_match = results[i]
        if goal_total < fewest_goals_count:
             fewest_goals_count = goal_total
             fewest_goals_match = results[i]

      return [format_match(most_goals_match), format_match(fewest_goals_match)]

def get_goal_total(i):
     return reduce(lambda x, y: x+y, results[i].values())

def format_match(match_obj):
     return f"{list(match_obj.keys())[0]} vs {list(match_obj.keys())[1]}"

if __name__ == "__main__":
    main()

# TODO (extra): Write code to compute and display a league table
