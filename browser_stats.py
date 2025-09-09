# This program displays a report about browser usage statistics, as recorded by
# w3schools.com.
#
# Usage:
#
# $ python browser_stats.py
from collections import namedtuple, defaultdict
from browser_stats_data import browser_stats_by_year_and_month

BrowserRecord = namedtuple(
    "BrowserRecord", ["year", "month", "browser", "market_share"]
)


def main():
    browser_tuples = get_browser_tuples(browser_stats_by_year_and_month)
    reporting_period = get_reporting_period(browser_tuples)
    market_share_over_50 = get_over_50_market_share_browsers(browser_tuples)
    firefox_most_popular_month = firefox_most_popular(browser_tuples)
    display_report(reporting_period, market_share_over_50, firefox_most_popular_month)


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
    return reporting_period

def get_over_50_market_share_browsers(data_tuples):
    browser_record_list = []
    for browser_record in data_tuples:
        if browser_record.market_share > 50 and browser_record.browser not in browser_record_list:
            browser_record_list.append(browser_record.browser)

    return browser_record_list


def display_report(reporting_period, market_share_over_50, firefox_most_popular_month):
    print("A report of browser usage statistics, as recorded by w3schools.com:")
    print(f"This report covers the period {reporting_period}")
    print(f"The following browsers had had over 50% of market share: {', '.join(market_share_over_50)}")
    print(f"Firefox first became the most popular browser in {firefox_most_popular_month[0]} {firefox_most_popular_month[1]}")

def firefox_most_popular(data_tuples):
    month_year_browsers = defaultdict(list)
    for browser_record in data_tuples:
        month_year_browsers[(browser_record.year, browser_record.month)].append(browser_record)

    for (year, month), browser_records in month_year_browsers.items():
        max_market_share = max(browser_records, key=lambda record: record.market_share)
        if max_market_share.browser == "Firefox":
            return [month, year]

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
