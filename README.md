# Instagram: la «une» de l'ère mobile

![Mosaïque de quelques-unes des images partagées par des médias francophones dans Instagram au cours de la deuxième décennie de ce siècle](images/INSTAGRAM-Illustration-18.jpg)

Ce répertoire contient les fichiers et le code dont je me suis servi pour un article publié dans [*Les Cahiers du journalisme*](http://cahiersdujournalisme.org/) en 2021. Les articles des *Cahiers* sont revus par les pairs.

### Collecte de données dans CrowdTangle

La première étape de la collecte de données à consisté à recueillir **toutes les publications Instagram** de 32 médias représentant un échantillon représentatif des principaux médias de l'espace francophone (France, Canada, Belgique, Suisse, Liban). Pour ce faire, j'ai utilisé [CrowdTangle](https://www.crowdtangle.com/), un outil de détection de contenu viral fourni par Facebook, à qui appartient Instagram. Il permet d'extraire des données historiques. Ainsi, toutes les publications Instagram de chacun des médias, dès lors qu'ils se sont mis à publier sur cette plateforme, si ces publications sont contenues dans CrowdTangle, ont été recueillies. La récolte a été effectuée début septembre 2020.

Le fichier [**mediasfrancoinstagram-public.csv**](mediasfrancoinstagram-public.csv) regroupe ainsi **82&nbsp;908 publications** mises en ligne dans Instagram par 32 médias francophones entre le 26 mai 2011 ([https://www.instagram.com/p/EwS94/](plus ancienne publication de notre échantillon)) et le 31 août 2020. Les champs `description`, `image_text` et `sponsor` ont été retranchés pour respecter la propriété intellectuelle des médias concernés. Un fichier complet pourra néanmoins être transmis à tout chercheur qui le souhaiterait (contactez-moi par [courriel](roy.jean-hugues@uqam.ca)).
