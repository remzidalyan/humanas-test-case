# 🧠 Humanas Test Case - Fullstack Proje (Laravel + React + Django)

Bu proje, üç farklı teknolojiyi bir arada barındırır:

- **Laravel** (Backend - API servisleri)
- **React** (Frontend - sadece dışa açık servis)
- **Django** (Python API - tahminleme vs. için kullanılır)

Projeler, Docker Compose ile birlikte tek bir yapı içinde ayağa kaldırılır ve dışa sadece React servisi açılır. Bu
mimari hem local geliştirme hem de production için optimize edilmiştir.

---

## 📋 Sistem Gereksinimleri

- Docker (>= 20.x)
- Docker Compose (>= 2.x)
- WSL2 (Windows kullanıcıları için önerilir)
- 8GB+ RAM (minimum)
- Python 3.10+ (Sadece Django için özel geliştirmelerde)
- Node.js 18+ (sadece frontend build için özel durumlarda, ancak container içinde yapılması önerilir)

> Windows kullanıcıları için WSL 2 kullanması durumunda aktif olmalıdır. Linux kullanıcıları ekstra bir işlem yapmadan
> çalıştırabilir.

## 🌐 Docker Ağı (Network)

Tüm servisler aynı özel Docker ağı üzerinde çalışır:

```yaml
networks:
  humanas-test-case:
    external: true
```

---

## 🛠️ Kurulum

### 1. Geliştirme Ortamı

```bash
git clone https://github.com/remzidalyan/humanas-test-case.git
cd humanas-test-case
```

```bash
docker network create humanas-test-case  # Ortak ağ ilk kez oluşturulmalı
docker compose up --build
```

### 2. Canlı Ortamı

```bash
docker network create humanas-test-case # Ortak ağ ilk kez oluşturulmalı
docker compose -f docker-compose.prod.yml up --build -d
```

## 🔧 Ortam Değişkenleri

### 1. Geliştirme Ortamı

env dosyalarındaki url değişkenleri localhost olarak ayarlanmıştır. Eğer farklı bir url veya port kullanıyorsanız, bu
dosyaları güncelleyebilirsiniz.

### 2. Canlı Ortamı

env dosyalarındaki url değişkenleri canlı ortamda kullanılacak şekilde ayarlanmıştır. Eğer farklı bir url veya port
kullanıyorsanız, bu dosyaları güncelleyebilirsiniz.

## 📂 Proje Yapısı

```bash
.
├── backend        # Laravel
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── uploads.ini
│   └── .env.example
├── frontend       # React
│   ├── Dockerfile
│   └── Dockerfile.dev
├── mlapi          # Django + ML Model
│   └── Dockerfile
├── docker-compose.yml          # Geliştirme ortamı
├── docker-compose.prod.yml     # Üretim ortamı
└── README.md
```

## 🔍 Servisler ve Rolleri

| Servis     | Açıklama                               | Port            | Durum                  |
|------------|----------------------------------------|-----------------|------------------------|
| `backend`  | Ana backend API servisi                | `(expose:9000)` | Private / Sadece Nginx |
| `mlapi`    | Python ile yazılmış tahminleme servisi | `5000`          | Private                |
| `frontend` | Kullanıcı arayüzü                      | `80:3000`       | Public                 |
| `db`       | Laravel tarafından kullanılır          | `3306`          | Private                |
| `nginx`    | React için reverse proxy               | `8081:80`       | Public                 |

## 📞 Destek

Herhangi bir sorunla karşılaşırsanız bu repo altında [Issue](https://github.com/remzidalyan/humanas-test-case/issues)
açabilirsiniz.