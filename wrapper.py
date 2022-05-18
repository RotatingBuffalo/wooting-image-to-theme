from ctypes import *
import ctypes
from pickle import TUPLE
from types import FunctionType
from typing import List, Tuple


def collapse(val: int):
    if(val > 255):
        val = 255
    if(val < 0):
        val = 0
    return val


class Wrapper:
    """
    A basic wrapper class around the wooting API
    To see how keys correspond to row and column values, see the official chart here: https://dev.wooting.nl/rgb-sdk-guide/introduction-2/
    """
    dll = None

    # 0 <= row <= 20
    # 0 <= column <= 5

    def __init__(self) -> None:
        """
        Loads and provides access to the wooting API,
        as well as providing convenience functions for updating the keyboard's array without having to call like 4 functions.
        """
        self.dll = windll.LoadLibrary("./wooting-rgb-sdk64")

    def is_keyboard_connected(self) -> bool:
        """
        Returns true (1) if the keyboard is connected
        """
        return self.dll.wooting_rgb_kbd_connected()

    def set_callback_for_disconnect(self, callback: FunctionType) -> None:
        """
        Takes a function pointer to a callback, which will be run when a Wooting keyboard disconnects.
        This will trigger after a failed colour change.
        """
        CWRAPPER = CFUNCTYPE(None)
        wrapped_callback = CWRAPPER(callback)
        self.dll.wooting_rgb_set_disconnected_cb(wrapped_callback)
        return

    def wooting_rgb_reset(self) -> bool:
        """
        This function will restore all the colours to the colours that were originally on the keyboard.
        This function must be called when you close the application.
        Returns true (1) if the keyboard successfully resets.
        """
        return self.dll.wooting_rgb_reset()

    def wooting_rgb_direct_set_key(self, row: int, column: int, color: List[int]) -> bool:
        """
        Directly changes the colour of 1 key on the keyboard. This will not influence the keyboard colour array. 
        Use this function for simple amplifications, like a notification. Use the array functions if you want to change 
        the entire keyboard.

        Arguments:
            row: horizontal index of the key
            column: vertical index of the key
            color: RGB tuple- each value is one byte of a colour's RGB representation.

        Return:
            Returns true (1) if the colour was successfully set.
        """

        r = collapse(color[0])
        g = collapse(color[1])
        b = collapse(color[2])

        return self.dll.wooting_rgb_direct_set_key(
            row, column, r, g, b)

    def wooting_rgb_direct_reset_key(self, row: int, column: int) -> bool:
        """
        This function will directly reset the color of 1 key on the keyboard.
        This will not influence the keyboard color array. Use this function for simple amplifications, like a notification.
        Use the array functions if you want to change the entire keyboard.

        Arguments:
            row: row of the key to reset
            column: column of the key to reset

        Returns true (1) if the colour is reset.
        """
        return self.dll.wooting_rgb_direct_reset_key(row, column)

    def wooting_rgb_array_update_keyboard(self) -> bool:
        """
        This function will send the changes made to the wooting_rgb_array single and full functions to the keyboard.
        Returns true (1) if the colours are updated.
        """
        return self.dll.wooting_rgb_array_update_keyboard()

    def wooting_rgb_array_auto_update(self, auto_update: bool) -> None:
        """
        This function can be used to set an auto-update trigger after every change with the wooting_rgb_array single and full functions function.
        By default is set to false.

        Arguments:
            auto_update: Whether or not calling `wooting_rgb_array_set_single()` or `wooting_rgb_array_set_full()` should immediately 
            update the keyboard or if the keyboard should wait until you deliberately call `wooting_rgb_array_update_keyboard()`

        """
        return self.dll.wooting_rgb_array_auto_update(auto_update)

    def wooting_rgb_array_set_single(self, row: int, column: int, color: Tuple[int, int, int]) -> bool:
        """
        This function will set a single colour in the colour array. This will not directly update
        the keyboard (unless wooting_rgb_array_auto_update() has been set to True), so it can be called frequently.
        For example in a loop that updates the entire keyboard. This way you can avoid dealing with C arrays.
        """
        r = collapse(color[0])
        g = collapse(color[1])
        b = collapse(color[2])
        return self.dll.wooting_rgb_array_set_single(row, column, r, g, b)

    def wooting_rgb_array_set_full(self, buffer: List[int]) -> bool:
        """
        NOTE: You probably don't want to use this function.\n
        This function will set a complete color array.
        This will not directly update the keyboard (unless wooting_rgb_array_auto_update() has been set to True).
        It is recommended to use `wooting_rgb_array_set_single()` because I don't even think this works.

        Go read the actual wooting docs here if you want to know more.
        https://dev.wooting.io/rgb-sdk-guide/rgb-api-description/
        """
        cbuf = (ctypes.c_uint8 * len(buffer))(*buffer)
        return self.dll.wooting_rgb_array_set_full(cbuf)
