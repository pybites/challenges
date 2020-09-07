import argparse

from weather import Weather


def main():
    """
    Calls the Weather class from the commandline via argparse.
    """
    parser = argparse.ArgumentParser(
        description="Weather reporting at the command line."
    )
    parser.add_argument(
        "--city",
        "-c",
        help="City you want to get weather from. Defaults to London. Hyphenated or multiword cities must be delineated by a `_`. Example `nova_scotia`",
    )
    parser.add_argument(
        "--country-code",
        "-cc",
        help="Country Code for the city you have selected. Major, well known cities will often return a result when this flag is missing, e.g. salzburg. Defaults to GB.",
    )

    args = parser.parse_args()

    if args.city:
        # API allows ' ' but argparse does not.
        city = args.city.replace("_", " ")
        Weather(city, args.country_code)
    else:
        Weather()


if __name__ == "__main__":
    main()
