# Assignment - 4 DASS

### Yash Shivhare - 2021101105

Write unit tests for the codebase provided for assignment 3. The objective of unit testing is to observe how smaller chunks of code function in isolation to
ensure that they meet the expectations set for them. These expectations are not only in terms of
the correctness of the value that is output, but also things such as the type of the output, the fine
grained structure of the output, and the states of any external variables being modified by the
code.

### Testing Movement of King : king.move()

Made a class TestKing(unittest.TestCase) for checking functionality.

List of functions implemented:

- **testUp()**: test that **up** movement of king is functioning properly
- **testDown()**: test that **down** movement of king is functioning properly
- **testRight()**: test that **right** movement of king is functioning properly
- **testLeft()**: test that **left** movement of king is functioning properly
- **I have seen within each of them king’s speed is greater than equal to 0(in case of zero no movt. should occur)**
- **I have checked condition if the king was dead even before spawned(HERO_POS==(0,0))(released dead body :D) and checked that it won't move in such case.Hence the answer true**
- **I have also checked condition if the king was dead anytime(HERO_POS==-1)(including right after spawning) and checked that it won't move in such case as well.Hence the answer true**

### BONUS:
### Testing Attack of King : king.attack_target()

- Made a class TestAttack(unittest.TestCase) for checking functionality.

List of functions implemented:
- **testAttack()**: test that damage given by king = damage taken by cannon
- **testDead()**: test that if king is dead no damge should be dealt
- **testDestroy()**: test that if damage given by king > the maximum health of cannon then it should be destroyed