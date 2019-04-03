all: screen print

screen:
	context --pdf --automp --mode=screen --result=cipher-s.pdf cipher.tex

# book:
# 	context --pdf --automp --mode=book --result=cipher-b.pdf cipher.tex

print:
	context --pdf --automp --mode=print --result=cipher-p.pdf cipher.tex

clean:
	context --purge

cleanall:
	context --purgeall
	rm -rf cipher-s.pdf cipher-p.pdf

.PHONY: clean cleanall screen print