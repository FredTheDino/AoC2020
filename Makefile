ifneq ($(HY),)
	LANG=hy
	INRP=hy
else
	LANG=py
	INRP=pypy3
endif
FILES=$(wildcard $(LANG)*.$(LANG))
INPUT=$(patsubst $(LANG)%.$(LANG),input%.txt,$(FILES))
DAYS=$(patsubst $(LANG)%.$(LANG),%,$(FILES))

.PHONY: INPUT all

all: $(DAYS) FORCE

%: $(LANG)%.$(LANG) FORCE
	@ echo 
	@ echo == $< ==
	@ time $(INRP) $< < input$@.txt

FORCE:
