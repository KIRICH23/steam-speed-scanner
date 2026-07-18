"""
Steam Download Region Speed Scanner
Professional UX/UI Design
Scans all Steam download regions and finds the fastest one based on connection speed.
"""

import asyncio
import aiohttp
import time
from dataclasses import dataclass
from typing import Optional
import sys
import io

# Set UTF-8 encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Initialize colorama for Windows console color support
try:
    from colorama import init as colorama_init
    colorama_init()
except ImportError:
    pass

# ANSI color codes
class Colors:
    RESET = ""
    BOLD = ""
    DIM = ""
    ITALIC = ""
    UNDERLINE = ""
    RED = ""
    GREEN = ""
    YELLOW = ""
    BLUE = ""
    MAGENTA = ""
    CYAN = ""
    WHITE = ""
    GRAY = ""
    ORANGE = ""
    PINK = ""


def supports_color():
    """Check if the terminal supports ANSI colors."""
    if sys.platform == 'win32':
        try:
            from colorama import init
            return True
        except ImportError:
            import os
            wt_session = os.environ.get('WT_SESSION')
            term_program = os.environ.get('TERM_PROGRAM')
            if wt_session or term_program == 'vscode':
                return True
            return False
    return True


if supports_color():
    Colors.RESET = "\033[0m"
    Colors.BOLD = "\033[1m"
    Colors.DIM = "\033[2m"
    Colors.UNDERLINE = "\033[4m"
    Colors.RED = "\033[91m"
    Colors.GREEN = "\033[92m"
    Colors.YELLOW = "\033[93m"
    Colors.BLUE = "\033[94m"
    Colors.MAGENTA = "\033[95m"
    Colors.CYAN = "\033[96m"
    Colors.WHITE = "\033[97m"
    Colors.GRAY = "\033[90m"
    Colors.ORANGE = "\033[38;5;208m"
    Colors.PINK = "\033[38;5;213m"


def get_color(text: str, color: str) -> str:
    """Return colored text for terminal."""
    return f"{color}{text}{Colors.RESET}"


# UI Components
class UI:
    """UI helper class for consistent styling."""
    
    @staticmethod
    def clear_screen():
        """Clear the console screen."""
        print("\033[2J\033[H", end="", flush=True)
    
    @staticmethod
    def hide_cursor():
        """Hide cursor."""
        print("\033[?25l", end="", flush=True)
    
    @staticmethod
    def show_cursor():
        """Show cursor."""
        print("\033[?25h", end="", flush=True)
    
    @staticmethod
    def move_cursor(x: int, y: int):
        """Move cursor to position."""
        print(f"\033[{y};{x}H", end="", flush=True)
    
    @staticmethod
    def center_text(text: str, width: int = 80) -> str:
        """Center text within given width."""
        padding = (width - len(text.replace('\033[', '').replace('m', '').replace('0;', '').replace('0m', ''))) // 2
        return " " * padding + text
    
    @staticmethod
    def draw_line(char: str = "─", width: int = 80, color: str = Colors.GRAY) -> str:
        """Draw a horizontal line."""
        return get_color(char * width, color)
    
    @staticmethod
    def draw_box(title: str, content: list, width: int = 80, color: str = Colors.CYAN) -> str:
        """Draw a box with title."""
        lines = []
        lines.append(get_color("╔" + "═" * (width - 2) + "╗", color))
        lines.append(get_color("║", color) + " " + get_color(title, Colors.BOLD + color) + " " * (width - len(title) - 4) + get_color("║", color))
        lines.append(get_color("╠" + "═" * (width - 2) + "╣", color))
        for line in content:
            lines.append(get_color("║", color) + " " + line + " " * (width - len(line.replace('\033[', '').replace('m', '').replace('0;', '').replace('0m', '')) - 3) + get_color("║", color))
        lines.append(get_color("╚" + "═" * (width - 2) + "╝", color))
        return "\n".join(lines)


# Animation frames
SPINNER_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠴", "⠦", "⠧", "⠏"]
CHECK_MARK = "✓"
CROSS_MARK = "✗"
ROCKET = "🚀"
TROPHY = "🏆"
GLOBE = "🌍"
CLOCK = "⏱️"
SPEED = "⚡"


