###### BOARD REPERSENTATION AS A 1D ARRAY ------> CONVERT TO BITBOARD ONCE WE HAVE MOVE ORDERING WELL DONE.


#### BOARD


from pickle import TRUE


BOARD = [
        ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
        ' ','R','N','B','Q','K','B','N','R',' ',
        ' ','P','P','P','P','P','P','P','P',' ',
        ' ','.','.','.','.','.','.','.','.',' ',
        ' ','.','.','.','.','.','.','.','.',' ',
        ' ','.','.','.','.','.','.','.','.',' ',
        ' ','.','.','.','.','.','.','.','.',' ',
        ' ','p','p','p','p','p','p','p','p',' ',
        ' ','r','n','b','q','k','b','n','r',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ',' ',' '
        ]

#### GENERATE MOVES + CASTLE MOVE + EN PASSANT 

DIRECTIONS = {
    'N': -10,
    'S': 10,
    'E': 1,
    'W': -1 
    }


blackPieceLocations = {
    'K': [25],
    'Q': [24],
    'B': [23,26],
    'N': [22,27],
    'R': [21,28],
    'P': [31,32,33,34,35,36,37,38]
}

whitePieceLocations = {
    'K': [95],
    'Q': [94],
    'B': [93,96],
    'N': [92,97],
    'R': [91,98],
    'P': [81,82,83,84,85,86,87,88]
}

pieceLocations = {
    True: whitePieceLocations,
    False: blackPieceLocations
}

whitePromotionRow = [21,22,23,24,25,26,27,28]
blackPromotionRow = [91,92,93,94,95,96,97,98]
whitePawnStart = [81,82,83,84,85,86,87,88]
blackPawnStart = [31,32,33,34,35,36,37,38]
whitePieces = ['p','n','b','r','q','k']
blackPieces = ['P','N','B','R','Q','K']

def pawnMove(square, color):

    forward = 10
    pawnStart = blackPawnStart
    pawnPromotion = blackPromotionRow
    capturable = whitePieces
    if color: # we are white
        forward = -10
        pawnStart = whitePawnStart
        pawnPromotion = whitePromotionRow
        capturable = blackPieces
    legalMoves = []
    oneUp = square + forward
    # forward moves
    if BOARD[oneUp] == '.': # can move here
        legalMoves.append([square, oneUp])
        twoUp = oneUp + forward
        if BOARD[twoUp] == '.' and square in pawnStart:
            legalMoves.append([square, twoUp])
    eastCapture = oneUp + 1
    westCapture = oneUp - 1
    # captures
    if BOARD[eastCapture] in capturable:
        legalMoves.append([square, eastCapture])
    if BOARD[westCapture] in capturable:
        legalMoves.append([square, westCapture])
    return legalMoves





def knightMove(square, color):
    legalMoves = []
    capturable = whitePieces
    if color:
        capturable = blackPieces    
    for x in [10, -10, 1, -1]:
        if x == 10 or x == -10:
            for i in [1,-1]:
                pos = square + 2*x + i
                
                if BOARD[pos] in capturable or BOARD[pos] == '.':
                    legalMoves.append([square, pos])
        if x == 1 or x == -1:
            for i in [10,-10]:
                pos = square + 2*x + i
                
                if BOARD[pos] in capturable or BOARD[pos] == '.':
                    legalMoves.append([square, pos])
    return legalMoves




def bishopMove(square, color):
    legalMoves = []
    capturable = whitePieces
    if color:
        capturable = blackPieces
    
    diagonals = [11, 9, -11, -9]
    for i in diagonals:
        for x in range(1,8):
            pos = square + (i*x)

            if BOARD[pos] in capturable:
                legalMoves.append([square, pos])
                break
            if BOARD[pos] == '.':
                legalMoves.append([square, pos])
            else:
                break
            
        
    return legalMoves


def rookMove(square, color):
    legalMoves = []
    capturable = whitePieces
    if color:
        capturable = blackPieces
    directions = [10,-10,1,-1]
    for i in directions:
        for x in range(1,8):
            pos = square + (i*x)

            if BOARD[pos] in capturable:
                legalMoves.append([square, pos])
                break
            if BOARD[pos] == '.':
                legalMoves.append([square, pos])
            else:
                break
    return legalMoves




def queenMove(square, color):
    legalMoves = []
    legalMoves += rookMove(square, color)
    legalMoves += bishopMove(square, color)
    return legalMoves
    

def kingMove(square, color):
    legalMoves = []
    capturable = whitePieces
    if color:
        capturable = blackPieces

    directions = [10,-10,1,-1]
    for i in directions:
        
        pos = square + (i)

        if BOARD[pos] in capturable:
            legalMoves.append([square, pos])
            
        if BOARD[pos] == '.':
            legalMoves.append([square, pos])
        else:
            pass
    
    diagonals = [11, 9, -11, -9]
    for i in diagonals:
        
        pos = square + (i)

        if BOARD[pos] in capturable:
            legalMoves.append([square, pos])
            
        if BOARD[pos] == '.':
            legalMoves.append([square, pos])
        else:
            pass
    

    
    return legalMoves



def genMoves(color):
    legalMoves = [] 
    locations = pieceLocations[False]
    if color:
        locations = pieceLocations[True]
    for piece in locations:
        if piece == 'K':
            legalMoves += kingMove(locations[piece][0], color)
        elif piece == 'Q':
            for pos in locations[piece]:
                legalMoves += queenMove(pos, color)
        elif piece == 'R':
            for pos in locations[piece]:
                legalMoves += rookMove(pos, color)
        elif piece == 'B':
            for pos in locations[piece]:
                legalMoves += bishopMove(pos, color)
        elif piece == 'N':
            for pos in locations[piece]:
                legalMoves += knightMove(pos, color)
        elif piece == 'P':
            for pos in locations[piece]:
                legalMoves += pawnMove(pos, color)
        



    return legalMoves








