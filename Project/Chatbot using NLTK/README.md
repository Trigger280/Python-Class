                                     Documentation for Chatbot: ROBO
#Overview
---------------------------------
This project involves building a chatbot called Robo, which interacts with users by answering queries about chatbots or general text input. The chatbot leverages Natural Language Processing (NLP) techniques to understand and respond to user input, focusing on keyword matching and semantic similarity.

------------------------------
#Features:
------------------------------
Greeting Recognition:
Detects and responds to simple greetings like "hi", "hello", or "what's up".
Contextual Responses:
Uses a corpus-based approach to provide responses relevant to the user’s input.
Fallback Handling:
Responds with a default message when unable to understand the input.
Exit Commands:
Recognizes user inputs like "bye" or "thank you" to terminate the conversation politely.

----------------------------------
#System Requirements:
----------------------------------
Python 3.x
Libraries:
        io
        random
        string
        warnings
        nltk (Natural Language Toolkit)
        sklearn (scikit-learn for TfidfVectorizer and cosine similarity)

---------------------------------
#Implementation Details:
---------------------------------
@1. Preprocessing:
The chatbot uses tokenization and lemmatization for preprocessing:

Tokenization: Splits the text into sentences and words.
Lemmatization: Reduces words to their base forms to normalize input.

Key Functions:
LemTokens: Lemmatizes a list of tokens.
LemNormalize: Tokenizes, converts text to lowercase, removes punctuation, and lemmatizes.
@2. Corpus
The corpus (chatbot.txt) is a plain text file containing data for training the chatbot.
It is read and converted to lowercase for consistency.
@3. Greeting Detection
Predefined greetings (GREETING_INPUTS) are matched using simple keyword matching.
If a match is found, a random greeting response is returned from GREETING_RESPONSES.
@4. TF-IDF and Cosine Similarity
TF-IDF Vectorization: Converts text into numerical features based on term frequency-inverse document frequency.
Cosine Similarity: Measures similarity between user input and sentences in the corpus to find the most relevant response.

Key Steps:
Append user input to the sentence token list.
Compute TF-IDF vectors for the corpus.
Calculate cosine similarity between user input and each sentence in the corpus.
Retrieve the most similar sentence as the response.
@5. Fallback Message
If no relevant response is found (similarity score of 0), the chatbot replies with a default message:
"I am sorry! I don't understand you".
@6. Conversation Handling
The chatbot runs in a while loop, accepting user input until the user types "bye".
Handles "thank you" with an acknowledgment response.

----------------------------------
Key Functions:
----------------------------------
greeting(sentence)

Input: User sentence
Output: A greeting response if a match is found; otherwise, None.
response(user_response)

Input: User query
Output: Best-matching response from the corpus or a fallback message.

--------------------------
Usage:
--------------------------
Run the script in a Python environment.
Interact with the chatbot by typing queries.
Type "bye" to exit the conversation.

---------------------------------------------------------------------------------------------------
                                         Sample Conversation  
---------------------------------------------------------------------------------------------------        
plaintext
Copy code
ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!
User: Hello
ROBO: hi there
User: What are chatbots?
ROBO: Chatbots are programs designed to simulate conversation with human users.
User: Thanks
ROBO: You are welcome..
