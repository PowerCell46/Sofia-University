# Курсова задача „Цифрова обработка на аерокосмическа информация“

## Избрана Територия:
### ***Община Банско***
![Bansko Municipality Map](https://github.com/PowerCell46/Sofia-University/blob/main/Digital%20processing%20on%20aerospace%20information/images/BanskoMunicipality.png)

Избрах **община Банско**, тъй като съм добре запознат с района и той ми е изключително приятен. Посещавам го няколко пъти в годината и винаги ме впечатлява с уникалната си атмосфера и красота.

## Избрано Сателитно изображение:

- Използвана платформа: [apps.sentinel-hub.com](https://apps.sentinel-hub.com/)  
<br/>
Зададени параметри: <br/>
**Satellite**: Sentinel-2 L2A <br/>  
**Max cloud coverage**: 17% <br/>  
**Time Range**:  
  - **From**: 22-06-24  
  - **To**: 22-09-24  

![Used Platform](https://github.com/PowerCell46/Sofia-University/blob/main/Digital%20processing%20on%20aerospace%20information/images/UsedPlatform.png)

## Характеристики на избраното Сателитно изображение:
**Satellite**: Sentinel-2 L2A <br/>
**Date**: 25-08-24 <br/>
**Cloud coverage**: 1.1% <br/>

![Satellite Image](https://github.com/PowerCell46/Sofia-University/blob/main/Digital%20processing%20on%20aerospace%20information/images/SatelliteImage.png)

## Изготвена Карта № 1:
- Работата с **ArcGIS Pro** включва очертаване на границите на избраната територия и оформяне на картата с подходящо форматиране, като добавяне на заглавие, северна стрелка и мащаб за по-голяма прецизност и професионален изглед.

![Final Map 1](https://github.com/PowerCell46/Sofia-University/blob/main/Digital%20processing%20on%20aerospace%20information/images/Layout.jpg)

## Стъпки при Изготвена Карта № 2:
- Изготвяне на **контролирана пиксел базирана класификация**: <br/>
създаване на 6 класа: *Urban, Forest, Vegetation, Non-arable land, Rocks & Clouds*. <br/> 
Избиране на площи, заети от 6те класа:

![Cropped Areas](https://github.com/PowerCell46/Sofia-University/blob/main/Digital%20processing%20on%20aerospace%20information/images/croppedAreas.png)

- Работа с Image Classification Wizard

![Classified Areas](https://github.com/PowerCell46/Sofia-University/blob/main/Digital%20processing%20on%20aerospace%20information/images/classifiedAreas.png)

- Изчислена заета категория за 6те класа: <br/>
**Клас 1**: 0,20235073539524484 <br/>
**Клас 2**: 316,8260541524773 <br/>
**Клас 3**: 45,97326253159773 <br/>
**Клас 4**: 76,43506916320683 <br/>
**Клас 5**: 29,444480336365046 <br/>
**Клас 6**: 6,860808431450139 <br/>
**Total: 475,7420253504914**

![Total occupied territory](https://github.com/PowerCell46/Sofia-University/blob/main/Digital%20processing%20on%20aerospace%20information/images/totalOccupiedTeritory.png)

- **Процент точност** на класифицираните територии: <br/>
0,833333 = **83% accuracy**

![Accuracy](https://github.com/PowerCell46/Sofia-University/blob/main/Digital%20processing%20on%20aerospace%20information/images/Accuracy.png)

## Изготвена Карта № 2:
- Карта на територията на **община Банско**, с 6те класифицирани територии: *Urban, Forest, Vegetation, Non-arable land, Rocks & Clouds*. <br/>
Форматиране на картата: заглавие, легенда, северна стрелка & мащаб.

![Final Map 2](https://github.com/PowerCell46/Sofia-University/blob/main/Digital%20processing%20on%20aerospace%20information/images/FinalMap2.jpg)
