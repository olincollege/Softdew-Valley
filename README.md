# Stardew Valley Clone
Stardew Valley Clone (also known as SoftDew Valley) is a project designed to 
replicate the main farming aspects of the game Stardew Valley by ConcernedApe.
This project uses a MVC (model, view, controller) architecture and the pygame 
library. The model aspects are made up of classes for different objects in the 
game (farmer class, ground class, inventory class, etc) and a main model class. 
The main model class handles interactions between these classes. The view class
handles displaying sprites and other information, and the controller class 
takes user input to update the model classes.

The main functions of our game are to plant seeds, water them, and harvest them after 
the necessary number of days. The controls for the game are explained in more 
detail in the usage section.

## Website Link
Our website can be found at https://olincollege.github.io/Softdew-Valley/

## Installation 
Use our *requirements.txt* file to install the required libraries 

```bash
pip install -r requirements.txt 
```

## Usage 
The game can be run by running the main.py file. 

The user can control their character using WASD keys to move up, left, down, 
and right respectively. The number keys can be used select a slot in the 
inventory, and once the user has an item selected (hoe, watering can, seed), 
the space bar can be used to use the item. Inventory slots can also be selected
by clicking on the desired item. Different plants have different numbers 
of days they take to grow and must be watered every day to grow. A plant will 
not grow if it is not watered. The user can sleep by entering the house and 
walking to the bed and can harvest plants by pressing the H key once that plant
is fully grown.

## Credits
The people that worked on this project were Alex George, Amanda Chang, and 
Meagan Lipsman.
