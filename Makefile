LANG=hy
FILES=$(wildcard day*.$(LANG))
INPUT=$(patsubst day%.$(LANG),input%.txt,$(FILES))

.PHONY: INPUT

all: $(INPUT)

input%.txt: day%.$(LANG)
	@ echo 
	@ echo == $< ==
	@ time $(LANG) $< < $@
	@ touch $@
