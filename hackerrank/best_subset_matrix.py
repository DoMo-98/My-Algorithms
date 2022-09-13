# def get_zero_zero( matrix ):
#     length = len( matrix ) - 1
#     return max( [ matrix[0][0], matrix[0][ length ], matrix[ length ][0], matrix[ length ][ length ] ] )

# def get_zero_one( matrix ):
#     length = len( matrix ) - 1
#     return max( [ matrix[0][1], matrix[0][ length - 1 ], matrix[ length ][1], matrix[ length ][ length - 1 ] ] )

# def get_one_zero( matrix ):
#     length = len( matrix ) - 1
#     return max( [ matrix[1][0], matrix[1][ length ], matrix[ length - 1 ][0], matrix[ length - 1 ][ length ] ] )

# def get_one_one( matrix ):
#     length = len( matrix ) - 1
#     return max( [ matrix[1][1], matrix[1][ length - 1 ], matrix[ length - 1 ][1], matrix[ length - 1 ][ length - 1 ] ] )

# ----------------------------------------------------------------------------------------------------------------------

def get_sum_bestdiagonalset( matrix ):
    length = len( matrix ) - 1
    max_numbers = []

    for i in range( len( matrix ) // 2 + 1 ):
        max_numbers.append( max( [ matrix[i][i], matrix[i][ length - i ], matrix[ length - i ][i], matrix[ length - i ][ length - i ] ] ) )
        for j in range( i + 1, len( matrix ) // 2 + 1 ):
            max_numbers.append( max( [ matrix[i][j], matrix[i][ length - j], matrix[ length - i ][j], matrix[ length - i ][ length - j ] ] ) )
            max_numbers.append( max( [ matrix[j][i], matrix[j][ length - i ], matrix[ length - j ][i], matrix[ length - j ][ length - i ] ] ) )


    return sum( max_numbers )