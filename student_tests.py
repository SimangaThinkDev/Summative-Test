import unittest
from assessment import *

class StudentTests(unittest.TestCase):

    def test_validate_user_credentials(self) -> None :

         self.assertEqual( validate_user_credentials( "Fentse123", "lock!pass" ), (True, any) )
         self.assertEqual( validate_user_credentials( "Mpho1060", "lock!" ), (True, any) )
         self.assertEqual( validate_user_credentials( "Smanga11", "lock!pass" ), (True, any) )


    def test_extract_hashtags(self) -> None:
         
        text1 = "#Python #python some text #fire"
        text2 = ""
        text3 = "##Invalid #Valid some text to check"

        self.assertEqual( extract_hashtags( text1 ), ["python", "fire"] )
        self.assertEqual( extract_hashtags( text2 ), [] )
        self.assertEqual( extract_hashtags( text3 ), ["valid"] )

    
    def test_find_matrix_saddle_points( self ) -> None:

        matrix1 = [
            [1, 2],
            [3, 4],
        ]

        self.assertEqual( find_matrix_saddle_points( matrix1 ), [(1, 0)] )

        matrix2 = [
            [7, 8, 9],
            [13, 5, 7],
            [1, 9, 10],
        ]

        self.assertEqual( find_matrix_saddle_points( matrix2 ), () )

        matrix3 = [
            [120, 3, 51],
            [34, 16, 28],
            [101, 2, 200],
        ]

        self.assertEqual( find_matrix_saddle_points( matrix3 ), ( [1, 1] ) )


    def test_tic_tac_toe_winner(self) -> None:

        board1 = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.assertEqual( tic_tac_toe_winner( board1 ), None )
        
        # Test Diagonal X win
        board2 = [
            ["O", "", "X"],
            ["O", "X", "O"],
            ["X", "", ""]
        ]
        self.assertEqual( tic_tac_toe_winner( board2 ), "X" )


        # Test Horizontal O win
        board3 = [
            ["", "", "X"],
            ["", "X", "X"],
            ["O", "O", "O"]
        ]
        self.assertEqual( tic_tac_toe_winner( board3 ), "O" )


        # Test vertical O win
        board4 = [
            ["X", "X", "O"],
            ["", "X", "O"],
            ["", "", "O"]
        ]
        self.assertEqual( tic_tac_toe_winner( board4 , "O") )


    def test_analyze_stock_prices(self) -> None:

        market1 = [ 22, 22.4, 23.12, 21, 17.99, 25.60, 27, 22 ]
        self.assertEqual( analyze_stock_prices( market1 ), ( 4, 7 ) ) # 7 Not inclusive
        
        market2 = [ 100, 100.5, 98.99, 110, 115.30, 113, 117, 122.30, 140, 133.40, 130.98, 128.12 ]
        self.assertEqual( analyze_stock_prices( market2 ), ( 5, 9 ) ) # 9 Not inclusive
        
        market3 = [  ]
        self.assertEqual( analyze_stock_prices( market3 ), ( None, None ) ) # as per the question


if __name__ == "__main__":
    unittest.main( verbosity=2 )