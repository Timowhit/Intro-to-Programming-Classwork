#Author: Timothy Whitehead

#Purpose: Practice formatting strings.

print("Please enter the following information:")

print()

    # the basic info
first = input("First name: ")
last = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

    # the extra info
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? Y/N")

    # Now print out the ID Card
print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last.upper()}, {first.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print()

# spacing extra info

print(f"Hair: {hair_color:15} Eyes: {eye_color}")
print(f"Month: {month:14} Training: {training}")
print("----------------------------------------")