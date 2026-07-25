"""Test suite for Manus Autonomous Web Agent solution."""
import unittest
from manus_autonomous_web_agent import ManusAutonomousWebAgent

class TestManusAutonomousWebAgent(unittest.TestCase):

    def test_web_goal_execution(self):
        agent = ManusAutonomousWebAgent()
        res = agent.execute_web_goal("Search market data", "https://example.com")
        
        self.assertEqual(res["status"], "MANUS_GOAL_ACHIEVED")
        self.assertEqual(res["actions_executed"], 3)

if __name__ == "__main__":
    unittest.main()
