#!/bin/bash

# HackBot v2.0 by Cria - Termux & MSYS2
# Menu colorido e mais ferramentas

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # sem cor

banner() {
    clear
    echo -e "${CYAN}"
    echo "========================================="
    echo "            🚀 HackBot v2.0 🚀"
    echo "        By Cria | Termux & MSYS2"
    echo "========================================="
    echo -e "${NC}"
}

menu() {
    banner
    echo -e "${GREEN}1)${NC} Scan de rede com Nmap"
    echo -e "${GREEN}2)${NC} Whois"
    echo -e "${GREEN}3)${NC} Ping"
    echo -e "${GREEN}4)${NC} Traceroute"
    echo -e "${GREEN}5)${NC} Aircrack-ng (placeholder)"
    echo -e "${GREEN}6)${NC} Sair"
    echo ""
    read -p "Escolhe a opção 👉 " opcao

    case $opcao in
        1) nmap_scan ;;
        2) whois_lookup ;;
        3) ping_host ;;
        4) traceroute_host ;;
        5) aircrack_placeholder ;;
        6) exit ;;
        *) echo -e "${RED}Opção inválida!${NC}"; sleep 1; menu ;;
    esac
}

nmap_scan() {
    read -p "Digite o IP ou domínio pra scan 👉 " alvo
    echo -e "${YELLOW}Rodando Nmap no $alvo...${NC}"
    nmap -A -T4 "$alvo"
    read -p "Pressiona ENTER pra voltar ao menu"
    menu
}

whois_lookup() {
    read -p "Digite o domínio pra consulta WHOIS 👉 " dominio
    echo -e "${YELLOW}Consultando WHOIS em $dominio...${NC}"
    whois "$dominio"
    read -p "Pressiona ENTER pra voltar ao menu"
    menu
}

ping_host() {
    read -p "Digite o IP ou domínio pra pingar 👉 " alvo
    echo -e "${YELLOW}Pingando $alvo (5 pacotes)...${NC}"
    ping -c 5 "$alvo"
    read -p "Pressiona ENTER pra voltar ao menu"
    menu
}

traceroute_host() {
    read -p "Digite o IP ou domínio pra traceroute 👉 " alvo
    echo -e "${YELLOW}Fazendo traceroute para $alvo...${NC}"
    traceroute "$alvo"
    read -p "Pressiona ENTER pra voltar ao menu"
    menu
}

aircrack_placeholder() {
    echo ""
    echo -e "${RED}⚠️ Aircrack-ng precisa de Linux com modo monitor!${NC}"
    echo "👉 Não rola no Termux nem MSYS2."
    echo "✅ Use Kali Linux, Parrot ou Ubuntu pra isso."
    read -p "Pressiona ENTER pra voltar ao menu"
    menu
}

menu
