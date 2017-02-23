from algorithm import run_that_beast
from parse_files import parse
from stringify import stringify

DATASETS = ['me_at_the_zoo.in', 'kittens.in', 
             'trending_today.in', 'videos_worth_spreading.in']


if __name__ == "__main__":
    for dataset in DATASETS:

        print '\nProblem: ' + dataset
        problem = parse('input/' + dataset)
        solution_with_caches = run_that_beast(problem)

        stringify(solution_with_caches, dataset + '_out')
