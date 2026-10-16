import sys

def is_leap_year(year):
    if year % 4 == 0:
        return "leap year"
    else:
        return "not"

if __name__ == "__main__":
    year = int(sys.arg[1])
    print("year is:", is_leap_year(year))