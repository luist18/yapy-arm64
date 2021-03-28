.text
.global CountCommon
.type CountCommon, "function"

CountCommon:	MOV		W9, #0

CICLO1:			CBZ		W2, FIM
				SUB 	W2, W2, #1
				LDR		W5, [X3]
				ADD		X3, X3, #4

				MOV		W7, W0
				MOV		X10, X1

CICLO2:			CBZ		W7,	CICLO1
				SUB		W7, W7, #1
				LDR		W6,	[X10]
				ADD		X10, X10, #4

				CMP		W6, W5
				B.EQ	INCREMENT
				B		CICLO2

INCREMENT:		ADD		W9, W9, #1
				B		CICLO2

FIM:			MOV		W0, W9
				RET
