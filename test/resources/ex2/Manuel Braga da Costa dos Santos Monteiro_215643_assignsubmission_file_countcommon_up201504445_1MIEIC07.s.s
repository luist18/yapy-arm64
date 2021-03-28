.text
.global CountCommon
.type CountCommon,"function"

CountCommon:
		mov			X6, #0
		mov			X7, x2
		mov			X8, x3

CICLO:
		CBZ			x0, FIM
		LDR  		w4, [x1]
		B			SUBCICLO

SUBCICLO:
		CBZ			x7, MIDCICLO
		LDR  		w10, [X8]
		ADD			x8, x8, #4
		SUB			X7, X7, #1
		CMP			w4, w10
	 	B.EQ		ADD
	 	B			SUBCICLO

MIDCICLO:
		ADD			x1, x1, #4
		SUB			X0, X0, #1
		mov			X7, x2
		mov			X8, x3
		B			CICLO

ADD:
		ADD 		x6, x6, #1
		B			SUBCICLO

FIM:
		MOV 		x0, x6
		ret
