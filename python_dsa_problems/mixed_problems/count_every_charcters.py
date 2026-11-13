#Mixed Problems 25-50
#Name: Premnath Sonkusare

def count_each_character(word: str) -> str:
    low = 0
    ans = ""

    while low < len(word):
        count = 1
        high = low + 1

        while high < len(word) and word[low] == word[high]:
            count += 1
            high += 1

        ans = ans + word[low] + str(count)
        low = high
    return ans

if __name__ == "__main__":
    input_word = input("Enter the word: ")
    count = count_each_character(input_word)
    print(f"Character frequency: {count}")