#!/usr/bin/env python3

import time
import random
import re
from pyrogram import Client

# Replace these with your own values

api_id = '27398278'
api_hash = '7cfce511b5a1d7e3d759f8ff633f0ef5'
phone_number = '+250791309988'

# Input list of Telegram channels here
groups = [
    "https://t.me/eminentlegitworks",
    "https://t.me/bagthebread",
    "https://t.me/SwerveShops",
    "https://t.me/nonstopchop",
    "https://t.me/richhome11",
    "https://t.me/LOCKYZVERIFIEDHIT",
    "https://t.me/sanemarketing",
    "https://t.me/everybodyeatsfytb",
    "https://t.me/Orderseatsrides",
    "https://t.me/windsales",
    "https://t.me/scamfam18",
    "https://t.me/localscammers91",
    "https://t.me/fbiz247",
    "https://t.me/thewoosmoke",
    "https://t.me/DrugKoden",
    "https://t.me/WKF_Group",
    "https://t.me/TREETGOOD",
    "https://t.me/Thewoochat",
    "https://t.me/fraudstars123",
    "https://t.me/usagold12cashbtc1",
    "https://t.me/INGODWETRVST",
    "https://t.me/DTC_IPIP",
    "https://t.me/BinsAndMethodsSauce",
    "https://t.me/CCShowChat",
    "https://t.me/CashappServicesChat",
    "https://t.me/aiocrime2",
    "https://t.me/BusinessGruppa",
    "https://t.me/LegitWorkers",
    "https://t.me/LEGITTDEALS",
    "https://t.me/legitcreme",
    "https://t.me/LeTHelPThENeeDs300",
    "https://t.me/Bestteamcarder",
    "https://t.me/AlphaMarket",
    "https://t.me/globalfinancenetworkers",
    "https://t.me/afrishop2019",
    "https://t.me/fraudway",
    "https://t.me/TradeMarkFullz",
    "https://t.me/gwopchasers",
    "https://t.me/CHOPDONTSTOP2021",
    "https://t.me/thegarage9",
    "https://t.me/mine_olymp",
    "https://t.me/GangMarket300",
    "https://t.me/Fraud_City",
    "https://t.me/Wealleatalready",
    "https://t.me/LEEBOSSWELL",
    "https://t.me/hutsonrexCS12",
    "https://t.me/joingroomcarder",
    "https://t.me/H_T_P1",
    "https://t.me/escrow1",
    "https://t.me/limitlessdealers",
    "https://t.me/CaLounge",
    "https://t.me/Ttp44",
    "https://t.me/DatingsitesLogins",
    "https://t.me/General_Business",
    "https://t.me/Thejunglemarket",
    "https://t.me/Twopac28",
    "https://t.me/saltedstore",
    "https://t.me/OGUsernames",
    "https://t.me/cardinguschat",
    "https://t.me/TrustedMarket",
    "https://t.me/adsment",
    "https://t.me/BreadWs",
    "https://t.me/projecttgmarket",
    "https://t.me/a1sell",
    "https://t.me/PowerMarketing",
    "https://t.me/FnayShopChat",
    "https://t.me/BankLords",
    "https://t.me/Bigdope12",
    "https://t.me/jwettinest",
    "https://t.me/PlMPS",
    "https://t.me/YDOpenmarket",
    "https://t.me/logsgang1",
    "https://t.me/royalmarkets",
    "https://t.me/platinummarket",
    "https://t.me/fraudgodbinochatslatt",
    "https://t.me/swiper_goddd",
    "https://t.me/baguaqilai",
    "https://t.me/Pos_on_off",
    "https://t.me/LucifersMarket",
    "https://t.me/spaminferno",
    "https://t.me/Multitips3",
    "https://t.me/Futureboost",
    "https://t.me/trapexclude",
    "https://t.me/fuckthebanks1",
    "https://t.me/spamitalia_ita",
    "https://t.me/hqmoneyhub",
    "https://t.me/buysellplace",
    "https://t.me/DarksideForum",
    "https://t.me/chatroom099",
    "https://t.me/CvByLoryeJerry",
    "https://t.me/nbaszn",
    "https://t.me/DiggerAndCo",
    "https://t.me/FRAUD667",
    "https://t.me/exoticcfraudz",
    "https://t.me/scam2amily",
    "https://t.me/holygangshit",
    "https://t.me/dark3conomy",
    "https://t.me/bandonoproblem20",
    "https://t.me/legitdumps101201",
    "https://t.me/Moneystopnonsen",
    "https://t.me/how2berich",
    "https://t.me/BINS5",
    "https://t.me/universalspam",
    "https://t.me/seller_11008",
    "https://t.me/WerbungDeutschland",
    "https://t.me/willgotbins",
    "https://t.me/WinnersWayy",
    "https://t.me/Bitcoin_Hong_Kong",
    "https://t.me/STR88PROF",
    "https://t.me/SofacySecurityAffairs",
    "https://t.me/MoneyMakingMethodz",
    "https://t.me/whitewookies",
    "https://t.me/bankbookbusiness2211",
    "https://t.me/sanwellsofficialchat",
    "https://t.me/choppingnetwork",
    "https://t.me/huslehardi",
    "https://t.me/KillerDumps45",
    "https://t.me/tavosdicechat",
    "https://t.me/Honorablemention1010",
    "https://t.me/BuYeRssAnDsElLeRss",
    "https://t.me/letseatfam",
    "https://t.me/SCAMDEMICTRAPERS",
    "https://t.me/basetoolscarders",
    "https://t.me/GlobalCompravendita0",
    "https://t.me/ScammersChat",
    "https://t.me/TrueToSwipe",
    "https://t.me/ScamStarrs",
    "https://t.me/Saynotoripper",
    "https://t.me/letsmakebands",
    "https://t.me/NYCCARDER",
    "https://t.me/Renofficialgroup",
    "https://t.me/validcreditcredit550",
    "https://t.me/fraud_harem",
    "https://t.me/unknownxsimplemindedman",
    "https://t.me/bestsauxe",
    "https://t.me/consenting",
    "https://t.me/TrapScamily",
    "https://t.me/BTO101",
    "https://t.me/swoonchat",
    "https://t.me/openmarketchat",
    "https://t.me/MoneyMoves6xx",
    "https://t.me/ONLY50CHAT",
    "https://t.me/legitfa",
    "https://t.me/mostwantedsauce",
    "https://t.me/Worldbanking1"
]

# Function to extract the username/channel name from the URL
def extract_username(url):
    match = re.search(r't\.me\/([a-zA-Z0-9_]+)', url)
    if match:
        return match.group(1)
    return None

# Create a Pyrogram Client
app = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

async def join_channels():
    async with app:
        for channel_url in groups:
            username = extract_username(channel_url)
            #username = channel_url
            if username:
                try:
                    await app.join_chat(username)
                    print(f"Successfully joined {channel_url}")
                except Exception as e:
                    print(f"Failed to join {channel_url}: {e}")
                delay = random.randint(300, 600) # I made a random delay in between joining channels/groups of 300 to 600 sec
                time.sleep(delay)
            else:
                print(f"Invalid URL format: {channel_url}")

if __name__ == "__main__":
    app.run(join_channels())
