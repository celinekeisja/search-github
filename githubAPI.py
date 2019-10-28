import argparse
import requests
import csv
from datetime import datetime


def datetime_name(output_name):
    """Creates a filename for the output according to the given format."""
    now = datetime.now()
    return f'{output_name}-{now.strftime("%Y-%m-%d-%H-%M")}.csv'


def search(url, output_name, token):
    ''' Puts the results of the search in a CSV file. '''
    header = {'Authorization': f'Token {token}'}
    r = requests.get(url, headers=header)
    name = datetime_name(output_name)
    with open(name, 'w+', newline='', encoding="utf-8") as csv_file:
        field_n = ['Project Name', 'Description', 'URL', 'Programming Language', 'Last Updated']
        writer = csv.DictWriter(csv_file, fieldnames=field_n)
        writer.writeheader()
        for key in range(len(r.json()['items'])):
            d = {"Project Name": r.json()['items'][key]['name'], "Description": r.json()['items'][key]['description'], "URL": r.json()['items'][key]['url'],
                 "Programming Language": r.json()['items'][key]['language'], "Last Updated": r.json()['items'][key]['updated_at']}
            writer.writerow(d)
    return f'Created {name}!'


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("search")
    parser.add_argument("url")
    parser.add_argument("output_name")
    parser.add_argument("token")
    args = parser.parse_args()
    url = f'{args.url}?q={args.search}&per_page=1000'
    print(search(url, args.output_name, args.token))