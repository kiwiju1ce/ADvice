## 포팅 메뉴얼

### 사용 외부 API
1. Google Vision API
2. Google Translation API

### nginx 설치
```bash
 sudo apt-get install nginx
 sudo vim /etc/nginx/default.conf
```
default.conf를 해당 위치에 저장합니다.

### 도커 / 도커 컴포즈 설치
```bash
sudo apt update
sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
``