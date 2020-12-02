ifneq ($(PYTHON),)
	LANG=py
	INRP=python3
else
	LANG=hy
	INRP=hy
endif
FILES=$(wildcard day*.$(LANG))
INPUT=$(patsubst day%.$(LANG),input%.txt,$(FILES))

.PHONY: INPUT

all: $(INPUT)

input%.txt: day%.$(LANG) FORCE
	@ echo 
	@ echo == $< ==
	@ time $(INRP) $< < $@
	@ touch $@

FORCE:
