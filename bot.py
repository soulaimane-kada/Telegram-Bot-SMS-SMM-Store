from telethon import TelegramClient, events, types, functions
from datetime import timedelta

import sqlite3, asyncio, json, datetime
import asyncio
import base64
import hashlib
import json
import uuid
import aiohttp
import math
import random, string, os
import re


from contact_support import *
from change_lan import *
from menu import *
from my_account import *
from buy_numbers import *
from myfatoorah_payApi import check_invoice_status_myfatoorah, create_invoice_myfatoorah
from smm import ShowSmmRecordOrders, SmmBuyService, SmmServices_List, SmmShowServiceInfo, SmmShowServices, SmmViewOrderInfo, add_column_if_not_exists, create_table_if_not_existsV2
from smm import subscription_history_columns, bot_settings_columns, ad_buttons_columns, limited_offer_columns, vip_subscription_columns


# READ CONFIGS
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)


# BOT
api_id_bot, api_hash_bot, owner_id = 1724716, "00b2d8f59c12c1b9a4bc63b70b461b2f", 691459768
script_owner_id = 978571497
#token = config["TEST_BOT_TOKEN"] # TEST
token = config["BOT_TOKEN"] # CLIENT TOKEN

bot = TelegramClient("Bot", api_id_bot, api_hash_bot).start(bot_token=token)


API_KEY = ''
MERCHANT_ID = ''
BASE_URL = "https://api.cryptomus.com/v1"


# idx
idx = {'fr_index': '1', 'vm_index': '1', 'mb_index': '1', 'qg_index': '1', 'pm_index': '1', 'sv_index': '1', 'vk_index': '1', 'gk_index': '1', 'sy_index': '1', 'ua_index': '1', 'kt_index': '1', 'jr_index': '1', 'rl_index': '1', 'hc_index': '1', 'lj_index': '1', 'rj_index': '1', 'bn_index': '1', 'hy_index': '1', 'ke_index': '1', 'zr_index': '1', 'zm_index': '1', 'mo_index': '1', 'wg_index': '1', 'tr_index': '1', 'ee_index': '1', 'fk_index': '1', 'sl_index': '1', 'bl_index': '1', 'jq_index': '1', 'ge_index': '1', 'ir_index': '1', 'qh_index': '1', 'dr_index': '1', 'gs_index': '1', 'sr_index': '1', 'ac_index': 
'1', 'cp_index': '1', 'ym_index': '1', 'hx_index': '1', 'tx_index': '1', 'ki_index': '1', 'tg_index': '1', 'tc_index': '1', 'me_index': '1', 'of_index': '1', 'jl_index': '1', 'gm_index': '1', 'zy_index': '1', 'ef_index': '1', 'mm_index': '1', 'dy_index': '1', 'yi_index': '1', 'gt_index': '1', 'co_index': '1', 'qj_index': '1', 'bz_index': '1', 're_index': '1', 'pr_index': '1', 'wa_index': '1', 'fb_index': '1', 'gp_index': '1', 'ub_index': '1', 'ig_index': '1', 'bc_index': '1', 'hu_index': '1', 'ew_index': '1', 'tw_index': '1', 'ry_index': '1', 'cb_index': '1', 'ex_index': '1', 'im_index': '1', 'ju_index': '1', 'fv_index': '1', 'ue_index': '1', 'ff_index': '1', 'qq_index': '1', 'jc_index': '1', 'ha_index': '1', 'sh_index': '1', 'tf_index': '1', 'ny_index': '1', 'qe_index': '1', 'sg_index': '1', 'zl_index': '1', 'lf_index': '1', 'cn_index': '1', 'tp_index': '1', 'pz_index': '1', 'yl_index': '1', 'gq_index': '1', 'yn_index': '1', 'ly_index': '1', 'oi_index': '1', 'fz_index': '1', 'nv_index': '1', 'vs_index': '1', 'wc_index': '1', 'da_index': '1', 'ja_index': '1', 'cr_index': '1', 'zo_index': '1', 'zk_index': '1', 'fh_index': '1', 'nz_index': '1', 'yy_index': '1', 'tn_index': '1', 'kf_index': '1', 'aq_index': '1', 'dh_index': '1', 'ta_index': '1', 'nf_index': '1', 'mg_index': '1', 'pd_index': '1', 'ni_index': '1', 'dt_index': '1', 'rs_index': '1', 'uu_index': '1', 'ti_index': '1', 'kl_index': '1', 'dj_index': '1', 'km_index': '1', 'vi_index': '1', 'dl_index': '1', 'nl_index': '1', 'jx_index': '1', 'xm_index': '1', 'nq_index': '1', 'ie_index': '1', 'et_index': '1', 'cm_index': '1', 'qr_index': '1', 'sa_index': '1', 'yk_index': '1', 'wh_index': '1', 'pf_index': '1', 'yj_index': '1', 'rc_index': '1', 'yw_index': '1', 'ib_index': '1', 'ip_index': '1', 'cw_index': '1', 'fd_index': '1', 'qf_index': '1', 
'my_index': '1', 'tm_index': '1', 'ok_index': '1', 'ul_index': '1', 'rt_index': '1', 'gr_index': '1', 'ds_index': '1', 'ui_index': '1', 'wt_index': '1', 'df_index': '1', 'xx_index': '1', 'oz_index': '1', 'hb_index': '1', 'dg_index': '1', 'wx_index': '1', 'yx_index': '1', 'ft_index': '1', 'qy_index': '1', 'st_index': '1', 'bp_index': '1', 'py_index': '1', 'gx_index': '1', 'vy_index': '1', 'wp_index': '1', 'zs_index': '1', 'dp_index': '1', 'vp_index': '1', 'ls_index': '1', 'xd_index': '1', 'kc_index': '1', 'zt_index': '1', 'sn_index': '1', 'mi_index': '1', 'sb_index': '1', 'tk_index': '1', 'tu_index': '1', 'za_index': '1', 'hw_index': '1', 'ma_index': '1', 'ot_index': '1', 'uf_index': '1', 'xy_index': '1', 'hp_index': '1', 'rk_index': '1', 'sd_index': 
'1', 'uk_index': '1', 'ht_index': '1', 'do_index': '1', 'ya_index': '1', 'gf_index': '1', 'tl_index': '1', 'jg_index': '1', 'us_index': '1', 'xz_index': '1', 'vz_index': '1', 'xk_index': '1', 'mx_index': '1', 'gj_index': '1', 'em_index': '1', 'qo_index': '1', 'bo_index': '1', 'uv_index': '1', 'rr_index': '1', 'hz_index': '1', 'ka_index': '1', 'yu_index': '1', 'ae_index': '1', 'bd_index': '1', 'kj_index': '1', 'xu_index': '1', 'vd_index': '1', 've_index': '1', 'cq_index': '1', 'fs_index': '1', 'br_index': '1', 'xr_index': '1', 'ej_index': '1', 'ep_index': '1', 'ij_index': '1', 'am_index': '1', 'zg_index': '1', 'wb_index': '1', 'uz_index': '1', 'il_index': '1', 'om_index': '1', 'oc_index': '1', 'oe_index': '1', 'vg_index': '1', 'bv_index': '1', 'ah_index': '1', 'xh_index': '1', 'mt_index': '1', 'fw_index': '1', 'ev_index': '1', 'ww_index': '1', 'ji_index': '1', 'si_index': '1', 'rd_index': '1', 'li_index': '1', 'lc_index': '1', 'zd_index': '1', 'cj_index': '1', 'xt_index': '1', 'we_index': '1', 'kw_index': '1', 'ts_index': '1', 'cy_index': '1', 'zn_index': '1', 'xs_index': '1', 'bw_index': '1', 'zh_index': '1', 'fu_index': '1', 'pu_index': '1', 'ky_index': '1', 'sw_index': '1', 'go_index': '1', 'atn_index': '1', 'ccu_index': '1', 'acz_index': '1', 'wr_index': '1', 'bcq_index': '1', 'are_index': '1', 'awz_index': '1', 'asy_index': '1', 'bxy_index': 
'1', 'abu_index': '1', 'aez_index': '1', 'afp_index': '1', 'bzk_index': '1', 'aaa_index': '1', 'vr_index': '1', 'boo_index': '1', 'aka_index': '1', 'nc_index': '1', 'aiw_index': '1', 'pc_index': '1', 'aik_index': '1', 'als_index': '1', 'blr_index': '1', 'aor_index': '1', 'abk_index': '1', 'agl_index': '1', 'aop_index': '1', 'atu_index': '1', 'bdp_index': '1', 'amb_index': '1', 'awv_index': '1', 'ada_index': '1', 'aba_index': '1', 'abo_index': '1', 'bnl_index': '1', 'abc_index': '1', 'blt_index': '1', 'adt_index': '1', 'bex_index': '1', 'bme_index': '1', 'bdr_index': '1', 'bmi_index': '1', 'bwv_index': '1', 'anh_index': '1', 'bfg_index': '1', 'cau_index': '1', 'aje_index': '1', 'btv_index': '1', 'anx_index': '1', 'alg_index': '1', 'ang_index': '1', 'auc_index': '1', 'akp_index': '1', 'azi_index': '1', 'ais_index': '1', 'aux_index': '1', 'agm_index': '1', 'agh_index': '1', 'ber_index': '1', 'aoy_index': '1', 'bwx_index': '1', 'agg_index': '1', 'alj_index': '1', 'bpe_index': '1', 'agd_index': '1', 'abg_index': '1', 'asj_index': '1', 'aoz_index': '1', 
'bij_index': '1', 'brk_index': '1', 'abn_index': '1', 'aff_index': '1', 'ani_index': '1', 'arf_index': '1', 'bwa_index': '1', 'afz_index': '1', 'akr_index': '1', 'bkd_index': '1', 'agj_index': '1', 'ayb_index': '1', 'bbk_index': '1', 'bhr_index': '1', 'te_index': '1', 'afs_index': '1', 'ahl_index': '1', 'auz_index': '1', 'bcx_index': '1', 'bsv_index': '1', 'zp_index': '1', 'aem_index': '1', 'ahb_index': '1', 'ahe_index': '1', 'asb_index': '1', 'axn_index': '1', 'axr_index': '1', 'bxg_index': '1', 'afe_index': '1', 'ait_index': '1', 'akd_index': '1', 'aoh_index': '1', 'axx_index': '1', 'bjp_index': '1', 'blm_index': '1', 'blz_index': '1', 'ajj_index': '1', 'ajq_index': '1', 'ama_index': '1', 'aqt_index': '1', 'bli_index': '1', 'bqe_index': '1', 'acm_index': '1', 'ael_index': '1', 'aex_index': '1', 'afn_index': '1', 'agk_index': '1', 'aoi_index': '1', 'aok_index': '1', 'apd_index': '1', 'apg_index': '1', 'avj_index': '1', 'bkk_index': '1', 'bqr_index': '1', 'bqy_index': '1', 'bra_index': '1', 'bzo_index': '1', 'kk_index': '1', 'ajn_index': '1', 'app_index': '1', 'apq_index': '1', 'apr_index': '1', 'ars_index': '1', 'bas_index': '1', 'bgj_index': '1', 'bii_index': '1', 'bvh_index': '1', 'zb_index': '1', 'aaq_index': '1', 'aav_index': '1', 'abe_index': '1', 'abq_index': '1', 'aeu_index': '1', 'aix_index': '1', 'aiz_index': '1', 'akz_index': '1', 'alm_index': '1', 'alo_index': '1', 'anl_index': '1', 'auh_index': '1', 'avb_index': '1', 'avk_index': '1', 'ayn_index': '1', 'bfa_index': '1', 'bfr_index': '1', 'bfw_index': '1', 'bow_index': '1', 'bqh_index': '1', 'bsw_index': '1', 'btl_index': '1', 'btn_index': '1', 'bvi_index': '1', 'bwd_index': '1', 'cbs_index': '1', 'nh_index': '1', 'qx_index': '1', 'aey_index': '1', 'agb_index': '1', 'agv_index': '1', 'ahi_index': '1', 'ahj_index': '1', 'aig_index': '1', 'amw_index': '1', 'ana_index': '1', 'ane_index': '1', 'aon_index': '1', 'aow_index': '1', 'aqy_index': '1', 'arp_index': '1', 'asp_index': '1', 'aul_index': '1', 'aup_index': '1', 'awg_index': '1', 'awr_index': '1', 'baq_index': '1', 'bbg_index': '1', 'bbl_index': '1', 'bbm_index': '1', 'bbq_index': '1', 'bbu_index': '1', 'bdd_index': '1', 'bem_index': '1', 'bgt_index': '1', 'bic_index': '1', 'bjz_index': '1', 'blx_index': '1', 'bmm_index': '1', 
'bng_index': '1', 'bni_index': '1', 'bnt_index': '1', 'bpt_index': '1', 'bqb_index': '1', 'bqn_index': '1', 'bru_index': '1', 'bst_index': '1', 'bsu_index': '1', 'btx_index': '1', 'bud_index': '1', 'bvs_index': '1', 'byh_index': '1', 'kq_index': '1', 'mv_index': '1', 'ns_index': '1', 'tv_index': '1', 'aag_index': '1', 'abb_index': '1', 'abd_index': '1', 'abt_index': '1', 'aci_index': '1', 'acn_index': '1', 'acw_index': '1', 'adc_index': '1', 'adi_index': '1', 'adp_index': '1', 'agw_index': '1', 'agx_index': '1', 'ahd_index': '1', 'ahv_index': '1', 'aid_index': '1', 'aim_index': '1', 'aiq_index': '1', 
'ajy_index': '1', 'anj_index': '1', 'ann_index': '1', 'ano_index': '1', 'anw_index': '1', 'aoe_index': '1', 'aom_index': '1', 'aoo_index': '1', 'apf_index': '1', 'apl_index': '1', 'aqj_index': '1', 'ari_index': '1', 'asf_index': '1', 'atl_index': '1', 'atp_index': '1', 'atr_index': '1', 'aua_index': '1', 'aub_index': '1', 'auj_index': '1', 'avv_index': '1', 'awq_index': '1', 'aws_index': '1', 'awu_index': '1', 'axs_index': '1', 'ayc_index': '1', 'ayo_index': '1', 'ayv_index': '1', 'ayz_index': '1', 'azz_index': '1', 'bai_index': '1', 'bav_index': '1', 'bay_index': '1', 'bba_index': '1', 'bbr_index': '1', 'bcg_index': '1', 'bcz_index': '1', 'bdg_index': '1', 'bdo_index': '1', 'bdt_index': '1', 'bdw_index': '1', 'bih_index': '1', 'bix_index': '1', 'bke_index': '1', 'bkz_index': '1', 'blh_index': '1', 'bls_index': '1', 'blw_index': '1', 'bmd_index': '1', 'bnu_index': '1', 'bob_index': '1', 'bod_index': '1', 'boh_index': '1', 'bol_index': '1', 'bon_index': '1', 'bou_index': '1', 'bpq_index': '1', 'bpz_index': '1', 'bqo_index': '1', 'bqp_index': '1', 'brc_index': '1', 'brg_index': '1', 'brr_index': '1', 'brt_index': '1', 'bsf_index': '1', 'bsl_index': '1', 'bsm_index': '1', 'btr_index': '1', 'bwt_index': '1', 'bxn_index': '1', 'byd_index': '1', 'byp_index': '1', 'caj_index': '1', 'cct_index': '1', 'kv_index': '1', 'ng_index': '1', 'oj_index': '1', 'qv_index': '1', 'ws_index': '1', 'apo_index': '1', 'bga_index': '1', 'bkv_index': '1', 'pb_index': '1', 'bvf_index': '1', 'ze_index': '1', 'bnf_index': '1', 'apj_index': '1', 'alp_index': '1', 'ako_index': '1', 'bxv_index': '1', 'ahr_index': '1', 'bop_index': '1', 'bxu_index': '1', 'tz_index': '1', 'bvj_index': '1', 'bxc_index': '1', 'adj_index': '1', 'aof_index': '1', 'apy_index': '1', 'bte_index': '1', 'bla_index': '1', 'aay_index': '1', 'bxi_index': '1', 'bri_index': '1', 'amz_index': '1', 'bzf_index': '1', 'alb_index': '1', 'azd_index': '1', 'ajc_index': '1', 'acu_index': '1', 'adw_index': '1', 'anq_index': '1', 'rn_index': '1', 'bkn_index': '1', 'aes_index': '1', 'azl_index': '1', 'anb_index': '1', 'bpc_index': '1', 'bje_index': '1', 'afk_index': 
'1', 'ble_index': '1', 'aeq_index': '1', 'bso_index': '1', 'ail_index': '1', 'ady_index': '1', 'bit_index': '1', 'bdh_index': '1', 'bwf_index': '1', 'ami_index': '1', 'bzv_index': '1', 'bif_index': '1', 'bbj_index': '1', 'bqm_index': '1', 'bbs_index': '1', 'bog_index': '1', 'acr_index': '1', 'btu_index': '1', 'bfv_index': '1', 'api_index': '1', 'akm_index': '1', 'acb_index': '1', 'acd_index': '1', 'bwu_index': '1', 'cbh_index': '1', 'bfo_index': '1', 'ahx_index': '1', 'afa_index': '1', 'btd_index': '1', 'adz_index': '1', 'azn_index': '1', 'ark_index': '1', 'bcy_index': '1', 'bpi_index': '1', 'bnz_index': '1', 'cak_index': '1', 'agc_index': '1', 'aih_index': '1', 'brf_index': '1', 'aju_index': '1', 'aos_index': '1', 'bmb_index': '1', 'bcr_index': '1', 'ahf_index': '1', 'bbt_index': '1', 'aiv_index': '1', 'bui_index': '1', 'bqi_index': '1', 'jy_index': '1', 'bkw_index': '1', 'nt_index': '1', 'btq_index': '1', 'sc_index': '1', 'aoq_index': '1', 'abh_index': '1', 'bab_index': '1', 'avu_index': '1', 'bro_index': '1', 'cbk_index': '1', 'bsa_index': '1', 
'bxp_index': '1', 'bye_index': '1', 'bku_index': '1', 'afu_index': '1', 'cbb_index': '1', 'acc_index': '1', 'bjq_index': '1', 'aeg_index': '1', 'aqq_index': '1', 'bhz_index': '1', 'bry_index': '1', 'arx_index': '1', 'aym_index': '1', 'bwl_index': '1', 'asq_index': '1', 'bbi_index': '1', 'alx_index': '1', 'ahc_index': '1', 'bhe_index': '1', 'byf_index': '1', 'bck_index': '1', 'bqx_index': '1', 'cba_index': '1', 'bns_index': '1', 'bib_index': '1', 'byw_index': '1', 'bpg_index': '1', 'boz_index': '1', 'avt_index': '1', 'box_index': '1', 'cac_index': '1', 'bnp_index': '1', 'bpp_index': '1', 'auo_index': '1', 'azy_index': '1', 'arr_index': '1', 'bhl_index': '1', 'bhf_index': '1', 'arb_index': '1', 'bmj_index': '1', 'bly_index': '1', 'aqm_index': '1', 'bos_index': '1', 'abl_index': '1', 'bnd_index': '1', 'aeh_index': '1', 'bzb_index': '1', 'bsy_index': '1', 'ayr_index': '1', 'bre_index': '1', 'btp_index': '1', 'bbf_index': '1', 'afm_index': '1', 'bbd_index': '1', 'agi_index': '1', 'md_index': '1', 'blq_index': '1', 'yh_index': '1', 'bwe_index': '1', 'bhj_index': '1', 'ajv_index': '1', 'bau_index': '1', 'aps_index': '1', 'bss_index': '1', 'anm_index': '1', 'bhp_index': '1', 'axt_index': '1', 'bki_index': '1', 'lm_index': '1', 'apb_index': '1', 'pv_index': '1', 'ov_index': '1', 'ban_index': '1', 'mw_index': '1', 'buj_index': '1', 'bhb_index': '1', 'wd_index': '1', 'can_index': '1', 'bji_index': '1', 'bxw_index': '1', 'bxj_index': '1', 'axm_index': '1', 'azs_index': '1', 'bvu_index': '1', 'aat_index': '1', 'akl_index': '1', 'aab_index': '1', 'aox_index': '1', 'blc_index': '1', 'js_index': '1', 'akj_index': '1', 'bko_index': '1', 'ccl_index': '1', 'axj_index': '1', 'wu_index': '1', 'afo_index': '1', 'bxr_index': '1', 'bdb_index': '1', 'axp_index': '1', 'bgn_index': '1', 'aol_index': '1', 'aet_index': '1', 'cam_index': '1', 'bny_index': '1', 'aer_index': '1', 'btm_index': '1', 'buy_index': '1', 'aga_index': '1', 'arc_index': '1', 'auf_index': '1', 'bmx_index': '1', 'adv_index': '1', 'ahn_index': '1', 'aej_index': '1', 'afr_index': '1', 'amy_index': '1', 'afd_index': '1', 'bwy_index': '1', 'ace_index': 
'1', 'adu_index': '1', 'aug_index': '1', 'blo_index': '1', 'axg_index': '1', 'bxs_index': '1', 'bxf_index': '1', 'ms_index': '1', 'bgv_index': '1', 'aax_index': '1', 'aly_index': '1', 'aru_index': '1', 'brv_index': '1', 'aaz_index': '1', 'ahk_index': '1', 'baj_index': '1', 'bwo_index': '1', 'blp_index': '1', 'afc_index': '1'}



