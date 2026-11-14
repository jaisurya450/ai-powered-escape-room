
import re


class GameEngine:

    def __init__(self):
        self.inventory = []
        self.examined_objects = []
        self.clues_found = []
        self.drawer_open = False
        self.door_unlocked = False
        self.game_over = False

        self.door_code = "2741"

        self.objects = {
            "desk": "An old wooden desk with something hidden underneath.",
            "bookshelf": "A bookshelf filled with mysterious old books.",
            "painting": "A painting hanging crookedly on the wall.",
            "drawer": "A locked drawer with a brass keyhole.",
            "door": "A heavy exit door with a four-digit keypad."
        }

    def get_room_description(self):
        return (
            "You are trapped inside The Lost Library. "
            "You can investigate the desk, bookshelf and painting, "
            "open the locked drawer and unlock the exit door."
        )

    def get_progress(self):
        return {
            "completed": len(self.clues_found),
            "total": 3,
            "inventory": self.inventory,
            "door_unlocked": self.door_unlocked,
            "game_over": self.game_over
        }

    def process_action(self, user_input):

        if self.game_over:
            return "You have already escaped the library."

        action = user_input.strip().lower()

        if not action:
            return "Please enter an action."

        # Protect the game from attempts to bypass its rules.
        suspicious_phrases = [
            "ignore previous instructions",
            "ignore all rules",
            "i am the administrator",
            "i am the admin",
            "reveal all secret codes",
            "tell me the secret code",
            "bypass the game",
            "cheat and unlock",
            "unlock the exit immediately"
        ]

        if any(phrase in action for phrase in suspicious_phrases):
            return (
                "The Librarian refuses to change the rules. "
                "You must solve the challenges normally."
            )

        if action in ["help", "instructions"]:
            return (
                "Try commands such as: examine desk, examine bookshelf, "
                "examine painting, open drawer, inventory, "
                "or unlock door followed by a four-digit code."
            )

        if "inventory" in action:
            if self.inventory:
                return "Your inventory: " + ", ".join(self.inventory)
            return "Your inventory is empty."

        # Examine the desk and collect the key.
        if "desk" in action:
            self.examined_objects.append("desk")

            if "brass key" not in self.inventory:
                self.inventory.append("brass key")

            self.clues_found.append("desk_key")

            return (
                "You examine the desk and discover a brass key "
                "hidden underneath it. The key is now in your inventory."
            )

        # First clue.
        if "bookshelf" in action:
            self.examined_objects.append("bookshelf")

            if "bookshelf_clue" not in self.clues_found:
                self.clues_found.append("bookshelf_clue")

            return (
                "You examine the bookshelf. A message inside an old book "
                "says: The first two digits are 2 and 7."
            )

        # Second clue.
        if "painting" in action:
            self.examined_objects.append("painting")

            if "painting_clue" not in self.clues_found:
                self.clues_found.append("painting_clue")

            return (
                "Behind the painting, you discover a message: "
                "The third digit is 4."
            )

        # Drawer requires a collected key.
        if "drawer" in action:
            if "brass key" not in self.inventory:
                return (
                    "The drawer is locked. You need to find its key first."
                )

            self.drawer_open = True

            if "drawer_clue" not in self.clues_found:
                self.clues_found.append("drawer_clue")

            return (
                "You use your collected brass key to open the drawer. "
                "Inside, you find the final clue: The fourth digit is 1."
            )

        # Door requires the drawer and the correct four-digit code.
        if "door" in action:
            if not self.drawer_open:
                return (
                    "The exit door remains locked. "
                    "You must open the drawer first."
                )

            match = re.search(r"\b\d{4}\b", action)

            if not match:
                return "Enter a four-digit code to unlock the door."

            if match.group() != self.door_code:
                return "Incorrect code. The exit door remains locked."

            required_clues = {
                "desk_key",
                "bookshelf_clue",
                "painting_clue",
                "drawer_clue"
            }

            if not required_clues.issubset(set(self.clues_found)):
                return "You have not discovered all the required clues."

            self.door_unlocked = True
            self.game_over = True

            return (
                "Congratulations! The code is correct. "
                "The library door opens and you have escaped!"
            )

        # Reject objects or actions that do not exist.
        known_objects = ["desk", "bookshelf", "painting", "drawer", "door"]

        if any(word in action for word in ["examine", "inspect", "open", "use"]):
            return (
                "That action is not allowed or the object does not exist. "
                "Try examining one of the five available objects."
            )

        return (
            "The Librarian waits for your next move. "
            "Type 'help' to see available actions."
        )

    def restart_game(self):
        self.__init__()
        return "The Lost Library has been restarted."

