from hyperion.agent import Agent

def test_greet():
    agent = Agent(name="Test")
    assert agent.greet() == "Hello, I am Test!"
