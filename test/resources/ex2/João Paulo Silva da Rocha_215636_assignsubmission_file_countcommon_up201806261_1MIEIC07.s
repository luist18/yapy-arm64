.text
.global CountCommon
.type CountCommon,"function"

CountCommon:	MOV X10,#0

CICLO:	CBZ X0,FIM
		SUB X0,X0,#1
		LDR W11,[X1]
		ADD X1,X1,#4
		MOV X8,X2
		MOV X9,X3
		B COMPARAR

COMPARAR:	CBZ X8,CICLO
			SUB X8,X8,#1
			LDR W12,[X9]
			ADD X9,X9,#4
			CMP W11,W12
			B.EQ ADICIONAR
			B COMPARAR

ADICIONAR:	ADD X10,X10,#1
			B COMPARAR



FIM:	MOV X0,X10
		ret