@dataclass
class SpeedTestResult:
    """Stores the result of a speed test for a CDN endpoint."""
    endpoint_name: str
    url: str
    speed_mbps: float
    latency_ms: float
    success: bool
    error: Optional[str] = None
    status: str = ""


class ProgressDisplay:
    """Handles animated progress display during testing."""
    
    def __init__(self, total: int):
        self.total = total
        self.current = 0
        self.completed = 0
        self.failed = 0
        self.animation_index = 0
        self.start_time = time.perf_counter()
        self.results: list[SpeedTestResult] = []
    
    def update(self, result: SpeedTestResult):
        """Update progress with a new result."""
        self.current += 1
        self.results.append(result)
        if result.success:
            self.completed += 1
        else:
            self.failed += 1
    
    def get_elapsed(self) -> str:
        """Get elapsed time as formatted string."""
        elapsed = time.perf_counter() - self.start_time
        return f"{elapsed:.1f}s"
    
    def get_progress_bar(self, width: int = 40) -> str:
        """Generate a progress bar."""
        if self.total == 0:
            return " " * width
        ratio = self.current / self.total
        filled = int(width * ratio)
        bar = get_color("█" * filled, Colors.GREEN) + get_color("░" * (width - filled), Colors.GRAY)
        return bar
    
    def get_animation_frame(self) -> str:
        """Get current animation frame."""
        frame = SPINNER_FRAMES[self.animation_index % len(SPINNER_FRAMES)]
        self.animation_index += 1
        return get_color(frame, Colors.CYAN)
    
    def render(self, current_region: str = "") -> str:
        """Render the current progress display."""
        elapsed = self.get_elapsed()
        progress_bar = self.get_progress_bar(40)
        percent = (self.current / self.total * 100) if self.total > 0 else 0
        frame = self.get_animation_frame()
        
        status = f"{get_color('✓', Colors.GREEN)}{self.completed}" + "/" + f"{get_color('✗', Colors.RED)}{self.failed}"
        
        output = f"\r  {frame}  [{status}]  {progress_bar}  {get_color(f'{percent:5.1f}%', Colors.YELLOW)}  {get_color(elapsed, Colors.BLUE)}"
        
        if current_region:
            if len(current_region) > 30:
                current_region = current_region[:27] + "..."
            output += f"  {get_color('→', Colors.CYAN)} {get_color(current_region, Colors.WHITE)}"
        
        return output
    
    def clear_line(self) -> str:
        """Clear current line."""
        return "\r" + " " * 120 + "\r"


