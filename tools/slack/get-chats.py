# slack_to_db.py

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import sqlite3  # Example: Using SQLite

# Set your Slack OAuth token
slack_token = 'YOUR_OAUTH_TOKEN'
channel_id = 'your_channel_id'  # Replace with the desired channel ID

# Initialize the Slack client
client = WebClient(token=slack_token)

def fetch_messages_from_slack():
    try:
        response = client.conversations_history(channel=channel_id)
        messages = response['messages']
        return messages
    except SlackApiError as e:
        print(f"Error fetching messages: {e.response['error']}")

def insert_messages_into_db(messages):
    conn = sqlite3.connect('slack_messages.db')  # Example: SQLite database
    cursor = conn.cursor()

    for msg in messages:
        text = msg.get('text', '')
        timestamp = msg.get('ts', '')
        user_id = msg.get('user', '')

        # Insert into the database (example query)
        cursor.execute("INSERT INTO messages (text, timestamp, user_id) VALUES (?, ?, ?)",
                       (text, timestamp, user_id))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    messages_from_slack = fetch_messages_from_slack()
    insert_messages_into_db(messages_from_slack)
    print("Messages copied to the database successfully!")
