import telebot
from telebot import types
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image
from io import BytesIO

BarcodeGeneratorBot = telebot.TeleBot('')

@BarcodeGeneratorBot.message_handler(commands=['start'])
def StartMessage(Message):
    BarcodeGeneratorBot.send_message(Message.chat.id, f"Привіт ✌️. Напиши штрих код для создания картинки")

@BarcodeGeneratorBot.message_handler(content_types=['text'])
def GetText(Message):
    Barcode =  Message.text
    BarcodeGeneratorBot.delete_message(Message.chat.id, Message.message_id)

    try:
        if len(Barcode)!=12:
            raise ValueError("Штрих-код должен содержать ровно 12 цифр.")
        
        BarcodeImage = EAN13(Barcode, writer=ImageWriter())

        BarcodeFileIO = BytesIO()
        BarcodeImage.write(BarcodeFileIO)
        BarcodeFileIO.seek(0)

        BarcodeImage = Image.open(BarcodeFileIO)
        
        BarcodeImage = BarcodeImage.resize((1000, int(1000 / BarcodeImage.width * BarcodeImage.height)), Image.LANCZOS)
        
        BarcodeFileIO = BytesIO()
        BarcodeImage.save(BarcodeFileIO, format='PNG', dpi=(300, 300))
        BarcodeFileIO.seek(0)

        BarcodeGeneratorBot.send_document(Message.chat.id, BarcodeFileIO, visible_file_name=f'Barcode.png')
        BarcodeGeneratorBot.send_message(Message.chat.id, f"Штрих код {Barcode}")
    except:
        pass

BarcodeGeneratorBot.infinity_polling()
