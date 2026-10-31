# Chess Trainer
A chess board that can show current position of the pieces, as well as highlight vulnerability state of each piece, and also square occupation for the empty squares of the board (on which empty squares it's currently safe to move a piece). It does not involve bots, you move white & black pieces manually throughout the game.

The idea is to use this application during a game so it can show you, for example, which pieces are safe to capture or which pieces of yours are currently guarded by other pieces. In other words, it saves you the effort of carefully observing the entire board piece by piece and lets you focus on the game strategy itself. This is very suitable for beginners that already know the rules (moves, etc.), but don't know any strategies and are not used to keeping track of everything in chess.

> [!NOTE]
> This project is a work-in-progress and there's still a few things to be done to complete or improve its functionality.

### USAGE:  
The software uses basic chess sprites for rendering the regular chess board and pieces, as well as additional icons & colors to highlight the details in the current situation. The icons & colors go as described:
- Colors:
  - blue: white's occupancy
  - red: black's occupancy
  - green: both teams occupy the square
- Icons:
  - dot: a regular move (only rendered on a empty square)
  - ring: a piece is unguarded and can be captured (blue ring: white can safely capture, red ring: black can safely capture)
  - star: a piece is guarded (it may also appear on a empty square if a pawn can promote itself)
  - flag: castling can be made
  - cross: en passant can be made

The software uses importance priority in rendering specific icons: for example, if a piece is guarded but also threatened at the same time, the game will draw a star but will use the green color to draw it.

To launch software run the `main.py` file.

### CONTROLS:  
**[ MOUSE ]** select squares and move pieces on the board  
**[ ARROWKEYS ]** traverse previous moves in a game  
**[ SPACE ]** plays a random legal move for the current player  
**[ I ]** toggle the render of 'dot' icons (for the highlights only)  
**[ S ]** save the game to a text file that is loaded into the board upon running the software  
**[ ESC ]** close software

### REQUIREMENTS:
Python 3.11+  
Pygame 2.3.1+

### SCREENSHOTS:  
<img width="1308" height="1347" alt="Screenshot (19)" src="https://github.com/user-attachments/assets/4b0f8caf-031d-4642-b276-4dbb24ef4902" />
<img width="1311" height="1347" alt="Screenshot (20)" src="https://github.com/user-attachments/assets/1a287ad0-2fcf-4bcf-a6a7-cf509934fbb2" />
<img width="1307" height="1343" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/74fb3d7a-9ccd-48ab-8903-e25a018db7ab" />
<img width="1305" height="1347" alt="Screenshot (29)" src="https://github.com/user-attachments/assets/2e146e8d-4f68-44d6-ba13-f167da427f80" />
<img width="1308" height="1347" alt="Screenshot (30)" src="https://github.com/user-attachments/assets/652d03ca-14c9-42d8-b76b-99953652a577" />
