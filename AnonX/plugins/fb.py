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
             await message.reply(f"400: Sorry, Unable To Find It Make Sure Its Publically Available :)")
        except Exception as e:
          #  await message.reply_text(f"https://ddinstagram.com{content_value}")
            
          #     await message.reply(tracemsg)
            ##optinal 
            await message.reply(f"400: Sorry, Unable To Find It  try another or report it  to @masterolic or support chat @spotify_supportbot 🤖  ")

        finally:
            
               
            if 'downfile' in locals():
                os.remove(downfile)