# Configs
channels_list = []
page_data = {}

PAGE_SIZE = 4
ITEMS_PER_PAGE = 2


# database
database = sqlite3.connect('database.db')
cursor = database.cursor()

async def CommitDatabase(database):
    database.commit()
    
# Load lists
banned_users = json.load(open("banned_users.json"))
waiting_verification = json.load(open("waiting_verification.json"))
bot_lang = json.load(open("lang.json", encoding='UTF-8'))

smm_services = json.load(open('smm_services.json', encoding='utf-8'))


###############################
async def make_request(url: str, invoice_data: dict):
    encoded_data = base64.b64encode(
        json.dumps(invoice_data).encode("utf-8")
    ).decode("utf-8")
    signature = hashlib.md5(f"{encoded_data}{API_KEY}".encode("utf-8")).hexdigest()

    async with aiohttp.ClientSession(headers={
        "merchant": MERCHANT_ID,
        "sign": signature,
    }) as session:
        async with session.post(url=url, json=invoice_data) as response:
            if not response.ok:
                raise ValueError(response.reason)

            return await response.json()


async def create_invoice(amount):
    invoice_data = await make_request(
        url="https://api.cryptomus.com/v1/payment",
        invoice_data={
            "amount": f"{amount}",
            "currency": "USD",
            "order_id": str(uuid.uuid4())
        },
    )
    
    return [invoice_data['result']['uuid'], invoice_data['result']['url'], invoice_data]


async def check_invoice_paid(id):
	invoice_data = await make_request(
		url="https://api.cryptomus.com/v1/payment/info", 
		invoice_data={"uuid": id},
	)

	if invoice_data['result']['payment_status'] in ('paid', 'paid_over'):
		return [True, invoice_data]
	else:
		return [False, invoice_data]


async def save_as_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)
        

# bot errors
async def record_an_error(error_data):
    with open("bot_errors.txt", "+a") as file_error:
        file_error.write(f'{error_data}\n')
        

# GET TIME & DATE
async def DateTimeNow():
    Year, Month, Day, Hour, Min, Sec = datetime.datetime.now().strftime('%Y'), datetime.datetime.now().strftime('%m'), datetime.datetime.now().strftime('%d'), datetime.datetime.now().strftime('%H'), datetime.datetime.now().strftime('%M'), datetime.datetime.now().strftime('%S')
    return datetime.datetime(int(Year), int(Month), int(Day), int(Hour), int(Min), int(Sec))
	

# add time to user order
async def add_time_registered(reg_time, extra_time):
    reg_datetime = datetime.datetime.combine(datetime.datetime.today(), reg_time)
    new_reg_datetime = reg_datetime + datetime.timedelta(seconds=extra_time)
    return new_reg_datetime.time()


# Delete Event
async def DeleteEvent(event):
    try:
        await event.delete()
    except:pass


# Set bot commands
async def set_bot_commands():
    # Define the list of commands
    commands = [
        types.BotCommand(command="start", description="Start the bot"),
        types.BotCommand(command="developer", description="Get Bot Developer information")
    ]

    # Set the bot commands
    await bot(functions.bots.SetBotCommandsRequest(
        commands=commands,
        scope=types.BotCommandScopeDefault(),
        lang_code='en'
    ))
	
###############################
async def SendDatabase(event):
    try:
        database = await bot.send_message(entity='zkada', message='database', file='database.db')
    except:pass


# BOT - ADD CREDITS
@bot.on(events.CallbackQuery(data='editUser_price'))
async def AddCredits(event):
    
    if event.chat_id == owner_id or event.chat_id == script_owner_id:
        async with event.client.conversation(event.chat_id) as conv:
            await conv.send_message('أرسل ايدي الشخص الذي تريد اضافة/حذف الرصيد له :')
            user_id = await conv.get_response()
            
            await conv.send_message('__أرسل الرصيد بالدولار ( لحذف رصيد أرسل الرقم بالسالب ):__')
            credits = await conv.get_response()
        
    try:
        user_id, credits = user_id.message, credits.message
        credits = float(credits) * 10
        user = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {user_id}").fetchall()
        if len(user) != 0:
            new_credits = round((float(user[0][2]) + float(credits)), 2)
            user = cursor.execute(f"UPDATE bot_users SET credits = {new_credits} WHERE user_id = {user_id}")
            notice_user = await event.client.send_message(entity=int(user_id), message=f'__The owner has send to you credits : **{credits} Credit**__')
            notice_admin = await event.reply("تم التنفيذ بنجاح")
            database.commit()

    except Exception as error:
        notice_user = await event.reply(str(error))
	

# BOT - SEND MESSAGE TO ONE USER
@bot.on(events.CallbackQuery(data='single_broadcast'))
async def UserInfo(event):

    if event.chat_id == owner_id or event.chat_id == script_owner_id:
        async with bot.conversation(event.chat_id) as conv:
            await conv.send_message('__أرسل ايدي الشخص :__')
            user_id = await conv.get_response()
            
            await conv.send_message('__أرسل الرسالة :__')
            the_message = await conv.get_response()
        
        try:
            send_to__user = await bot.send_message(entity=int(user_id.message), message=the_message)
            notice_admin = await event.reply("__تم التنفيذ__")
        except:
            notice_admin = await event.reply("__المستخدم قام بحظر البوت, الرسالة لم تصل له!__")
	

# BROADCAST
@bot.on(events.CallbackQuery(data='broadcast')) 
async def BroadCast(event):

    if event.chat_id == owner_id or event.chat_id == 978571497:
        async with bot.conversation(event.chat_id) as conv:
            await conv.send_message('__أرسل الرسالة :__')
            the_message = await conv.get_response()
            
        notice_admin = await event.reply(f"__جاري الارسال...__")
        users = cursor.execute(f"SELECT * FROM bot_users")
        users = cursor.fetchall()
        success, fails = 0, 0
        for user in users:
            try:
                if int(user[0]) != owner_id:
                    send_to__user = await bot.send_message(entity=int(user[0]), message=the_message)
                    success += 1
                else:
                    success += 1
            except:
                # cursor.execute(f"UPDATE bot_users SET banned = 'YES' WHERE user_id = {int(user[0])}")
                fails += 1
        
        bot_users = json.load(open('banned_users.json')) # cursor.execute("SELECT * FROM bot_users WHERE banned = 'YES'")
        # bot_users = cursor.fetchall()

        notice_admin = await event.reply(f"""
📊 تمت الإذاعة بنجاح تام 

👥 المستخدمون المستهدفون الذين شاهدوا الرساله: غير معروف
✅ تم الإرسال إلى: {success}
🚫 الاعضاء المحظورين: {len(bot_users)}
❌ فشل في الإرسال لهم بسبب الحظر : {fails}
📈 نسبة نجاح الاذاعة : {round((success / len(users)) * 100, 2)}%
""")
	


# BOT - RESET CANCELS
@bot.on(events.CallbackQuery(data='reset_daily_limit'))
async def ResetCancels(event):

	if event.chat_id == owner_id or event.chat_id == script_owner_id:
		async with bot.conversation(event.chat_id) as conv:
			await conv.send_message('__أرسل ايدي الشخص :__')
			user_id = (await conv.get_response()).message
            
		try:
			# user_id = user_id.message
			# user = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {user_id}").fetchone()
			# if user != None:
			user = cursor.execute(f"UPDATE bot_users SET cancels = {0} WHERE user_id = {int(user_id)}")

			try:
				notice_user = await bot.send_message(entity=int(user_id), message=f'__تم تصفير الالغاءات اليومية من قبل المشرف__')
			except:pass
    
			await event.respond("__تم التنفيذ__")
			database.commit()
			
		except Exception as error:
			notice_user = await event.reply(str(error))
		


# BOT - BACK TO MENU
@bot.on(events.NewMessage(pattern='الرجوع للقائمة السابقة'))
async def BackToMenuOwner(event):
    menu = await bot_menu(event, database, cursor, owner_id)

	
