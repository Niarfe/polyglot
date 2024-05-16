default:
	@cat makefile | grep -E ".*:\s*#"

requirements:
	brew install coreutils # for shuf

read:           # read the vocab list as ordered
	cat vocab.txt | xargs bash showntell.sh

random:         # read the covab list in random order
	cat vocab.txt | shuf | xargs bash showntell.sh
