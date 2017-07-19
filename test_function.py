def custom_score_x(game, player)
    def is_near_walls(move, walls):
        for wall in walls:
            if move in wall:
                return True
        return False

    def percent_occupied(game):
        blank_spaces = game.get_blank_spaces()
        return int((len(blank_spaces)/(game.width * game.height)) * 100)

    walls = [
        [(0, i) for i in range(game.width)],
        [(i, 0) for i in range(game.height)],
        [(game.width - 1, i) for i in range(game.width)],
        [(i, game.height - 1) for i in range(game.height)]
    ]

    corners = [(0,0), (0,game.width-1), (game.height-1,0), (game.height-1,game.width-1)]

    own_moves = game.get_legal_moves(player)
    opp_moves = game.get_legal_moves(game.get_opponent(player))
    own_score = 0
    opp_score = 0

    for move in own_moves:
        if percent_occupied(game) < 75:
            if is_near_walls(move, walls):
                own_score += 20
            if is_in_corners(move, corners):
                own_score -= 20
        else:
            if is_near_walls(move, walls):
                own_score -= 20
            if is_in_corners(move, corners):
                own_score += 20

    for move in opp_moves:
        if percent_occupied(game) < 75:
            if is_near_walls(move, walls):
                opp_score += 10
            if is_in_corners(move, corners):
                opp_score -= 20
        else:
            if is_near_walls(move, walls):
                own_score -= 10
            if is_in_corners(move, corners):
                own_score += 20

    # return float(own_score*own_score - opp_score)
    return float(own_score*own_score - 1.5*opp_score*opp_score)
