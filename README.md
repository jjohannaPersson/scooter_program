__Travis__
[![Build Status](https://app.travis-ci.com/jjohannaPersson/scooter_program.svg?branch=master)](https://app.travis-ci.com/jjohannaPersson/scooter_program)
__Scrutinizer__
[![Build Status](https://scrutinizer-ci.com/g/jjohannaPersson/scooter_program/badges/build.png?b=master)](https://scrutinizer-ci.com/g/jjohannaPersson/scooter_program/build-status/master)

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/jjohannaPersson/scooter_program/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/jjohannaPersson/scooter_program/?branch=master)

## Projekt

Detta repo är en del av ett grupparbete i kursen Pattern på Blekinge Tekniska Högskola. Projeket går ut på att skapa ett system för elsparkcyklar. Denna del är gjord för att visa att systemet fungerar med hjälp av en simulering.

## Ladda ner

Börja med att ladda ner repot från Github. Skapa sedan en config fil med din API nyckel. Om du inte gör detta så kommer inte programmet att fungera.

## Starta

Innan du startar simuleringen så behöver du först starta upp servern med kommandot:
```
sudo docker-compose up -d server
```
Sedan kan du starta simuleringen med kommandot:
```
python3 main.py
```

## Testa
För att testa koden kan du köra:
```
python3 test.py
```
För pylint för alla filer så ställer du dig i roten och kör:
```
pylint scooter_program
```
