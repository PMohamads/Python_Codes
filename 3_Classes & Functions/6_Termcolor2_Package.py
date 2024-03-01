from termcolor2 import c
from termcolor2 import colored
print(c("hello").red.on_white.blink.underline.dark)
print(colored('hello', 'red'), colored('world', 'green'))

