import matplotlib.pyplot as plt
from load_csv import load


def gdp_to_life_expectancy(year):

    life_data = load('life_expectancy_years.csv')
    gdp_data = (
        load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    )

    life_data_year = life_data[year]
    gdp_data_year = gdp_data[year]

    plt.scatter(gdp_data_year, life_data_year)

    plt.title(year)
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')

    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    plt.show()


def main():
    gdp_to_life_expectancy('1900')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
