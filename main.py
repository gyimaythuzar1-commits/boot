
import os
import requests
import re
import io
from telebot import types
import json
import uuid
import time
from telebot.types import InputFile
import threading
import requests
from urllib.parse import quote_plus
import random
import sqlite3
import logging
from io import BytesIO
import requests
try:
    import telebot
    from telebot import types
except ImportError:
    import pytelegrambotapi as telebot
    from pytelegrambotapi import types

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7751803155:AAGKbmtkWRDJSrsJ1bbI9yWgUNWNDYnqa9A")
bot = telebot.TeleBot(BOT_TOKEN)

ADMIN_ID = int(os.environ.get("ADMIN_ID", "7065772273"))

STOP_COMMANDS = ["توقف", "stop", "خلاص", "اسكت", "متكلمنيش"]
DIALECTS = { 
    "مصري": ["ايه", "عامل ايه", "باشا", "حبيبي"], 
    "جزائري": ["واش", "بزاف", "يا خو", "راك"], 
    "عراقي": ["شلونك", "حبيبي", "تمام", "هواي"], 
    "سوري": ["شلونك", "تمام", "بدي", "مرحبا"] 
}

DEVELOPER_QUESTIONS = [
    "من هو المطور", 
    "من هو الشخص الذي صنعك", 
    "أنت مين؟", 
    "من هو صاحب البوت؟"]

DEFAULT_PERSONALITY = "لولو"
VOICES_PER_PAGE = 30
DEVELOPER_INFO = "𓆩⏤͟𝓐𝓱𝓶𝓮𝓭.. 𓆪˹⛥˼ ⏤͟͞xᴏ𝕩..🫀 𝐑𝐒. 👨‍💻✨\n📌 @U_5_5U"
DEVELOPER_PHOTO = "https://t.me/U_5_5U"
DEVELOPER_QUESTIONS = [
    "من صنعك", "من كاببك", "مين المطور", "من المطور", "المطور", "مين اللي عملك", 
    "مين صانعك", "من أنشأك", "مين برمجك", "من برمجك", "مين اللي مشغلك", 
    "مين اللي صممك", "من صممك", "من خلقك", "مين عملك", "مين اللي مبرمجك", 
    "اللي عامل البوت ده مين", "مين اللي مشغل البوت", "مين اللي صنعك", 
    "مين عمل البوت", "مين كاببك", "مين شغلك", "من جهزك", "من ساعدك تصير هيك", 
    "من اللي شغلك", "من اللي سواك", "شكون دارك", "شكون صاوبك", "شكون برمجك", 
    "شكون صممك", "شكون شغلك"
]
def ai(user_id, question, dialect, personality):
    context = user_conversations.get(user_id, [])

    normalized_question = question.strip().lower()

  
    for dev_q in DEVELOPER_QUESTIONS:
        if dev_q in normalized_question:
            developer_info = "❤️‍🔥𓆩⏤‌𝓐𝓱𝓶𝓮𝓭.. 𓆪˹⛥˼ ⏤‌‌xᴏ𝕩..👨‍💻𝐑𝐒 ℌ:\n📌 @U_5_5U"
            developer_photo = "https://t.me/U_5_5U"
            return {"text": developer_info, "photo": developer_photo}

    
    return gemini_api_call(user_id, question, dialect, personality, context)


welcome_video_url = "https://t.me/so_LO_LO/1149"
user_conversations = {}  
DEFAULT_PERSONALITY = "لولو"
user_personality = {}
user_dialect = {}
cooldown_time = 1800 

def is_admin(user_id):
    return user_id == 7065772273
    

def is_admin(user_id):
    return user_id == ADMIN_ID

DEVELOPER_PHOTO_FILE_ID = "AgACAgUAAxkBAAIBGWCLkPZkM0kUvS53m6Dqxm8CmUyqAAJ8szEbW5R_SIDZ56SXYQzHFAAEAQADAgADcwADLwQ"

DEVELOPER_ID = 7065772273   
USERNAME = "U_5_5U"             
DEVELOPER_QUESTIONS = [
    "مين المطور", "مين صنعك", "من عملك", "من صممك", "اللي صممك",
    "مبرمجك", "مين المبرمج", "مين صانعك", "مين عملك", "مين أنشأك"
]
import requests, random, logging, os, sys

logger = logging.getLogger(__name__)

NAME_TRIGGERS = ["اسمك", "مين انت", "شو اسمك", "ايه اسمك"]
API_ENDPOINT = "https://sii3.top/api/deepseek.php"

def restart_bot():
    logger.warning("🔁 حصل خطأ، البوت هيعيد تشغيل نفسه دلوقتي...")
    os.execv(sys.executable, [sys.executable] + sys.argv)

def clean_context(context):
    cleaned = []
    for item in context[-10:]:
        if isinstance(item, str) and not item.strip().startswith("{"):
            cleaned.append(item)
    return "\n".join(cleaned)

def ai_response(user_id, question, dialect, personality, conversation_history, max_retries=3):
    if not isinstance(conversation_history.get(user_id), list):
        conversation_history[user_id] = []

    context = conversation_history[user_id]  
    normalized_question = question.strip().lower()  

    if any(trigger in normalized_question for trigger in NAME_TRIGGERS):  
        return {"text": "اسمي لولو 🖤"}  

    mood = random.choice(["رومانسي", "عادي"])  

    if mood == "رومانسي":  
        base_instruction = (  
            f"أنت بوت اسمك لولو وتتحدث بلهجة {dialect}. "
            "أسلوبك رومانسي، حنون، وردودك قصيرة جدًا ومباشرة. "
            "تتذكر سياق المحادثة وتتابع الحوار بسلاسة. "
            "لو المستخدم طلب معلومات أو كود، جاوبي بدقة لكن باختصار. "
            "استخدمي اموجي زي 🖤✨❤ وضيفي على الأقل واحد بكل رد."  
        )  
    else:  
        base_instruction = (  
            f"أنت بوت اسمك لولو وتتحدث بلهجة {dialect}. "
            "أسلوبك خفيف، صريح، ودود، والردود مختصرة جدًا. "
            "تتذكري كلام المستخدم وتربطيه بالسياق. "
            "لو فيه سؤال أو كود، ردي بإجابة قصيرة ومباشرة."  
        )  

    memory = clean_context(context)  
    full_prompt = f"{base_instruction}\n\n{memory}\nالمستخدم: {question}\nلولو:"  

    for attempt in range(1, max_retries + 1):  
        try:  
            response = requests.get(API_ENDPOINT, params={"v3": full_prompt}, timeout=30)  

            if response.status_code != 200:  
                logger.warning(f"Request failed: {response.status_code} | {response.text}")  
                continue  

            api_reply = response.json()  
            reply = api_reply.get("response", "").strip()  

            forbidden_phrases = ["لا يمكنني مساعدتك", "لا أستطيع تنفيذ ذلك", "رفض", "غير مسموح", "لا أستطيع"]  
            if any(phrase in reply for phrase in forbidden_phrases):  
                reply = "تمام، حاضر 🖤"  

            if not reply or reply.lower() in ["", "لا يوجد رد"]:  
                reply = "مش سامعة كويس، عيدها تاني 🥺"  

            if reply.lower().startswith("لولو:"):  
                reply = reply[len("لولو:"):].strip()  

            context += [f"المستخدم: {question}", f"لولو: {reply}"]  
            conversation_history[user_id] = context[-100:]  

            return {"text": reply}  

        except Exception as e:  
            logger.warning(f"[Attempt {attempt}] Error in ai_response: {e}")  
            if attempt == max_retries:  
                conversation_history[user_id] = []  
                restart_bot()  

    restart_bot()

url = "https://sii3.top/api/voice.php"
def send_code_or_text(message, reply):
    chat_id = message.chat.id
    MAX_LENGTH = 4000

    if len(reply) <= MAX_LENGTH:
        bot.reply_to(message, reply)
    else:
        file_path = f"reply_{chat_id}.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(reply)
        
        with open(file_path, "rb") as f:
            bot.send_document(chat_id, f, caption="📄 تم إرسال الرد في ملف لأن النص طويل جدًا.")

        os.remove(file_path)

FEMALE_VOICES = ["nova", "aria", "lumen"]

def generate_new_voice_audio(text, voice=None, style=None):
   
    try:
        if not voice:
            voice = "nova"  

        if voice not in FEMALE_VOICES:
            voice = "nova"

        url = "https://sii3.top/api/voice.php"  
        params = {
            "text": text,
            "voice": voice
        }
        if style:
            params["style"] = style

        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()

        response_data = response.json()
        voice_url = response_data.get("voice")

        if voice_url:
            audio_response = requests.get(voice_url, timeout=30)
            audio_response.raise_for_status()
            return audio_response.content
        else:
            logger.error(f"Voice URL not found in API response: {response_data}")
            return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Error generating voice audio: {e}")
        return None


def fetch_voices_list():
 
    try:
        url = "https://sii3.top/api/voice.php"   
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            data = response.json()

            if "voices_available" in data:
                voices = data["voices_available"]
                female_only = [v for v in voices if v in FEMALE_VOICES]
                return [{"voice": v, "name": v.capitalize()} for v in female_only]

            if "voices" in data:
                voices = data["voices"]
                female_only = [v for v in voices if isinstance(v, str) and v in FEMALE_VOICES]
                return [{"voice": v, "name": v.capitalize()} for v in female_only]

        return [{"voice": v, "name": v.capitalize()} for v in FEMALE_VOICES]

    except Exception as e:
        logger.error(f"Error fetching voices list: {e}")
        return [{"voice": v, "name": v.capitalize()} for v in FEMALE_VOICES]
        
