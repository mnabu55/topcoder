from typing import List, Tuple, Optional


class EllysCandies:
    def getWinner(self, box):
        lbox = list(box)
        lbox.sort(reverse=True)
        num_box = len(lbox)

        for i in range(num_box):
            for j in range(i, num_box):
                lbox[j] += lbox[i]

        elly_box = lbox[0::2]
        kris_box = lbox[1::2]
        if sum(elly_box) >= sum(kris_box):
            win = "Elly"
        else:
            win = "Kris"
        return win
