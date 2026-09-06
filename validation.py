
def resolve_branch(repo, branch_name):
	
	for branch in repo.branches:
		
		if branch.name == branch_name:
			return branch_name
		
	else:
		remote_branch  = f"origin/{branch_name}"
		
		for ref in repo.remotes.origin.refs:
			if ref.name == remote_branch:
				return remote_branch
		raise ValueError("branch is not found")
				
	
