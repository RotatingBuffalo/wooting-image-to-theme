from imagetokeyboard import image_to_wooting_sized_buffer
from wrapper import *
from time import sleep


def main():
    w = Wrapper()
    if not (w.is_keyboard_connected()):
        print("your keyboard isn't even connected dingus.")
        return
    wallpaper = "C:/Users/maxbe/Theming/Wallpapers/landscapes/evening-sky.png"
    newColors = image_to_wooting_sized_buffer(
        wallpaper)
    for i in range(6):
        for j in range(21):
            w.wooting_rgb_array_set_single(i, j, newColors[j*i + j])

    w.wooting_rgb_array_update_keyboard()
    sleep(5)
    w.wooting_rgb_reset()


if __name__ == "__main__":
    main()
