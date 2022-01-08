import os
import logging
import random
from Script import script
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, MessageEmpty, MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from database.ia_filterdb import Media, get_file_details
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, PICS, RESULTS_COUNT, SUDO_CHATS_ID, SUDO_CHATS_ID_GS, CHAT_ID
from utils import get_size, is_subscribed, temp
from drive import drive
from requests import get as g

logger = logging.getLogger(__name__)

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton('🔍 টেলিগ্রাম ফাইল সার্চ 🔍', switch_inline_query_current_chat='')
            ],[
            InlineKeyboardButton('➕অন্য গ্রুপে ফাইল সার্চ ➕', switch_inline_query='')
            ],[            
            InlineKeyboardButton('🇧🇩 Bnagldesh Hoarding 🇧🇩', url='https://t.me/BangladeshHoarding')
            ],[
            InlineKeyboardButton('ℹ️ Help ℹ️', callback_data='help'),
            InlineKeyboardButton('😊 About BDH 😊', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        if not await db.is_user_exist(message.from_user.id):
            await db.add_user(message.from_user.id, message.from_user.first_name)
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "🤖 Join Our Channel", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            btn.append([InlineKeyboardButton(" 🔄 Try Again", callback_data=f"checksub#{message.command[1]}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text="**Please Join Our Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown"
            )
        return
    if len(message.command) ==2 and message.command[1] in ["subscribe", "error", "okay"]:
        buttons = [[
            InlineKeyboardButton('🔍 টেলিগ্রাম ফাইল সার্চ 🔍', switch_inline_query_current_chat='')
            ],[
            InlineKeyboardButton('➕অন্য গ্রুপে ফাইল সার্চ ➕', switch_inline_query='')
            ],[            
            InlineKeyboardButton('🇧🇩 Bnagldesh Hoarding 🇧🇩', url='https://t.me/BangladeshHoarding')
            ],[
            InlineKeyboardButton('ℹ️ Help ℹ️', callback_data='help'),
            InlineKeyboardButton('😊 About 😊', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        if not await db.is_user_exist(message.from_user.id):
            await db.add_user(message.from_user.id, message.from_user.first_name)
        return
    file_id = message.command[1]
    files = (await get_file_details(file_id))[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
        except Exception as e:
            print(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        )

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')


@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        'This will delete all indexed files.\nDo you want to continue??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="YES", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="CANCEL", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await message.answer()
    await message.message.edit('Succesfully Deleted All The Indexed Files.')

#ALEXMOD STARTED FROM NOW
DEFAULT_START_MARKUP= InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("🔍 টেলিগ্রাম ফাইল সার্চ 🔍", switch_inline_query_current_chat='')
        ],
        [
        InlineKeyboardButton("➕অন্য গ্রুপে ফাইল সার্চ ➕", switch_inline_query='')
        ],
        [
        InlineKeyboardButton("🖲️ Rules", callback_data="source"),
        InlineKeyboardButton("About Group 🧑", callback_data="about")
        ],
        [
        InlineKeyboardButton('📢 Bangladesh Hoarding 📢', url=f"https://t.me/bangladeshHoarding")
        ]]
    )
#Anonomous Chating
@Client.on_message(filters.command('n') & filters.private & filters.user(ADMINS))
async def anno(bot, update):
    await bot.send_message(CHAT_ID,update.text)
    
#/help Command 
@Client.on_message(filters.command("help") & ~filters.edited)
async def help_command(_, message):
    reply_markup = DEFAULT_START_MARKUP
    await message.reply_text(
        text="Hi...I'm BDH Search Bot of @BangladeshHoarding.\n"
              "Here you can search files in Inline mode as well as PM, Check commands\n"
              "Use the below buttons to search files or send me the name of file to search.",        
        disable_web_page_preview=True,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )
#/search. /find, /s, /f - For searching files in gDrive
@Client.on_message(filters.command(["search", "find", "f", "s", "list"]) & ~filters.edited & filters.chat(SUDO_CHATS_ID))
async def search(_, message):
    global i, m, data
    if len(message.command) < 2:
      await message.reply_text('ফাইল খুঁজতে নিচের কমান্ড গুলো ব্যবহার করুন \n /search [FileName] \n /find [FileName] \n /s [FileName] \n /f [FileName] \n\n এইভাবে খুঁজুনঃ /s Avenger')
      return
    query = message.text.split(' ',maxsplit=1)[1]
    m = await message.reply_text("**🔎 ফাইলটি খোঁজা হচ্ছে 🔎..অপেক্ষা করুন 🙏.. \n\n 💚@BangladeshHoarding💚**")
    data = drive.drive_list(query)
    
    results = len(data)
    i = 0
    i = i + RESULTS_COUNT

    if results == 0:
        await m.edit(text="দুঃখিত 😐, কোন ফাইল পাওয়া যায়নি, অথবা আপনি ভুল নামে খুঁজছেন... @imdb বট হতে সঠিক নাম জেনে নিন । \n\n 💚@BangladeshHoarding💚")
        return

    text = f"**🔎 𝐓𝐨𝐭𝐚𝐥 𝐑𝐞𝐬𝐮𝐥𝐭𝐬:** __{results}__ \n"
    for count in range(min(i, results)):
        if data[count]['type'] == "file":
            text += f"""
📄**[ {data[count]['name']} ]({data[count]['url'?a=view]})**
**📀𝐒𝐢𝐳𝐞:** __{data[count]['size']}__
▁▁▁▁[🄱🄳🄷](https://t.me/BangladeshHoarding)▁▁▁▁▁▁▁▁▁▁▁▁\n"""

        else:
            text += f"""
📂**[ {data[count]['name']} ]({data[count]['url']})**
▁▁▁▁[🄱🄳🄷](https://t.me/BangladeshHoarding)▁▁▁▁▁▁▁▁▁▁▁▁\n"""
    if len(data) > RESULTS_COUNT:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="<< ⏮️ পূর্ববর্তী",
                        callback_data="previous"
                    ),
                    InlineKeyboardButton(
                        text="পরবর্তী ⏭️ >>",
                        callback_data="next"
                    )                  
                ],
                [
                    InlineKeyboardButton("🔍 টেলিগ্রাম ফাইল সার্চ 🔍", switch_inline_query_current_chat="")
                ],
            ]
        )
        try:
            await m.edit(text=text, disable_web_page_preview=True, reply_markup=keyboard)
        except (MessageEmpty, MessageNotModified):
            pass
        return
    try:
        await m.edit(text=text, disable_web_page_preview=True)
    except (MessageEmpty, MessageNotModified):
        pass


@Client.on_callback_query(filters.regex("previous"))
async def previous_callbacc(_, CallbackQuery):
    global i, ii, m, data
    if i < RESULTS_COUNT:
        await CallbackQuery.answer(
            "আপনি প্রথম পেইজে আছেন...",
            show_alert=True
        )
        return
    ii -= RESULTS_COUNT
    i -= RESULTS_COUNT
    text = ""

    for count in range(ii, i):
        try:
            if data[count]['type'] == "file":
                text += f"""
📄**[ {data[count]['name']} ]({data[count]['url'?a=view]})**
**📀𝐒𝐢𝐳𝐞:** __{data[count]['size']}__
▁▁▁▁[🄱🄳🄷](https://t.me/BangladeshHoarding)▁▁▁▁▁▁▁▁▁▁▁▁\n"""

            else:
                text += f"""
📂**[ {data[count]['name']} ]({data[count]['url']})**
▁▁▁▁[🄱🄳🄷](https://t.me/BangladeshHoarding)▁▁▁▁▁▁▁▁▁▁▁▁\n"""
        except IndexError:
            continue

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="<< ⏮️ পূর্ববর্তী",
                    callback_data="previous"
                ),
                InlineKeyboardButton(
                    text="পরবর্তী ⏭️ >>",
                    callback_data="next"
                )              
            ],
            [
                InlineKeyboardButton("🔍 টেলিগ্রাম ফাইল সার্চ 🔍", switch_inline_query_current_chat="")
            ],
        ]
    )
    try:
        await m.edit(text=text, disable_web_page_preview=True, reply_markup=keyboard)
    except (MessageEmpty, MessageNotModified):
        pass


