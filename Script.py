class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
Hi, I'm <a href='https://t.me/BangladeshHoarding'>BDH Search Bot</a> of <a href='https://t.me/BangladeshHoarding'>🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩</a>. I can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.

• /logs - to get the rescent errors
• /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.
* /imdb or /im - fetch info from imdb.
* /post or /p - fetch post templet with info from imdb
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /index  - to add files from a channel
• /leave  - to leave from a chat.
• /disable  -  do disable a chat.
* /enable - re-enable chat.
* /webss - to take screenshot of website
* /search,/find,/s,/f- to search files in Gdrive (Authorize chats only) 
• /ban  - to ban a user.
• /unban  - to unban a user.
• /channel - to get list of total connected channels
• /broadcast - to broadcast a message to all BDH users"""
    ABOUT_TXT = """ℹ️ <a href='https://t.me/BangladeshHoarding'>🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩</a> is a non-profit group Where anyone can mirror and store there favourite files/contents which are already available on the internet and user’s can access there files anytime... and this group has a global file search index so user's can search there content too...

🙏 Disclaimer : Every file of <a href='https://t.me/BangladeshHoarding'>🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩</a> is already available on Internet <a href='https://t.me/BangladeshHoarding'>🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩</a> doesn’t rip/pirate anything. Copyright owner Please drop a message <a href='http://t.me/BDH_PM_bot'>BDH_PM</a> to take down ⛔️ content from group storage... <br> **There is no specific Owner of <a href='https://t.me/BangladeshHoarding'>🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩</a>, all group members are the owner of <a href='https://t.me/BangladeshHoarding'>🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩</a>***
Thank you...
BDH 🇧🇩

The rules

Welcome to  🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩 

✅ 1. Please Talk in Bangla/English language.
✅ 2. Respect every Member and avoid fights.
✅ 3. Search before mirroring anything Search Files in a Proper Way.
❌ 4. Don't PM anyone without asking them first. 
❌ 5. Don't Search files repeatedly, Search after one search task is complete..   
❌ 6. Don't Abuse Bots. Check Bot commands before using bots.
❌ 7. Don't  Share Fake News, Vulgar things and also No Bitcoin and crypto Things. Do Not Spam.
❌ 8. Don't upload Porn/Fake Files/Malware etc. We don't hate porn or porn lovers  but you cant upload it Here.Help us to keep the group clean.

we can't help you if you break any rules...we must ban you forever.

============G-Translated================

🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩  এ আপনাকে স্বাগতম।

✅ 1. গ্রুপে বাংলা/ইংরেজি ভাষায় কথা বলুন।
✅ 2. প্রত্যেক সদস্যকে সম্মান করুন এবং চ্যাট ফাইট এড়িয়ে চলুন।
✅ 3. কিছু মিরর করার আগে ফাইল সার্চ করুন। সঠিক উপায়ে ফাইল সার্চ করুন.
❌ 4. কাউকে প্রথমে জিজ্ঞাসা না করে মেসেজ করবেন না।
❌ 5. বারবার ফাইল সার্চ করবেন না, একটি সার্চ টাস্ক শেষ হলে আর একটি সার্চ করুন..
❌ 6. বটদের অপব্যবহার করবেন না। বট ব্যবহার করার আগে বট কমান্ড চেক করুন।
❌ 7. ফেক নিউজ, অশ্লীল জিনিস এবং কোন বিটকয়েন এবং ক্রিপ্টো জিনিস শেয়ার করবেন না। স্প্যাম করো না.
❌ 8. অশ্লীল/জাল ফাইল/ম্যালওয়্যার ইত্যাদি আপলোড করবেন না৷ আমরা পর্ণ বা পর্নো প্রেমীদের ঘৃণা করি না তবে আপনি এটি এখানে আপলোড করতে পারবেন না৷ গ্রুপটি সুন্দর রাখতে আমাদের সহায়তা করুন৷

আপনি কোনো নিয়ম ভঙ্গ করলে আমরা আপনাকে কোন প্রকার সাহায্য করতে পারব না...আমাদের অবশ্যই আপনাকে চিরতরে ব্যান করতে হবে।

"""
    SOURCE_TXT = """<b>NOTE:</b>

Welcome to  🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩 

✅ 1. Please Talk in Bangla/English language.
✅ 2. Respect every Member and avoid fights.
✅ 3. Search before mirroring anything Search Files in a Proper Way.
❌ 4. Don't PM anyone without asking them first. 
❌ 5. Don't Search files repeatedly, Search after one search task is complete..   
❌ 6. Don't Abuse Bots. Check Bot commands before using bots.
❌ 7. Don't  Share Fake News, Vulgar things and also No Bitcoin and crypto Things. Do Not Spam.
❌ 8. Don't upload Porn/Fake Files/Malware etc. We don't hate porn or porn lovers  but you cant upload it Here.Help us to keep the group clean.

we can't help you if you break any rules...we must ban you forever.

============G-Translated================

🇧🇩★ 𝘉𝘢𝘯𝘨𝘭𝘢𝘥𝘦𝘴𝘩 𝘏𝘰𝘢𝘳𝘥𝘪𝘯𝘨 ★🇧🇩  এ আপনাকে স্বাগতম।

✅ 1. গ্রুপে বাংলা/ইংরেজি ভাষায় কথা বলুন।
✅ 2. প্রত্যেক সদস্যকে সম্মান করুন এবং চ্যাট ফাইট এড়িয়ে চলুন।
✅ 3. কিছু মিরর করার আগে ফাইল সার্চ করুন। সঠিক উপায়ে ফাইল সার্চ করুন.
❌ 4. কাউকে প্রথমে জিজ্ঞাসা না করে মেসেজ করবেন না।
❌ 5. বারবার ফাইল সার্চ করবেন না, একটি সার্চ টাস্ক শেষ হলে আর একটি সার্চ করুন..
❌ 6. বটদের অপব্যবহার করবেন না। বট ব্যবহার করার আগে বট কমান্ড চেক করুন।
❌ 7. ফেক নিউজ, অশ্লীল জিনিস এবং কোন বিটকয়েন এবং ক্রিপ্টো জিনিস শেয়ার করবেন না। স্প্যাম করো না.
❌ 8. অশ্লীল/জাল ফাইল/ম্যালওয়্যার ইত্যাদি আপলোড করবেন না৷ আমরা পর্ণ বা পর্নো প্রেমীদের ঘৃণা করি না তবে আপনি এটি এখানে আপলোড করতে পারবেন না৷ গ্রুপটি সুন্দর রাখতে আমাদের সহায়তা করুন৷

আপনি কোনো নিয়ম ভঙ্গ করলে আমরা আপনাকে কোন প্রকার সাহায্য করতে পারব না...আমাদের অবশ্যই আপনাকে চিরতরে ব্যান করতে হবে।
"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. BDH Search should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- BDH Search Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. BDH Search supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/BangladeshHoarding)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of BDH Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