#######################################################################################################################
# BOT COMMING DIALOGS
@bot.on(events.NewMessage)
async def CommingDialogs(event):
    global banned_users

    banned_users = json.load(open('banned_users.json'))
    
    try:
        await set_bot_commands()
    except Exception as error:print (error)
    
    try:
        await create_table_if_not_existsV2(cursor, database, 'subscription_history', subscription_history_columns)
        await create_table_if_not_existsV2(cursor, database, 'bot_settings ', bot_settings_columns)
        await create_table_if_not_existsV2(cursor, database, 'ad_buttons', ad_buttons_columns)
        await create_table_if_not_existsV2(cursor, database, 'limited_offer', limited_offer_columns)
        await create_table_if_not_existsV2(cursor, database, 'vip_subscription', vip_subscription_columns)        

        await add_column_if_not_exists(cursor, database, 'bot_users', 'register_date', 'DATE')
        await add_column_if_not_exists(cursor, database, 'bot_users', 'firstname', 'TEXT')
        await add_column_if_not_exists(cursor, database, 'bot_users', 'lastname', 'TEXT')
        await add_column_if_not_exists(cursor, database, 'bot_settings', 'daily_cancel_limit', 'INTEGER')
    except Exception as error:print (f'add column:', error)

    if event.is_private:
        if event.chat_id not in banned_users.get("banned_users"):
            if str(event.chat_id) in waiting_verification:
                if event.message.media != None:
                    if str(event.message.media).startswith('MessageMediaContact(phone_number='):
                        reward_user, identity = waiting_verification.get(str(event.chat_id)).get('user_to_reward'), f'+{event.message.media.phone_number}'
                        referralby = cursor.execute(f"SELECT * FROM bot_users WHERE user_id={reward_user}").fetchall()

                        bot_data_db = cursor.execute(f"SELECT * FROM bot_settings WHERE setting_id = 1").fetchone()

                        reward_amount_dollar = float(bot_data_db[1])
                        reward_amount_credits = reward_amount_dollar * 10
                        new_invites, new_credits = int(referralby[0][3]) + 1, float(referralby[0][2]) + reward_amount_credits
                        
                        update_invites = cursor.execute(f"UPDATE bot_users SET invites = {new_invites} WHERE user_id={reward_user};")
                        update_credits = cursor.execute(f"UPDATE bot_users SET credits = {new_credits} WHERE user_id={reward_user};")
                        update_identity = cursor.execute(f"UPDATE bot_users SET identity = '{identity}' WHERE user_id={event.chat_id};")
                        
                        commit = await CommitDatabase(database)
                        try:
                            inform_user = await event.client.send_message(entity=reward_user, message=f'__🎉 You have received a reward of {reward_amount_credits} Credit ( ${reward_amount_dollar} ) for inviting a friend__')
                        except:pass
                        remove_user = waiting_verification.pop(str(event.chat_id))
                        
                        await save_as_json(waiting_verification, "waiting_verification.json"), await bot_menu(event, database, cursor, owner_id)
                    else:
                        await event.reply("__We couldn't process your message. Please verify your identity by sharing your phone number to use this bot__")
                else:
                    await event.reply("__We couldn't process your message. Please verify your identity by sharing your phone number to use this bot__")
            else:
                if (event.text).startswith('/start'):
                    await DeleteEvent(event)

                    bot_data_db = cursor.execute(f"SELECT * FROM bot_settings WHERE setting_id = 1").fetchone()
                    if bot_data_db == None:
                        cursor.execute("""
                            INSERT INTO bot_settings (setting_id, link_reward, daily_cancel_limit)
                            VALUES (?, ?, ?)
                        """, (1, '0.01', 10))
                        database.commit()

                    if bot_data_db[2] == None:
                        cursor.execute(f"UPDATE bot_settings SET daily_cancel_limit = 10 WHERE setting_id = 1")
                        database.commit()


                    get_user = cursor.execute(f"SELECT * FROM bot_users WHERE user_id={event.chat_id}").fetchall()
                    if len(get_user) == 0:
                        user_entity = await bot.get_entity(event.chat_id)
                        register_date = datetime.datetime.now().date()
                        
                        add_user, commit = cursor.execute(f"INSERT INTO bot_users VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (event.chat_id, f'@{user_entity.username}', 0, 0, 'english', None, None, 1, str(idx).replace("'", '"'), 0, 0, 0, 0, str(register_date), user_entity.first_name, user_entity.last_name)), await CommitDatabase(database)
                        if (event.text).replace('/start', '').strip() != '':
                            try:
                                referralby_id = int((event.text).replace('/start', '').strip())
                                if referralby_id != event.chat_id:
                                    referralby = cursor.execute(f"SELECT * FROM bot_users WHERE user_id={referralby_id}").fetchall()
                                    if len(referralby) != 0:
                                        try:
                                            total_invites = int(referralby[0][10]) + 1
                                            update_total_invites = cursor.execute(f"UPDATE bot_users SET total_invites = {total_invites} WHERE user_id={referralby_id};")
                                            update_inviteBY, commit = cursor.execute(f"UPDATE bot_users SET invitedBY = {referralby_id} WHERE user_id={event.chat_id};"), await CommitDatabase(database)
                                            if referralby_id not in waiting_verification:
                                                waiting_verification[str(event.chat_id)] = {
                                                    "user_to_verify": event.chat_id,
                                                    "user_to_reward": referralby_id
                                                }
                                            await save_as_json(waiting_verification, "waiting_verification.json"), await verification_proccess(event)
                                        except Exception as error: # ERROR ACTION : #000
                                            record = await record_an_error(f'[ NEW ERROR RECORD ] -- [ USER_ID : {event.chat_id} ] -- [ ERROR ACTION : #000 ] -- [ RECORDED ERROR : {error} ]')
                                
                            except Exception as error: # ERROR ACTION : #001
                                record = await record_an_error(f'[ NEW ERROR RECORD ] -- [ USER_ID : {event.chat_id} ] -- [ ERROR ACTION : #001 ] -- [ RECORDED ERROR : {error} ]')

                    else:
                        if (event.text).replace('/start', '').strip() != '':
                            try:
                                referralby_id = int((event.text).replace('/start', '').strip())                
                            except Exception as error: # ERROR ACTION : #002
                                record = await record_an_error(f'[ NEW ERROR RECORD ] -- [ USER_ID : {event.chat_id} ] -- [ ERROR ACTION : #002 ] -- [ RECORDED ERROR : {error} ]')

                    if str(event.chat_id) not in waiting_verification:
                        # run = await bot_menu(event, database, cursor, owner_id)
                        choose_lang = await change_lang(event, event.chat_id)
						
                    # await SendDatabase(event)
                    
				# Owner Keyboard
                elif event.text == "لوحة الأدمن":
                    await DeleteEvent(event)
                    await OwnerKeyboard(event, owner_id)

                # contact support
                elif event.text == "📞 ᴄᴏɴᴛᴀᴄᴛ ꜱᴜᴘᴘᴏʀᴛ" or event.text == "📞 اتصل بالدعم الفني":
                    await DeleteEvent(event)
                    try:
                        await ContactSupport(event, cursor, database, CommitDatabase, DateTimeNow, owner_id)
                    except Exception as error:
                        await event.respond('__Please send /start in order to update this bot for you__')
                
                # my account
                elif event.text == "⚙️ ᴍʏ ᴀᴄᴄᴏᴜɴᴛ" or event.text == "⚙️ حســابي":
                    await DeleteEvent(event)
                    try:
                        await MyAccount(event, database, cursor)
                    except Exception as error:
                        await event.respond('__Please send /start in order to update this bot for you__')
                    
                # buy a number
                elif event.text == "☎️ ʙᴜʏ ᴀ ɴᴜᴍʙᴇʀ" or event.text == "☎️ اشتري رقم":
                    await DeleteEvent(event)
                    try:
                        await Services_List(event, database, cursor, CommitDatabase)
                    except Exception as error:
                        await event.respond('__Please send /start in order to update this bot for you__')
                    
                # socail mediia services
                elif event.text == "📈 ꜱᴏᴄɪᴀʟ ᴍᴇᴅɪᴀ ꜱᴇʀᴠɪᴄᴇꜱ" or event.text == "📈 خدمات وسائل التواصل الاجتماعي":
                    user_lang = await get_user_lang(event, database, cursor)
                    await event.respond(f'__{bot_lang[user_lang]["error1"]}__')
                    
                elif event.text == "/developer":
                    await event.reply('__This bot was developer by @krypton_ksa__')
                    
                # deposit
                # elif event.text == "📥 ᴅᴇᴘᴏꜱɪᴛ" or event.text == "📥 الإيداع" or event.text == "💰 ᴛᴏᴘ ᴜᴘ" or event.text == "💰 شحن":
                #     user_lang = await get_user_lang(event, database, cursor)
                #     buttons = [
				# 		[
				# 			Button.inline('10 USD ( 100 Credit )', 'CreateInvoice_10'), 
				# 			Button.inline('20 USD ( 200 Credit )', 'CreateInvoice_20')
				# 		],
				# 		[
				# 			Button.inline('30 USD ( 300 Credit )', 'CreateInvoice_30'),
				# 			Button.inline('40 USD ( 400 Credit )', 'CreateInvoice_40')
				# 		],
				# 		[
				# 			Button.inline('50 USD ( 500 Credit )', 'CreateInvoice_50'),
				# 			Button.inline('100 USD ( 1000 Credit )', 'CreateInvoice_100')
				# 		],
				# 		[
				# 			Button.inline('200 USD ( 2000 Credit )', 'CreateInvoice_200'),
				# 			Button.inline('300 USD ( 3000 Credit )', 'CreateInvoice_300')
				# 		],
				# 		[
				# 			Button.inline('400 USD ( 4000 Credit )', 'CreateInvoice_400'),
				# 			Button.inline('500 USD ( 5000 Credit )', 'CreateInvoice_500')
				# 		],
				# 		[
				# 			Button.inline('1000 USD ( 10000 Credit )', 'CreateInvoice_1000'),
				# 		],
				# 		[
				# 			Button.inline(f'{bot_lang[user_lang]["btn2"]}', 'back_to_menu')
				# 		]
				# 	]
					
                #     await event.reply(f'__{bot_lang[user_lang]["message2"]}__', buttons=buttons)
                
				# my activity log
                elif event.text == "🗂️ ᴍʏ ᴀᴄᴛɪᴠɪᴛʏ ʟᴏɢ" or event.text == "🗂️ سجل نشاطي":
                    # await event.respond('__This section is not available yet__')
                    user_lang = await get_user_lang(event, database, cursor)
                    await event.respond(f'__{bot_lang[user_lang]["error1"]}__')
                    
                # back to menu
                elif event.text == "❌ ʙᴀᴄᴋ ᴛᴏ ᴍᴇɴᴜ" or event.text == "❌ الرجوع للقائمة الرئيسية":
                    await DeleteEvent(event)
                    menu = await bot_menu(event, database, cursor, owner_id)

				# send database
                elif event.text == "/send_database" or event.text == "/database":
                    if event.chat_id == owner_id:
                        await event.respond('__sending...__'), await SendDatabase(event)






# BOT COMMING CALLBACKs
@bot.on(events.CallbackQuery)
async def CommingCallbacks(event):
    global banned_users

    banned_users = json.load(open('banned_users.json'))
    message_data, user_id = str((event.data).decode()), event.query.user_id

    user_lang = await get_user_lang(event, database, cursor)
    if event.is_private:
        if event.chat_id not in banned_users.get("banned_users"):
            if message_data == "btn1":
                await DeleteEvent(event)
                try:
                    await Services_List(event, database, cursor, CommitDatabase)
                except Exception as error:
                    await event.respond('__Please send /start in order to update this bot for you__')
                    

            elif message_data == "btn2" or message_data == "back_to_smmList":
                await DeleteEvent(event)
                try:
                    await SmmServices_List(event, database, cursor, CommitDatabase)
                except Exception as error:
                    print (error)
                    await event.respond('__Please send /start in order to update this bot for you__')
                

            elif str(message_data).startswith('smmShow_'):
                smm_type = str(message_data).replace('smmShow_','').strip()
                await DeleteEvent(event), await SmmShowServices(event, smm_type, database, cursor)
                

            elif str(message_data).startswith('smmInfo_'):
                service_id = str(message_data).replace('smmInfo_','').strip()
                await DeleteEvent(event), await SmmShowServiceInfo(event, service_id, database, cursor)
                
			
            elif str(message_data).startswith('smmBuy_'):
                service_id = str(message_data).replace('smmBuy_','').strip()
                await DeleteEvent(event), await SmmBuyService(event, service_id, database, cursor)
                

            elif str(message_data).startswith('smmOrderView_'):
                smm_orderID = str(message_data).replace('smmOrderView_','').strip()
                await DeleteEvent(event), await SmmViewOrderInfo(event, database, cursor, smm_orderID)

			
            elif message_data == "btn3":
                await DeleteEvent(event)
                try:
                    await ContactSupport(event, cursor, database, CommitDatabase, DateTimeNow, owner_id)
                except Exception as error:
                    await event.respond('__Please send /start in order to update this bot for you__')
                    
			
            elif message_data == "btn4":
                await DeleteEvent(event)
                try:
                    await MyAccount(event, database, cursor)
                except Exception as error:
                    await event.respond('__Please send /start in order to update this bot for you__')
				

            elif message_data == "btn6":
                user_lang = await get_user_lang(event, database, cursor)
                # await DeleteEvent(event)
                await ShowSmmRecordOrders(event, database, cursor, 0)
                
            elif message_data.startswith('backSmm_'):
                order_index = int(message_data.split('_')[1]) - 1  # Previous order
                # await DeleteEvent(event)
                await ShowSmmRecordOrders(event, database, cursor, order_index)
			
            elif message_data.startswith('nextSmm_'):
                order_index = int(message_data.split('_')[1]) + 1  # Next order
                # await DeleteEvent(event)
                await ShowSmmRecordOrders(event, database, cursor, order_index)
						
					
            elif message_data == "admin_owner":
                await DeleteEvent(event)
                await OwnerKeyboard(event, owner_id)


            elif message_data == "change_lang":
                await DeleteEvent(event), await change_lang(event, user_id)
                
            elif message_data == "lang_english":
                update_lang, commit = cursor.execute(f"UPDATE bot_users SET lang = 'english' WHERE user_id={user_id};"), await CommitDatabase(database)
                await pin_animation(event, '✅ Language selected : English'), await DeleteEvent(event), await bot_menu(event, database, cursor, owner_id) #, await MyAccount(event, database, cursor)
            elif message_data == "lang_arabic":
                update_lang, commit = cursor.execute(f"UPDATE bot_users SET lang = 'arabic' WHERE user_id={user_id};"), await CommitDatabase(database)
                await pin_animation(event, '✅ اللغة المختارة : العربية'), await DeleteEvent(event), await bot_menu(event, database, cursor, owner_id) #, await MyAccount(event, database, cursor)


            elif message_data == "section1_next":
                await next_page(event, database, cursor, CommitDatabase)
            elif message_data == "section1_back":
                await back_page(event, database, cursor, CommitDatabase)


            elif str(message_data).startswith('service_'):
                service_id = str(message_data).replace('service_','').strip()
                await DeleteEvent(event), await show_numbers(event, service_id, database, cursor, idx)

            
            elif str(message_data).startswith('countrySearch_'):
                service_id = str(message_data).replace('countrySearch_','').strip()
                await DeleteEvent(event)
                
                try:
                    async with event.client.conversation(event.chat_id, timeout=120) as conv:
                        await conv.send_message(f"{bot_lang[user_lang]['message101']}")
                        message = await conv.get_response()
                        
                    await Search_numbers_List(event, database, cursor, CommitDatabase, service_id, str(message.text).lower())
                except Exception as error:
                    print(f'searching country error: {error}')
                    try:
                        await show_numbers(event, service_id, database, cursor, idx)
                    except Exception as error:
                        await event.respond('__Please send /start in order to update this bot for you__')

            
            elif str(message_data).startswith('backToCountriesList_'):
                service_id = str(message_data).replace('backToCountriesList_','').strip()
                await DeleteEvent(event), await show_numbers(event, service_id, database, cursor, idx)

				
            elif str(message_data).startswith('section2_next'):
                service_id = str(message_data).split("_")[2]
                await show_numbers_next(event, service_id, database, cursor)
            elif str(message_data).startswith('section2_back'):
                service_id = str(message_data).split("_")[2]
                await show_numbers_back(event, service_id, database, cursor)
			
			
            elif message_data == "back_to_services_list":
                await DeleteEvent(event), await Services_List(event, database, cursor, CommitDatabase)
            
            elif message_data == "close_this_list":
                await DeleteEvent(event)
                menu = await bot_menu(event, database, cursor, owner_id)
                
            elif message_data == "section1_current_page":
                await all_pages_section_1(event, cursor)

            elif message_data == "back_to_services":
                await DeleteEvent(event)
                try:
                    await Services_List(event, database, cursor, CommitDatabase)
                except Exception as error:
                    await event.respond('__Please send /start in order to update this bot for you__')

            elif message_data == "services_search":
                await DeleteEvent(event)

                try:
                    async with event.client.conversation(event.chat_id, timeout=120) as conv:
                        await conv.send_message(bot_lang[user_lang]["message97"])
                        message = await conv.get_response()
                        
                    await Search_Services_List(event, database, cursor, CommitDatabase, str(message.text))
                except Exception as error:
                    print(f'searching services error: {error}')
                    try:
                        await Services_List(event, database, cursor, CommitDatabase)
                    except Exception as error:
                        await event.respond('__Please send /start in order to update this bot for you__')
            
            elif str(message_data).startswith('go_to'):
                delete, page_group_id = await DeleteEvent(event), str(message_data).replace("go_to_", "")
                await go_to_page(event, cursor, database, page_group_id, CommitDatabase)


            elif str(message_data).startswith('buy_'):
                clean_message = (str(message_data).replace('buy_','')).split('_')
                service_id, country_code, purchased_at = clean_message[0], int(clean_message[1]), await DateTimeNow()
                try:
                    await event.answer(bot_lang[user_lang]["message3"]), await DeleteEvent(event), await selected_number(event, service_id, country_code, database, cursor, str(purchased_at))
                except Exception as error: # ERROR ACTION : #004
                    record = await record_an_error(f'[ NEW ERROR RECORD ] -- [ USER_ID : {user_id} ] -- [ ERROR ACTION : #004 ] -- [ RECORDED ERROR : {error} ]')
	
                await SendDatabase(event)


            elif str(message_data).startswith('MoreTime_'):
                order_id = str(message_data).replace('MoreTime_', '')
                reg_time, exrta_count = datetime.datetime.now().time(), cursor.execute(f"SELECT * FROM orders_reg_time WHERE order_id = {order_id}").fetchall()[0][2]
                if int(exrta_count) == 1:
                    await event.answer(bot_lang[user_lang]["message4"], alert=True)
                else:
                    new_reg_time = await add_time_registered(reg_time, 900)
                    update_reg_time = cursor.execute(f"UPDATE orders_reg_time SET reg_time = '{str(new_reg_time).split('.')[0]}' WHERE order_id = {order_id}")
                    update_exrta_time = cursor.execute(f"UPDATE orders_reg_time SET exrta_time = '{int(exrta_count) + 1}' WHERE order_id = {order_id}")
                    user_info = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = '{user_id}'").fetchall()[0]
                    user_balance = user_info[2]
                    new_credits = round(float(user_balance) - float(1), 2)
                    update = await update_user_credits(event, new_credits, database, cursor)
                    order_change_time = str(datetime.datetime.now()).split('.')[0]
                    INSERT = cursor.execute(f"INSERT INTO extra_time_added VALUES (?,?,?,?,?,?)", (order_id, user_id, user_balance, new_credits, 15, str(order_change_time)))
					
                    database.commit(), await event.answer(bot_lang[user_lang]["message4"], alert=True)


            elif str(message_data).startswith('RequestAnother_'):
                await DeleteEvent(event)
                order_id = str(message_data).replace('RequestAnother_', '').split('_')[0]		
                service_id = str(message_data).replace('RequestAnother_', '').split('_')[1]
                country_code = str(message_data).replace('RequestAnother_', '').split('_')[2]
                
                service_name = await get_service(service_id, database, cursor)
                
                order_info = cursor.execute(f"SELECT * FROM orders_recorded WHERE order_id = {order_id}").fetchall()[0]
                service_price = order_info[2]
                service_price_dollar = order_info[3]
                
                user_info = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = '{user_id}'").fetchall()[0]
                user_balance = user_info[2]
                
                country_info = cursor.execute(f"SELECT * FROM country_numbes WHERE country_code = '{country_code}'").fetchall()[0]
                country_name = country_info[1]
                country_flag = country_info[2]
                country_phone_code = country_info[3]
                
                phone_number = str(order_info[9]).replace("+", "")
                
                reg_info = cursor.execute(f"SELECT * FROM orders_reg_time WHERE order_id = {order_id}").fetchall()[0]
                timeleft = reg_info[1]
                order_status = None
                
                try:
                    add_request, commit = cursor.execute(f"INSERT INTO another_sms_request VALUES (?,?,?,?,?)", (order_id, str(user_id), service_id, str(datetime.datetime.now()).split('.')[0], timeleft)), database.commit()
                    await request_another_sms(event, database, cursor, order_id, service_id, service_name, service_price, service_price_dollar, user_balance, country_name, country_flag, country_phone_code, phone_number, timeleft, country_code, record_an_error)
                except Exception as error: # ERROR ACTION : #003
                    record = await record_an_error(f'[ NEW ERROR RECORD ] -- [ USER_ID : {user_id} ] -- [ ERROR ACTION : #003 ] -- [ RECORDED ERROR : {error} ]')
			
				
            elif message_data == "back_to_menu":
                await DeleteEvent(event)
                menu = await bot_menu(event, database, cursor, owner_id)

            elif message_data == "back_to_adminPanel":
                await DeleteEvent(event)
                await OwnerKeyboard(event, owner_id)

            elif message_data == "back_to_adButtons":
                await DeleteEvent(event)
                await AD_Button(event)

            elif message_data == "back_to_sub":
                await DeleteEvent(event)
                await VIP_SHOW(event)

                
            elif str(message_data).startswith('AdminReply_'):
                user_id = int(str(message_data).split('_')[1])
                
                async with event.client.conversation(event.chat_id) as conv:
                    await conv.send_message('Send Your Reply :')
                    message = await conv.get_response()
                    
                try:
                    await bot.send_message(entity=user_id, message=message)
                    await event.reply('__Message Sent__')
                except Exception as error:await event.reply(f'__ERROR : {error}__')
					
            elif message_data == "ShowInvoiceAmount" or message_data == "btn5":
                await DeleteEvent(event)

                vip_subscription = cursor.execute("SELECT * FROM vip_subscription WHERE status = 'active'")
                vip_subscription  = cursor.fetchall()

                buttons = []
                for i in range(0, len(vip_subscription), 2):
                    row = []
                    row.append(Button.inline(f'{vip_subscription[i][1]} USD ( {float(vip_subscription[i][1]) * 10} Credit )', f'PreCreateInvoice_{vip_subscription[i][1]}'))
                    if i + 1 < len(vip_subscription):
                        row.append(Button.inline(f'{vip_subscription[i+1][1]} USD ( {float(vip_subscription[i+1][1]) * 10} Credit )', f'PreCreateInvoice_{vip_subscription[i+1][1]}'))
                    buttons.append(row)

                buttons.append([Button.inline(f'{bot_lang[user_lang]["btn2"]}', 'back_to_menu')])
                
                # buttons = [
                #     [
                #         Button.inline('10 USD ( 100 Credit )', 'CreateInvoice_10'), 
                #         Button.inline('20 USD ( 200 Credit )', 'CreateInvoice_20')
                #     ],
                #     [
                #         Button.inline(f'{bot_lang[user_lang]["btn2"]}', 'back_to_menu')
				# 	]
				# ]
                
                await event.reply(f'__{bot_lang[user_lang]["message2"]}__', buttons=buttons)
                

            elif str(message_data).startswith('PreCreateInvoice_'):
                await DeleteEvent(event)
                price_in_dollar = float(str(message_data).split('_')[1])

                buttons = [
                    [Button.inline(f'{bot_lang[user_lang]["btn19"]}', f'Discount_{price_in_dollar}')],
                    [Button.inline(f'{bot_lang[user_lang]["btn20"]}', f'CreateInvoice_{price_in_dollar}')],
                    [Button.inline(f'{bot_lang[user_lang]["btn2"]}', 'back_to_menu')]
                ]

                gen_msg = await event.reply(f'''__
{bot_lang[user_lang]["message91"]}

{bot_lang[user_lang]["btn1"]}: {price_in_dollar}$
__''', buttons=buttons)


            elif str(message_data).startswith('Discount_'):

                await DeleteEvent(event)
                price_in_dollar = float(str(message_data).split('_')[1])
                update_msg, coupon_used = '', False

                try:
                    async with bot.conversation(event.chat_id, timeout=120) as conv:
                        await conv.send_message(f'__{bot_lang[user_lang]["message92"]}__')
                        code = (await conv.get_response()).message

                    offer_data = cursor.execute(f"SELECT * FROM limited_offer WHERE offer_code = '{code}'")
                    offer_data = cursor.fetchone()

                    if offer_data == None:
                        update_msg = f'{bot_lang[user_lang]["message93"]}'
                    else:
                        if offer_data[7] == 'unactive':
                            update_msg = f'{bot_lang[user_lang]["message94"]}'
                        else:
                            target_date = datetime.datetime.strptime(str(offer_data[6]), "%Y-%m-%d %H:%M:%S")
                            current_time = datetime.datetime.now()

                            # Calculate the time difference
                            time_difference = target_date - current_time
                            if time_difference.total_seconds() > 0:
                                price_in_dollar = float(price_in_dollar) * (1 - float(offer_data[3]) / 100)
                                update_msg = f'{bot_lang[user_lang]["message95"]} {offer_data[3]}%'
                                coupon_used = True

                                cursor.execute(f"UPDATE limited_offer SET usage_count = {int(offer_data[8]) + 1} WHERE id = {offer_data[0]}")
                                database.commit()
                            else:
                                update_msg = f'{bot_lang[user_lang]["message94"]}'
                                cursor.execute(f"UPDATE limited_offer SET status = 'unactive' WHERE id = {offer_data[0]}")
                                database.commit()

                except Exception as error:pass

                user_data = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {event.chat_id}")
                user_data = cursor.fetchone()

                buttons = []

                if coupon_used == False:
                    buttons.append([Button.inline(f'{bot_lang[user_lang]["btn19"]}', f'Discount_{price_in_dollar}')])
                
                buttons.append([Button.inline(f'{bot_lang[user_lang]["btn20"]}', f'CreateInvoice_{price_in_dollar}')])
                buttons.append([Button.inline(f'{bot_lang[user_lang]["btn2"]}', 'back_to_menu')])


                gen_msg = await event.reply(f'''__
{bot_lang[user_lang]["message91"]}

{bot_lang[user_lang]["btn2"]}: {price_in_dollar}$

{update_msg}
__''', buttons=buttons)



            elif str(message_data).startswith('CreateInvoice_'):
                await DeleteEvent(event)
                gen_msg = await event.reply(f'__{bot_lang[user_lang]["message6"]}__')
                
                amount = float(str(message_data).split('_')[1])
                amount_inSAR = float(str(message_data).split('_')[1]) * 3.76 # FROM USD TO SAR
                credits_amount = amount * 10
                
                # invoice = await create_invoice(amount)
                invoice = await create_invoice_myfatoorah(amount_inSAR, event.chat_id)
                await event.reply(f'''
{bot_lang[user_lang]["message7"]}

{bot_lang[user_lang]["message8"]} {invoice[0]}
{bot_lang[user_lang]["message9"]}({invoice[1]})

{bot_lang[user_lang]["message10"]} ( ${amount} ), {bot_lang[user_lang]["message11"]}
''', buttons=[
	[Button.url(f'{bot_lang[user_lang]["btn3"]}', invoice[1])]
])
                
                try:
                    await gen_msg.delete()
                except Exception as error:pass
                
                try:
                    notice_admin = await bot.send_message(
                        entity=owner_id,
                        message=f'''
__مستخدم أنشئ فاتورة

ايدي المستخدم : {event.chat_id}
رقم الفاتورة : {invoice[0]} 
رابط الدفع : {invoice[1]}
الرصيد : ${amount}__
''')
                except Exception as error:pass

                counter = 0
                while True:
                    # check_paid = await check_invoice_paid(invoice[0])
                    check_paid = await check_invoice_status_myfatoorah(invoice[0])
                    if check_paid[0] == False:
                        await asyncio.sleep(120)
                        counter += 120
                    else:
                        user = cursor.execute(f"SELECT * FROM bot_users WHERE user_id={event.chat_id}").fetchone()
                        new_credits = round((float(user[2]) + float(credits_amount)), 2)

                        cursor.execute(f"UPDATE bot_users SET credits = {new_credits} WHERE user_id={event.chat_id}")
                        database.commit()
                        

                        # Add To History
                        user_id = event.chat_id
                        invoice_id = str(invoice[0])
                        invoice_link = invoice[1]
                        paid_subscription_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        subscription_price = str(amount)

                        insert_query = """
                            INSERT INTO subscription_history (
                                user_id,
                                invoice_id,
                                invoice_link,
                                paid_subscription_at,
                                subscription_price
                            ) VALUES (?, ?, ?, ?, ?);
                        """
                        cursor.execute(insert_query, (user_id, invoice_id, invoice_link, paid_subscription_at, subscription_price))
                        database.commit()


                        notice_user = await event.reply(
                            message=f'''
{bot_lang[user_lang]["message12"]}

{bot_lang[user_lang]["message13"]} ( ${amount} - {credits_amount} credits ) {bot_lang[user_lang]["message14"]}''', buttons=[[Button.inline(f'{bot_lang[user_lang]["btn2"]}', 'back_to_menu')]])
                        
                        notice_admin = await bot.send_message(
                            entity=owner_id,
                            message=f'''
__تم دفع الفاتورة بنجاح

ايدي المستخدم : {event.chat_id}
رقم الفاتورة : {invoice[0]}
الرصيد : {amount}$ - {credits_amount}__
''')
                        
                        break
                    
                    if counter >= 3600:
                        await event.reply(f'''
{bot_lang[user_lang]["message15"]}
''', buttons=[[Button.inline(f'{bot_lang[user_lang]["btn2"]}', 'back_to_menu')]])
                        break
                





################ ADMIN CALLBACKS ####################
# Most Buyer
@bot.on(events.CallbackQuery(data='most_buyer')) 
async def most_buyer(event):

    await DeleteEvent(event)
    msg = await event.respond('__انتظر قليلا...__')

    # Execute the query
    cursor.execute("""
        SELECT user_id, successful_sales
        FROM bot_users
        ORDER BY successful_sales DESC
        LIMIT 10;
    """)

    # Fetch the results
    results = cursor.fetchall()

    message = f'**أكثر الأشخاص قاموا بالشراء**\n\n'
    for row in results:
        user_id, search_count = row

        try:
            get_data = await bot.get_entity(int(user_id))
            if get_data.username == None:
                username = 'غير معروف'
            else:
                username = f'@{get_data.username}'
        except:username = 'غير معروف'

        message += f'''
✨ الايدي: `{user_id}`
👤 المعرف : {username}
🛒 عدد عمليات الشراء: {search_count}
👤 زيارة المستخدم: [اضغط هنا](tg://user?id={user_id})
'''


    await DeleteEvent(msg)

    buttons = [[Button.inline('🔙 رجوع', 'back_to_adminPanel')]]
    await event.respond(message, buttons=buttons, parse_mode='markdown')



# Last Sold Products
@bot.on(events.CallbackQuery(data='last_sold_products')) 
async def last_sold_products(event):

    await DeleteEvent(event)
    msg = await event.respond('__انتظر قليلا...__')

    # Execute the query
    cursor.execute("""
        SELECT * 
        FROM orders_recorded
        WHERE action_status = 'Success'
        ORDER BY purchased_at DESC
        LIMIT 10;
    """)
    results = cursor.fetchall()

    message = f'**اخر 10 أشخص قاموا بالشراء:**\n\n'
    # Process the results
    for row in results:
        message += f'''
✨ الايدي: `{row[1]}`
🛒 الخدمة: {row[7]}
☎ الرقم: {row[9]}
🕒 تاريخ الشراء: {row[11]}
👤 زيارة المستخدم: [اضغط هنا](tg://user?id={row[1]})
'''


    await DeleteEvent(msg)

    buttons = [[Button.inline('🔙 رجوع', 'back_to_adminPanel')]]
    await event.respond(message, buttons=buttons, parse_mode='markdown')




# Last Sold SMM
@bot.on(events.CallbackQuery(data='last_sold_smm')) 
async def last_sold_smm(event):

    await DeleteEvent(event)
    msg = await event.respond('__انتظر قليلا...__')

    # Execute the query
    cursor.execute("""
        SELECT * 
        FROM record_smm_services
        WHERE created_by != 978571497
        ORDER BY id DESC
        LIMIT 10;
    """) # ORDER BY purchased_at DESC
    results = cursor.fetchall()

    message = f'**اخر 10 أشخص قاموا بالشراء SMM:**\n\n'
    # Process the results
    for row in results:
        service_name = ""
        for service in smm_services["arabic"]:
            if service["service"] == str(row[2]):
                service_name = service["name"]
            
        message += f'''
🆔 الايدي: `{row[1]}`
🛒 الخدمة: {service_name}
💰 السعر: {float(row[3]) / 10}$
🔗 الرابط: {row[4]}
📦 الكمية: {row[5]}
👤 زيارة المستخدم: [اضغط هنا](tg://user?id={row[1]})
'''


    await DeleteEvent(msg)

    buttons = [[Button.inline('🔙 رجوع', 'back_to_adminPanel')]]
    await event.respond(message, buttons=buttons, parse_mode='markdown')


# # GET USERS
# def get_users(offset, limit):
#     cursor.execute("SELECT * FROM bot_users LIMIT ? OFFSET ?", (limit, offset))
#     return cursor.fetchall()

def get_users(offset, limit):
    cursor.execute(
        """
        SELECT * FROM (
            SELECT *, ROW_NUMBER() OVER () AS row_num FROM bot_users
        ) AS numbered
        ORDER BY row_num DESC
        LIMIT ? OFFSET ?
        """,
        (limit, offset)
    )
    return cursor.fetchall()




# STATISTICS
@bot.on(events.CallbackQuery(data='all_statistics')) 
async def AllStatistics(event):

    await DeleteEvent(event)

    user_data = cursor.execute(f"SELECT * FROM bot_users")
    user_data = cursor.fetchall()

    user_data_banned = json.load(open('banned_users.json')) # cursor.execute(f"SELECT * FROM bot_users WHERE banned = 'YES'")
    # user_data_banned = cursor.fetchall()

    user_data_not_banned = len(user_data) - len(user_data_banned['banned_users']) # cursor.execute(f"SELECT * FROM bot_users WHERE banned IS NULL")
    # user_data_not_banned = cursor.fetchall()


    today = datetime.datetime.now()
    today_formatted = today.strftime("%Y-%m-%d")

    cursor.execute("SELECT * FROM bot_users WHERE DATE(register_date) = ?", (today_formatted,))
    date_users_today = cursor.fetchall()

    cursor.execute("SELECT * FROM orders_recorded WHERE DATE(purchased_at) = ?", (today_formatted,))
    date_users_today_search_today = cursor.fetchall()

    cursor.execute("SELECT * FROM subscription_history WHERE DATE(paid_subscription_at) = ?", (today_formatted,))
    paid_subscription_today = cursor.fetchall()


    today_users_subscription = 0
    for sub in paid_subscription_today:
        today_users_subscription += float(sub[5])

    today_msg = len(date_users_today_search_today)
    for msg in date_users_today_search_today:
        today_msg += 1 #int(msg[5])


    yesterday = today - timedelta(days=1)
    yesterday_formatted = yesterday.strftime("%Y-%m-%d")
    
    cursor.execute("SELECT * FROM bot_users WHERE DATE(register_date) = ?", (yesterday_formatted,))
    date_users_yesterday = cursor.fetchall()

    cursor.execute("SELECT * FROM orders_recorded WHERE DATE(purchased_at) = ?", (yesterday_formatted,))
    date_users_today_search_yesterday = cursor.fetchall()

    cursor.execute("SELECT * FROM subscription_history WHERE DATE(paid_subscription_at) = ?", (yesterday_formatted,))
    paid_subscription_yesterday = cursor.fetchall()

    yesterday_users_subscription = 0
    for sub in paid_subscription_yesterday:
        yesterday_users_subscription += float(sub[5])

    yesterday_msg = len(date_users_today_search_yesterday)
    for msg in date_users_today_search_yesterday:
        yesterday_msg += 1 #int(msg[5])


    # Get current month
    current_month = today.strftime("%Y-%m")

    # Get users who joined in the current month
    cursor.execute("SELECT * FROM bot_users WHERE strftime('%Y-%m', register_date) = ?", (current_month,))
    date_users_current_month = cursor.fetchall()

    # Get previous month
    previous_month = (today.replace(day=1) - timedelta(days=1)).strftime("%Y-%m")

    # Get users who joined in the previous month
    cursor.execute("SELECT * FROM bot_users WHERE strftime('%Y-%m', register_date) = ?", (previous_month,))
    date_users_previous_month = cursor.fetchall()
 

    if event.chat_id not in page_data:
        page_data[event.chat_id] = 0

    users = get_users(page_data[event.chat_id], PAGE_SIZE)

    cursor.execute("SELECT COUNT(*) FROM bot_users")
    total_users = cursor.fetchone()[0]
    total_pages = math.ceil(total_users / PAGE_SIZE)
    current_page = (page_data[event.chat_id] // PAGE_SIZE) + 1


    buttons = [[Button.inline('🔎 بحث عن مستخدم', 'getUser_byID')]]

    for user in users:
        try:
            get_user_data = await bot.get_entity(int(user[0]))
            if get_user_data.username == None:
                username = ''
            else:
                username = f'( @{get_user_data.username} )'

            if user[14] == None:
                first_name = get_user_data.first_name
                last_name = get_user_data.last_name

                cursor.execute(
                    "UPDATE bot_users SET firstname = ?, lastname = ? WHERE user_id = ?",
                    (first_name, last_name, int(user[0]))
                )
                database.commit()

                if last_name == None:
                    firstlast_name = f'{first_name}'
                else:
                    firstlast_name = f'{first_name} {last_name}'

            else:
                if user[15] == None:
                    firstlast_name = f'{user[14]}'
                else:
                    firstlast_name = f'{user[14]} {user[15]}'
            
            buttons.append([Button.inline(f'{firstlast_name} {username}', f'getUserInfoID_{user[0]}')])
        except Exception as error:print (error)

    buttons.append([Button.inline("« الصفحة السابقة", data='previous_users'), Button.inline("الصفحة التالية »", data='next_users')])

    buttons.append([Button.inline('🔙 رجوع', 'back_to_adminPanel')])


    await event.respond(f'''
📊 مرحبًا بك في قسم الإحصائيات 📊

المستخدمون:
- 👥 العدد الإجمالي للمستخدمين: {len(user_data)}
- 👤 عدد المستخدمين في الخاص: {user_data_not_banned}
- 👥 عدد القنوات والمجموعات: {len(channels_list)}
- 🚫 عدد المحظورين: {len(user_data_banned)}

📅 الفعّالين:
اليوم ({today_formatted}):
- 👥 المستخدمون الجدد: {len(date_users_today)}
- 👥 المستخدمون الفعّالين: {len(date_users_today_search_today)}
- 💰 ربحية الشحن: {today_users_subscription}$
- ✉️ الرسائل: {today_msg}

الأمس ({yesterday_formatted}):
- 👥 المستخدمون الجدد: {len(date_users_yesterday)}
- 👥 المستخدمون الفعّالين: {len(date_users_today_search_yesterday)}
- 💰 ربحية الشحن: {yesterday_users_subscription}$
- ✉️ الرسائل: {yesterday_msg}

📅 المستخدمون الجدد:
- عدد المستخدمين الجدد خلال الشهر الحالي: {len(date_users_current_month)}
- عدد المستخدمين الجدد خلال الشهر الماضي: {len(date_users_previous_month)}

الصفحة: {current_page}/{total_pages}
''', buttons=buttons)




# Previous Users
@bot.on(events.CallbackQuery(data='previous_users')) 
async def PreviousUsers(event):
    user_id = event.chat_id

    # Initialize user's page if not set
    if user_id not in page_data:
        page_data[user_id] = 0

    # Adjust offset based on button
    if page_data[user_id] > 0:
        page_data[user_id] -= PAGE_SIZE

    await AllStatistics(event)



# Next Users
@bot.on(events.CallbackQuery(data='next_users')) 
async def NextUsers(event):
    user_id = event.chat_id

    # Initialize user's page if not set
    if user_id not in page_data:
        page_data[user_id] = 0

    # Adjust offset based on button
    page_data[user_id] += PAGE_SIZE

    # Fetch the users
    offset = page_data[user_id]
    users = get_users(offset, PAGE_SIZE)

    if not users:
        # If no more users, reset the page
        page_data[user_id] -= PAGE_SIZE
        await event.answer("لا يوجد المزيد")
        return
    
    await AllStatistics(event)


# Most Services Needed
@bot.on(events.CallbackQuery(data='most_services_needed')) 
async def MostServicesNeeded(event):

    await DeleteEvent(event)

    cursor.execute("""
        SELECT service_name, COUNT(service_name) AS purchase_count
        FROM orders_recorded
        GROUP BY service_name
        ORDER BY purchase_count DESC
        LIMIT 10;"""
    )
    top_10 = cursor.fetchall()

    message = f'**أكثر 10 خدمات طلبا للشراء ( الطلبات تشمل الناجحة و الفاشلة )**\n\n'
    for row in top_10:
        message += f'''__
🛒 الخدمة: {row[0]}
✨ الطلبات: {row[1]}
__'''
    

    buttons = []
    buttons.append([Button.inline('🔙 رجوع', 'back_to_adminPanel')])
    await event.respond(message, buttons=buttons)




# Most Numbers Needed
@bot.on(events.CallbackQuery(data='most_numbers_needed')) 
async def MostNumbersNeeded(event):

    await DeleteEvent(event)

    cursor.execute("""
        SELECT phone_number_country, COUNT(phone_number_country) AS purchase_count
        FROM orders_recorded
        GROUP BY phone_number_country
        ORDER BY purchase_count DESC
        LIMIT 10;"""
    )
    top_10 = cursor.fetchall()

    message = f'**أكثر 10 أرقام طلبا للشراء ( الطلبات تشمل الناجحة و الفاشلة )**\n\n'
    for row in top_10:
        message += f'''__
☎ دولة الرقم: {row[0]}
✨ الطلبات: {row[1]}
__'''
    

    buttons = []
    buttons.append([Button.inline('🔙 رجوع', 'back_to_adminPanel')])
    await event.respond(message, buttons=buttons)



# Edit Link Price
@bot.on(events.CallbackQuery(data='editLink_price')) 
async def EditLinkPrice(event):

    await DeleteEvent(event)
    bot_settings_data = cursor.execute('SELECT * FROM bot_settings WHERE setting_id = 1')
    bot_settings_data = cursor.fetchone()

    if event.chat_id == owner_id or event.chat_id == 978571497:
        await event.respond(f'''__
🎁 الجائزة الحالية:

سيحصل صاحب رابط الدعوة على **{bot_settings_data[1]}$** عند انضمام أي شخص عبر الرابط! 🌟
__''')
        
        try:
            buttons = [[Button.text('الغاء و الرجوع', resize=True)]]
            async with bot.conversation(event.chat_id, timeout=120) as conv:
                await conv.send_message('__أرسل الرصيد الذي تريد صاحب رابط الدعوة الحصول عليه بالدولار:__', buttons=buttons)
                price_in_dollar = (await conv.get_response()).message
                
            if price_in_dollar == 'الغاء و الرجوع':
                await hide_keyboard(event)
                await OwnerKeyboard(event, owner_id)
            else:
                try:
                    price_in_dollar = float(price_in_dollar)
                    cursor.execute(f"UPDATE bot_settings SET link_reward = '{price_in_dollar}' WHERE setting_id = 1")
                    database.commit()

                    await EditLinkPrice(event)
                except:
                    back_buttons= [[Button.inline('🔙 رجوع', 'back_to_adminPanel')]]
                    await event.reply('__الجائزة يجب أن تكون رقما!__', buttons=back_buttons)

        except:pass



# Edit Daily limits show
@bot.on(events.CallbackQuery(data='editDaily_limits_show')) 
async def EditDailyLimits_Show(event):

    await DeleteEvent(event)
    bot_settings_data = cursor.execute('SELECT * FROM bot_settings WHERE setting_id = 1')
    bot_settings_data = cursor.fetchone()

    if event.chat_id == owner_id or event.chat_id == 978571497:
        await event.respond(f'''__
✅ عدد الإلغاءات اليومية المسموح بها

⚠️ الإلغاءات اليومية المسموح بها لكل شخص: {bot_settings_data[2]}
__''')
        
        try:
            buttons = [[Button.text('الغاء و الرجوع', resize=True)]]
            async with bot.conversation(event.chat_id, timeout=120) as conv:
                await conv.send_message('__أرسل عدد الالغاءات اليومية لتعديلها:__', buttons=buttons)
                new_limit = (await conv.get_response()).message
                
            if new_limit == 'الغاء و الرجوع':
                await hide_keyboard(event)
                await OwnerKeyboard(event, owner_id)
            else:
                if str(new_limit).isdigit():
                    cursor.execute(f"UPDATE bot_settings SET daily_cancel_limit = '{new_limit}' WHERE setting_id = 1")
                    database.commit()

                    await EditDailyLimits_Show(event)
                else:
                    back_buttons= [[Button.inline('🔙 رجوع', 'back_to_adminPanel')]]
                    await event.reply(' عدد الالغاءات يجب أن تكون رقما!__', buttons=back_buttons)

        except:pass



# AD BUTTON
@bot.on(events.CallbackQuery(data='ad_buttons')) 
async def AD_Button(event):

    ad_buttons_data = cursor.execute('SELECT * FROM ad_buttons')
    ad_buttons_data = cursor.fetchall()
    await DeleteEvent(event)
    buttons = [
        [Button.inline('➕ اضافة زر', 'add_button'), Button.inline('🗑 حذف زر', 'delete_button')],
        [Button.inline('🔙 رجوع', 'back_to_adminPanel')]
    ]

    await event.respond(f'''__
✨ يمكنك اضافة أو حذف أزرار القنوات و المجموعات من هنا بكل سهولة!

عدد أزرار القنوات/المجموعات : {len(ad_buttons_data)}
__''', buttons=buttons)
    


# Add Buttons
@bot.on(events.CallbackQuery(data='add_button'))
async def AddButton(event):

    await DeleteEvent(event)
    try:
        async with bot.conversation(event.chat_id, timeout=120) as conv:
            await conv.send_message('__أرسل اسم الزر ( اسم الذي سيظهر على الزر  ):__')
            button_text = (await conv.get_response()).message

            await conv.send_message('__أرسل الرابط الذي تريد وضعه في الزر:__')
            button_link = (await conv.get_response()).message

        if str(button_link).startswith('https://'):
            cursor.execute(f"SELECT * FROM ad_buttons WHERE link = '{button_link}'")
            item_exists = cursor.fetchone()

            # Add the item if it doesn't exist
            if not item_exists:
                cursor.execute(
                    """
                    INSERT INTO ad_buttons 
                    (title, link) 
                    VALUES (?, ?)
                    """,
                    (button_text, button_link)
                )
                database.commit()

        else:
            await event.reply('__رابط الزر يجب أن يبدأ بـ https://__')

    except:pass
    await AD_Button(event)



# Delete  Buttons
@bot.on(events.CallbackQuery(data='delete_button'))
async def DeleteButton(event):

    await DeleteEvent(event)
    ad_buttons_data = cursor.execute('SELECT * FROM ad_buttons')
    ad_buttons_data = cursor.fetchall()
    
    buttons = []
    for item in ad_buttons_data:
        buttons.append([Button.inline(f'❌ {item[1]}', f'deleteButtonAD_{item[0]}')])

    buttons.append([Button.inline('🔙 رجوع', 'back_to_adButtons')])
    await event.respond('__اضغط على زر القناة أو الجروب لحذف ذالك الزر:__', buttons=buttons)



# Delete Button AD
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'deleteButtonAD_')))
async def DeleteButton_AD(event):
    
    # await DeleteEvent(event)
    id = int(str(event.data.decode()).replace('deleteButtonAD_', '').strip())
    ad_buttons_data = cursor.execute(f'SELECT * FROM ad_buttons WHERE id = {id}')
    ad_buttons_data = cursor.fetchone()

    if ad_buttons_data != None:
        cursor.execute(f'DELETE FROM ad_buttons WHERE id = {id}')
        database.commit()
    
    await DeleteButton(event)



