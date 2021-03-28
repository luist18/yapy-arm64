/*
 * countcommon_up201906784_1MIEIC07.s
 *
 *  Created on: 16 Apr 2020
 *      Author: marga
 */

.text
.global CountCommon
.type CountCommon, "function"

CountCommon: 	cbz x2, end
				mov x4, #0

vec1: 			cbz x0, end
				ldr w5, [x1]
				add x1, x1, #4
				sub x0, x0, #1
				mov x7, x2
				mov x9, x3

vec2:			cbz x7, vec1
				ldr w6, [x9]
				add x9, x9, #4
				sub x7, x7, #1
				cmp w5, w6
				b.ne vec2
				add x4, x4, #1
				b vec1

end: 			mov x0, x4
				ret
