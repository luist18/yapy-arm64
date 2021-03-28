.text
.global CountCommon
.type CountCommon, "function"

CountCommon:	mov W12, 0
				b CICLOA

CICLOA:			cbz W0, FINAL
				sub W0, W0, 1
				add X1, X1, 4
				mov X4, X3
				mov W5, W2
				b CICLOB

CICLOB:			cbz W5, CICLOA
				sub W5, W5, 1
				add X4, X4, 4
				b COMPARACAO

COMPARACAO:		ldr W11, [X1]
				ldr W10, [X4]
				cmp W11, W10
				b.eq CONTADOR
				b CICLOB

CONTADOR:		add W12, W12, 1
				b CICLOB

FINAL:			mov W0, W12
				ret
