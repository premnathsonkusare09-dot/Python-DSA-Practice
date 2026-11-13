#Mixed Problems 25-50
#Name: Premnath Sonkusare

def get_reverse_sentence(sentence:str)->str:
    words = sentence.split()
    words.reverse()
    return " ".join(words)

if __name__ == "__main__":
    try:
        input_sentence = str(input("Enter the sentence:"))
        rev_sent = get_reverse_sentence(input_sentence)
        print(f"Reversed Sentence is: {rev_sent}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))