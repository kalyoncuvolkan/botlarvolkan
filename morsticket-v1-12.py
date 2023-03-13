# -*- coding: utf-8 -*-
import pyodbc
from prettytable import PrettyTable
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import pandas as pd


bot = telebot.TeleBot("6152048061:AAG1neo60YyvZzus4nIdKI1Ri3enKfMJnFE")

# Changes list
CHANGES_LIST = [
    '-- Feriye isimli müşteri için şube sistemi eklendi. Feriye müşterisi seçildiğinde şube seçme ekranı gelecek',
    
    '-- Uygulama çalışmayı durdurduğunda yeniden başlatılacak.',
    
    '-- Açık servis kayıtlarındaki listede bulunan çerçeveler kaldırıldı. /merhaba komutu ile menüyü açabilirsin'
    
]

## Uygulama versiyon numarası
APP_VERSION = "v1.120"
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
        button1 = InlineKeyboardButton("Servis Başlat", callback_data='query1100')
        button2 = InlineKeyboardButton("Servis Bitir", callback_data='query1201')
        button3 = InlineKeyboardButton("Açık Servisleri Göster", callback_data='query1300')
        button4 = InlineKeyboardButton("Mors için ne yaptım", callback_data='query1301')
        button5 = InlineKeyboardButton("Servis Dashboarda Git", url="https://morsit.link/servisler")
        keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5]])
        bot.send_message(chat_id=-991478600, text="Merhaba Salvo. Hangi işlemi başlatmak istiyorsun ", reply_markup=keyboard)
        
        # SALVO SERVİS AÇILACK FİRMALAR
        
    def query1100(self):
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
            button1 = InlineKeyboardButton("Feriye", callback_data='query1101')
            button2 = InlineKeyboardButton("Emar Sağlık", callback_data='query1102')
            button3 = InlineKeyboardButton("Fabrika Mimarlık", callback_data='query1103')
            button4 = InlineKeyboardButton("Aktaç Gıda", callback_data='query1104')
            button5 = InlineKeyboardButton("Kate Hotel", callback_data='query1106')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5]])
            bot.send_message(chat_id=-991478600, text="Hangi müşteri için servis başlatıyorsunuz ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()
        
    def query1101(self):
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
            button1 = InlineKeyboardButton("Feriye Lokantası", callback_data='query1111')
            button2 = InlineKeyboardButton("Madera", callback_data='query1112')
            button3 = InlineKeyboardButton("İstanbul Modern", callback_data='query1113')
            button4 = InlineKeyboardButton("Diğer", callback_data='query1114')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4]])
            bot.send_message(chat_id=-991478600, text="Hangi şubesi için kayıt açacaksın ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()    
       
       # SALVO SERVİS AÇMA SORGULARI
        
    def query1111(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Lokantasi');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye Lokantası için servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query1112(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Madera');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Madera için servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query1113(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Istanbul Modern');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'İstanbul Modern için servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query1114(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (1, 1, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Diger');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye`nin sistemde tanımlı olmayan bir lokasyonu için servis kaydı açıldı')
        cursor.close()
        conn.close() 
    
    def query1102(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (2, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Emar Sağlık için servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query1103(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (3, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Fabrika Mimarlık için servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query1104(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (4, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Aktaç için servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query1106(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd) " \
                           "VALUES (6, 1, DATEADD(HOUR, 3, GETDATE()), NULL, NULL);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Kate Hotel için servis kaydı açıldı')
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
            
            
            
        # VOLKAN MENÜ
        
    def query5000(self):
        button1 = InlineKeyboardButton("Servis Başlat", callback_data='query5100')
        button2 = InlineKeyboardButton("Servis Bitir", callback_data='query5201')
        button3 = InlineKeyboardButton("Açık Servisleri Göster", callback_data='query5300')
        button4 = InlineKeyboardButton("Mors için ne yaptım", callback_data='query5301')
        button5 = InlineKeyboardButton("Servis Dashboarda Git", url="https://morsit.link/servisler")
        keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5]])
        bot.send_message(chat_id=-991478600, text="Merhaba Volkan. Hangi işlemi başlatmak istiyorsun ", reply_markup=keyboard)
        
        # VOLKAN SERVİS AÇILACK FİRMALAR
        
    def query5100(self):
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
            button1 = InlineKeyboardButton("Feriye", callback_data='query5101')
            button2 = InlineKeyboardButton("Emar Sağlık", callback_data='query5102')
            button3 = InlineKeyboardButton("Fabrika Mimarlık", callback_data='query5103')
            button4 = InlineKeyboardButton("Aktaç Gıda", callback_data='query5104')
            button5 = InlineKeyboardButton("Kate Hotel", callback_data='query5106')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4], [button5]])
            bot.send_message(chat_id=-991478600, text="Hangi müşteri için servis başlatıyorsunuz ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()
       
       # VOLKAN SERVİS AÇMA SORGULARI
        
    def query5101(self):
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
            button1 = InlineKeyboardButton("Feriye Lokantası", callback_data='query5111')
            button2 = InlineKeyboardButton("Madera", callback_data='query5112')
            button3 = InlineKeyboardButton("İstanbul Modern", callback_data='query5113')
            button4 = InlineKeyboardButton("Diğer", callback_data='query5114')
            keyboard = InlineKeyboardMarkup([[button1, button2], [button3, button4]])
            bot.send_message(chat_id=-991478600, text="Hangi şubesi için kayıt açacaksın ? ", reply_markup=keyboard)
            
        cursor.close()
        conn.close()
        
    def query5111(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Feriye Lokantasi');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye Lokantası için servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query5112(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, Feriye Lokantası);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye Lokantası için servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query5113(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, Feriye Lokantası);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye Lokantası için servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query5114(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (1, 2, DATEADD(HOUR, 3, GETDATE()), NULL, 'Diger');"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Feriye`nin sistemde tanımlı olmayan bir lokasyonu için servis kaydı açıldı')
        cursor.close()
        conn.close() 
    
    def query5102(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (2, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Emar Sağlık için servis kaydı açıldı')
        cursor.close()
        conn.close()
        
    def query5103(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (3, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Fabrika Mimarlık için servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query5104(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (4, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Aktaç için servis kaydı açıldı')
        cursor.close()
        conn.close()

    def query5106(self):
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
            insert_query = "INSERT INTO ServiceRecords (CustomerId, StaffId, ServiceStart, ServiceEnd, Notes) " \
                           "VALUES (6, 2, DATEADD(HOUR, 3, GETDATE()), NULL, NULL);"
            cursor.execute(insert_query)
            conn.commit()
            bot.send_message(-991478600, 'Kate Hotel için servis kaydı açıldı')
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
query_handler('query5100', MssqlConnection().query5100, ['kalyoncuvolkan'])
query_handler('query5101', MssqlConnection().query5101, ['kalyoncuvolkan'])
query_handler('query5111', MssqlConnection().query5111, ['kalyoncuvolkan'])
query_handler('query5112', MssqlConnection().query5112, ['kalyoncuvolkan'])
query_handler('query5113', MssqlConnection().query5113, ['kalyoncuvolkan'])
query_handler('query5114', MssqlConnection().query5114, ['kalyoncuvolkan'])
query_handler('query5102', MssqlConnection().query5102, ['kalyoncuvolkan'])
query_handler('query5103', MssqlConnection().query5103, ['kalyoncuvolkan'])
query_handler('query5104', MssqlConnection().query5104, ['kalyoncuvolkan'])
query_handler('query5106', MssqlConnection().query5106, ['kalyoncuvolkan'])
query_handler('query5201', MssqlConnection().query5201, ['kalyoncuvolkan'])
query_handler('query5300', MssqlConnection().query5300, ['kalyoncuvolkan'])
query_handler('query5301', MssqlConnection().query5301, ['kalyoncuvolkan'])
query_handler('query1100', MssqlConnection().query1100, ['salvoromi'])
query_handler('query1101', MssqlConnection().query1101, ['salvoromi'])
query_handler('query1111', MssqlConnection().query1111, ['salvoromi'])
query_handler('query1112', MssqlConnection().query1112, ['salvoromi'])
query_handler('query1113', MssqlConnection().query1113, ['salvoromi'])
query_handler('query1114', MssqlConnection().query1114, ['salvoromi'])
query_handler('query1102', MssqlConnection().query1102, ['salvoromi'])
query_handler('query1103', MssqlConnection().query1103, ['salvoromi'])
query_handler('query1104', MssqlConnection().query1104, ['salvoromi'])
query_handler('query1106', MssqlConnection().query1106, ['salvoromi'])
query_handler('query1201', MssqlConnection().query1201, ['salvoromi'])
query_handler('query1300', MssqlConnection().query1300, ['salvoromi'])
query_handler('query1301', MssqlConnection().query1301, ['salvoromi'])

bot.polling()









