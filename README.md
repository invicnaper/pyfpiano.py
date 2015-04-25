# pyfpiano.py
a tiny instrument player written in python

![alt text](http://nsa38.casimages.com/img/2015/04/25/15042502361591450.png "pyfpiano.py console")
![alt text](http://nsa38.casimages.com/img/2015/04/25/150425023719886467.png "pyfpiano.py")


# How to Install it

pyfpiano.py is designed for linux , to use the script you should install some modules and libraries

    sudo apt-get install fluidsynth
    sudo apt-get install libavbin-dev
    
python modules

    sudo pip install pygame
    sudo pip install pyglet
    sudo pip install mingus
    sudo pip install fluidsynth
    
# How to use it
 
Download the script , then execute it using python .

    python pyfpiano.py --help
or
    ./pyfpiano.py --help
    
# Play piano

    ./pyfpiano.py --play piano
  
# Play guitar

    ./pyfpiano.py --play guitar
    
# Changing notes

    ./pyfpiano.py --play piano --note 3
    
this will play notes using the type 3 ; ex : A-3 C-3 E-3 F-3 G-3  
    
# Saving the play

    ./pyfiano.py --play piano --save test
    
then when you wanna save the file , press 's' 

# Note list 

- 0 - C#
- 1 - D#
- 2 - F# 
- 3 - G#
- 4 - A# 
