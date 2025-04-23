print("Enter your age.")
age = int(input())
def age_status(age):
    if age >= 18:
     return("You are an Adult")
    elif age <= 17:
        return("You are a minor")
age_check = age_status(age)
print(age_check)