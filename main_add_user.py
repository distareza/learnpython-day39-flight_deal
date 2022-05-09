import requests
import my_configuration
import data_manager

print("Welcome to Reza's Flight Club")
print("We find the best flight deals and email to you")
user_first_name = input("What is your first name ?")
user_last_name = input("What is your last name ?")
user_email = input("What is your email?")
confirmation_mail = input("Type your email again.")

body = {
    "user": {
        "firstName": user_first_name,
        "lastName": user_last_name,
        "email": user_email
    }
}
bearer_headers = {
    "Authorization": f"Bearer {my_configuration.sheet_token}"
}

if user_email == confirmation_mail:
    existing_data = requests.get(data_manager.SHEETY_USERS_ENDPOINT, headers=bearer_headers)
    existing_user = [ item["email"].lower() for item in existing_data.json()["users"] ]
    if user_email.lower() in existing_user:
        print(f"Sorry, email {user_email} is already been registered")
        exit(1)

    response = requests.post(url=data_manager.SHEETY_USERS_ENDPOINT, json=body, headers=bearer_headers)
    response.raise_for_status()
    print("Your email is successfully added, look forwards to send you the best flight deals")


