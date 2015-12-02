import webbrowser
import os
import re

# Styles and scripting for the page
# (changed the top margin of the modal to accommodate for the movie storyline
# and added select2 for the movie-genre-select)
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="http://cdnjs.cloudflare.com/ajax/libs/select2/4.0.1/css/select2.min.css" rel="stylesheet" />
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/select2/4.0.1/js/select2.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 50px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
</head>
'''


# The main page layout and title bar
# (added a select dropdown to show only the selected genre)
main_page_content = '''
  <body>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-8">
          <label>Movie genre(s) to show: </label>
          <select class="genres-droplist" multiple="multiple" style="width:75%"></select>
        </div>
      </div>
      <div class="row">{movie_tiles}</div>
    </div>

    <!-- Modals Data -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
          <div class="modal-body text-center" id="movie-storyline">
          </div>
        </div>
      </div>
    </div>

    {js_script}

  </body>
</html>
'''

# A single movie entry html template
# (v2.0 should improve the long storyline and re-do the webpage
# generation)
movie_tile_content = '''
        <div class="col-md-6 col-lg-4 movie-tile text-center All {movie_tag}" data-trailer-youtube-id="{trailer_youtube_id}" data-movie-storyline="{movie_storyline}" data-toggle="modal" data-target="#trailer">
            <img src="{poster_image_url}" width="220" height="342">
            <h2>{movie_title}</h2>
            <span class="label label-primary" data-genre="{movie_genre}" data-tag="{movie_tag}">{movie_genre}</span>
        </div>
'''

# JS script variable to append it at the end, so we can generate
# a droplist from the pre-rendered labels
# (although that is already solved with the 'document.ready' function, 
# I'm just used to put my scripts at the end...)
script = '''
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            /* added the storyline description on the modal body */
            $("#movie-storyline").empty().append($("<p>"+$(this).attr('data-movie-storyline')+"</p>"));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        /* Inits the droplist as a select2 */
          $(".genres-droplist").select2({placeholder: "Select a genre"});
        /* Generates the movie-genre droplist by checking if each label found on the tile
        exists or not already as an option in it */
          $(".label-primary").each(function(){
            var exists = false;
            var genre = $(this).attr('data-genre');
            var tag = $(this).attr('data-tag');
            $(".genres-droplist option").each(function(){
              if ($(this).attr('value') == genre) {
                exists = true;
              }
            });
            if (!exists) {
              $(".genres-droplist").append($("<option value='"+tag+"'>"+genre+"</option>"));
            }
          });
        /* Checks for a change on the select2 and shows whatever is chosen hiding everything else
        by using a cheat hiding first all of the tiles and then showing just the ones selected */
          $(".genres-droplist").on("change", function(){
            if ( $(".genres-droplist").select2("data").length ) {
              $(".All").hide();
              $(".genres-droplist").select2("data").forEach(function(SelectedItem){
                $("."+SelectedItem['id']).show();
              });
            } else {
              $(".All").show();
            }
          });
          
        });
    </script>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        # (added some more info to improve the modal and the front 
        # page as well)
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_tag=movie.tag,
            movie_genre=movie.genre,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    # (here we could add some more content by adding a modal generator,
    # thus, changing the js that loads every modal must be done)
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        js_script=script)

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
