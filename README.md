# Multi-threaded Proxy Account Creation

```
┌─────────────────┐
│ proxy_links.txt │
└────────┬────────┘
         │ Read & Shuffle
         ▼
┌─────────────────┐
│ Proxy List      │
│ ┌─────┐ ┌─────┐ │
│ │Proxy│ │Proxy│ │
│ │  1  │ │  2  │ │
│ └─────┘ └─────┘ │
│     ...         │
└────────┬────────┘
         │ Create Threads
         ▼
┌─────────────────────────────────────────┐
│              Thread Pool                │
│ ┌─────────┐ ┌─────────┐     ┌─────────┐ │
│ │Thread 1 │ │Thread 2 │ ... │Thread N │ │
│ │(Proxy 1)│ │(Proxy 2)│     │(Proxy N)│ │
│ └────┬────┘ └────┬────┘     └────┬────┘ │
└──────┼──────────┼──────────────┼───────┘
       │          │              │
       ▼          ▼              ▼
┌─────────────────────────────────────────┐
│         Account Creation Process         │
│                                         │
│ For each thread:                        │
│ 1. Wait random interval (2-10 seconds)  │
│ 2. Use assigned proxy for requests      │
│ 3. Create account                       │
│ 4. Save account info                    │
│ 5. Repeat until stopped                 │
└─────────────────────────────────────────┘
```

## Process Breakdown:

1. **Load Proxies:**
   ```python
   with open("proxy_links.txt", "r") as file:
       proxy_links = file.readlines()
   random.shuffle(proxy_links)
   ```

2. **Create Threads:**
   ```python
   for index, proxy_url in enumerate(proxy_links[:register.num_threads]):
       thread = threading.Thread(target=automate_registration_loop, 
                                 args=(register, proxy_url.strip(), index))
       threads.append(thread)
       thread.start()
   ```

3. **Registration Loop:**
   ```python
   def automate_registration_loop(register, proxy_url, thread):
       while not stop_flag.is_set():
           sleep_duration = random.randint(2, 10)
           time.sleep(sleep_duration)
           register.register_user(proxy_url, thread)
   ```

4. **Use Proxy in Requests:**
   ```python
   proxies = {
       "http": f"http://{proxy_url}",
       "https": f"http://{proxy_url}",
   }
   response = session.request(method, url, ..., proxies=proxies)
   ```

5. **Handle Interrupts:**
   ```python
   try:
       while any(thread.is_alive() for thread in threads):
           for thread in threads:
               thread.join(timeout=0.5)
           if stop_flag.is_set():
               break
   except KeyboardInterrupt:
       print("Interrupt received. Stopping threads...")
       stop_flag.set()
   ```

## Key Points:

- Proxies are loaded from a file and shuffled for random distribution.
- Each thread is assigned a unique proxy.
- Threads operate independently, creating accounts through their assigned proxies.
- Random intervals between registrations help avoid detection.
- The main thread monitors for interrupts and can stop all threads gracefully.

## An example:

Generating 100 accounts with 5 proxies:

```
Proxy 1 (proxy1.example.com:8080):  [A][A][A][A][A]...[A]  (20 accounts)
Proxy 2 (proxy2.example.com:3128):  [A][A][A][A][A]...[A]  (20 accounts)
Proxy 3 (proxy3.example.com:80):    [A][A][A][A][A]...[A]  (20 accounts)
Proxy 4 (proxy4.example.com:443):   [A][A][A][A][A]...[A]  (20 accounts)
Proxy 5 (proxy5.example.com:8888):  [A][A][A][A][A]...[A]  (20 accounts)
```

------------------------------------------------GENERAL SETTINGS--------------------------------------------------------
WALLETS_TO_WORK = 0 | The software will take wallets from the table according to the rules described below 0 = all
wallets in sequence 3 = only wallet No. 3 4, 20 = wallets No. 4 and No. 20
[5, 25] = wallets from No. 5 to No. 25

    ACCOUNTS_IN_STREAM      | Number of wallets in the stream to execute. If there are 100 wallets in total, and 10 is specified,
                                then the software will make 10 rounds of 10 wallets each

    EXCEL_PASSWORD          | Enables password prompt when entering the software. First, set the password in the table
    EXCEL_PAGE_NAME         | The name of the sheet in the table. Example: 'creoPlay'

--------------------------------------------CLASSIC-ROUTES CONTROL------------------------------------------------------

    mint_creoPlay_tokens           # mint $BNB on creoPlay Faucet
    transfer_bnb                   # swap on BEX ($BNB -> $BTC)
          
    Select the necessary modules for interaction
    You can create any route, the software will work strictly according to it. For each list, one module will be selected
    into the route, if the software selects None, it will skip that list of modules.
    The list of modules is above.

    CLASSIC_ROUTES_MODULES_USING = [
        ['transfer_bnb'],
        ['mint_nft'],
        ['make_market_item'],
        ['create_market_sale'],
        ['swap_quickswap_okx_usdc'],
        ['buy_creo_token'],
        ['save_pvp_log'],
        ['save_battle_log'],
        ['save_activity_log']
        ...
    ]

"""


