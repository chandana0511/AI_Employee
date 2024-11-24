import argparse
from modules.data_processing import load_data, clean_data
from modules.analysis_engine import perform_regression, perform_clustering, perform_classification
from modules.report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="AI Employee for Data Analysis")
    parser.add_argument('command', choices=['load', 'analyze', 'report'], help="Command to run")
    parser.add_argument('--file', type=str, help="Path to the data file")
    args = parser.parse_args()

    if args.command == 'load':
        df = load_data(args.file)
        df = clean_data(df)
        print("Data loaded and cleaned successfully.")
        print(df.head())

    elif args.command == 'analyze':
        df = load_data(args.file)
        df = clean_data(df)
        regression_model = perform_regression(df, ['Feature1', 'Feature2'], 'Target')
        print("Analysis done. Regression coefficients:", regression_model.coef_)

    elif args.command == 'report':
        df = load_data(args.file)
        df = clean_data(df)
        generate_report(df)

if __name__ == "__main__":
    main()
