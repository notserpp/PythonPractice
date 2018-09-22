def name_input():
    name = raw_input("Enter your First and Last name: ")
    age = int(raw_input("Enter your age: "))
    years_left = 100 - age;
    random_number = int(raw_input("Enter a random number: "))

    for x in range(random_number):
        print name + ", you will turn 100 years old in", years_left, "years"


name_input()
