
sentence = "This is a common interview question"

sentence_unpack = [*sentence.lower()]
sentence_unpack.sort()
#print(sorted(sentence_unpack))

for x in range(5):
    sentence_unpack.remove(" ")


letter_freq = {}

for letter in sentence:
    if letter in letter_freq:
        letter_freq[letter] =+ 1
    else:
        letter_freq[letter] = 1

print(letter_freq)

letter_freq_sort = sorted(letter_freq.items(), key=lambda kv: kv[1], reverse=True)

print(letter_freq_sort[0])


#print(sentence_unpack)
#print(len(sentence_unpack))



letter_count = []
letters = []

#letter_count = [letter]
#dict = {letter: number of times in sentence} letter_count = {t
index = 0

sentence_unpack.sort()

#print(sentence_unpack)

unique_sentence = set(sentence_unpack)
unique_sentence = set(list(sentence_unpack))

unique_sentence = sorted(unique_sentence)

#print(unique_sentence)

letters = unique_sentence


print("number of single letters : ", unique_sentence)


print("these are the letters", letters)

#print("this is the amount of times letters showed", letter_count)

#print("test", letter_count)

amount_a = sentence_unpack.count("a")
letter_count.insert(0, amount_a)
amount_c = sentence_unpack.count("c")
letter_count.insert(1, amount_c)
amount_e = sentence_unpack.count("e")
letter_count.insert(2, amount_e)
amount_h = sentence_unpack.count("h")
letter_count.insert(3, amount_h)
amount_i = sentence_unpack.count("i")
letter_count.insert(4, amount_i)
amount_m = sentence_unpack.count("m")
letter_count.insert(5, amount_m)
amount_n = sentence_unpack.count("n")
letter_count.insert(6, amount_n)
amount_o = sentence_unpack.count("o")
letter_count.insert(7, amount_o)
amount_q = sentence_unpack.count("q")
letter_count.insert(8, amount_q)
amount_r = sentence_unpack.count("r")
letter_count.insert(9, amount_r)
amount_s = sentence_unpack.count("s")
letter_count.insert(10, amount_s)
amount_t = sentence_unpack.count("t")
letter_count.insert(11, amount_t)
amount_u = sentence_unpack.count("u")
letter_count.insert(12, amount_u)
amount_v = sentence_unpack.count("v")
letter_count.insert(13, amount_v)
amount_w = sentence_unpack.count("w")
letter_count.insert(14, amount_w)

#print("letter count", letter_count)

zipped = list(zip(letters, letter_count))

#print(zipped)

def most_com(zipped):
    return zipped[1]

zip_num = zipped.sort(key=most_com, reverse=True)
#print("test", zipped)

print("The most common letter in the above sentence is :", zipped[0])

# for index in range(1, 15):
#     if amount_t >
#
# for index in range(1 , 30):
#     print(index)




# while index != 30:
#     sentence_unpack.count("t") =
#
# for index in range(1, 30):


#if sentence_unpack.count("t")

#print("T has ", sentence_unpack.count("t"))
# print(sentence_unpack.count("h"))
# print(sentence_unpack.count("i"))
# print(sentence_unpack.count("s"))
# print(sentence_unpack.count("a"))
# print(sentence_unpack.count("c"))
# print(sentence_unpack.count("o"))
# print(sentence_unpack.count("m"))
# print(sentence_unpack.count("n"))
# print(sentence_unpack.count("e"))
# print(sentence_unpack.count("r"))
# print(sentence_unpack.count("v"))
# print(sentence_unpack.count("w"))
# print(sentence_unpack.count("q"))
# print(sentence_unpack.count("u"))
# print(sentence_unpack.count("t"))
