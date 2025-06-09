import argparse
from .agent import Agent


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run Hyperion coding agent")
    parser.add_argument("--name", default="Hyperion", help="Name of the agent")
    args = parser.parse_args(argv)

    agent = Agent(name=args.name)
    print(agent.greet())


if __name__ == "__main__":
    main()
