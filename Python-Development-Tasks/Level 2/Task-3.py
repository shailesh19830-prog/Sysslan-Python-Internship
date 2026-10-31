def analyze_text(text):
    char_count = len(text)
    # split() breaks the string into a list of words based on spaces
    word_count = len(text.split())
    return char_count, word_count

sample_text = "Hello world! Welcome to Python programming."
chars, words = analyze_text(sample_text)
print(f"Text: '{sample_text}'")
print(f"Total Characters: {chars}")
print(f"Total Words: {words}")