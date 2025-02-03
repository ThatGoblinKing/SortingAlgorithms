from winsound import Beep
from random import shuffle

class Tone:
    def __init__(self, pitch, length = 400):
        self.pitch = pitch
        self.length = length

    def __int__(self):
        return self.pitch

    def __add__(self, other : int):
        return self.pitch + other

    def __repr__(self):
        return str(self.pitch)

    def play(self):
        Beep(self.pitch, self.length)


def bubbleSort(array):
    unsorted = True
    while unsorted:
        for i in range(len(array)):
            if i + 1 < len(array) and int(array[i]) > int(array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                array[i].play()
        unsorted = False
        for j in range(len(array)):
            if j + 1 < len(array):
                if int(array[j]) > int(array[j+1]):
                    unsorted = True
    for tone in array:
        tone.play()
    return array

dataSet = [Tone(i, 100) for i in range(200, 1000, 200)]
shuffle(dataSet)

print(bubbleSort(dataSet))
