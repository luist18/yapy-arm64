.text
.global CountCommon
.type CountCommon, "function"

CountCommon:	mov w6 ,0
				cbz w2,FIM
LOOP:			mov x21,x3
				mov w7,w2
				cbz w0,FIM
				sub w0,w0,1
				ldr w4,[x1]
				add x1,x1,4
				b LOOP2
LOOP2:			cbz w7,LOOP
				ldr w20,[x21]
				cmp w4,w20
				beq LOOP3
				add x21,x21,4
				sub w7,w7,1
				b LOOP2
LOOP3:			add w6,w6,1
				b LOOP
FIM:			mov w0,w6
				ret
