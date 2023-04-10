# bitarray management

# adapted from pythoncoder's message in https://forum.micropython.org/viewtopic.php?f=2&t=5274

class bit():
    def __init__(self):
        self.bits = bytearray(1)

    def __getitem__(self, n):
        return (self.bits[0] >> n) & 1

    def __setitem__(self, n, v):
        if v:
            self.bits[0] |= v << n
        else:
            self.bits[0] &= ~(1 << n)

b = bit()
print(b)
