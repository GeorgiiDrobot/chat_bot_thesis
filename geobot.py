import telegram.ext
import telegram.ext 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import datetime
import sqlite3
import random
from datetime import date
from datetime import datetime, timedelta
import sqlite3 as sql
import os
from sqlite3 import Error
from telegram import KeyboardButton
import re 
from datetime import datetime as er
import logging
import xlwt
from openpyxl import load_workbook
from telegram import LabeledPrice, ShippingOption
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
)
logging.basicConfig(  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
wc=["Welcome to Botshop.\nSelect the products and receive at your door step.\nCheck our Instock and also Pre-Order products.\n\nSHOP ONLNE.STAY HOME. STAY SAFE"]
faq=["****"]
walletadd=['*******']
BUTTON,AB,DES,PHO,PRI,PADD,DELETEPRO,DELETE,SHE,CH,DESCC,DELCAT,LOG,ADMIN,DELADMIN,USE,DELUSE,ORDERR,SUPP,ADM,AHSEN,PDB,PDVM,DDFF,TXID,HAM,PENORD,SH,NNAME,CCONTACT,AADDRESS=range(31)
def start(update, context):
    bnm=update.message.from_user
    try:
        userna=bnm.usernamee
    except:
        userna=bnm.first_name
    userb=str(update.effective_user.id)
    print(userb)

    if  userb == "1394902938" or userb=="605276138": 
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌Delete product", callback_data="2")],
                   [InlineKeyboardButton("🛒 Orders", callback_data="99"),InlineKeyboardButton("Edit FQs", callback_data="912a")],
                   [InlineKeyboardButton("➕ Add Category", callback_data="90c"),InlineKeyboardButton("❌Delete Category", callback_data="8cd")],
                   [InlineKeyboardButton("Edit Logo", callback_data="8ab"),InlineKeyboardButton("🙋‍♂️ Welcome message", callback_data="912")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON 
    else:   
            connection = sqlite3.connect("users.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT id FROM COMPANY where id= {}".format(int(update.effective_user.id))) 
            jobs = cursor.fetchall()
            if len(jobs) ==0:
                cursor.execute("INSERT INTO COMPANY (ID) \
                    VALUES ({})".format(int(update.effective_user.id)))
                connection.commit()
                connection.close()
                conn = sqlite3.connect('data.db')
                conn.execute("INSERT INTO COMPANY (ID,username,date,price,orderid,status,payment,pname,productID,aa,bb,ct,uname,address,nmbr,dtime) \
                  VALUES ({}, '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(int(update.effective_user.id),userna,"0","0","0","0","0","0","0","0","0","0","0","0","0","0"))
                conn.commit()
                conn.close() 
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard3 = KeyboardButton(text="☎️ Contact us")
            loc_keyboard4 = KeyboardButton(text="⁉️ FAQ")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard3,loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
            return BUTTON
def button(update,context):
    h=update.effective_user.id
    query = update.callback_query
    a=query.data                
    if a== '1': 
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send name of product',reply_markup=reply_markup)
        return AB
    elif a=='2':
        keyf=[]
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c)
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 

        context.bot.send_message(chat_id=update.effective_user.id,text="Select the category to delete its product",reply_markup=reply_markup)  
        return DELETE 
    elif a=="912a":
        context.bot.send_message(chat_id=update.effective_user.id,text="Send FAQ to edit")          
        return SHE
    elif a=="912":
        context.bot.send_message(chat_id=update.effective_user.id,text="Send Welcome message")          
        return SH   
    elif a=="1adm":
        context.bot.send_message(chat_id=update.effective_user.id,text="Send UserID of Admin")          
        return ADMIN
    elif a=="1use":
        context.bot.send_message(chat_id=update.effective_user.id,text="Send UserIDof user")          
        return USE
    elif a=='2adm':
        keyf=[]
        conn = sqlite3.connect('admin.db')
        cursor = conn.execute("SELECT username from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c)
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 

        context.bot.send_message(chat_id=update.effective_user.id,text="Select userID of admin to delete",reply_markup=reply_markup)  
        return DELADMIN 
    elif a=='2use':
        keyf=[]
        conn = sqlite3.connect('banuser.db')
        cursor = conn.execute("SELECT username from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c)
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 

        context.bot.send_message(chat_id=update.effective_user.id,text="Select userID of user to unban",reply_markup=reply_markup)  
        return DELUSE
    elif a=="90c":       
        context.bot.send_message(chat_id=update.effective_user.id,text="Send Category name")         
        return CH
    elif a=='200':
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard3 = KeyboardButton(text="☎️ Contact us")
            loc_keyboard4 = KeyboardButton(text="⁉️ FAQ")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard3,loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
            return BUTTON
    elif a=='8cd':
        keyf=[]
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c)
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 

        context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption="Select the category to delete",reply_markup=reply_markup)  
        return DELCAT
    elif a=='8ab':   
            keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send shop logo',reply_markup=reply_markup)
            return LOG 
    elif a== '161': #quantity
        cc=update.callback_query.message.caption
        #cc=cc.replace("EUR","")
        dv=update.callback_query.message.photo[-1].file_id
        cf=update.callback_query.message.message_id
        d=cc
        df=cc.split("𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲:  ")
        df=df[1]
        df=df.strip()
        xd=df
        df=float(df)
        if df>1:
          d=cc
          df=cc.split("𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲:  ")
          df=df[1]
          df=df.strip()
          xdd=df
          dff=float(df)
          df=dff
          dff=dff-1
          mf=cc.split("𝐏𝐫𝐢𝐜𝐞:   ")
          mf=mf[1]
          mf=mf.split("𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:  ")
          mf=mf[0]
          mf=mf.strip()
          mf=mf.replace("EUR","")
          fgh=mf
          mf=float(mf)
          vc=float(df)
          op=mf/vc
          np=op*dff
          mf=float(mf)
          vc=float(df)
          np=round(np,2)    
          np=str(np)
          dy=str(dff)
          hjam="𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲:  {}".format(xdd)
          hjamn="𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲:  {}".format(dy)
          dfg="𝐏𝐫𝐢𝐜𝐞:   {}".format(fgh)
          dff="𝐏𝐫𝐢𝐜𝐞:   {}".format(np)
          cc=cc.replace(hjam,hjamn)
          cc=cc.replace(dfg,dff)
          keyboard =[[InlineKeyboardButton("➕ Add", callback_data="16"),InlineKeyboardButton("🔙 Cancel", callback_data="200")],[InlineKeyboardButton("➕ Quantity", callback_data="160"),InlineKeyboardButton("➖ Quantity", callback_data="161")]]
          reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
          context.bot.edit_message_caption(chat_id=update.effective_user.id,message_id=cf,caption=cc,reply_markup=reply_markup)     
    elif a== '160': #ADD QUANTITY
        cc=update.callback_query.message.caption
        #cc=cc.replace("EUR","")
        dv=update.callback_query.message.photo[-1].file_id
        cf=update.callback_query.message.message_id
        d=cc
        df=cc.split("𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲:  ")
        df=df[1]
        df=df.strip()
        xdd=df
        dff=float(df)
        df=dff
        dff=dff+1
        mf=cc.split("𝐏𝐫𝐢𝐜𝐞:   ")
        mf=mf[1]
        mf=mf.split("𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:  ")
        mf=mf[0]
        mf=mf.strip()
        mf=mf.replace("EUR","")
        fgh=mf       
        mf=float(mf)
        vc=float(df)
        op=mf/vc
        np=op*dff
        mf=float(mf)
        vc=float(df)
        np=round(np,2)        
        jk=str(np)
        dy=str(dff)
        hjam="𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲:  {}".format(xdd)
        hjamn="𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲:  {}".format(dy)
        dfg="𝐏𝐫𝐢𝐜𝐞:   {}".format(fgh)
        dff="𝐏𝐫𝐢𝐜𝐞:   {}".format(jk)
        cc=cc.replace(hjam,hjamn)
        cc=cc.replace(dfg,dff)
        keyboard =[[InlineKeyboardButton("➕ Add", callback_data="16"),InlineKeyboardButton("🔙 Cancel", callback_data="200")],[InlineKeyboardButton("➕ Quantity", callback_data="160"),InlineKeyboardButton("➖ Quantity", callback_data="161")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.edit_message_caption(chat_id=update.effective_user.id,message_id=cf,caption=cc,reply_markup=reply_markup) 
    elif a== '16':
        cc=update.callback_query.message.caption
        dv=update.callback_query.message.photo[-1].file_id
        fg=cc
        cf=update.callback_query.message.message_id
        df=cc.split("𝐏𝐫𝐢𝐜𝐞:   ")
        df=df[1]
        df=df.split("𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:  ")
        df=df[0]
        df=df.strip()
        dd=cc.split("𝐍𝐚𝐦𝐞:  ")
        dd=dd[1]
        dd=dd.split("𝐈𝐃:  ")
        dd=dd[0]
        dd=dd.strip()
        mm=cc.split("𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲:  ")
        mm=mm[1]
        mm=mm.strip()
        cc=cc.split("𝐈𝐃:  ")
        cc=cc[1]
        cc=cc.split("𝐏𝐫𝐢𝐜𝐞:   ")
        cc=cc[0]
        cc=cc.strip()              
        pric=df
        nam=dd
        pid=cc
        print(pric)
        conn = sqlite3.connect('cart.db')    
        cursor = conn.execute("DELETE from COMPANY where ID='{}'".format(str(update.effective_user.id)))
        conn.execute("INSERT INTO COMPANY (ID,name,productID,price,quantity) \
                VALUES ('{}', '{}','{}', '{}', '{}')".format(str(update.effective_user.id),nam,pid,pric,mm))
        conn.commit()
        keyboard =[[InlineKeyboardButton("✅ Checkout", callback_data="44a")],[InlineKeyboardButton("🔙 Cancel", callback_data="255")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.edit_message_caption(chat_id=update.effective_user.id,message_id=cf,caption=fg,reply_markup=reply_markup)
        conn.close()
        return BUTTON
    elif a== '22':
      query.answer()
      conn = sqlite3.connect('cart.db')
      cursor = conn.execute("SELECT name,Price,quantity from COMPANY where ID= '{}'".format(str(update.effective_user.id)))
      conn.commit()
      global x
      x="Here is your Order Detail:\n\n"
      for row in cursor: 
        m=row[2]+" x "+row[0]+ "     "+row[1]+"\n"   
        x=x+m
      cursor = conn.execute("SELECT SUM(Price),SUM(quantity) from COMPANY where ID= '{}'".format(str(update.effective_user.id)))
      global ap
      ap=""
      global nj
      nj=""
      for row in cursor:
            ap=float(row[0])
            ap=round(ap,2)
            conn = sqlite3.connect('data.db')
            conn.execute("UPDATE COMPANY set pr = '{}' where ID = {}".format(ap,int(update.effective_user.id)))
            conn.commit()
      keyboard =[[InlineKeyboardButton("✅ Confirm", callback_data="44a")],[InlineKeyboardButton("🔙 Cancel", callback_data="200")]]   
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text=x+"\nTotal"+" "+str(ap)+"EUR" ,reply_markup=reply_markup)           
      return BUTTON
    elif a=="44a":   
        context.bot.send_message(chat_id=update.effective_user.id,text="Please enter your 𝐍𝐚𝐦𝐞")
        return NNAME
    elif a=='1payy':
        keyboard =[[InlineKeyboardButton("📝 Orders", callback_data="1payyb")],[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐀𝐝𝐝𝐫𝐞𝐬𝐬: {}\nPay Exact amount of your order then add transaction ID of your payment from Order section.\nThankyou'.format(walletadd[0]),reply_markup=reply_markup)
        return BUTTON
    elif a=='1payyb':
            conn = sqlite3.connect('orders.db')
            cursor = conn.execute("SELECT orderid,status from COMPANY where ID= '{}' ".format(str(update.effective_user.id)))
            conn.commit()
            keyf=[]
            for row in cursor:
                print(row[1])
                if row[1]=="Pending":
                    k="⏳"
                elif row[1]=="Accept":
                    k="✅"
                elif row[1]=="Delivered":
                    k="🚚"
                elif row[1]=="Rejected":
                    k="❌"
                c=[InlineKeyboardButton(row[0]+k, callback_data=row[0])]
                keyf.append(c)
            b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Select Order to check detail",reply_markup=reply_markup) 
            return DDFF
    elif a== '99':
      query.answer()  
      key=[["⏳ - PENDING","History"],["Cancel"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="Select the Order Type:",reply_markup=reply_markup)
      return HAM 
    elif a=="1090":
      cc=update.callback_query.message.text
      d=cc
      global dfr
      dfr=cc.split("User ID: ")
      dfr=dfr[1]
      dfr=dfr.strip()
      keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text='Type your text and send',reply_markup=reply_markup)
      return ADM
    elif a=="10900":
          keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
          reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
          context.bot.send_message(chat_id=update.effective_user.id,text="Type text and send to Admin",reply_markup=reply_markup)
          return AHSEN
    elif a=='100':
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌delete product", callback_data="2")],
                   [InlineKeyboardButton("🛒 Orders", callback_data="99"),InlineKeyboardButton("Edit FQs", callback_data="912a")],
                   [InlineKeyboardButton("➕ Add Category", callback_data="90c"),InlineKeyboardButton("❌Delete Category", callback_data="8cd")],
                   [InlineKeyboardButton("Edit Logo", callback_data="8ab"),InlineKeyboardButton("🙋‍♂️ Welome message", callback_data="912")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON 

    elif a== '1234': #Reject
        c=update.callback_query.message.message_id
        cc=update.callback_query.message.text
        d=cc
        df=cc.split("𝐎𝐫𝐝𝐞𝐫 𝐧𝐮𝐦𝐛𝐞𝐫: ")
        df=df[1]
        df=df.strip()
        df=df.split("𝐎𝐫𝐝𝐞𝐫 𝐭𝐢𝐦𝐞: ")
        df=df[0]
        df=df.strip()
        conn = sqlite3.connect('data.db')
        cursor = conn.execute("UPDATE COMPANY set aa={} where ID='{}'".format(df,update.effective_user.id))
        conn.commit()
        keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send Trannsaction ID\n𝐎𝐫𝐝𝐞𝐫 𝐧𝐮𝐦𝐛𝐞𝐫: {}".format(df),reply_markup=reply_markup)
        return TXID
    elif a== '1122': #Reject
        c=update.callback_query.message.message_id
        cc=update.callback_query.message.text
        d=cc
        df=cc.split("𝐓𝐫𝐚𝐧𝐬𝐚𝐜𝐭𝐢𝐨𝐧 𝐈𝐃: ")
        df=df[1]
        df=df.strip()
        df=df.split("𝐎𝐫𝐝𝐞𝐫 𝐧𝐮𝐦𝐛𝐞𝐫: ")
        df=df[0]
        df=df.strip()
        dfa=cc.split("𝐎𝐫𝐝𝐞𝐫 𝐧𝐮𝐦𝐛𝐞𝐫: ")
        dfa=dfa[1]
        dfa=dfa.strip()
        conn = sqlite3.connect('orders.db')
        cursor = conn.execute("UPDATE COMPANY set payment={} where orderid='{}'".format(df,dfa))
        conn.commit()
        keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Transaction ID added for order# {}".format(dfa),reply_markup=reply_markup)
        return BUTTON
    elif a=='120':
        c=update.callback_query.message.message_id
        cc=update.callback_query.message.text
        d=cc
        df=cc.split("𝐎𝐫𝐝𝐞𝐫𝐈𝐃: ")
        df=df[1]
        df=df.strip()
        df=df.split("𝐏𝐫𝐨𝐝𝐮𝐜𝐭 𝐍𝐚𝐦𝐞: ")
        df=df[0]
        df=df.strip()
        dd=cc.split("𝐔𝐬𝐞𝐫𝐈𝐃:  ")
        dd=dd[1]
        dd=dd.split("𝐔𝐬𝐞𝐫'𝐬 𝐍𝐚𝐦𝐞:  ")
        dd=dd[0]
        dd=dd.strip()
        hhhh="Your order is being processed\n𝐎𝐫𝐝𝐞𝐫 𝐧𝐮𝐦𝐛𝐞𝐫# {}".format(df)  
        conn = sqlite3.connect('orders.db')
        cursor = conn.execute("UPDATE COMPANY set status='Accept' where orderid='{}'".format(df))
        conn.commit() 
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=dd,text=hhhh)   
        context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="{}\n ACCEPTED".format(d),reply_markup=reply_markup)
    elif a=='130':
        c=update.callback_query.message.message_id
        cc=update.callback_query.message.text
        d=cc
        df=cc.split("𝐎𝐫𝐝𝐞𝐫𝐈𝐃: ")
        df=df[1]
        df=df.strip()
        df=df.split("𝐏𝐫𝐨𝐝𝐮𝐜𝐭 𝐍𝐚𝐦𝐞: ")
        df=df[0]
        df=df.strip()
        dd=cc.split("𝐔𝐬𝐞𝐫𝐈𝐃:  ")
        dd=dd[1]
        dd=dd.split("𝐔𝐬𝐞𝐫'𝐬 𝐍𝐚𝐦𝐞:  ")
        dd=dd[0]
        dd=dd.strip()
        hhhh="Your order rejected bt the admin\n𝐎𝐫𝐝𝐞𝐫 𝐧𝐮𝐦𝐛𝐞𝐫# {}".format(df)  
        conn = sqlite3.connect('orders.db')
        cursor = conn.execute("UPDATE COMPANY set status='Rejected' where orderid='{}'".format(df))
        conn.commit() 
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=dd,text=hhhh)   
        context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="{}\n Rejected".format(d),reply_markup=reply_markup)
        return BUTTON

def nname(update, context):
    msg=update.message.text
    conn = sqlite3.connect('data.db')
    conn.execute("UPDATE COMPANY set uname = '{}' where ID = {}".format(msg,int(update.effective_user.id)))
    conn.commit()  
    context.bot.send_message(chat_id=update.effective_user.id,text="Please enter your 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐍𝐮𝐦𝐛𝐞𝐫")
    return CCONTACT
def ccontact(update, context):
    msg=update.message.text
    conn = sqlite3.connect('data.db')
    conn.execute("UPDATE COMPANY set nmbr = '{}' where ID = {}".format(msg,int(update.effective_user.id)))
    conn.commit()  
    context.bot.send_message(chat_id=update.effective_user.id,text="Please enter your 𝐀𝐝𝐝𝐫𝐞𝐬𝐬")
    return AADDRESS
def aaddress(update, context):
    msg=update.message.text
    conn = sqlite3.connect('data.db')
    conn.execute("UPDATE COMPANY set address = '{}' where ID = {}".format(msg,int(update.effective_user.id)))
    conn.commit()  
    keyboard =[[InlineKeyboardButton("10:00 - 12:00", callback_data="10 - 12")],[InlineKeyboardButton("12:00 - 14:00", callback_data="12 - 14")],
                [InlineKeyboardButton("14:00 - 16:00", callback_data="44a")],[InlineKeyboardButton("16:00 - 18:00", callback_data="16 - 18")],
                [InlineKeyboardButton("18:00 - 20:00", callback_data="18 - 20")]]   
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Select your 𝐃𝐞𝐥𝐢𝐯𝐞𝐫𝐲 𝐓𝐢𝐦𝐞" ,reply_markup=reply_markup)           
    return ORDERR
def sh(update,context):
    a=update.message.text
    wc.pop(0)
    wc.append(a)
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Welcome message updated",reply_markup=reply_markup)
    return BUTTON
def ham(update,context):
  msg=update.message.text
  if msg=="Cancel":
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌Delete product", callback_data="2")],
                   [InlineKeyboardButton("🛒 Orders", callback_data="99"),InlineKeyboardButton("Edit FQs", callback_data="912a")],
                   [InlineKeyboardButton("➕ Add Category", callback_data="90c"),InlineKeyboardButton("❌Delete Category", callback_data="8cd")],
                   [InlineKeyboardButton("Edit Logo", callback_data="8ab"),InlineKeyboardButton("🙋‍♂️ Welcome message", callback_data="912")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON 
  elif msg=="⏳ - PENDING":
            conn = sqlite3.connect('orders.db')
            cursor = conn.execute("SELECT orderid,uname from COMPANY where status= '{}' ".format("Pending"))
            conn.commit()
            keyf=[]
            for row in cursor:
                c=[InlineKeyboardButton("⏳ "+"{},{}".format(row[0],row[1]), callback_data=row[0])]
                keyf.append(c)
            b=[InlineKeyboardButton("🔙Back", callback_data='🔙Back')] 
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Select Order to check detail",reply_markup=reply_markup) 
            return PENORD
  elif msg=="History":

        style = xlwt.easyxf('font: bold 1, color black;')
        conn = sqlite3.connect('orders.db') 
        cursor = conn.execute("SELECT ID,price,quantity,status,pname,payment,username,contact,orderID,date from COMPANY ")
        conn.commit() 
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            f = open("orders.txt", "w",encoding="utf-8")
            conn = sqlite3.connect('orders.db') 
            cursor = conn.execute("SELECT ID,price,quantity,status,pname,payment,username,contact,orderID,date,uname,address,time from COMPANY ")
            conn.commit()
            xa="Orders\n"
            i=0
            j=0
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet("Order History")
            sheet.write(i, 1, "order_id", style)
            sheet.write(i, 2, "user_name", style)
            sheet.write(i, 3, "user_id",  style)
            sheet.write(i, 4,"product_name",  style)
            sheet.write(i, 5, "Price",  style)
            sheet.write(i, 6, "Delivery_Time",  style)
            sheet.write(i, 7, "Contact_number",  style)
            sheet.write(i, 8, "order_date+time",  style)
            sheet.write(i, 9, "Address",  style)
            sheet.write(i, 10, "Order_status",  style)


            
            for row in cursor:
                    i=i+1
                    j=j+1
                    inv=row[0]
                    vgy=row[1]
                    xdrt=row[2]
                    sheet.write(i, 1, row[8], style)
                    sheet.write(i, 2, row[10], style)
                    sheet.write(i, 3, row[0],  style)
                    sheet.write(i, 4, row[4],  style)
                    sheet.write(i, 5, row[1],  style)
                    sheet.write(i, 6, row[12],  style)
                    sheet.write(i, 7, row[7], style)
                    sheet.write(i, 8, row[9], style)
                    sheet.write(i, 9, row[11],  style)
                    sheet.write(i, 10, row[3],  style)
            workbook.save("orders.xls")
            keyboard =[[InlineKeyboardButton("Main Menu", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_document(chat_id=update.effective_user.id,document=open('orders.xls', 'rb'),reply_markup=reply_markup)
        else:
                keyboard =[[InlineKeyboardButton("❌", callback_data="100")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="You have no orders",reply_markup=reply_markup)
                return BUTTON
def penord(update,context):
    query = update.callback_query
    msg=query.data
    print(msg)
    if msg=="🔙Back":
      key=[["⏳ - PENDING","History"],["Cancel"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="Select the Order Type:",reply_markup=reply_markup)
      return HAM 
    else:
        conn = sqlite3.connect('orders.db')
        cursor = conn.execute("SELECT ID,price,quantity,status,pname,payment,username,contact,orderID,date,uname,address,time from COMPANY where orderid ='{}'".format(msg))
        conn.commit()
        for row in cursor: 
            g="\n𝐔𝐬𝐞𝐫𝐈𝐃:  "+row[0]+"\n𝐔𝐬𝐞𝐫'𝐬 𝐍𝐚𝐦𝐞:  "+row[10]+"\n𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐍𝐮𝐦𝐛𝐞𝐫: "+row[7]+"\n𝐀𝐝𝐝𝐫𝐞𝐬𝐬: "+row[11]+"\n𝐎𝐫𝐝𝐞𝐫𝐈𝐃: "+row[8]+"\n𝐏𝐫𝐨𝐝𝐮𝐜𝐭 𝐍𝐚𝐦𝐞: "+row[4]+"\n𝐏𝐫𝐢𝐜𝐞: "+row[1]+"\n𝐎𝐫𝐝𝐞𝐫 𝐃𝐚𝐭𝐞/𝐓𝐢𝐦𝐞:  "+row[9]+"\n𝐃𝐞𝐥𝐢𝐯𝐞𝐫𝐲 𝐓𝐢𝐦𝐞: "+row[12]+"\n𝐒𝐭𝐚𝐭𝐮𝐬 "+row[3]+"\n\n"
            keyboard =[[InlineKeyboardButton("Accept", callback_data="120"),InlineKeyboardButton("Reject", callback_data="130")],[InlineKeyboardButton("🔙 Cancel", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Pending order:\n"+g,reply_markup=reply_markup)
            return BUTTON
def txid(update, context):
    msg=update.message.text
    c=update.message.message_id
    cc=update.message.text
    d=cc
    conn = sqlite3.connect('data.db')
    cursor = conn.execute("SELECT aa from COMPANY where ID= '{}'".format(str(update.effective_user.id)))
    conn.commit()
    for row in cursor:
        df=row[0]

    keyboard =[[InlineKeyboardButton("✅ Confirm", callback_data="1122"),InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="𝐓𝐫𝐚𝐧𝐬𝐚𝐜𝐭𝐢𝐨𝐧 𝐈𝐃: {}\n𝐎𝐫𝐝𝐞𝐫 𝐧𝐮𝐦𝐛𝐞𝐫: {}".format(msg,df),reply_markup=reply_markup)
    return TXID   
def orderr(update, context):
    query = update.callback_query
    msg=query.data
    conn = sqlite3.connect('data.db')
    cursor = conn.execute("SELECT username,uname,nmbr,address from COMPANY where ID= '{}'".format(str(update.effective_user.id)))
    conn.commit()
    for row in cursor:
        myname=row[0]
        namee=row[1]
        numberr=row[2]
        addresss=row[3]
    conn = sqlite3.connect('cart.db')
    cursor = conn.execute("SELECT name,Price,quantity from COMPANY where ID= '{}'".format(str(update.effective_user.id)))
    conn.commit()
    for row in cursor:
        jjj=row[0]
        kkk=row[1]
        lll=row[2]
        yu= random.randint (0,999999)
        x=er.today().strftime("%m/%d/%Y, %H:%M:%S")
        conn = sqlite3.connect('orders.db')
        conn.execute("INSERT INTO COMPANY (ID,price,quantity,status,pname,payment,username,contact,orderID,date,uname,address,time) \
                            VALUES ('{}', '{}','{}', '{}','{}','{}','{}', '{}','{}', '{}', '{}','{}', '{}')".format(str(update.effective_user.id),kkk,lll,"Pending",jjj,"Pending",myname,numberr,yu,x,namee,addresss,msg))
        conn.commit()
        keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Your order has been placed.\nOr team will contact you as soon as possible. Thanks',reply_markup=reply_markup)
        return BUTTON
def jos(update, context):
    msg=update.message.text
    user=str(update.effective_user.id)             
    if msg=="🛒 Products":
            conn = sqlite3.connect('cat.db')
            cursor = conn.execute("SELECT cat from COMPANY")
            conn.commit()
            keyf=[]
            for row in cursor:
                c=[InlineKeyboardButton(row[0], callback_data=row[0])]
                keyf.append(c) 
            b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
            keyf.append(b) 
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 
            context.bot.send_message(chat_id=update.effective_user.id,text="Select Category to view its products",reply_markup=reply_markup)
            return PDB
    elif msg=="⁉️ FAQ":
        keyboard = [[InlineKeyboardButton("🔙 Main Menu", callback_data='200')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_user.id,text=faq[0],reply_markup=reply_markup)                       
        return BUTTON
    elif msg=="☎️ Contact us":
            keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Leave a message for support ✉️",reply_markup=reply_markup)
            return SUPP
    elif msg=="📝 Orders":
            conn = sqlite3.connect('orders.db')
            cursor = conn.execute("SELECT orderid,status from COMPANY where ID= '{}' ".format(str(update.effective_user.id)))
            conn.commit()
            keyf=[]
            for row in cursor:
                print(row[1])
                if row[1]=="Pending":
                    k="⏳"
                elif row[1]=="Accept":
                    k="✅"
                elif row[1]=="Delivered":
                    k="🚚"
                elif row[1]=="Rejected":
                    k="❌"
                c=[InlineKeyboardButton(row[0]+k, callback_data=row[0])]
                keyf.append(c)
            b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Select Order to check detail",reply_markup=reply_markup) 
            return DDFF

def ddff(update,context):
    query = update.callback_query
    msg=query.data
    print(msg)
    conn = sqlite3.connect('orders.db')
    cursor = conn.execute("SELECT ID,price,quantity,status,pname,payment,username,contact,orderID,date,uname,address,time from COMPANY where orderid ='{}'".format(msg))
    conn.commit()
    for row in cursor:
        g="𝐍𝐚𝐦𝐞: "+row[10]+"\n𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐍𝐮𝐦𝐛𝐞𝐫: "+row[7]+"\n𝐀𝐝𝐝𝐫𝐞𝐬𝐬: "+row[11]+"\n𝐃𝐞𝐥𝐢𝐯𝐞𝐫𝐲 𝐓𝐢𝐦𝐞: "+row[12]+"\n𝐎𝐫𝐝𝐞𝐫 𝐧𝐮𝐦𝐛𝐞𝐫: "+row[8]+"\n𝐎𝐫𝐝𝐞𝐫 𝐭𝐢𝐦𝐞: "+row[9]+"\n𝐏𝐚𝐲𝐦𝐞𝐧𝐭: "+"𝐂𝐚𝐬𝐡 𝐨𝐧 𝐃𝐞𝐥𝐢𝐯𝐞𝐫𝐲"+"\n"+"𝐎𝐫𝐝𝐞𝐫 𝐝𝐞𝐭𝐚𝐢𝐥𝐬: \n"+"𝐏𝐫𝐨𝐝𝐮𝐜𝐭: \n"+row[4]+"\n𝐏𝐫𝐢𝐜𝐞: "+row[1]+"\n\n𝐎𝐫𝐝𝐞𝐫 𝐒𝐭𝐚𝐭𝐮𝐬:"+row[3]

        keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=g,reply_markup=reply_markup)
        return BUTTON

def supp(update,context):
    msg=update.message.text
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Thanks for your message.\nWe will get back to you as soon as possible 🙏",reply_markup=reply_markup)
    keyboar =[[InlineKeyboardButton("Reply", callback_data="1090")]]
    reply_marku = InlineKeyboardMarkup(keyboar,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id= 605276138,text="Help and support Request\nMessage:\n"+str(msg)+"\nUser ID: "+str(update.effective_user.id),reply_markup=reply_marku) 
    return BUTTON
def adm(update,context):
    msg=update.message.text
    context.bot.send_message(chat_id=update.effective_user.id,text="Message Sent")
    keyboar =[[InlineKeyboardButton("Reply", callback_data='10900')]]
    reply_marku= InlineKeyboardMarkup(keyboar,resize_keyboard=True)
    context.bot.send_message(chat_id=str(dfr),text=msg,reply_markup=reply_marku)
    return BUTTON 
def ahsen(update, context):
    msg=update.message.text
    context.bot.send_message(chat_id=update.effective_user.id,text="Message Sent")
    keyboar =[[InlineKeyboardButton("Reply", callback_data='1090')]]
    reply_marku = InlineKeyboardMarkup(keyboar,resize_keyboard=True)
    context.bot.send_message(chat_id= 605276138,text="Message from User\n"+str(msg)+"\nUser ID: "+str(update.effective_user.id),reply_markup=reply_marku)
    return BUTTON
def pdb(update,context):
    query = update.callback_query
    msg=query.data
    print(msg)    
    if msg=="🌎Main Menu":
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard3 = KeyboardButton(text="☎️ Contact us")
            loc_keyboard4 = KeyboardButton(text="⁉️ FAQ")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard3,loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
    elif msg=="200":
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard3 = KeyboardButton(text="☎️ Contact us")
            loc_keyboard4 = KeyboardButton(text="⁉️ FAQ")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard3,loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
    else:
        conn = sqlite3.connect('data.db')
        cursor=conn.execute("UPDATE COMPANY set ct = '{}' where ID = {}".format(msg,int(update.effective_user.id)))
        conn.commit()
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT des from COMPANY where cat= '{}' ".format(msg))  
        conn.commit() 
        for name in cursor:
            ggp=name[0]
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT name from COMPANY where cat= '{}' ".format(msg))  
        conn.commit()                             
        keyf=[]
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT name from COMPANY where cat= '{}' ".format(msg))
            conn.commit()
            for row in cursor:
                c=[InlineKeyboardButton(row[0], callback_data=row[0])]
                keyf.append(c)
            b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=str(ggp),reply_markup=reply_markup)            
            return PDVM
        else:
            keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='This Category has no Items',reply_markup=reply_markup)
            return BUTTON
def pdvm(update,context):
    query = update.callback_query
    msg=query.data
    print(msg)
    if msg=="🌎Main Menu":
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard3 = KeyboardButton(text="☎️ Contact us")
            loc_keyboard4 = KeyboardButton(text="⁉️ FAQ")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard3,loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
    elif msg=="200":
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard3 = KeyboardButton(text="☎️ Contact us")
            loc_keyboard4 = KeyboardButton(text="⁉️ FAQ")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard3,loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup) 
    else:
        conn = sqlite3.connect('data.db')
        cursor = conn.execute("SELECT ct from COMPANY where ID={} ".format(str(update.effective_user.id)))
        conn.commit()
        for names in cursor:
            hjj=names[0] 
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT name,description,price,productID,img from COMPANY where cat= '{}'  AND name='{}' ".format(hjj,msg))                              
            keyf=[]
            jobs = cursor.fetchall()
            if len(jobs) !=0:
                conn = sqlite3.connect('shop.db')
                cursor = conn.execute("SELECT name,description,price,productID,img from COMPANY where cat= '{}'  AND name='{}' ".format(hjj,msg)) 
                for row in cursor:                                 
                    lk="https://t.me/makesomeprofitBOT?start={}".format(row[3])
                    m="𝐍𝐚𝐦𝐞:  "+row[0]+"\n𝐈𝐃:  "+row[3]+"\n𝐏𝐫𝐢𝐜𝐞:   "+row[2]+"EUR"+"\n𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:  "+row[1] +"\n𝐐𝐮𝐚𝐧𝐭𝐢𝐭𝐲:  1.0"
                    keyboard =[[InlineKeyboardButton("🛒 Buy", callback_data="16"),InlineKeyboardButton("🔙 Cancel", callback_data="200")],
                    [InlineKeyboardButton("➕ Quantity", callback_data="160"),InlineKeyboardButton("➖ Quantity", callback_data="161")]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                    context.bot.send_photo(chat_id=update.effective_user.id,photo=row[4],caption=m,reply_markup=reply_markup)
                    return BUTTON   
            else:
                        keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
                        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                        context.bot.send_message(chat_id=update.effective_user.id,text='This Category has no Items',reply_markup=reply_markup)
                        return BUTTON

def admin(update,context):
    a=update.message.text
    conn = sqlite3.connect('admin.db')
    conn.execute("INSERT INTO COMPANY (username) \
        VALUES ('{}')".format(a))
    conn.commit()
    conn.close()
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='{} added as admin'.format(a),reply_markup=reply_markup)
    return BUTTON 
def use(update,context):
    a=update.message.text
    conn = sqlite3.connect('banuser.db')
    conn.execute("INSERT INTO COMPANY (username) \
        VALUES ('{}')".format(a))
    conn.commit()
    conn.close()
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='{} banned'.format(a),reply_markup=reply_markup)
    return BUTTON
def deladmin(update,context):
    c=update.callback_query.message.message_id
    query = update.callback_query
    msg=query.data
    conn = sqlite3.connect('admin.db')
    cursor = conn.execute("DELETE from COMPANY where username='{}'".format(msg))
    conn.commit()
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Admin Deleted",reply_markup=reply_markup)
    return BUTTON
def deluse(update,context):
    c=update.callback_query.message.message_id
    query = update.callback_query
    msg=query.data
    conn = sqlite3.connect('banuser.db')
    cursor = conn.execute("DELETE from COMPANY where username='{}'".format(msg))
    conn.commit()
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="User unbanned",reply_markup=reply_markup)
    return BUTTON
def log(update,context):
    msg=update.message.photo[-1].file_id
    newFile = context.bot.getFile(msg)
    newFile.download('logo.jpg')
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Logo edited successfully',reply_markup=reply_markup)
    return BUTTON
def delcat(update,context):
    c=update.callback_query.message.message_id
    query = update.callback_query
    msg=query.data
    conn = sqlite3.connect('cat.db')
    cursor = conn.execute("DELETE from COMPANY where cat='{}'".format(msg))
    conn.commit()
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Category Deleted",reply_markup=reply_markup)
    return BUTTON
def ch(update,context):
    a=update.message.text
    msg=update.message.text
    global wopw
    wopw=msg
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Send Category Description",reply_markup=reply_markup)
    return DESCC
def descc(update,context):
    a=update.message.text
    msg=update.message.text
    conn = sqlite3.connect('cat.db')
    conn.execute("INSERT INTO COMPANY (cat,des) \
        VALUES ('{}','{}')".format(wopw,msg))
    conn.commit()
    conn.close()
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Category Updated",reply_markup=reply_markup)
    return BUTTON
def she(update,context):
       a=update.message.text
       faq.pop(0)
       faq.append(a)
       keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
       reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
       context.bot.send_message(chat_id=update.effective_user.id,text="FAQs updated",reply_markup=reply_markup)
       return BUTTON
def delete(update,context):
    query = update.callback_query
    msg=query.data
    keyf=[]
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("SELECT name from COMPANY where cat='{}'".format(msg))
    conn.commit()
    keyf=[]
    for row in cursor:
        c=[InlineKeyboardButton(row[0], callback_data=row[0])]
        keyf.append(c)
    reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Select the product name to delete the product ",reply_markup=reply_markup)  
    return DELETEPRO
def deletepro(update,context):
    query = update.callback_query
    msg=query.data
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("DELETE from COMPANY where name='{}'".format(msg))
    conn.commit()
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Product Deleted",reply_markup=reply_markup)
    return BUTTON
def ab(update,context):
    msg=update.message.text
    global nm
    nm =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Decription of product',reply_markup=reply_markup)
    return DES
def des(update,context):
    msg=update.message.text
    global ds
    ds =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Picture of product',reply_markup=reply_markup)
    return PHO
def pho(update,context):
    msg=update.message.photo[-1].file_id
    global pid
    pid =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Price of product without currency symbol',reply_markup=reply_markup)
    return PRI
def pri(update,context):
    msg=update.message.text
    global pc
    pc =msg
    try:
        float(msg)
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c)
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 
        context.bot.send_message(chat_id=update.effective_user.id,text="Select category for this product",reply_markup=reply_markup)
        return PADD
    except:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send Price of product without currency symbol',reply_markup=reply_markup)
        return PRI
def padd(update,context):
    query = update.callback_query
    msg=query.data
    yu= random.randint (0,999999)
    conn = sqlite3.connect('shop.db')
    conn.execute("INSERT INTO COMPANY (name,description,price,productID,img,cat) \
                        VALUES ('{}', '{}','{}', '{}','{}','{}')".format(nm,ds,pc,yu,pid,msg))
    conn.commit()
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Product added" ,reply_markup=reply_markup)
    return BUTTON

def main(): #5092451409:AAF24_hzhm5w7OE06FVu-Pp23isUtWUuJH0
  updater = Updater("5288140372:AAGhPjGZVHxvw11ATHQx9-Qoq8YBrsbBSNQ", use_context=True)
  dp = updater.dispatcher
  conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start),MessageHandler(Filters.regex('^(🛒 Products|📝 Orders|☎️ Contact us|⁉️ FAQ)$'), jos)],
        states={    
            BUTTON: [CallbackQueryHandler(button)],
            AB: [MessageHandler(Filters.text, ab),CallbackQueryHandler(button)],
            DES: [MessageHandler(Filters.text, des),CallbackQueryHandler(button)],
            PHO: [MessageHandler(Filters.photo, pho),CallbackQueryHandler(button)],
            PRI: [MessageHandler(Filters.text, pri),CallbackQueryHandler(button)],
            NNAME: [MessageHandler(Filters.text, nname),CallbackQueryHandler(button)],
            CCONTACT: [MessageHandler(Filters.text, ccontact),CallbackQueryHandler(button)],
            AADDRESS: [MessageHandler(Filters.text, aaddress),CallbackQueryHandler(button)],
            SHE: [MessageHandler(Filters.text, she),CallbackQueryHandler(button)],
            SH: [MessageHandler(Filters.text, sh),CallbackQueryHandler(button)],
            HAM: [MessageHandler(Filters.text, ham),CallbackQueryHandler(button)],
            CH: [MessageHandler(Filters.text, ch),CallbackQueryHandler(button)],
            ADMIN: [MessageHandler(Filters.text, admin),CallbackQueryHandler(button)],
            DESCC: [MessageHandler(Filters.text, descc),CallbackQueryHandler(button)],
            USE: [MessageHandler(Filters.text, use),CallbackQueryHandler(button)],
            SUPP: [MessageHandler(Filters.text, supp),CallbackQueryHandler(button)],
            ADM: [MessageHandler(Filters.text, adm),CallbackQueryHandler(button)],
            AHSEN: [MessageHandler(Filters.text, ahsen),CallbackQueryHandler(button)],

            TXID: [MessageHandler(Filters.text, txid),CallbackQueryHandler(button)],
            LOG: [MessageHandler(Filters.photo, log),CallbackQueryHandler(button)],
            DELETEPRO: [CallbackQueryHandler(deletepro)],
            DELETE: [CallbackQueryHandler(delete)],
            PENORD: [CallbackQueryHandler(penord)],
            DELCAT: [CallbackQueryHandler(delcat)],
            DELUSE: [CallbackQueryHandler(deluse)],
            PADD: [CallbackQueryHandler(padd)],
            PDB: [CallbackQueryHandler(pdb)],
            ORDERR: [CallbackQueryHandler(orderr)],
            PDVM: [CallbackQueryHandler(pdvm)],
            DELADMIN: [CallbackQueryHandler(deladmin)],
            DDFF: [CallbackQueryHandler(ddff)],

        },  #DELETEPRO,DELETE
        fallbacks=[CommandHandler('start', start)],
        allow_reentry=True
    )
  dp.add_handler(conv_handler)
  updater.start_polling()
  updater.idle()
    
if __name__ == '__main__':
    main()