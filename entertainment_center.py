import fresh_tomatoes
import media

interstellar = media.Movie("Interstellar",
	"SciFi",
	"In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team of researchers through the wormhole and across the galaxy to find out which of three planets could be mankind's new home.",
	"http://meetinthelobby.com/wp-content/uploads/2014/11/Interstellar-Teaser-Movie-Poster-Large.jpg",
	"https://www.youtube.com/watch?v=0vxOhd4qlnA")

prometheus = media.Movie("Prometheus",
	"SciFi Thriller",
	"The discovery of a clue to mankind's origins on Earth leads a team of explorers to the darkest parts of the universe. Two brilliant young scientists lead the expedition. Shaw (Noomi Rapace) hopes that they will meet a race of benevolent, godlike beings who will in some way verify her religious beliefs, while Holloway (Logan Marshall-Green) is out to debunk any spiritual notions. However, neither the scientists nor their shipmates are prepared for the unimaginable terrors that await them.",
	"http://www.gstatic.com/tv/thumb/movieposters/8815605/p8815605_p_v7_ad.jpg",
	"https://www.youtube.com/watch?v=HHcHYisZFLU")

martian = media.Movie("The Martian",
	"SciFi",
	"When astronauts blast off from the planet Mars, they leave behind Mark Watney (Matt Damon), presumed dead after a fierce storm. With only a meager amount of supplies, the stranded visitor must utilize his wits and spirit to find a way to survive on the hostile planet. Meanwhile, back on Earth, members of NASA and a team of international scientists work tirelessly to bring him home, while his crew mates hatch their own plan for a daring rescue mission.",
	"http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
	"https://www.youtube.com/watch?v=ej3ioOneTy8")

movies = [prometheus, interstellar, martian]
fresh_tomatoes.open_movies_page(movies)