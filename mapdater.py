b
print("Toby's Map Dater (1808 to 2020)")
print("")
print("Yemen is:")
print("A - Ottoman (On the Red Sea)")
print("B - Small")
print("C - In half (North/South Yemen)")
print("D - Dented")
print("E - Normal (The same as how it looks today)")
print("F - It doesn't exist")
answer = input("Input Answer > ")

if answer.lower() == "a":
    print("Your map is from 1896 to 1919.")
elif answer.lower() == "b":
    print("Germany is:")
    print("A - Relatively in one piece (excluding Konigsberg/Kaliningrad if applicable)")
    print("B - Huge")
    print("C - In four pieces")
    print("D - In two pieces (East/West Germany)")
    answer = input("Input Answer > ")

    if answer.lower() == "a":
        print("Is Anatolia Ottoman or Turkish?")
        print("A - Ottoman")
        print("B - Turkish")
        answer = input("Input Answer > ")

        if answer.lower() == "a":
            print("Does Ukraine Exist? Y/N")
            answer = input("Input Answer > ")
            
            if answer.lower() == "y":
                print("Your map is from 1919 to 1920.")
            elif answer.lower() == "n":
                print("Your map is from 1921 to 1922.")
                
        if answer.lower() == "b":
            print("Your map is from 1923 to 1939.")
            answer = "buffer"
    if answer.lower() == "b":
        print("Your map is from 1939 to 1945.")
    if answer.lower() == "c":
        print("Your map is from 1946 to 1950.")
    if answer.lower() == "d":
        print("Is Syria part of the UAR? Y/N")
        answer = input ("Input Answer > ")

        if answer.lower() == "y":
            print("Your map is from 1959 to 1962.")
        if answer.lower() == "n":
            print("Tanganyika or Tanzania?")
            print("A - Tanganyika")
            print("B - Tanzania")
            answer = input("Input Answer > ")

            if answer.lower() == "a":
                print("Your map is from 1950 to 1959.")
            if answer.lower() == "b":
                print("a")
                if answer.lower() == "y":
                    print("Your map is from 1968.")
                if answer.lower() == "n":
                    print("Your map is from 1962 to 1967")
            
elif answer.lower() == "c":
    print("How much of the Sinai Peninsula does Israel own?")
    print("A - None")
    print("B - Some")
    print("C - All")
    answer = input ("Input Answer > ")

    if answer.lower == "a":
        print("Your map is from 1983 to 1991.")
    if answer.lower == "b":
        print("Your map is from 1975 to 1982.")
    if answer.lower == "c":
        print("Your map is from 1968 to 1976.")

elif answer.lower() == "d":
    print("Is Hong Kong British or Chinese?")
    print("A - British")
    print("B - Chinese")
    answer = input("Input Answer > ")
    if answer.lower() == "a":
        print("Your map is from 1991 to 1997.")
    if answer.lower() == "b":
        print("Your map is from 1997 to 2001.")

elif answer.lower() == "e":
    print("Does South Sudan exist? Y/N")
    answer = input("Input Answer > ")
    if answer.lower() == "y":
        print("Your map is from 2013 to 2020.")
    if answer.lower() == "n":
        print("Does Montenegro exist? Y/N")
        answer = input("Input Answer > ")
        if answer.lower() == "y":
            print("Does Kosovo exist? Y/N")
            answer = input("Input Answer > ")
            if answer.lower == "y":
                print("Your map is from 2009 to 2013.")
            if answer.lower == "n":
                print("Your map is from 2007 to 2009.")
                answer = "buffer"
        if answer.lower() == "n":
            print("Your map is from 2001 to 2007.")
#1808-1919code
elif answer.lower() == "f":
    print("Does Poland exist? Y/N")
    answer = input("Input Answer > ")
    if answer.lower() == "y":
        print("Your map is from 1808 to 1815.")
    if answer.lower() == "n":
        print("Is Germany in once piece? Y/N")
        answer = input("Input Answer > ")
        if answer.lower() == "y":
            print("Your map is from 1871 to 1896.")
        if answer.lower() == "n":
            print("Is Italy united? Y/N")
            answer = input("Input Answer > ")

            if answer.lower() == "y":
                print("Your map is from 1861 to 1870.")
            if answer.lower() == "n":
                print("Mexico is:")
                print("A - Spain")
                print("B - Massive")
                print("C - Normal sized")
                answer = input("Input Answer > ")
            else:
                print("error")

                if answer.lower() == "a":
                    print("Your map is from 1815 to 1821.")
                if answer.lower() == "b":
                    print("The Netherlands is:")
                    print("A - Big")
                    print("B - Normal sized")
                    answer = input("Input Answer > ")

                    if answer == "a":
                        print("Your map is from 1821 to 1830.")
                    if answer == "b":
                        print("Your map is from 1830 to 1847.")
                if answer.lower == "c":
                    print("Does the Orange Free State exist? Y/N")
                    answer = input("Input Answer > ")

                    if answer == "y":
                        print("Your map is from 1855 to 1861.")
                    if answer == "n":
                        print("Your map is from 1848 to 1855.")
