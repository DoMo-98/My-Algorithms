import re

def math_func_parse( func, variables_map ):
    """
    Parse a math function string and return the result.
    """

    # Check for valid function string
    if not re.match( r'^[a-zA-Z0-9_]+$', func ):
        raise Exception( 'Invalid function string: ' + func )
    
    for i in variables_map:
        if i in func:
            func = func.replace( i, str( variables_map[ i ] ) )
    func.replace( ' ', '' )

    str_num = ""
    nums = []
    operations = []

    for i in func:
        if i.isnumeric():
            str_num += i
        else:
            if str_num != "":
                nums.append( int( str_num ) )
                str_num = ""
            operations.append( i )
    
    # TODO
            