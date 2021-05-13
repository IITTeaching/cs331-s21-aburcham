import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    word_list = book_to_words(book_url)
    max = 0
    for x in word_list:
        if max < len(x):
            max = len(x)

    for x in range(max):
        byte_lst = c_sort(word_list, max - 1, x,)
    return byte_lst

def c_sort(arr, max, cur):
    char_array = [0 for x in range(len(arr))]
    c = [0 for x in range(128)]
    for x in arr:
        if max - cur < len(x):
            c[x[max - cur]] += 1
        else:
            c[0] += 1

    for x in range(128):
        c[x] += c[x-1]

    for x in range(len(arr) -1, -1, -1):
        if max - cur < len(arr[x]):
            char_array[c[arr[x][max - cur]] - 1] = arr[x]
            c[arr[x][max - cur]] -= 1            
        else:
            char_array[c[0] - 1] = arr[x]
            c[0] -= 1            

    return char_array