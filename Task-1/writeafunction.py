def is_leap(year):
    leap = False
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    # Write your logic here
    else:
      return leap
year = int(input())
print(is_leap(year))