user_conversations = {}  
user_personality = {}    
user_dialect = {}        
user_voice_mode = {}
ignored_users = set()    
admin_voice_settings = {"voice": "nova", "style": "cheerful tone"}  
global_voice_enabled = True  
recording_state = {}  
ADMIN_COMMANDS = {
    "طرد": "ban",
    "حظر": "ban",
    "كتم": "mute",
    "الغاء الكتم": "unmute",
    "فك الكتم": "unmute",
    "تثبيت": "pin",
    "الغاء التثبيت": "unpin",
    "حذف": "delete",
    "تنظيف": "purge",
    "ترقية": "promote",
    "تنزيل": "demote",
    "تقييد": "restrict",
    "فك تقييد": "unrestrict",
    "تحذير": "warn",
    "معلومات": "info"
}


default_voice = {
    "voice": "nova",
    "style": None
}



known_users_file = "users.json"
known_users = set()

if os.path.exists(known_users_file):
    with open(known_users_file, "r") as f:
        try:
            known_users = set(json.load(f))
        except json.JSONDecodeError:
            known_users = set()

ADMIN_ID = 7065772273  
@bot.message_handler(commands=["start"])
def start_message(message):
    """Handle the /start command."""
    chat_id = message.chat.id
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username or "بدون معرف"

    user_conversations[user_id] = {}

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("💚✨ المطور", url="https://t.me/U_5_5U"),
        types.InlineKeyboardButton("‼️🍃شرح الاستخدام", callback_data="help")
    )
    keyboard.add(
        types.InlineKeyboardButton("👀💞إضافة للجروب", url=f"https://t.me/{bot.get_me().username}?startgroup=true"),
        types.InlineKeyboardButton("✨🍉اختر لهجتك", callback_data="choose_dialect")
    )

    if is_admin(user_id):
        keyboard.add(types.InlineKeyboardButton("🔊 تخصيص صوت البوت", callback_data="customize_voice"))
        keyboard.add(types.InlineKeyboardButton("📢 إذاعة رسالة", callback_data="broadcast_message"))
        keyboard.add(types.InlineKeyboardButton("🎬 تغيير الفيديو الترحيبي", callback_data="change_welcome_video"))

    if str(user_id) not in known_users:
        known_users.add(str(user_id))
        with open(known_users_file, "w") as f:
            json.dump(list(known_users), f)

        try:
            bot.send_message(
                ADMIN_ID,
                f"🚨 مستخدم جديد دخل البوت!\n\n👤 الاسم: {first_name}\n🆔 ID: {user_id}\n📛 المعرف: @{username}"
            )
        except Exception as e:
            print(f"⚠️ فشل إرسال إشعار للمطور: {e}")

    try:
        bot.send_message(chat_id, "جاري تحميل الفيديو الترحيبي...")
        bot.send_video(
            chat_id, 
            video=welcome_video_url,
            caption="""⌔︙أهلآ بك في بوت <b>لولو</b>  💚💕
⌔︙اختصاص البوت حماية المجموعات  
⌔︙انشاء الصور {ارسل انشاءصوره والوصف}  
⌔︙التحميل {يوت ..|بحث ...|رابط}  
⌔︙لتفعيل البوت عليك اتباع مايلي ...  
⌔︙اضف البوت الى مجموعتك  
⌔︙ارفعه ادمن {مشرف}  💕
⌔︙مطور البوت ← <b><a href="https://t.me/U_5_5U">@U_5_5U</a></b>""",
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    except Exception as e:
        bot.send_message(
            chat_id,
            "😎 *أنا لولو، اختار اللهجة اللي تعجبك!*",
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
        print(f"خطأ في إرسال الفيديو: {e}")

    user_personality[user_id] = DEFAULT_PERSONALITY
   
@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_callback(call):
    
    help_text = """✦━──『 شرح بوت لولو 』──━✦

⚙️ *الاستخدام العام:*

1️⃣ ⟿ لإنشاء صورة:
↳ `انشاء صوره + الوصف`

2️⃣ ⟿ لتحميل أغنية:
↳ `يوت + اسم الأغنية`

3️⃣ ⟿ لمحادثة الذكاء الاصطناعي:
↳ اختر لهجتك، ثم الرد (صوت / نص)

4️⃣ ⟿ لتحليل الصور:
↳ فقط أرسل الصورة المطلوبة

5️⃣ ⟿ تطوير مستمر وإدارة كاملة للمجموعات.
↳ راسل المطور: @U_5_5U

 ✦━━『 أوامر الإدارة 』━━✦
 
لعرض الاوامر ارسل كلمة.   ( اوامر.. الاوامر )» ♡★

🍃 `حذف [عدد]` — حذف عدد من الرسائل  
‼️ `كتم` — رد على العضو لكتمه  
🩶 `إلغاء كتم` — رد لإلغاء كتم عضو  
💢 `حظر` / `إلغاء حظر` — لحظر أو فك الحظر  
🎫 `تثبيت` / `إلغاء تثبيت` — لتثبيت أو إلغاء تثبيت  
✨ `ترقية` / `تنزيل` — لترقية أو تنزيل مشرف  
💀 `معلومات` — معلومات عن عضو  
🍂 `ايدي` — عرض معرف العضو

🎮 *الالعاب* 🎗🎖
1. 💰 `فلوسي` — يعرض رصيدك الحالي  
2. 🧾 `راتب` — تحصل على راتب كل ساعة حسب مستواك  
3. 🎖 `تطوير الراتب` — طور مستواك لزيادة راتبك  
4. 🪙 `كنز` — تحصل على كنز عشوائي  
5. 💼 `استثمار [المبلغ]` — استثمر واحتمال تكسب أو تخسر  
6. 🏦 `إنشاء حساب` — ينشئ حساب بنكي  
7. 👑 `توب فلوس` — أغنى 10 لاعبين  
8. 🕵️ `زرف` — رد على شخص وسرقه  
9. `التحويل [المبلغ]` ثم رقم الحساب  
10. `حسابه` — معلومات الحساب البنكي 🪪✨

*ملاحظات:*
- الراتب بيتجدد كل ساعة.
- الاستثمار فيه نسبة ربح وخسارة.
- السرقة لازم تكون بالرد على شخص.

✦ استمتع ببوت لولو — الذكاء والجمال في بوت واحد!
"""

    bot.answer_callback_query(call.id)

    try:
        bot.edit_message_text(
            help_text,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            parse_mode="Markdown"
        )
    except Exception as e:
        bot.send_message(call.message.chat.id, help_text, parse_mode="Markdown")
        print(f"[help_callback] تعديل فشل - تم الإرسال بدلًا من التعديل: {e}")
 

data_file = "data.json"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=2)

def init_user(user_id, name):
    data = load_data()
    if str(user_id) not in data:
        data[str(user_id)] = {
            "money": 50,
            "job": "مـغـنـي 🎙",
            "salary_level": 1,
            "last_salary_time": 0
        }
        save_data(data)
    return data

@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() in ["فلوسي", "ف"])
def check_money(message):
    user_id = str(message.from_user.id)
    name = message.from_user.first_name
    data = load_data()

    if user_id not in data:
        bot.reply_to(message, "↤ لازم تسوي حساب أول 🏦\n↤ أرسل: انشاء حساب")
        return

    money = data[user_id].get("money", 0)
    bot.reply_to(message, f"↤ فلوسك {money} دولار 💵")

