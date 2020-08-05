
# For 32 bit, it will return 32. But for 64, it will return 64.
import struct
print(struct.calcsize("P") * 8)
