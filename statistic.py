import pandas as pd
import matplotlib.pyplot as plt
from log import log
import geopandas as gpd


df = pd.read_csv('steam_players.csv')

class Stat:

    @log
    def statistic():
        country_stats = df.groupby('country')['playerid'].nunique().reset_index()
        country_stats.columns = ['Страна', 'Количество игроков']
        country_stats['Игроки (сотни тысяч)'] = country_stats['Количество игроков'] / 100000
        plt.figure(figsize=(16, 9))
        plt.bar(country_stats['Страна'], country_stats['Игроки (сотни тысяч)'], color='skyblue')
        plt.title('Количество игроков Steam')
        plt.ylabel('В сотнях тысяч)')
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()