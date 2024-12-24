"""
Replace letters with similar sounding ones 

Ex: `ظ` with `ذ`  

"""

import re
import unicodedata

from mappings import similar_sounding_letters

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