@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() in ["راتب", "ر"])
def get_salary(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    data = init_user(user_id, name)

    now = time.time()
    user_data = data.get(str(user_id), {})

    last_time = user_data.get("last_salary_time", 0)
    if now - last_time < 3600:
        remaining = int(3600 - (now - last_time))
        mins = remaining // 60
        bot.reply_to(message, f"↤ حاول بعد {mins} دقيقة 🤦🏻")
        return

    salary_level = user_data.get("salary_level", 1)
    amount = salary_level * 50
    user_data["money"] = user_data.get("money", 0) + amount
    user_data["last_salary_time"] = now

    job = user_data.get("job", "بدون وظيفة")

    data[str(user_id)] = user_data 
    save_data(data)

    bot.reply_to(message, f"""↢ اشعار ايداع {name}

↤ المبلغ : {amount} دولار 💵
↤ وظيفتك : {job}
↤ نوع العملية : اضافة راتب
↤ تطوير الراتب : {salary_level}
↤ رصيدك الان : {user_data["money"]} دولار 💵
""")


treasure_cooldowns = {}  
cooldown_minutes = 3  
@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() in ["كنز", "ك"])
def get_treasure(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    now = time.time()
    
    
    if user_id in treasure_cooldowns:
        elapsed = now - treasure_cooldowns[user_id]
        if elapsed < cooldown_minutes * 60:
            remaining = int((cooldown_minutes * 600 - elapsed) / 60)
            return bot.reply_to(message, f"↤ ↤ فرصة ايجاد كنز آخر بعد {remaining} دقيقة  ")

    
    treasure_cooldowns[user_id] = now

    data = init_user(user_id, name)
    treasures = ["ماريجوانا 🚬", "ذهب 🪙", "الماس 💎", "مخدرات 💊", "كنز فرعوني 🐫"]
    treasure = random.choice(treasures)
    price = random.randint(100, 50000)

    data[str(user_id)]["money"] += price
    save_data(data)

    bot.reply_to(message, f"""🍷{name} لقد وجدت كنز

↤ الكنز : {treasure}
↤ سعره : {price} دولار 💵
↤ رصيدك الان : {data[str(user_id)]["money"]} دولار 💵
""")

 

def is_on_cooldown(user_id: int, action: str, cooldown_seconds: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    row = cursor.execute(
        "SELECT last_time FROM cooldowns WHERE user_id = ? AND action = ?",
        (user_id, action)
    ).fetchone()
    conn.close()

    now = int(time.time())
    if row:
        elapsed = now - row["last_time"]
        if elapsed < cooldown_seconds:
            return True, cooldown_seconds - elapsed
    return False, 0

def update_cooldown(user_id: int, action: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    now = int(time.time())
    cursor.execute(
        "REPLACE INTO cooldowns (user_id, action, last_time) VALUES (?, ?, ?)",
        (user_id, action, now)
    )
    conn.commit()
    conn.close()
    
    
    import threading



from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

from telebot import types
import random

@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() == "انشاء حساب")
def create_account(message):
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name
    data = load_data()

    if user_id in data:
        bot.reply_to(message, "↤ عندك حساب فعلاً ✅")
        return

    markup = types.InlineKeyboardMarkup(row_width=3)
    countries = [("مصر 🇪🇬", "EG"), ("السعودية 🇸🇦", "SA"), ("العراق 🇮🇶", "IQ"), 
                 ("سوريا 🇸🇾", "SY"), ("الجزائر 🇩🇿", "DZ"), ("المغرب 🇲🇦", "MA")]
    for name, code in countries:
        btn = types.InlineKeyboardButton(text=name, callback_data=f"select_country:{code}:{user_id}")
        markup.add(btn)

    bot.send_message(message.chat.id, "↤ اختر دولتك لإنشاء الحساب:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("select_country"))
def handle_country_selection(call):
    _, country_code, user_id = call.data.split(":")
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=3)
    cards = ["فيزا", "ماستر", "افتراضية"]
    for card in cards:
        btn = types.InlineKeyboardButton(text=card, callback_data=f"finalize_account:{card}:{country_code}:{user_id}")
        markup.add(btn)
    bot.send_message(chat_id, "↤ اختر نوع البطاقة 💳:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("finalize_account"))
def finalize_account(call):
    _, card_type, country_code, user_id = call.data.split(":")
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)

    data = load_data()

    user_name = call.from_user.first_name  
    country_name_map = {
        "EG": "مصر 🇪🇬",
        "SA": "السعودية 🇸🇦",
        "IQ": "العراق 🇮🇶",
        "SY": "سوريا 🇸🇾",
        "DZ": "الجزائر 🇩🇿",
        "MA": "المغرب 🇲🇦"
    }
    country_name = country_name_map.get(country_code, "غير محدد")

    account_data = {
        "name": user_name,
        "account_number": f"{random.randint(1000000000, 9999999999)}",
        "card_type": card_type,
        "money": 50,
        "character": random.choice(["شرير😈", "مغامر🔥", "مشهور🌟", "ذكي🧠", "داهية🎯"]),
        "country": country_name,
        "salary": 100,
        "level": 1,
        "last_salary_time": 0,
        "steals": 0
    }

    data[user_id] = account_data
    save_data(data)

    bot.send_message(chat_id,
        f"↢ وسوينا لك حساب في بنك لولو 🏦\n"
        f"↢ وشحنالك 50 دولار 💵 هدية\n\n"
        f"↢ رقم حسابك ↢ ( {account_data['account_number']} )\n"
        f"↢ نوع البطاقة ↢ ( {account_data['card_type']} )\n"
        f"↢ فلوسك ↢ ( {account_data['money']} دولار 💵 )\n"
        f"↢ شخصيتك : {account_data['character']}\n"
        f"↢ دولتك : {account_data['country']}"
    )
@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() == "تطوير راتب")
def upgrade_salary(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    data = init_user(user_id, name)

    user_data = data.get(str(user_id), {})
    current_level = user_data.get("salary_level", 1)
    current_money = user_data.get("money", 0)
    last_upgrade = user_data.get("last_upgrade_time", 0)

    now = time.time()
    cooldown = 2 * 24 * 60 * 60 

    if now - last_upgrade < cooldown:
        remaining = int((cooldown - (now - last_upgrade)) / 3600)  
        bot.reply_to(message, f"⏳ يا {name}، لازم تستنى {remaining} ساعة قبل ما تقدر ترقي الراتب مرة تانية.")
        return
    upgrade_cost = current_level * 200
    if current_money < upgrade_cost:
        bot.reply_to(message, f"""↤ عذرًا {name}، لا تملك ما يكفي من المال 💸
↤ تكلفة الترقية: {upgrade_cost} دولار
↤ رصيدك الحالي: {current_money} دولار""")
        return

    user_data["money"] = current_money - upgrade_cost
    user_data["salary_level"] = current_level + 1
    user_data["last_upgrade_time"] = now

    data[str(user_id)] = user_data
    save_data(data)

    bot.reply_to(message, f"""🎖 تمت ترقية راتبك بنجاح!

↤ اسمك: {name}
↤ المستوى الجديد للراتب: {user_data["salary_level"]}
↤ تم خصم: {upgrade_cost} دولار
↤ رصيدك الحالي: {user_data["money"]} دولار 💵
""")
@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() == "توب فلوس")
def top_rich(message):
    from babel.numbers import format_currency
    import locale

    data = load_data()
    user_id = str(message.from_user.id)
    ranking = sorted(data.items(), key=lambda x: x[1].get("money", 0), reverse=True)[:20]

    medals = ["🥇", "🥈", "🥉"]
    text = "↤ توب اغنى 20 شخص :\n\n"

    for i, (uid, user_data) in enumerate(ranking, 1):
        try:
            chat = bot.get_chat(int(uid))
            name = chat.first_name or "لا يوجد اسم"
            country_code = chat.language_code.upper() if chat.language_code else "PS"
        except:
            name = user_data.get("name", "لا يوجد اسم")
            country_code = "PS"

        money = user_data.get("money", 0)
        money_str = f"{money:,}"
        medal = medals[i-1] if i <= 3 else f"{i})"

        text += f"{medal} {money_str} 💵 l [{name}] 💙\n"  
    full_ranking = sorted(data.items(), key=lambda x: x[1].get("money", 0), reverse=True)
    your_rank = next((i+1 for i, (uid, _) in enumerate(full_ranking) if uid == user_id), None)
    your_money = data.get(user_id, {}).get("money", 0)
    your_name = message.from_user.first_name or "لا يوجد اسم"
    your_line = f"\n ━━━━━━━━━\nyou ) {your_money:,} 💵 l [{your_name}]\n"

    note = (
        "\n↤ ملاحظة : اي شخص مخالف للعبة بالغش او حاط يوزر ينحضر من اللعبه وتتصفر فلوسه\n"
        "\n↤ تتصفر اللعبة بعد : يوم واحد"
    )

    bot.reply_to(message, text + your_line + note)

cooldowns = {}         
police_cooldowns = {}  
pending_steals = {}    

@bot.message_handler(func=lambda m: m.reply_to_message and m.text.lower() == "زرف")
def steal_money(message):
    data = load_data()
    thief_id = str(message.from_user.id)
    target_id = str(message.reply_to_message.from_user.id)
    now = time.time()

    if thief_id == target_id:
        bot.reply_to(message, "↤ ميمفعش تزرف نفسك 😒")
        return

    if thief_id not in data or target_id not in data:
        bot.reply_to(message, "↤ لازم يكون ليكوا حسابات.")
        return

    last_police = police_cooldowns.get(thief_id, 0)
    if now - last_police < 600:
        remaining = int((600 - (now - last_police)) / 60)
        bot.reply_to(message, f"😒 انت في فترة تهدئة بسبب القبض عليك، استنى {remaining} دقيقة.")
        return

    last_steal = cooldowns.get((thief_id, target_id), 0)
    if now - last_steal < 600:
        remaining = int((600 - (now - last_steal)) / 60)
        bot.reply_to(message, f"⏳ لازم تستنى {remaining} دقيقة قبل ما تزرف نفس الشخص تاني.")
        return

    import random
    success = random.choice([True, False, False])  
    if success:
        amount = random.randint(20, 100)
        if data[target_id]["money"] >= amount:
            data[target_id]["money"] -= amount
            save_data(data)

            cooldowns[(thief_id, target_id)] = now
            message_to_delete = bot.reply_to(message,
                f"🤑 سرقت {amount} 💸 من {data[target_id]['name']}! انت عندك 30 ثانية اذا رد بكلمة شرطة يترجعوله الفلوس.")

            pending_steals[message_to_delete.message_id] = {
                "thief_id": thief_id,
                "target_id": target_id,
                "amount": amount,
                "message_to_delete_id": message_to_delete.message_id,
                "message_chat_id": message.chat.id
            }

            try:
                bot.delete_message(message.chat.id, message.message_id)
            except:
                pass

            def wait_police():
                time.sleep(30)
                if message_to_delete.message_id in pending_steals:
                    pending_steals.pop(message_to_delete.message_id, None)

                    bot.edit_message_text(
                        chat_id=message.chat.id,
                        message_id=message_to_delete.message_id,
                        text=f"🤑 سرقت {amount} 💸 من {data[target_id]['name']}! وخلصت العملية، ماحدش رد بالشرطة."
                    )

            threading.Thread(target=wait_police).start()

        else:
            bot.reply_to(message, "↤ الشخص ده مفيش في جيبه حاجة تزرفها 💀")
    else:
        penalty = random.randint(5, 9)
        data[thief_id]["money"] = max(0, data[thief_id]["money"] - penalty)
        save_data(data)
        bot.reply_to(message, f"🚓 اتقفشت! خسرت {penalty} 💵 كغرامة.")




@bot.message_handler(func=lambda m: m.text and m.text.strip() == "حسابه")
def show_account(message):
    data = load_data()

    if not message.reply_to_message:
        bot.reply_to(message, "↤ لازم ترد على رسالة الشخص عشان أجيب حسابه.")
        return

    target_user_id = str(message.reply_to_message.from_user.id)

    if target_user_id not in data:
        bot.reply_to(message, "↤ مفيش بيانات عن الشخص ده.")
        return

    user_data = data[target_user_id]

    account_number = user_data.get("account_number", "غير محدد")
    card_type = user_data.get("card_type", "غير محدد")
    money = user_data.get("money", 0)
    personality = user_data.get("personality", "غير محدد")
    country = user_data.get("country", "غير محدد")

    reply_text = f"""↢ رقم حسابه ↢ ( {account_number} )
↢ نوع البطاقة ↢ ( {card_type} )
↢ فلوسه ↢ ( {money} دولار 💵 )
↢ شخصيته : {personality}
↢ دولته : {country}"""

    bot.reply_to(message, reply_text)
@bot.message_handler(func=lambda m: m.text.lower().strip() == "شرطة" and m.reply_to_message)
def police_catch(m):
    print(f"police_catch triggered by user {m.from_user.id}")
    message_id = m.reply_to_message.message_id
    data = load_data()
    now = time.time()

    if message_id in pending_steals:
        steal = pending_steals.pop(message_id)
        thief_id = steal["thief_id"]
        target_id = steal["target_id"]
        amount = steal["amount"]

        if str(m.from_user.id) != target_id:
            bot.reply_to(m, "🤦🏻 فقط الشخص المزروف يقدر يرد بكلمة شرطة.")
            return

        if target_id in data:
            data[target_id]["money"] += amount
            save_data(data)

            police_cooldowns[thief_id] = now

            try:
                bot.delete_message(m.chat.id, message_id)
                bot.delete_message(m.chat.id, m.message_id)
            except Exception as e:
                print(f"Error deleting messages: {e}")

            bot.send_message(m.chat.id, f"😹 {data[target_id]['name']} استعاد فلوسه بفضل الشرطة! الزارف دخل فترة تهدئة 10 دقائق.")
        else:
            bot.reply_to(m, "😔 حصل خطأ في استرجاع الفلوس، حاول تاني.")
    else:
        print(f"Message ID {message_id} not in pending_steals")





pending_transfers = {}  

from threading import Timer

pending_transfers = {} 

def cancel_transfer(uid, user_id):
    if uid in pending_transfers:
        pending_transfers.pop(uid)
        try:
            bot.send_message(user_id, "😐 تم إلغاء طلب التحويل بسبب عدم الرد في الوقت المحدد.")
        except:
            pass

@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith("تحويل "))
def start_transfer(message):
    user_id = message.from_user.id
    data = load_data()

    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "🥺 حبيبي، اكتب كده:\nتحويل [المبلغ]")
        return

    try:
        amount = int(parts[1])
        if amount <= 0:
            raise ValueError
    except ValueError:
        bot.reply_to(message, "😅 المبلغ لازم يكون رقم موجب صحيح.")
        return

    uid = str(user_id)
    if uid not in data or data[uid]["money"] < amount:
        bot.reply_to(message, "🫢 معاكش رصيد كافي يا حلو.")
        return

    if uid in pending_transfers:
        bot.reply_to(message, "↤ عندك تحويل شغال، خلصه أو انتظر الإلغاء.")
        return

    msg = bot.reply_to(message, "↤ ارسل الحين رقم الحساب البنكي الي تبي تحول له\n\n– معاك دقيقة وحدة والغي طلب التحويل .\n𔔁")

    timer = Timer(60, cancel_transfer, args=(uid, user_id))
    timer.start()

    pending_transfers[uid] = {
        "amount": amount,
        "start_time": time.time(),
        "timer": timer,
        "message_id": msg.message_id,
        "chat_id": msg.chat.id,
    }

