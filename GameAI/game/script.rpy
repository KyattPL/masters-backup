define me = Character('Me', color="#c8c8ff")
define adam = Character('Adam', color="#ffffcc")
define florian = Character('Florian', color="#33ccff")
define mary = Character('Mary', color="#6666ff")
define nathaniel = Character('Nathaniel', color="#79798b")
define randy = Character('Randy', color="#ffcc66")

default was_adam_questioned = False
default was_florian_questioned = False
default was_mary_questioned = False
default was_nathaniel_questioned = False
default was_randy_questioned = False

default protagonist_name = "John"

label start:
    jump intro

label bad_end:
    "GAME FINISHED - BAD ENDING"
    return

label good_end:
    "GAME FINISHED - GOOD ENDING"
    return