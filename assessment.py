# import here

def validate_user_credentials(username: str, password: str) -> tuple[bool, str]:
    """
    Validate user credentials against specific rules.
    
    Rules:
    - Username must be 5-15 characters, alphanumeric only
    - Password must be 8-20 characters, containing at least one digit and one special character
    
    Args:
        username (str): The username to validate
        password (str): The password to validate
        
    Returns:
        tuple: (bool, str) where bool indicates validity and str contains error message if invalid
    """
    pass


def extract_hashtags(text: str) -> list[str] :
    """
    Extract all unique hashtags from a text string, sorted alphabetically.
    
    A hashtag starts with #, contains no spaces, and is case-insensitive
    (treat #Python and #python as the same tag).
    
    Args:
        text (str): The input text to scan for hashtags
        
    Returns:
        list: Sorted list of unique hashtags in lowercase
    """
    pass


def find_matrix_saddle_points(matrix: list[list[ int ]]) -> list[tuple[int, int]]:
    """
    Find all saddle points in a 2D matrix.
    
    A saddle point is an element that is the minimum in its row and maximum in its column.
    
    Args:
        matrix (list of lists): A 2D matrix of numbers
        
    Returns:
        list: List of tuples (row_index, col_index) for each saddle point
    """
    pass


def tic_tac_toe_winner(board: list[list[str]]) -> str :
    """
    Determine the winner of a tic-tac-toe game.
    
    Args:
        board (list of lists): 3x3 board with 'X', 'O', or '' (empty)
        
    Returns:
        str: 'X', 'O' for winner, 'Draw' for full board with no winner, 
             or None for game not finished
    """
    pass


def analyze_stock_prices(prices: list[float]) -> tuple[int, int] :
    """
    Analyze daily stock prices to find the best day to buy and sell.
    
    Args:
        prices (list): List of daily prices (floats) in chronological order
        
    Returns:
        tuple: (buy_day_index, sell_day_index) for maximum profit.
               Returns (None, None) if no profitable trade possible.
    """
    pass


def count_nested_keys(data: dict) -> int:
    """
    Count all keys in a nested dictionary structure at all levels.
    
    Args:
        data (dict): A potentially nested dictionary structure
        
    Returns:
        int: Total count of all keys at all nesting levels
    """
    pass


def generate_collatz_sequence(start: int) -> list[int]:
    """
    Generate the Collatz sequence from a starting number until it reaches 1.
    
    Rules:
    - If number is even: divide by 2
    - If odd: multiply by 3 and add 1
    
    Args:
        start (int): Positive integer to start the sequence
        
    Returns:
        list: The complete sequence including the starting number and ending at 1
    """
    pass


def validate_sudoku_board(board: list[list[int]]) -> bool:
    """
    Validate a 9x9 Sudoku board according to standard rules.
    
    Args:
        board (list of lists): 9x9 grid with numbers 1-9 or 0 for empty
        
    Returns:
        bool: True if board is valid (no duplicates in rows, columns, or 3x3 boxes)
    """
    pass


def find_anagrams(word: str, word_list: list[str]) -> list[str]:
    """
    Find all anagrams of a given word in a list of words.
    
    Args:
        word (str): The target word to find anagrams for
        word_list (list): List of candidate words
        
    Returns:
        list: All words from word_list that are anagrams of the input word
    """
    pass


def calculate_network_latency(routers: list[str], connections: list[tuple[str, str, int]]) -> int:
    """
    Calculate maximum network latency between any two routers in a network.
    
    Args:
        routers (list): List of router identifiers
        connections (list of tuples): Pairs (router1, router2, latency)
        
    Returns:
        int: Maximum latency between any two connected routers
             Returns -1 if network is disconnected
    """
    pass


if __name__ == "__main__":
    # Don't believe in Unittests
    # Test your code here...
    pass