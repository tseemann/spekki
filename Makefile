
all: clean dev

dev:
	pip3 install --user -e .

clean:
	find . -name "*~" -print -delete
	
	
