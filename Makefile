all: screen print

screen:
	context --pdf --automp --mode=screen --result=cipher-s cipher.tex

# book:
# 	context --pdf --automp --mode=book --result=cipher-b cipher.tex

print:
	context --pdf --automp --mode=print --result=cipher-p cipher.tex

clean:
	context --purge

cleanall:
	context --purgeall --purgeresult
	rm -rf cipher-s.pdf cipher-p.pdf

.PHONY: clean cleanall screen print