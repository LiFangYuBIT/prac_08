from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    MENU = "q)uit, c)hoose taxi, d)rive"
    print(MENU)

    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    choose = input(">>> ").lower()
    while choose != "q":
        if choose == "d":
            if current_taxi:
                current_taxi.start_fare()
                print(current_taxi.start_fare())
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                print(current_taxi.get_fare())
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                total_bill += current_taxi.get_fare()
                print(total_bill)
            else:
                print("You need to choose a taxi before you can drive")

        elif choose == "c":
            print("Taxis available: ")
            for index, taxi in enumerate(taxis):
                print(f"{index} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

        else:
            print("Invalid option")

        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        choose = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


main()
