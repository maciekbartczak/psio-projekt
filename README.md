
# Motion Capture Game

Gra polega na sterowaniu rakietą oraz unikaniu asteroid. 
Za każdą unikniętą asteroidę otrzymujemy 10 punktów. 
Gra kończy się przy kolizji z asteroidą.
Rakieta jest sterowana za pomocą ruchu ręki przechwytywanego za pomocą kamery.


## Użyte technologie

Gra została napisana w Pythonie z pomocą modułu Pygame. 
Do przechwytywania ruchu dłoni użyto modułu Open-CV i Mediapipe.


## Instalacja

Tworzenie i aktywacja wirtualnego środowiska Linux

```bash
  pip install virtualenv
  cd \ścieżka\do\folderu
  virtualenv venv
  \venv\Scripts\activate.bat
```

Tworzenie i aktywacja wirtualnego środowiska Windows

```bash
  pip install virtualenv
  cd /ścieżka/do/folderu
  virtualenv venv
  source venv/bin/activate
```

Instalacja wymaganych modułów

```python
  pip install requirements.txt
```
    
## Demo

![Starting screen](https://i.ibb.co/0f1mwqL/1.png)

![Gameplay](https://i.ibb.co/TbjkvVJ/2.png)

![Ending screen](https://i.ibb.co/FnCzqhF/3.png)
