import keyring

def main():
    print("KEYRING EXAMPLE: retrieve username & password")

    service_id = "name_of_app"
    usernameKey = keyring.get_password(service_id, "username")
    passwordKey = keyring.get_password(service_id, usernameKey)

    print("service_id  = " + str(service_id))
    print("usernameKey = " + str(usernameKey))
    print("passwordKey = " + str(passwordKey))

    print("DONE!")

if __name__ == "__main__":
    main()