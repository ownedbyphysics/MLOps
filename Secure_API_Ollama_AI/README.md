# Secure API + Ollama PoC
This is a proof-of-concept (PoC) FastAPI application that integrates with Ollama to generate AI responses using the Mistral model. The API includes a simple API key system with limited credits per key (25 tokens).

📌 Features

FastAPI backend

API key authentication with credit tracking

Integration with Ollama (running locally)

Generates responses using the Mistral model

📌 Setup

Install the required dependencies.

Create a .env file and add your API key.

📌 Run the FastAPI server.


✅ Usage
You can test the API using Postman or by running testAPI.py. The API expects a POST request to the /generate endpoint with a valid API key and a prompt.

📷 Example response:

![image](https://github.com/user-attachments/assets/2826db69-683b-4056-97fa-6ed6f4a939c6)
