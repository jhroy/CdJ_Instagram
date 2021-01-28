# Instagram: la «une» de l'ère mobile

![Mosaïque de quelques-unes des images partagées par des médias francophones dans Instagram au cours de la deuxième décennie de ce siècle](images/INSTAGRAM-Illustration-18.jpg)

Ce répertoire contient les fichiers et le code dont je me suis servi pour un article publié dans [*Les Cahiers du journalisme*](http://cahiersdujournalisme.org/) en 2021. Les articles des *Cahiers* sont revus par les pairs.

### Collecte de données dans CrowdTangle

La première étape de la collecte de données à consisté à recueillir **toutes les publications Instagram** de 32 médias représentant un échantillon représentatif des principaux médias de l'espace francophone (France, Canada, Belgique, Suisse, Liban). Pour ce faire, j'ai utilisé [CrowdTangle](https://www.crowdtangle.com/), un outil de détection de contenu viral fourni par Facebook, à qui appartient Instagram. Il permet d'extraire des données historiques. Ainsi, toutes les publications Instagram de chacun des médias, dès lors qu'ils se sont mis à publier sur cette plateforme, si ces publications sont contenues dans CrowdTangle, ont été recueillies. La récolte a été effectuée début septembre 2020.

Le fichier [**mediasfrancoinstagram-public.csv**](mediasfrancoinstagram-public.csv) regroupe ainsi **82&nbsp;908 publications** mises en ligne dans Instagram par 32 médias francophones entre le 26 mai 2011 ([https://www.instagram.com/p/EwS94/](plus ancienne publication de notre échantillon)) et le 31 août 2020. Les champs textuels `description` et `image_text` ont été retranchés afin de respecter la propriété intellectuelle des médias concernés. Un fichier complet pourra néanmoins être transmis à tout.e chercheur.euse qui le souhaiterait (contactez-moi par [courriel](roy.jean-hugues@uqam.ca)). Ce fichier complet pourra permettre plus aisément à un.e chercheur.euse de reproduire les étapes ultérieures. Mais toute personne qui a accès à CrowdTangle pourrait puiser les publications Instagram des 32 médias francophones de notre échantillon et se créer son propre fichier, moyennant quelques heures de travail.

Le tableau ci-dessous présente la liste des médias examinés dans cette étude avec quelques métadonnées sur leurs publications.


| Compte Instagram | Pays | Abonnés (au 31 août 2020) | Nombre de publications (2011-2020) | Somme des « J’aime » | Somme des commentaires | Somme des vues |
|---|---|---|---|---|---|---|
| FRANCE 24 | France | 1 346 479 | 6 045 | 4 360 312 | 100 563 | 18 286 023 |
| Le Monde | France | 1 242 888 | 7 486 | 14 536 874 | 178 858 | 605 326 |
| Radio France Internationale | France | 476 873 | 3 247 | 852 173 | 17 509 | 1 895 300 |
| Le Figaro 🗞 | France | 439 673 | 4 834 | 4 818 443 | 96 956 | 2 298 006 |
| Mediapart | France | 364 438 | 1 828 | 2 249 459 | 66 421 | 986 458 |
| franceinfo | France | 342 512 | 2 573 | 1 694 917 | 36 465 | 7 332 685 |
| BFMTV | France | 329 388 | 1 113 | 940 386 | 32 936 | 9 213 586 |
| Libération | France | 300 364 | 2 896 | 2 575 117 | 41 349 | 1 577 385 |
| RTL | France | 162 655 | 4 516 | 862 823 | 27 351 | 703 952 |
| Radio-Canada Information | Canada | 153 190 | 6 199 | 1 253 095 | 36 502 | 7 962 640 |
| La Presse | Canada | 138 544 | 3 705 | 688 150 | 14 737 | 96 463 |
| TF1 Le JT | France | 127 721 | 1 083 | 598 876 | 12 599 | 5 819 446 |
| La Voix du Nord | France | 122 275 | 3 385 | 1 270 199 | 18 814 | 514 416 |
| TVA Nouvelles | Canada | 115 305 | 566 | 276 348 | 13 068 | 2 568 677 |
| Ouest-France | France | 111 342 | 1 545 | 1 045 061 | 13 589 | 181 895 |
| Le Devoir | Canada | 81 356 | 4 944 | 992 823 | 21 905 | 368 407 |
| RTL info | Belgique | 72 868 | 1 854 | 730 283 | 23 380 | 1 365 645 |
| LCI | France | 65 922 | 1 497 | 308 374 | 9 675 | 6 241 371 |
| SudOuest | France | 65 566 | 727 | 418 714 | 6 524 | 49 258 |
| Le Journal de Montréal | Canada | 65 011 | 632 | 99 042 | 4 070 | 157 544 |
| RTBF | Belgique | 62 720 | 1 032 | 277 775 | 7 983 | 676 828 |
| RTS - Radio Télévision Suisse | Suisse | 57 159 | 590 | 175 038 | 4 222 | 1 295 162 |
| L'Orient-Le Jour 🗞 | Liban | 45 753 | 3 546 | 979 964 | 20 008 | 1 256 818 |
| Le Soir | Belgique | 42 903 | 4 229 | 600 543 | 12 462 | 511 872 |
| Le Temps | Suisse | 42 249 | 2 040 | 301 749 | 5 037 | 10 945 |
| Tribune de Genève | Suisse | 31 110 | 1 858 | 287 051 | 5 746 | 270 169 |
| Le Dauphiné Libéré | France | 27 540 | 810 | 111 297 | 2 025 | 60 967 |
| 24heures | Suisse | 26 167 | 1 537 | 131 546 | 3 607 | 132 621 |
| Le Monde Afrique | France | 17 610 | 369 | 32 563 | 588 | 222 |
| LaLibre.be | Belgique | 16 805 | 2 024 | 102 789 | 2 224 | 164 665 |
| Le Matin | Suisse | 14 813 | 701 | 46 880 | 1 138 | 1 273 |
| Le Soleil de Québec | Canada | 13 772 | 3 491 | 597 313 | 18 196 | 20 447 |
|---|---|---|---|---|---|---|
|  |  | *6 522 971 | 82 902 | 44 215 977 | 856 507 | 72 626 472* |
