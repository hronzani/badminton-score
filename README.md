# badminton-score
A simple and fast scoreboard for badminton games and tournaments

Although Badminton was the inspiration, this scoreboard could be used in other sports, with few modifications.

The main goal is to be used with a Raspberry Pi (console mode, not grafic) and TV, so it could be used in places without an eletronic scoreboard. But its ok to use with any computer also, just uncomment the full screen option on main file.

It runs under python 3 (recommended) or 2, and needs pygame (native on Raspberry Pi, or use *pip install pygame* to get it) .

**Keyboard Controls**
Key|Function
---|--------
a|increment by 1 point Player 1 current game
z|decrement by 1 point Player 1 current game
j|increment by 1 point Player 2 current game
m|decrement by 1 point Player 2 current game
2|show second game score
3|show third game score
4|hide second game score
5|hide third game score
9|Quit program

The simple layout was inspired by [this project](https://github.com/bnw/badminton-anzeige).

**Screenshot:**

![Badminton Scoreboard](./scrshot.png)

**Usage:**

$ python badminton_score.py

Enter the name of players, and enjoy :)
