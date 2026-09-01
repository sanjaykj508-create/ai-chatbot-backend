\# AI Chatbot Backend



A multi-turn AI chatbot backend built with \*\*FastAPI\*\* and \*\*Google Gemini API\*\*.



\## Features



\* Real AI responses using Google Gemini

\* Multi-turn conversation support

\* Conversation history using `conversation\_id`

\* Context window management

\* Keeps the latest 10 messages

\* System prompt for consistent chatbot behavior

\* Retry mechanism for temporary API failures

\* FastAPI Swagger API documentation

\* API key stored using an environment variable



\## Technologies



\* Python

\* FastAPI

\* Uvicorn

\* Google Gemini API

\* Google GenAI Python SDK



\## Project Structure



```text

ai-chatbot-backend/

├── app.py

├── requirements.txt

├── .gitignore

└── README.md

```



\## Setup



\### 1. Clone the repository



```bash

git clone https://github.com/sanjaykj508-create/ai-chatbot-backend.git

cd ai-chatbot-backend

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the virtual environment



Windows PowerShell:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\## API Key Setup



Create a Gemini API key and store it as an environment variable.



Windows PowerShell:



```powershell

$env:GEMINI\_API\_KEY="YOUR\_API\_KEY"

```



Do not commit or share your API key.



\## Run the Application



```bash

uvicorn app:app --reload

```



The API will run at:



```text

http://127.0.0.1:8000

```



Swagger documentation:



```text

http://127.0.0.1:8000/docs

```



\## Chat Endpoint



The chatbot uses:



```text

GET /chat

```



Parameters:



```text

conversation\_id

message

```



Example:



```text

/chat?conversation\_id=sanjay001\&message=Hello

```



\## Multi-Turn Conversation



The `conversation\_id` identifies a conversation.



Example:



```text

Turn 1:

My name is Sanjay and I am learning Python.



Turn 2:

What is my name and what am I learning?

```



The chatbot can use the previous conversation context to answer the second question.



\## Context Window Management



To prevent the conversation history from growing indefinitely, the application keeps only the \*\*latest 10 messages\*\*.



```python

MAX\_MESSAGES = 10

history = history\[-MAX\_MESSAGES:]

```



Older messages are removed from the context sent to the Gemini API.



\## Testing



The chatbot was tested with a multi-turn conversation using the same `conversation\_id`.



Example:



1\. Introduced the user's name and learning topic.

2\. Asked the chatbot to recall the information.

3\. Asked about the assistant's role.

4\. Asked for a Python learning roadmap.

5\. Asked for a personalized Python learning plan.



The chatbot successfully maintained conversation context.



\## Security



The Gemini API key is not stored in the source code.



The `.gitignore` file excludes:



```text

.env

venv/

\_\_pycache\_\_/

\*.pyc

```



Never upload API keys or other secrets to GitHub.



\## Author



Sanjay Kj



