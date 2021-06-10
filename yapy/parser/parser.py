from lark import Lark
from yapy.parser.parser_result import ParserResult

arm64_parser = Lark(r"""
    program: header* (label | instruction)*

    label: "."? CNAME ":"

    header: ".text"i
            | ".data"
            | CNAME ":" (".double" | ".quad" | ".int" | ".float" | ".single") ("+" | "-")? (HEXDIGIT | DECIMAL | INT)
            | ".global"i /.+/
            | ".type"i (CNAME)? /.+/
            | ".model"i /.+/
            | ".align"i /.+/
            | ".extern"i /.+/


    int_constant: "#"? (("-" | "+")? (INT | DECIMAL) | (("-" | "+")? "0x"i HEXDIGIT+))

    char: /"."/ | /'.'/

    w_register: "w"i INT
    x_register: "x"i INT

    b_register: "b"i INT
    d_register: "d"i INT
    s_register: "s"i INT
    h_register: "h"i INT

    simd_register: ("q"i | "v"i | "b"i) INT ("." (INT? ("b"i | "h"i | "s"i | "d"i) ("[" INT "]")?))?

    ?normal_register: w_register | x_register | int_constant | simd_register

    ?fp_register: d_register | s_register | h_register | b_register | int_constant

    ?goto: "."? CNAME

    ?op_t: "sp"i | normal_register | fp_register | char | goto

    ?op: op_t ("," op2)?

    ?op2: osxtw | osxtb | olsl | olsr | oasr | ouxtw | ouxtb

    address: CNAME | "[" (x_register | CNAME) ("," op)? "]" "!"? ("," op)?

    !cc: "lo"i
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

    ?instruction: (simd_instructions
                | arithmetic_instruction
                | bitwise_logical_instruction
                | bitfield_instruction
                | bit_byte_instruction
                | load_store_instruction
                | branch_instructions
                | conditional_instructions
                | compare_instructions
                | advanced_instructions
                | fp_instructions) ";"?

    ?arithmetic_instruction: add
                            | sub
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
                        
    ?load_store_instruction: strb
                            | strh
                            | stur
                            | str
                            | stp
                            | ldrsb
                            | ldrsh
                            | ldrsw
                            | ldrb
                            | ldrh
                            | ldurb
                            | ldur
                            | ldr
                            | ldp

    ?branch_instructions: bcc
                        | bl
                        | b
                        | ret
                        | cbnz
                        | cbz
    
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

    ?advanced_instructions: sxtb
                            | sxtw
                            | uxtb
                            | uxth
                            | uxtw
                       
    ?fp_instructions: fadd
                    | fsub
                    | fmul
                    | fnmul
                    | fmadd
                    | fnmadd
                    | fmsub
                    | fnmsub
                    | fdiv
                    | fneg
                    | fabs
                    | fmax
                    | fmin
                    | fsqrt
                    | frinti
                    | fmov
                    | fcsel
                    | fcmp
                    | fccmp
                    | fcvt
                    | scvtf
                    | ucvtf
                    | fcvtns
                    | fcvtnu

    ?simd_instructions: dup
                        | ins
                        | xtn2
                        | xtn
                        | smov
                        | umov
                        | saddl2
                        | saddl
                        | saddw2
                        | saddw
                        | subhn
                        | addp
                        | addv
                        | shl
                        | sshr
                        | ushr
                        | bsl
                        | rev64
                        | saddlv
                        | smaxv
                        | sminv
                        | cmcc
                        | fcmcc
                        | uaddlv
                        | uminv
                        | abs
                        | umaxv
                        | faddp

    sxtb: "sxtb"i op "," op
    sxtw: "sxtw"i op "," op
    uxtb: "uxtb"i op "," op
    uxth: "uxth"i op "," op
    uxtw: "uxtw"i op "," op

    osxtw: "sxtw"i op_t?
    osxtb: "sxtb"i op_t?
    olsl: "lsl"i op_t?
    olsr: "lsr"i op_t?
    oasr: "asr"i op_t?
    ouxtw: "uxtb"i op_t?
    ouxtb: "uxtw"i op_t?
                            
    add: ("add"i | "adds"i) op "," op "," op
    sub: ("sub"i | "subs"i) op "," op "," op
    neg: ("neg"i | "negs"i) op "," op
    ngc: ("ngc"i | "ngc"i) op "," op
    mul: "mul"i op "," op "," op
    umull: "umull"i x_register "," op "," op
    umulh: "umulh"i x_register "," op "," op
    smull: "smull"i x_register "," op "," op
    smulh: "smulh"i x_register "," op "," op
    madd: "madd"i normal_register "," normal_register "," normal_register "," normal_register
    msub: "msub"i normal_register "," normal_register "," normal_register "," normal_register
    mneg: "mneg"i normal_register "," normal_register "," normal_register
    umaddl: "umaddl"i x_register "," w_register "," w_register "," op
    umsubl: "umsubl"i x_register "," w_register "," w_register "," x_register
    umnegl: "umnegl"i x_register "," w_register "," w_register
    smaddl: "smaddl"i x_register "," w_register "," w_register "," op
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
    mov: "mov"i op "," op
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
    ldrsb: "ldrsb"i op "," address
    ldrb: "ldrb"i op "," address
    ldr: "ldr"i op "," address
    ldrh: "ldrh"i op "," address
    ldrsh: "ldrsh"i op "," address
    ldrsw: "ldrsw"i op "," address
    ldurb: "ldurb"i op "," address
    ldur: "ldur"i op "," address
    ldp: "ldp"i op "," op "," address

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

    cmp: "f"? "cmp"i op "," op
    cmn: "cmn"i op "," op

    fadd: "fadd"i fp_register "," fp_register "," op
    fsub: "fsub"i fp_register "," fp_register "," op
    fmul: "fmul"i fp_register "," fp_register "," op
    fnmul: "fnmul"i fp_register "," fp_register "," op
    fmadd: "fmadd"i fp_register "," fp_register "," op "," op
    fnmadd: "fnmadd"i fp_register "," fp_register "," op "," op
    fmsub: "fmsub"i fp_register "," fp_register "," op "," op
    fnmsub: "fnmsub"i fp_register "," fp_register "," op "," op
    fdiv: "fdiv"i fp_register "," fp_register "," op
    fneg: "fneg"i fp_register "," op
    fabs: "fabs"i op "," op
    fmax: "fmax"i fp_register "," op "," op
    fmin: "fmin"i fp_register "," op "," op
    fsqrt: "fsqrt"i fp_register "," op
    frinti: "frinti"i fp_register "," op
    
    fmov: "fmov"i op "," op
    fcsel: "fcsel"i op "," op "," op "," cc
    fcmp: "fcmp"i op "," op
    fccmp: "fccmp"i op "," op "," op "," cc

    fcvt: "fcvt"i op "," op
    scvtf: "scvtf"i op "," op
    ucvtf: "ucvtf"i op "," op
    fcvtns: "fcvtns"i op "," op
    fcvtnu: "fcvtnu"i op "," op

    dup: "dup"i simd_register "," op
    ins: "ins"i simd_register "," op
    xtn2: "xtn2"i simd_register "," simd_register
    xtn: "xtn"i simd_register "," simd_register
    smov: "smov"i op "," simd_register
    umov: "umov"i op "," simd_register

    saddl2: "saddl2"i simd_register "," simd_register "," simd_register
    saddl: "saddl"i simd_register "," simd_register "," simd_register
    saddw2: "saddw2"i simd_register "," simd_register "," simd_register
    saddw: "saddw"i simd_register "," simd_register "," simd_register
    subhn: "subhn"i simd_register "," simd_register "," simd_register
    addp: "addp"i simd_register "," simd_register "," simd_register
    shl: "shl"i simd_register "," simd_register "," op
    sshr: "sshr"i simd_register "," simd_register "," op
    ushr: "ushr"i simd_register "," simd_register "," op
    bsl: "bsl"i simd_register "," simd_register "," simd_register
    rev64: "rev64"i simd_register "," simd_register

    addv: "addv"i op "," simd_register
    saddlv: "saddlv"i op "," simd_register
    smaxv: "smaxv"i op "," simd_register
    sminv: "sminv"i op "," simd_register

    cmcc: "cm"i cc simd_register "," simd_register "," op
    fcmcc: "fcm"i cc simd_register "," simd_register "," simd_register

    uaddlv: "uaddlv"i op "," op
    uminv: "uminv"i op "," op
    abs: "abs"i op "," op
    umaxv: "umaxv"i op "," simd_register
    faddp: "faddp"i op "," simd_register

    %import common.WORD
    %import common.CNAME
    %import common.HEXDIGIT
    %import common.INT
    %import common.DECIMAL
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