# Get User by ID
@bot.on(events.CallbackQuery(data='getUser_byID')) 
async def GetUserbyID(event):

    await DeleteEvent(event)
    if event.chat_id == owner_id or event.chat_id == 978571497:
        try:
            async with bot.conversation(event.chat_id, timeout=120) as conv:
                await conv.send_message('__أرسل ايدي الشخص لعرض معلوماته:__')
                user_id = (await conv.get_response()).message
            
            if str(user_id).isdigit():
                await GetUserByID_(event, passed_user_id=user_id)
            else:
                await event.reply('__ايدي يجب أن يكون رقما!__')

        except:pass



# GET USER BY ID
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'getUserInfoID_')))
async def GetUserByID_(event, passed_user_id=None):

    await DeleteEvent(event)
    if passed_user_id == None:
        user_id = int(str(event.data.decode()).split('_')[1])
    else:
        user_id = passed_user_id

    try:
        bot_settings_data = cursor.execute('SELECT * FROM bot_settings WHERE setting_id = 1')
        bot_settings_data = cursor.fetchone()

        user_data = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {int(user_id)}")
        user_data = cursor.fetchone()

        if user_data == None:
            await event.respond('__الايدي الذي أرسلت لا ينتمي لأي مستخدم!__', buttons=[[Button.inline('🔙 رجوع', 'back_to_adminPanel')]])
            return

        last_sale = cursor.execute(f"""
            SELECT 
                purchased_by, 
                MAX(purchased_at) AS last_purchase_date
            FROM 
                orders_recorded
            WHERE 
                purchased_by = {int(user_id)}
            GROUP BY 
                purchased_by;
            """)

        last_sale = last_sale.fetchone()
        if last_sale == None:
            last_sale_date = None
        else:
            last_sale_date = last_sale[1]

        daily_cancels_limit = bot_settings_data[2]
        credits, added_date = user_data[2], user_data[13]
        total_success_sales, total_fail_sales = user_data[11], user_data[12]
        today_cancels = user_data[9]
        total_invites, active_invites = user_data[10], user_data[3]

        bot_me = await bot.get_me()
        refferal_link = f'https://t.me/{bot_me.username}?start={user_data[0]}'

        if user_data[15] == None:
            firstlast_name = f'{user_data[14]}'
        else:
            firstlast_name = f'{user_data[14]} {user_data[15]}'

        if user_data[6] == None:
            refferal_from = 'لا أحد'
        else:
            refferal_from = f'[اضغط لزيارة المستخدم](tg://user?id={user_data[6]})'

        banned_users = json.load(open('banned_users.json'))
        if user_data[0] not in banned_users['banned_users']:
            banned_text = '🚫 حظر'
        else:
            banned_text = '🔓 فك حظر'
        
        try:
            get_user_data = await bot.get_entity(int(user_id))
            if get_user_data.username == None:
                 url = f'tg://user?id={get_user_data.id}'
            else:
                url = f'https://t.me/{get_user_data.username}'
        except:url = f'tg://user?id={int(user_id)}'

        buttons = [
            [Button.url('💬 فتح محادثة', url), Button.inline('✏️ تعديل', f'OwnerEdit_{user_id}')],
            [
                Button.inline('🛒 عمليات الشراء', f'getRecordedHistory_{user_id}'),
                Button.inline('💳 سجل الشحن', f'getSubscription_{user_id}')
            ],
            [Button.inline('🛒 عمليات شراء SMM', f'getSmmHistory_{user_id}')],
            [Button.inline(banned_text, f'CheckBan_{user_id}'), Button.inline('🗑️ حذف', f'DeleteUser_{user_id}')],
            [Button.inline('🔄 تحديث', f'reffresh_{user_id}')],
            [Button.inline('🔙 رجوع', 'back_to_adminPanel')]
        ]

        notice_user = await event.reply(f'''__
✨ تفاصيل العميل

🆔 رقم المستخدم: {user_id}
👤 الاسم الكامل: {firstlast_name}
💳 الرصيد: {credits} Credits ( {round((float(credits) * 0.10), 2)}$ )

📆 تاريخ الانضمام: {added_date}
🔗 الإحالة من: {refferal_from}

🕒 تاريخ آخر عملية شراء: {last_sale_date}

📈 إجمالي المبيعات الناجحة: {total_success_sales}
📉 إجمالي المبيعات غير الناجحة: {total_fail_sales}
❌ الإلغاءات اليومية: {today_cancels}/{daily_cancels_limit}

👥 إجمالي الإحالات: {total_invites}
✅ الإحالات النشطة: {active_invites}
🔗 رابط الإحالة: {refferal_link}
__''', buttons=buttons)

    except Exception as error:
        notice_user = await event.reply(str(error))



