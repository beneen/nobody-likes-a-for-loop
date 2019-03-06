
"""
-----
reverse words in a sentence. I'm cheating because I used .split lol.
-----
"""

def reverse_words(text):
    return " ".join(text.split(" ")[::-1])



def main():
    print(reverse_words(input("insert text1:")))


if __name__ == "__main__":
    main()
