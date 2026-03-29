def load_data(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            question, answer = line.strip().split(":")
            data[question.lower()] = answer
    return data


def save_user_details(filename, details):
    with open(filename, 'a') as file:
        file.write(details + "\n")