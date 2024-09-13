countrydb = {}
while True:
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capital")
    print("5. Delete")

    choice = int(input("Enter an option of your choice : "))

    if choice == 1:
        country = input("Enter a country: ").upper()
        capital = input("Enter a capital: ").upper()

        countrydb[country] = capital

    if choice == 2:
        print(countrydb.keys())
   
    if choice == 3:
        print(countrydb.values())

    if choice == 4:
        country = input("Enter a country: ").upper()
        print(countrydb[country])

    if choice == 5:
        country = input("Enter a country: ").upper()
        del countrydb[country]
   