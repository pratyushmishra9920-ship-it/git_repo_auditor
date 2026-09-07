from git import Repo
import tempfile
from . import handlers, parsers
from git.exc import GitCommandError, InvalidGitRepositoryError


def main():
	print("*" * 80)
	print("                               GIT REPO AUDITOR")
	print("*" * 80)
	print()
	
	parser = parsers.create_parser()

	args = parser.parse_args()

	if args.repo:
		
		try:
			repo_path = tempfile.mkdtemp()
			Repo.clone_from(args.repo, repo_path)
			repo = Repo(repo_path)

		except GitCommandError as e:
			parser.error(f"failed to clone: {e}")
	else:

		try:
			repo = Repo(".")

		except InvalidGitRepositoryError as e:
			parser.error(f"current directory is not git directory: {e}")
	

	args.func(args, repo)

		



if __name__ == "__main__":
	main()



