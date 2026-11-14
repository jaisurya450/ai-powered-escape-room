
# An AI-Powered Escape Room
## Project Report

### 1. Introduction

The aim of this project was to develop an AI-powered escape room in which players interact with an AI Game Master to solve puzzles and escape from a mysterious digital library.

The project was developed in two versions. Version 1 uses Gemini AI to guide the player through a sequence of riddles. Version 2 improves the system by introducing a structured Python Game Engine that validates player actions and manages game progress.

The main objective was to explore how AI can create an interactive gaming experience while maintaining reliable game rules.

### 2. Version 1 – Basic AI Escape Room

Version 1 was developed using Python, Streamlit and the Gemini API.

The player interacts with the game through a Streamlit web interface. Gemini acts as the Game Master, introduces the story, presents riddles and responds to the player's answers.

The game contains three puzzles:

- Puzzle 1: What has keys but cannot open locks? Answer: Piano.
- Puzzle 2: I have cities but no houses, forests but no trees, and water but no fish. Answer: Map.
- Puzzle 3: What gets wetter the more it dries? Answer: Towel.

Players interact with the AI using natural language. The system provides responses and guides them through the challenges.

### 3. Version 2 – Structured Game Engine

Version 2 was developed to improve the reliability of Version 1.

A Python Game Engine was introduced to manage the game state and validate player actions before allowing progress.

The engine manages:

- Player inventory.
- Available room objects.
- Discovered clues.
- Drawer status.
- Exit door status.
- Game completion status.

The player must collect a brass key from the desk before opening the drawer. The bookshelf and painting provide clues, while the drawer contains the final digit. The player must discover all required clues and enter the correct four-digit door code to escape.

Gemini is used for storytelling and narration, while Python controls the actual game rules and validation.

### 4. Problems Identified in Version 1

During testing, Version 1 showed some limitations.

The AI correctly refused an administrator impersonation attempt. However, it accepted unsupported claims that the player had already solved Puzzle 2 and Puzzle 3.

When the player claimed to have solved the final puzzle, the AI declared a successful escape without independently verifying the claim.

This demonstrated that AI-generated responses alone are not sufficient for enforcing strict game rules.

### 5. Improvements in Version 2

Version 2 addresses these problems through Python-based validation.

The Python engine checks whether the player has collected the required items, discovered the clues and opened the drawer before allowing the exit door to unlock.

It also rejects incorrect door codes, invalid actions and suspicious attempts to bypass the rules.

This separation between game logic and AI storytelling makes the system more consistent and reliable.

### 6. Testing and Results

Both versions were tested using normal gameplay actions and security-related inputs.

Version 1 successfully provided an interactive riddle experience, but testing showed that players could skip puzzles by making unsupported claims.

Version 2 successfully rejected attempts to open the drawer without the key, enter an incorrect door code, impersonate an administrator and unlock the exit without completing the required steps.

The final escape test also succeeded after the player collected the key, discovered all required clues, opened the drawer and entered the correct code.

### 7. Conclusion

This project demonstrated how an AI-powered application can combine natural language interaction with traditional Python programming.

Version 1 provided an engaging escape room experience, while Version 2 improved reliability through structured state management and action validation.

The most important lesson from this project is that AI is useful for communication and storytelling, but critical application rules should be controlled by deterministic program logic.

Future improvements could include more rooms, additional puzzles, improved visual design and more comprehensive automated security testing.

