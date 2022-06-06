# https://leetcode.com/problems/filling-bookcase-shelves/
# UNFINISHED

def minheightShelves(books, shelfWidth):
    tallest_shelf_book_h = below_h = 0
    w_left = shelfWidth

    for i in range(len(books) - 1, -1, -1):
        w, h = books[i]
        new_w_left = w_left - w
        if new_w_left > 0:
            tallest_shelf_book_h = max(tallest_shelf_book_h, h)
            w_left = new_w_left
        elif new_w_left == 0:
            w_left = shelfWidth
            below_h += max(tallest_shelf_book_h, h)
            tallest_shelf_book_h = 0
        elif new_w_left < 0:
            below_h += tallest_shelf_book_h
            tallest_shelf_book_h = h
            w_left = shelfWidth - w

    return below_h + tallest_shelf_book_h

print(minheightShelves([[1,3],[2,4],[3,2]], 6))

