# Create matrix of Users x Games
# Each row should be a User
# Each column should be a Game
	# For testing
UserGames = [
		[1, 1, 0, 1],
		[0, 0, 1, 1],
		[1, 0, 0, 0],
		[0, 1, 1, 0],
		[1, 0, 1, 0]
	]

for currentUser in UserGames:
	rankings = []
	for otherUser in UserGames:
		rankings.append(getRanking(currentUser, otherUser))
