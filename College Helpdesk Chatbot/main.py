from file_handler import load_data, save_user_details
from chatbot import get_response

def chatbot():
    print("--------------------------------------------------")
    print("🤖 Welcome to College Helpdesk Chatbot")
    print("--------------------------------------------------")

    # 👉 Branding / Highlights
    print("\n✨ You can ask about:")
    print("👉 Placements")
    print("👉 Alumni")
    print("👉 Highest Package")

    data = load_data("data.txt")

    while True:
        user_input = input("\nYou: ")

        response, not_found = get_response(user_input, data)
        print("Chatbot:", response)

        if not_found:
            print("\n For better assistance, you can talk to a college executive.")

            connect = input("Do you want to connect with an executive? (yes/no): ").lower()

            if connect == "yes":
                print("\nPlease fill your details:")

                name = input("Enter your name: ")
                phone = input("Enter your phone number: ")
                email = input("Enter your email: ")

                details = f"Name: {name}, Phone: {phone}, Email: {email}"

                save_user_details("user_details.txt", details)

                print("\nTHANKS FOR REACHING OUT !!")
                print("HAVE A GREAT DAY .")
                break

        choice = input("\nDo you want to ask another question? (yes/no): ").lower()

        if choice == "no":
            print("\nTHANKS FOR REACHING OUT !!")
            print("HAVE A GREAT DAY .")

            connect = input("\nDo you want to talk to a college executive? (yes/no): ").lower()

            if connect == "yes":
                print("\n Please fill your details:")

                name = input("Enter your name: ")
                phone = input("Enter your phone number: ")
                email = input("Enter your email: ")

                details = f"Name: {name}, Phone: {phone}, Email: {email}"

                save_user_details("user_details.txt", details)

                print("\n Our executive will contact you soon.")

            break


if __name__ == "__main__":
    chatbot()