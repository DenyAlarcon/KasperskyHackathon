import sys
from base64 import b64encode, b64decode

data = sys.stdin.readline()

def reverse_bytes(bytes):
    # print("------------------------")
    # print(bytes)
    bytes_len = len(bytes)
    for i in range(0, int(bytes_len / 2), 2):
        b_left = bytes[i:i+2]
        b_right = bytes[-2-i:bytes_len-i]
        # print("1: " + bytes[:i])
        # print("2: " + b_left)
        # print("3: " + bytes[i+2:-2-i])
        # print("4: " + b_right)
        # print("5: " + bytes[bytes_len-i:])
        bytes = bytes[:i] + b_right + bytes[i+2:-2-i] + b_left + bytes[bytes_len-i:]
        # print(bytes)
    # print("------------------------")
    return bytes


def get_zeros_second_line(data):
    decoded_hex_data = ""
    try:
        decoded_hex_data = b64decode(data).hex()
    except Exception as e:
        return "NOT BMP"

    # print(decoded_hex_data)

    bfType = decoded_hex_data[0:4]
    bfSize = decoded_hex_data[4:12]
    bfReserved1 = decoded_hex_data[12:16]
    bfReserved2 = decoded_hex_data[16:20]
    bfOffBits = decoded_hex_data[20:28]

    # print("bfType: " + bfType)
    # print("bfSize: " + bfSize + " - " + str(int(reverse_bytes(bfSize), 16)))
    # print("bfReserved1: " + bfReserved1 + " - " + str(int(reverse_bytes(bfReserved1), 16)))
    # print("bfReserved2: " + bfReserved2 + " - " + str(int(reverse_bytes(bfReserved2), 16)))
    # print("bfOffBits: " + bfOffBits + " - " + str(int(reverse_bytes(bfOffBits), 16)))

    if (bfType != "424d" and bfType != "4d42"):
        return "NOT BMP"

    if (len(decoded_hex_data)/2 != int(reverse_bytes(bfSize), 16)):
        return "NOT BMP"

    bciSize = decoded_hex_data[28:36]
    # print("bciSize: " + bciSize + " - " + str(int(reverse_bytes(bciSize), 16)))

    if (int(reverse_bytes(bciSize), 16) == 12):
        # print("CORE")
        bcWidth = decoded_hex_data[36:40]
        bcHeight = decoded_hex_data[40:44]
        bcPlanes = decoded_hex_data[44:48]
        bcBitCount = decoded_hex_data[48:52]
        # print("bcWidth: " + bcWidth + " - " + str(int(reverse_bytes(bcWidth), 16)))
        # print("bcHeight: " + bcHeight + " - " + str(int(reverse_bytes(bcHeight), 16)))
        # print("bcPlanes: " + bcPlanes + " - " + str(int(reverse_bytes(bcPlanes), 16)))
        # print("bcBitCount: " + bcBitCount + " - " + str(int(reverse_bytes(bcBitCount), 16)))

        start = int(int(reverse_bytes(bfOffBits), 16) * 2 + int(reverse_bytes(bcWidth), 16) * (int(reverse_bytes(bcBitCount), 16) / 8) * ((int(reverse_bytes(bcHeight), 16) - 2) * 2))
        stop = int(int(reverse_bytes(bfOffBits), 16) * 2 + int(reverse_bytes(bcWidth), 16) * (int(reverse_bytes(bcBitCount), 16) / 8) * ((int(reverse_bytes(bcHeight), 16) - 1) * 2))
        # print("start: " + str(start))
        # print("stop: " + str(stop))
        step = 6
        count = 0
        for i in range(start, stop, step):
            if (decoded_hex_data[i:i+step] == "000000"):
                count = count + 1
    elif (int(reverse_bytes(bciSize), 16) == 40):
        # print("3/4/5")
        biWidth = decoded_hex_data[36:44]
        biHeight = decoded_hex_data[44:52]
        biPlanes = decoded_hex_data[52:56]
        biBitCount = decoded_hex_data[56:60]
        biCompression = decoded_hex_data[60:68]
        biSizeImage = decoded_hex_data[68:76]
        biXPelsPerMeter = decoded_hex_data[76:84]
        biYPelsPerMeter = decoded_hex_data[84:92]
        biClrUsed = decoded_hex_data[92:100]
        biClrImportant = decoded_hex_data[100:108]
        # print("biWidth: " + biWidth + " - " + str(int(reverse_bytes(biWidth), 16)))
        # print("biHeight: " + biHeight + " - " + str(int(reverse_bytes(biHeight), 16)))
        # print("biPlanes: " + biPlanes + " - " + str(int(reverse_bytes(biPlanes), 16)))
        # print("biBitCount: " + biBitCount + " - " + str(int(reverse_bytes(biBitCount), 16)))
        # print("biCompression: " + biCompression + " - " + str(int(reverse_bytes(biCompression), 16)))
        # print("biSizeImage: " + biSizeImage + " - " + str(int(reverse_bytes(biSizeImage), 16)))
        # print("biXPelsPerMeter: " + biXPelsPerMeter + " - " + str(int(reverse_bytes(biXPelsPerMeter), 16)))
        # print("biYPelsPerMeter: " + biYPelsPerMeter + " - " + str(int(reverse_bytes(biYPelsPerMeter), 16)))
        # print("biClrUsed: " + biClrUsed + " - " + str(int(reverse_bytes(biClrUsed), 16)))
        # print("biClrImportant: " + biClrImportant + " - " + str(int(reverse_bytes(biClrImportant), 16)))

        start = int(int(reverse_bytes(bfOffBits), 16) * 2 + int(reverse_bytes(biWidth), 16) * (int(reverse_bytes(biBitCount), 16) / 8) * ((int(reverse_bytes(biHeight), 16) - 2) * 2))
        stop = int(int(reverse_bytes(bfOffBits), 16) * 2 + int(reverse_bytes(biWidth), 16) * (int(reverse_bytes(biBitCount), 16) / 8) * ((int(reverse_bytes(biHeight), 16) - 1) * 2))
        # print("start: " + str(start))
        # print("stop: " + str(stop))
        step = 6
        count = 0
        for i in range(start, stop, step):
            if (decoded_hex_data[i:i+step] == "000000"):
                count = count + 1
            # print(decoded_hex_data[i:i+step])
    else:
        return "NOT BMP"

    # print(int("28", 16))
    return count

# print(data)
print(get_zeros_second_line(data))