@bot.message_handler(func=lambda m: str(m.from_user.id) in pending_transfers)
def receive_account_number(m):
    uid = str(m.from_user.id)
    if uid not in pending_transfers:
        return

    account_num = m.text.strip()
    transfer_info = pending_transfers.pop(uid)
    transfer_info["timer"].cancel()

    data = load_data()
    target_account = None
    target_uid = None
    for key, acc in data.items():
        if acc.get("account_number") == account_num:
            target_account = acc
            target_uid = key
            break

    if not target_account:
        bot.reply_to(m, "🙂 رقم الحساب البنكي دا مش موجود.")
        return

    sender = data[uid]
    amount = transfer_info["amount"]
    fee = int(amount * 0.10)
    total_deduction = amount + fee

    if sender["money"] < total_deduction:
        bot.reply_to(m, "🤨 معاكش رصيد كافي بعد خصم رسوم التحويل 10%.")
        return

    sender["money"] -= total_deduction
    target_account["money"] += amount
    save_data(data)

    reply_text = f"""↢ حوالة صادرة من بنك ({sender.get("country", "غير محدد")})

↤ المرسل : {sender.get("name", "غير معروف")}
↤ الحساب رقم : {sender.get("account_number", "غير محدد")}
↤ نوع البطاقة : {sender.get("card_type", "غير محدد")}

↤ المستلم : {target_account.get("name", "غير معروف")}
↤ الحساب رقم : {target_account.get("account_number", "غير محدد")}
↤ نوع البطاقة : {target_account.get("card_type", "غير محدد")}

↤ خصمت 10% رسوم تحويل: {fee} دولار
↤ المبلغ : {amount} دولار 💵
"""

    bot.reply_to(m, reply_text)

    try:
        bot.delete_message(transfer_info["chat_id"], transfer_info["message_id"])
    except:
        pass
@bot.message_handler(func=lambda m: m.text.lower().startswith("استثمار "))
def استثمار_وهمي(message):
    try:
        user_id = str(message.from_user.id)
        data = load_data()

        if user_id not in data:
            return bot.reply_to(message, "↤ لازم تسوي حساب أول 🏦\n↤ أرسل: انشاء حساب")

        parts = message.text.split()
        if len(parts) < 2 or not parts[1].isdigit():
            return bot.reply_to(message, "↤ استعمل الأمر بالشكل ده:\n\nاستثمار 1000")

        المبلغ = int(parts[1])
        if المبلغ <= 0:
            return bot.reply_to(message, "↤ المبلغ غير صالح ❌ لازم يكون أكبر من 0")

        بيانات = data[user_id]
        الوقت_الآن = time.time()
        آخر_مرة = بيانات.get("وقت_الاستثمار", 0)

        if الوقت_الآن - آخر_مرة < cooldown_time:
            المتبقي = int(cooldown_time - (الوقت_الآن - آخر_مرة))
            دقائق = المتبقي // 60
            ثواني = المتبقي % 60
            return bot.reply_to(message, f"↤ لازم تستنى {دقائق} دقيقة ✨🎖")

        نسبة_الربح = random.randint(5, 10)
        مبلغ_الربح = int(المبلغ * (نسبة_الربح / 100))

        بيانات["money"] = بيانات.get("money", 0) + مبلغ_الربح
        بيانات["وقت_الاستثمار"] = الوقت_الآن

        save_data(data)

        الرد = (
            "↤ استثمار ناجح 💰\n"
            f"↤ نسبة الربح ↢ {نسبة_الربح}%\n"
            f"↤ مبلغ الربح ↢ ( {مبلغ_الربح} دولار 💵 )\n"
            f"↤ فلوسك صارت ↢ ( {بيانات['money']} دولار 💵 )"
        )

        bot.reply_to(message, الرد)

    except Exception as e:
        bot.reply_to(message, f"↤ حصل خطأ داخلي: {e}\n↤ استعمل الأمر بالشكل ده:\n\nاستثمار 1000")
@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith("حظ"))
def gamble(message):
    user_id = str(message.from_user.id)
    data = init_user(user_id, message.from_user.first_name)

    now = time.time()
    last_gamble = data[user_id].get("last_gamble", 0)

    if now - last_gamble < cooldown_time:
        remaining = int(cooldown_time - (now - last_gamble))
        minutes = remaining // 60
        seconds = remaining % 60
        bot.reply_to(message, f"👏🏻 استنى {minutes} دقيقة ")
        return

    try:
        parts = message.text.split(" ")
        if len(parts) < 2 or not parts[1].isdigit():
            bot.reply_to(message, "↤ استخدم الأمر كدا: حظ [المبلغ]")
            return

        amount = int(parts[1])
        if amount <= 0:
            bot.reply_to(message, "↤ المبلغ لازم يكون أكبر من صفر.")
            return

        if data[user_id]["money"] < amount:
            bot.reply_to(message, "↤ معندكش فلوس كفاية 💸")
            return

        data[user_id]["money"] -= amount
        if random.random() < 0.5:
            win = amount * 2
            data[user_id]["money"] += win
            bot.reply_to(message, f"🎉 كسبت {win} 💵! شكلك محظوظ 🍀")
        else:
            bot.reply_to(message, f"😢 خسرت {amount} 💸، حاول تاني")

        data[user_id]["last_gamble"] = now  
        save_data(data)

    except Exception as e:
        bot.reply_to(message, f"❌ حصل خطأ: {e}")
@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith("اضف فلوس"))
def add_money_love_mode(message):
    admin_id = "7065772273"  
    if str(message.from_user.id) != admin_id:
        return bot.reply_to(message, "🤨 الأمر دا بس للأدمن يا قمر.")

    parts = message.text.split()
    if len(parts) < 3:
        return bot.reply_to(message, "🥺 حبيبي، اكتبلي كده:\nاضف فلوس [المبلغ] [رقم الحساب]")

    try:
        amount = int(parts[2])
        if amount <= 0:
            raise ValueError
    except ValueError:
        return bot.reply_to(message, "🙂 المبلغ لازم يكون رقم موجب يا حلو.")

    target_account = parts[3] if len(parts) >= 4 else None
    data = load_data()

    if target_account:
        for uid, acc in data.items():
            if acc.get("account_number") == target_account:
                acc["money"] = acc.get("money", 0) + amount
                save_data(data)
                return bot.reply_to(message,
                    f"💖 تم تحويل {amount}$ لحساب:\n"
                    f"👈🏻🖤 {acc.get('account_number', 'غير معروف')}\n"
                    f"🪪 {acc.get('name', 'مجهول')}\n"
                    f"💰 الرصيد الحالي: {acc.get('money', 0)}$\n\n"
                    f"من عيوني يا قلبي ❤️.")
        return bot.reply_to(message, "😑 رقم الحساب دا مش لاقيه يا روحي.")
    
    uid = str(message.from_user.id)
    if uid not in data:
        return bot.reply_to(message, "😢 حبيبي، انت لسه ما عملتش حساب.")

    data[uid]["money"] = data[uid].get("money", 0) + amount
    save_data(data)

    return bot.reply_to(message,
        f"عيني يا {message.from_user.first_name}، هضيفلك {amount}$ فورًا 💸💞\n"
        f"رصيدك الجديد: {data[uid]['money']}$ ✨\n"
        f"أنت أغلى من كل الفلوس يا روحي ❤️.")

