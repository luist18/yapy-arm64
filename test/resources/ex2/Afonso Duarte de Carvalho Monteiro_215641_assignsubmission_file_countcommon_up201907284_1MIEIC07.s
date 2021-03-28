.text
.global CountCommon
.type CountCommon, "function"

CountCommon:
		mov w4, 0
		mov x7, x3 // I save the 2nd sequence's parameters with the intent of reseting them
		mov x8, x2 // before the next element of the 1st sequence is tested

main_cicle:
		cbz w0, end
		ldr w5, [x1]
		b second_cicle

second_cicle:
		cbz w2, next
		ldr w6, [x3]
		cmp w5, w6
		beq tick
		add x3, x3, 4
		sub w2, w2, 1
		b second_cicle

tick:
		add w4, w4, 1
		b next

next:
		add x1, x1, 4
		sub w0, w0, 1
		mov x2, x8
		mov x3, x7
		b main_cicle

end:
		mov w0, w4
		ret
