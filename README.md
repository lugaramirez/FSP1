# FSP1
Full Stack Web Developer Project 1

This code uses Udacity's "fresh_tomatoes.py" (with some modifications) to create a movie trailers list with titles, genres, storylines, posters, and trailers.

In order to modify the content of the generated html code, you should add each entry in the file "entertainment_center.py" as follows:

 Template for entry creation
 ---------------------------
 ```
 variable_name = media.Movie(
    "Title",
    "Genre",
    "Storyline",
    "Poster image URL",
    "Youtube trailer URL")
```

And then, in order for it to appear on the generated page, you should add this new entry (in the example "variable_name"), to the "movies" array (found at the second to last line in the file).

To render the page, install python (2.7 or 3.4 from https://www.python.org/downloads/ ). Copy all the files (entertainment_center.py, media.py, fresh_tomatoes.py) to a known location and execute:

Windows:
```
[file location]> c:\python[version number]\python.exe entertainment_center.py
```
Linux:
```
[file location]$ python entertainment_center.py
```

This will open a new tab on your default browser and generate an html file on [file location] that you can use and upload anywhere.
