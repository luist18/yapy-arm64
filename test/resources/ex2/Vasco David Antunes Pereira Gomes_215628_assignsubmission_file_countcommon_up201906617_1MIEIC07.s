.text
.global CountCommon
.type CountCommon,"function"

CountCommon: MOV W4,0
cicloB:	CBZ W2, fim
		LDR W5,[X3],4
		SUB W2,W2,1
		MOV W7,W0
		MOV X9,X1

cicloA: CBZ W7,cicloB
		LDR W6,[X9],4
		SUB W7,W7,1
		CMP W5,W6
		CINC W4,W4,EQ
		b cicloA

fim: MOV W0,W4
	RET
