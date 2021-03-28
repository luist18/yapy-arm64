.text
.global CountCommon
.type CountCommon, "function"

CountCommon:	MOV W9, #0

loop1:			CBZ W0, end
				LDR W10, [X1], #4
				SUB W0, W0, #1
				MOV W14, W2
				MOV X15, X3

loop2:			CBZ W14, loop1
				LDR W11, [X15], #4
				SUB W14, W14, #1
				CMP W10, W11
				b.NE loop2
				ADD W9, W9, #1
				b loop1

end:			MOV W0, W9
				ret
