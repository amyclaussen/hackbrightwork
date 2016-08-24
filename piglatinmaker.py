prefix_ifvowel = "agab"
prefix_ifcons = "gada"
suffix_ifvowel = "doegay"
suffix_ifcons = "oogay"

def pig_latin(word):
	pig_latin_word = word
	if word[0].lower() in ["a","e","i","o","u"]:
		pig_latin_word = prefix_ifvowel + word.lower()
	else:
		pig_latin_word = prefix_ifcons + word.lower()
	if word[-1].lower() in ["a","e","i","o","u"]:
		pig_latin_word = pig_latin_word + suffix_ifvowel
	else:
		pig_latin_word = pig_latin_word + suffix_ifcons
	return pig_latin_word


