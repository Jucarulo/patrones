# Token for working on github (replace yours here given are placeholder)

import os
print(os.path.dirname(os.path.realpath(__file__)))
this_dir = os.path.dirname(os.path.realpath(__file__))

GIT_KEY="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"

with open(this_dir + "/repo_keys.txt") as f:
	for line in f:
		tups=line.strip().split("=")
		if tups[0] == "GIT_KEY":
			GIT_KEY=tups[1]
