import os
import aiohttp
import json
from pyrogram import Client, filters, emoji
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import Update, Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from info import ARQ_API_BASE_URL, ARQ_API_KEY, MONGO_STR
from pymongo import MongoClient
from re import match
from plugin import *

@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == "private":
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
            f" ℹ️ 𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎 ℹ️ \n\n<b>🗣 𝘍𝘪𝘳𝘴𝘵 𝘕𝘢𝘮𝘦 :</b> {first}\n<b>🗣 𝘓𝘢𝘴𝘵 𝘕𝘢𝘮𝘦 :</b> {last}\n<b>🕵️‍ 𝘜𝘴𝘦𝘳𝘯𝘢𝘮𝘦 :</b> {username}\n<b>🕵️‍♂️ 𝘜𝘴𝘦𝘳 𝘐𝘋 :</b> <code>{user_id}</code>\n<b>🏢 𝘋𝘢𝘵𝘢 𝘊𝘦𝘯𝘵𝘦𝘳:</b> <code>{dc_id}</code>",
            quote=True
        )

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += (
            "<b>🗣 𝘊𝘩𝘢𝘵 𝘐𝘋</b>: "
            f"<code>{message.chat.id}</code>\n"
        )
        if message.reply_to_message:
            _id += (
                "<b>🕵️‍♂️ 𝘜𝘴𝘦𝘳 𝘐𝘋 :</b>: "
                f"<code>{message.from_user.id}</code>\n"
                "<b>🕵️‍♂️ 𝘙𝘦𝘱𝘭𝘪𝘦𝘥 𝘜𝘴𝘦𝘳 𝘐𝘋 :</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += (
                "<b>🕵️‍♂️ 𝘜𝘴𝘦𝘳 𝘐𝘋 :</b>: "
                f"<code>{message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(
            _id,
            quote=True
        )

