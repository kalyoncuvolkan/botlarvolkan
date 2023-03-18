# -*- coding: utf-8 -*-
import pyodbc
from prettytable import PrettyTable
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import pandas as pd


bot = telebot.TeleBot("6152048061:AAG1neo60YyvZzus4nIdKI1Ri3enKfMJnFE")

# Changes list
CHANGES_LIST = [
    '-- Uzak ve Yerinde Destek tipleri eklendi',
    
    '-- Uygulama çalışmayı durdurduğunda yeniden başlatılacak.',
    
    '-- Açık servis kayıtlarındaki listede bulunan çerçeveler kaldırıldı. /merhaba komutu ile menüyü açabilirsin'
    
]

## Uygulama versiyon numarası
APP_VERSION = "v1.130"
# Uygulama başlangıcı
if __name__ == "__main__":
    print(f"Uygulama {APP_VERSION} sürümü başlatıldı. Yapılan son değişiklikleri görmek için /degisiklikler komutunu kullanabilirsin.")
    bot.send_message(chat_id=-991478600, text=f"Uygulama {APP_VERSION} sürümü başlatıldı. Yapılan son değişiklikleri görmek için /degisiklikler komutunu kullanabilirsin.")

# Chatidler 801556203(Mors Dev) 991478600(Mors Prod) Prod Token=6152048061:AAG1neo60YyvZzus4nIdKI1Ri3enKfMJnFE Dev Token=6223959679:AAGs6NBnTqIS2XxVn15GY3HgRU5EQrYciZc
class MssqlConnection(object):
    def __init__(self):
        self.SERVER = 'mssql-101881-0.cloudclusters.net'
        self.PORT = 10158  
        self.UID = 'volkan'
        self.PASSWORD = 'Ww31volser31*'
        self.DATABASE = 'ServiceTimes'

    def connect_mssql(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=%s,%s;'
            'DATABASE=%s;'
            'UID=%s;'
            'PWD=%s' % (self.SERVER, self.PORT, self.DATABASE, self.UID, self.PASSWORD),
            autocommit=True)
        return conn

        
        # SALVO MENÜ
        
    def query1000(self):
        button1 = InlineKeyboardButton("Servis Başlat", callback_data='query1100T')
        button2 = InlineKeyboardButton("Servis Bitir", callback_data='query1201')
        button3 = InlineKeyboardButton("Açık Servisleri Göster", callback_data='query1300')
        button4 = InlineKeyboardButton("Mors için ne yaptım", callback_data='query1301')
        button5 = InlineKeyboardButton("Servis Dashboarda Git", url="https://morsit.link/servisler")
        keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5]])
        bot.send_message(chat_id=-991478600, text="Merhaba Salvo. Hangi işlemi başlatmak istiyorsun ", reply_markup=keyboard)
        
        # SALVO SERVİS AÇILACK FİRMALAR
        
    def query1100T(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            button1 = InlineKeyboardButton("Uzak Destek Başlat", callback_data='query1100R')
            button2 = InlineKeyboardButton("Yerinde Destek Başlat", callback_data='query1100L')
            keyboard = InlineKeyboardMarkup([[button1], [button2]])
            bot.send_message(chat_id=-991478600, text="Lüten servis tipini seçin", reply_markup=keyboard)
            
        cursor.close()
        conn.close()
    
        #YERİNDE SERVİS MENÜ
    
    def query1100L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            button1 = InlineKeyboardButton("Feriye", callback_data='query1101L')
            button2 = InlineKeyboardButton("Emar Sağlık", callback_data='query1102L')
            button3 = InlineKeyboardButton("Fabrika Mimarlık", callback_data='query1103L')
            button4 = InlineKeyboardButton("Aktaç Gıda", callback_data='query1104L')
            button5 = InlineKeyboardButton("Kate Hotel", callback_data='query1106L')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5]])
            bot.send_message(chat_id=-991478600, text="Hangi müşteri için servis başlatıyorsunuz ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()
        
    def query1101L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            button1 = InlineKeyboardButton("Feriye Lokantası", callback_data='query1111L')
            button2 = InlineKeyboardButton("Madera", callback_data='query1112L')
            button3 = InlineKeyboardButton("İstanbul Modern", callback_data='query1113L')
            button4 = InlineKeyboardButton("Diğer", callback_data='query1114L')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4]])
            bot.send_message(chat_id=-991478600, text="Hangi şubesi için kayıt açacaksın ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()    
       
       # SALVO SERVİS AÇMA SORGULARI
        
    def query1111L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # FERİYE LOKANTASI YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Lokantasi', 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye Lokantası için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query1112L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # MADERA YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Madera', 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Madera için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query1113L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # İSTANBUL MODERN YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Istanbul Modern', 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'İstanbul Modern için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query1114L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # FERİYE LOKANTASI YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Diger', 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye`nin sistemde tanımlı olmayan lokasyonu  için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close() 
    
    def query1102L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (2, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Emar Sağlık için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query1103L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (3, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Fabrika Mimarlık için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query1104L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (4, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Aktaç için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query1106L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (6, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Kate Hotel için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()        
        
        #REMOTE SERVİS MENÜ
    
    def query1100R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            button1 = InlineKeyboardButton("Feriye", callback_data='query1101R')
            button2 = InlineKeyboardButton("Emar Sağlık", callback_data='query1102R')
            button3 = InlineKeyboardButton("Fabrika Mimarlık", callback_data='query1103R')
            button4 = InlineKeyboardButton("Aktaç Gıda", callback_data='query1104R')
            button5 = InlineKeyboardButton("Kate Hotel", callback_data='query1106R')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5]])
            bot.send_message(chat_id=-991478600, text="Hangi müşteri için servis başlatıyorsunuz ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()
        
    def query1101R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            button1 = InlineKeyboardButton("Feriye Lokantası", callback_data='query1111R')
            button2 = InlineKeyboardButton("Madera", callback_data='query1112R')
            button3 = InlineKeyboardButton("İstanbul Modern", callback_data='query1113R')
            button4 = InlineKeyboardButton("Diğer", callback_data='query1114R')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4]])
            bot.send_message(chat_id=-991478600, text="Hangi şubesi için kayıt açacaksın ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()    
       
       # SALVO SERVİS AÇMA SORGULARI
        
    def query1111R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # FERİYE LOKANTASI YENİ UZAK SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Lokantasi', 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye Lokantası için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query1112R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # MADERA YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Madera', 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Madera için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query1113R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # İSTANBUL MODERN YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Istanbul Modern', 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'İstanbul Modern için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query1114R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # FERİYE LOKANTASI YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Diger', 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye`nin sistemde tanımlı olmayan lokasyonu  için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close() 
    
    def query1102R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (2, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Emar Sağlık için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query1103R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (3, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Fabrika Mimarlık için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query1104R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (4, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Aktaç için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query1106R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (6, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Kate Hotel için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()
        
        # SALVO SERVİS KAPAMA SORGULARI
        
    def query1201(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()

        # açık kayıt kontrolü
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count == 0:
            # açık servis kaydı yok, hata mesajı gönder
            bot.send_message(-991478600, 'Açık bir servis kaydınız bulunmuyor.')
        else:
            # açık servis kaydı var, update işlemi yap
            query1 = "UPDATE ServiceRecords " \
                     "SET ServiceEnd = DATEADD(HOUR, 3, GETDATE()) " \
                     "WHERE StaffId = 1 AND ServiceEnd IS NULL;"
            cursor.execute(query1)
            conn.commit()

            # ikinci sorgu
            query2 = "SELECT ServiceDuration " \
                     "FROM ServiceRecords " \
                     "WHERE StaffId = 1 " \
                     "AND ServiceStart >= CONVERT(DATE, GETDATE()) " \
                     "AND ServiceEnd IS NOT NULL " \
                     "AND ServiceEnd >= DATEADD(minute, -10, GETDATE());"

            cursor.execute(query2)
            rows = cursor.fetchall()

            # verileri işleme
            if not rows:
                bot.send_message(-991478600, 'Açık bir servis kaydınız bulunmuyor.')
            else:
                for row in rows:
                    print(row)

                # telegram mesajı gönderme
                message = f'Servis kaydı sona erdi, {row[0]} dakika servis verilerek servis kaydı sonlanmıştır.'
                bot.send_message(-991478600, message)

            cursor.close()
            conn.close()


        # SALVO AÇIK SERVİSLERİ LİSTELE
        
    
    
    def query1300(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 1 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count == 0:
            # açık servis kaydı yok, mesaj gönder
            bot.send_message(-991478600, 'Açık servis kaydınız bulunmuyor.')
        else:
            # açık servis kaydı var, tabloyu oluşturup mesaj gönder
            query = "SELECT sr.Id, " \
                    "CONVERT(varchar(5), sr.ServiceStart, 101) + ' ' + CONVERT(varchar(5), sr.ServiceStart, 108) AS 'Başlangıç', " \
                    "c.CustomerName AS 'Müşteri' " \
                    "FROM ServiceRecords sr " \
                    "JOIN Customers c ON sr.CustomerId = c.Id " \
                    "WHERE sr.StaffId = 1 AND sr.ServiceEnd IS NULL;"
            cursor.execute(query)
            rows = cursor.fetchall()
            headers = [i[0] for i in cursor.description]
            table = PrettyTable(headers)
            for row in rows:
                table.add_row(row)
            bot.send_message(-991478600, f'```\n{table}\n```', parse_mode='MarkdownV2')
     
    def query1301(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
            
        query = "SELECT st.Firstname, c.CustomerName, CONVERT(VARCHAR(10), sr.ServiceDuration) + ' Dakika' AS ServiceDuration " \
                "FROM ServiceRecords sr " \
                "INNER JOIN Staff st ON sr.StaffId = st.StaffId " \
                "INNER JOIN Customers c ON sr.CustomerId = c.Id " \
                "WHERE sr.StaffId = 1 AND CONVERT(DATE, sr.ServiceEnd) = CONVERT(DATE, GETDATE()) " \
                "ORDER BY st.Firstname, c.CustomerName, sr.ServiceDuration;"
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [i[0] for i in cursor.description]
        table = PrettyTable(headers)
        table.header = False  # Başlıkları kaldır
        table.border = False  # Kenarlıkları kaldır
        if not rows:
            bot.send_message(-991478600, "Sistemimizde bugün için bir servis kaydın yok. Acaba tüm gün yeni bir hobinin mi peşinde koştun?")
        else:
            for row in rows:
                table.add_row(row)
            bot.send_message(-991478600, f'```\n{table}\n```', parse_mode='MarkdownV2')
        cursor.close()
        conn.close() 
            
            
            
        # VOLKAN ANA MENÜ
        
    def query5000(self):
        button1 = InlineKeyboardButton("Servis Başlat", callback_data='query5100T')
        button2 = InlineKeyboardButton("Servis Bitir", callback_data='query5201')
        button3 = InlineKeyboardButton("Açık Servisleri Göster", callback_data='query5300')
        button4 = InlineKeyboardButton("Mors için ne yaptım", callback_data='query5301')
        button5 = InlineKeyboardButton("Servis Dashboarda Git", url="https://morsit.link/servisler")
        keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5]])
        bot.send_message(chat_id=-991478600, text="Merhaba Volkan. Hangi işlemi başlatmak istiyorsun ", reply_markup=keyboard)
        
        # VOLKAN SERVİS TİPİ SEÇME MENÜSÜ
        
    def query5100T(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # AÇIK SERVİS VARMI BAK
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            button1 = InlineKeyboardButton("Uzak Destek Başlat", callback_data='query5100R')
            button2 = InlineKeyboardButton("Yerinde Destek Başlat", callback_data='query5100L')
            keyboard = InlineKeyboardMarkup([[button1], [button2]])
            bot.send_message(chat_id=-991478600, text="Lüten servis tipini seçin", reply_markup=keyboard)
            
        cursor.close()
        conn.close()
    
        #YERİNDE SERVİS MENÜ
    
    def query5100L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # AÇIK SERVİS VARMI BAK
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            button1 = InlineKeyboardButton("Feriye", callback_data='query5101L')
            button2 = InlineKeyboardButton("Emar Sağlık", callback_data='query5102L')
            button3 = InlineKeyboardButton("Fabrika Mimarlık", callback_data='query5103L')
            button4 = InlineKeyboardButton("Aktaç Gıda", callback_data='query5104L')
            button5 = InlineKeyboardButton("Kate Hotel", callback_data='query5106L')
            button6 = InlineKeyboardButton("Valente Tekstil", callback_data='query5105L')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5, button6]])
            bot.send_message(chat_id=-991478600, text="Hangi müşteri için yerinde servis başlatıyorsunuz ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()

# FERİYE ŞUBE SEÇİMİ
        
    def query5101L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # AÇIK SERVİS VARMI BAK
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            button1 = InlineKeyboardButton("Feriye Lokantası", callback_data='query5111L')
            button2 = InlineKeyboardButton("Madera", callback_data='query5112L')
            button3 = InlineKeyboardButton("İstanbul Modern", callback_data='query5113L')
            button4 = InlineKeyboardButton("Diğer", callback_data='query5114L')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4]])
            bot.send_message(chat_id=-991478600, text="Hangi şubesi için kayıt açacaksın ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()    
       
       # VOLKAN FERİYE ŞUBESİ İÇİN YEREL SERVİS AÇAR
        
    def query5111L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # FERİYE LOKANTASI YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Lokantasi', 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye Lokantası için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()

        # VOLKAN FERİYE MADERA ŞUBESİ İÇİN YEREL SERVİS AÇAR

    def query5112L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # MADERA YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Madera', 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Madera için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()
        
       # VOLKAN FERİYE ISTANBUL MODERN ŞUBESİ İÇİN YEREL SERVİS AÇAR 
        
    def query5113L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # İSTANBUL MODERN YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Istanbul Modern', 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'İstanbul Modern için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()
        
        # VOLKAN FERİYE TANIMSIZ ŞUBESİ İÇİN YEREL SERVİS AÇAR
        
    def query5114L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # FERİYE LOKANTASI YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Diger', 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye`nin sistemde tanımlı olmayan lokasyonu  için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close() 
    
        # VOLKAN EMAR İÇİN YEREL SERVİS AÇAR
    
    def query5102L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (2, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Emar Sağlık için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()
        
        # VOLKAN FABRİKA İÇİN YEREL SERVİS AÇAR
        
    def query5103L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (3, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Fabrika Mimarlık için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()

        # VOLKAN AKTAÇ İÇİN YEREL SERVİS AÇAR

    def query5104L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (4, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Aktaç için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()

        # VOLKAN VALENTE İÇİN YEREL SERVİS AÇAR

    def query5105L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (5, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Valente için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()

        # VOLKAN KATE HOTEL İÇİN YEREL SERVİS AÇAR

    def query5106L(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (6, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Local');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Kate Hotel için yerinde servis kaydı açıldı')
        cursor.close()
        conn.close()        
        
        # VOLKAN REMOTE SERVİS MENÜ
    
    def query5100R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            button1 = InlineKeyboardButton("Feriye", callback_data='query5101R')
            button2 = InlineKeyboardButton("Emar Sağlık", callback_data='query5102R')
            button3 = InlineKeyboardButton("Fabrika Mimarlık", callback_data='query5103R')
            button4 = InlineKeyboardButton("Aktaç Gıda", callback_data='query5104R')
            button5 = InlineKeyboardButton("Kate Hotel", callback_data='query5106R')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5]])
            bot.send_message(chat_id=-991478600, text="Hangi müşteri için uzaktan servis başlatıyorsunuz ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()
        
        # VOLKAN FERİYE UZAKTAN SERVİS MENÜSÜ
        
    def query5101R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            button1 = InlineKeyboardButton("Feriye Lokantası", callback_data='query5111R')
            button2 = InlineKeyboardButton("Madera", callback_data='query5112R')
            button3 = InlineKeyboardButton("İstanbul Modern", callback_data='query5113R')
            button4 = InlineKeyboardButton("Diğer", callback_data='query5114R')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4]])
            bot.send_message(chat_id=-991478600, text="Hangi şubesi için kayıt açacaksın ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()    
       
       # VOLKAN FERİYE LOKANTASI ŞUBESİ İÇİN UZAKTAN SERVİS AÇAR
        
    def query5111R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # FERİYE LOKANTASI YENİ UZAK SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Lokantasi', 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye Lokantası için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()

        # VOLKAN FERİYE MADERA ŞUBESİ İÇİN UZAKTAN SERVİS AÇAR

    def query5112R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # MADERA YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Madera', 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Madera için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()
        
        # VOLKAN FERİYE İSTANBUL MODERN ŞUBESİ İÇİN UZAKTAN SERVİS AÇAR
        
    def query5113R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # İSTANBUL MODERN YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Istanbul Modern', 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'İstanbul Modern için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query5114R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # FERİYE LOKANTASI YENİ YERİNDE SERVİS KAYDI EKLER
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Diger', 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye`nin sistemde tanımlı olmayan lokasyonu  için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close() 
    
    # VOLKAN EMAR İÇİN UZAKTAN SERVİS AÇAR
    
    def query5102R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (2, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Emar Sağlık için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()
        
        # VOLKAN FABRİKA İÇİN UZAKTAN SERVİS AÇAR
        
    def query5103R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (3, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Fabrika Mimarlık için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()

        # VOLKAN AKTAÇ İÇİN UZAKTAN SERVİS AÇAR

    def query5104R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (4, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Aktaç için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()

        # VOLKAN KATE İÇİN UZAKTAN SERVİS AÇAR

    def query5106R(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count > 0:
            # açık servis kaydı var, hata mesajı gönder
            bot.send_message(-991478600, 'Açık servis kaydınızı sonlandırmadan yeni kayıt açamazsınız.')
        else:
            # yeni servis kaydı ekle
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes, ServiceTypes) " \
                           "VALUES (6, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL, 'Remote');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Kate Hotel için uzaktan servis kaydı açıldı')
        cursor.close()
        conn.close()        
        
        # VOLKAN SERVİS KAPAMA SORGULARI
        
    def query5201(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()

        # açık kayıt kontrolü
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count == 0:
            # açık servis kaydı yok, hata mesajı gönder
            bot.send_message(-991478600, 'Açık bir servis kaydınız bulunmuyor.')
        else:
            # açık servis kaydı var, update işlemi yap
            query1 = "UPDATE ServiceRecords " \
                     "SET ServiceEnd = DATEADD(HOUR, 3, GETDATE()) " \
                     "WHERE StaffId = 2 AND ServiceEnd IS NULL;"
            cursor.execute(query1)
            conn.commit()

            # ikinci sorgu
            query2 = "SELECT ServiceDuration " \
                     "FROM ServiceRecords " \
                     "WHERE StaffId = 2 " \
                     "AND ServiceStart >= CONVERT(DATE, GETDATE()) " \
                     "AND ServiceEnd IS NOT NULL " \
                     "AND ServiceEnd >= DATEADD(minute, -10, GETDATE());"

            cursor.execute(query2)
            rows = cursor.fetchall()

            # verileri işleme
            if not rows:
                bot.send_message(-991478600, 'Açık bir servis kaydınız bulunmuyor.')
            else:
                for row in rows:
                    print(row)

                # telegram mesajı gönderme
                message = f'Servis kaydı sona erdi, {row[0]} dakika servis verilerek servis kaydı sonlanmıştır.'
                bot.send_message(-991478600, message)

            cursor.close()
            conn.close()
    
    

        # VOLKAN SERVİS KAYITLARI
        
    
    
    def query5300(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
        # kontrol koşulu
        check_query = "SELECT COUNT(*) FROM ServiceRecords WHERE StaffId = 2 AND ServiceEnd IS NULL;"
        cursor.execute(check_query)
        count = cursor.fetchone()[0]
        if count == 0:
            # açık servis kaydı yok, mesaj gönder
            bot.send_message(-991478600, 'Açık servis kaydınız bulunmuyor.')
        else:
            # açık servis kaydı var, tabloyu oluşturup mesaj gönder
            query = "SELECT sr.Id, " \
                    "CONVERT(varchar(5), sr.ServiceStart, 101) + ' ' + CONVERT(varchar(5), sr.ServiceStart, 108) AS 'Başlangıç', " \
                    "c.CustomerName AS 'Müşteri' " \
                    "FROM ServiceRecords sr " \
                    "JOIN Customers c ON sr.CustomerId = c.Id " \
                    "WHERE sr.StaffId = 2 AND sr.ServiceEnd IS NULL;"
            cursor.execute(query)
            rows = cursor.fetchall()
            headers = [i[0] for i in cursor.description]
            table = PrettyTable(headers)
            table.align = 'l'  # Sütun hizalamasını sol tarafa ayarla
            table.border = False  # Kenarlıkları kaldır
            for row in rows:
                table.add_row(row)
            data_rows = table.get_string(header=False, border=False).strip()
            header_row = table.get_string(fields=headers).strip()
            
            # Verileri ve başlıkları ayrı ayrı göndererek iki satıra ayır
            header_lines = header_row.splitlines()
            data_lines = data_rows.splitlines()
            # İki satır arasına boşluk ekleyin
            header = header_lines[0]
            data = '\n'.join([data_lines[0], '', '\n'.join(data_lines[1:-1])])
            
            bot.send_message(-991478600, f'{header}\n{data}', parse_mode='MarkdownV2')





    def query5301(self):
        conn = self.connect_mssql()
        cursor = conn.cursor()
            
        query = "SELECT st.Firstname, c.CustomerName, CONVERT(VARCHAR(10), sr.ServiceDuration) + ' Dakika' AS ServiceDuration " \
                "FROM ServiceRecords sr " \
                "INNER JOIN Staff st ON sr.StaffId = st.StaffId " \
                "INNER JOIN Customers c ON sr.CustomerId = c.Id " \
                "WHERE sr.StaffId = 2 AND CONVERT(DATE, sr.ServiceEnd) = CONVERT(DATE, GETDATE()) " \
                "ORDER BY st.Firstname, c.CustomerName, sr.ServiceDuration;"
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [i[0] for i in cursor.description]
        table = PrettyTable(headers)
        table.header = False  # Başlıkları kaldır
        table.border = False  # Kenarlıkları kaldır
        if not rows:
            bot.send_message(-991478600, "Sistemimizde bugün için bir servis kaydın yok. Acaba tüm gün yeni bir hobinin mi peşinde koştun?")
        else:
            for row in rows:
                table.add_row(row)
            bot.send_message(-991478600, f'```\n{table}\n```', parse_mode='MarkdownV2')
        cursor.close()
        conn.close()


# BOTUMUZ MESAJLARI BURADA DİNLİYOR

@bot.message_handler(commands=['degisiklikler'])
def send_changes(message):
    changes_text = '\n'.join(CHANGES_LIST)
    bot.send_message(message.chat.id, changes_text)

def query_handler(query_name, query_func, allowed_users):
    def handler(call):
        username = call.from_user.username
        if username in allowed_users:
            query_func()
        else:
            bot.answer_callback_query(call.id, text="Bu işlemi yapmak için yetkiniz yok.")
    bot.callback_query_handler(func=lambda call: call.data == query_name)(handler)


@bot.message_handler(commands=['merhaba'])
def start_handler(message):
    username = message.from_user.username
    text = message.text.lower()
    if username == "salvoromi":
        if "merhaba" in text:
            MssqlConnection().query1000()
    elif username == "kalyoncuvolkan":
        if "merhaba" in text:
            MssqlConnection().query5000()
    else:
        bot.reply_to(message, "Kullanıcı adınız sisteme tanımlı değil bu nedenle işlem gerçekleştiremezsiniz.")

# Query handlers
query_handler('query5100T', MssqlConnection().query5100T, ['kalyoncuvolkan'])
query_handler('query5100L', MssqlConnection().query5100L, ['kalyoncuvolkan'])
query_handler('query5100R', MssqlConnection().query5100R, ['kalyoncuvolkan'])
query_handler('query5101L', MssqlConnection().query5101L, ['kalyoncuvolkan'])
query_handler('query5101R', MssqlConnection().query5101R, ['kalyoncuvolkan'])
query_handler('query5102L', MssqlConnection().query5102L, ['kalyoncuvolkan'])
query_handler('query5102R', MssqlConnection().query5102R, ['kalyoncuvolkan'])
query_handler('query5103L', MssqlConnection().query5103L, ['kalyoncuvolkan'])
query_handler('query5103R', MssqlConnection().query5103R, ['kalyoncuvolkan'])
query_handler('query5104L', MssqlConnection().query5104L, ['kalyoncuvolkan'])
query_handler('query5105L', MssqlConnection().query5105L, ['kalyoncuvolkan'])
query_handler('query5104R', MssqlConnection().query5104R, ['kalyoncuvolkan'])
query_handler('query5106L', MssqlConnection().query5106L, ['kalyoncuvolkan'])
query_handler('query5106R', MssqlConnection().query5106R, ['kalyoncuvolkan'])
query_handler('query5111L', MssqlConnection().query5111L, ['kalyoncuvolkan'])
query_handler('query5111R', MssqlConnection().query5111R, ['kalyoncuvolkan'])
query_handler('query5112L', MssqlConnection().query5112L, ['kalyoncuvolkan'])
query_handler('query5112R', MssqlConnection().query5112R, ['kalyoncuvolkan'])
query_handler('query5113L', MssqlConnection().query5113L, ['kalyoncuvolkan'])
query_handler('query5113R', MssqlConnection().query5113R, ['kalyoncuvolkan'])
query_handler('query5114L', MssqlConnection().query5114L, ['kalyoncuvolkan'])
query_handler('query5114R', MssqlConnection().query5114R, ['kalyoncuvolkan'])
query_handler('query5201', MssqlConnection().query5201, ['kalyoncuvolkan'])
query_handler('query5300', MssqlConnection().query5300, ['kalyoncuvolkan'])
query_handler('query5301', MssqlConnection().query5301, ['kalyoncuvolkan'])
query_handler('query1100T', MssqlConnection().query1100T, ['salvoromi'])
query_handler('query1100R', MssqlConnection().query1100R, ['salvoromi'])
query_handler('query1100L', MssqlConnection().query1100L, ['salvoromi'])
query_handler('query1101L', MssqlConnection().query1101L, ['salvoromi'])
query_handler('query1101R', MssqlConnection().query1101R, ['salvoromi'])
query_handler('query1102L', MssqlConnection().query1102L, ['salvoromi'])
query_handler('query1102R', MssqlConnection().query1102R, ['salvoromi'])
query_handler('query1103L', MssqlConnection().query1103L, ['salvoromi'])
query_handler('query1103R', MssqlConnection().query1103R, ['salvoromi'])
query_handler('query1104L', MssqlConnection().query1104L, ['salvoromi'])
query_handler('query1104R', MssqlConnection().query1104R, ['salvoromi'])
query_handler('query1106L', MssqlConnection().query1106L, ['salvoromi'])
query_handler('query1106R', MssqlConnection().query1106R, ['salvoromi'])
query_handler('query1111L', MssqlConnection().query1111L, ['salvoromi'])
query_handler('query1111R', MssqlConnection().query1111R, ['salvoromi'])
query_handler('query1112L', MssqlConnection().query1112L, ['salvoromi'])
query_handler('query1112R', MssqlConnection().query1112R, ['salvoromi'])
query_handler('query1113L', MssqlConnection().query1113L, ['salvoromi'])
query_handler('query1113R', MssqlConnection().query1113R, ['salvoromi'])
query_handler('query1114L', MssqlConnection().query1114L, ['salvoromi'])
query_handler('query1114R', MssqlConnection().query1114R, ['salvoromi'])
query_handler('query1201', MssqlConnection().query1201, ['salvoromi'])
query_handler('query1300', MssqlConnection().query1300, ['salvoromi'])
query_handler('query1301', MssqlConnection().query1301, ['salvoromi'])

bot.polling()









