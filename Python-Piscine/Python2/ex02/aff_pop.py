import matplotlib.pyplot as plt
from load_csv import load
import matplotlib.ticker as ticker


def tens_of_millions(x, pos):
    """Formats the y-axis labels to show the number in millions."""
    return '%1.0fM' % (x * 1e-6)


def parse_population(population_str):
    """Parses a population string and returns a float."""
    multiplier = 1
    if 'k' in population_str:
        multiplier = 1000
        population_str = population_str.replace('k', '')
    elif 'M' in population_str:
        multiplier = 1000000
        population_str = population_str.replace('M', '')
    elif 'B' in population_str:
        multiplier = 1000000000
        population_str = population_str.replace('B', '')
    return float(population_str) * multiplier


def compare_population(country1, country2):
    """Draws a line graph of the population of two countries over the years."""
    data = load('population_total.csv')
    country1_data = data[data['country'] == country1]
    country2_data = data[data['country'] == country2]

    years = country1_data.columns[1:-50].astype(int)
    country1_population = country1_data.values[0][1:-50]
    country2_population = country2_data.values[0][1:-50]

    country1_population = [parse_population(str(pop)) for pop in country1_population]
    country2_population = [parse_population(str(pop)) for pop in country2_population]

    plt.plot(years, country1_population, linestyle='-', color='b')
    plt.plot(years, country2_population, linestyle='-', color='g')

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')

    plt.xticks(range(1800, 2041, 40))
    plt.yticks(range(10_000_000, 51_000_000, 10_000_000))

    formatter = ticker.FuncFormatter(tens_of_millions)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.legend([country1, country2], loc='lower right')

    plt.show()


def main():
    compare_population('Canada', 'South Korea')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
