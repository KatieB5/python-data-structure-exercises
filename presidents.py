from datetime import date

from presidents_data import presidents_by_party

from collections import namedtuple

print('There have been presidents from {} different parties'.format(len(presidents_by_party)))

President = namedtuple('President', [
    'name', 'party', 'born', 'took_office', 'left_office'
])

presidents = []

for party, presidents_list in presidents_by_party.items():
    for president in presidents_list:
        president = President(name = president["name"], party=party,
                born=president["born"],
                took_office=president["took_office"],
                left_office=president["left_office"]
            )
        presidents.append(president)

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
