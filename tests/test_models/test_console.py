import unittest
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
# test case units for methods within the custom console
    def test_prompt(self):
        """Test custom prompt."""
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_do_quit(self):
        """Test quit command."""
        interpreter = HBNBCommand()
        self.assertTrue(interpreter.do_quit(""))

    def test_do_EOF(self):
        """Test EOF handling."""
        interpreter = HBNBCommand()
        self.assertTrue(interpreter.do_EOF(""))

    def test_emptyline(self):
        """Test line behavior."""
        interpreter = HBNBCommand()
        # No assertion needed, emptyline should do nothing
        interpreter.emptyline()


if __name__ == "__main__":
    unittest.main()
