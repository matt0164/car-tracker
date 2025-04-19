# bmw_tracker_main.py

from modules.scraper import scrape_mock_inventory
from modules.emailer import send_bmw_email
from config import SEARCH_CONFIG


def filter_listings(listings):
    results = []
    for car in listings:
        if car["price"] <= SEARCH_CONFIG["max_price"] and car["mileage"] <= SEARCH_CONFIG["max_mileage"]:
            if all(term in [f.lower() for f in car["features"]] for term in SEARCH_CONFIG["must_have"]):
                results.append(car)
    return results


def format_email_body(filtered_listings):
    if not filtered_listings:
        return "No new BMW 530e listings matched your filters today."

    lines = []
    for car in filtered_listings:
        lines.append(
            f"{car['model']} - ${car['price']:,} - {car['mileage']} miles\nDealer: {car['dealer']}\n{car['link']}\n")
    return "\n".join(lines)


if __name__ == "__main__":
    all_listings = scrape_mock_inventory()
    matches = filter_listings(all_listings)
    email_body = format_email_body(matches)
    send_bmw_email("🚗 BMW 530e Daily Tracker", email_body)