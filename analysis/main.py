from analysis.analyzer import Analyzer
from analysis.input_provider import InputProvider
from analysis.tester import Tester


def run_comparison_analysis():
    input_provider = InputProvider()
    tester = Tester(input_provider.benchmarks)
    analyzer = Analyzer()

    while True:
        file = input_provider.next_file
        if file is None:
            break
        elif 'aaa.txt' in file:
            continue
        print(f'Running test for file {file}')
        tester.run_compressors(file)

    input_provider.clean()
    tester.store_results()
    analyzer.run_analysis(tester.results)


if __name__ == '__main__':
    run_comparison_analysis()
