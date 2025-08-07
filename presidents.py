from datetime import date, datetime

from presidents_data import presidents_by_party

from collections import namedtuple, Counter

def main():
    president_namedtuples = get_presidents_data(presidents_by_party)
    party = get_party_with_most_presidents(president_namedtuples)
    youngest_rep = get_est_pres(president_namedtuples, "youngest", "Republican")
    oldest_dem = get_est_pres(president_namedtuples, "oldest", "Democratic")
    youngest_pres = get_est_pres(president_namedtuples, "youngest")
    oldest_pres = get_est_pres(president_namedtuples, "oldest")
    output_message(party, youngest_rep, oldest_dem, youngest_pres, oldest_pres)

def get_presidents_data(data_dict):
    President = namedtuple('President', [
        'name', 'party', 'born', 'took_office', 'took_office_age', 'left_office'
    ])

    presidents = []

    for party, presidents_list in data_dict.items():
        for president in presidents_list:
            born_date = president["born"]
            took_office_date = president["took_office"]
            age_at_office = (took_office_date - born_date).days // 365

            president = President(
                name = president["name"],
                party=party,
                born=president["born"],
                took_office=president["took_office"],
                took_office_age=age_at_office,
                left_office=president["left_office"]
            )

            presidents.append(president)

    return presidents

def get_party_with_most_presidents(presidents):
    """Create a Counter object to then use most_common([n]) to return a
    list with a tuple containing the most common presidential party and
    the count. The access and return the name of the party."""
    party_counts = Counter(p.party for p in presidents)
    return party_counts.most_common(1)[0][0]

def get_est_pres(presidents, youngest_or_oldest, pres_party=None):
    """Get a list of all presidents for a given party, then return the
    name of the oldest or youngest president depending on the args
    passed into the function. If no party is specified, return the
    oldest or youngest president overall"""
    if pres_party is None:
        party_presidents = presidents
    else:
        party_presidents = [p for p in presidents if p.party == pres_party]

    min_max = min if youngest_or_oldest == "youngest" else max
    return min_max(party_presidents, key=lambda p: p.took_office_age).name

def output_message(*args):
    print(args)


if __name__ == "__main__":
    main()

# TODO:
# * Display a report that answers the following questions:
#   * Which party has had most presidents?
#   * Who was the youngest Republican president when they took office?
#   * Who was the oldest Democrat president when they took office?
#   * Who was the youngest president (from any party) when they took office?
#   * Who was the oldest president (from any party) when they took office?
#   * Which month saw the most presidents take office?
#   * Which decade saw the most presidents take office?
#   * Which party has been in power for longest?
#   * What is the average age of becoming president?
#   * Which presidents have taken office more than once?
