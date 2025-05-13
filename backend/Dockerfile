FROM php:8.1-fpm

# Sistem paketleri + PHP eklentileri
RUN apt-get update && apt-get install -y \
      zip unzip curl libpng-dev libonig-dev libxml2-dev \
      git libcurl4-openssl-dev libzip-dev \
    && docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd zip \
    && docker-php-ext-enable opcache

# php.ini üzerine kendi ayarlarımızı kopyala
COPY uploads.ini /usr/local/etc/php/conf.d/99-uploads.ini

# Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html

COPY composer.json composer.lock ./
RUN composer install --no-scripts --no-autoloader

COPY . .

RUN composer dump-autoload --optimize \
 && php artisan key:generate

EXPOSE 9000
CMD ["php-fpm"]
