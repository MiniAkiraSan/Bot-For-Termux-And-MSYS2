#!/usr/bin/env python3
import os
import sys

# Cores ANSI para terminal
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
NC = '\033[0m'  # sem cor

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{CYAN}{'='*40}")
    print("            🚀 HackBot v2.0 🚀")
    print("        By Cria | Termux & MSYS2")
    print(f"{'='*40}{NC}")

def run_cmd(command):
    os.system(command)

def nmap_scan():
    alvo = input("👉 Digita o IP ou domínio pra scan: ")
    print(f"{YELLOW}Rodando Nmap em {alvo}...{NC}")
    run_cmd(f"nmap -A -T4 {alvo}")
    input("
Pressiona ENTER pra voltar...")

def whois_lookup():
    dominio = input("👉 Digita o domínio pra consulta WHOIS: ")
    print(f"{YELLOW}Consultando WHOIS em {dominio}...{NC}")
    run_cmd(f"whois {dominio}")
    input("
Pressiona ENTER pra voltar...")

def ping_host():
    alvo = input("👉 Digita o IP ou domínio pra pingar: ")
    print(f"{YELLOW}Pingando {alvo} (5 pacotes)...{NC}")
    run_cmd(f"ping -c 5 {alvo}")
    input("
Pressiona ENTER pra voltar...")

def traceroute_host():
    alvo = input("👉 Digita o IP ou domínio pra traceroute: ")
    print(f"{YELLOW}Fazendo traceroute para {alvo}...{NC}")
    run_cmd(f"traceroute {alvo}")
    input("
Pressiona ENTER pra voltar...")

def aircrack_placeholder():
    print(f"
{RED}⚠️ Aircrack-ng precisa de Linux com modo monitor!{NC}")
    print("👉 Não rola no Termux nem MSYS2.")
    print("✅ Use Kali Linux, Parrot ou Ubuntu pra isso.
")
    input("Pressiona ENTER pra voltar...")

def menu():
    while True:
        banner()
        print(f"{GREEN}1){NC} Scan de rede com Nmap")
        print(f"{GREEN}2){NC} Whois")
        print(f"{GREEN}3){NC} Ping")
        print(f"{GREEN}4){NC} Traceroute")
        print(f"{GREEN}5){NC} Aircrack-ng (placeholder)")
        print(f"{GREEN}6){NC} Sair")
        escolha = input("
Escolhe a opção 👉 ")

        if escolha == '1':
            nmap_scan()
        elif escolha == '2':
            whois_lookup()
        elif escolha == '3':
            ping_host()
        elif escolha == '4':
            traceroute_host()
        elif escolha == '5':
            aircrack_placeholder()
        elif escolha == '6':
            sys.exit()
        else:
            print(f"{RED}Opção inválida!{NC}")
            input("Pressiona ENTER pra continuar...")

if __name__ == '__main__':
    menu()