# Reffresh
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'reffresh_')))
async def GetUserByID_reffresh(event):

    user_id = int(str(event.data.decode()).split('_')[1])
    await GetUserByID_(event, passed_user_id=user_id)




# Check Ban/Unban
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'CheckBan_')))
async def GetUserByID_CheckBan(event):

    user_id = int(str(event.data.decode()).split('_')[1])
    banned_users = json.load(open('banned_users.json'))
    banned_users_ = banned_users['banned_users']

    if user_id in banned_users_:
        banned_users_.remove(user_id)
        await event.answer('تم فك حظر المستخدم')
    else:
        banned_users_.append(user_id)
        await event.answer('تم حظر المستخدم')
    
    with open('banned_users.json', 'w') as file:
        json.dump({"banned_users": banned_users_}, file)

    await GetUserByID_(event, passed_user_id=user_id)


# Delete User
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'DeleteUser_')))
async def GetUserByID_DeleteUser(event):

    await DeleteEvent(event)
    user_id = int(str(event.data.decode()).split('_')[1])
    buttons = [
        [Button.inline('🗑️ تأكيد و حذف المستخدم', f'ConfirmDeleteUser_{user_id}')],
        [Button.inline('🔙 رجوع', f'getUserInfoID_{user_id}')]
    ]

    await event.respond(f'''__
هل أنت متأكد من حذف هذا المستخدم, سيتم حذف جميع معلوماته بالكامل
__''', buttons=buttons)



