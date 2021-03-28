.text
.global CountCommon
.type CountCommon, "function"

CountCommon: mov w5,0


ciclo:	cbz w0,END
		ldur w4,[x1]
		sub w0,w0,1
		mov w7,0


ciclo2: cbz w2,ciclo3
		ldur w6, [x3]
		cmp w4,w6
		b.eq NEXT
		add w7,w7,1
		add x3,x3,4
		sub w2,w2,1
		b ciclo2


ciclo3: add x1,x1,4
		b ciclo4

NEXT:	add w5,w5,1
		add x1,x1,4
		b ciclo4

ciclo4: cbz w7,ciclo
		sub x3,x3,4
		sub w7,w7,1
		add w2,w2,1
		b ciclo4


END: mov w0,w5
ret
