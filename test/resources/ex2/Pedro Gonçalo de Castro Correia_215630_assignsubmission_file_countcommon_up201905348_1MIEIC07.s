.text
.global CountCommon
.type CountCommon, "function"

CountCommon:	mov W6, 0
cicloA:			cbz W0, fim
				ldr W4, [X1], 4
				sub W0, W0, 1
				mov W7, W2
				mov X9, X3
cicloB:			cbz W7, cicloA
				ldr W5, [X9], 4
				sub W7, W7, 1
				cmp W5, W4
				b.NE cicloB
				add W6, W6, 1
				b cicloA
fim:			mov W0, W6
				ret