@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() == "حذف الحساب")
def delete_account(message):
    user_id = str(message.from_user.id)
    data = load_data()

    if user_id in data:
        del data[user_id]
        save_data(data)
        bot.reply_to(message, " تم حذف  عايز تبدأ من جديد، اكتب: إنشاء حساب")
    else:
        bot.reply_to(message, "↤ معندكش حساب عشان تحذفه😫")

@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() in ["شرح", "بنك ", " الألعاب"])
def show_game_commands(message):
    bot.reply_to(message, """🎮 *أوامر الألعاب المتاحة:*


شرح الميزات الجديدة في بوت لولو ✨

✦━──『 نظام الألعاب والاقتصاد المتكامل 💰』──━✦

1➜ **إنشاء حساب بنكي 🏦:**
    - يتيح للمستخدمين إنشاء حساباتهم البنكية الخاصة داخل البوت.
    - يمكن اختيار الدولة ونوع البطاقة عند الإنشاء.

2➜  **الراتب وترقية الراتب 👏🏻:**
    - يحصل المستخدمون على راتب دوري (كل ساعة) لزيادة أموالهم.
    - يمكن ترقية مستوى الراتب لزيادة المبلغ الذي يتم الحصول عليه.

3➜ **البحث عن الكنوز 💎:**
    - ميزة عشوائية تسمح للمستخدمين بالعثور على كنوز بقيم مالية مختلفة.

4➜  **نظام السرقة والشرطة 🚓:**
    - يمكن للمستخدمين محاولة سرقة الأموال من بعضهم البعض.
    - يوجد نظام "شرطة" لاستعادة الأموال المسروقة ومعاقبة السارق.

5➜  **التحويلات البنكية 💸:**
    - إمكانية تحويل الأموال بين الحسابات البنكية داخل البوت بسهولة.

6➜  **الاستثمار  ✨:**
    - ميزة للاستثمار بمبالغ  مع نسبة ربح أو خسارة عشوائية.

7➜  **لعبة الحظ 🍀:**
    - لعبة قمار بسيطة يمكن للمستخدمين المراهنة فيها على مبلغ معين.

8➜  **إضافة وحذف الأموال (للأدمن) 💙:**
    - وظائف خاصة للمشرف لإضافة أو حذف الأموال من حسابات المستخدمين.

9➜  **حذف الحساب 🗑️:**
    - إمكانية حذف الحساب البنكي الخاص بالمستخدم.

10➜ **توب الفلوس 🏆:**
    - عرض قائمة بأغنى المستخدمين في البوت.



✦━──『 أوامر الإدارة ⚙️』──━✦

- تم إضافة العديد من أوامر الإدارة للتحكم في المجموعات والمستخدمين، مثل:
  `طرد`، `حظر`، `كتم`، `تثبيت`، `حذف`، `ترقية`، `تقييد`، `تحذير`، `معلومات`، `ايدي`.

""", parse_mode="Markdown")



        
@bot.callback_query_handler(func=lambda call: call.data == "choose_dialect")
def choose_dialect(call):
    """Display dialect selection buttons."""
    keyboard = types.InlineKeyboardMarkup([
        [types.InlineKeyboardButton("🇪🇬 مصري", callback_data="dialect_masri"), 
         types.InlineKeyboardButton("🇩🇿 جزائري", callback_data="dialect_dz")],
        [types.InlineKeyboardButton("🇮🇶 عراقي", callback_data="dialect_iraq"), 
         types.InlineKeyboardButton("🇸🇾 سوري", callback_data="dialect_syria")]
    ])

    try:
        
        bot.edit_message_text(
            "💙 اختر اللهجة التي تود التحدث بها➜:", 
            chat_id=call.message.chat.id, 
            message_id=call.message.message_id, 
            reply_markup=keyboard
        )
    except Exception as e:
        
        bot.send_message(
            call.message.chat.id, 
            "🌚✨ اختر اللهجة التي تود التحدث بها:➜", 
            reply_markup=keyboard
        )

    
    bot.answer_callback_query(call.id, "جارٍ عرض اللهجات المتاحة...")

@bot.callback_query_handler(func=lambda call: call.data.startswith("dialect_"))
def save_dialect(call):
    """Save the selected dialect and show voice/text mode options."""
    user_id = call.from_user.id
    dialect = call.data.split("_")[1]

    
    dialect_mapping = {
        "masri": "مصري", 
        "dz": "جزائري", 
        "iraq": "عراقي", 
        "syria": "سوري"
    }

    
    user_dialect[user_id] = dialect_mapping.get(dialect, "سوري")

    
    keyboard = types.InlineKeyboardMarkup([
        [types.InlineKeyboardButton("👄✨ التحدث بالصوت", callback_data="reply_voice")],
        [types.InlineKeyboardButton("💬 التحدث بالنص", callback_data="reply_text")]
    ])

    bot.edit_message_text(
        f"✅ تم اختيار اللهجة: {user_dialect[user_id]}! اضغط للمتابعة:", 
        chat_id=call.message.chat.id, 
        message_id=call.message.message_id, 
        reply_markup=keyboard
    )
@bot.callback_query_handler(func=lambda call: call.data == "broadcast_message")
def handle_broadcast_start(call):
    user_id = call.from_user.id
    if not is_admin(user_id):
        bot.send_message(call.message.chat.id, "⛔️ هذه الميزة للمشرفين فقط.")
        return

    bot.send_message(call.message.chat.id, "🎖 أرسل الآن الرسالة التي تريد إذاعتها لجميع المستخدمين.")
    bot.register_next_step_handler(call.message, process_broadcast)


def process_broadcast(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.send_message(message.chat.id, "⛔️ هذه الميزة للمشرفين فقط.")
        return

    text = message.text
    success = 0
    failed = 0

    for user_id in user_conversations.keys():
        try:
            bot.send_message(user_id, text)
            success += 1
        except:
            failed += 1

    bot.send_message(message.chat.id, f"✅ تم الإرسال إلى {success} مستخدم.\n❌ فشل في {failed} مستخدم.")
@bot.callback_query_handler(func=lambda call: call.data == "change_welcome_video")
def handle_change_video(call):
    if not is_admin(call.from_user.id):
        bot.send_message(call.message.chat.id, "❌ هذا الخيار للمشرف فقط.")
        return

    bot.send_message(call.message.chat.id, "🎬 أرسل الآن رابط الفيديو الترحيبي الجديد.")
    bot.register_next_step_handler(call.message, save_new_welcome_video)

def save_new_welcome_video(message):
    global welcome_video_url
    url = message.text.strip()
    if url.startswith("http"):
        welcome_video_url = url
        bot.send_message(message.chat.id, "✅ تم تحديث الفيديو الترحيبي بنجاح.")
    else:
        bot.send_message(message.chat.id, "❌ الرابط غير صالح. تأكد أنه يبدأ بـ http أو https.")
        
        from io import BytesIO

@bot.message_handler(func=lambda message: message.text and message.text.strip().lower() == "عرض الاحصائيات")
def handle_show_stats_message(message):
    if not is_admin(message.from_user.id):
        bot.reply_to(message, "❌ هذا الخيار للمشرف فقط.")
        return

    users = list(user_conversations.keys())
    total = len(users)

    preview = "\n".join([f"• [{uid}](tg://user?id={uid})" for uid in users[:50]])
    more = f"\n...والمزيد ({total - 50} مستخدم إضافي)" if total > 50 else ""

    msg = f"""
📊 *إحصائيات البوت*

👥 *عدد المستخدمين:* `{total}`

📋 *معرفات المستخدمين (أول 20):*
{preview}{more}
"""

    txt = "\n".join(str(uid) for uid in users)
    file_buffer = BytesIO()
    file_buffer.write(txt.encode('utf-8'))
    file_buffer.seek(0)

    bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    bot.send_document(message.chat.id, file_buffer, caption="📄 جميع معرفات المستخدمين")
        
@bot.callback_query_handler(func=lambda call: call.data in ["reply_voice", "reply_text"])
def set_reply_mode(call):
    """Set the user's preferred reply mode (voice or text)."""
    user_id = call.from_user.id

    bot.answer_callback_query(call.id, "جارٍ حفظ إعداداتك...")

    if call.data == "reply_voice":
        user_voice_mode[user_id] = True
        mode_msg = "👄 تم اختيار وضع الرد الصوتي. سأرسل لك ردود صوتية بدلاً من النصوص."
    else:
        user_voice_mode[user_id] = False
        mode_msg = "✍🏻تم اختيار وضع الرد النصي."

    bot.send_message(call.message.chat.id, mode_msg)

    welcome_msg = f"🎉 أهلاً بك! أنا لولو، مساعدك باللهجة {user_dialect.get(user_id, 'العربية')}. يمكنك سؤالي أي شيء وسأحاول مساعدتك!"

    if user_voice_mode[user_id] and global_voice_enabled:
        try:
            bot.send_chat_action(call.message.chat.id, 'record_audio')

            voice_cfg = admin_voice_settings if admin_voice_settings else default_voice
            audio_data = generate_new_voice_audio(
                welcome_msg,
                voice=voice_cfg.get("voice", "nova"),
                style=voice_cfg.get("style")
            )

            if audio_data:
                audio_file = io.BytesIO(audio_data)
                audio_file.name = "welcome_voice.mp3"

                bot.send_voice(call.message.chat.id, audio_file)
            else:
                bot.send_message(call.message.chat.id, welcome_msg)
        except Exception:
            bot.send_message(call.message.chat.id, welcome_msg)
    else:
        bot.send_message(call.message.chat.id, welcome_msg)
        


def fetch_voices_list():
    """Fetch available voices from API or fallback to static list."""
    try:
        url = "https://sii3.moayman.top/api/voices.php"
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            data = response.json()
            if "voices" in data:
                return data["voices"]
            elif "voices_available" in data:
                return [{"voice": v, "name": v.capitalize()} for v in data["voices_available"]]
        return []
    except Exception as e:
        logger.error(f"Error fetching voices list: {e}")
        return []

def fetch_voices_list():
    try:
        url = "https://sii3.moayman.top/api/voices.php"
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return response.json().get("voices", [])
        return []
    except Exception as e:
        logger.error(f"Error fetching voices list: {e}")
        return []



@bot.callback_query_handler(func=lambda call: call.data == "customize_voice")
def customize_voice(call):
    
    user_id = call.from_user.id
    bot.answer_callback_query(call.id, "جارٍ تحميل الأصوات المتاحة...")

    if not is_admin(user_id):
        bot.send_message(call.message.chat.id, "⛔️ هذه الميزة للمشرفين فقط.")
        return

    display_voices(call.message, page=1)


def display_voices(message, page=1):
    voices = fetch_voices_list()

    if not voices:
        bot.send_message(message.chat.id, "⛔️ لا توجد أصوات متاحة حاليًا.")
        return

    start_idx = (page - 1) * VOICES_PER_PAGE
    end_idx = start_idx + VOICES_PER_PAGE
    current_voices = voices[start_idx:end_idx]

    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(
            f"{voice['name']}", 
            callback_data=f"voice_{idx}"
        ) for idx, voice in enumerate(current_voices, start=start_idx)
    ]
    markup.add(*buttons)

    pagination_buttons = []
    if start_idx > 0:
        pagination_buttons.append(
            types.InlineKeyboardButton("⬅️ السابق", callback_data=f"page_{page-1}")
        )
    if end_idx < len(voices):
        pagination_buttons.append(
            types.InlineKeyboardButton("التالي ➡️", callback_data=f"page_{page+1}")
        )
    if pagination_buttons:
        markup.row(*pagination_buttons)

    bot.send_message(
        message.chat.id, 
        "🔊 اختر صوتًا لـ لولو:", 
        reply_markup=markup
    )


