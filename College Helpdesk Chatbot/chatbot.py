from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_response(user_input, data):
    user_input = user_input.lower()

    questions = list(data.keys())

    # Combine dataset questions + user input
    all_texts = questions + [user_input]

    # Convert text to vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_texts)

    # Compare similarity
    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]

    # Threshold (tune this if needed)
    if best_score > 0.3:
        best_question = questions[best_match_index]
        return data[best_question], False
    else:
        return "Sorry, I couldn't understand your question.", True
