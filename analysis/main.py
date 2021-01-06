from analysis.analyzer import Analyzer
from analysis.input_provider import InputProvider
from analysis.tester import Tester


def run_comparison_analysis():
    input_provider = InputProvider()
    tester = Tester()
    analyzer = Analyzer()

    while not input_provider.is_finished:
        file = input_provider.next_file
        tester.run_compressors(file)

    analyzer.run_analysis(tester.results)


if __name__ == '__main__':
    run_comparison_analysis()
