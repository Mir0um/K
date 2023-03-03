
class color():
    reset_color = '\033[0m'

    def set_color(r, g, b, background=False):
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

    def clear():
        print("\n" * 100 + "\033c")

if __name__ == "__main__":
    print(str(color.set_color(0,200,0,True)) + "test")