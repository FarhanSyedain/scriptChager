from mappings.combo_letter_diacritic_character_mapping import combo_letter_diacritic_character_mapping

def replace_with_combo_characters(text: str):
    for separated, combo in combo_letter_diacritic_character_mapping.items():
        text = text.replace(separated, combo)

    return text
