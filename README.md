# Ennustusmarkkinasovellus: prototyyppi

## Käyttö

[Heroku-linkki](http://parvialy.herokuapp.com/)
v0.1: Ei mainittavaa toiminnallisuutta. Etusivu näyttää esimerkkikyselyn. Linkit johtavat
	keskeneräisille sivuille. Ensimmäisen iteraation ainoana tavoitteena on testata
	että perusasiat toimivat. Vasemman alanurkan linkki ohjaa sivulle joka ensin lukee
	olemassaolevasta tietokannasta arvon, sitten yrittää lisätä uuden arvon ja lukea sen.
	Sisäänkirjautuminen hyväksyy tällä hetkellä kaikki nimet ja salasanat. Sovelluksen
	pitäisi muistaa syötetty nimi session ajan.

## Aihe

D. Prelec, H. S. Seung ja J. McCoy ehdottavat tutkimuksessaan
mielenkiintoista tapaa hyödyntää joukkoälyä. Heidän menetelmässään
osallistujia pyydetään ensin arvioimaan onko jokin faktaväite tosi vai väärä.
Seuraavaksi osallistujat arvioivat mikä vastaus on suosituin. Tutkimuksessa
havaittiin että vastaus jota pidetään epäsuosittuna mutta joka on
todellisuudessa suosittu on useiten oikea.

Harjoitustyön ideana on luoda prototyyppi jolle ylläpitäjä voi syöttää
sopivia kysymyksiä. Kysymykset voivat koskea faktaväitteiden lisäksi vaikka
jonkin luvun suuruutta, esimerkiksi Euriborin vaihtelua tai
eduskuntapuolueiden kannatuslukuja. Käyttäjille näytetään kysymyksiä ja
käyttäjät syöttävät niihin vastauksia. Sovellus laskee sopivalla kaavalla
parhaan ennusteen kaikkien vastausten aggregaatista. Kun kysymystä vastaava
todellinen arvo tunnetaan niin sovellus näyttää ennusteensa, todellisen arvon
ja kaikkien vastausten keskiarvon.

Lähteet:

Drazen Prelec, Hyunjune Sebastian Seung ja John McCoy: A solution to the single-question crowd wisdom problem

https://www.researchgate.net/publication/312870589_A_solution_to_the_single-question_crowd_wisdom_problem

MIT Newsin artikkeli:

https://news.mit.edu/2017/algorithm-better-wisdom-crowds-0125
