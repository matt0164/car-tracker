# modules/scraper.py

def scrape_mock_inventory():
    return [
        {
            "dealer": "BMW of Bayside",
            "model": "2023 BMW 530e xDrive",
            "price": 43987,
            "mileage": 23388,
            "features": ["navigation", "wireless carplay", "awd"],
            "link": "https://www.bmwbayside.com/auto/preowned-2023-bmw-5-series-530e-xdrive-near-queens-ny/100494766/"
        },
        {
            "dealer": "Competition BMW",
            "model": "2022 BMW 530e xDrive",
            "price": 32225,
            "mileage": 46000,
            "features": ["navigation", "awd"],
            "link": "https://www.competitionbmw.com/"
        }
    ]