@Client.on_callback_query(filters.regex("next"))
async def next_callbacc(_, CallbackQuery):
    global i, ii, m, data
    ii = i
    i += RESULTS_COUNT
    text = ""

    for count in range(ii, i):
        try:
            if data[count]['type'] == "file":
                text += f"""
📄**[ {data[count]['name']} ]({data[count]['url'?a=view]})**
**📀𝐒𝐢𝐳𝐞:** __{data[count]['size']}__
▁▁▁▁[🄱🄳🄷](https://t.me/BangladeshHoarding)▁▁▁▁▁▁▁▁▁▁▁▁\n"""

            else:
                text += f"""
📂**[ {data[count]['name']} ]({data[count]['url']})**
▁▁▁▁[🄱🄳🄷](https://t.me/BangladeshHoarding)▁▁▁▁▁▁▁▁▁▁▁▁\n"""
        except IndexError:
            continue

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="<< ⏮️ পূর্ববর্তী",
                    callback_data="previous"
                ),
                InlineKeyboardButton(
                    text="পরবর্তী ⏭️ >>",
                    callback_data="next"
                )              
            ],
            [
                InlineKeyboardButton("🔍 টেলিগ্রাম ফাইল সার্চ 🔍", switch_inline_query_current_chat="")
            ],
        ]
    )
    try:
        await m.edit(text=text, disable_web_page_preview=True, reply_markup=keyboard)
    except (MessageEmpty, MessageNotModified):
        pass

#webss MOD- For taking website screenShot
@Client.on_message(filters.command("webss"))
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text("Give A Url To Fetch Screenshot.")
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**Taking Screenshot**")
        await m.edit("**Uploading Soon**")
        try:
            await message.reply_photo(
                photo=f"https://api.apiflash.com/v1/urltoimage?access_key=b6136e28fba742d7800d0ca235b9e68c&url={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("No Such Website.")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))
        
#Wellcome New Member MOD  
@Client.on_message(filters.new_chat_members)
async def welcome(_, message):  
    welcome_msg = f""" 
𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩
𝐈 𝐡𝐨𝐩𝐞 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐠𝐨𝐢𝐧𝐠 𝐭𝐨 𝐡𝐚𝐯𝐞 𝐚 𝐠𝐫𝐞𝐚𝐭 𝐭𝐢𝐦𝐞 𝐰𝐢𝐭𝐡 𝐮𝐬.😃 
𝐒𝐨 𝐡𝐚𝐩𝐩𝐲 𝐭𝐨 𝐡𝐚𝐯𝐞 𝐲𝐨𝐮 𝐚𝐦𝐨𝐧𝐠 𝐮𝐬.😊
"""
    reply_markup = DEFAULT_START_MARKUP
    await message.reply_text(        
        text=welcome_msg,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
