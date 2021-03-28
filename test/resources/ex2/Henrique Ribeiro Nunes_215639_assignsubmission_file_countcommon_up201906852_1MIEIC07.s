.text
.global CountCommon
.type CountCommon, "function"

CountCommon:	MOV 	W4, #0
				MOV 	X9, X3
CICLO:			CBZ		W0, FIM
				SUB 	W0, W0, #1
				MOV 	W7, W2
				LDR		W5, [X1]
SUBCICLO:		CBZ		W7, CONT
				SUB		W7, W7, #1
				LDR		W6, [X3]
				ADD		X3, X3, #4
				CMP		W6, W5
				B.NE	SUBCICLO
				ADD		W4, W4, #1
CONT:			MOV 	X3, X9
				ADD		X1, X1, #4
				B		CICLO
FIM:			MOV		W0, W4
				RET
