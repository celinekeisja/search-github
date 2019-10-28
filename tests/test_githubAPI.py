from githubAPI import *
import os
from datetime import datetime

output_name = 'SampleName'
url = 'https://api.github.com/search/repositories?=tetris&per_page1000'
token = '80256d3906258d0621dbce2852e1ac7dd8d67ca9'
final_name = f'{output_name}-{datetime.now().strftime("%Y-%m-%d-%H-%M")}.csv'


def test_search():
    """Test search method."""
    assert search(url, final_name, token) == f'Created {final_name}!'
    assert os.path.isfile(fr'C:\Users\TEU_USER\PycharmProjects\search-github\tests\{final_name}')


def test_datetime_name():
    """Test datetime_name method."""
    assert datetime_name(output_name) == final_name
