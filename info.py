import re
from os import environ
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
#Torrent Search
ARQ_API_BASE_URL =environ.get('API_BASE_URL', 'https://thearq.tech/')

# GDrive Search Config
RESULTS_COUNT = 4  # NOTE Nuber of results to show, 4 is better
SUDO_CHATS_ID = [ 993876207, -575492766, -1001319419576, -1001190259319, -1001352599350, 1304152521, 993876207, -497415557, -1001620235788]
SUDO_CHATS_ID_GS = [ 993876207, 1304152521 ]

DRIVE_NAME = [

    "Lost_In_the_Ocene",	# 0
    "Bangla_Movies",		# 1
    "Bollywood",  		# 2
    "Hollywood",  		# 3
    "IMDB_Top_List",  		# 4
    "Collection_Pack",  	# 5    
    "South_Indian",  		# 6
    "PSA_Movies",  		# 7
    "PSA_Series",  		# 8
    "TV_Series",  		# 9
    "Courses",  		# 10
    "DC_Zero",  		# 11
    "Bot_Uploads_2",    # 12
    "APDS_1",  			# 13
    "APDS_2",  			# 14
    "APDS_1.0",  		# 15
    "APDS_1.2",  		# 16
    "APDS_1.3",  		# 17
    "APDS_2.1",  		# 18
    "APDS_2.2",  		# 19
    "APDS_2.3",  		# 20
    "APDS_2.4",  		# 21
    "Xtreme_6",  		# 22   
    "DEC_20",  			# 23
    "Jan_21",  			# 24
    "Jan_21_1",  		# 25
    "March_21",  		# 26
    "June_21",  		# 27
    "May_21",  			# 28
    "Oct_20",  			# 29
    "Sep_20",  			# 30
    "Aug_20",  			# 31
    "July_20",  		# 32
    "March_20",  		# 33
    "Xtreme_1",  		# 34
    "Xtreme_2",  		# 35  
    "Xtreme_3",  		# 36
    "Xtreme_4",  		# 37
    "Xtreme_5",  		# 38
    "Shinobi_1",  		# 39
    "Shinobi_2",  		# 40
    "RSSMO1080",  			# 1
    "RSSmo720",  			# 2
    "pcgames",  		# 3  
    "gdm1",  			# 4
    "gdm2",  			# 5
    "gdm4",  			# 6
    "gdm5",  			# 7
    "gdm6",  			# 8
    "blz1",  			# 9
    "blz2",  			# 10
    "blz3",  			# 11
    "blz4",  			# 12
    "Abrar",  			# 13
    "mhj",  			# 14
    "mhjP",  			# 15
    "mhTD1",  			# 16
    "mhTD2",  			# 17
    "mhTD3",  			# 18
    "mhTD4",  			# 19
    "mhTD5",  			# 20
    "mhTD6",  			# 21
    "mhTD7",  			# 22
    "mhTD7",  			# 23
    "ausgt21",  		# 24
    "slbots",  			# 25
    "slold_f1",  		# 26
    "slold_f2",  		# 27
    "slold_f3",  		# 28
    "slcontent_1080p",  	# 29
    "slcontent_hindi_90s",  	# 30
    "slcontent_hindi_2000",  	# 31
    "slcontens_hindi_10-14",  	# 32
    "slcon_hindi_15-17",  	# 33
    "slcon_hindi_5",  		# 34
    "Hindi_1080p",  		# 35    
]

