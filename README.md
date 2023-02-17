# Children-LED-light
Noční barevné světlo pro děti


<h1>Dětské LED světlo</h1>
<h2>RGB LED lampička</h2>

<p>Lampička s LED WS2812B ovládaná tlačítky a senzorem barev TCS34725. Tlačítka slouží k zapnutí/vypnutí a přepínání přednastavených režimů. Pokud je režim pro senzor barev, nastaví se taková barva, jakou má poslední přiložený předmět.</p>
<img src="img/xxx.jpg" alt="Vnitřek lampičky" width="400">

<h3>Schéma zapojení</h3>
<img src="schematic/schema.PNG" alt="Chema zapojeni" width="600">

<h3>Programy</h3>
<p><a href="childrenLight.py">childrenLight.py</a> - hlavní program</p>
<p><a href="tcs34725.py">tcs34725.py</a> - knihovna pro senzor barev TCS34725 z projektu <a href=#projekt_TCS34725>níže</a></p>
<p><a href="test_tcs34725.py">test_tcs34725.py</a> - testovací program z projektu <a href=#projekt_TCS34725>níže</a></p>
<p><a href="neopixel.py">neopixel.py</a> - knihovna pro práci s RGB LED WS2812B z projektu <a href=#projekt_NEOPIXEL>níže</a></p>


<!--
<h3>Soupis použitých komponent</h3>
<ul>
  <li>U1 - řídící jednotka - <a href="https://rpishop.cz/kontrolery/2759-m5stack-atom-lite-esp32-vyvojovy-kit.html">M5Stack ATOM Lite ESP32</a></li>
  <li>D1 až D24 - RGB LED - <a href="https://www.laskakit.cz/24x-inteligentni-rgb-led-neopixel-kruh-65--ws2812b--5050--5v/">Kruh 24x RGB LED NeoPixel Ø65, WS2812B, 5050, 5V</a></li>
  <li>U2 - ochrana Li-ion baterie - <a href="https://www.laskakit.cz/ochrana-li-ion-baterie-1s-3a/">Ochrana li-ion baterie 1S 3A</a></li>
  <li>U3 - nabíjecí modul - <a href="https://www.laskakit.cz/nabijecka-boost-pro-usb-powerbank-5v--usb-c/">Nabíječka + boost pro USB Powerbank 5V, USB-C</a></li>
  <li>SW1 - tlačítko - <a href="https://ecom.cz/eshop/detail/68498-T-0660HAC-160G">Tlačítko spínací do PS,12V/50,výška 6mm</a></li>
  <li>SW2 - spínač - <a href="https://ecom.cz/eshop/detail/70765-VP-SS12F15G6">Spínač SS12F15G6-G</a></li>
  <li>BT1 - li-ion akumulátor - např. <a href="https://www.laskakit.cz/geb-lipol-baterie-801454-580mah-3-7v-jst-ph-2-0/">GeB LiPol Baterie 801454 580mAh 3.7V JST-PH 2.0</a></li>
  <li>Propojovací vodiče - z UTP kabelu</li>
  <li>Programovací kabel - programovací kabel USB-A na USB-C</li>
</ul>

<h3>3D modely tištěných dílů a fotografie</h3>
<p>Model krabičky vychází z <a href="https://www.thingiverse.com/thing:2503641">Hexagonal LED Lamp with USB chargeable 18650 battery</a></p>
<p>3D modely pro tisk <a href="https://www.printables.com/cs/model/289219-hexagon-led-lamp">Hexagon LED lamp</a></p>
-->
<h3>Problémy a řešení</h3>
<p>Error: "Traceback (most recent call last): File "<stdin>", line 9, in <module> <B>ValueError: bad SCL pin</B>" - v řádku <code>i2c_bus = I2C(1, sda=Pin(2), scl=Pin(3))</code> je třeba správně zadat piny a pořadí I2C. Pokud je I2C0, nastaví se 0, pro I2C1 se nastaví 1.</p>
<!--
<h3>Co dál?</h3>
<p>Upravit program tak, aby v případě, že se nenaváže spojení s wi-fi, bylo možné ovládat lampičku alespoň pomocí tlačítka.</p>
<p>Doprogramovat další režimy svícení a přepínat mezi nimi v aplikaci Blynk IoT. Případně ještě přidat další tlačítko na přepínání těchto režimů.</p>
-->


<h3>Literatura</h3>
<ul>
  <li><a id="projekt_TCS34725" href="https://techtotinker.blogspot.com/2021/04/033-micropython-technotes-tcs34725-rgb.html">033 - MicroPython TechNotes: TCS34725 RGB Color Sensor</a> - projekt, kde se pracuje s TCS34725</li>
  <li><a href="https://youtu.be/VNSo75WlyCk">033 - MicroPython TechNotes: TCS34725 RGB Color Sensor</a> - video k předešlému projektu</li>
  <li><a id="projekt_NEOPIXEL" href="https://github.com/blaz-r/pi_pico_neopixel">pi_pico_neopixel</a> - projekt s ukázkou práce s raspeberry pi pico a RGB LED Neopixel</li>
</ul>