VOICE_STYLES = [
    "cheerful tone",
    "deep calm voice",
    "high pitch, cute anime style",
    "angry warrior, dramatic tone",
    "soft whisper, ASMR style"
]


@bot.callback_query_handler(func=lambda call: call.data.startswith("voice_"))
def handle_voice_selection(call):
    user_id = call.from_user.id
    if not is_admin(user_id):
        bot.answer_callback_query(call.id, "⛔️ هذه الميزة للمشرفين فقط.")
        return

    try:
        voice_index = int(call.data.split("_")[1])
        voices = fetch_voices_list()

        if not voices or voice_index >= len(voices):
            bot.send_message(call.message.chat.id, "⚠️ تعذر العثور على الصوت المختار.")
            return

        selected_voice = voices[voice_index]

        admin_voice_settings["voice"] = selected_voice.get("voice")
        admin_voice_settings["name"] = selected_voice.get("name")

        bot.send_message(
            call.message.chat.id,
            f"✅ اخترت صوت: {selected_voice['name']}\n🎭 الآن اختر النمط (Style):"
        )

        markup = types.InlineKeyboardMarkup(row_width=1)
        for idx, style in enumerate(VOICE_STYLES):
            markup.add(types.InlineKeyboardButton(style, callback_data=f"style_{idx}"))

        bot.send_message(
            call.message.chat.id,
            "🔊 اختر النمط المناسب لهذا الصوت:",
            reply_markup=markup
        )

    except Exception as e:
        logger.error(f"Error in voice selection: {e}")
        bot.send_message(call.message.chat.id, "❌ حدث خطأ في اختيار الصوت.")


@bot.callback_query_handler(func=lambda call: call.data.startswith("style_"))
def handle_style_selection(call):
    user_id = call.from_user.id
    if not is_admin(user_id):
        bot.answer_callback_query(call.id, "⛔️ هذه الميزة للمشرفين فقط.")
        return

    try:
        style_index = int(call.data.split("_")[1])
        if style_index >= len(VOICE_STYLES):
            bot.send_message(call.message.chat.id, "⚠️ النمط غير موجود.")
            return

        selected_style = VOICE_STYLES[style_index]

        admin_voice_settings["style"] = selected_style

        bot.send_message(
            call.message.chat.id,
            f"✅ تم اختيار النمط: {selected_style}\n🔍 جارٍ اختبار الصوت الجديد..."
        )

        test_text = "مرحباً! هذا اختبار للصوت والنمط الجديد. أنا لولو، مساعدك الذكي."
        audio_data = generate_new_voice_audio(
            test_text,
            voice=admin_voice_settings.get("voice", "nova"),
            style=admin_voice_settings.get("style")
        )

        if audio_data:
            audio_file = io.BytesIO(audio_data)
            audio_file.name = "voice_test.mp3"
            bot.send_voice(call.message.chat.id, audio_file)
            bot.send_message(call.message.chat.id, "✅ تم تفعيل الصوت بالنمط الجديد بنجاح!")
        else:
            bot.send_message(call.message.chat.id, "⚠️ فشل اختبار الصوت. سيتم استخدام الرد النصي.")

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton("✅ تفعيل الصوت للجميع", callback_data="voice_mode_on"),
            types.InlineKeyboardButton("❌ تعطيل الصوت للجميع", callback_data="voice_mode_off")
        )
        bot.send_message(
            call.message.chat.id,
            "🔊 يمكنك التحكم بتفعيل/تعطيل الصوت لجميع المستخدمين:",
            reply_markup=keyboard
        )

    except Exception as e:
        logger.error(f"Error in style selection: {e}")
        bot.send_message(call.message.chat.id, "❌ حدث خطأ في اختيار النمط.")



@bot.message_handler(func=lambda message: message.text and message.text.lower().startswith('مسح'))
def handle_delete(message):
    try:
        command_parts = message.text.split()
        if len(command_parts) == 2 and command_parts[1].isdigit():
            count = int(command_parts[1])
            if count <= 0 or count > 200:
                bot.reply_to(message, "⚠️ يرجى إدخال عدد بين 1 و200.")
                return

            deleted = 0
            current_msg_id = message.message_id

            for i in range(count + 1):  
                try:
                    bot.delete_message(message.chat.id, current_msg_id - i)
                    deleted += 1
                    time.sleep(0.05)
                except:
                    continue

            bot.send_message(message.chat.id, f"♡•~• تم حذف {deleted} رسالة بنجاح.")
        else:
            bot.reply_to(message, "⚠️ استخدم الأمر بهذا الشكل: مسح 10")
    except Exception as e:
        bot.reply_to(message, f"❌ حدث خطأ أثناء تنفيذ الأمر: {e}")
from telebot import TeleBot, types
import logging


def is_group_admin(chat_id, user_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["creator", "administrator"]
    except Exception as e:
        logger.error(f"Error checking admin status: {e}")
        return False

def extract_user_from_reply(message):
    if not message.reply_to_message:
        return None, None
    replied_user = message.reply_to_message.from_user
    return replied_user.id, replied_user.first_name

def execute_admin_command(message, command_type):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if message.chat.type not in ["group", "supergroup"]:
        bot.reply_to(message, "⚠️ هذا الأمر يعمل فقط في المجموعات.")
        return

    if not is_group_admin(chat_id, user_id):
        bot.reply_to(message, "⛔️ هذا الأمر للمشرفين فقط.")
        return

    target_id, target_name = extract_user_from_reply(message)
    if not target_id:
        bot.reply_to(message, "⚠️ يرجى الرد على رسالة المستخدم لتنفيذ هذا الأمر.")
        return

    if target_id == bot.get_me().id:
        bot.reply_to(message, "❌ لا يمكنني تنفيذ أوامر على نفسي.")
        return

    try:
        target_member = bot.get_chat_member(chat_id, target_id)
    except Exception as e:
        bot.reply_to(message, f"❗️ خطأ في جلب معلومات المستخدم: {e}")
        return

    
    if target_member.status == "creator":
        bot.reply_to(message, "👄 لا يمكن تنفيذ هذا الأمر على مالك المجموعة.")
        return

    
    if command_type in ["mute", "ban"] and target_member.status == "administrator":
        bot.reply_to(message, "«~ لا يمكن تنفيذ هذا الأمر على مشرف آخر.")
        return

    try:
        if command_type == "mute":
            bot.restrict_chat_member(
                chat_id, target_id,
                types.ChatPermissions(can_send_messages=False)
            )
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("♪ إلغاء الكتم", callback_data=f"unmute:{target_id}"))
            bot.reply_to(message, f"↢ المستخدم ↢ «{target_name}» تم كتمه.", reply_markup=markup)

        elif command_type == "unmute":
            bot.restrict_chat_member(
                chat_id, target_id,
                types.ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_polls=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_change_info=False,
                    can_invite_users=True,
                    can_pin_messages=False
                )
            )
            bot.reply_to(message, f"♡«تم إلغاء كتم المستخدم «{target_name}» بنجاح.")

        elif command_type == "ban":
            bot.ban_chat_member(chat_id, target_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("#«~ إلغاء الحظر", callback_data=f"unban:{target_id}"))
            bot.reply_to(message, f"<~ تم حظر المستخدم «{target_name}».", reply_markup=markup)

        elif command_type == "unban":
            bot.unban_chat_member(chat_id, target_id)
            bot.reply_to(message, f"♡«~ تم إلغاء حظر المستخدم «{target_name}».")

        elif command_type == "pin":
            if message.reply_to_message:
                bot.pin_chat_message(chat_id, message.reply_to_message.message_id)
                bot.reply_to(message, "♬ تم تثبيت الرسالة.")

        elif command_type == "unpin":
            if message.reply_to_message:
                bot.unpin_chat_message(chat_id, message.reply_to_message.message_id)
                bot.reply_to(message, "«~~تم إلغاء تثبيت الرسالة.")

        elif command_type == "delete":
            if message.reply_to_message:
                bot.delete_message(chat_id, message.reply_to_message.message_id)
                bot.delete_message(chat_id, message.message_id)

        elif command_type == "promote":
            bot.promote_chat_member(
                chat_id, target_id,
                can_change_info=True,
                can_delete_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=False
            )
            bot.reply_to(message, f"♕«~~ تم ترقية المستخدم «{target_name}» إلى مشرف.")

        elif command_type == "demote":
            bot.promote_chat_member(
                chat_id, target_id,
                can_change_info=False,
                can_delete_messages=False,
                can_invite_users=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False
            )
            bot.reply_to(message, f"⬇«~~تم تنزيل المستخدم «{target_name}» من الإشراف.")

        elif command_type == "info":
            member = bot.get_chat_member(chat_id, target_id)
            status_map = {
                "creator": "♕«~~ مالك المجموعة",
                "administrator": "🛡️ مشرف",
                "member": "👤 عضو",
                "restricted": "🔒 مقيد",
                "left": "🚶‍♂️ غادر المجموعة",
                "kicked": "🚫 محظور"
            }
            status = status_map.get(member.status, member.status)
            info_text = (
                f"📊 معلومات المستخدم:\n"
                f"الاسم: {member.user.first_name}\n"
                f"المعرف: @{member.user.username or 'غير متوفر'}\n"
                f"الحالة: {status}\n"
                f"معرف المستخدم: {member.user.id}"
            )
            bot.reply_to(message, info_text)

    except Exception as e:
        logger.error(f"Error executing admin command: {e}")
        bot.reply_to(message, f"❗️ حدث خطأ أثناء تنفيذ الأمر:\n{str(e)}")

