from lark import Lark
from yapy.parser.parser_result import ParserResult

arm64_parser = Lark(r"""
    program: header* (label | instruction)*

    label: (INT | CNAME)* ":"

    header: ".text"i
            | ".global"i /.+/
            | ".type"i /.+/
            | ".model"i /.+/
            | ".align"i /.+/


    int_constant: "#"? ("-"? INT | "0x"i HEXDIGIT+)

    char: /"."/ | /'.'/

    w_register: "w"i INT
    x_register: "x"i INT

    ?normal_register: w_register | x_register

    ?goto: (INT | CNAME)*

    ?op: normal_register | int_constant | char | "sp"i | goto

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

    ?instruction: (arithmetic_instruction
                | bitwise_logical_instruction
                | bitfield_instruction
                | bit_byte_instruction
                | load_store_instruction
                | branch_instructions
                | conditional_instructions
                | compare_instructions) ";"?

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
                            
    add: ("add"i | "adds"i) normal_register "," op "," op
    sub: ("sub"i | "subs"i) normal_register "," op "," op
    neg: ("neg"i | "negs"i) normal_register "," op
    ngc: ("ngc"i | "ngc"i) normal_register "," op
    mul: "mul"i normal_register "," op "," op
    umull: "umull"i x_register "," op "," op
    umulh: "umulh"i x_register "," op "," op
    smull: "smull"i x_register "," op "," op
    smulh: "smulh"i x_register "," op "," op
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
    lsr: "lsr"i normal_register "," normal_register "," op
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

    str: "str"i op "," address
    strb: "strb"i op "," address
    strh: "strh"i op "," address
    stur: "stur"i op "," address
    stp: "stp"i op "," op "," address
    ldr: "ldr"i op "," address
    ldrb: "ldrb"i op "," address
    ldrsb: "ldrsb"i op "," address
    ldrh: "ldrh"i op "," address
    ldrsh: "ldrsh"i op "," address
    ldrsw: "ldrsw"i op "," address
    ldur: "ldur"i op "," address
    ldp: "ldp"i op "," normal_register "," address

    b: "b"i goto
    bl: "bl"i goto
    ret: "ret"i x_register?
    bcc: ("b."i | "b"i) cc goto
    cbz: "cbz"i normal_register "," goto
    cbnz: "cbnz"i normal_register "," goto

    csel: "csel"i op "," op "," op "," cc
    csinc: "csinc"i op "," op "," op "," cc
    csneg: "csneg"i op "," op "," op "," cc
    csinv: "csinv"i op "," op "," op "," cc
    cset: "cset"i op "," cc
    csetm: "csetm"i op "," cc
    cinc: "cinc"i op "," op "," cc
    cneg: "cneg"i op "," op "," cc
    cinv: "cinv"i op "," op "," cc

    cmp: "cmp"i op "," op
    cmn: "cmn"i op "," op

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
