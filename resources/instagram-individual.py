import instaloader
import json
import os

# Inicializa o Instaloader
L = instaloader.Instaloader()

# -------------------------------
# Função: salvar dados em JSON (arquivo individual)
# -------------------------------
def save_to_json(data, filename: str, output_dir: str = "instagram_data"):
    """Salva dados em JSON em um arquivo específico."""
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, filename)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Dados salvos em {output_file}")
    return output_file


# -------------------------------
# Função: registrar no log geral
# -------------------------------
def append_to_log(data, output_dir: str = "instagram_data", log_file: str = "log.json"):
    """Acumula todos os resultados em um único log.json."""
    os.makedirs(output_dir, exist_ok=True)
    log_path = os.path.join(output_dir, log_file)

    # Se já existe, carrega
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            try:
                log_data = json.load(f)
            except json.JSONDecodeError:
                log_data = []
    else:
        log_data = []

    # Adiciona novo dado (se for lista, junta todos)
    if isinstance(data, list):
        log_data.extend(data)
    else:
        log_data.append(data)

    # Salva atualizado
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)

    print(f"📒 Log atualizado em {log_path}")


# -------------------------------
# Função: baixar dados de um post via URL
# -------------------------------
def get_post_data(post_url: str, output_dir: str = "instagram_data"):
    """Extrai informações de um post público a partir da URL, salva e registra no log."""
    shortcode = post_url.rstrip("/").split("/")[-1]
    post = instaloader.Post.from_shortcode(L.context, shortcode)

    post_info = {
        "shortcode": shortcode,
        "url": post_url,
        "author": post.owner_username,
        "caption": post.caption,
        "likes": post.likes,
        "comments": post.comments,
        "is_video": post.is_video,
        "media_url": post.url,
        "date": post.date_utc.isoformat()
    }

    # Salvar individual
    save_to_json(post_info, f"{shortcode}_post.json", output_dir)

    # Registrar no log geral
    append_to_log(post_info, output_dir)

    return post_info


# -------------------------------
# Função: baixar posts de um perfil
# -------------------------------
def get_profile_posts(username: str, limit: int = 5, output_dir: str = "instagram_data"):
    """Extrai posts de um perfil público, salva e registra no log."""
    os.makedirs(output_dir, exist_ok=True)

    profile = instaloader.Profile.from_username(L.context, username)

    posts_data = []
    for idx, post in enumerate(profile.get_posts(), start=1):
        post_info = {
            "shortcode": post.shortcode,
            "url": f"https://www.instagram.com/p/{post.shortcode}/",
            "author": post.owner_username,
            "caption": post.caption,
            "likes": post.likes,
            "comments": post.comments,
            "is_video": post.is_video,
            "media_url": post.url,
            "date": post.date_utc.isoformat()
        }
        posts_data.append(post_info)
        print(f"📌 Post {idx}: {post_info['url']}")

        if limit and idx >= limit:
            break

    # Salvar individual
    save_to_json(posts_data, f"{username}_posts.json", output_dir)

    # Registrar no log geral
    append_to_log(posts_data, output_dir)

    return posts_data


# -------------------------------
# Exemplo de uso
# -------------------------------
if __name__ == "__main__":
    # Exemplo 1: pegar dados de um post específico
    post_url = "https://www.instagram.com/p/DOyxebhia79/"
    post_data = get_post_data(post_url)
    print("\n🔎 Post único:")
    print(json.dumps(post_data, indent=2, ensure_ascii=False))

    # Exemplo 2: pegar posts de um perfil
    username = "adelle.fr"
    profile_posts = get_profile_posts(username, limit=5)
    print(f"\n📊 Total coletado do perfil {username}: {len(profile_posts)} posts")
