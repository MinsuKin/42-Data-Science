import matplotlib.pyplot as plt
from load_csv import load


def draw_country_life_expectancy(country_name):
    """Shows a graph of the life expectancy of a country over the years."""

    data = load('life_expectancy_years.csv')
    country_data = data[data['country'] == country_name]

    years = country_data.columns[1:].astype(int)
    life_expectancy = country_data.values[0][1:]

    plt.plot(years, life_expectancy, linestyle='-', color='b')

    plt.title(f'{country_name} Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')

    plt.show()


def main():
    draw_country_life_expectancy('Canada')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