@Client.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "`𝐅𝐞𝐭𝐜𝐡𝐢𝐧𝐠 𝐮𝐬𝐞𝐫 𝐢𝐧𝐟𝐨...`"
    )
    await status_message.edit(
        "`𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐮𝐬𝐞𝐫 𝐢𝐧𝐟𝐨...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        await status_message.edit("No valid user_id / message specified")
    else:
        message_out_str = ""
        message_out_str += f"* ℹ️ 𝐅𝐔𝐋𝐋 𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎 ℹ️ *\n\n"
        message_out_str += f"<b>🗣 𝘍𝘪𝘳𝘴𝘵 𝘕𝘢𝘮𝘦:</b> {from_user.first_name}\n"
        last_name = from_user.last_name or "<b>None</b>"
        message_out_str += f"<b>🗣 𝘓𝘢𝘴𝘵 𝘕𝘢𝘮𝘦:</b> {last_name}\n"
        message_out_str += f"<b>🕵️‍♂️ 𝘜𝘴𝘦𝘳 𝘐𝘋 :</b> <code>{from_user.id}</code>\n"
        username = from_user.username or "<b>None</b>"
        dc_id = from_user.dc_id or "[User Doesnt Have A Valid DP]"
        message_out_str += f"<b>🏢 𝘋𝘢𝘵𝘢 𝘊𝘦𝘯𝘵𝘦𝘳 :</b> <code>{dc_id}</code>\n"
        message_out_str += f"<b>🕵️‍ 𝘜𝘴𝘦𝘳𝘯𝘢𝘮𝘦 :</b> @{username}\n"
        message_out_str += f"<b>🔗 𝘗𝘳𝘰𝘧𝘪𝘭𝘦 𝘓𝘪𝘯𝘬 :</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
        message_out_str += f"<b>👁 𝘓𝘢𝘴𝘵 𝘚𝘦𝘦𝘯 :</b> {from_user.status}\n"
        message_out_str += f"<b>🤖 𝘐𝘴 𝘉𝘰𝘵 :</b> {from_user.is_bot}\n"
        message_out_str += f"<b>🚫 𝘐𝘴 𝘍𝘢𝘬𝘦 :</b> {from_user.is_fake}\n"
        message_out_str += f"<b>🚫 𝘐𝘴 𝘚𝘤𝘢𝘮 :</b> {from_user.is_scam}\n"
        message_out_str += f"<b>🚫 𝘐𝘴 𝘙𝘦𝘴𝘵𝘳𝘪𝘤𝘵𝘦𝘥 :</b> {from_user.is_scam}\n"
        message_out_str += f"<b>✅ 𝘐𝘴 𝘝𝘦𝘳𝘪𝘧𝘪𝘦𝘥 𝘣𝘺 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮 :</b> {from_user.is_verified}\n"
        
        if message.chat.type in (("supergroup", "channel")):
            try:
                chat_member_p = await message.chat.get_member(from_user.id)
                joined_date = datetime.fromtimestamp(
                    chat_member_p.joined_date or time.time()
                ).strftime("%Y.%m.%d %H:%M:%S")
                message_out_str += (
                    "<b>➲ 𝘑𝘰𝘪𝘯𝘦𝘥 𝘵𝘩𝘪𝘴 𝘊𝘩𝘢𝘵 𝘰𝘯:</b> <code>"
                    f"{joined_date}"
                    "</code>\n"
                )
            except UserNotParticipant:
                pass
        chat_photo = from_user.photo
        if chat_photo:
            local_user_photo = await client.download_media(
                message=chat_photo.big_file_id
            )
            buttons = [[
                InlineKeyboardButton('❌ Close ❌', callback_data='close_data')
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await message.reply_photo(
                photo=local_user_photo,
                quote=True,
                reply_markup=reply_markup,
                caption=message_out_str,
                parse_mode="html",
                disable_notification=True
            )
            os.remove(local_user_photo)
        else:
            buttons = [[
                InlineKeyboardButton('❌ Close ❌', callback_data='close_data')
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await message.reply_text(
                text=message_out_str,
                reply_markup=reply_markup,
                quote=True,
                parse_mode="html",
                disable_notification=True
            )
        await status_message.delete()

@Client.on_message(filters.command(["imdb", 'im']))
async def imdb_search(client, message):
    if ' ' in message.text:
        k = await message.reply('🔎 আইএমডিবি তে খোঁজা হচ্ছে .. \n 🔍...𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐈𝐌𝐃𝐛')
        r, title = message.text.split(None, 1)
        movies = await get_poster(title, bulk=True)
        if not movies:
            return await message.reply("❌ কিছু পাওয়া যায়নি ❌\n 𝐍𝐨 𝐫𝐞𝐬𝐮𝐥𝐭𝐬 𝐅𝐨𝐮𝐧𝐝 ❌")
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{movie.get('title')} - {movie.get('year')}",
                    callback_data=f"imdb#{movie.movieID}",
                )
            ]
            for movie in movies
        ]
        await k.edit('আইএমডিবি হতে যা পেলুম... \n 𝐇𝐞𝐫𝐞 𝐢𝐬 𝐰𝐡𝐚𝐭 𝐢 𝐟𝐨𝐮𝐧𝐝 𝐨𝐧 𝐈𝐌𝐃𝐛', reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply('মুভি/ সিরিজ এর নাম দিন...\n । 𝐆𝐢𝐯𝐞 𝐦𝐞 𝐚 𝐦𝐨𝐯𝐢𝐞 / 𝐒𝐞𝐫𝐢𝐞𝐬 𝐍𝐚𝐦𝐞')

@Client.on_callback_query(filters.regex('^imdb'))
async def imdb_callback(bot: Client, query: CallbackQuery):
    i, movie = query.data.split('#')
    imdb = await get_poster(query=movie, id=True)
    btn = [
            [
                InlineKeyboardButton(
                    text=f"{imdb.get('title')} - {imdb.get('year')}",
                    url=imdb['url'],
                )
            ]
        ]
    if imdb.get('poster'):
        await query.message.reply_photo(photo=imdb['poster'], caption=f"IMDb Data:\n\n🏷 <a href={imdb['url']}>{imdb.get('title')}</a>\n\n<b>🎭 Genres:</b> {imdb.get('genres')}\n<b>📆 Year:</b><a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a>\n<b>🌟 Rating:</b> <a href={imdb['url']}/ratings>{imdb.get('rating')}</a> / 10\n\n<i><b>🖋 StoryLine:</b>{imdb.get('plot')} </i>", reply_markup=InlineKeyboardMarkup(btn))
        await query.message.delete()
    else:
        await query.message.edit(f"IMDb Data:\n\n🏷 <a href={imdb['url']}>{imdb.get('title')}</a>\n\n<b>🎭 Genres:</b> {imdb.get('genres')}\n<b>📆 Year:</b> <a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a>\n<b>🌟 Rating:</b>  <a href={imdb['url']}/ratings>{imdb.get('rating')}</a> / 10\n\n<i><b>🖋 StoryLine:</b> {imdb.get('plot')} </i>", reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
    await query.answer(b)

posttem = """\n\n ▬▬▬ [❝ 🄻🄸🄽🄺🅂 ❞](https://t.me/BangladeshHoarding) ▬▬▬ \n\n\n\n ▬▬▬▬ [❝ 🄱🄳🄷 ❞](https://t.me/BangladeshHoarding) ▬▬▬▬ \n\n[🚀 𝐉𝐨𝐢𝐧 𝐍𝐨𝐰](https://t.me/BangladeshHoarding) | [💬 𝐈𝐧𝐛𝐨𝐱](https://t.me/BDH_PM_bot) | [🙏 𝐃𝐢𝐬𝐜𝐥𝐚𝐢𝐦𝐞𝐫](https://t.me/bangladeshhoarding/5)"""
@Client.on_message(filters.command(["post", 'p']))
async def imdb_search_post(client, message):
    if ' ' in message.text:
        k = await message.reply('🔎 আইএমডিবি তে খোঁজা হচ্ছে .. \n 🔍...𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐈𝐌𝐃𝐛')
        r, title = message.text.split(None, 1)
        movies = await get_poster(title, bulk=True)
        if not movies:
            return await message.reply("❌ কিছু পাওয়া যায়নি ❌\n 𝐍𝐨 𝐫𝐞𝐬𝐮𝐥𝐭𝐬 𝐅𝐨𝐮𝐧𝐝 ❌")
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{movie.get('title')} - {movie.get('year')}",
                    callback_data=f"post#{movie.movieID}",
                )
            ]
            for movie in movies
        ]
        await k.edit('আইএমডিবি হতে যা পেলুম... \n 𝐇𝐞𝐫𝐞 𝐢𝐬 𝐰𝐡𝐚𝐭 𝐢 𝐟𝐨𝐮𝐧𝐝 𝐨𝐧 𝐈𝐌𝐃𝐛', reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply('পোস্ট টেম্পলেট পেতে মুভি/ সিরিজ এর নাম দিন...\n । 𝐆𝐢𝐯𝐞 𝐦𝐞 𝐚 𝐦𝐨𝐯𝐢𝐞 / 𝐒𝐞𝐫𝐢𝐞𝐬 𝐍𝐚𝐦𝐞 To get BDH post template')

@Client.on_callback_query(filters.regex('^post'))
async def imdb_callback(bot: Client, query: CallbackQuery):
    i, movie = query.data.split('#')
    imdb = await get_poster(query=movie, id=True)
    btn = [
            [
                InlineKeyboardButton(
                    text=f"{imdb.get('title')} - {imdb.get('year')}",
                    url=imdb['url'],
                )
            ]
        ]
    if imdb.get('poster'):
        await query.message.reply_photo(photo=imdb['poster'], caption=f"🏷 <b><a href={imdb['url']}>{imdb.get('title')}</a><b>\n\n<b>🎭 Genres:</b> <i>{imdb.get('genres')}</i>\n<b>📆 Year:</b> <i><a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a></i>\n<b>🌟 Rating:</b> <a href={imdb['url']}/ratings>{imdb.get('rating')}</a> / 10\n\n<i><b>🖋 StoryLine:</b> {imdb.get('plot')}</i> {posttem}", reply_markup=InlineKeyboardMarkup(btn))
        await query.message.delete()
    else:
        await query.message.edit(f"🏷 <b><a href={imdb['url']}>{imdb.get('title')}</a></b>\n\n<b>🎭 Genres:</b> <i>{imdb.get('genres')}</i>\n<b>📆 Year:</b> <i><a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a></i>\n<b>🌟 Rating:</b> <i><a href={imdb['url']}/ratings>{imdb.get('rating')}</a></i> / 10\n\n<i><b>🖋 StoryLine:</b> {imdb.get('plot')} </i>{posttem}", reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
    await query.answer(b)
        
#Torrent Search 
@Client.on_message(filters.command(['thelp']))
async def help(_, message):
    await message.reply_text("টরেন্ট সার্চ করতে এই কমান্ড ব্যাবহার করুন...\n /t [File name] \n /m [File name]")

m = None
i = 0
a = None
query = None


@Client.on_message(filters.command(["t", "m"]))
async def torrent(_, message):
    global m
    global i
    global a
    global query
    try:
        await message.delete()
    except:
        pass
    if len(message.command) < 2:
        await message.reply_text("টরেন্ট সার্চ করতে এই কমান্ড ব্যাবহার করুন...\n /t [File name] \n /m [File name]")
        return
    query = message.text.split(None, 1)[1].replace(" ", "%20")
    m = await message.reply_text("🔎 টরেন্ট'টি খোঁজা হচ্ছে 🔎...অপেক্ষা করুন 🙏")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{ARQ_API_BASE_URL}torrent?query={query}") \
                    as resp:
                a = json.loads(await resp.text())
    except:
        await m.edit("দুঃখিত 😐, কোন টরেন্ট পাওয়া যায়নি, অথবা আপনি ভুল নামে খুঁজছেন..😐")
        return
    result = (
        f"**Page - {i+1}**\n\n"
        f"Name: {a[i]['name']}\n"
        f"Upload: {a[i]['uploaded']}\n"
        f"Size: {a[i]['size']}\n"
        f"Leechers: {a[i]['leechs']} "
        f"seeders: {a[i]['seeds']}\n"
        f"Magnet: `{a[i]['magnet']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Next {emoji.RIGHT_ARROW}",
                                         callback_data="next"),
                    InlineKeyboardButton(f"Delete {emoji.CROSS_MARK}",
                                         callback_data="delete")
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("next"))
async def callback_query_next(_, message):
    global i
    global m
    global a
    global query
    i += 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"Name: {a[i]['name']}\n"
        f"Upload: {a[i]['uploaded']}\n"
        f"Size: {a[i]['size']}\n"
        f"Leechers: {a[i]['leechs']} "
        f"seeders: {a[i]['seeds']}\n"
        f"Magnet: `{a[i]['magnet']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"{emoji.LEFT_ARROW} Previous",
                                         callback_data="previous"),
                    InlineKeyboardButton(f"Next {emoji.RIGHT_ARROW}",
                                         callback_data="next"),
                    InlineKeyboardButton(f"Delete {emoji.CROSS_MARK}",
                                         callback_data="delete")

                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("previous"))
