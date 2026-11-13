#Mixed Problems 25-50
#Name: Premnath Sonkusare

def count_vowels(word:str)->int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    try:
        input_word = str(input("Enter the Word:"))
        count_vowel = count_vowels(input_word)
        print(f"Count of vowels in {input_word} is: {count_vowels}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))