DRIVE_ID = [

"0AJtq-dCXNVYwUk9PVA",
"1UlKMzEtvWUqmPFIgveo5Uy_jwV1qR9R_",
"1VJkDLP3bv6InG9R_W9tBC45BxU3CH0fx",
"1NSCH5JB6Bl4_zhn6yIuwRiiarvhtcHkz",
"1eYjlGPCxXP1zUDFu3O9YaeZWnbzxT-p1",
"1hAThVZuFOmG2B5PJ9nolMwr9MuM2ssN8",
"1_kXJpnyXFnRpiejZtmrUCp1DOQs5C0bf",
"19H_bD_MKRQ70qH6pCKS4z5969VdPzlaf",
"131Cl1yDNOGW0ahkB07grHGATM7Nfb2lV",
"1GhdZDc6iHisfDiUlyRkUDlWjHyeRNbk6",
"1QRljHTOJgYdgQ1iUs3GAplZPXE5vJB60",
"0ACxIdvo1MF53Uk9PVA",
"0AF6GSe5szgopUk9PVA",
"0AKhAHXxVeDP1Uk9PVA",
"0AKFcTGWfx3U9Uk9PVA",
"0AN4XtN1OGhoYUk9PVA",
"0ADPlc-eHo4JcUk9PVA",
"0AMIAQwRYOLXpUk9PVA",
"0ALGSJKwIQHweUk9PVA",
"0ALiNO3Hu006FUk9PVA",
"0ADgIvgxFERrkUk9PVA",
"0AO3RmaSwhxQ2Uk9PVA",
"1O-xmbS8QFIE0QY1AzMr3HYzPwvW5ZbYx",
"1SE4US3pprtC7lbA1CZb-LwaFGEjgnay2",
"18ngROC4tLF2uKGpo0VkE5Elp94MJMIk4",
"1sEcpXGAbhT3X7kOE1g8knbvh5jOTUx7K",
"1Au7Ed8ibC8tE0l3Tf4UNR55qM9ogkca9",
"1-SOFqWFHpckALJz437-irVhAnjzxgLkW",
"1SrbdybfP0gB8HNup2uPMYzvidT10o2qW",
"1CxdVc9C-6-sllOe8lD1IqWy1uKbvKmBD",
"1D5N5DddEoz1KCUGHjUYD3TeuqskTvbZj",
"1guot-8-dGoY1tJ2UeroBi_QkDAC_wMDS",
"1rMsivIt0M6BlZXgiOaLWmeyap8EX6YWE",
"1iGNP47SiCy-NI9h755EdtAa4hK4aaaJ5",
"164Zwctr57FGN3YmAPAHH99PueKhp7hL0",
"1O1kTFP-T2itcxslRxgqOKa4RkZto_2jf",
"1_wfopFhnP7um9a3234glOqQ6A5kUIdUE",
"1DqvkdLqBAJZTMFt-isDj09PelD_9nM7W",
"1grD_3UjRv2OtRPXgGnsVDzlpWQgcBdZx",
"1mmUK5AHB51u1GXw53i_0U_6VEf62AmHT",
"1kQU-BlpAQe_lBsKBEQ1u9HSqZU2AN2xw",
"1VCPCYGRoYPUEO7lWHukcMgHSyLD3GaT5",
"1-bVjEwoXmnG-C2bm1nQQZMtT4jO72aij",
"1C4HF43XNbgEbebN-ym0dnIwHOV_gDu8b",
"1cXxOtuR8xgsMppA1MjTsUSUktDKXQfqi",
"1fZp98s7iDRwWeW0S4Q7CQXVZbrrOGNjI",
"1zXldes4Q0CeJXTR18lZvY-4kTDgIvtHg",
"1yZ4ir37Krt5Pt0ZpaCjZ1TV5EYqmP_W6",
"1oy4zgaGt7GDMHMKzsRl37npatV48rJTu",
"1Ghz-NT_mvvlGBdDX2hrafetdAWU95gAb",
"1TFArAACVAjYz2daSBBc9jsFNbH3G16x4",
"1YlMRBZbEv4wXBbUYcyva5Qpn3ds6m0La",
"1027qKuZGLjBh3_mFBQN4ejz6eEmxeck6",
"1JPMlwGH8JHWEryjCFNeHOKxyDNF6E7Ug",
"0AGRh7-6BtgzmUk9PVA",
"0AC1woHItpMG_Uk9PVA",
"1-PWrAunH92rxLKnPbBSRrMEASMZ3jqbg",
"0ADkoqVE06_tiUk9PVA",
"0AGyxparFnWEmUk9PVA",
"0AEjlASCBDyCQUk9PVA",
"0ALZf6od8OUvYUk9PVA",
"0AJ-T74bez-XLUk9PVA",
"0ANzSPxSpWWN0Uk9PVA",
"0AHR2Pgqjg8CtUk9PVA",
"1d_nMzq_N19GFIwZn-lHjI001G8pesmb9",
"1fhbUFp9gDpyEsM47CPfS9SuyI9PrLh8c",
"1AfmXmhPnQ08xhIQq6JJ4WqXadoQ4kRIz",
"1A5W-pFBd9z5KDZMUBM0Y7FLPMRzabPVS",
"1RQZ58wka72LT_5v2IlEdwSpze-wEEyHl",
"1E8fwqoHmAe4LGbT5n_MK9AV3Y5OQNQub",
"1ZK1UnQF7ix06mYqGnRORVNYlJ7-2zZfD",
"1ZUCtEc2z5ZhOAsHHnstT1iYS35iFZJDh",
"1rHPcrPd3pQnFVf1eqRDSQgm08PKC13zg",
"1GHzj9fsxnW9mYdXZ9dA8oRhY0fb0PAL7",
"1TbmPQD_ffLcQ24tJ3yuxD4RgP50Se2Rk",
"1ZcuWM29L6Gb2pLH5cMIY-9mruNPBU2IM",
"1PGEUJApE-ORfxyQfcio3RaIVHfFvAORI",
"1WRZjg9Z4ls2EWOWomDdpMC7NkwmPFmLZ",
"1tat-X_7oS8SlA45uX6hrcm5gyS9MbnmK",
"1VMu38EPKM1XBfzK7u2wn5nwuc2cJMvEf",
"1vJmoqJi0SqUEAqluKAQ4u5z1y-LKIIJu",
"1udZ58YOrRU-E2bbsgSrjpeSrEVTfQQBu",
"1n-XXOw4FADHZLX3q9B8xBNud64PoNugE",
"10bSAOuwjZUEfep0hYP5ZIJwyhAab9ApL",
"1RPYqFN-qwrXqZjRY07ahpGLhg5-nSQN6",
"1HhxDjKidxgdOfx9WMckOkKUkDixxGAoQ",
"19eITtEIH0dMLlZ67Eb8Wc_zI2yWVx7Co",
"1lkyAUBAYcxdOxHr7fAsv3T-D6JAv60W4",
"1dryi92O0xv9g2GH57_-lV7xPPIASR0I2",
"1bFzSXdvKwTYNsqssAxsIP9KjAyNyHNn1",
"1NvnN0QfeYP096Hv6Ly_iCBMlln1Kp0om",
"1_rFKpzwgZL3iJgV5gcxBpTqQnx7h9eEs",
"16czVI9ZwNUQRIio1XOWrxxGyoGCg4g5M",
"1f9zhCcAetn7TuUlB8z8e-lh_GtnJu_zn",
"1fD9TrkOdq6SboKe9f2GXJTK4sQDcwb7t",
"1rOzV8l7pRJE_NnQ97pIP1GtyAWwvfZAE",
"1LG4InWLqXGqKscDgZK83J94hg0WH7Uqo",
"1YHOTmXEBH3Q912qwswscI-hNSBpkXlmi",
"1AjcQZqCgLZXEX_XDOQi6HbSjpaa4sNco",
"1dCvd0gePZV_B3kfr2kK2XuigD30cmXLh",
"1GujcqvJVX4A7WQ_akLkCWHQSIUy_yEFS",
"1B6A8T8s8R-hXEaNO_0v59GeAvVBnCGTT",
"1HaI4zz_qDLgvLlO5UL3M3sZq0J8qox_j",
"1StegCht11U_dZzQdthz3iysQi8Sj8dZw",
"1sUPKffhIwcm0K69htrhi0WuoPZkEhDBi",
"1t_rzu4I-aAu6ySkWzCyYpZ9vKJEEjiA0",
"1kb-j_doUidBuO496dGArkJ2J4NC3AglE",
"19OUCSLvVL9Fc_d5LhNhvKBkTNRxTjFdP",
"1DVd19-RtHe4f89OlN_iq9rLEG0U4Vufc",
"1Ac7LCB0RLLXXMxHIYF1GVRxuymdjXbaa",
"1Zvmac5W_t1S2bnRY01yjzUmdaSE90TuH",
"1ilWTJpwO6Txt_7XGACDYCk2CNKT2FgEK",
"1IsdQXGAPLhPfaoGvdYN8TRvdMBbepPnP",
"1tJtdfK79kOsLGpPITfuklriNUkTghq6c",
"1G3HsKLawDT4XeC-SwGY3O1hIwaDcdlM9",
"189k827BYKOCJlLnrgech6v0kuuBRlTmn",
"1nFQmpnlAaqZdqRRjZ5iSzWTauZDS-guz",
]

