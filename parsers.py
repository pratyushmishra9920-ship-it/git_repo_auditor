import argparse
from . import handlers


def create_parser():

	parsers = argparse.ArgumentParser(description="Analyze Git repositories from the command line.")

	parsers.add_argument(
			"--repo",
			help="repository URL to analyze"
	)

	subparsers = parsers.add_subparsers(dest="command")
	

	history_parser = subparsers.add_parser(
			"history",
			help="show commit history",
			description="Show the commit history of the repository."
	)
	history_parser.add_argument(
			"--limit",
			type=int,
			help="number of commits to show"
	)
	history_parser.set_defaults(func=handlers.history_handler)
	
	compare_parser = subparsers.add_parser(
			"compare",
			help="compare two branches",
			description="Compare two branches of the repository."
	)
	compare_parser.add_argument(
			"branch1",
			help="first branch name"
	)
	compare_parser.add_argument(
			"branch2",
			help="second branch name"
	)
	compare_parser.set_defaults(func=handlers.compare_handler)
	

	stats_parser = subparsers.add_parser(
			"stats",
			help="show repository statistics",
			description="Show statistics about the repository."
	)
	stats_parser.set_defaults(func=handlers.stats_handler)
	

	parsers.add_argument(
			"--format",
			choices=["json", "text"],
			help="format of output"
	)



	return parsers 
