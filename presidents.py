from datetime import date

from presidents_data import presidents_by_party

from collections import namedtuple

def main():
    presidents = get_presidents_data(presidents_by_party)

def get_presidents_data(presidents_data):
    President = namedtuple('President', [
        'name', 'party', 'born', 'took_office', 'left_office'
    ])

    presidents = []

    for party, presidents_list in presidents_data.items():
        for president in presidents_list:
            president = President(name = president["name"], party=party,
                    born=president["born"],
                    took_office=president["took_office"],
                    left_office=president["left_office"]
                )
            presidents.append(president)

    return presidents


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
