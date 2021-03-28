.text
.global CountCommon
.type CountCommon, "function"

CountCommon: MOV W4, #0
             CBZ W0, FIM
             CBZ W2, FIM
             MOV X10, X3
             MOV W7, W0
             MOV W11, W2
CICLO:       LDR W5, [X1]
             LDR W6, [X3]
             SUB W9, W6, W5
             CBZ W9, IGUAL
             ADD X3, X3, #4
             SUB W11, W11, #1
             CBZ W11, PROXIMO
             B   CICLO
IGUAL:       ADD W4, W4, #1
             ADD X3, X3, #4
             SUB W11, W11, #1
             CBZ W11, PROXIMO
             B   CICLO
PROXIMO:     ADD X1, X1, #4
             SUB W7, W7, #1
             CBZ W7, FIM
             MOV W11, W2
             MOV X3, X10
             B   CICLO
FIM:         MOV W0, W4
             ret
