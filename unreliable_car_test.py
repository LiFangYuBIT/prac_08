from unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("More Reliable Car", 100, 90)
    unreliable_car = UnreliableCar("Unreliable Car", 100, 10)

    for i in range(1, 10):
        print(f"Attempting to drive {i}km:")
        print(f"{reliable_car.name:<20} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name:<20} drove {unreliable_car.drive(i):2}km")
        print("=="*10)

    print(reliable_car)
    print(unreliable_car)


if __name__ == '__main__':
    main()
