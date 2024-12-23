"""
Replace letters with similar sounding ones 

Ex: `ظ` with `ذ`  

"""

import re
import unicodedata

similar_sounding_letters = {
    "ع": {"representative": "ا", "remove_at_end": False},
    "پھ": {"representative": "ف", "remove_at_end": False},
    "ط": {"representative": "ت", "remove_at_end": False},
    "ث" : {"representative": "س", "remove_at_end": False},
    "ص": {"representative": "س", "remove_at_end": False},
    "ڑ": {"representative": "ڈ", "remove_at_end": False},   
    "ہ": {"representative": "ح", "remove_at_end": True},
    "خ": {"representative": "کھ", "remove_at_end": False},
    "غ": {"representative": "گ", "remove_at_end": False},
    "ض": {"representative": "ذ", "remove_at_end": False},
    "ظ": {"representative": "ذ", "remove_at_end": False},
    "ذ": {"representative": "ز", "remove_at_end": False}
}

def replace_similar_sounds(text):
    text = unicodedata.normalize('NFC', text)

    for sound, data in similar_sounding_letters.items():
        representative = data["representative"]
        remove_at_end = data["remove_at_end"]
        
        text = text.replace(sound, representative)

        if  remove_at_end:
            pattern = rf"(?<=\S){re.escape(representative)}(?=\s|\b|\W|$)"
            text = re.sub(pattern, "", text)

    return text


