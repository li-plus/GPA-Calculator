from bs4 import BeautifulSoup
import argparse


def weighted_average(weights, values):
    return sum(w * v for w, v in zip(weights, values)) / sum(weights)


def main():
    old_map = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
               'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0}
    new_map = {k: min(4.0, v + 0.3) for k, v in old_map.items()}

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)
    args = parser.parse_args()

    with open(args.path, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    weights = [float(tag.text.strip()) for tag in soup.select('#table1 > tbody > tr > td:nth-of-type(3)')]
    letters = [tag.text.strip() for tag in soup.select('#table1 > tbody > tr > td:nth-of-type(4)')]

    valid_weights = []
    valid_letters = []
    for weight, letter in zip(weights, letters):
        if letter in old_map:
            valid_weights.append(weight)
            valid_letters.append(letter)

    weights = valid_weights
    letters = valid_letters

    print('old gpa', weighted_average(weights,  [old_map[x] for x in letters]))
    print('new gpa', weighted_average(weights,  [new_map[x] for x in letters]))


if __name__ == '__main__':
    main()
