from taxi import Taxi


def main():
    prius_one = Taxi("Prius 1", 100)
    prius_one.drive(40)
    print(prius_one)
    print(f"Need Pay: ${prius_one.get_fare()}")

    prius_one.start_fare()
    prius_one.drive(100)
    print(prius_one)
    print(f"Need Pay: ${prius_one.get_fare()}")


if __name__ == '__main__':
    main()
