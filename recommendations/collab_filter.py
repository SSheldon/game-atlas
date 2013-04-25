# Computes the dot product of two vectors
def dot(VectorA, VectorB):
	sum = 0
	length = min(len(VectorA), len(VectorB))
	for i in range(0, length):
		sum += VectorA[i]*VectorB[i]
	return sum

# Computes the norm of a vector
def norm(Vector, power):
	radicand = 0
	for element in Vector:
		radicand += pow(element, power)
	return pow(float(radicand), 1/float(power))

# Gets the ranking of two users using vector space model search
def getRanking(UserA, UserB):
	return dot(UserA, UserB)/(norm(UserA, 2)*norm(UserB, 2))

def user_game_vectors(games, all_user_games):
    # Create a mapping from game_id to its vector index
    game_index = {game_id: i for i, game_id in enumerate(games)}
    for user_id, user_games in all_user_games.iteritems():
        game_vector = [0] * len(games)
        # Set the bits for this user's games
        for game_id in user_games:
            game_vector[game_index[game_id]] = 1
        # print user_id, game_vector
        yield user_id, game_vector

# Replace with code to select from user_game
# Create 2d matrix where rows are users and columns are games
# We may need additional dictionaries to map row indexes to user_ids
# and column indexes to game_ids
UserGames = [
		[1, 1, 0, 1],
		[0, 0, 1, 1],
		[1, 0, 0, 0],
		[0, 1, 1, 0],
		[1, 0, 1, 0]
	]

def recommend(currentUser, UserGames):
	rankings = {}
	for j, otherUser in enumerate(UserGames):
		rankings[j] = getRanking(currentUser, otherUser)
	rankings = list(reversed(sorted(rankings.items(), key=lambda x: x[1])))
	
	recommendations = []
	for ranking in rankings:
		otherUser = UserGames[ranking[0]]
		for i in range(0, len(otherUser)):
			if (otherUser[i] and not currentUser[i] and i not in recommendations):
				recommendations.append(i)
	return recommendations

for currentUser in UserGames:
	# Replace this with code to insert into database
	print recommend(currentUser, UserGames)
