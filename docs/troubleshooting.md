# Troubleshooting Guide

## Translation Issues
- **Problem**: Translation nodes (`Translate uk-en`, `Translate en-uk`) fail.
- **Solution**: Check the Hugging Face API Token and ensure the models (`Helsinki-NLP/opus-mt-uk-en`, `Helsinki-NLP/opus-mt-en-uk`) are accessible.
- **Result**: Translations applied correctly.

## MongoDB Atlas Logging Issues
- **Problem**: History not logged in `chatbot_db.chat_history`.
- **Solution**: Verify the Connection String, ensure Network Access allows your IP, and check input data (`user_query`, `answer`).
- **Result**: History successfully logged in MongoDB Atlas.

## Slack Notification Issues
- **Problem**: Notifications not sent to `#support-bot` or `#bot-errors`.
- **Solution**: Verify Webhook URLs, ensure the Slack app has permissions, and check input data.
- **Result**: Notifications sent to Slack channels.

## Telegram Response Issues
- **Problem**: No response sent to Telegram.
- **Solution**: Check Telegram Bot Token, ensure `Process AI Response` outputs a valid `message`, and verify Internet connectivity.
- **Result**: Responses sent to Telegram.