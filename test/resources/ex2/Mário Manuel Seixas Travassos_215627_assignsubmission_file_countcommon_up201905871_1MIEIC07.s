.text
.global CountCommon
.type CountCommon,"function"

CountCommon:	mov		x9	,	#0			//counter for equal values (to be returned later)
				mov		x10	,	#4			//register with the value of 4 (for use with the instructions)
				cbz		x2	,	fim			//if vecB's empty, the result is 0

loopA:			cbz		x0	,	fim			//if vecA's empty, the result is 0
				ldr		w6	,	[x1]
				mov		x5	,	#0			//sets counter of the position on vecB

loopB:			ldr		w7	,	[x3]
				cmp		w6	,	w7			//compares vector A's and vector B's elements
				b.ne	notEqual			//if it's not equal, gets the next element
				add		x9	,	x9	,	#1	//else, adds 1 to the equal value counter
				b		nextElementA	//if they're equal, repeating loopB is pointless

notEqual:		add		x3	,	x3	,	#4	//adds 4 bytes to x3's value, to get the next vecB's address
				add		x5	,	x5	,	#1	//adds 1 to vecB's counter
				cmp		x2	,	x5			//compares the counter to the size of vecB
				b.hi	loopB		//if the size is higher than the counter, loops back to loopB

nextElementA:	msub	x3	,	x10	,	x5	,	x3	//get the original address of vecB
				add		x1	,	x1	,	#4			//adds 4 bytes to x1's value, to get the next vecA's address
				sub		x0	,	x0	,	#1
				b		loopA

fim:			mov		x0	,	x9
				ret