async def callback_query_previous(_, message):
    global i
    global m
    global a
    global query
    i -= 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"Name: {a[i]['name']}\n"
        f"Upload: {a[i]['uploaded']}\n"
        f"Size: {a[i]['size']}\n"
        f"Leechers: {a[i]['leechs']} "
        f"seeders: {a[i]['seeds']}\n"
        f"Magnet: `{a[i]['magnet']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"{emoji.LEFT_ARROW} Previous",
                                         callback_data="previous"),
                    InlineKeyboardButton(f"Next {emoji.RIGHT_ARROW}",
                                         callback_data="next"),
                    InlineKeyboardButton(f"Delete {emoji.CROSS_MARK}",
                                         callback_data="delete")
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("delete"))
async def callback_query_delete(_, message):
    global m
    global i
    global a
    global query
    await m.delete()
    m = None
    i = 0
    a = None
    query = None
#Request MOD
'''Connecting To Database'''
mongo_client = MongoClient(MONGO_STR)
db_bot = mongo_client['RequestTrackerBot']
collection_ID = db_bot['channelGroupID']
query = {
    "groupID" : [
        "channelID",
        "userID"
    ]
}
if not collection_ID.find_one(query):
    collection_ID.insert_one(query)


requestRegex = "#[rR][eE][qQ][uU][eE][sS][tT] "


