"""try:
    birth_year = int(input('Enter your birth year: '))
    age = 2025 - birth_year
    risk = birth_year/age
except ValueError:
    print("Birth year must be an number")
except ZeroDivisionError:
    print("The birth year cannor be 2025 as it becomes zero")"""

try:
    birth_year = float(input('Enter your birth year: '))
    age = 2025-birth_year
    risk = birth_year/ age
except:
    print("either the age is zero or the birth_year is not a number")


try:
  birth_year = float(input('enter  your birth year: '))
  age = 2025-birth_year
  risk = birth_year/age
except:
  print('either the age is zero or the birth_year is not number')