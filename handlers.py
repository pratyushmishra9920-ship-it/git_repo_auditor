import os
from . import validation
from datetime import datetime

def history_handler(args, repo):
	
	print("-" * 80)
	print("                              COMMIT HISTORY")
	print("-" * 80)



	if not args.limit:
		commit = list(repo.iter_commits())
	else:
		commit = list(repo.iter_commits(max_count=args.limit))
	
	for i in range(len(commit)):
	
		current = commit[i]

		print("   Commit Hash: ", current.hexsha)
		print("   Message: ", current.message.strip())

		if i < (len(commit) - 1):
			
			previous = commit[i+1]
			
			diff = repo.git.diff(previous.hexsha, current.hexsha)

			for line in diff.splitlines():
				if line.startswith("+++") or line.startswith("---"):
					continue
				if line.startswith("+"):
					print("     Added: ", line[1:])
				elif line.startswith("-"):
					print("     Removed: ", line[1:])
			print()
		else:
			print()
			print("     Initial commit -  no previous commit to see changes")
			print()

	print("*" * 80)

def compare_handler(args, repo):
	
	print("-" * 80)
	print("                             BRANCH COMPARISON")
	print("-" * 80)



	branch_1 = validation.resolve_branch(repo, args.branch1)
	branch_2 = validation.resolve_branch(repo, args.branch2)	
	
	branch_1_commit = list(repo.iter_commits(branch_1))
	branch_2_commit = list(repo.iter_commits(branch_2))
	
	branch_1_hash = { commit.hexsha for commit in branch_1_commit }
	branch_2_hash = { commit.hexsha for commit in branch_2_commit }
	
	branch_1_only = branch_1_hash - branch_2_hash
	branch_2_only = branch_2_hash - branch_1_hash

	common = branch_1_hash & branch_2_hash 
	
	# branch 1 

	print(f"   {args.branch1} - only commit: ", len(branch_1_only))
	print()
	
	for commit in branch_1_commit:
		if commit.hexsha in branch_1_only:
			print("     hash: ", commit.hexsha)
			print("     message: ", commit.message.strip())
			print("     date: ", commit.committed_datetime)
			print("     author: ", commit.author)
			print()
	
	print("-" * 80)
 	
	# branch 2

	print(f"   {args.branch2} - only commit: ", len(branch_2_only))
	print()

	for commit in branch_2_commit:
		if commit.hexsha in branch_2_only:
			print("     hash: ", commit.hexsha)
			print("     message: ", commit.message.strip())
			print("     date: ", commit.committed_datetime)
			print("     author: ", commit.author)
			print()

	print("-" * 80)
	
	# Common
	print()
	print("   Common commits: ", len(common))
	print()

	print("*" * 80)
	
def stats_handler(args, repo):

	commit = list(repo.iter_commits())
	print()
	repo_name = os.path.basename(repo.remotes.origin.url)
	repo_name = repo_name.replace(".git", "")
	print("   Repository: ",repo_name)
	print()
	

	print("-" * 80)
	print("                         REPOSITORY STATISTICS")
	print("-" * 80)
	print()
	
	print("   Total Commits: ", len(commit))
	
	print()	

	bran = []
	for branch in repo.branches:
		bran.append(branch)
	print("   Local Branches: ", len(bran))
		
	print()	 
	
	remote_branches = []
	for ref in repo.remotes.origin.refs:
		remote_branches.append(ref.name)
	print("   Remote Branches: ", len(remote_branches))

	print()
	
	contributors = set()
	for commits in commit:
		contributors.add(commits.author.name)
	print("   Contributors: ", len(contributors))
	
	print()	

	size = 0
	for root, dirs, files in os.walk(repo.working_tree_dir):
		for filename in files:
			file_path = os.path.join(root, filename)
			size = size +  os.path.getsize(file_path)
	print("   Repository Size: ", size, "bytes")
	
	print()
		
	language_map = {
		# Python
		".py": "Python",
		
		# JavaScript / Web
		".js": "JavaScript",
		".jsx": "JavaScript",
		".ts": "TypeScript",
		".tsx": "TypeScript",

		# Web
		".html": "HTML",
		".htm": "HTML",
		".css": "CSS",
		".scss": "SCSS",
		".sass": "Sass",
		".less": "Less",

		# C / C++
		".c": "C",
		".h": "C/C++ Header",
		".cpp": "C++",
		".cc": "C++",
		".cxx": "C++",
		".hpp": "C++ Header",

		# Java / JVM
		".java": "Java",
		".kt": "Kotlin",
		".kts": "Kotlin",
		".scala": "Scala",

		# C#
		".cs": "C#",

		# Go
		".go": "Go",

		# Rust
		".rs": "Rust",

		# Ruby
		".rb": "Ruby",

		# PHP
		".php": "PHP",

		# Swift
		".swift": "Swift",

		# R
		".r": "R",

		# Dart
		".dart": "Dart",

		# Shell
		".sh": "Shell",
		".bash": "Bash",
		".zsh": "Zsh",
		".fish": "Fish",

		# Objective-C
		".m": "Objective-C",
		".mm": "Objective-C++",

		# Lua
		".lua": "Lua",

		# Perl
		".pl": "Perl",

		# Haskell
		".hs": "Haskell",

		# Elixir
		".ex": "Elixir",
		".exs": "Elixir",

		# Erlang
		".erl": "Erlang",

		# Julia
		".jl": "Julia",

		# MATLAB
		".m": "MATLAB",

		# SQL
		".sql": "SQL",

		# Markup / Documentation
		".md": "Markdown",
		".markdown": "Markdown",

		# Data / Configuration
		".json": "JSON",
		".yaml": "YAML",
		".yml": "YAML",
		".xml": "XML",

		# Docker
		".dockerfile": "Dockerfile",

		# Other
		".vue": "Vue",
		".svelte": "Svelte"
	}

	dict_language = {}
	for root, dirs, files in os.walk(repo.working_tree_dir):
		if ".git" in dirs:
			dirs.remove(".git")
		for filename in files:
			extension = os.path.splitext(filename)[1]
			language = language_map.get(extension)
			if language is None:
				continue
			if language in dict_language:
				dict_language[language] = dict_language[language] + 1
			else:
				dict_language[language] = 1

	print("   Languages: ")
	for language, count in dict_language.items():
		print(f"     {language}: {count}")

	print()
	

	print("-" * 80)
	print("   Repository Files: ")
	print("-" * 80)
	print()
	readme_path = os.path.join(repo.working_tree_dir, "README.md")
	if os.path.exists(readme_path):
		print("   README: Available")
	else:
		print("   README: Not Available")

	total_files = 0
	for root, dirs, files in os.walk(repo.working_tree_dir):
		for file in files:
			total_files = total_files + 1
	print("   Total Files: ", total_files)

	print()

	print("-" * 80)
	latest_commit = commit[0]
	print("   Latest commit: ")
	print("-" * 80)
	print()
	print("   Hash: ", latest_commit.hexsha)
	print("   Message: ", latest_commit.message.strip())
	print("   Author: ", latest_commit.author.name)
	print("   Date: ", latest_commit.committed_datetime)
	
	print()
	
	print("-" * 80)
	oldest_commit = commit[-1]
	print("   Oldest commit: ")
	print("-" * 80)
	print()
	print("   Hash: ", oldest_commit.hexsha)
	print("   Message: ", oldest_commit.message.strip())
	print("   Author: ", oldest_commit.author.name)
	print("   Date: ", oldest_commit.committed_datetime)	

	print()
	print("*" * 80)


