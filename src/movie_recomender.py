# LD 1st Personal Project, Movie Recomender
import time
import os
import csv

# REQUIREMENTS
    # A main function that runs the program and shows a persistent menu.
    # A parser function to load and normalize the provided movie list (CSV) into structured records.
    # Separate filter functions for: genre, director, actor(s), and length.
    # A function that combines selected filters (AND logic by default) and returns matching movies.
    # A function to pretty-print results and a function to print the full movie list.
    # Input validation and helpful error messages; handle missing or malformed movie records gracefully.
    # Allow interactive entry of filter values and length ranges (min/max or comparator).

# HINTS
    # Normalize text to lower-case and trim whitespace for case-insensitive matching.
    # Store multi-valued fields (genres, actors) as lists and match if any element contains the query term.
    # Implement length filtering with min and/or max values (support <, > comparators optionally).
    # If zero matches, suggest relaxing or removing one filter.
    # Provide a small sample movies file in the repo and include unit tests for filter logic.

# FILTER RULES CLARIFICATION
    # Matching is case-insensitive.
    # For genres and actors, match if any element contains the query substring (trim whitespace).
    # Length filter accepts min and/or max (integers). If only one provided, use it as bound.
    # Combine multiple filters using logical AND (movie must satisfy every selected filter).
    # If a movie is missing a field, it does not match a filter for that field.


