# -*- coding: utf-8 -*-
import winsound
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Sound file names (must be in the same directory as this file)
correct_file = "correct.wav"
game_complete_file = "game_complete.wav"
wrong_answer_file = "wrong_answer.wav"

# Create the full paths
correct_path = os.path.join(current_directory, correct_file)
game_complete_path = os.path.join(current_directory, game_complete_file)
wrong_answer_path = os.path.join(current_directory, wrong_answer_file)

def Correct():
    winsound.PlaySound(correct_path, winsound.SND_FILENAME)

def Game_complete():
    winsound.PlaySound(game_complete_path, winsound.SND_FILENAME)

def Wrong_answer():
    winsound.PlaySound(wrong_answer_path, winsound.SND_FILENAME)
