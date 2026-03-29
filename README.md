# College Helpdesk Chatbot

## Description
This project is a simple college helpdesk chatbot built using Python. It helps users get information about college-related queries such as fees, placements, courses, facilities, and more.

The chatbot uses basic Natural Language Processing (NLP) techniques like TF-IDF and cosine similarity to understand user input and provide relevant answers. If the chatbot is unable to answer a query, it offers the option to connect with a college executive by collecting user details.

---

## Features
- Answers common college-related questions
- Uses NLP for better understanding of user queries
- Handles similar or rephrased questions
- Option to connect with a college executive
- Stores user details for follow-up

---

## Technologies Used
- Python
- Scikit-learn (TF-IDF, Cosine Similarity)

---

## Project Structure
project_folder/
main.py # Runs the chatbot
chatbot.py # Contains NLP logic
file_handler.py # Handles file operations
data.txt # Stores questions and answers
user_details.txt # Stores user contact details (generated)


---

## How to Set Up

### Step 1: Install Python
Make sure Python 3 is installed on your system.

### Step 2: Install Required Library
Run the following command in terminal:
pip install scikit-learn

### Step 3: Download or Clone Repository
git clone <your-repo-link>
cd <your-folder>

---

## How to Run

Run the following command in terminal:
python main.py

---

## How to Use

1. Start the chatbot by running the program.
2. Enter your question in the terminal.
3. The chatbot will respond with the most relevant answer.
4. If the chatbot cannot answer, you can choose to connect with a college executive.
5. Enter your details if prompted.

---

## Example
You: fee structure
Chatbot: The college fee is 1 lakh per year


---

## Limitations
- Works only with predefined dataset
- Limited understanding compared to advanced AI systems
- Accuracy depends on the data provided

---

## Future Improvements
- Add GUI or web interface
- Improve NLP accuracy
- Add voice input support
- Expand dataset for better responses

---

## Conclusion
This project demonstrates a basic implementation of a chatbot using Python and simple NLP techniques. It is suitable for beginners to understand how chatbots work and how user queries can be processed and answered efficiently.