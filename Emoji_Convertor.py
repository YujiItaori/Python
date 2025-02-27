# emoji convertor

def emoji_convert(message):
    words = message.split(" ")
    emojis = {
        "happy": "😀",
        "sad": "😔"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

value = input("> ")
result = emoji_convert(value)
print(result)
