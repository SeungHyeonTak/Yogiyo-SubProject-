## YOGIYO CLONE PROJECT
요기요를 클론하여 만드는 개인프로젝트이고, 백엔드는 DRF를 사용하며 프론트는 따로 구성하지 않는다. <br> 
그리고 사장님 사이트(백오피스)는 Django_template을 사용하여 html, scss, javascript를 사용한다.
(* 사장님 사이트는 효과적인 작업을 위해 기본 설명만 있는 페이지는 제외함)

### Installation (설치 방법)

-----
- 가상환경 install
```bash
$ pyenv virtualenv 3.6.4 YGY
$ pyenv local pyenv
```

- requirements.txt install
```bash
$ pip install -r requirements.txt
```

### Usage (사용 방법)

-----

- api와 owner_site는 접속하는 url이 따로 설정 되어 runserver로 접속하는 방법이 다르다.

- api (local)
```bash
$ ./manage.py runserver 127.0.0.1:8100 --settings=config.settings.api-local
```

- api (prod)
```bash
$ ./manage.py runserver 127.0.0.1:8100 --settings=config.settings.api-prod
```

- owner_site (local)
```bash
$ ./manage.py runserver 127.0.0.1:8109 --settings=config.settings.mng_local
```

- owner_site (prod)
```bash
$ ./manage.py runserver 127.0.0.1:8109 --settings=config.settings.mng_prod
```

### Contributing (기여 방법)

-----

### License (라이센스)

-----

### Known Bugs (버그)

-----

### FAQ (Frequently Asked Qustions)

-----

### ToC (Table of Contents)

-----

