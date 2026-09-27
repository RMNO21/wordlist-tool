import math
import sys
import time
from itertools import permutations, product

# Ensure UTF-8 output on consoles that support it (prevents Windows codepage 1256/437 crashes)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

def run():
    ############################################################################################
    # Copyright (C) 2025-2026 Raman Tondro
    #
    # This program is free software; you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation; either version 2 of the License, or
    # (at your option) any later version.
    ############################################################################################

    banner = r"""
 __      __               .___________.__          __   ___________           .__   
/  \    /  \___________  __| _/\_____  \  |__  __ _|  |_ \__    ___/___   ____ |  |  
\   \/\/   /  _ \_  __ \/ __ |  /  ____/  |  \|  |  \   __\ |    | /  _ \ /  _ \|  |  
 \        (  <_> )  | \/ /_/ | /       \   Y  \  |  /|  |   |    |(  <_> |  <_> )  |__
  \__/\  / \____/|__|  \____ | \_______ \___|_/____/ |__|   |____| \____/ \____/|____/
       \/                   \/         \/                                             
    https://github.com/RMNO21/wordlist-tool/
    """
    try:
        print(banner)
    except Exception:
        print("\n=== Wordlist-Tool (https://github.com/RMNO21/wordlist-tool/) ===\n")

    def get_loopnum(max_len):
        while True:
            try:
                loop_input = input(f"Enter the loop/depth number (1-{min(10, max_len)}, default {min(2, max_len)}): ").strip()
                if not loop_input:
                    return min(2, max_len)
                loop = int(loop_input)
                if 0 < loop <= min(10, max_len):
                    return loop
                print(f"Error: loop must be between 1 and {min(10, max_len)}.")
            except ValueError:
                print("Error: please enter a valid integer.")

    def calc_total_words(words_list, loop_depth):
        total = 0
        c = len(words_list)
        for i in range(loop_depth):
            for combo in permutations(range(c), i + 1):
                total += math.prod(len(words_list[x]) for x in combo)
        return total

    def generate_preview_samples(words_list, loop_depth, separator, max_samples=6):
        samples = []
        c = len(words_list)
        for i in range(loop_depth):
            for combo in permutations(range(c), i + 1):
                for alt in product(*[words_list[x] for x in combo]):
                    samples.append(separator.join(alt))
                    if len(samples) >= max_samples:
                        return samples
        return samples

    # Collect word categories
    a = []
    c = 0
    print("Enter target keywords / patterns (use ',' for OR options, e.g. 'admin,user')")
    print("Press Enter on an empty line or type 'done' to finish:")

    while True:
        b = input(f"[{c + 1}]: ").strip()
        if b.lower() == "done" or b == "":
            break
        items = [x.strip() for x in b.split(',') if x.strip()]
        if items:
            a.append(items)
            c += 1

    if not a:
        print("[!] No keywords entered. Exiting.")
        return

    # Configuration loop with live preview and tweak support
    loop = get_loopnum(c)
    sep = input("Enter separator (e.g. '@', '_', '-', press Enter for none): ")

    while True:
        total_est = calc_total_words(a, loop)
        preview_samples = generate_preview_samples(a, loop, sep, max_samples=6)

        print("\n" + "=" * 55)
        print(" [*] SETTINGS & SAMPLE PREVIEW")
        print("=" * 55)
        print(f"  * Loop Depth     : {loop}")
        print(f"  * Separator      : '{sep}'")
        print(f"  * Estimated Words: {total_est:,} combinations")
        print("  * Sample Output  :")
        for idx, sample in enumerate(preview_samples, 1):
            print(f"     {idx}. {sample}")
        if total_est > len(preview_samples):
            print(f"     ... ({total_est - len(preview_samples):,} more)")
        print("=" * 55)

        choice = input("Proceed to generate? [Y = Yes / T = Tweak settings / N = Cancel]: ").strip().lower()
        if choice in ('y', 'yes', ''):
            break
        elif choice in ('t', 'tweak'):
            loop = get_loopnum(c)
            sep = input("Enter new separator (press Enter for none): ")
        else:
            print("[!] Generation cancelled by user.")
            return

    outfile = input("\nEnter output filename (e.g. wordlist.txt): ").strip()
    if not outfile:
        outfile = "wordlist.txt"

    print(f"\n[+] Generating {total_est:,} words...")
    start_time = time.time()
    generated_count = 0

    # High-speed buffered stream generation
    with open(outfile, "w", encoding="utf-8", buffering=1024*1024) as f:
        for i in range(loop):
            for combo in permutations(range(c), i + 1):
                for alt in product(*[a[x] for x in combo]):
                    f.write(sep.join(alt) + "\n")
                    generated_count += 1

    elapsed = max(1e-5, time.time() - start_time)
    throughput = generated_count / elapsed

    print(f"[OK] Success! Generated {generated_count:,} words in {elapsed:.3f}s ({throughput:,.0f} words/sec).")
    print(f"[OK] Saved to: {outfile}")

if __name__ == "__main__":
    run()
