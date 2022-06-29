# 4-mini-projects-at-Python

1)Let's be a 3 * 3 square in which you place rings. You have 27 rings, 9 for each size (small, medium, large). A triad that ends the game is done horizontally, vertically or diagonally. The trinity consists of rings of either the same size or from the smallest to the largest. Because you have rings, a ring can fit in any square, as long as it does not already have a ring of the same size. Write a program that randomly plays the game 100 times and returns the average of the steps to end the game.

2)Let's be a 3 * 3 square in which you place "caps". You have 27 "caps", 9 for each size (small, medium, large). A triad that ends the game is done horizontally, vertically or diagonally. The triad consists of caps of either the same size or from the smallest to the largest. Because you have lids, a lid can fit in any square, as long as it is free or there is a smaller lid. Write a program that randomly plays the game 100 times and returns the average of the steps to end the game.

5)You are given a text file that has only ASCII characters. First, edit the text so that you are left with only lowercase letters (uppercase and lowercase) and space. First, split this text into words according to the space. In the words you have, calculate the following statistics: a) what are the ten most popular words? If some appear the same number and come out more than ten, keep whichever you think or by chance. b) What are the first three combinations of the first two letters that most words begin with? c) Repeat the same for three letters.

7)Let's be an ASCII text file that contains a Python dictionary in each line. Each line dictionary contains the same keys as the other lines. These keys contain values that can only be numbers or text. Write code that reads this file, displays the available keys to the user and asks which of the available keys he is interested in. Then for this key displays the most popular value, the highest and the lowest.<br>
Example:<br>
Suppose your file contains the following dictionaries<br>
{"x": 3, "y": 4, "name": "bob"}<br>
{"x": 13, "y": - 4, "name": "malory"}<br>
{"x": - 3, "y": 104, "name": "trudy"}<br>
{"x": 1, "y": 14, "name": "alice"}<br>
Your password is displayed to the user: x, y, name<br>
Asks the user for the key. If he selects y, your code will have to return the values -4 and 104.
