# astroplot

Astronomy images are difficult to plot in a single line of code.
Astropy's ```simple_norm``` exists, but I wanted something easier than that. 

So here is astroplot -- Just call the function and it plots the image in logscale.

![image](https://github.com/SterlingYM/astroplot/assets/45109159/19626d06-860f-4c90-8c0f-8861b6f728a7)

Compare this against ```matplotlib.imshow()```:

![image](https://github.com/SterlingYM/astroplot/assets/45109159/5308ec8e-6c8a-4059-a29b-f9f3afc5a68a)

You can specify options, color maps, etc.

![image](https://github.com/SterlingYM/astroplot/assets/45109159/3e66408b-5bb0-473b-868a-08d085d50899)

An example to
1. specify color map
2. specify axes
3. set lower- and upper- flux percentiles (at which the values are considered minimum and maximum)
4. use the same color normalization for multiple images
![image](https://github.com/SterlingYM/astroplot/assets/45109159/c18aad14-959a-4e56-a71b-04c122caf336)