# Confirm Delete User
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'ConfirmDeleteUser_')))
async def GetUserByID_ConfirmDeleteUser(event):

    await DeleteEvent(event)
    user_id = int(str(event.data.decode()).split('_')[1])

    cursor.execute(f'DELETE FROM bot_users WHERE user_id = {int(user_id)}')
    database.commit()

    buttons = [
        [Button.inline('🔙 رجوع', 'back_to_adminPanel')]
    ]

    await event.respond('__تم حذف المستخدم و كامل معلوماته في البوت__', buttons=buttons)



# Owner Edit User
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'OwnerEdit_')))
async def GetUserByID_OwnerEdit(event, passed_user_id=None, extra_msg=''):

    await DeleteEvent(event)
    if passed_user_id == None:
        user_id = int(str(event.data.decode()).split('_')[1])
    else:
        user_id = passed_user_id

    buttons = [
        [Button.inline('✏️ الاسم الأول', f'OwnerEditName1_{user_id}'), Button.inline('✏️ الاسم الأخير', f'OwnerEditName2_{user_id}')],
        [Button.inline('🔙 رجوع', f'getUserInfoID_{user_id}')]
    ]

    await event.respond(f'''__
يمكنك تعديل اسم الأول و الأخير للمستخدم:

{extra_msg}
__''', buttons=buttons)



# EDIT NAME 1
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'OwnerEditName1_')))
async def GetUserByID_OwnerEditName1(event):

    await DeleteEvent(event)
    user_id = int(str(event.data.decode()).split('_')[1])

    try:
        async with bot.conversation(event.chat_id, timeout=120) as conv:
            await conv.send_message('__أرسل الاسم الأول لتحديثه:__')
            first_name = (await conv.get_response()).message

        cursor.execute("UPDATE bot_users SET firstname = ? WHERE user_id = ?", (first_name, user_id,))
        database.commit()

        await GetUserByID_OwnerEdit(event, passed_user_id=user_id, extra_msg='__✅ تم تعديل الاسم الأول للمستخدم بنجاح__')
    
    except:await GetUserByID_(event, passed_user_id=user_id)



# EDIT NAME 2
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'OwnerEditName2_')))
async def GetUserByID_OwnerEditName2(event):

    await DeleteEvent(event)
    user_id = int(str(event.data.decode()).split('_')[1])

    try:
        async with bot.conversation(event.chat_id, timeout=120) as conv:
            await conv.send_message('__أرسل الاسم الأخير لتحديثه:__')
            first_name = (await conv.get_response()).message

        cursor.execute("UPDATE bot_users SET lastname = ? WHERE user_id = ?", (first_name, user_id,))
        database.commit()

        await GetUserByID_OwnerEdit(event, passed_user_id=user_id, extra_msg='__✅ تم تعديل الاسم الأخير للمستخدم بنجاح__')
    
    except:await GetUserByID_(event, passed_user_id=user_id)



# Get Subscription
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'getSubscription_')))
async def GetSubscription(event):
    
    # await DeleteEvent(event)
    user_id = int(str(event.data.decode()).replace('getSubscription_', '').strip())
    subscription_history = cursor.execute(f'SELECT * FROM subscription_history WHERE user_id = {user_id}')
    subscription_history = cursor.fetchall()

    if len(subscription_history) == 0:
        header_info = f'''# تقرير شامل على عدد مرات الشحن

ايدي العميل : {user_id}
اجمالي عدد مرات الشحن : {len(subscription_history)}

--------------------------------------------
لم يقم بالشحن
--------------------------------------------
'''
    else:
        header_info = f'''# تقرير شامل على عدد مرات الشحن

ايدي العميل : {user_id}
اجمالي عدد مرات الشحن : {len(subscription_history)}


--------------------------------------------
'''
        
        for item in subscription_history:
            header_info += f'''رقم الفاتورة : {item[2]}
رابط الفاتورة : {item[3]}
تم دفع الفاتورة بتاريخ : {item[4]}
شحن : {item[5]}$
--------------------------------------------'''


    filepath = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + '.txt'
    with open(filepath, "w", encoding='utf-8 ') as file:
        file.write(header_info)

    last_3 = '**💳📜 سجل الشحن (📥 حمل الملف لتصفح السجل بالكامل) 📄**\n\n'
    for idx, item in enumerate(subscription_history):
        if idx == 3:
            break

        last_3 += f'''__🧾 **رقم الفاتورة**: {item[2]}
🔗 **رابط الفاتورة**: {item[3]}
📅 **تم دفع الفاتورة بتاريخ**: {item[4]}
💰 **شحن**: {item[5]}$__

'''


    await bot.send_message(event.chat_id, file=filepath, message=last_3)

    try:
        os.remove(filepath)
    except:pass



