.text
.global CountCommon
.type CountCommon,"function"

CountCommon:	mov W7, #0
				mov X6, #-4
        		b restore

restore:		mov W4, W0
				mov X5, #-4
				b loop

loop:			cbz w2, result
				sub w2, W2, 1
				add X6, X6, 4
				ldr W9, [X3, X6]
				b	insideLoop

insideLoop:		cbz W4,restore
				sub w4, W4, 1
				add X5, X5, 4
				ldr W8, [X1, X5]
				b	action

action:			cmp W9, W8
				b.eq add1
				b	insideLoop

add1:			add W7, W7, 1
				b	insideLoop

result:			mov W0, W7
				ret
