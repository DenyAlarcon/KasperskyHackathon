import sys
import codecs

# data = "0130D0ADD182D0B8D0BC20D0B6D0B0D180D0BAD0B8D0BC20D0B8D18ED0BBD18CD181D0BAD0B8D0BC20D0B4D0BDD191D0BC2000040101060130C0EDF2F3E0EDE5F2F2E020E2FBF8EBE020EDE020EFF0EEE3F3EBEAF32C20EAE0EA20E2F1E5E3E4E02C20F0E0EDEE2E20050119CEEDE020F1EFF3F1F2E8EBEEF1FC20EA20E1E5F0E5E3F32C200D0300030101660002000204010005020002012DD09ED0BDD0B020D181D0BFD183D181D182D0B8D0BBD0B0D181D18C20D0BA20D0B1D0B5D180D0B5D0B3D1832C200602000F014DD0BFD180D0BED188D0BBD0B0D181D18C20D0BFD0BE20D0BFD0BBD18FD0B6D18320D0B820D0BDD0B0D0BFD180D0B0D0B2D0B8D0BBD0B0D181D18C20D0B220D181D182D0BED180D0BED0BDD18320060122D0B1D0BBD0B8D0B6D0B0D0B9D188D0B5D0B920D0BAD0B0D184D0B5D0B9D0BDD0B82E120122D0B1D0BBD0B8D0B6D0B0D0B9D188D0B5D0B920D0BAD0BED184D0B5D0B9D0BDD0B82E03050005"

data = sys.stdin.readline()
data_length = len(data)
# print(data_length)

buffer = ""

charset = "utf-8"

def get_sum_bytes(bytes):
    sum = 0
    for i in range(0, len(bytes), 2):
        sum = sum + int(bytes[i:i+2], 16)
    return sum

i = 0
while i < data_length:
    # print("i: " + str(i))
    message_type = data[i:i+2]
    body_length = data[i+2:i+4]
    body_length_int = int(body_length, 16)
    # print("body_length_int: " + str(body_length_int))
    body = data[i+4:i+body_length_int*2+4]
    # print("body: " + str(body))
    decoded_body = codecs.decode(body, "hex").decode(charset)
    # print("decoded_body: " + str(decoded_body))
    control_sum = data[i+body_length_int*2+4:i+body_length_int*2+6]
    # print("control_sum: " + control_sum)

    if message_type == '01':
        # print("Добавить текст")
        remainder = get_sum_bytes(data[i:i+body_length_int*2+4]) % 8
        # print(remainder)
        if (remainder == int(control_sum, 16)):
            # print("Контрольная сумма верна")
            buffer = buffer + decoded_body
        # else:
        #     print("Контрольная сумма неверна")
    elif message_type == '02':
        # print("Удалить последний символ")
        # print("*" + buffer + "*")
        buffer = buffer[0:-1]
        # print("*" + buffer + "*")
    elif message_type == '03':
        # print("Продублировать последний символ")
        # print("*" + buffer + "*")
        buffer = buffer + buffer[-1]
        # print("*" + buffer + "*")
    elif message_type == '04':
        # print("Сменить кодировку")
        if body == "00":
            charset = "utf-8"
        elif body == "01":
            charset = "cp1251"
    elif message_type == '05':
        # print("Напечатать страницу")
        print(buffer)
    i = i + body_length_int * 2 + 6
    # print("---------------------")
    # body = data[4:(4+24)*4]
    # str1 = "abc"
    # print(str1[0:-1])
