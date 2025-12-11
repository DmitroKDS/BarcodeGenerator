# BarcodeGenerator

## About

This is a simple Telegram bot that generates EAN-13 barcodes as PNG images.

You send the bot a 12-digit number → it creates a high-resolution (300 DPI) barcode image and sends it back to you as a file.

## Use

### Requirements

`pip install pyTelegramBotAPI python-barcode pillow`

### How to run
1.	Put your bot token into the code:
`BarcodeGeneratorBot = telebot.TeleBot("YOUR_TELEGRAM_BOT_TOKEN")`

2.	Run the bot:
`python main.py`

3.	In Telegram, send /start, then send any 12-digit number – you’ll get a PNG barcode in response.
