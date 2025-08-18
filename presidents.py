from collections import namedtuple, Counter, defaultdict
from statistics import mean
from operator import itemgetter

from presidents_data import presidents_by_party


def main():
    president_namedtuples = get_presidents_data(presidents_by_party)
    party = get_party_with_most_presidents(president_namedtuples)
    youngest_rep = get_est_pres(president_namedtuples, "youngest", "Republican")
    oldest_dem = get_est_pres(president_namedtuples, "oldest", "Democratic")
    youngest_pres = get_est_pres(president_namedtuples, "youngest")
    oldest_pres = get_est_pres(president_namedtuples, "oldest")
    mean_age = get_mean_age(president_namedtuples)
    month = get_month(president_namedtuples)
    decade = get_decade(president_namedtuples)
    in_power_longest = get_in_power_longest(president_namedtuples)
    repeat_pres = get_repeat_pres(president_namedtuples)
    output_message(
        party,
        youngest_rep,
        oldest_dem,
        youngest_pres,
        oldest_pres,
        mean_age,
        month,
        decade,
        in_power_longest,
        repeat_pres,
    )


def get_presidents_data(data_dict):
    President = namedtuple(
        "President",
        [
            "name",
            "party",
            "born",
            "took_office",
            "took_office_age",
            "left_office",
            "in_office",
        ],
    )

    presidents = []

    for party, presidents_list in data_dict.items():
        for president in presidents_list:
            age_at_office = (president["took_office"] - president["born"]).days // 365
            time_in_office = (president["left_office"] - president["took_office"]).days

            president = President(
                name=president["name"],
                party=party,
                born=president["born"],
                took_office=president["took_office"],
                took_office_age=age_at_office,
                left_office=president["left_office"],
                in_office=time_in_office,
            )

            presidents.append(president)

    return presidents


def get_party_with_most_presidents(presidents):
    """Create a Counter object to then use most_common([n]) to return a
    list with a tuple containing the most common presidential party and
    the count. Then return the name of the party."""
    party_counts = Counter(p.party for p in presidents)
    return party_counts.most_common(1)[0][0]


def get_est_pres(presidents, youngest_or_oldest, pres_party=None):
    """Return the name of the oldest or youngest president depending on the args passed into the function. If no party is specified, return the oldest or youngest president overall."""
    if pres_party is None:
        party_presidents = presidents
    else:
        party_presidents = [p for p in presidents if p.party == pres_party]

    min_max = min if youngest_or_oldest.lower() == "youngest" else max
    return min_max(party_presidents, key=lambda p: p.took_office_age).name


def get_mean_age(presidents):
    return mean([p.took_office_age for p in presidents])


def get_month(presidents):
    """Return the most common month for presidents to take office, then return it to main."""
    month_or_year_counts = Counter(
        p.took_office.strftime("%B") for p in presidents
    )
    return month_or_year_counts.most_common(1)[0][0]


def get_decade(presidents):
    """Return the most common decade for presidents to take office, then return it to main."""
    month_or_year_counts = Counter(
        p.took_office.strftime("%Y")[:-1] for p in presidents
    )
    return month_or_year_counts.most_common(1)[0][0] + "0"


def get_in_power_longest(presidents):
    """Instantiate a default dict with the party names as keys and corresponding values of a count of the total number of days in office each president from that party had. Return the party with the highest count."""
    d = defaultdict(int)
    for p in presidents:
        d[p.party] += p.in_office
    return sorted(d.items(), key=itemgetter(1))[-1][0]


def get_repeat_pres(presidents):
    """Return a list of presidents who have taken office >1 time. This does not return presidents who had back-to-back-turns in office."""
    pres_counts = Counter(p.name for p in presidents)
    repeat_pres = [pres for pres in pres_counts if pres_counts[pres] > 1]
    return ", ".join(repeat_pres) if repeat_pres else "No presidents"


def output_message(*args):
    intro = "\nHere are some facts about US presidents:\n\n"
    text = f"The {args[0]} party has had most presidents.\n {args[1]} was the youngest Republican president when they took office.\n {args[2]} was the oldest Democrat president when they took office.\n {args[3]} was the youngest president (from any party) when they took office.\n {args[4]} was the oldest president (from any party) when they took office.\n {args[5]} is the average age of becoming president.\n {args[6]} saw the most presidents take office.\n {args[7]} was the decade that saw the most presidents take office.\n The {args[8]} party has been in power for longest.\n {args[9]} have taken office more than once."
    print(intro, text)


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
#   * What is the average age of becoming president?
#   * Which party has been in power for longest?
#   * Which presidents have taken office more than once?
#   * Which decade saw the most presidents take office?
