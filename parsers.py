import argparse
from . import handlers


def create_parser():

	parsers = argparse.ArgumentParser(description="Analyze Git repositories from the command line.")

	parsers.add_argument(
			"--repo",
			help="Repository URL or local path to analyze"
	)

	subparsers = parsers.add_subparsers(dest="command")
	

	history_parser = subparsers.add_parser(
			"history",
			help="Display commit history",
			description="Show the commit history of the repository."
	)
	history_parser.add_argument(
			"--limit",
			type=int,
			help="Maximum number of commits to display"
	)
	history_parser.set_defaults(func=handlers.history_handler)
	
	compare_parser = subparsers.add_parser(
			"compare",
			help="Compare two branches",
			description="Compare two branches of the repository."
	)
	compare_parser.add_argument(
			"branch1",
			help="First branch to compare"
	)
	compare_parser.add_argument(
			"branch2",
			help="Second branch to compare"
	)
	compare_parser.set_defaults(func=handlers.compare_handler)
	
	activity_parser = subparsers.add_parser(
			"activity",
			help="Analyze contributor and commit activity",
			description="Analyze contributor and commit activity."
	)
	activity_parser.set_defaults(func=handlers.activity_handler)

	health_parser = subparsers.add_parser(
			"health",
			help="Check repository health",
			description="Check the health of the repository."
	)
	health_parser.set_defaults(func=handlers.health_handler)
	
	stats_parser = subparsers.add_parser(
			"stats",
			help="Display repository statistics",
			description="Show statistics about the repository."
	)
	stats_parser.set_defaults(func=handlers.stats_handler)
	


	return parsers 
