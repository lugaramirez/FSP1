class Movie():
  """Bounds the variables used on the webpage to the object."""

  def __init__(self, title, genre, storyline, poster_image, trailer_youtube):
    """__init__ method.

        Sets the variables on the instance of 'Movie' in order to be used
        lated at the webpage generator.

        Args:
            title (str): Title of the movie to be shown on the webpage.
            genre (str): Genre to generate the tags and the selector list.
            storyline (str): From the movie, in order to display it on the
                modal that is shown when the poster image is click.
            poster_image (str): URL that shows the poster image to be shown
                on the webpage.
            trailer_youtube (str): URL of the movie trailer to be load on
                the modal.

        """
    self.title = title
    self.tag = genre.replace(" ", "")
    self.genre = genre
    self.storyline = storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube
    