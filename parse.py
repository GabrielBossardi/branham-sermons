import json
import pandas as pd
from sqlalchemy import create_engine

def main():
    # Read JSON from file
    with open('data/sermons.json') as f:
        json_data = json.load(f)

    username="postgres"
    password="postgres"
    host="localhost"
    port="5432"
    database="postgres"
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

    sermons = []
    for sermon in json_data:
        sermon_dict = {}
        sermon_dict['id'] = sermon['id']
        sermon_dict['title'] = sermon['title']['displayName']
        sermon_dict['date'] = sermon['date']['date']
        sermon_dict['date_display_name'] = sermon['date']['displayName']
        if sermon['date']['modifier']:
            sermon_dict['date_day_period'] = sermon['date']['modifier']['meaning']
        if sermon['location']['country']:
            sermon_dict['location_country'] = sermon['location']['country']['name']
            sermon_dict['location_country_abbv'] = sermon['location']['country']['abbreviation']
        if sermon['location']['state']:
            sermon_dict['location_state'] = sermon['location']['state']['name']
            sermon_dict['location_state_abbv'] = sermon['location']['state']['abbreviation']
        sermon_dict['location_city'] = sermon['location']['city']
        sermon_dict['building'] = sermon['building']['displayName']
        sermon_dict['audio'] = sermon['audio']['secure']

        sermons.append(sermon_dict)

    # Insert data into table
    df = pd.DataFrame.from_dict(sermons)
    df.to_sql('sermons', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    main()
