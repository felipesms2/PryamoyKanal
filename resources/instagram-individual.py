import instaloader
import json
import os

# Inicializa o Instaloader
L = instaloader.Instaloader()

# -------------------------------
# Função: salvar dados em JSON
# -------------------------------
def save_to_json(data, filename: str, output_dir: str = "instagram_data"):
    """Salva qualquer dado (dict ou list) em um arquivo JSON."""
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, filename)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Dados salvos em {output_file}")
    return output_file


# -------------------------------
# Função: baixar dados de um post via URL
# -------------------------------
def get_post_data(post_url: str, output_dir: str = "instagram_data"):
    """Extrai informações de um post público a partir da URL e salva em JSON."""
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

    # Salvar automaticamente
    save_to_json(post_info, f"{shortcode}_post.json", output_dir)

    return post_info


# -------------------------------
# Função: baixar posts de um perfil
# -------------------------------
def get_profile_posts(username: str, limit: int = 5, output_dir: str = "instagram_data"):
    """Extrai posts de um perfil público, salva em JSON e retorna os dados."""
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

        if limit and idx >= limit:  # Se limite for 0, pega todos
            break

    # Salva em JSON automaticamente
    save_to_json(posts_data, f"{username}_posts.json", output_dir)

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
    get_profile_posts(username, limit=5)
