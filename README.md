# Summative-Test Practice
## Author: Simangaliso Innocent Phakwe

## Your Mission, Should You Choose to Accept It...
Welcome, code warrior, to **Python SkillForge: Module 2**! This isn't just an assessment; it's a gauntlet designed to hone your Python skills, pushing you to think critically and embrace the robust practice of **Test-Driven Development (TDD)**. You'll be breathing life into dormant functions within `assessment.py`, and your mastery will be measured by whether your code stands up to the ultimate judge: the unit tests.

## What Awaits Your Mastery
Conquering this module means you'll solidify your command over:
* **Function Crafting:** Building elegant and purposeful Python functions.
* **Iterative Power:** Slicing and dicing data with 1D and 2D loops.
* **Logic Orchestration:** Directing your code's flow with precision using `if`, `elif`, and `else`.
* **Data Structures Demystified:** Navigating lists (including multi-dimensional matrices) and dictionaries like a pro.
* **Algorithmic Acumen:** Designing efficient solutions to diverse programming challenges.
* **String Sorcery:** Manipulating text with finesse, from parsing to transforming.
* **TDD Philosophy:** Adopting the powerful workflow of writing tests *before* writing code.

---

## Your Arsenal
* `assessment.py`: This is your primary workspace. All the functions you need to complete are here, waiting for your touch.
* `tests/`: A fortified vault containing pre-written unit tests for a specific set of functions. **Do not modify anything within this directory.**
* `README.md`: Your detailed tactical brief for this mission.

---

## The TDD Playbook: Two Engagements

This challenge features two distinct phases of TDD. For the **first five functions** (`validate_user_credentials`, `extract_hashtags`, `find_matrix_saddle_points`, `tic_tac_toe_winner`, `analyze_stock_prices`), you'll be on the offensive, crafting your own unit tests from scratch. This is your chance to truly understand the "Red" in the Red-Green-Refactor cycle.

For the **subsequent five functions** (`count_nested_keys`, `generate_collatz_sequence`, `validate_sudoku_board`, `find_anagrams`, `calculate_network_latency`), we've deployed pre-built tests in the `tests/` directory to guide your development.

### Your Strategy:

1.  **Secure Your Base:**
    * Begin by **forking this repository** to your personal GitHub account. This creates your private training ground.

2.  **Intel Gathering (Read the Blueprints):**
    * Open `assessment.py` and deeply absorb the **docstring** for the function you're targeting. It's your prime source of information on its purpose, arguments, and expected returns.
    * **For functions with provided tests (the last five):** Take a reconnaissance mission into the relevant file within the `tests/` directory (e.g., `test_count_nested_keys.py`). Observe the inputs and the `assertEqual` statements to grasp the evaluation criteria.

3.  **Phase 1: Forge Your Own Tests (Functions 1-5)**
    * Before you even think about implementing the function, envision how it should behave. What are the edge cases? What inputs should trigger specific outputs?
    * Create your unit tests directly in the **root directory** of your project (e.g., `my_tests.py` or `test_credential_validation.py`). These initial tests *must* fail – this is your deliberate "Red" state.
    * Execute your custom tests from the root: `python -m unittest my_tests.py` (adjust the filename as needed). Witness the glorious failures!

4.  **Phase 2: Utilize Provided Tests (Functions 6-10)**
    * For these functions, execute the supplied tests *before* writing a single line of function code: `python -m unittest tests/test_your_function_name.py` (swap `test_your_function_name.py` for the correct file). Expect to see failures – it's all part of the "Red" ritual.

5.  **Code the Breakthrough (Achieve Green!):**
    * Return to `assessment.py`.
    * Implement the function, focusing on writing the *minimum* amount of code necessary to make your failing test (or the provided one) pass.
    * Re-run your tests: `python -m unittest` followed by your test file or the relevant file in the `tests/` directory.
    * When the tests pass, you've achieved "Green" status! Celebrate this small victory.

6.  **Refine and Optimize (Refactor):**
    * (An optional, but highly recommended, strategic maneuver) Once green, review your code. Can it be more elegant, efficient, or readable without altering its functionality? This is your "Refactor" phase. After making improvements, rerun your tests to ensure you haven't introduced any regressions.

7.  **Repeat the Cycle:**
    * Move to the next challenge or the next failing test and repeat the TDD cycle.

### Interpreting Your Results:
* **OK:** All tests have been vanquished! Your code is robust.
* **FAILURES/ERRORS:** The `unittest` framework will provide detailed feedback on which tests didn't pass and why. Use this intel to pinpoint and debug the issues within your `assessment.py` functions.

Ready to sculpt your Python skills? Let the forging begin!
