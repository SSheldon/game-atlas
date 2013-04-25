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

def user_game_vector(user_games, game_indices):
    game_vector = [0] * len(game_indices)
    # Set the bits for this user's games
    for game_id in user_games:
        game_vector[game_indices[game_id]] = 1
    return game_vector

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

def recommend_games(user_id, all_user_games, games):
    # Create a mapping from game_id to its vector index
    game_indices = {game_id: i for i, game_id in enumerate(games)}
    game_vector = user_game_vector(all_user_games[user_id], game_indices)
    all_game_vectors = [
        user_game_vector(games, game_indices)
        for games in all_user_games.itervalues()
    ]
    recommended_indexes = recommend(game_vector, all_game_vectors)
    return [game_indices[i] for i in recommended_indexes]