"""Handlers"""

# Start & Help Handler
@Client.on_message(filters.private & filters.command(["req"]))
async def reqh(bot:Update, msg:Message):
    botInfo = await bot.get_me()
    await msg.reply_text(
        "<b>Hi, I am Request Tracker Bot🤖.\
        \nIf you hadn't added me in your Group & Channel then ➕add me now.\
        \n\nHow to Use me?</b>\
        \n\t1. Add me to your Group & CHannel.\
        \n\t2. Make me admin in both Channel & Group.\
        \n\t3. Give permission to Post , Edit & Delete Messages.\
        \n\t4. Now send Group ID & Channel ID in this format <code>/add GroupID ChannelID</code>.\
        \nNow Bot is ready to be used.\
        \n\n<b>😊Join @AJPyroVerse & @AJPyroVerseGroup for getting more awesome 🤖bots like this.</b>",
        parse_mode = "html",
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BDH",
                        url = f"https://telegram.me/bangladeshHoarding"
                    )
                ]
            ]
        )
    )
    return

@Client.on_message(filters.new_chat_members)
async def chatHandler(bot:Update, msg:Message):
    if msg.new_chat_members[0].is_self:
        await msg.reply_text(
            f"<b>Your Group ID is <code>{msg.chat.id}</code></b>",
            parse_mode = "html"
        )
    return

