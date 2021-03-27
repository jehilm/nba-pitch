from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import os

for i in range(2010, 2021):
    if not os.path.exists(f"{i}"):
        os.makedirs(f"{i}")
    client.players_advanced_season_totals(
        season_end_year=i,
        output_type=OutputType.CSV,
        output_file_path=f"./{i}/players.csv"
    )
    client.standings(
        season_end_year=i,
        output_type=OutputType.CSV, 
        output_file_path=f"./{i}/standings.csv"
    )