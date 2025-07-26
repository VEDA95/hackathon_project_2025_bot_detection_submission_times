import argparse


def main():
    parser = argparse.ArgumentParser(prog="bot_sub_detector", usage="%(prog) [options]")

    parser.add_argument(
        "import_data", type=str, help="Import Docket from JSON file to SQL Database"
    )
    parser.add_argument("diff", help="Run diff on imported docket data")

    args = parser.parse_args()

    if (args.import_data is None) and (args.diff is None):
        raise Exception("The import or diff command was not provided...")

    if args.import_data is not None:
        if len(args.import_data) == 0:
            raise Exception("A filename must be provided from import...")

    if args.diff is not None:
        pass


if __name__ == "__main__":
    main()
