from confusables import remove
from unicodedata import normalize

subscript = "𝟺ᴋ ᴠɪᴅᴇᴏ - ʙʟᴏᴡᴊᴏʙ - ᴅᴇᴇᴘᴛʜʀᴏᴀᴛ - ᴄᴜᴍ ɪɴ ᴍᴏᴜᴛʜ - ᴅᴇsɪ ᴄʟᴏᴛʜᴇs "

cases = [
    "🅱️ moji letters",
    "àçcéñt õbfûśçátè",
    "𝘂𝗻𝗶𝗰𝗼𝗱𝗲 𝗯𝗼𝗹𝗱",
    "sᴍᴀʟʟ ᴄᴀᴘs",
    "z͉a͙̰̻̤l̤̆g̺̜̩͇͇̅͂ͧo̞",
    "ｆｕｌｌ ｗｉｄｔｈ",
    "ƤŘ€ŦŦ¥ Ŧ€ЖŦ",
    "😱😈😇😉 emoji",
    "ₛᵤbₛcᵣᵢₚₜ",
    "ˢᵘᵖᵉʳˢᶜʳᶦᵖᵗ",
    "ₛₘₐˡˡ ᵗₑˣᵗ",
    "don't remove \"quotes\"",
    "preserve@example.com"
]

def normalize_unicode(text):
    return normalize("NFKD", text)

for case in cases:
    print("i: " + case)
    print("o: " + remove(normalize_unicode(case)))
    print("")