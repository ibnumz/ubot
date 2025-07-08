from pyrogram.types import CallbackQuery
from PyroUbot import PY
from PyroUbot.core.database import mongodb


# Koleksi MongoDB untuk prefix
prefixes = mongodb["PyroUbot"]["prefix"]

# Fungsi untuk hapus prefix
async def rem_pref(user_id: int):
    await prefixes.update_one(
        {"_id": user_id}, {"$unset": {"prefixesi": ""}}, upsert=True
    )

@PY.CALLBACK("reset_prefix_(\\d+)")
async def _(client, callback: CallbackQuery):
    user_id = int(callback.matches[0].group(1))

    try:
        await rem_pref(user_id)
        await callback.answer("✅ Prefix berhasil direset! harap ketik /restart di bot agar prefix berubah", show_alert=True)
    except Exception as e:
        await callback.answer(f"❌ Gagal: {e}", show_alert=True)
