# PsuedoCasting (working title) 

Cool system of rendering Graphics, in a 2.5d Wolfenstein style.

<I> Basically Fake Ray Casting. </I>

PseudoCasting is my new way of rendering "3d" graphics in python & pygame (or whatever language).

It's similar to [raycasting](http://lodev.org/cgtutor/raycasting.html), but more basic, and with less math.

The PseudoCasting engine takes a provided image, with a specified palette, and renders it in "3d" space with a first person camera.

### This is an example of a map image:

![Map Model](http://i.imgur.com/tSVaCJx.png)

The actual area is drawn to the left, and the palette is defined on the right.

The palette is used like this:

![Le Palette](http://i.imgur.com/iJZmhhV.png)

### This, as of version 2.0 (certainly not the final result), is what the engine looks like

![3d Rendered](http://i.imgur.com/LyEBkVG.png)