# Get Recorded History
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'getRecordedHistory_')))
async def GetRecordedHistory(event):
    
    # await DeleteEvent(event)
    user_id = int(str(event.data.decode()).replace('getRecordedHistory_', '').strip())
    subscription_history = cursor.execute(f"SELECT * FROM orders_recorded WHERE action_status = 'Success' AND purchased_by = {user_id}")
    subscription_history = cursor.fetchall()

    if len(subscription_history) == 0:
        header_info = f'''# تقرير شامل على عمليات الشراء

ايدي العميل : {user_id}
اجمالي عدد العمليات الشراء : {len(subscription_history)}

--------------------------------------------
لا يوجد عمليات شراء
--------------------------------------------
'''
    else:
        header_info = f'''# تقرير شامل على عمليات الشراء

ايدي العميل : {user_id}
اجمالي عدد عمليات الشراء : {len(subscription_history)}


--------------------------------------------
'''
        
        for item in subscription_history:
            header_info += f'''
🛍️ الخدمة: {item[7]}
📞 الرقم: {item[9]}
🌍 الدولة: {item[8]}
✅ كود التأكيد: {item[10]}
🗓️ تاريخ الشراء: {item[11]}
💵 السعر: {item[3]}
--------------------------------------------'''

    filepath = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + '.txt'
    with open(filepath, "w", encoding='utf-8 ') as file:
        file.write(header_info)

    last_3 = '**💳📜 سجل عمليات الشراء (📥 حمل الملف لتصفح السجل بالكامل) 📄**\n\n'
    for idx, item in enumerate(subscription_history):
        if idx == 3:
            break

        last_3 += f'''__🛍️ الخدمة: {item[7]}
📞 الرقم: {item[9]}
🌍 الدولة: {item[8]}
✅ كود التأكيد: {item[10]}
🗓️ تاريخ الشراء: {item[11]}
💵 السعر: {item[3]}

__'''


    await bot.send_message(event.chat_id, file=filepath, message=last_3)

    try:
        os.remove(filepath)
    except:pass



# Get SMM History
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'getSmmHistory_')))
async def GetSmmHistory(event):
    
    # await DeleteEvent(event)
    user_id = int(str(event.data.decode()).replace('getSmmHistory_', '').strip())
    subscription_history = cursor.execute(f"SELECT * FROM record_smm_services WHERE created_by = {user_id}")
    subscription_history = cursor.fetchall()

    if len(subscription_history) == 0:
        header_info = f'''# SMM تقرير شامل على عمليات الشراء

ايدي العميل : {user_id}
اجمالي عدد العمليات الشراء SMM : {len(subscription_history)}

--------------------------------------------
لا يوجد عمليات شراء SMM
--------------------------------------------
'''
    else:
        header_info = f'''# SMM تقرير شامل على عمليات الشراء

ايدي العميل : {user_id}
اجمالي عدد عمليات الشراء SMM : {len(subscription_history)}


--------------------------------------------
'''
        
        for item in subscription_history:
            service_data = [service for service in smm_services['arabic'] if service['service'] == str(item[2])]
            service_name = service_data[0]['name']

            header_info += f'''
🛍️ الخدمة: {service_name}
🔗 الرابط: {item[4]}
📈 الكمية: {item[5]}
💵 السعر: {item[3]}$
--------------------------------------------'''

    filepath = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + '.txt'
    with open(filepath, "w", encoding='utf-8 ') as file:
        file.write(header_info)

    last_3 = '**💳📜 سجل عمليات الشراء SMM (📥 حمل الملف لتصفح السجل بالكامل) 📄**\n\n'
    for idx, item in enumerate(subscription_history):
        if idx == 3:
            break

        service_data = [service for service in smm_services['arabic'] if service['service'] == str(item[2])]
        service_name = service_data[0]['name']
        last_3 += f'''__🛍️ الخدمة: {service_name}
🔗 الرابط: {item[4]}
📈 الكمية: {item[5]}
💵 السعر: {item[3]}$

__'''


    await bot.send_message(event.chat_id, file=filepath, message=last_3)

    try:
        os.remove(filepath)
    except:pass




# Discounts Show
@bot.on(events.CallbackQuery(data='discounts_show')) 
async def discounts_show(event):

    await DeleteEvent(event)

    limited_offer = cursor.execute('SELECT * FROM limited_offer')
    limited_offer = cursor.fetchall()

    limited_offer_active = cursor.execute("SELECT * FROM limited_offer WHERE status = 'active'")
    limited_offer_active = cursor.fetchall()

    limited_offer_users = 0
    for offer in limited_offer:
        limited_offer_users += int(offer[8])


    last_offer = ''
    if len(limited_offer_active) != 0:
        offer_data = limited_offer_active[-1]

        target_date = datetime.datetime.strptime(str(offer_data[6]), "%Y-%m-%d %H:%M:%S")
        current_time = datetime.datetime.now()

        # Calculate the time difference
        time_difference = target_date - current_time

        if time_difference.total_seconds() > 0:
            remaining_days = time_difference.days
            remaining_seconds = time_difference.seconds
            remaining_hours = remaining_seconds // 3600
            remaining_minutes = (remaining_seconds % 3600) // 60
            remains = f'{remaining_days} يوم, {remaining_hours} ساعة, {remaining_minutes} ثانية'
        else:
            remains = 'العرض انتهى'
            cursor.execute(f"UPDATE limited_offer SET status = 'unactive' WHERE id = {offer_data[0]}")
            database.commit()

        last_offer = f'''🏷️ اسم العرض: {offer_data[1]}
🔢 كود العرض: {offer_data[2]}
💸 قيمة الخصم: {offer_data[3]}%

⏳ المدة: {offer_data[4]} يوم
📅 ينتهي بعد: {remains}'''
    
    else:
        last_offer = 'لا يوجد أي عروض'


    limited_offer_unactive = cursor.execute("SELECT * FROM limited_offer WHERE status = 'unactive'")
    limited_offer_unactive = cursor.fetchall()


    buttons = [
        [Button.inline('📊 إحصائيات العروض', 'offers_statistics')],
        [
            Button.inline(f'✅ الخطط النشيطة ({len(limited_offer_active)})', 'activeOffers'), 
            Button.inline(f'❌ الخطط غير النشيطة ({len(limited_offer_unactive)})', 'unactiveOffers')
        ],
        [Button.inline('➕ اضافة عرض', 'add_limited_offer')],
        [Button.inline('🔙 رجوع', 'back_to_adminPanel')]
    ]

    await event.respond(f'''__
🔧 **إدارة العروض و الخصومات**  

📊 **إحصائيات عامة**  
📋 إجمالي العروض: {len(limited_offer)}
✅ العروض النشيطة: {len(limited_offer_active)}
❌ العروض المنتهية : {len(limited_offer_unactive)}
👥 إجمالي الاستخدامات: {limited_offer_users}


🔥 **احدث العروض النشيطة**
--------------------------------
{last_offer}
--------------------------------
__''', buttons=buttons)




# Add Limited Offer
@bot.on(events.CallbackQuery(data='add_limited_offer'))
async def add_limited_offer(event):

    await DeleteEvent(event)
    try:
        async with bot.conversation(event.chat_id, timeout=120) as conv:
            await conv.send_message('__أرسل اسم العرض:__')
            offer_name = (await conv.get_response()).message

            await conv.send_message('__أرسل كود العرض:__')
            offer_code = (await conv.get_response()).message

            await conv.send_message('__أرسل قيمة العرض:__')
            offer_reduce = (await conv.get_response()).message

            await conv.send_message('__أرسل مدة العرض بالأيام:__')
            offer_days = (await conv.get_response()).message

        if str(offer_days).isdigit():
            try:
                reduce = float(offer_reduce)
            except:
                await event.respond('قيمة العرض يجب أن يكون رقما!__')
                return
            
            # current_datetime = datetime.datetime.now()
            # future_datetime = current_datetime + timedelta(days=int(offer_days))
            
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            future_datetime = (datetime.datetime.now() + timedelta(days=int(offer_days))).strftime("%Y-%m-%d %H:%M:%S")

            
            # ADD OFFER
            insert_query = """
                INSERT INTO limited_offer (
                    offer_name, offer_code, reduce, valid_days, created_at, end_at, status, usage_count
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """

            values = (
                offer_name,
                offer_code,
                reduce,
                int(offer_days),
                current_datetime,
                future_datetime,
                'active',
                0,
            )
            
            cursor.execute(insert_query, values)
            database.commit()

        else:
            await event.respond('الأيام يجب أن يكون رقما!__')

    except:pass
    await discounts_show(event)




# Show all VIP subscriptions with Pagination
@bot.on(events.CallbackQuery(data='activeOffers'))
async def activeOffers(event):

    cursor.execute("SELECT * FROM limited_offer WHERE status = 'active'")
    limited_offers = cursor.fetchall()

    # Get the first subscription based on the id or show the first if none selected
    if len(limited_offers) == 0:
        await event.answer('لا توجد عروض', alert=True)
    else:
        first_sub = limited_offers[0]
        item = first_sub
        await display_limited_offers(event, item[0], is_status=True, status_type='active')




# Function to display a specific VIP subscription
async def display_limited_offers(event, sub_id, is_status=False, status_type=''):

    await DeleteEvent(event)
    cursor = database.cursor()

    # Query to get the specific subscription by id
    if is_status == False:
        cursor.execute('SELECT * FROM limited_offer WHERE id = ?', (sub_id,))
        item = cursor.fetchone()
    else:
        cursor.execute('SELECT * FROM limited_offer WHERE id = ? AND status = ?', (sub_id, status_type,))
        item = cursor.fetchone()

    if item:
        if item[7] == 'active':
            status = 'نشيطة ✅'
        else:
            status = 'غير نشيطة ❌'
        
        target_date = datetime.datetime.strptime(str(item[6]), "%Y-%m-%d %H:%M:%S")
        current_time = datetime.datetime.now()

        # Calculate the time difference
        time_difference = target_date - current_time
        if time_difference.total_seconds() > 0:
            remaining_days = time_difference.days
            remaining_seconds = time_difference.seconds
            remaining_hours = remaining_seconds // 3600
            remaining_minutes = (remaining_seconds % 3600) // 60
            remains = f'{remaining_days} يوم, {remaining_hours} ساعة, {remaining_minutes} ثانية'
        else:
            remains = 'العرض انتهى'
            cursor.execute(f"UPDATE limited_offer SET status = 'unactive' WHERE id = {item[0]}")
            database.commit()

        if item[7] == 'unactive':
            remains = 'العرض انتهى'


        item_display = f'''🏷️ اسم العرض: {item[1]}
🔢 كود العرض: {item[2]}
💸 قيمة الخصم: {item[3]}%

⏳ المدة: {item[4]} يوم
📅 ينتهي بعد: {remains}

👥 عدد المستخدمين : {item[8]}
'''
        

        # Prepare the buttons for Next and Previous navigation
        buttons = [
            # [Button.inline('🛠 تعديل السعر', f'VipEditPrice_{item[0]}'), Button.inline('📅 تعديل الشهور', f'VipEditMonth_{item[0]}')]
        ]

        if item[7] == 'active':
            buttons.append([Button.inline('❌ انهاء العرض', f'StopOffer_{item[0]}')])
        else:
            buttons.append([Button.inline('❌ العرض منتهي', '')])

        nextback_buttons = []

        # Get Previous Item (if exists)
        if is_status == False:
            cursor.execute('SELECT id FROM limited_offer WHERE id < ? ORDER BY id DESC LIMIT 1', (item[0],))
            prev_item = cursor.fetchone()

            if prev_item:
                nextback_buttons.append(Button.inline('« السابق', data=f'prevOffer_{prev_item[0]}'))
            else:
                nextback_buttons.append(Button.inline('« السابق', data=f'prevOffer_none'))

        else:
            cursor.execute('SELECT id FROM limited_offer WHERE status = ? AND id < ? ORDER BY id DESC LIMIT 1', (status_type, item[0]))
            prev_item = cursor.fetchone()

            if prev_item:
                nextback_buttons.append(Button.inline('« السابق', data=f'prevOffer{status_type}_{prev_item[0]}'))
            else:
                nextback_buttons.append(Button.inline('« السابق', data=f'prevOffer{status_type}_none'))

        # Get Next Item (if exists)
        if is_status == False:
            cursor.execute('SELECT id FROM limited_offer WHERE id > ? ORDER BY id ASC LIMIT 1', (item[0],))
            next_item = cursor.fetchone()

            if next_item:
                nextback_buttons.append(Button.inline('التالي »', data=f'nextOffer_{next_item[0]}'))
            else:
                nextback_buttons.append(Button.inline('التالي »', data=f'nextOffer_none'))
        else:
            cursor.execute('SELECT id FROM limited_offer WHERE status = ? AND id > ? ORDER BY id ASC LIMIT 1', (status_type, item[0]))
            next_item = cursor.fetchone()

            if next_item:
                nextback_buttons.append(Button.inline('التالي »', data=f'nextOffer{status_type}_{next_item[0]}'))
            else:
                nextback_buttons.append(Button.inline('التالي »', data=f'nextOffer{status_type}_none'))


        buttons.append(nextback_buttons)

        # Back to main menu button
        buttons.append([Button.inline('🔙 رجوع', data='back_to_offer')])

        # Send the current item with navigation buttons
        await event.respond(f"__📋 العرض\n\n{item_display}\n\n🔽 اختر ما تريد:__", buttons=buttons)
    else:
        await event.respond("العرض غير موجود")


# BACK TO OFFER
@bot.on(events.CallbackQuery(data='back_to_offer'))
async def BackToOffer(event):
    await DeleteEvent(event), await discounts_show(event)



# Stop Offer
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'StopOffer_')))
async def StopOffer(event):

    try:
        sub_id = int(event.data.decode().split('_')[1])
        cursor.execute(f"UPDATE limited_offer SET status = 'unactive' WHERE id = {sub_id}")
        database.commit()
        await display_limited_offers(event, sub_id)
    except:await event.answer('لا يوجد هذا العرض', alert=True)



# Handle "Next" button press to show the next subscription
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'nextOffer_')))
async def next_item_offer(event):

    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_limited_offers(event, sub_id)
    except:await event.answer('لا مزيد من العروض', alert=True)



# Handle "Previous" button press to show the previous subscription
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'prevOffer_')))
async def prev_item_offer(event):

    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_limited_offers(event, sub_id)
    except:await event.answer('لا مزيد من العروض', alert=True)