@Client.on_message(filters.forwarded & filters.private)
async def forwardedHandler(bot:Update, msg:Message):
    forwardInfo = msg.forward_from_chat
    if forwardInfo.type == "channel":
        await msg.reply_text(
            f"<b>Your Channel ID is <code>{forwardInfo.id}</code></b>",
            parse_mode = "html"
        )
    return

@Client.on_message(filters.private & filters.command("add"))
async def groupChannelIDHandler(bot:Update, msg:Message):
    message = msg.text.split(" ")
    if len(message) == 3:
        _, groupID, channelID = message
        try:
            int(groupID)
            int(channelID)
        except ValueError:
            await msg.reply_text(
                "<b>Group ID & Channel ID should be integer type😒.</b>",
                parse_mode = "html"
            )
        else:
            document = collection_ID.find_one(query)
            try:
                document[groupID]
            except KeyError:
                if idExtractor(channelID, document):
                    document[groupID] = [channelID, msg.chat.id]
                    collection_ID.update_one(
                        query,
                        {
                            "$set" : document
                        }
                    )
                    await msg.reply_text(
                        "<b>Your Group and Channel has now been added SuccessFully🥳.</b>",
                        parse_mode = "html"
                    )
                else:
                    await msg.reply_text(
                        "<b>Your Channel ID already Added🤪.</b>",
                        parse_mode = "html"
                    )
            else:
                await msg.reply_text(
                    "<b>Your Group ID already Added🤪.</b>",
                    parse_mode = "html"
                )

    else:
        await msg.reply_text(
            "<b>Invalid Format😒\
            \nSend Group ID & Channel ID in this format <code>/add GroupID ChannelID</code>.</b>",
            parse_mode = "html"
        )

@Client.on_message(filters.private & filters.command("remove"))
async def channelgroupRemover(bot:Update, msg:Message):
    message = msg.text.split(" ")
    if len(message) == 2:
        _, groupID = message
        document = collection_ID.find_one(query)
        for key in document:
            if key == groupID:
                if document[key][1] == msg.chat.id:
                    del document[key]
                    collection_ID.update_one(
                        query,
                        {
                            "$set" : document
                            }
                    )
                    await msg.reply_text(
                        "<b>Your Channel ID & Group ID has now been Deleted😢 from our Database.\
                        \nYou can add them again by using <code>/add GroupID ChannelID</code>.</b>",
                        parse_mode = "html"
                    )
                    break
                else:
                    await msg.reply_text(
                        "<b>😒You are not the one who added this Channel ID & Group ID.</b>",
                        parse_mode = "html"
                    )
        else:
            await msg.reply_text(
                "<b>Given Group ID is not found in our Database🤔.</b>",
                parse_mode = "html"
            )
    else:
        await msg.reply_text(
            "<b>Invalid Command😒\
            Use <code>/remove GroupID</code></b>.",
            parse_mode = "html"
        )


