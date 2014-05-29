img/%.rec: img/%.py
	@ttyrec -e "python $<" $@

img/%.gif: img/%.rec
	@ttygif $<
	@concat.sh $@
	@echo $(basename $<) | cut -d'-' -f2 | xargs -0 -I ! convert $@ -coalesce -repage 0x0 -crop !+0+0 +repage $@

gifs: $(addsuffix .gif, $(basename $(wildcard img/*.py)))

.PHONY: gifs
