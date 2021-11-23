import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.ERROR)

from pyrogram import Client, filters, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, MONGO_STR
from utils import temp
from pyrogram.types import (
    Update,
    Message,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pymongo import MongoClient
from re import match
from plugin import *

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        self.username = '@' + me.username
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")
        
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

app = Bot()
app.run()
