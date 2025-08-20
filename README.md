# 📡 Pryamoy Kanal  

> 🕒 Um agregador cronológico de redes sociais — sem algoritmos de recomendação.  

---

![Laravel](https://img.shields.io/badge/Laravel-12.x-red?logo=laravel)  
![PHP](https://img.shields.io/badge/PHP-8.2-blue?logo=php)  
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)  
![Redis](https://img.shields.io/badge/Cache-Redis-red?logo=redis)  
![License](https://img.shields.io/badge/license-MIT-green)  
![Status](https://img.shields.io/badge/status-Em%20desenvolvimento-yellow)  

---

## ✨ Visão Geral

O **Pryamoy Kanal** (Прямой Канал = *Canal Direto*) é um projeto que reúne publicações de várias redes sociais em um único feed **100% cronológico**.  
Sem filtros, sem manipulação, sem algoritmos de recomendação.  

---

## 🚀 Funcionalidades

- 🔗 Integração com múltiplas redes sociais  
- 🕒 Linha do tempo **cronológica**  
- 👤 Perfis para usuários e criadores de conteúdo  
- 🔍 Filtros por rede e tipo de post  
- 💬 Interações básicas *(planejado)*  

---

## 🛠️ Tecnologias

- **Backend:** Laravel + PHP 8.2  
- **Banco de dados:** PostgreSQL (com particionamento para performance)  
- **Cache:** Redis para feed rápido  
- **Infra:** Docker, Horizon (queues), futura escalabilidade horizontal  

---

## 📌 Objetivo

Dar controle de volta ao usuário: um feed **simples e direto**, que respeita a ordem real das publicações.  

---

## 🤝 Contribuição

Quer ajudar? Faça um fork, crie sua branch e abra um Pull Request:  

```bash
git checkout -b minha-feature
git commit -m "feat: adiciona nova funcionalidade X"
git push origin minha-feature
