#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# @author       Yonghwan, Roh(somma@somma.kr)
# @date         2021/08/29 15:19 created.
# @copyright    (C)Somma,Inc. All rights reserved.
#

# =============================================================================
# Process
# =============================================================================
iid_proc_base = 1000
iid_bt_proc_start = iid_proc_base + 500
iid_bt_proc_stop = iid_proc_base + 501
iid_bt_image_load = iid_proc_base + 502
iid_bt_proc_open = iid_proc_base + 504
iid_bt_proc_dup = iid_proc_base + 505
iid_bt_remote_thread = iid_proc_base + 506
iid_proc_max = 1999

# Process.flag
ef_on_ext_storage = 0x00000001
pf_on_ext_storage = ef_on_ext_storage
pf_proc_blocked	= 0x00000002
pf_wow = 0x00000004
pf_no_image = 0x00000008
pf_access_fail = 0x00000010
pf_zero_size = 0x00000020

# =============================================================================
# File
# =============================================================================
iid_file_base = 2000
iid_bt_file = iid_file_base + 500
iid_bt_file_namedpipe = iid_file_base + 501
iid_mstr_file_rename = iid_file_base + 113

# File I/O flag
ff_superseded = 0x00000001  # Existing file replaced
ff_created = 0x00000002  # New file created
ff_overwritten = 0x00000004  # Existing file overwritten

ff_delete_disposition = 0x00000010  # Delete disposition has set
ff_delete_on_close = 0x00000020  # Delete-on-close disposition has set
ff_renamed = 0x00000040  # File renamed
ff_map_write = 0x00000080  # File mapped to be written
ff_written = 0x00000100

ff_executable = 0x00000200  # File is executable
ff_extern_storage = 0x00000300  # File is on external storage
ff_predefined_path = 0x00000800  # File is on specified path by configuration
ff_net_share = 0x00001000  # File is on network share path

# =============================================================================
# Network
# =============================================================================
iid_net_base = 3000

# Event block ID for network
iid_bt_net_connect = iid_net_base + 500
iid_bt_net_accept = iid_net_base + 501
iid_bt_net_udp_sent = iid_net_base + 502
iid_bt_net_udp_recv = iid_net_base + 503
iid_bt_dns_reply = iid_net_base + 504

# =============================================================================
# Registry
# =============================================================================
iid_reg_base = 4000
iid_mstr_reg_base = iid_reg_base + 100
iid_bt_reg = iid_reg_base + 500
iid_mstr_reg_set_value = iid_mstr_reg_base + 3
iid_mstr_reg_delete_key = iid_mstr_reg_base + 4
iid_mstr_reg_delete_value = iid_mstr_reg_base + 5
iid_mstr_reg_rename_key = iid_mstr_reg_base + 6
iid_reg_max = 4999

# WMI
iid_wmi_base = 5000
iid_wmi_query = 5502

# =============================================================================
# PNP
# =============================================================================
iid_pnp_base = 6000
iid_bt_pnp = iid_pnp_base + 500

# =============================================================================
# Disk
# =============================================================================
iid_disk_base = 7000
iid_bt_disk = iid_disk_base + 500

# =============================================================================
# Host information
# =============================================================================
iid_host_info_base = 8000
iid_bt_update_host_info = iid_host_info_base + 500


# =============================================================================
# Windows event log
# =============================================================================
iid_evt_base = 9000
iid_bt_evt_logon_success = iid_evt_base + 500
iid_bt_evt_logon_failure = iid_evt_base + 501
iid_bt_evt_logoff = iid_evt_base + 502
iid_bt_evt_shutdown_service = iid_evt_base + 503
iid_bt_evt_clear_event_log = iid_evt_base + 504
iid_bt_evt_session_create = iid_evt_base + 505
iid_bt_evt_session_remove = iid_evt_base + 506
iid_bt_evt_driver_register = iid_evt_base + 507
iid_bt_evt_service_start_failed = iid_evt_base + 508
iid_bt_evt_service_install = iid_evt_base + 509
iid_bt_windows_update_install = iid_evt_base + 510
iid_bt_evt_powershell_script_block = iid_evt_base + 511
iid_evt_max = 9999


def event_to_str(event_id):        
    """ Event ID to String
    """
    if event_id == iid_bt_proc_start:
        return 'proc_start'
    elif event_id == iid_bt_proc_stop:
        return 'proc_stop'
    elif event_id == iid_bt_image_load:
        return 'image_load'
    # iid_bt_image_unload = 'image_unload'
    elif event_id == iid_bt_proc_open:
        return 'proc_open'
    elif event_id == iid_bt_proc_dup:
        return 'proc_dup'
    elif event_id == iid_bt_remote_thread:
        return 'remote_thread'

    elif event_id == iid_bt_file:
        return 'file'
    elif event_id == iid_bt_file_namedpipe:
        return 'file_namedpipe'
    elif event_id == iid_mstr_file_rename:
        return 'file_rename'

    elif event_id == iid_bt_net_connect:
        return 'net_connect'
    elif event_id == iid_bt_net_accept:
        return 'net_accept'
    elif event_id == iid_bt_net_udp_sent:
        return 'net_udp_sent'
    elif event_id == iid_bt_net_udp_recv:
        return 'net_udp_recv'
    elif event_id == iid_bt_dns_reply:
        return 'dns_reply'


    elif event_id == iid_bt_reg:
        return 'reg'        
    elif event_id == iid_mstr_reg_set_value:
        return 'reg_set_value'        
    elif event_id == iid_mstr_reg_delete_key:
        return 'reg_delete_key'
    elif event_id == iid_mstr_reg_delete_value:
        return 'reg_delete_value'
    elif event_id == iid_mstr_reg_rename_key:
        return 'reg_rename_key'

    elif event_id == iid_wmi_query:
        return 'wmi_query'

    elif event_id == iid_bt_pnp:
        return 'pnp'
    elif event_id == iid_bt_disk:
        return 'disk'

    elif event_id == iid_bt_update_host_info:
        return 'update_host_info'

    elif event_id == iid_bt_evt_logon_success:
        return 'logon_success'
    elif event_id == iid_bt_evt_logon_failure:
        return 'logon_failure'
    elif event_id == iid_bt_evt_logoff:
        return 'logoff'
    elif event_id == iid_bt_evt_shutdown_service:
        return 'shutdown_service'
    elif event_id == iid_bt_evt_clear_event_log:
        return 'clear_event_log'
    elif event_id == iid_bt_evt_session_create:
        return 'session_create'
    elif event_id == iid_bt_evt_session_remove:
        return 'session_remove'
    elif event_id == iid_bt_evt_driver_register:
        return 'driver_register'
    elif event_id == iid_bt_evt_service_start_failed:
        return 'service_start_failed'
    elif event_id == iid_bt_evt_service_install:
        return 'service_install'
    elif event_id == iid_bt_windows_update_install:
        return 'windows_update_install'
    elif event_id == iid_bt_evt_powershell_script_block:
        return 'powershell script block'