# Steam CDN endpoints with actual server hostnames
STEAM_CDN_ENDPOINTS = {
    # === EUROPE ===
    "Netherlands - Amsterdam": "http://cache1-ams1.steamcontent.com/",
    "Germany - Frankfurt": "http://cache1-fra1.steamcontent.com/",
    "UK - London": "http://cache1-lhr1.steamcontent.com/",
    "France - Paris": "http://cache1-cdg1.steamcontent.com/",
    "Sweden - Stockholm": "http://cache1-arn1.steamcontent.com/",
    "Poland - Warsaw": "http://cache1-waw1.steamcontent.com/",
    "Spain - Madrid": "http://cache1-mad1.steamcontent.com/",
    "Italy - Milan": "http://cache1-mxp1.steamcontent.com/",
    "Russia - Moscow": "http://cache1-dme1.steamcontent.com/",
    "Turkey - Istanbul": "http://cache1-ist1.steamcontent.com/",
    "Greece - Athens": "http://cache1-ath1.steamcontent.com/",
    "Austria - Vienna": "http://cache1-vie1.steamcontent.com/",
    "Switzerland - Zurich": "http://cache1-zrh1.steamcontent.com/",
    "Czech - Prague": "http://cache1-prg1.steamcontent.com/",
    "Denmark - Copenhagen": "http://cache1-cph1.steamcontent.com/",
    "Finland - Helsinki": "http://cache1-hel1.steamcontent.com/",
    "Norway - Oslo": "http://cache1-osl1.steamcontent.com/",
    "Portugal - Lisbon": "http://cache1-lis1.steamcontent.com/",
    "Romania - Bucharest": "http://cache1-otp1.steamcontent.com/",
    "Ukraine - Kiev": "http://cache1-kbp1.steamcontent.com/",
    "Hungary - Budapest": "http://cache1-bud1.steamcontent.com/",
    "Bulgaria - Sofia": "http://cache1-sof1.steamcontent.com/",
    
    # === NORTH AMERICA ===
    "US - Seattle": "http://cache1-sea1.steamcontent.com/",
    "US - Los Angeles": "http://cache1-lax1.steamcontent.com/",
    "US - Chicago": "http://cache1-ord1.steamcontent.com/",
    "US - New York": "http://cache1-jfk1.steamcontent.com/",
    "US - Miami": "http://cache1-mia1.steamcontent.com/",
    "US - Dallas": "http://cache1-dfw1.steamcontent.com/",
    "Canada - Montreal": "http://cache1-yul1.steamcontent.com/",
    "Canada - Vancouver": "http://cache1-yvr1.steamcontent.com/",
    
    # === ASIA ===
    "Japan - Tokyo": "http://cache1-nrt1.steamcontent.com/",
    "Japan - Osaka": "http://cache1-kix1.steamcontent.com/",
    "Korea - Seoul": "http://cache1-icn1.steamcontent.com/",
    "China - Shanghai": "http://cache1-pvg1.steamcontent.com/",
    "China - Beijing": "http://cache1-pek1.steamcontent.com/",
    "Taiwan - Taipei": "http://cache1-tpe1.steamcontent.com/",
    "Hong Kong": "http://cache1-hkg1.steamcontent.com/",
    "Singapore": "http://cache1-sin1.steamcontent.com/",
    "Thailand - Bangkok": "http://cache1-bkk1.steamcontent.com/",
    "Vietnam - Hanoi": "http://cache1-han1.steamcontent.com/",
    "Indonesia - Jakarta": "http://cache1-cgk1.steamcontent.com/",
    "Philippines - Manila": "http://cache1-mnl1.steamcontent.com/",
    "Malaysia - Kuala Lumpur": "http://cache1-kul1.steamcontent.com/",
    "India - Mumbai": "http://cache1-bom1.steamcontent.com/",
    "India - Delhi": "http://cache1-del1.steamcontent.com/",
    "Kazakhstan - Almaty": "http://cache1-ala1.steamcontent.com/",
    "UAE - Dubai": "http://cache1-dxb1.steamcontent.com/",
    "Israel - Tel Aviv": "http://cache1-tlv1.steamcontent.com/",
    "Saudi Arabia - Riyadh": "http://cache1-ruh1.steamcontent.com/",
    
    # === OCEANIA ===
    "Australia - Sydney": "http://cache1-syd1.steamcontent.com/",
    "Australia - Melbourne": "http://cache1-mel1.steamcontent.com/",
    "Australia - Perth": "http://cache1-per1.steamcontent.com/",
    "New Zealand - Auckland": "http://cache1-akl1.steamcontent.com/",
    
    # === SOUTH AMERICA ===
    "Brazil - Sao Paulo": "http://cache1-gru1.steamcontent.com/",
    "Brazil - Rio de Janeiro": "http://cache1-gig1.steamcontent.com/",
    "Brazil - Porto Alegre": "http://cache1-poa1.steamcontent.com/",
    "Argentina - Buenos Aires": "http://cache1-eze1.steamcontent.com/",
    "Chile - Santiago": "http://cache1-scl1.steamcontent.com/",
    "Colombia - Bogota": "http://cache1-bog1.steamcontent.com/",
    "Peru - Lima": "http://cache1-lim1.steamcontent.com/",
    
    # === AFRICA ===
    "South Africa - Johannesburg": "http://cache1-jnb1.steamcontent.com/",
    "South Africa - Cape Town": "http://cache1-cpt1.steamcontent.com/",
}

