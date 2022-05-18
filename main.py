
from imagetokeyboard import image_to_wooting_sized_buffer
from wrapper import *
import winreg


def main():
    w = Wrapper()
    if not (w.is_keyboard_connected()):
        print("your keyboard isn't even connected dingus.")
        return
    # Doing a little bit of windows registry tomfoolery to get your current wallpaper.
    wallpaperKey = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop")
    cw_path = winreg.QueryValueEx(wallpaperKey, "WallPaper")[0]

    # The actual code.
    newColors = image_to_wooting_sized_buffer(cw_path)
    for i in range(0, 21):
        for j in range(0, 6):
            w.wooting_rgb_array_set_single(j, i, newColors[i*6 + j])
    w.wooting_rgb_array_update_keyboard()


if __name__ == "__main__":
    main()