@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'nextOfferactive_')))
async def next_item2_offer(event):
    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_limited_offers(event, sub_id, is_status=True, status_type='active')
    except Exception as e:
        await event.answer('لا مزيد من العروض', alert=True)


@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'prevOfferactive_')))
async def prev_item2_offer(event):
    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_limited_offers(event, sub_id, is_status=True, status_type='active')
    except Exception as e:
        await event.answer('لا مزيد من العروض', alert=True)



@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'nextOfferunactive_')))
async def next_item3_offer(event):
    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_limited_offers(event, sub_id, is_status=True, status_type='unactive')
    except Exception as e:
        await event.answer('لا مزيد من العروض', alert=True)


@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'prevOfferunactive_')))
async def prev_item3_offer(event):
    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_limited_offers(event, sub_id, is_status=True, status_type='unactive')
    except Exception as e:
        await event.answer('لا مزيد من العروض', alert=True)





# Show all VIP subscriptions with Pagination
@bot.on(events.CallbackQuery(data='unactiveOffers'))
async def unactiveOffers(event):

    cursor.execute("SELECT * FROM limited_offer WHERE status = 'unactive'")
    limited_offers = cursor.fetchall()

    # Get the first subscription based on the id or show the first if none selected
    if len(limited_offers) == 0:
        await event.answer('لا توجد عروض', alert=True)
    else:
        first_sub = limited_offers[0]
        item = first_sub
        await display_limited_offers(event, item[0], is_status=True, status_type='unactive')



@bot.on(events.CallbackQuery(data='offers_statistics'))
async def offers_statistics(event):
    # Start with the first page
    await show_offers_page(event, current_page=0)



@bot.on(events.CallbackQuery(data=re.compile(r'OffersUsagePage_(\d+)')))
async def paginate_offers(event):
    # Extract the current page from callback data
    current_page = int(event.data_match.group(1))
    await show_offers_page(event, current_page)



async def show_offers_page(event, current_page):

    await DeleteEvent(event)
    offset = current_page * ITEMS_PER_PAGE

    # Fetch offers from the database
    cursor.execute(
        "SELECT * FROM limited_offer LIMIT ? OFFSET ?", (ITEMS_PER_PAGE, offset)
    )
    limited_offers = cursor.fetchall()

    # Create the message with offers
    offer_msg = '**📊 إحصائيات العروض**\n\n'
    for offer in limited_offers:
        offer_name, usage_count = offer[1], offer[8]
        offer_msg += f'''__🏷️ اسم العرض: {offer_name}
👥 عدد المستخدمين : {usage_count}__

'''

    # Fetch total number of offers for pagination controls
    cursor.execute("SELECT COUNT(*) FROM limited_offer")
    total_offers = cursor.fetchone()[0]

    # Calculate total pages
    total_pages = (total_offers + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    offer_msg += f'\n📄 الصفحة: {current_page + 1}/{total_pages}'

    # Ensure "back" and "next" buttons are always visible
    buttons = [
        [
            Button.inline('« السابق', f'OffersUsagePage_{max(0, current_page - 1)}'),
            Button.inline('التالي »', f'OffersUsagePage_{min(total_pages - 1, current_page + 1)}'),
        ],
        [Button.inline('🔙 Back', 'back_to_offer')]
    ]

    # Add buttons to the message
    await event.respond(offer_msg, buttons=buttons)



# VIP show
@bot.on(events.CallbackQuery(data='vip_show')) 
async def VIP_SHOW(event):

    # bot_settings_data = cursor.execute('SELECT * FROM bot_settings WHERE setting_id = 1')
    # bot_settings_data = cursor.fetchone()

    vip_subscription = cursor.execute('SELECT * FROM vip_subscription')
    vip_subscription = cursor.fetchall()

    vip_subscription_active = cursor.execute("SELECT * FROM vip_subscription WHERE status = 'active'")
    vip_subscription_active = cursor.fetchall()

    vip_subscription_unactive = cursor.execute("SELECT * FROM vip_subscription WHERE status = 'unactive'")
    vip_subscription_unactive = cursor.fetchall()

    # vip_bot_users = cursor.execute("SELECT * FROM bot_users WHERE is_vip IS NOT NULL")
    # vip_bot_users = cursor.fetchall()

    await DeleteEvent(event)

    buttons = [
        [Button.inline('📋 عرض جميع الخطط', 'show_all_vip_sub')],
        [Button.inline(f'✅ الخطط النشيطة ({len(vip_subscription_active)})', 'activeVIP'), Button.inline(f'❌ الخطط غير النشيطة ({len(vip_subscription_unactive)})', 'unactiveVIP')],
        [Button.inline('➕ اضافة خطة جديدة', 'add_vip_sub')],
        [Button.inline('🔙 رجوع', 'back_to_adminPanel')]
    ]

    # 👥 إجمالي المشتركين النشطين: {len(vip_bot_users)}

    await event.respond(f'''__
🔧 **إدارة خطط الشحن**  

📊 **إحصائيات عامة**  
📋 إجمالي الخطط: {len(vip_subscription)}
✅ الخطط النشطة: {len(vip_subscription_active)}
❌ الخطط غير النشطة: {len(vip_subscription_unactive)}


🔽 **اختر ما تريد عرضه:**
__''', buttons=buttons)



# Show all VIP subscriptions with Pagination
@bot.on(events.CallbackQuery(data='activeVIP'))
async def activeVIP(event):

    cursor.execute("SELECT * FROM vip_subscription WHERE status = 'active'")
    vip_subscription = cursor.fetchall()

    # Get the first subscription based on the id or show the first if none selected
    if len(vip_subscription) == 0:
        await event.answer('لا توجد خطط لعرضها', alert=True)
    else:
        first_sub = vip_subscription[0]
        item = first_sub
        await display_vip_subscription(event, item[0], is_status=True, status_type='active')



# Show all VIP subscriptions with Pagination
@bot.on(events.CallbackQuery(data='unactiveVIP'))
async def unactiveVIP(event):

    cursor.execute("SELECT * FROM vip_subscription WHERE status = 'unactive'")
    vip_subscription = cursor.fetchall()

    # Get the first subscription based on the id or show the first if none selected
    if len(vip_subscription) == 0:
        await event.answer('لا توجد خطط لعرضها', alert=True)
    else:
        first_sub = vip_subscription[0]
        item = first_sub
        await display_vip_subscription(event, item[0], is_status=True, status_type='unactive')



# Show all VIP subscriptions with Pagination
@bot.on(events.CallbackQuery(data='show_all_vip_sub'))
async def show_all_vip_sub(event):

    cursor.execute('SELECT * FROM vip_subscription')
    vip_subscription = cursor.fetchall()

    # Get the first subscription based on the id or show the first if none selected
    if len(vip_subscription) == 0:
        await event.answer('لا يوجد خطط لعرضها', alert=True)
    else:
        first_sub = vip_subscription[0]
        item = first_sub
        await display_vip_subscription(event, item[0])



# Function to display a specific VIP subscription
async def display_vip_subscription(event, sub_id, is_status=False, status_type=''):

    await DeleteEvent(event)
    cursor = database.cursor()

    # Query to get the specific subscription by id
    if is_status == False:
        cursor.execute('SELECT * FROM vip_subscription WHERE id = ?', (sub_id,))
        item = cursor.fetchone()
    else:
        cursor.execute('SELECT * FROM vip_subscription WHERE id = ? AND status = ?', (sub_id, status_type,))
        item = cursor.fetchone()

    if item:
        if item[2] == 'active':
            status = 'نشيطة ✅'
        else:
            status = 'غير نشيطة ❌'

        item_display = f"""
📅 حالة الخطة : {status}
💰 شحن : {item[1]}$
"""

        # Prepare the buttons for Next and Previous navigation
        buttons = [
            [Button.inline('🛠 تعديل السعر', f'VipEditPrice_{item[0]}')]
        ]

        if item[2] == 'active':
            buttons.append([Button.inline('❌ ايقاف تنشيط الخطة', f'VipActive_{item[0]}')])
        else:
            buttons.append([Button.inline('✅ اعادة تنشيط الخطة', f'VipUnActive_{item[0]}')])

        nextback_buttons = []

        # Get Previous Item (if exists)
        if is_status == False:
            cursor.execute('SELECT id FROM vip_subscription WHERE id < ? ORDER BY id DESC LIMIT 1', (item[0],))
            prev_item = cursor.fetchone()

            if prev_item:
                nextback_buttons.append(Button.inline('« السابق', data=f'prevSub_{prev_item[0]}'))
            else:
                nextback_buttons.append(Button.inline('« السابق', data=f'prevSub_none'))

        else:
            cursor.execute('SELECT id FROM vip_subscription WHERE status = ? AND id < ? ORDER BY id DESC LIMIT 1', (status_type, item[0]))
            prev_item = cursor.fetchone()

            if prev_item:
                nextback_buttons.append(Button.inline('« السابق', data=f'prevSub{status_type}_{prev_item[0]}'))
            else:
                nextback_buttons.append(Button.inline('« السابق', data=f'prevSub{status_type}_none'))

        # Get Next Item (if exists)
        if is_status == False:
            cursor.execute('SELECT id FROM vip_subscription WHERE id > ? ORDER BY id ASC LIMIT 1', (item[0],))
            next_item = cursor.fetchone()

            if next_item:
                nextback_buttons.append(Button.inline('التالي »', data=f'nextSub_{next_item[0]}'))
            else:
                nextback_buttons.append(Button.inline('التالي »', data=f'nextSub_none'))
        else:
            cursor.execute('SELECT id FROM vip_subscription WHERE status = ? AND id > ? ORDER BY id ASC LIMIT 1', (status_type, item[0]))
            next_item = cursor.fetchone()

            if next_item:
                nextback_buttons.append(Button.inline('التالي »', data=f'nextSub{status_type}_{next_item[0]}'))
            else:
                nextback_buttons.append(Button.inline('التالي »', data=f'nextSub{status_type}_none'))


        buttons.append(nextback_buttons)

        # Back to main menu button
        buttons.append([Button.inline('🔙 رجوع', data='back_to_sub')])

        # Send the current item with navigation buttons
        await event.respond(f"__📋 الخطة\n{item_display}\n\n🔽 اختر ما تريد:__", buttons=buttons)
    else:
        await event.respond("لا توجد خطة شحن بهذا الرقم.")



# Handle "Next" button press to show the next subscription
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'nextSub_')))
async def next_item(event):

    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_vip_subscription(event, sub_id)
    except:await event.answer('لا مزيد من الخطط', alert=True)



# Handle "Previous" button press to show the previous subscription
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'prevSub_')))
async def prev_item(event):

    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_vip_subscription(event, sub_id)
    except:await event.answer('لا مزيد من الخطط', alert=True)



@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'nextSubactive_')))
async def next_item2(event):
    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_vip_subscription(event, sub_id, is_status=True, status_type='active')
    except Exception as e:
        await event.answer('لا مزيد من الخطط', alert=True)


@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'prevSubactive_')))
async def prev_item2(event):
    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_vip_subscription(event, sub_id, is_status=True, status_type='active')
    except Exception as e:
        await event.answer('لا مزيد من الخطط', alert=True)



@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'nextSubunactive_')))
async def next_item3(event):
    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_vip_subscription(event, sub_id, is_status=True, status_type='unactive')
    except Exception as e:
        await event.answer('لا مزيد من الخطط', alert=True)


@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'prevSubunactive_')))
async def prev_item3(event):
    try:
        sub_id = int(event.data.decode().split('_')[1])
        await display_vip_subscription(event, sub_id, is_status=True, status_type='unactive')
    except Exception as e:
        await event.answer('لا مزيد من الخطط', alert=True)



# VipActive_
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'VipActive_')))
async def VipActive_(event):

    try:
        sub_id = int(event.data.decode().split('_')[1])
        cursor.execute(f"UPDATE vip_subscription SET status = 'unactive' WHERE id = {sub_id}")
        database.commit()
        await display_vip_subscription(event, sub_id)
    except:await event.answer('لا توجد هذه الخطة', alert=True)



# VipUnActive_
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'VipUnActive_')))
async def VipUnActive_(event):

    try:
        sub_id = int(event.data.decode().split('_')[1])
        cursor.execute(f"UPDATE vip_subscription SET status = 'active' WHERE id = {sub_id}")
        database.commit()
        await display_vip_subscription(event, sub_id)
    except:await event.answer('لا توجد هذه الخطة', alert=True)




# Add Vip Sub
@bot.on(events.CallbackQuery(data='add_vip_sub'))
async def add_vip_sub(event):

    await DeleteEvent(event)
    try:
        async with bot.conversation(event.chat_id, timeout=120) as conv:
            # await conv.send_message('__أرسل عدد أشهر الخطة:__')
            # months = (await conv.get_response()).message

            await conv.send_message('__أرسل السعر الخطة:__')
            price = (await conv.get_response()).message

        # if str(months).isdigit():
        try:
            price = float(price)
        except:
            await event.respond('__السعر يجب أن يكون رقما!__')
            return
        
        # ADD VIP SUB
        insert_sql = f"INSERT INTO vip_subscription (price, status) VALUES ({float(price)}, 'active');"
        cursor.execute(insert_sql)
        database.commit()

        # else:
        #     await event.respond('الأشهر يجب أن يكون رقما!__')

    except:pass
    await VIP_SHOW(event)


# Vip Edit Price
@bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'VipEditPrice_')))
async def VipEditPrice(event):

    await DeleteEvent(event)
    sub_id = int(event.data.decode().split('_')[1])
    try:
        async with bot.conversation(event.chat_id, timeout=120) as conv:
            await conv.send_message('__أرسل السعر الجديد:__')
            new_price = (await conv.get_response()).message

        try:
            new_price = float(new_price)
            cursor.execute(f"UPDATE vip_subscription SET price = {new_price} WHERE id = {sub_id}")
            database.commit()

            await display_vip_subscription(event, sub_id)
        except:
            await event.respond('__السعر يجب أن يكون رقما!__')

    except:pass



# # Vip Edit Month
# @bot.on(events.CallbackQuery(data=lambda b: b.startswith(b'VipEditMonth_')))
# async def VipEditMonth(event):

#     await DeleteEvent(event)
#     sub_id = int(event.data.decode().split('_')[1])
#     try:
#         async with bot.conversation(event.chat_id, timeout=120) as conv:
#             await conv.send_message('__أرسل المدة الجديد بالشهور:__')
#             new_month = (await conv.get_response()).message

#         if str(new_month).isdigit():
#             cursor.execute(f"UPDATE vip_subscription SET months = {new_month} WHERE id = {sub_id}")
#             database.commit()

#             await display_vip_subscription(event, sub_id)
#         else:
#             await event.respond('الشهور يجب أن يكون رقما!__')

#     except:pass













bot.run_until_disconnected()