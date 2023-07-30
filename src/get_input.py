"""Defining input class."""
import sys
import termios
import tty
import signal


# This Python code defines a class Get with a single method __call__ which gets a single character of input from the user.
# The __call__ method uses the termios and tty modules to put the terminal in raw mode, which allows the program to read input one character at a time, without waiting for the user to press enter.
# It then uses the sys.stdin.read(1) method to read a single character from the standard input stream (which is usually the keyboard), and returns that character.
# Overall, this class can be used to get a single character of input from the user in a Python program.
class Get:
    """Class to get input."""

    def __call__(self):
        """Defining __call__."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class AlarmException(Exception):
    """Handling alarm exception."""
    pass


def alarmHandler(signum, frame):
    """Handling timeouts."""
    raise AlarmException


def input_to(getch, timeout=0.1):
    """Taking input from user."""
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return None
    

# The first code block defines a Python function called input_to that takes a getch function as an argument and reads a single character of input from the user within a specified timeout. The second code block defines a class called Get that provides a similar functionality of reading a single character of input from the user.
# However, there are some differences in functionality between these two implementations:

# input_to takes a function getch as an argument, which is used to read a single character of input from the user. This allows the user to provide their own function for getting input, which can be useful for custom input sources (e.g., a game controller or a hardware device). In contrast, the Get class has a fixed implementation of getting input from the keyboard using the tty and termios modules.
# input_to sets a signal handler to handle timeout and returns None if no input is received before the timeout. In contrast, the Get class blocks the program until input is received, which may not be desirable in some applications.
# input_to returns None if no input is received before the timeout. In contrast, the Get class will keep waiting for input until a character is received.
# In summary, the input_to function is a more flexible and configurable way to get input with a timeout, while the Get class provides a simpler implementation that blocks until input is received.