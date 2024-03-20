import unittest
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def test_prompt(self):
        """Test the custom prompt."""
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_do_quit(self):
        """Test the quit command."""
        interpreter = HBNBCommand()
        self.assertTrue(interpreter.do_quit(""))

    def test_do_EOF(self):
        """Test the EOF handling."""
        interpreter = HBNBCommand()
        self.assertTrue(interpreter.do_EOF(""))

    def test_emptyline(self):
        """Test empty line behavior."""
        interpreter = HBNBCommand()
        # No assertion needed, emptyline should do nothing
        interpreter.emptyline()


if __name__ == "__main__":
    unittest.main()
