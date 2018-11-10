import keyring

def main():
    print("KEYRING EXAMPLE: store username & password")

    service_id = "name_of_app"
    username   = "user123"
    password   = "pass123"

    #service_id = "telegram_group"
    #username   = "XXXXX"
    #password   = "XXXXX"

    print("service_id = " + str(service_id))
    print("username   = " + str(username))
    print("password   = " + str(password))

    keyring.set_password(service_id, "username", username)
    keyring.set_password(service_id, username, password)

    print("DONE!")

if __name__ == "__main__":
    main()