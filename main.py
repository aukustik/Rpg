from character import MainChar
from level_turtorial import LevelTurtorial
from achievments import *

main_character = MainChar("Vitalik")
first_kill = FirstKill()
main_character.add_observer(first_kill)
level = LevelTurtorial()
level.turtorial(main_character)