.text
.global CountCommon
.type CountCommon,"function"

CountCommon:	mov W4, #0
				mov W7, W2
				mov X9, X3
CICLO1:			cbz W0, FIM
				ldr W5, [X1], #4
				sub W0, W0, #1
CICLO2:			cbz W2, RESET
				ldr W6, [X3], #4
				sub W2, W2, #1
				cmp W5, W6
				b.EQ FOUND
				b CICLO2
FOUND:			add W4, W4, #1
RESET:			mov W2, W7
				mov X3, X9
				b CICLO1
FIM:			mov W0, W4
				ret
