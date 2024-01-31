# A Hawaiian Star Dictionary - star_names

#### Video Demo: https://youtu.be/7K9GUJiiuJY

#### Description: My program I created was inspired by the Hawaiian stars. Like other cultures, Native Hawaiians had names for their own stars. There are a total of 26 stars that can be named in Hawaiian. I decided to create a program that would serve as a Hawaiian star dictionary where the user could input the name of a star, and it would output the Hawaiian name for that star (should it exist).


#### I first created a csv file that included the english and hawaiian names for the 26 stars. I made sure to note that they were written in a specific way that would require me to convert the user input to a new form using title(). The name of my csv file is inoa_hoku.csv. In my project.py file, I organized it in a way that prompted the user to input a "star name" and then I checked that the input was valid.

#### Valid inputs had to make sure that it was not at all numeric. Valid inputs also had to make sure it wasn't just blank. Also, when the input was finally compared to that of the information within the csv file, there was a final check if that star was in fact in that list or not.

#### Instead of just making the hawaiian star name as an output by itself, I decided to make it into a sentence. To verbalize that the Hawaiian name for "blank" star was "blank". I also wanted to add a creative twist to my output. This is where i put a lot of my time into figuring out. I wanted to include along with the sentence, a hawaiian tribal pattern that I was able to create using ASCII characters. That way, I was cleverly able to include some kind of visual in the terminal window along with the sentence.

#### I also created a test_project.py file that serves as a test module for my program. I was able to test 3 of the functions that i created in the program to make sure they worked as anticipated.