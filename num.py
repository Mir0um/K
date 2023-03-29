from ctypes import cdll, c_char_p, c_int, pointer

lib = cdll.LoadLibrary('./libnum.so')

def inverse_num(nb, siz):
    return lib.inverse_num(nb, siz)

def ralong(text, length):
    text_ptr = c_char_p(text.encode('utf-8'))
    length_ptr = c_int(length)
    result = lib.ralong(text_ptr, length_ptr)
    return result.decode('utf-8')