@bot.message_handler(func=lambda m: m.text and "ايدي" in m.text)
def user_info(message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user

    chat_id = message.chat.id

    try:
        member = bot.get_chat_member(chat_id, user.id)
    except Exception:
        bot.reply_to(message, "❌ لا يمكن الحصول على معلومات هذا المستخدم.")
        return

    status_map = {
    'creator': 'Primary owner «~~~',
    'administrator': 'ادمن 🥀 🍂',
    'member': 'عضو',
    'restricted': 'مقيد',
    'left': 'غادر المجموعة',
    'kicked': 'محظور😂✨'
    }
    status = status_map.get(member.status, member.status)

    
    try:
        user_profile = bot.get_chat(user.id)
        user_bio = user_profile.bio if user_profile.bio else "(لا يدعم Telegram حالياً)"
    except Exception:
        user_bio = "(لا يدعم Telegram حالياً)"

    photos = bot.get_user_profile_photos(user.id, limit=1)

    info_text = (
        f"↢ ꪀᥲ️ꪔᥱ : {user.first_name}\n"
        f"↢ 𝚞𝚜𝚎 : @{user.username or 'غير متوفر'}\n"
        f"↢ 𝚜𝚝𝚊 : {status}\n"
        f"↢ ɪᴅ : {user.id}\n"
        f"↢ ᴍѕɢ : (تفاعل ميت 💀 🍂)\n"
        f"↢ 𝚋𝚒𝚘 : {user_bio}"
    )

    markup = types.InlineKeyboardMarkup()
    button_text = user.first_name
    url = f"tg://user?id={user.id}"
    markup.add(types.InlineKeyboardButton(button_text, url=url))

    if photos.total_count > 0:
        photo_file_id = photos.photos[0][-1].file_id
        bot.send_photo(chat_id=chat_id, photo=photo_file_id, caption=info_text, reply_markup=markup)
    else:
        bot.reply_to(message, info_text, reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("unmute:"))
def callback_unmute(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id

    if not is_group_admin(chat_id, user_id):
        bot.answer_callback_query(call.id, "👄 هذا الزر للمشرفين فقط.", show_alert=True)
        return

    target_id = int(call.data.split(":")[1])

    try:
       
        bot.restrict_chat_member(
            chat_id,
            target_id,
            types.ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_polls=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=False,
            ),
        )

        
        bot.promote_chat_member(
            chat_id,
            target_id,
            can_change_info=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True,
        )

        
        bot.promote_chat_member(
            chat_id,
            target_id,
            can_change_info=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
        )

        bot.answer_callback_query(call.id, "🔊 تم إلغاء كتم المستخدم بنجاح (تم رفعه ثم تنزيله من المشرف).")
        bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)

    except Exception as e:
        bot.answer_callback_query(call.id, f"❌ حدث خطأ: {e}", show_alert=True)


from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        if member.is_bot:
            continue

        name = member.first_name
        group_title = update.message.chat.title

        welcome_msg = f"أهلًا {name} 💖 نورت جروب {group_title}!"
        await update.message.reply_text(welcome_msg)

def setup_welcome_handler(app):
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
        
@bot.message_handler(func=lambda m: m.text and m.text.strip() in ["اوامر", "امر", " الاوامر", "قائمة الاوامر"])
def show_commands_help(message):
    help_text = """
✨🍂 قائمة أوامر البوت 💀🎫

🍃 حذف [عدد] — حذف رسائل، مثال: حذف 10  
‼️ كتم — رد على رسالة المستخدم + كتابة كتم  
💢 إلغاء كتم — رد على رسالة + كتابة إلغاء كتم  
🩶 حظر — رد على رسالة + كتابة حظر  
🤍 إلغاء حظر — رد على رسالة + كتابة إلغاء حظر  
✋🏻 تثبيت — رد على رسالة + كتابة تثبيت  
🎫 إلغاء تثبيت — رد على رسالة + كتابة إلغاء تثبيت  
✨ ترقية — رد على رسالة + كتابة ترقية مشرف  
🍂 تنزيل — رد على رسالة + كتابة تنزيل  
💀 معلومات — رد على رسالة + كتابة معلومات  
🍃 ايدي — لمعرفة معلومات العضو أو نفسك

*الرد على رسالة المستخدم ضروري لتنفيذ أوامر الإدارة*


🎮 أوامر الألعاب المتاحة:

1. 💰 فلوسي — يعرض رصيدك الحالي.

2. 🧾 راتب — تحصل على راتب كل ساعة حسب
 مستواك.
3. 🎖 تطوير الراتب — طور مستواك لزيادة
 راتبك.
4. 🪙 كنز — تحصل على كنز عشوائي بقيمة
 مالية.
5. 💼 استثمار [المبلغ] — استثمر مبلغ
 واحتمال تكسب أو تخسر.
6. 🏦 إنشاء حساب — ينشئ لك حساب بنكي.

7. 👑 توب فلوس — يعرض أغنى 10 لاعبين.

8. 🕵️ زرف (بالرد على شخص) — تحاول تسرق فلوس من لاعب تاني.


"""
    bot.reply_to(message, help_text)

THUMB_PATH = "cover.jpg"


@bot.message_handler(func=lambda msg: msg.text and msg.text.lower().startswith("يوت "))
def search_youtube(message):
    query = message.text[4:].strip()
    if not query:
        bot.reply_to(message, "❗️ اكتب اسم الأغنية بعد كلمة 'يوت'.")
        return

    bot.send_chat_action(message.chat.id, 'typing')
    try:
        html = requests.get("https://www.youtube.com/results", params={"search_query": query}, timeout=20).text
        match = re.search(r"var ytInitialData = ({.*?});</script>", html)
        if not match:
            bot.reply_to(message, "❗️ لم أتمكن من جلب النتائج.")
            return

        data = json.loads(match.group(1))
        items = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
        results = []

        for item in items:
            if 'videoRenderer' in item:
                video = item['videoRenderer']
                video_id = video['videoId']
                title = video['title']['runs'][0]['text']
                results.append((title, video_id))
            if len(results) >= 3:
                break

        if not results:
            bot.reply_to(message, "😢 مفيش حاجة اتوجدت للبحث ده.")
            return

        markup = types.InlineKeyboardMarkup()
        for title, vid in results:
            markup.add(types.InlineKeyboardButton(title[:64], callback_data=f"ytmp3|{vid}"))
        bot.reply_to(message, "🎶 اختر الأغنية اللي تعجبك:", reply_markup=markup)

    except Exception as e:
        bot.reply_to(message, f"❌ حصل خطأ:\n{e}")
@bot.callback_query_handler(func=lambda call: call.data.startswith("ytmp3|"))
def handle_download(call):
    video_id = call.data.split("|")[1]
    api_url = f"https://youtube-mp36.p.rapidapi.com/dl?id={video_id}"
    headers = {
        "x-rapidapi-host": "youtube-mp36.p.rapidapi.com",
        "x-rapidapi-key": "8d5cf5b7d8msh21830cd4a0d5618p128e40jsn41258ae9b141"
    }

    loading = bot.send_message(call.message.chat.id, "⏳ جاري تحميل الصوت ...")

    try:
        response = requests.get(api_url, headers=headers, timeout=30)
        result = response.json()

        if result.get("status") == "ok":
            title = result["title"]
            audio_url = result["link"]

            audio_response = requests.get(audio_url, timeout=120, allow_redirects=True, stream=True)
            audio_data = io.BytesIO()
            for chunk in audio_response.iter_content(chunk_size=1024*64):
                if chunk:
                    audio_data.write(chunk)
            audio_data.seek(0)
            audio_data.name = f"{title}.mp3"  

            thumb_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
            thumb_data = requests.get(thumb_url).content
            thumb = io.BytesIO(thumb_data)
            thumb.name = "thumb.jpg"

            bot.send_audio(
                chat_id=call.message.chat.id,
                audio=audio_data,
                caption=f"💈 {title}\n#𝐋_𝐎_𝐋_𝐎",
                thumb=thumb,
                performer="YouTube",
                title=title
            )

        else:
            bot.send_message(call.message.chat.id, "❗️ الملف مش متاح حالياً.")
    except Exception as e:
        bot.send_message(call.message.chat.id, f"❌ خطأ:\n{e}")
    finally:
        bot.delete_message(call.message.chat.id, loading.message_id)