@Client.on_message(filters.group & filters.regex(requestRegex + "(.*)"))
async def requestHandler(bot:Update, msg:Message):
    groupID = str(msg.chat.id)

    document = collection_ID.find_one(query)
    try:
        channelIDL = document[groupID]
    except KeyError:
        pass
    else:
        channelID = channelIDL[0]

        fromUser = msg.from_user
        mentionUser = f"<a href='tg://user?id={fromUser.id}'>{fromUser.first_name}</a>"
        requestText = f"<b>Request by {mentionUser}\n\n{msg.text}</b>"
        originalMSG = msg.text
        findRegexStr = match(requestRegex, originalMSG)
        requestString = findRegexStr.group()
        contentRequested = originalMSG.split(requestString)[1]
        
        groupIDPro = groupID.removeprefix(str(-100))
        channelIDPro = channelID.removeprefix(str(-100))

        requestMSG = await bot.send_message(
            int(channelID),
            requestText,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Requested Message",
                            url = f"https://t.me/c/{groupIDPro}/{msg.message_id}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "🚫Reject",
                            "reject"
                        ),
                        InlineKeyboardButton(
                            "Done✅",
                            "done"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "⚠️Unavailable⚠️",
                            "unavailable"
                        )
                    ]
                ]
            )
        )

        replyText = f"<b>👋 Hello {mentionUser} !!\n\n📍 Your Request for {contentRequested} has been submitted to the admins.\n\n🚀 Your Request Will Be Uploaded In 48hours or less.\n📌 Please Note that Admins might be busy. So, this may take more time.\n\n👇 See Your Request Status Here 👇</b>"

        await msg.reply_text(
            replyText,
            parse_mode = "html",
            reply_to_message_id = msg.message_id,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "⏳Request Status⏳",
                            url = f"https://t.me/c/{channelIDPro}/{requestMSG.message_id}"
                        )
                    ]
                ]
            )
        )
    finally:
        return

@Client.on_callback_query()
async def callBackButton(bot:Update, callback_query:CallbackQuery):
    channelID = str(callback_query.message.chat.id)
    document = collection_ID.find_one(query)

    resultID = idExtractor(channelID, document)
    if resultID:
        groupID, channelOwnerID = resultID

        data = callback_query.data
        if data == "rejected":
            return await callback_query.answer(
                "This request is rejected💔...\nAsk admins in group for more info💔",
                show_alert = True
            )
        elif data == "completed":
            return await callback_query.answer(
                "This request Is Completed🥳...\nCheckout in Channel😊",
                show_alert = True
            )
        if callback_query.from_user.id == channelOwnerID:

            if data == "reject":
                result = "REJECTED"
                groupResult = "has been Rejected💔."
                button = InlineKeyboardButton("Request Rejected🚫", "rejected")
            elif data == "done":
                result = "COMPLETED"
                groupResult = "is Completed🥳."
                button = InlineKeyboardButton("Request Completed✅", "completed")
            elif data == "unavailable":
                result = "UNAVAILABLE"
                groupResult = "has been rejected 💔 Due to Unavailablity🥲."
                button = InlineKeyboardButton("Request Rejected🚫", "rejected")

            msg = callback_query.message
            originalMsg = msg.text
            findRegexStr = match(requestRegex, originalMsg)
            requestString = findRegexStr.group()
            contentRequested = originalMsg.split(requestString)[1]
            requestedBy = originalMsg.removeprefix("Request by ").split('\n\n')[0]
            userid = msg.entities[1].user.id
            mentionUser = f"<a href='tg://user?id={userid}'>{requestedBy}</a>"
            originalMsgMod = originalMsg.replace(requestedBy, mentionUser)
            originalMsgMod = f"<s>{originalMsgMod}</s>"

            newMsg = f"<b>{result}</b>\n\n{originalMsgMod}"

            await callback_query.edit_message_text(
                newMsg,
                parse_mode = "html",
                reply_markup = InlineKeyboardMarkup(
                    [
                        [
                            button
                        ]
                    ]
                )
            )

            replyText = f"<b>Dear {mentionUser}🧑\nYour request for {contentRequested} {groupResult}\n👍Thanks for requesting!</b>"
            await bot.send_message(
                int(groupID),
                replyText,
                parse_mode = "html"
            )
        
        else:
            await callback_query.answer(
                "Who the hell are you?\nYour are not Owner😒.",
                show_alert = True
            )
    return
