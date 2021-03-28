.text
.global CountCommon
.type CountCommon, "function"

CountCommon:	MOV 	W4, 0
				MOV     X20, X3
				MOV		W7, W2
				CBZ 	W2, end

loop:			LDR 	W5, [X1]
				LDR 	W6, [X3]
			    CBZ		W0, end

loop1: 			CBZ 	W7, loop2
				SUB		W7, W7, 1
				CMP		W5, W6
				ADD 	X3, X3, 4
				B.EQ 	loop3
				b		loop

loop2:			SUB 	W0, W0, 1
				ADD		X1, X1, 4
				MOV 	X3, X20
				MOV 	W7, W2
				b		loop

loop3:			ADD 	W4, W4, 1
				b       loop2

end:			MOV 	W0, W4
				RET



