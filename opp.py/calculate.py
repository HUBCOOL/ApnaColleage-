score = int(input("Enter your grade:"))

if score >=100:
    grade ="AA"

elif score >=90:
    grade ="A"

elif score >=80:
    grade ="C"

elif score >=70:
    grade ="D"

elif score >=101:
    print("Plz verify your grade with dp")
    exit()

else:
    grade ="F"




print("Grade:",grade)