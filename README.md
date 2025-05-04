# Customer Support Chatbot

## Overview
This project is an automated customer support chatbot built using **n8n.io**. It processes user queries via Telegram, retrieves relevant data from Airtable, translates queries using Hugging Face models, generates responses with FlanT5, logs history in MongoDB Atlas, and sends notifications to Slack. The chatbot is designed to handle multilingual queries (Ukrainian to English and back) and provide seamless support automation.

## Features
- **Telegram Integration**: Receives user queries and sends responses via Telegram.
- **Airtable for RAG**: Retrieves relevant question-answer pairs for context.
- **Hugging Face Translation**: Translates Ukrainian queries to English (`Helsinki-NLP/opus-mt-uk-en`) and responses back to Ukrainian (`Helsinki-NLP/opus-mt-en-uk`).
- **FlanT5 for Response Generation**: Generates answers using the `google/flan-t5-base` model.
- **MongoDB Atlas Logging**: Logs chat history in the cloud for analysis.
- **Slack Notifications**: Notifies the team of responses and errors in dedicated channels.

## Workflow Structure
1. **Telegram Trigger**: Captures user queries from Telegram.
2. **Airtable Search/Record**: Retrieves relevant data for RAG.
3. **Airtable Test**: Validates retrieved data.
4. **Template or AI Rules**: Prepares data for processing.
5. **Translate uk-en (userQuery, Question, Answer)**: Translates inputs to English.
6. **Translate test uk-en**: Combines translated data.
7. **Format RAG Context**: Creates a prompt for AI.
8. **AI (FlanT5)**: Generates a response.
9. **Translate en-uk**: Translates the response back to Ukrainian.
10. **Process AI Response**: Formats the response.
11. **Send Telegram message**: Sends the response to the user.
12. **MongoDB Insert**: Logs the query and response in MongoDB Atlas.
13. **Slack**: Sends notifications to `#support-bot`.
14. **Error Trigger → Send Telegram message (Error) → Slack (Error)**: Handles errors and notifies `#bot-errors`.

## Setup Instructions
### Prerequisites
- n8n.io account (cloud or self-hosted).
- Telegram Bot Token (create via BotFather).
- Airtable account with a base containing question-answer pairs.
- Hugging Face API Token for translation and FlanT5 models.
- MongoDB Atlas account for history logging.
- Slack workspace with an app for Incoming Webhooks.

### Installation
1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/customer-support-chatbot.git
   cd customer-support-chatbot
   ```
2. **Import the Workflow**:
   - Open n8n.io.
   - Import the workflow from `workflow.json` (located in the repository).
3. **Configure Credentials**:
   - **Telegram**: Add your Bot Token and Chat ID.
   - **Airtable**: Add your API Key and Base ID.
   - **Hugging Face**: Add your API Token for translation and FlanT5 models.
   - **MongoDB Atlas**: Add your Connection String (e.g., `mongodb+srv://user:password@cluster0.mongodb.net/chatbot_db`).
   - **Slack**: Add Webhook URLs for `#support-bot` and `#bot-errors` channels.
4. **Test the Workflow**:
   - Send a test query via Telegram (e.g., "як відстежити моє замовлення?").
   - Verify the response in Telegram, history in MongoDB Atlas, and notifications in Slack.

## Usage
- Send a query via Telegram to the bot.
- The bot retrieves relevant data, translates the query, generates a response, and sends it back.
- History is logged in MongoDB Atlas (`chatbot_db.chat_history`).
- Notifications are sent to Slack channels `#support-bot` (responses) and `#bot-errors` (errors).

## Troubleshooting
See `docs/troubleshooting.md` for common issues and solutions.

## Technologies Used
- **n8n.io**: Workflow automation.
- **Telegram**: User interaction.
- **Airtable**: Data storage for RAG.
- **Hugging Face**: Translation and AI response generation.
- **MongoDB Atlas**: Cloud-based history logging.
- **Slack**: Team notifications.

## Future Improvements
- Add support for more languages.
- Implement vector search in MongoDB Atlas for advanced RAG.
- Add user feedback collection via Telegram buttons.

## Contact
For questions or collaboration, reach out to [your-email@example.com](mailto:your-email@example.com).