def activity_handler(args, repo):

	print("-" * 80)
	print("                                 ACTIVITY")
	print("-" * 80)
	
	commits = list(repo.iter_commits())
	
	contributor_dict = {}
	for commit in commits:
		if commit.author.name in contributor_dict:
			contributor_dict[commit.author.name] = contributor_dict[commit.author.name] + 1
		else:
			contributor_dict[commit.author.name] = 1

	print()
	
	print("   CONTRIBUTOR ACTIVITY : ")
	print()   
	for name, count in contributor_dict.items():
		print(f"     {name}: {count}")
	
	print()
	print("     Most Active Contributor: ",max(contributor_dict, key=contributor_dict.get))
	print()
	

	time_dict = {}
	for commit in commits:
		date = datetime.fromtimestamp(commit.committed_date).date()
		if date in time_dict:
			time_dict[date] = time_dict[date] + 1
		else:
			time_dict[date] = 1
	
	print("   COMMIT ACTIVITY : ")
	print()
	for time, occur in time_dict.items():
		print(f"     {time}: {occur}")
	print()
	
	max_date = max(time_dict, key=time_dict.get)
	max_month = max_date.strftime("%B %Y")
	print("     Most Active Month: ", max_month)
	
	print()


	print("*" * 80)

def health_handler(args, repo):
	
	commit = list(repo.iter_commits())	

	print("-" * 80)
	print("                                    HEALTH")
	print("-" * 80)
	print()

	pass_count = 0

	files_name = []
	for root, dirs, files in os.walk(repo.working_tree_dir):
		for filename in files:
			files_name.append(filename)
	try:
		if repo:
			print("   ✓ GIT REPOSITORY: PASS")
			pass_count = pass_count + 1
		else:
			print("    GIT REPOSITORY: WARNING")	
	except:
		print("   not a git repository")
	

	try:
		if "README.md" in files_name:
			print("   ✓ README: PASS")
			pass_count = pass_count + 1
		else:
			print("    README: WARNING")
	except:
		print("   README file does not exist")

	try:
		if ".gitignore" in files_name:
			print("   ✓ .gitignore: PASS")
			pass_count = pass_count + 1
		else:
			print("    .gitignore: WARNING")
	except:
		print("   .gitignore file does not exist")

	try:
		if "LICENSE" in files_name:
			print("   ✓ LICENSE: PASS")
			pass_count = pass_count + 1
		else:
			print("⚠   LICENSE: WARNING")
	except:
		print("   LICENSE file does not exist")
	

	contributors = set()
	for commits in commit:
		contributors.add(commits.author.name)
	
	try:		
		if len(contributors) > 0:
			print("   ✓ Contributors: PASS")
			pass_count = pass_count + 1
		else:
			print("    Contributors: WARNING")
	except:
		print("   contributors does not exist")

	bran = []
	for branch in repo.branches:
		bran.append(branch)
	
	try:	
		if len(bran) > 0:
			print("   ✓ Branches: PASS")
			pass_count = pass_count + 1
		else:
			print("    Branches: WARNING")
	except:
		print("branches does not exist")
	
	try:
		if len(commit) > 0:
			print("   ✓ Commits: PASS")
			pass_count = pass_count + 1
		else:
			print("    Commits: WARNING")
	except:
		print("   commits does not exist")
	print()
	
	print("-" * 80)
	print("                                OVERALL HEALTH")
	print("-" * 80)
	print()
	
	print(f"            {pass_count} / 7 CHECKS PASSED")
	
	print()

	percentage = round((pass_count / 7) * 100, 2)
	print(f"            {percentage}")
	
	print()
	
	if 90 < percentage <= 100:
		print("            EXCELLENT")
	elif 75 < percentage <= 90:
		print("            GOOD")
	elif 50 <= percentage <= 75:
		print("            NEEDS ATTENTION")
	elif percentage < 50:
		print("            POOR")
	

	print()
	print("*" * 80)