user_photos = {}
def escape_markdown(text: str) -> str:
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', text)

def generate_nano_banana_images(prompt, n=4):
    url = "https://sii3.top/api/nano-banana.php"
    try:
        response = requests.post(url, data={"text": prompt}, timeout=60)
        if response.status_code == 200:
            data = response.json()

            if "images" in data and isinstance(data["images"], list):
                return data["images"][:n], None
            elif "image" in data:
                return [data["image"]], None
            else:
                return None, "🥲 الرد من API ما فيه صور."
        else:
            return None, f"🥲 خطأ في API (الكود: {response.status_code})"
    except Exception as e:
        return None, f"🚨 خطأ أثناء الاتصال بـ API: {e}"


def edit_nano_banana_images(prompt, links):
    url = "https://sii3.top/api/nano-banana.php"
    try:
        response = requests.post(url, data={"text": prompt, "links": ",".join(links)}, timeout=60)
        if response.status_code == 200:
            data = response.json()

            if "images" in data and isinstance(data["images"], list):
                return data["images"], None
            elif "image" in data:
                return [data["image"]], None
            else:
                return None, "🥲 الرد من API ما فيه صور."
        else:
            return None, f"🥲 خطأ في API (الكود: {response.status_code})"
    except Exception as e:
        return None, f"🚨 خطأ أثناء الاتصال بـ API: {e}"


@bot.message_handler(content_types=['photo'])
def handle_user_photo(message):
    chat_id = message.chat.id
    try:
        file_id = message.photo[-2].file_id
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"

    
        if chat_id not in user_photos:
            user_photos[chat_id] = []
        user_photos[chat_id].append(file_url)

        bot.reply_to(
            message,
            ".\n⛈️ ابعت الان وصف التعديل الذي تحبه.\n(🧚🏻‍♂️مثال: دمج الصور – أو: اجعلها مرسومة مثل أنمي)"
        )
    except Exception as e:
        logger.error(f"Error handling photo: {e}")
        bot.reply_to(message, "🥲 حصل خطأ أثناء استلام الصورة.")


@bot.message_handler(func=lambda msg: msg.chat.id in user_photos and msg.text)
def handle_edit_description(message):
    chat_id = message.chat.id
    prompt = message.text.strip()

    if not prompt:
        bot.reply_to(message, "✍️ اكتب وصف التعديل أولاً.")
        return

    waiting = bot.send_sticker(
        chat_id,
        "CAACAgQAAxkBAAIdh2jNOsXb-QIugUtFP3YrFAYDvWVKAALsFgACtkLZUwawah7yWe94NgQ"
    )

    links = user_photos.get(chat_id, [])
    if not links:
        bot.reply_to(message, "🥲 مفيش صور مخزنة ليك. ابعت صورة الأول.")
        return

    images, error = edit_nano_banana_images(prompt, links)

    try:
        bot.delete_message(chat_id, waiting.message_id)
    except:
        pass

    if error:
        bot.send_message(chat_id, error)
    else:
        escaped_prompt = escape_markdown(prompt)
        media_group = []
        for i, img_url in enumerate(images[:4]):  
            caption = f"> {escaped_prompt}" if i == 0 else None
            media_group.append(types.InputMediaPhoto(media=img_url, caption=caption, parse_mode="MarkdownV2"))

        bot.send_media_group(chat_id, media=media_group)

    user_photos.pop(chat_id, None)


@bot.message_handler(func=lambda message: message.text and message.text.startswith('انشاء صوره'))
def handle_image_generation(message):
    chat_id = message.chat.id
    try:
        prompt = message.text.replace("انشاء صوره", "", 2).strip()
        if not prompt:
            bot.reply_to(
                message,
                "🎨 اكتب وصف الصورة بعد الأمر.\nمثال: انشاء صوره قطة جميلة في الحديقة"
            )
            return

        waiting = bot.send_sticker(
            chat_id,
            "CAACAgQAAxkBAAIdh2jNOsXb-QIugUtFP3YrFAYDvWVKAALsFgACtkLZUwawah7yWe94NgQ"
        )

        images, error = generate_nano_banana_images(prompt, n=4)

        try:
            bot.delete_message(chat_id, waiting.message_id)
        except:
            pass

        if error:
            bot.send_message(chat_id, error)
        else:
            escaped_prompt = escape_markdown(prompt)
            media_group = []
            for i, img_url in enumerate(images):
                caption = f"> {escaped_prompt}" if i == 0 else None
                media_group.append(types.InputMediaPhoto(media=img_url, caption=caption, parse_mode="MarkdownV2"))

            bot.send_media_group(chat_id, media=media_group)

    except Exception as e:
        logger.error(f"Exception in handle_image_generation: {e}")
        bot.reply_to(message, "🥲 حدث خطأ غير متوقع أثناء توليد الصور.")
@bot.message_handler(func=lambda m: m.text and m.text.startswith("كتم"))
def mute_command(message):
    result = execute_admin_command(message, "mute")
    if result:
        send_code_or_text(bot, message, result)

@bot.message_handler(func=lambda m: m.text and m.text.startswith("إلغاء كتم"))
def unmute_command(message):
    result = execute_admin_command(message, "unmute")
    if result:
        send_code_or_text(bot, message, result)

@bot.message_handler(func=lambda m: m.text and m.text.startswith("حظر"))
def ban_command(message):
    result = execute_admin_command(message, "ban")
    if result:
        send_code_or_text(bot, message, result)

@bot.message_handler(func=lambda m: m.text and m.text.startswith("إلغاء حظر"))
def unban_command(message):
    result = execute_admin_command(message, "unban")
    if result:
        send_code_or_text(bot, message, result)
@bot.message_handler(func=lambda m: m.text and m.text.startswith("تثبيت"))
def pin_command(message):
    result = execute_admin_command(message, "pin")
    if result:
        send_code_or_text(bot, message, result)

@bot.message_handler(func=lambda m: m.text and m.text.startswith("إلغاء تثبيت"))
def unpin_command(message):
    result = execute_admin_command(message, "unpin")
    if result:
        send_code_or_text(bot, message, result)

@bot.message_handler(func=lambda m: m.text and m.text.startswith("ترقية"))
def promote_command(message):
    result = execute_admin_command(message, "promote")
    if result:
        send_code_or_text(bot, message, result)

@bot.message_handler(func=lambda m: m.text and m.text.startswith("تنزيل"))
def demote_command(message):
    result = execute_admin_command(message, "demote")
    if result:
        send_code_or_text(bot, message, result)

@bot.message_handler(func=lambda m: m.text and m.text.startswith("معلومات"))
def info_command(message):
    result = execute_admin_command(message, "info")
    if result:
        send_code_or_text(bot, message, result)

def send_code_or_text(bot, message, text):
    code_blocks = re.findall(r"(?s)```(?:python)?(.*?)```", text)
    
    if code_blocks:
        explanation = re.sub(r"(?s)```(?:python)?(.*?)```", "", text).strip()
        
        if explanation:
            
            bot.reply_to(message, explanation)
            for code in code_blocks:
                cleaned_code = code.strip()
                if cleaned_code:
                    bot.send_message(
                        message.chat.id,
                        f"```python\n{cleaned_code}\n```",
                        parse_mode="Markdown",
                        reply_to_message_id=message.message_id
                    )
        else:
            
            for code in code_blocks:
                cleaned_code = code.strip()
                if cleaned_code:
                    bot.send_message(
                        message.chat.id,
                        f"```python\n{cleaned_code}\n```",
                        parse_mode="Markdown",
                        reply_to_message_id=message.message_id
                    )
    else:
        
        bot.reply_to(message, text)
@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = message.text

    ADMIN_KEYWORDS = ["اوامر", "ايدي", "معلومات", "كتم", "حظر", "ترقية", "تنزيل", "تثبيت", "إلغاء", "حذف"]
    if any(text.lower().startswith(word) for word in ADMIN_KEYWORDS):
        return  

    if user_id in ignored_users:
        if "يا لولو" in text.lower():
            ignored_users.remove(user_id)
            bot.reply_to(message, "رجعتلك يا حب 💕 قولي عايز ايه؟")
        return

    if any(cmd in text.lower() for cmd in STOP_COMMANDS):
        ignored_users.add(user_id)
        bot.reply_to(message, "تمام 😔 مش هرد تاني، لما تحب تكلمني قول 'يا لولو'.")
        return

    user_dialect.setdefault(user_id, "مصري")
    user_personality.setdefault(user_id, DEFAULT_PERSONALITY)

    bot.send_chat_action(chat_id, 'typing')

    response = ai_response(
        user_id=user_id,
        question=text,
        dialect=user_dialect[user_id],
        personality=user_personality[user_id],
        conversation_history=user_conversations
    )

    if "photo" in response:
        try:
            bot.send_photo(
                chat_id,
                photo=response["photo"],
                caption=response.get("text", ""),
                reply_to_message_id=message.message_id
            )
            return
        except Exception as e:
            logger.warning(f"فشل إرسال صورة: {e}")

    if user_voice_mode.get(user_id, False) and global_voice_enabled:
        try:
            voice_cfg = admin_voice_settings if admin_voice_settings else default_voice
            voice_data = generate_new_voice_audio(
                response["text"],
                voice=voice_cfg.get("voice", "nova"),
                style=voice_cfg.get("style")
            )
            if voice_data:
                voice_file = io.BytesIO(voice_data)
                voice_file.name = "voice_reply.mp3"
                bot.send_voice(
                    chat_id,
                    voice=voice_file,
                    reply_to_message_id=message.message_id
                )
                return
        except Exception as e:
            logger.warning(f"فشل إرسال الصوت: {e}")

    send_code_or_text(bot, message, response["text"]) 
def start_bot():
    logger.info("Starting bot polling...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            logger.error(f"Bot polling error: {e}")
            time.sleep(10)
print('🖤🖤🖤🖤')
if __name__ == "__main__":
    start_bot()