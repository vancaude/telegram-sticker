# telegram-sticker-downloader

Ein einfaches Python-Skript zum Herunterladen kompletter Telegram-Stickerpacks (inkl. animierter `.tgs` oder statischer `.webp` Sticker).

## Voraussetzungen:

- Python 3.7+
- [Telethon](https://github.com/LonamiWebs/Telethon)

Telethon installieren mit:

```bash
pip install telethon
```

Auf my.telegram.org den API Key erstelllen.

API ID und  API Hash wird im script benötigt.


```bash
python downloader.py
```

Beispiel:

Wie heißt der Stickerpack-Name (z. B. Animated_Round_Pretty_Cat)?
> CuteBearsPack

Lade 15 Sticker aus CuteBearsPack herunter ...
 CuteBearsPack/1.webp
 CuteBearsPack/2.webp
 ...