SPEED_TEST_URLS = [
    "https://speed.cloudflare.com/__down?bytes=1048576",
    "https://speed.cloudflare.com/__down?bytes=262144",
]


class SteamSpeedScanner:
    """Scans Steam CDN endpoints and measures download speeds."""
    
    def __init__(self, timeout_seconds: int = 10, show_progress: bool = True):
        self.timeout_seconds = timeout_seconds
        self.results: list[SpeedTestResult] = []
        self.show_progress = show_progress
        self.progress: Optional[ProgressDisplay] = None
        self.current_region = ""
    
    async def test_endpoint(
        self, 
        session: aiohttp.ClientSession, 
        name: str, 
        base_url: str
    ) -> SpeedTestResult:
        """Test download latency for a single CDN endpoint."""
        self.current_region = name
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "*/*",
        }
        
        try:
            start_time = time.perf_counter()
            
            async with session.get(
                base_url,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=self.timeout_seconds),
                allow_redirects=True
            ) as response:
                await response.read()
                latency_ms = (time.perf_counter() - start_time) * 1000
                
                return SpeedTestResult(
                    endpoint_name=name,
                    url=base_url,
                    speed_mbps=0.0,
                    latency_ms=round(latency_ms, 2),
                    success=True,
                    status="latency"
                )
                
        except asyncio.TimeoutError:
            return SpeedTestResult(
                endpoint_name=name,
                url=base_url,
                speed_mbps=0.0,
                latency_ms=0.0,
                success=False,
                error="Timeout",
                status="timeout"
            )
        except aiohttp.ClientError as e:
            return SpeedTestResult(
                endpoint_name=name,
                url=base_url,
                speed_mbps=0.0,
                latency_ms=0.0,
                success=False,
                error=str(type(e).__name__),
                status="error"
            )
        except Exception as e:
            return SpeedTestResult(
                endpoint_name=name,
                url=base_url,
                speed_mbps=0.0,
                latency_ms=0.0,
                success=False,
                error=str(e),
                status="error"
            )
    
    async def _latency_test(
        self,
        name: str,
        base_url: str,
        session: aiohttp.ClientSession,
        latency_ms: float
    ) -> SpeedTestResult:
        """Estimate speed based on latency."""
        estimated_speed = max(0.1, 100 / (latency_ms + 1))

        return SpeedTestResult(
            endpoint_name=name,
            url=base_url,
            speed_mbps=round(estimated_speed, 2),
            latency_ms=round(latency_ms, 2),
            success=True,
            status="latency",
            error=None
        )

    async def measure_real_speed(
        self,
        session: aiohttp.ClientSession,
        name: str,
        base_url: str
    ) -> SpeedTestResult:
        """Measure actual download speed using Steam CDN."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "*/*",
        }

        start_time = time.perf_counter()
        latency_ms = None
        try:
            async with session.get(
                base_url,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=5),
                allow_redirects=True
            ) as response:
                await response.read()
                latency_ms = (time.perf_counter() - start_time) * 1000
        except Exception:
            pass

        for test_url in SPEED_TEST_URLS:
            try:
                start_download = time.perf_counter()
                async with session.get(
                    test_url,
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=30),
                    allow_redirects=True
                ) as response:
                    if response.status == 200:
                        data = await response.read()
                        download_time = time.perf_counter() - start_download

                        bytes_downloaded = len(data)
                        if download_time > 0:
                            speed_bps = (bytes_downloaded * 8) / download_time
                            speed_mbps = speed_bps / 1_000_000
                        else:
                            speed_mbps = float('inf')

                        return SpeedTestResult(
                            endpoint_name=name,
                            url=base_url,
                            speed_mbps=round(speed_mbps, 2),
                            latency_ms=round(latency_ms or 0, 2),
                            success=True,
                            status="measured",
                            error=None
                        )
            except Exception:
                continue

        if latency_ms is not None:
            return await self._latency_test(name, base_url, session, latency_ms)
        return SpeedTestResult(
            endpoint_name=name,
            url=base_url,
            speed_mbps=0.0,
            latency_ms=0.0,
            success=False,
            error="Could not measure latency or speed",
            status="error"
        )

    async def scan_all_endpoints(self, concurrent: int = 5) -> list[SpeedTestResult]:
        """Scan all CDN endpoints."""
        self.results = []
        total = len(STEAM_CDN_ENDPOINTS)
        self.progress = ProgressDisplay(total)
        
        connector = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            semaphore = asyncio.Semaphore(concurrent)

            async def limited_test(name: str, url: str):
                async with semaphore:
                    result = await self.test_endpoint(session, name, url)
                    self.progress.update(result)
                    if self.show_progress:
                        print(self.progress.render(name), end="", flush=True)
                        await asyncio.sleep(0.03)
                        print(self.progress.clear_line(), end="", flush=True)
                    return result

            limited_tasks = [
                limited_test(name, url)
                for name, url in STEAM_CDN_ENDPOINTS.items()
            ]

            self.results = await asyncio.gather(*limited_tasks)

            # Speed test for top 10 by latency
            print(f"\n\n  {get_color('⚡', Colors.YELLOW)} {get_color('Testing real download speed for top 10 regions...', Colors.BOLD + Colors.CYAN)}\n")

            latency_sorted = sorted(
                [r for r in self.results if r.success],
                key=lambda x: x.latency_ms if x.latency_ms > 0 else float('inf')
            )[:10]

            for i, result in enumerate(latency_sorted, 1):
                done = False
                start_t = time.perf_counter()

                async def animate():
                    frame_idx = 0
                    while not done:
                        elapsed = time.perf_counter() - start_t
                        spinner = SPINNER_FRAMES[frame_idx % len(SPINNER_FRAMES)]
                        line = f"  [{get_color(f'{i}', Colors.CYAN)}/{get_color('10', Colors.CYAN)}] {get_color(spinner, Colors.CYAN)} Testing {get_color(result.endpoint_name, Colors.WHITE)}  {get_color(f'{elapsed:4.0f}s', Colors.DIM)}"
                        print(f"{line:<79}", end="\r", flush=True)
                        frame_idx += 1
                        await asyncio.sleep(0.1)

                anim_task = asyncio.create_task(animate())
                speed_result = await self.measure_real_speed(session, result.endpoint_name, result.url)
                done = True
                anim_task.cancel()
                line = f"  [{get_color(f'{i}', Colors.CYAN)}/{get_color('10', Colors.CYAN)}] {get_color('✓', Colors.GREEN)} {result.endpoint_name:<34} {get_color(f'{speed_result.speed_mbps:>6.2f} Mbps', Colors.GREEN)}  {get_color(f'{speed_result.latency_ms:>6.0f}ms', Colors.BLUE)}"
                print(f"{line:<79}", end="\r", flush=True)
                for j, r in enumerate(self.results):
                    if r.endpoint_name == result.endpoint_name:
                        self.results[j] = speed_result
                        break
            print()

        print(" " * 80 + "\r", end="", flush=True)
        measured = [r for r in self.results if r.status == "measured"]
        estimated = [r for r in self.results if r.status != "measured"]
        measured.sort(key=lambda x: x.speed_mbps, reverse=True)
        estimated.sort(key=lambda x: x.speed_mbps, reverse=True)
        self.results = measured + estimated
        return self.results
    
    def print_results(self):
        """Print formatted speed test results with professional UI."""
        print()
        
        # Header
        print(get_color("╔" + "═" * 78 + "╗", Colors.CYAN))
        print(get_color("║", Colors.CYAN) + UI.center_text(get_color("📊 STEAM DOWNLOAD REGION SPEED TEST RESULTS", Colors.BOLD + Colors.WHITE), 78) + get_color("║", Colors.CYAN))
        print(get_color("╚" + "═" * 78 + "╝", Colors.CYAN))
        print()
        
        if not self.results:
            print(get_color("  No results available. Run scan first.", Colors.RED))
            return
        
        successful = [r for r in self.results if r.success]
        failed = [r for r in self.results if not r.success]
        
        # Summary stats
        print(f"  {get_color('📈 SUMMARY:', Colors.BOLD + Colors.CYAN)}")
        print(f"  ┌" + "─" * 76 + "┐")
        print(f"  │  Total Regions: {get_color(f'{len(self.results):>3}', Colors.WHITE)}  |  {get_color('✓', Colors.GREEN)} Success: {get_color(f'{len(successful):>3}', Colors.GREEN)}  |  {get_color('✗', Colors.RED)} Failed: {get_color(f'{len(failed):>3}', Colors.RED)}{' ' * 34}│")
        print(f"  └" + "─" * 76 + "┘")
        print()
        
        # Top 10 Results
        print(f"  {get_color('🏆 TOP 10 FASTEST REGIONS:', Colors.BOLD + Colors.YELLOW)}")
        print(f"  ┌{'─' * 76}┐")
        print(f"  │ {get_color('Rank', Colors.GRAY):<6} {get_color('Region', Colors.GRAY):<32} {get_color('Speed (Mbps)', Colors.GRAY):<16} {get_color('Latency', Colors.GRAY):<12} │")
        print(f"  ├{'─' * 76}┤")
        
        top_results = successful[:10]
        for i, result in enumerate(top_results, 1):
            # Medal icons and colors
            if i == 1:
                rank = get_color("🥇 1", Colors.YELLOW + Colors.BOLD)
                speed_color = Colors.GREEN + Colors.BOLD
            elif i == 2:
                rank = get_color("🥈 2", Colors.CYAN + Colors.BOLD)
                speed_color = Colors.GREEN
            elif i == 3:
                rank = get_color("🥉 3", Colors.MAGENTA + Colors.BOLD)
                speed_color = Colors.GREEN
            else:
                rank = get_color(f"   {i}", Colors.GRAY)
                speed_color = Colors.WHITE if result.speed_mbps >= 10 else Colors.YELLOW
            
            # Speed color based on value
            if result.status == "measured":
                if result.speed_mbps >= 50:
                    speed_color = Colors.GREEN + Colors.BOLD
                elif result.speed_mbps >= 10:
                    speed_color = Colors.GREEN
                elif result.speed_mbps >= 1:
                    speed_color = Colors.YELLOW
                else:
                    speed_color = Colors.ORANGE
            
            speed_display = get_color(f"{result.speed_mbps:>10.2f}", speed_color)
            latency_display = f"{result.latency_ms:>8.1f}ms"
            
            region_name = result.endpoint_name[:30] if len(result.endpoint_name) > 30 else result.endpoint_name
            
            status_icon = get_color("✓", Colors.GREEN) if result.status == "measured" else get_color("~", Colors.CYAN)
            
            print(f"  │ {rank}  {region_name:<32} {speed_display}  {get_color(latency_display, Colors.BLUE):<12} {status_icon} │")
        
        print(f"  └{'─' * 76}┘")
        print()
        
        # Failed connections
        if failed:
            print(f"  {get_color('❌ FAILED CONNECTIONS:', Colors.BOLD + Colors.RED)}")
            print(f"  ┌{'─' * 76}┐")
            for result in failed[:15]:  # Show first 15 failures
                error_color = Colors.RED if "Timeout" in str(result.error) else Colors.YELLOW
                error_display = get_color(result.error, error_color)
                region_name = result.endpoint_name[:45] if len(result.endpoint_name) > 45 else result.endpoint_name
                print(f"  │   • {region_name:<43} {error_display:<25} │")
            if len(failed) > 15:
                print(f"  │   {get_color(f'... and {len(failed) - 15} more', Colors.GRAY):<74} │")
            print(f"  └{'─' * 76}┘")
            print()
        
        # Recommendation
        if successful:
            actual_speed = [r for r in successful if r.status == "measured"]
            best = actual_speed[0] if actual_speed else successful[0]
            
            test_type = "Measured" if best.status == "measured" else "Latency estimate"
            test_icon = "⚡" if best.status == "measured" else "📶"
            
            print(get_color("╔" + "═" * 78 + "╗", Colors.GREEN))
            print(get_color("║", Colors.GREEN) + " " * 78 + get_color("║", Colors.GREEN))
            print(get_color("║", Colors.GREEN) + UI.center_text(f"{get_color('🏆', Colors.YELLOW)} {get_color('RECOMMENDED REGION', Colors.BOLD + Colors.WHITE)}", 78) + get_color("║", Colors.GREEN))
            print(get_color("║", Colors.GREEN) + " " * 78 + get_color("║", Colors.GREEN))
            print(get_color("║", Colors.GREEN) + UI.center_text(f"{get_color(best.endpoint_name, Colors.GREEN + Colors.BOLD)}  {get_color(test_icon + ' ' + test_type, Colors.GRAY)}", 78) + get_color("║", Colors.GREEN))
            print(get_color("║", Colors.GREEN) + " " * 78 + get_color("║", Colors.GREEN))
            print(get_color("║", Colors.GREEN) + UI.center_text(f"{get_color('⚡ Speed:', Colors.CYAN)} {get_color(f'{best.speed_mbps:.2f} Mbps', Colors.GREEN + Colors.BOLD)}  |  {get_color('📶 Latency:', Colors.CYAN)} {get_color(f'{best.latency_ms:.1f} ms', Colors.YELLOW)}", 78) + get_color("║", Colors.GREEN))
            print(get_color("║", Colors.GREEN) + " " * 78 + get_color("║", Colors.GREEN))
            print(get_color("╚" + "═" * 78 + "╝", Colors.GREEN))
            print()
            
            # Instructions
            print(f"  {get_color('📝 HOW TO APPLY:', Colors.BOLD + Colors.CYAN)}")
            print(f"  ┌{'─' * 76}┐")
            print(f"  │  1. Open Steam → Settings → Downloads{' ' * 36}│")
            print(f"  │  2. Change 'Download Region' to: {get_color(best.endpoint_name.split(' - ')[0] if ' - ' in best.endpoint_name else best.endpoint_name, Colors.GREEN):<42}│")
            print(f"  │  3. Restart Steam for changes to take effect{' ' * 32}│")
            print(f"  └{'─' * 76}┘")
            print()


async def main():
    """Main entry point."""
    # Header
    print()
    print(get_color("╔" + "═" * 78 + "╗", Colors.CYAN))
    print(get_color("║", Colors.CYAN) + " " * 78 + get_color("║", Colors.CYAN))
    print(get_color("║", Colors.CYAN) + UI.center_text(f"{get_color('🚀', Colors.YELLOW)} {get_color('STEAM SPEED SCANNER', Colors.BOLD + Colors.WHITE)}", 78) + get_color("║", Colors.CYAN))
    print(get_color("║", Colors.CYAN) + UI.center_text(get_color('Find the fastest download region for your connection', Colors.DIM + Colors.CYAN), 78) + get_color("║", Colors.CYAN))
    print(get_color("║", Colors.CYAN) + " " * 78 + get_color("║", Colors.CYAN))
    print(get_color("╚" + "═" * 78 + "╝", Colors.CYAN))
    print()
    
    print(f"  {get_color('🌍', Colors.CYAN)} Scanning {get_color(f'{len(STEAM_CDN_ENDPOINTS)} regions', Colors.BOLD + Colors.WHITE)}...")
    print(f"  {get_color('⚡', Colors.YELLOW)} Testing latency and download speed")
    print()
    
    scanner = SteamSpeedScanner(timeout_seconds=15, show_progress=True)
    results = await scanner.scan_all_endpoints(concurrent=5)
    scanner.print_results()
    
    print()
    print(f"  {get_color('═' * 60, Colors.GRAY)}")
    print(f"  {get_color('Press ENTER to exit...', Colors.DIM + Colors.WHITE)}")
    print(f"  {get_color('═' * 60, Colors.GRAY)}")
    try:
        input()
    except Exception:
        import time
        time.sleep(5)
    return scanner.results


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n\n  {get_color('[Scan cancelled by user]', Colors.RED)}\n")
    except Exception as e:
        print(f"\n\n  {get_color(f'[ERROR: {e}]', Colors.RED)}\n")
