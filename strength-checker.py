password = input("Enter Password: ")

score = 0


if len(password) >= 8:
    score += 1
if len(password) >= 12:
    score += 1

hasUpper = False
hasLower = False
hasDigit = False
hasSpecial = False


for ch in password:
    if ch.isupper():
        hasUpper = True
    elif ch.islower():
        hasLower = True
    elif ch.isdigit():
        hasDigit = True
    else:
        hasSpecial = True


if hasUpper:
    score += 1
if hasLower:
    score += 1
if hasDigit:
    score += 1
if hasSpecial:
    score += 1


if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")


print("\nSuggestions to improve:")
if len(password) < 8:
    print("- Increase length to at least 8 characters")
if not hasUpper:
    print("- Add uppercase letters")
if not hasLower:
    print("- Add lowercase letters")
if not hasDigit:
    print("- Add numbers")
if not hasSpecial:
    print("- Add special characters")