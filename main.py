from parse_files import parse

DATASETS = ['kittens.in', 'me_at_the_zoo.in',
             'trending_today.in', 'videos_worth_spreading.in']


if __name__ == "__main__":
    for dataset in DATASETS:

        print '\nProblem: ' + dataset
        parse('input/' + dataset)
