from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetShortName
import os

# API Zugangsdaten von https://my.telegram.org/apps
api_id = 70839426        # API ID
api_hash = 'e48f92a10b7dd3c5af6129b8cc4f09ea'  # API Hash

sticker_pack_name = input("Wie heißt der Stickerpack-Name (z. B. Animated_Round_Pretty_Cat)?\n> ").strip()

os.makedirs(sticker_pack_name, exist_ok=True)

with TelegramClient('session_name', api_id, api_hash) as client:
    sticker_set = client(GetStickerSetRequest(
        stickerset=InputStickerSetShortName(sticker_pack_name),
        hash=0
    ))

    print(f"\n🔽 Lade {len(sticker_set.documents)} Sticker aus {sticker_pack_name} herunter ...")

    for i, doc in enumerate(sticker_set.documents):
        ext = '.tgs' if doc.mime_type == 'application/x-tgsticker' else '.webp'
        filename = f"{sticker_pack_name}/{i+1}{ext}"
        client.download_media(doc, filename)
        print(f" {filename}")
