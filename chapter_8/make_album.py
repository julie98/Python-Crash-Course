def make_album(artist, title, tracks = 0):
	"""Build a dictionary containing information about an album."""
	singer_album = {
	'artist' : artist.title(),
	'title' : title.title(),
	'tracks' : tracks,
	}

	return singer_album


# album = make_album('taylor swift', 'reputation', 8)
# print(album)

# album = make_album('beethoven', 'ninth symphony')
# print(album)

# album = make_album('avirl lavigne', 'let go')
# print(album)


artist_prompt = "Please input the artist. "
title_prompt = "Please input the title. "
tracks_prompt = "Please input the tracks. "

while True:
	artist_name = input(artist_prompt)
	if artist_name == 'quit':
		break
	title_name = input(title_prompt)
	if title_name == 'quit':
		break
	tracks_name = input(tracks_prompt)
	if tracks_name == 'quit':
		break
	else:
		album = make_album(artist_name, title_name, tracks_name)
		print(album)