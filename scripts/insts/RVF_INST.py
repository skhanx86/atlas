RV32F_INST = [
    {'mnemonic': 'fmv.w.x', 'handler': 'fmv_w_x_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fmv.x.w', 'handler': 'fmv_x_w_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.s.w', 'handler': 'fcvt_s_w_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.s.wu', 'handler': 'fcvt_s_wu_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.w.s', 'handler': 'fcvt_w_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.wu.s', 'handler': 'fcvt_wu_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'flw', 'handler': 'flw_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': True, 'cof': False},
    {'mnemonic': 'fsw', 'handler': 'fsw_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': True, 'cof': False},
    {'mnemonic': 'fadd.s', 'handler': 'fadd_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fsub.s', 'handler': 'fsub_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fmul.s', 'handler': 'fmul_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fdiv.s', 'handler': 'fdiv_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fsqrt.s', 'handler': 'fsqrt_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fmadd.s', 'handler': 'fmadd_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fmsub.s', 'handler': 'fmsub_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fnmsub.s', 'handler': 'fnmsub_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fnmadd.s', 'handler': 'fnmadd_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fsgnj.s', 'handler': 'fsgnj_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fsgnjn.s', 'handler': 'fsgnjn_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fsgnjx.s', 'handler': 'fsgnjx_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fmin.s', 'handler': 'fmin_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fmax.s', 'handler': 'fmax_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'feq.s', 'handler': 'feq_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'flt.s', 'handler': 'flt_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fle.s', 'handler': 'fle_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
    {'mnemonic': 'fclass.s', 'handler': 'fclass_s_32', 'cost': 1, 'tags': 'F_EXT_32', 'memory': False, 'cof': False},
]

RV64F_INST = [
    {'mnemonic': 'fmv.w.x', 'handler': 'fmv_w_x_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fmv.x.w', 'handler': 'fmv_x_w_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.s.w', 'handler': 'fcvt_s_w_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.s.wu', 'handler': 'fcvt_s_wu_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.w.s', 'handler': 'fcvt_w_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.wu.s', 'handler': 'fcvt_wu_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.l.s', 'handler': 'fcvt_l_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.lu.s', 'handler': 'fcvt_lu_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.s.l', 'handler': 'fcvt_s_l_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fcvt.s.lu', 'handler': 'fcvt_s_lu_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'flw', 'handler': 'flw_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': True, 'cof': False},
    {'mnemonic': 'fsw', 'handler': 'fsw_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': True, 'cof': False},
    {'mnemonic': 'fadd.s', 'handler': 'fadd_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fsub.s', 'handler': 'fsub_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fmul.s', 'handler': 'fmul_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fdiv.s', 'handler': 'fdiv_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fsqrt.s', 'handler': 'fsqrt_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fmadd.s', 'handler': 'fmadd_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fmsub.s', 'handler': 'fmsub_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fnmsub.s', 'handler': 'fnmsub_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fnmadd.s', 'handler': 'fnmadd_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fsgnj.s', 'handler': 'fsgnj_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fsgnjn.s', 'handler': 'fsgnjn_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fsgnjx.s', 'handler': 'fsgnjx_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fmin.s', 'handler': 'fmin_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fmax.s', 'handler': 'fmax_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'feq.s', 'handler': 'feq_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'flt.s', 'handler': 'flt_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fle.s', 'handler': 'fle_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
    {'mnemonic': 'fclass.s', 'handler': 'fclass_s_64', 'cost': 1, 'tags': 'F_EXT_64', 'memory': False, 'cof': False},
]
