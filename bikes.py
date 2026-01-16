'''
Natalia Gerasimova
CS 5001, Spring 2026
Homework 1, Program 2 -- Bike shop
'''

BIKE_WHEELS = 2
BIKE_FRAME = 1
BIKE_LINKS = 50

def main():
    """
    This function calculates possible amount of bikes the shop could make
    as well as the leftovers amount. All calculations are made based on
    spare parts amount. 

    Test cases:
    Test 1:
    Input:
        Wheels: 7
        Frames: 4
        Links: 150
    Expected result:
        Total bikes: 3
    Leftovers:
        Wheels: 1
        Frame 1
            Links:0

    Test 2:
    Input:
        Wheels: -7
        Frames: 4.8
        Links: 150
    Expected result:
        Total bikes: 3
        Leftovers:
            Wheels: 1
        Frame 1
        Links:0

    Test 3:
    Input:
        Wheels: 0
        Frames: -4.5
        Links: 45
    Expected result:
        Total bikes: 0
        Leftovers:
            Wheels: 0
            Frame 4
            Links: 45

    """
    bike_wheels_provided = abs(int(float(input("How many wheels do you have? "))))
    bike_frames_provided = abs(int(float(input("How many frames do you have? ")))) 
    bike_links_provided = abs(int(float(input("How many links do you have? "))))

    max_bikes_from_wheels = bike_wheels_provided // BIKE_WHEELS
    max_bikes_from_frames = bike_frames_provided // BIKE_FRAME
    max_bikes_from_links = bike_links_provided // BIKE_LINKS

    bikes_possible = min(max_bikes_from_wheels, max_bikes_from_frames, max_bikes_from_links)

    leftover_bike_wheels = bike_wheels_provided - (bikes_possible * BIKE_WHEELS)
    leftover_bike_frames = bike_frames_provided - (bikes_possible * BIKE_FRAME)
    leftover_bike_links = bike_links_provided - (bikes_possible * BIKE_LINKS)

    print(f"Total bikes I can make: {bikes_possible}")
    print("I'm keeping the leftovers for myself")
    print("Leftovers:")
    print(f"{leftover_bike_wheels} wheels")
    print(f"{leftover_bike_frames} frames")
    print(f"{leftover_bike_links} links")
if __name__ == "__main__":
    main()