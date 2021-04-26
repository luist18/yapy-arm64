from lark import Lark
from yapy.parser.parser_result import ParserResult

arm64_parser = Lark(r"""
    program: header* (label | instruction)*

    label: CNAME ":"

    header: ".text"
            | ".global" /.+/
            | ".type" /.+/


    int_constant: "#"? "-"? INT | "0x"i HEXDIGIT+

    char: /"."/ | /'.'/

    w_register: "w"i INT
    x_register: "x"i INT

    ?normal_register: w_register | x_register

    ?op: normal_register | int_constant | char | "sp"i

    address: "[" (x_register | CNAME) ("," op)? "]" "!"? ("," op)?

    ?cc: "lo"i
        | "hi"i
        | "ls"i
        | "hs"i
        | "lt"i
        | "gt"i
        | "le"i
        | "ge"i
        | "eq"i
        | "ne"i
        | "mi"i
        | "pl"i
        | "vs"i
        | "vc"i
        | "cs"i
        | "cc"i

    ?instruction: arithmetic_instruction
                | bitwise_logical_instruction
                | bitfield_instruction
                | bit_byte_instruction
                | load_store_instruction
                | branch_instructions
                | conditional_instructions
                | compare_instructions

    ?arithmetic_instruction: add
                            | sub
                            | add
                            | sub
                            | neg
                            | neg
                            | mul
                            | umull
                            | umulh
                            | smull
                            | smulh
                            | madd
                            | msub
                            | mneg
                            | umaddl
                            | umsubl
                            | umnegl
                            | smaddl
                            | smsubl
                            | smnegl
                            | udiv
                            | sdiv
    
    ?bitwise_logical_instruction: and
                                | bic
                                | orr
                                | orn
                                | eor
                                | eon
                                | lsl
                                | lsr
                                | asr
                                | ror
                                | mov
                                | mvn
                                | tst

    ?bitfield_instruction: bfi
                            | ubfx
                            | sbfx
    
    ?bit_byte_instruction: cls
                            | clz
                            | rbit
                            | rev
                            | rev16
                            | rev32
                        
    ?load_store_instruction: str
                            | strb
                            | strh
                            | stur
                            | stp
                            | ldr
                            | ldrb
                            | ldrsb
                            | ldrh
                            | ldrsh
                            | ldrsw
                            | ldur
                            | ldp

    ?branch_instructions: b
                        | bl
                        | ret
                        | bcc
                        | cbz
                        | cbnz
    
    ?conditional_instructions: csel
                                | csinc
                                | csneg
                                | csinv
                                | cset
                                | csetm
                                | cinc
                                | cneg
                                | cinv

    ?compare_instructions: cmp
                            | cmn
                            
    add: ("add"i | "adds"i) normal_register "," normal_register "," op
    sub: ("sub"i | "subs"i) normal_register "," normal_register "," op
    neg: ("neg"i | "negs"i) normal_register "," op
    ngc: ("ngc"i | "ngc"i) normal_register "," normal_register
    mul: "mul"i normal_register "," normal_register "," normal_register
    umull: "umull"i x_register "," w_register "," w_register
    umulh: "umulh"i x_register "," x_register "," x_register
    smull: "smull"i x_register "," w_register "," w_register
    smulh: "smulh"i x_register "," x_register "," x_register
    madd: "madd"i normal_register "," normal_register "," normal_register "," normal_register
    msub: "msub"i normal_register "," normal_register "," normal_register "," normal_register
    mneg: "mneg"i normal_register "," normal_register "," normal_register
    umaddl: "umaddl"i x_register "," w_register "," w_register "," x_register
    umsubl: "umsubl"i x_register "," w_register "," w_register "," x_register
    umnegl: "umnegl"i x_register "," w_register "," w_register
    smaddl: "smaddl"i x_register "," w_register "," w_register "," x_register
    smsubl: "smsubl"i x_register "," w_register "," w_register "," x_register
    smnegl: "smnegl"i x_register "," w_register "," w_register
    udiv: "udiv"i normal_register "," normal_register "," normal_register
    sdiv: "sdiv"i normal_register "," normal_register "," normal_register

    and: ("and"i | "ands"i) normal_register "," normal_register "," op
    bic: ("bic"i | "bics"i) normal_register "," normal_register "," op
    orr: "orr"i normal_register "," normal_register "," op
    orn: "orn"i normal_register "," normal_register "," op
    eor: "eor"i normal_register "," normal_register "," op
    eon: "eon"i normal_register "," normal_register "," op
    lsl: "lsl"i normal_register "," normal_register "," op
    lsr: "lsr"i normal_register "," normal_register "," normal_register
    asr: "asr"i normal_register "," normal_register "," op
    ror: "ror"i normal_register "," normal_register "," op
    mov: "mov"i normal_register "," op
    mvn: "mvn"i normal_register "," op
    tst: "tst"i normal_register "," op

    bfi: "bfi"i normal_register "," normal_register "," int_constant "," int_constant
    ubfx: "ubfx"i normal_register "," normal_register "," int_constant "," int_constant
    sbfx: "sbfx"i normal_register "," normal_register "," int_constant "," int_constant

    cls: "cls"i normal_register "," normal_register
    clz: "clz"i normal_register "," normal_register
    rbit: "rbit"i normal_register "," normal_register
    rev: "rev"i normal_register "," normal_register
    rev16: "rev16"i normal_register "," normal_register
    rev32: "rev32"i x_register "," x_register

    str: "str"i normal_register "," address
    strb: "strb"i w_register "," address
    strh: "strh"i w_register "," address
    stur: "stur"i normal_register "," address
    stp: "stp"i normal_register "," normal_register "," address
    ldr: "ldr"i normal_register "," address
    ldrb: "ldrb"i w_register "," address
    ldrsb: "ldrsb"i normal_register "," address
    ldrh: "ldrh"i w_register "," address
    ldrsh: "ldrsh"i normal_register "," address
    ldrsw: "ldrsw"i x_register "," address
    ldur: "ldur"i normal_register "," address
    ldp: "ldp"i normal_register "," normal_register "," address

    b: "b"i CNAME
    bl: "bl"i CNAME
    ret: "ret"i x_register?
    bcc: ("b."i | "b"i) cc CNAME
    cbz: "cbz"i normal_register "," CNAME
    cbnz: "cbnz"i normal_register "," CNAME

    csel: "csel"i normal_register "," normal_register "," normal_register "," cc
    csinc: "csinc"i normal_register "," normal_register "," normal_register "," cc
    csneg: "csneg"i normal_register "," normal_register "," normal_register "," cc
    csinv: "csinv"i normal_register "," normal_register "," normal_register "," cc
    cset: "cset"i normal_register "," cc
    csetm: "csetm"i normal_register "," cc
    cinc: "cinc"i normal_register "," normal_register "," cc
    cneg: "cneg"i normal_register "," normal_register "," cc
    cinv: "cinv"i normal_register "," normal_register "," cc

    cmp: "cmp"i normal_register "," op
    cmn: "cmn"i normal_register "," normal_register

    %import common.WORD
    %import common.CNAME
    %import common.HEXDIGIT
    %import common.INT
    %import common.WS
    %import common.CPP_COMMENT
    %import common.C_COMMENT

    %ignore CPP_COMMENT
    %ignore C_COMMENT
    %ignore WS
    """, start="program")


class Parser:

    @staticmethod
    def parse(content):
        return ParserResult(arm64_parser.parse(content))
