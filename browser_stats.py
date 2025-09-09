# This program displays a report about browser usage statistics, as recorded by
# w3schools.com.
#
# Usage:
#
# $ python browser_stats.py
from collections import namedtuple
from browser_stats_data import browser_stats_by_year_and_month

BrowserRecord = namedtuple(
    "BrowserRecord", ["year", "month", "browser", "market_share"]
)


def main():
    browser_tuples = get_browser_tuples(browser_stats_by_year_and_month)
    get_reporting_period(browser_tuples)


def get_browser_tuples(data):
    browser_tuples = []

    for year, months in data.items():
        for month, browsers in months.items():
            for browser, market_share in browsers.items():
                browser_tuples.append(
                    BrowserRecord(
                        year=year,
                        month=month,
                        browser=browser,
                        market_share=market_share,
                    )
                )
    return browser_tuples

def get_reporting_period(data_tuples):
    reporting_period = f"{data_tuples[-1].month} {data_tuples[-1].year} to {data_tuples[0].month} {data_tuples[0].year}"
    print(data_tuples)
    return reporting_period

if __name__ == "__main__":
    main()


# TODO:
# * Display a report that answers the following questions:
#   * What period does the report cover?
#   * In the period covered, which browsers have had over 50% of market share?
#   * In which month did Firefox first become the most popular browser?
#   * In which month did Chrome first overtake IE in popularity?
#   * In which month was Firefox's popularity highest?
#   * In which month was the combined popularity of Safari and Opera highest?
#   * Which month saw the biggest percentage point rise in Chrome's popularity?
#   * Which month saw the biggest percentage point