INDEX_URL = [

"http://search.indexbd.cf/0:",
"http://search.indexbd.cf/1:",
"http://search.indexbd.cf/2:",
"http://search.indexbd.cf/3:",
"http://search.indexbd.cf/4:",
"http://search.indexbd.cf/5:",
"http://search.indexbd.cf/6:",
"http://search.indexbd.cf/7:",
"http://search.indexbd.cf/8:",
"http://search.indexbd.cf/9:",
"http://search.indexbd.cf/10:",
"http://search.indexbd.cf/11:",
"http://search.indexbd.cf/12:",
"http://search.indexbd.cf/13:",
"http://search.indexbd.cf/14:",
"http://search.indexbd.cf/15:",
"http://search.indexbd.cf/16:",
"http://search.indexbd.cf/17:",
"http://search.indexbd.cf/18:",
"http://search.indexbd.cf/19:",
"http://search.indexbd.cf/20:",
"http://search.indexbd.cf/21:",
"http://search.indexbd.cf/22:",
"http://search.indexbd.cf/23:",
"http://search.indexbd.cf/24:",
"http://search.indexbd.cf/25:",
"http://search.indexbd.cf/26:",
"http://search.indexbd.cf/27:",
"http://search.indexbd.cf/28:",
"http://search.indexbd.cf/29:",
"http://search.indexbd.cf/30:",
"http://search.indexbd.cf/31:",
"http://search.indexbd.cf/32:",
"http://search.indexbd.cf/33:",
"http://search.indexbd.cf/34:",
"http://search.indexbd.cf/35:",
"http://search.indexbd.cf/36:",
"http://search.indexbd.cf/37:",
"http://search.indexbd.cf/38:",
"https://dontabuse:shinobicloud@one.shinobi.workers.dev/0:/Bot_1",
"https://dontabuse:shinobicloud@two.shinobi.workers.dev/0:/Bot_2",
"http://search2.indexbd.cf/1:",
"http://search2.indexbd.cf/2:",
"http://search2.indexbd.cf/3:",
"http://search2.indexbd.cf/4:",
"http://search2.indexbd.cf/5:",
"http://search2.indexbd.cf/6:",
"http://search2.indexbd.cf/7:",
"http://search2.indexbd.cf/8:",
"http://search2.indexbd.cf/9:",
"http://search2.indexbd.cf/10:",
"http://search2.indexbd.cf/11:",
"http://search2.indexbd.cf/12:",
"http://search2.indexbd.cf/13:",
"http://search2.indexbd.cf/14:",
"http://search2.indexbd.cf/15:",
"http://search2.indexbd.cf/16:",
"http://search2.indexbd.cf/17:",
"http://search2.indexbd.cf/18:",
"http://search2.indexbd.cf/19:",
"http://search2.indexbd.cf/20:",
"http://search2.indexbd.cf/21:",
"http://search2.indexbd.cf/22:",
"http://search2.indexbd.cf/23:",
"http://search2.indexbd.cf/24:",
"http://search2.indexbd.cf/25:",
"http://search2.indexbd.cf/26:",
"http://search2.indexbd.cf/27:",
"http://search2.indexbd.cf/28:",
"http://search2.indexbd.cf/29:",
"http://search2.indexbd.cf/30:",
"http://search2.indexbd.cf/31:",
"http://search2.indexbd.cf/32:",
"http://search2.indexbd.cf/33:",
"http://search2.indexbd.cf/34:",
"http://search2.indexbd.cf/35:",
"https://s2.packsindex.workers.dev/0:/10bit%20Collection",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/10bit",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/3xO",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/afm72",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/ArcX",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/Balthallion",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/bandi",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/d3g",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/DUHiT",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/Frys",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/Goki",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/HxD",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/joy",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/kappa",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/Natty%20(QXR)",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/prof",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/qman",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/r0b0t",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/r00t",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/Ranvijay",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/sampa",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/TombDoc",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/Vyndros",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/Weasly%20HONE",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/Weasly%20HONE%202",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/XXXPAV69%20",
"https://s2.packsindex.workers.dev/0:/30+%20Encoders%20Collection%20[50%20TB]/YOGI",
"https://s2.packsindex.workers.dev/0:/3000+%20Movies%20Random%20Collection",
"https://s2.packsindex.workers.dev/0:/Documentary%20Movies%20Collection",
"https://s2.packsindex.workers.dev/0:/Hevcbay%20Collection",
"https://s2.packsindex.workers.dev/0:/JYK%20Encodes%20Collection/JYK.720p.BRRip",
"https://s2.packsindex.workers.dev/0:/JYK%20Encodes%20Collection/JYK.1080p.BluRay%20(A-Z)/JYK.1080p.BluRay.A-L%20[691GB]",
"https://s2.packsindex.workers.dev/0:/JYK%20Encodes%20Collection/JYK.1080p.BluRay%20(A-Z)/JYK.1080p.BluRay.M-Z%20[747GB]",
"https://s2.packsindex.workers.dev/0:/ShiNobi/MOVIES",
"https://s2.packsindex.workers.dev/0:/ShiNobi/ShiNobi",
"https://s2.packsindex.workers.dev/0:/ShiNobi/TV%20SERIES",
"https://s2.packsindex.workers.dev/0:/Tigole%20Complete%20Collection/tigole%20-%20unsorted",
"https://s2.packsindex.workers.dev/0:/Tollywood%20Collection/Tollywood%20Movies",
"https://s2.packsindex.workers.dev/0:/TombDoc%20Collection",
"https://s2.packsindex.workers.dev/0:/TombDoc%20Collection/!Series",
"http://search2.indexbd.cf/0:",
]
