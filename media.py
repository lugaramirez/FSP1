class Movie():
  def __init__(self, title, genre, storyline, poster_image, trailer_youtube):
    self.title = title
    self.tag = genre.replace(" ", "")
    self.genre = genre
    self.storyline = storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube
    