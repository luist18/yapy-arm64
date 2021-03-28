.text
.global CountCommon
.type CountCommon,"function"


CountCommon:	MOV W10,0
				CBZ W0,VAZIO
				CBZ W2,VAZIO
LOOP1:			MOV W4,W0
				MOV X14, X1
				LDR W6,[X3]
LOOP2:			CBZ W4, FIM_1
				LDR X7,[X14]
				CMP W6,W7
				B.EQ ADD
CONTINUE:		ADD X14,X14,4
				SUB W4,W4,1
				B 	LOOP2
FIM_1:			SUB W2,W2,1
				CBZ W2,FIM
				ADD X3,X3,4
				B	LOOP1
ADD:			ADD W10,W10,1
				B CONTINUE
FIM:			MOV W0,W10
				RET
VAZIO:			MOV W0,#0
				RET
