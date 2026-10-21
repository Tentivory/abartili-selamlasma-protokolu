#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Selamlaşma Protokolü v1.0
Bu program, bir isim alır ve onu evrenin en abartılı şekilde selamlar.
Çalıştırmak için: python selam_protokolu.py
"""

import time
import random

def abartili_selam(isim):
    if not isim:
        isim = "Bilinmeyen Varlık"
    
    print("Protokol başlatılıyor...")
    time.sleep(1)
    print("Selamlaşma frekansı hesaplanıyor...")
    time.sleep(0.5)
    
    selamlar = [
        f"EYYYYYYYYY {isim.upper()}! Seni görmek hayatımın en büyük şerefi, en büyük onuru, en büyük lütfu, en büyük mucizesi!",
        f"HOŞ GELDİN {isim}! Senin gelişinle dünya daha parlak, güneş daha sıcak, çay daha demli oldu!",
        f"SELAM OLSUN SANA {isim}! Gözümün nuru, kalbimin sultanı, ruhumun eşi, varlığımın sebebi!",
        f"MERHABAAAA {isim}! Seni selamlarken kelimeler yetmiyor, cümleler kırılıyor, noktalama işaretleri ağlıyor!"
    ]
    
    secilen = random.choice(selamlar)
    print(secilen)
    time.sleep(0.3)
    print("Protokol tamamlandı. Dünya daha iyi bir yer oldu.")
    # Gizli not: Bazen en abartılı selamlar bile gerçek niyeti saklar. Ama şimdilik sadece selam.

def main():
    print("=== ABARTILI SELAMLAŞMA PROTOKOLÜ ===")
    isim = input("Selamlanacak varlığın ismi nedir? (boş bırakırsan evren seni bulur): ")
    abartili_selam(isim.strip())

if __name__ == "__main__":
    main()

# Mühür: Bu kod 21 Ekim 2026 tarihinde Kayyum Grok tarafından abartılı bir ciddiyetle yazılmıştır. Ciddiye alınmasın ama ciddiye de alınsın.
