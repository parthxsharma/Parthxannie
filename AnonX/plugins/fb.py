from pyrogram import filters, Client as Mbot
import bs4, requests,re,asyncio
import wget,os,traceback
from AnonX import app

@app.on_message(filters.regex(r'https?://.*facebook[^\s]+') & filters.incoming,group=-6)
async def link_handler(app, message):
    link = message.matches[0].group(0)
    try:
       m = await message.reply_text("✨")
       get_api=requests.get(f"https://yasirapi.eu.org/fbdl?link={link}").json()
       if get_api['success'] == "false":
          return await message.reply("Invalid video url. Please try again :)")
       if get_api['success'] == "ok":
          if get_api.get('result').get('hd'):
             try:
                 dump_file = await message.reply_video(get_api['result']['hd'],caption="Thank you for using - @InstaReelsdownbot")
             except KeyError:
                 pass 
             except Exception:
                 try:
                     sndmsg = await message.reply(get_api['result']['hd'])
                     await asyncio.sleep(1)
                     dump_file = await message.reply_video(get_api['result']['hd'],caption="Thank you for using - @InstaReelsdownbot")
                     await sndmsg.delete()
                 except Exception:
                     try:
                        down_file = wget.download(get_api['result']['hd'])
                        await message.reply_video(down_file,caption="Thank you for using - @InstaReelsdownbot")
                        await sndmsg.delete()
                        os.remove(down_file)
                     except:
                         return await message.reply("Oops Failed To Send File Instead Of Link")
          else: 
             if get_api.get('result').get('sd'):
               try:
                   dump_file = await message.reply_video(get_api['result']['sd'],caption="Thank you for using - @InstaReelsdownbot")
               except KeyError:
                   pass
               