# CODE
def type_print(string, delay = 0.06):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function. Displays menu. Options are: Search, Print EVERYTHING, Exit. Has inner functions
def main():
    movies_found = []

    # Filter funtion for Genre. This will ask for a genre like "romance" or sm and grab everything that has the genre "Romance" IN IT
    def find_genre():
        nonlocal movies_found

        genre = input("What is the genre you are looking for (ex: 'Science Fiction,' 'Romance,' 'Drama')\n").strip().lower()
        if not movies_found:
            try:
                with open("P:\DeLong, Lizzie\Personal_Portfolio\docs\Movies_list.csv", "r") as csv_file:
                    content = csv.reader(csv_file)
                    headers = next(content)
                    for line in content:
                        if genre in line[2].lower():
                            movies_found.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
            except:
                print("Something went wrong with reading the file")
        else:
            # not first time filtering and need to get stuff to futher filter
            for item in movies_found:
                if genre not in item['Genre'].lower():
                    # It does not pass the director parameter
                    movies_found.remove(item)

    # Filter for Director. This will take in a name (or part of a name) and find every movie with the name in the DIRECTOR'S name
    def find_director():
        nonlocal movies_found

        director = input("What is the name for directors you want to search for (ex: 'Chris,' 'John')\n").strip().lower()
        if not movies_found:
            # any previous filters have not given me an already narrowed down list
            try:
                with open("P:\DeLong, Lizzie\Personal_Portfolio\docs\Movies_list.csv", "r") as csv_file:
                    content = csv.reader(csv_file)
                    headers = next(content)
                    for line in content:
                        if director in line[1].lower():
                            movies_found.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
            except:
                print("Something went wrong with reading the file")
        else:
            # not first time filtering and need to get stuff to futher filter
            for item in movies_found:
                if director not in item['Director'].lower():
                    # It does not pass the director parameter
                    movies_found.remove(item)

    # Filter for Actor. Same as director but look in the ACTOR'S name
    def find_actor():
        nonlocal movies_found

        actor = input("What is the name of the actor you wish to filter for (ex: 'Chris,' 'Ryan')\n").strip().lower()
        if not movies_found:
            try:
                with open("P:\DeLong, Lizzie\Personal_Portfolio\docs\Movies_list.csv", "r") as csv_file:
                    content = csv.reader(csv_file)
                    headers = next(content)
                    for line in content:
                        if actor in line[5].lower():
                            movies_found.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
            except:
                print("Something went wrong reading the file")
        else:
            for item in movies_found:
                if actor not in item['Notable Actors'].lower():
                    movies_found.remove(item)

    # Filter for length. Take in a min and/or max and find the movies that fit in the range. IF no min given, min = 0. IF no max given, max = 200 (Every movie in CSV is shorter than that)
    def length_filter():
        while True:
            type_print("What would you like the minimum length in MINUTES to be (put a space if you don't want a minimum)\n")
            min = input("NOTE: Omit 'minutes'\n").strip().lower()
            if min.isdigit() == True:
                min = float(min)
                break
            elif min == "":
                min = 0
                break
            else:
                print("Invalid input. Try again")
                continue
        while True:
            type_print("What would you like the maximum length in MINUTES to be (put a space if you don't want a maximum)\n")
            max = input("NOTE: Omit 'minutes'\n").strip().lower()
            if max.isdigit() == True:
                max = float(max)
                break
            elif max == '':
                max = 200
                break
            else:
                print("Invalid input. Try again")
                continue
        if not movies_found:
            try:
                with open("P:\DeLong, Lizzie\Personal_Portfolio\docs\Movies_list.csv", "r") as csv_file:
                    content = csv.reader(csv_file)
                    headers = next(content)
                    for line in content:
                        if line[4] > min and line[4] < max:
                            movies_found.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
            except:
                print("Something went wrong reading the file")
        else:
            for item in movies_found:
                if float(item['Length (min)']) < min or float(item['Length (min)']) > max:
                    movies_found.remove(item)

    # Function that is the one asking for the parameters and will use the results from the calling to get the movies that fit all parameters. Return this list that fit parameters
    def find_filters():
        while True:
            type_print("Choose the filters you would like to apply (enter them separated by spaces):\n1) Genre\n2) Director\n3) Actor\n4) Length (min and/or max)\nExample entry: '1 2 4'\n")
            filters = input("Type the numbers for your filters:\n").strip().lower()
            if "1" not in filters and "2" not in filters and "3" not in filters and "4" not in filters:
                print("Invalid input. Please try again")
                continue
            else:
                for item in filters.split(" "):
                    if item == "1":
                        find_genre()
                    if item == "2":
                        find_director()
                    if item == "3":
                        find_actor()
                    if item == "4":
                        length_filter()
                    else:
                        pass
                        # Item was not 1-4 so we skip
                break

    # Function to print very nicely
    def pretty_print():
        nonlocal action # figure out if user filtering or viewing whole freaking thing

        if action == "2":
            # viewing the entire stupid file
            try:
                with open("P:\DeLong, Lizzie\Personal_Portfolio\docs\Movies_list.csv", "r") as csv_file:
                    content = csv.reader(csv_file)
                    headers = next(content)
                    num = 1
                    for line in content:
                        print(f"{num}) {headers[0]}: {line[0]}\n{headers[1]}: {line[1]}\n{headers[2]}: {line[2]}\n{headers[3]}: {line[3]}\n{headers[4]}: {line[4]}\n{headers[5]}: {line[5]}\n")
                        num += 1
            except:
                print("Something went wrong reading the file")
        elif action == "1":
            # only print the found movies list
            if not movies_found:
                type_print("It seems that movies fiting your requested parameters could not be found.\nTry broadening your parameters\n")
            else:
                num = 1
                for line in movies_found:
                    print(f"{num}) Title: {line['Title']}\nDirector: {line['Director']}\nGenre(s): {line['Genre']}\nRating: {line['Rating']}\nLength (minutes): {line['Length (min)']}\nActors: {line['Notable Actors']}\n")
                    num += 1
        else:
            print("Something's wrong :D")

    # main code start
    type_print("Welcome user to a program that will let you search through a catolog of movies!\n")
    while True:
        type_print("What would you like to do:\n1) Search with Parameters\n2) View Entire Movie List\n3) Leave\n")
        action = input("Type the number corresponding to what you want to do:\n").strip().lower()
        if action == "1":
            find_filters()
            print("Movies found:")
            pretty_print()
            time.sleep(5)
            print() # making new lines so that its not all clumped together and is more readable
            print()
        elif action == "2":
            print("Full movie cataloge:")
            pretty_print()
            time.sleep(5)
            print() # making new lines so that its not all clumped together and is more readable
            print()
        elif action == "3":
            print("Thank you for using my program!")
            break
        else:
            print("Invalid input. Please try again")
            continue
